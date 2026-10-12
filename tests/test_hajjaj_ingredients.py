"""Guard the Hajjaj family's source amounts, supplied forms and provenance scope."""

import collections
import copy
import json
import subprocess
import sys

import pytest
import review_hajjaj_ingredients as repair


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
    assert counts == {
        "new_curation_history": 20,
        "new_references": 150,
        "new_evidence": 535,
        "quantity_corrections": 37,
        "ingredient_labels_corrected": 137,
        "ingredient_identities_corrected": 90,
        "ingredient_mim_links_corrected": 54,
        "unsupported_ingredient_identity_slots_removed": 57,
        "ingredient_context_notes_corrected": 243,
    }
    assert collections.Counter(
        c["status"] for r in frozen_plan["records"] for c in r["claims"]
    ) == {
        "correct": 37,
        "unsupported": 206,
    }
    assert sum(r["primary_article_linked"] for r in frozen_plan["records"]) == 18


def test_scope_and_units_are_preserved(reviewed):
    before, after, item = reviewed
    assert dict(repair.check(before, after, item)) == item["counts"]
    for key in (
        "id",
        "name",
        "original_name",
        "category",
        "physical_state",
        "preparation_steps",
        "media_term",
        "applications",
        "target_organisms",
        "variants",
        "notes",
    ):
        assert before.get(key) == after.get(key)
    assert before["curation_history"] == after["curation_history"][:-1]
    for claim in item["claims"]:
        old = repair.runner.get_node(before, claim["pointer"])
        new = repair.runner.get_node(after, claim["pointer"])
        assert new["concentration"] == claim["new"]
        assert new["evidence"] == claim["new_evidence"]
        assert all(e["snippet"] and e["explanation"] for e in new["evidence"])
        assert len({e["reference"] for e in new["evidence"]}) == len(new["evidence"])
        if claim["status"] == "unsupported":
            assert new["concentration"] == old["concentration"]
            assert "database assertion" in new["notes"] or "MediaDB assertion" in new["notes"]
        else:
            assert new["concentration"]["unit"] == "G_PER_L"
            assert "no molecular weight or conversion arithmetic" in claim["explanation"]
    for ref in after["references"]:
        assert all(k in ref["notes"] for k in ("source_type=", "discovery_mode=", "accessed_on="))
        if ref["reference"].startswith("doi:"):
            assert ref["year"] == 2001
        elif "/media/" in ref["reference"] or "/chebi/" in ref["reference"]:
            assert "year" not in ref


def test_source_specific_identity_decisions(reviewed):
    _, after, item = reviewed
    nodes = {n["preferred_term"]: n for n in after["ingredients"]}
    moly = nodes["Ammonium heptamolybdate tetrahydrate"]
    assert "term" not in moly
    assert moly["concentration"] == {"value": "0.004045", "unit": "MILLIMOLAR"}
    assert any(e["snippet"] == "2H4N.MoO4" for e in moly["evidence"])
    if not item["primary_article_linked"]:
        assert item["key"] in {"330", "331"}
        assert not any(ref["reference"].startswith("doi:") for ref in after["references"])
        assert "Calcium chloride anhydrous" in nodes
        assert nodes["Sodium Glutamate"]["term"]["id"] == "CHEBI:64220"
        assert all(c["new"] == c["old"] for c in item["claims"])
        return
    expected = {
        "iron(2+) sulfate heptahydrate": "CHEBI:75836",
        "manganese(II) sulfate tetrahydrate": "CHEBI:86358",
        "zinc sulfate heptahydrate": "CHEBI:32312",
        "magnesium sulfate heptahydrate": "CHEBI:31795",
        "calcium chloride dihydrate": "CHEBI:86158",
    }
    for label, identifier in expected.items():
        assert nodes[label]["term"] == {"id": identifier, "label": label}
        if "mediaingredientmech_chebi_term" in nodes[label]:
            assert nodes[label]["mediaingredientmech_chebi_term"] == nodes[label]["term"]
    for label in ("copper(II) chloride dihydrate", "Sodium glutamate monohydrate", "Isoleucine"):
        if label in nodes:
            assert (
                "term" not in nodes[label] and "mediaingredientmech_chebi_term" not in nodes[label]
            )
    if item["key"] == "318":
        assert any("Figure 3" in e["explanation"] for e in nodes["Glucose"]["evidence"])


def test_equivalent_serialization_is_accepted(reviewed):
    before, after, item = reviewed
    rehash(item, after)
    assert dict(repair.check(before, after, item)) == item["counts"]


def test_every_operation_rejects_rehashed_forgery(reviewed):
    before, after, item = reviewed
    for op in repair.sources()[1][item["key"]]["operations"]:
        changed, forged = copy.deepcopy(after), copy.deepcopy(item)
        repair.runner.get_node(changed, op["pointer"][:-1])[op["pointer"][-1]] = "forged"
        rehash(forged, changed)
        with pytest.raises(AssertionError):
            repair.check(before, changed, forged)


@pytest.mark.parametrize(
    "kind", ["history", "event", "quantity", "taxon", "claim", "scope", "association", "extra"]
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
    elif kind == "association":
        item["primary_article_linked"] = not item["primary_article_linked"]
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
    assert repair.apply(plan, root) == {"changed": 20, "already_applied": 0}
    assert repair.apply(plan, root) == {"changed": 0, "already_applied": 20}
    assert repair.apply(plan, root, verify=True) == {"changed": 0, "already_applied": 20}


@pytest.mark.parametrize(
    "kind",
    [
        "drift",
        "duplicate",
        "outside",
        "case",
        "symlink",
        "source",
        "version",
        "counts",
        "verify",
        "untracked",
        "noop",
    ],
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
        last["path"] = last["path"].replace("bacterial", "BACTERIAL")
    elif kind == "source":
        plan["source_sha256"] = "0" * 64
    elif kind == "version":
        plan["version"] = 999
    elif kind == "counts":
        last["counts"]["new_evidence"] = 999
    elif kind == "untracked":
        subprocess.run(["git", "rm", "--cached", "--", last["path"]], cwd=root, check=True)
    elif kind == "noop":
        last["after_sha256"] = last["before_sha256"]
    with pytest.raises((AssertionError, ValueError)):
        repair.apply(plan, root, verify=kind == "verify")
    assert all((root / p).read_bytes() == raw for p, raw in original.items())


def test_optimized_python_cannot_disable_guards(monkeypatch):
    monkeypatch.delenv("PYTHONPATH", raising=False)
    result = subprocess.run(
        [sys.executable, "-O", "-c", "import review_hajjaj_ingredients as r; r.sources()"],
        cwd=repair.ROOT / "scripts",
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0 and "do not use -O" in result.stderr
