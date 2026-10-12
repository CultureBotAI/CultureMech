"""Guard Bristol preparation stages and BBM source-specific concentration evidence."""

import collections
import copy
import json
import subprocess
import sys

import pytest
import review_utex_bristol_bbm as repair


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
    assert sum(len(r["claims"]) for r in frozen_plan["records"]) == 40
    assert sum(len(r["extra_claims"]) for r in frozen_plan["records"]) == 5
    assert counts == {
        "new_curation_history": 5,
        "new_references": 2,
        "bibliographic_entries_enriched": 9,
        "new_evidence": 40,
        "child_link_notes_corrected": 1,
        "unsupported_quantity_slots_removed": 8,
        "variant_context_descriptions_corrected": 2,
        "variant_quantity_texts_corrected": 1,
        "stock_context_notes_corrected": 2,
        "ingredient_context_notes_corrected": 1,
        "preparation_actions_corrected": 1,
        "recipe_context_notes_corrected": 2,
        "relationship_dose_descriptions_corrected": 2,
        "stock_labels_corrected": 1,
    }
    assert collections.Counter(
        c["status"] for r in frozen_plan["records"] for c in r["claims"]
    ) == {"correct": 8, "evidence_only": 31, "conflict": 1}


def test_supported_changes_are_narrow_and_invertible(reviewed):
    before, after, item = reviewed
    assert dict(repair.check(before, after, item)) == item["counts"]
    assert before["curation_history"] == after["curation_history"][:-1]
    assert before.get("target_organisms") == after.get("target_organisms")
    assert before["id"] == after["id"]
    for claim in item["claims"]:
        old = repair.runner.get_node(before, claim["pointer"])
        new = repair.runner.get_node(after, claim["pointer"])
        assert new.get("concentration") == claim["new"]
        for key in (
            "term",
            "mediaingredientmech_chebi_term",
            "nutritional_roles",
            "physicochemical_roles",
        ):
            assert old.get(key) == new.get(key)
        if claim["new"] is None:
            assert "concentration" not in new
            assert new["notes"]
        else:
            assert old["concentration"] == new["concentration"]
    for ref in after["references"]:
        if ref["reference"].startswith("https://utex.org/"):
            assert "year" not in ref
            assert "publication year is unknown" in ref["notes"]
            assert all(
                key in ref["notes"] for key in ("source_type=", "discovery_mode=", "accessed_on=")
            )


def test_bbm_preserves_stock_boundaries_and_conflicts(frozen_plan):
    item = next(r for r in frozen_plan["records"] if r["key"] == "bold-basal-medium")
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    for old, stock in zip(before["solutions"], after["solutions"], strict=True):
        assert stock["concentration"] == {"value": "0.05", "unit": "ML_PER_L"}
        assert "approximately" in stock["notes"]
        assert "concentration" not in stock["composition"][0]
        assert [n["concentration"] for n in old["composition"][1:]] == [
            n["concentration"] for n in stock["composition"][1:]
        ]
    assert after["evidence"][0]["snippet"] == "One drop equals approximately 0.05 mL."
    acid = after["solutions"][1]["composition"][1]
    assert "do not specify acid strength" in acid["notes"]
    assert "concentrated" not in acid["notes"]
    manganese = after["solutions"][3]["composition"][3]
    assert manganese["concentration"] == {"value": "1.44", "unit": "G_PER_L"}
    assert "retained unverified" in manganese["notes"]
    assert "not this concentration" in manganese["evidence"][0]["explanation"]
    assert len(after["ingredients"]) == len(before["ingredients"]) == 7
    assert before["preparation_steps"] == after["preparation_steps"]
    variant = after["variants"][0]
    assert before["variants"][0]["evidence"] == variant["evidence"][:-1]
    assert "0.25, 0.75, 2.50, 5.0 and 15.0 ng/L" in variant["modifications"][2]
    assert "pre-experiment" in variant["modifications"][3]
    assert "4.5 ppm NH4Cl" in variant["modifications"][3]
    assert "exact equivalence" in variant["description"]
    evidence = variant["evidence"][-1]
    assert evidence["reference"] == "doi:10.3390/plants11131669"
    assert "vessel capacity, not culture volume" in evidence["explanation"]
    assert "unspecified ppm basis" in evidence["explanation"]


def test_child_preparation_stages_and_reciprocal_note(frozen_plan):
    docs = {r["key"]: repair.runner.load_yaml(r["after_text"]) for r in frozen_plan["records"]}
    child = docs["bristol-nacl-medium"]
    assert child["ingredients"][0]["concentration"] == {"value": "0.062", "unit": "MOLAR"}
    assert "concentration" not in child["solutions"][0]
    assert child["solutions"][0]["culturemech_term"]["id"] == docs["bristol-medium"]["id"]
    assert (
        child["solutions"][0]["preferred_term"] == "Bristol mineral base (before volume adjustment)"
    )
    assert child["parent_media"]["notes"] == child["variant_modifications"][0]
    assert "through step one" in docs["bristol-medium"]["variant_children"][3]["notes"]
    bot = docs["botryococcus-medium"]
    assert bot["solutions"][0]["concentration"] == {"value": "940", "unit": "ML_PER_L"}
    assert "concentration" not in bot["ingredients"][1]
    assert "final phosphate contribution, not stock strength" in bot["notes"]
    assert bot["preparation_steps"][1]["action"] == "MIX"
    proteose = docs["proteose-medium"]
    assert proteose["solutions"][0]["concentration"] == {"value": "1000", "unit": "ML_PER_L"}
    assert proteose["ingredients"][0]["concentration"] == {"value": "1", "unit": "G_PER_L"}
    assert all(doc["physical_state"] == "LIQUID" for doc in docs.values())


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
    assert repair.apply(plan, root) == {"changed": 5, "already_applied": 0}
    assert repair.apply(plan, root) == {"changed": 0, "already_applied": 5}
    assert repair.apply(plan, root, verify=True) == {"changed": 0, "already_applied": 5}


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


def test_optimized_python_cannot_disable_guards(monkeypatch):
    monkeypatch.delenv("PYTHONPATH", raising=False)
    result = subprocess.run(
        [sys.executable, "-O", "-c", "import review_utex_bristol_bbm as r; r.sources()"],
        cwd=repair.ROOT / "scripts",
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0 and "do not use -O" in result.stderr
