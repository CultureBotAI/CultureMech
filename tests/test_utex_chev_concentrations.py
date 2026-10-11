"""Claim scope, unit arithmetic and guarded writes for the UTEX CHEV cohort."""

import collections
import copy
import json
import subprocess
from decimal import Decimal

import pytest
import review_utex_chev_concentrations as repair


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


def rehash(item, doc):
    # JSON is valid YAML, so forged inputs exercise semantics independently of formatting.
    item["after_text"] = json.dumps(doc, ensure_ascii=False)
    item["after_sha256"] = repair.runner.sha(item["after_text"].encode())


def test_complete_inventory_and_totals(frozen_plan):
    counts, statuses = collections.Counter(), collections.Counter()
    for item in frozen_plan["records"]:
        counts.update(item["counts"])
        statuses.update(c["status"] for c in item["claims"])
    assert counts == {
        "new_evidence": 34,
        "new_curation_history": 9,
        "bibliographic_entries_enriched": 9,
        "quantity_corrections": 21,
        "ingredient_context_notes_corrected": 32,
    }
    assert statuses == {"correct": 21, "evidence_only": 9, "conflict": 1, "schema_gap": 3}
    _, records = repair.sources()
    assert {r["path"] for r in frozen_plan["records"]} == {r["path"] for r in records.values()}


def test_every_claim_has_narrow_source_support(reviewed):
    before, after, item = reviewed
    assert dict(repair.check(before, after, item)) == item["counts"]
    assert len(item["claims"]) == len(repair.runner.all_claims(before))
    record = repair.sources()[1][item["key"]]
    for claim in item["claims"]:
        old = repair.runner.get_node(before, claim["pointer"])
        new = repair.runner.get_node(after, claim["pointer"])
        evidence = claim["evidence"]
        assert evidence["reference"] == record["url"]
        assert evidence["snippet"] in record["table"][claim["row_index"]]
        assert evidence["supports"] == "SUPPORT"
        assert repair.runner.field_name(claim["pointer"]) in evidence["explanation"]
        assert "Locator:" in evidence["explanation"]
        if claim["status"] == "correct":
            amount, unit = record["table"][claim["row_index"]][2].split()
            assert unit in {"mL", "cc"}
            assert Decimal(new["concentration"]["value"]) == Decimal(amount) / 1000
            assert new["concentration"]["unit"] == "L"
            assert "not a per-liter concentration" in evidence["explanation"]
        elif claim["status"] in {"conflict", "schema_gap"}:
            assert new["concentration"] == old["concentration"]
            assert "notes only" in evidence["explanation"]
            expected = (
                "remains unverified" if claim["status"] == "conflict" else "remains unresolved"
            )
            assert expected in evidence["explanation"]
        owner = repair.runner.get_node(after, claim["evidence_pointer"])
        old_owner = repair.runner.get_node(before, claim["evidence_pointer"])
        assert owner["evidence"] == old_owner.get("evidence", []) + [evidence]
        if claim["pointer"][0] == "solutions":
            assert claim["evidence_pointer"] == [] and "evidence" not in new
    for key in (
        "id",
        "media_term",
        "target_organisms",
        "parent_media",
        "variant_children",
        "variant_modifications",
        "preparation_steps",
        "physical_state",
        "composition_type",
    ):
        assert before.get(key) == after.get(key)
    assert after["curation_history"][:-1] == before["curation_history"]
    bibliography = next(r for r in after["references"] if r["reference"] == record["url"])
    assert "year" not in bibliography and "authors" not in bibliography
    assert "source_type=culture_collection_page" in bibliography["notes"]
    assert "discovery_mode=existing_record_reference" in bibliography["notes"]


def test_forgery_serialization_itself_is_accepted(reviewed):
    before, after, item = reviewed
    rehash(item, after)
    assert dict(repair.check(before, after, item)) == item["counts"]


@pytest.mark.parametrize(
    "field,value", [("value", "999"), ("unit", "ML_PER_L"), ("per_volume", "per 15 mL")]
)
def test_each_quantity_rehashed_forgery_rejected(reviewed, field, value):
    before, after, item = reviewed
    for claim in item["claims"]:
        changed, forged = copy.deepcopy(after), copy.deepcopy(item)
        node = repair.runner.get_node(changed, claim["pointer"])
        node["concentration"][field] = (
            "MOLAR" if node["concentration"].get(field) == value else value
        )
        rehash(forged, changed)
        with pytest.raises(AssertionError):
            repair.check(before, changed, forged)


@pytest.mark.parametrize(
    "kind",
    [
        "identity",
        "quote",
        "reference",
        "scope",
        "notes",
        "history",
        "event",
        "title",
        "year",
        "classification",
        "relationship",
        "order",
        "claim",
        "unresolved",
        "extra_root",
    ],
)
def test_rehashed_semantic_forgery_rejected(reviewed, kind):
    before, after, item = reviewed
    claim = item["claims"][0]
    node = repair.runner.get_node(after, claim["pointer"])
    evidence = repair.runner.get_node(after, claim["evidence_pointer"])["evidence"][-1]
    if kind == "identity":
        node["term"] = {"id": "CHEBI:999999999", "label": "forged chemical"}
    elif kind in {"quote", "reference", "scope"}:
        evidence[{"quote": "snippet", "reference": "reference", "scope": "explanation"}[kind]] = (
            "forged"
        )
    elif kind == "notes":
        node["notes"] = "per liter final medium"
    elif kind == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif kind == "event":
        after["curation_history"][-1]["curator"] = "someone else"
    elif kind in {"title", "year"}:
        after["references"][1][kind] = 2026 if kind == "year" else "forged title"
    elif kind == "classification":
        after["composition_type"] = "DEFINED"
    elif kind == "relationship":
        after["parent_media"] = {"id": "CultureMech:999999"}
    elif kind == "order":
        after["ingredients"].append(copy.deepcopy(node))
    elif kind == "claim":
        claim["status"] = "verified"
    elif kind == "unresolved":
        item["unresolved"] = []
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
    # Every real before/after document gets separate schema CLI validation.
    monkeypatch.setattr(repair, "validate_recipe", lambda *a, **k: [])
    return tmp_path


def test_apply_readback_noop(plan, tmp_path, monkeypatch):
    root = make_repo(tmp_path, plan, monkeypatch)
    assert repair.apply(plan, root) == {"changed": 9, "already_applied": 0}
    assert repair.apply(plan, root) == {"changed": 0, "already_applied": 9}
    assert repair.apply(plan, root, verify=True) == {"changed": 0, "already_applied": 9}


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
    assert all((root / p).read_bytes() == raw for p, raw in original.items())
