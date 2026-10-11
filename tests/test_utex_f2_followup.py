"""Guard study-formulation scope, exact evidence and the append-only F/2 successor."""

import collections
import copy
import json
import subprocess
import sys
from decimal import Decimal

import pytest
import review_utex_f2_followup as repair


@pytest.fixture(scope="module")
def frozen_plan():
    return json.loads(repair.PLAN.read_text())


@pytest.fixture
def plan(frozen_plan):
    return copy.deepcopy(frozen_plan)


@pytest.fixture(params=sorted(repair.KEYS))
def reviewed(frozen_plan, request):
    item = copy.deepcopy(next(r for r in frozen_plan["records"] if r["key"] == request.param))
    return tuple(repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text")) + (item,)


def rehash(item, after):
    item["after_text"] = json.dumps(after, ensure_ascii=False)
    item["after_sha256"] = repair.runner.sha(item["after_text"].encode())


def test_inventory_and_counts(frozen_plan):
    counts = collections.Counter()
    for item in frozen_plan["records"]:
        counts.update(item["counts"])
    assert sum(len(r["claims"]) for r in frozen_plan["records"]) == 7
    assert counts == {
        "new_evidence": 2,
        "new_references": 2,
        "new_curation_history": 2,
        "bibliographic_entries_enriched": 2,
        "variant_evidence_snippets_added": 1,
        "variant_evidence_explanations_extended": 1,
        "variant_quantity_texts_corrected": 1,
        "relationship_dose_descriptions_corrected": 2,
        "corrected_evidence_snippets": 1,
        "root_evidence_explanations_corrected": 1,
    }


def test_supported_changes_are_narrow_and_invertible(reviewed):
    before, after, item = reviewed
    assert dict(repair.check(before, after, item)) == item["counts"]
    assert before["curation_history"] == after["curation_history"][:-1]
    assert before.get("target_organisms") == after.get("target_organisms")
    assert before["solutions"] == after["solutions"]
    assert before["preparation_steps"] == after["preparation_steps"]
    assert [c["old"] for c in repair.runner.all_claims(before)] == [
        c["old"] for c in repair.runner.all_claims(after)
    ]
    if item["key"] == "f-2-medium":
        assert before["ingredients"] == after["ingredients"]
        assert before["variants"][0]["modifications"] == after["variants"][0]["modifications"]
        assert before["variants"][0]["evidence"] == after["variants"][0]["evidence"][:-1]
        assert before["variants"][2]["evidence"] == after["variants"][2]["evidence"][:-1]
        note = after["variants"][2]["evidence"][-1]["explanation"]
        assert '"Trace elements (\u03bcM)"' in note
        assert "Trace elements (\u00b5M)" not in note
        assert "main methods were not inspected" in note
        assert "1 nM sodium selenite" in after["variants"][2]["modifications"][0]
        assert Decimal("0.001") * 1000 == Decimal("1")
        assert "nonahydrate" in after["variants"][2]["modifications"][0]
    else:
        assert "concentration" not in after["ingredients"][0]
        assert after["solutions"][0]["concentration"] == {"value": "0.175", "unit": "L"}
        assert after["parent_media"]["notes"] == after["variant_modifications"][0]
        assert "175 mL aliquot" in after["parent_media"]["notes"]
        assert "250 mL flask" in after["parent_media"]["notes"]
        assert after["ingredients"][0]["evidence"][0]["snippet"] == (
            "add a pinch of NH4MgPO4 to each flask."
        )


def test_equivalent_serialization_is_accepted(reviewed):
    before, after, item = reviewed
    rehash(item, after)
    assert dict(repair.check(before, after, item)) == item["counts"]


def test_every_operation_rejects_rehashed_forgery(reviewed):
    before, after, item = reviewed
    record = repair.sources()[1][item["key"]]
    for op in record["operations"]:
        changed, forged = copy.deepcopy(after), copy.deepcopy(item)
        if op["kind"] == "append":
            repair.runner.get_node(changed, op["pointer"])[-1]["reference"] = "forged"
        else:
            repair.runner.get_node(changed, op["pointer"][:-1])[op["pointer"][-1]] = "forged"
        rehash(forged, changed)
        with pytest.raises(AssertionError):
            repair.check(before, changed, forged)


@pytest.mark.parametrize(
    "kind", ["history", "event", "quantity", "taxon", "claim", "scope", "extra"]
)
def test_unreviewed_changes_are_rejected(reviewed, kind):
    before, after, item = reviewed
    if kind == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif kind == "event":
        after["curation_history"][-1]["curator"] = "another person"
    elif kind == "quantity":
        after["ingredients"][0]["concentration"] = {"value": "999", "unit": "G_PER_L"}
    elif kind == "taxon":
        after.setdefault("target_organisms", []).append({"preferred_term": "invented"})
    elif kind == "claim":
        item["claims"][0]["status"] = "verified"
    elif kind == "scope":
        item["unresolved"] = []
    else:
        after["unreviewed"] = True
    rehash(item, after)
    with pytest.raises(AssertionError):
        repair.check(before, after, item)


def make_repo(tmp_path, plan, monkeypatch):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    for item in plan["records"]:
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    subprocess.run(["git", "add", "data"], cwd=tmp_path, check=True)
    monkeypatch.setattr(repair, "validate_recipe", lambda *a, **k: [])
    return tmp_path


def test_apply_readback_and_noop(plan, tmp_path, monkeypatch):
    root = make_repo(tmp_path, plan, monkeypatch)
    assert repair.apply(plan, root) == {"changed": 2, "already_applied": 0}
    assert repair.apply(plan, root) == {"changed": 0, "already_applied": 2}
    assert repair.apply(plan, root, verify=True) == {"changed": 0, "already_applied": 2}


@pytest.mark.parametrize(
    "kind",
    ["drift", "duplicate", "outside", "case", "symlink", "source", "version", "counts", "verify"],
)
def test_failed_preflight_changes_nothing(plan, tmp_path, monkeypatch, kind):
    root = make_repo(tmp_path, plan, monkeypatch)
    last = plan["records"][-1]
    path = root / last["path"]
    if kind == "drift":
        path.write_bytes(path.read_bytes() + b"\n# concurrent edit\n")
    elif kind == "symlink":
        destination = root / "saved.yaml"
        path.rename(destination)
        path.symlink_to(destination)
    original = {r["path"]: (root / r["path"]).read_bytes() for r in plan["records"]}
    if kind == "duplicate":
        plan["records"][-1] = copy.deepcopy(plan["records"][0])
    elif kind == "outside":
        last["path"] = "../../outside.yaml"
    elif kind == "case":
        last["path"] = last["path"].replace("algae", "ALGAE")
    elif kind == "source":
        plan["source_sha256"] = "0" * 64
    elif kind == "version":
        plan["version"] = 999
    elif kind == "counts":
        last["counts"]["new_evidence"] = 999
    with pytest.raises((AssertionError, ValueError)):
        repair.apply(plan, root, verify=kind == "verify")
    assert all((root / p).read_bytes() == raw for p, raw in original.items())


def test_optimized_python_cannot_disable_guards():
    result = subprocess.run(
        [sys.executable, "-O", "-c", "import review_utex_f2_followup as r; r.sources()"],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0 and "do not use -O" in result.stderr
