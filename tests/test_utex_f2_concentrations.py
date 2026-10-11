"""Guard F/2 source scope, chemical forms, omitted amounts and no-op application."""

import collections
import copy
import json
import subprocess

import pytest
import review_utex_f2_concentrations as repair


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


def test_inventory_and_totals(frozen_plan):
    counts = collections.Counter()
    for item in frozen_plan["records"]:
        counts.update(item["counts"])
    assert sum(len(r["claims"]) for r in frozen_plan["records"]) == 105
    assert counts == {
        "new_evidence": 110,
        "new_curation_history": 5,
        "new_references": 17,
        "bibliographic_entries_enriched": 21,
        "unsupported_quantity_slots_removed": 21,
        "quantity_corrections": 1,
        "ingredient_context_notes_corrected": 66,
        "ingredient_identities_corrected": 12,
        "ingredient_labels_corrected": 12,
        "preparation_actions_corrected": 1,
        "preparation_descriptions_corrected": 1,
        "child_link_notes_corrected": 1,
    }


def test_every_claim_is_accounted_and_scoped(reviewed):
    before, after, item = reviewed
    source, records = repair.sources()
    record = records[item["key"]]
    assert dict(repair.check(before, after, item)) == item["counts"]
    assert [c["pointer"] for c in item["claims"]] == [
        c["pointer"] for c in repair.runner.all_claims(before)
    ]
    for claim in item["claims"]:
        node = repair.runner.get_node(after, claim["pointer"])
        assert node.get("concentration") == claim["new"]
        assert claim["snippet"] in source["sources"][claim["reference"]]["text"]
        if claim["new"] is None:
            assert "concentration" not in node and node["notes"]
        if claim["identity_corrected"]:
            decision = repair.resolve_ingredient(node)
            assert decision.identifier == decision.ontology_id == claim["identity_corrected"]
    for pointer, entries in repair.evidence_by_owner(record).items():
        owner = repair.runner.get_node(after, pointer)
        assert (
            owner["evidence"]
            == repair.runner.get_node(before, pointer).get("evidence", []) + entries
        )
        assert len({e["reference"] for e in owner["evidence"]}) == len(owner["evidence"])
    for node in after["solutions"]:
        assert "evidence" not in node
    for field in (
        "id",
        "name",
        "target_organisms",
        "variants",
        "parent_media",
        "physical_state",
        "composition_type",
    ):
        assert before.get(field) == after.get(field)
    assert before["curation_history"] == after["curation_history"][:-1]


def test_json_yaml_equivalence_is_accepted(reviewed):
    before, after, item = reviewed
    rehash(item, after)
    assert dict(repair.check(before, after, item)) == item["counts"]


@pytest.mark.parametrize(
    "field,value", [("value", "999"), ("unit", "MOLAR"), ("per_volume", "per 250 mL")]
)
def test_all_105_quantity_fields_reject_rehashed_forgery(reviewed, field, value):
    before, after, item = reviewed
    for claim in item["claims"]:
        forged, changed = copy.deepcopy(item), copy.deepcopy(after)
        node = repair.runner.get_node(changed, claim["pointer"])
        node.setdefault("concentration", {"value": "1000", "unit": "ML_PER_L"})[field] = value
        rehash(forged, changed)
        with pytest.raises(AssertionError):
            repair.check(before, changed, forged)


@pytest.mark.parametrize("field", ["snippet", "reference", "supports", "explanation"])
def test_every_new_evidence_entry_rejects_rehashed_forgery(reviewed, field):
    before, after, item = reviewed
    record = repair.sources()[1][item["key"]]
    for pointer, entries in repair.evidence_by_owner(record).items():
        offset = len(repair.runner.get_node(before, pointer).get("evidence", []))
        for index in range(len(entries)):
            forged, changed = copy.deepcopy(item), copy.deepcopy(after)
            repair.runner.get_node(changed, pointer)["evidence"][offset + index][field] = "forged"
            rehash(forged, changed)
            with pytest.raises(AssertionError):
                repair.check(before, changed, forged)


@pytest.mark.parametrize(
    "kind",
    [
        "identity",
        "notes",
        "history",
        "event",
        "title",
        "year",
        "relationship",
        "order",
        "claim",
        "unresolved",
        "extra_root",
        "new_taxon",
    ],
)
def test_other_rehashed_forgery_rejected(reviewed, kind):
    before, after, item = reviewed
    node = after["ingredients"][0]
    if kind == "identity":
        node["term"] = {"id": "CHEBI:999999", "label": "forged"}
    elif kind == "notes":
        node["notes"] = "one liter of solvent"
    elif kind == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif kind == "event":
        after["curation_history"][-1]["curator"] = "someone else"
    elif kind in {"title", "year"}:
        after["references"][1][kind] = 2026 if kind == "year" else "forged"
    elif kind == "relationship":
        after["parent_media"] = {"id": "CultureMech:999999"}
    elif kind == "order":
        after["ingredients"].append(copy.deepcopy(node))
    elif kind == "claim":
        item["claims"][0]["status"] = "verified"
    elif kind == "unresolved":
        item["unresolved"] = []
    elif kind == "new_taxon":
        after.setdefault("target_organisms", []).append({"preferred_term": "invented"})
    else:
        after["invented"] = True
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
    # Real baseline/proposed documents are separately schema-validated.
    monkeypatch.setattr(repair, "validate_recipe", lambda *a, **k: [])
    return tmp_path


def test_apply_readback_and_noop(plan, tmp_path, monkeypatch):
    root = make_repo(tmp_path, plan, monkeypatch)
    assert repair.apply(plan, root) == {"changed": 5, "already_applied": 0}
    assert repair.apply(plan, root) == {"changed": 0, "already_applied": 5}
    assert repair.apply(plan, root, verify=True) == {"changed": 0, "already_applied": 5}


@pytest.mark.parametrize(
    "kind",
    [
        "late_drift",
        "duplicate",
        "outside",
        "symlink",
        "source",
        "version",
        "case",
        "counts",
        "verify_before_apply",
    ],
)
def test_failed_preflight_writes_nothing(plan, tmp_path, monkeypatch, kind):
    root = make_repo(tmp_path, plan, monkeypatch)
    original = {r["path"]: (root / r["path"]).read_bytes() for r in plan["records"]}
    last = plan["records"][-1]
    if kind == "late_drift":
        target = root / last["path"]
        target.write_bytes(target.read_bytes() + b"\n# concurrent edit\n")
        original[last["path"]] = target.read_bytes()
    elif kind == "duplicate":
        plan["records"][-1] = copy.deepcopy(plan["records"][0])
    elif kind == "outside":
        last["path"] = "../../outside.yaml"
    elif kind == "symlink":
        target = root / last["path"]
        saved = root / "elsewhere.yaml"
        target.rename(saved)
        target.symlink_to(saved)
    elif kind == "source":
        plan["source_sha256"] = "0" * 64
    elif kind == "version":
        plan["version"] = 999
    elif kind == "case":
        last["path"] = last["path"].replace("algae", "ALGAE")
    elif kind == "counts":
        last["counts"]["new_evidence"] = 999
    with pytest.raises((AssertionError, ValueError)):
        repair.apply(plan, root, verify=kind == "verify_before_apply")
    assert all((root / path).read_bytes() == raw for path, raw in original.items())
