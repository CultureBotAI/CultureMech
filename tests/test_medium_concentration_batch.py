"""Offline cohort consistency; live/cached source retrieval is a separate check."""

import copy
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from decimal import Decimal
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports/ingredient_concentration_curation"
BATCHES = sorted(REPORTS.glob("20261007-mediadive-media-*-*/plan.json"))
sys.path.insert(0, str(ROOT / "scripts"))
from review_solution_concentration_evidence import (  # noqa: E402
    followup_chain,
    followup_result_hash,
)

SPEC = importlib.util.spec_from_file_location(
    "batch_provenance_audit", REPORTS / "20261007-dsmz1399-stock-boundary/audit_diff.py"
)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)
FOLLOWUPS = AUDIT.review_plans()


def assert_current_record_and_count_original(item, successors, monkeypatch):
    raw = (ROOT / item["path"]).read_bytes()
    expected, _ = followup_result_hash(item, successors)
    assert hashlib.sha256(raw).hexdigest() == expected
    chain = followup_chain(item, successors)
    if chain:
        # Audit later changes independently without charging them to this batch.
        with monkeypatch.context() as patch:
            patch.setattr(AUDIT, "counts", Counter())
            assert AUDIT.invert_chain(raw, chain) == yaml.safe_load(item["after_text"])
    assert AUDIT.invert_chain(item["after_text"].encode(), [item]) == yaml.safe_load(
        item["before_text"]
    )


@pytest.mark.parametrize("plan_path", BATCHES, ids=lambda path: path.parent.name)
def test_medium_batch_hashes_claims_reports_and_provenance(plan_path):
    plan = json.loads(plan_path.read_text())
    assert plan["target_class"] == "MediaRecipe"
    start, stop = map(int, plan_path.parent.name.rsplit("-", 2)[1:])
    inventory = json.loads((REPORTS / "20261007-medium-source-inventory.json").read_text())
    assert len(plan["records"]) == stop - start
    statuses = Counter()
    changed = 0
    successors = [r for path in FOLLOWUPS for r in json.loads(path.read_text())["records"]]
    for item, original in zip(plan["records"], inventory["records"][start:stop], strict=True):
        for key in ("path", "id", "medium_id", "name", "before_sha256"):
            assert item[key] == original[key]
        assert not item["failure"] and not item["baseline_errors"] and not item["post_errors"]
        raw = (ROOT / item["path"]).read_bytes()
        expected, _ = followup_result_hash(item, successors)
        assert hashlib.sha256(raw).hexdigest() == expected
        doc = yaml.load(raw, Loader=yaml.CSafeLoader)
        assert doc["id"] == item["id"]
        # Independently audit each repair, then check the original claims at their
        # original scope. Later stock moves/withdrawals are not hash exemptions.
        chain = followup_chain(item, successors)
        historical = AUDIT.invert_chain(raw, chain) if chain else doc
        relative = item["path"].removeprefix("data/normalized_yaml/")
        lines = (plan_path.parent / "records" / (relative + ".md")).read_text().splitlines()
        assert [line for line in lines if line.startswith("- Record:")] == [
            f"- Record: {item['path']}"
        ]
        assert not any(line.startswith("- State: preview") for line in lines)
        assert sum(line.startswith("| `") for line in lines) == len(item["claims"])
        has_changes = item["before_sha256"] != item["after_sha256"]
        changed += has_changes
        accepted = [c for c in item["claims"] if c["status"] in {"add", "correct", "evidence_only"}]
        assert bool(accepted) == has_changes
        if has_changes:
            events = [
                e
                for e in doc["curation_history"]
                if e["action"] == "CURATED_MEDIUM_CONCENTRATION_SOURCE_EVIDENCE"
                and e["timestamp"] == plan["created_at"]
            ]
            assert len(events) == 1 and events[0]["curator"] == "codex"
        for claim in item["claims"]:
            statuses[claim["status"]] += 1
            if claim["pointer"] is None:
                assert claim["new"] is None
                continue
            node = historical
            for key in claim["pointer"]:
                node = node[key]
            if claim not in accepted:
                assert node.get("concentration") == claim["old"]
                continue
            assert claim["pointer"][0] == "ingredients" and len(claim["pointer"]) == 2
            assert (
                claim["reference"] == f"https://mediadive.dsmz.de/rest/medium/{item['medium_id']}"
            )
            assert node["concentration"] == claim["new"] == claim["old"]
            row = json.loads(claim["snippet"])
            assert row["compound"] == node["preferred_term"]
            assert (
                row["optional"] == 0 and not row.get("attribute") and row.get("solution_id") is None
            )
            if row.get("condition"):
                assert (
                    row["condition"] == "for solid medium" and doc["physical_state"] == "SOLID_AGAR"
                )
            assert Decimal(claim["new"]["value"]) == Decimal(str(row["g_l"]))
            assert claim["new"]["unit"] == "G_PER_L"
            entries = [e for e in node["evidence"] if e["reference"] == claim["reference"]]
            assert len(entries) == 1 and entries[0]["snippet"] == claim["snippet"]
            assert entries[0]["supports"] == "SUPPORT"
            assert claim["field"] in entries[0]["explanation"]
            assert item["source_sha256"] in entries[0]["explanation"]
            refs = [r for r in historical["references"] if r["reference"] == claim["reference"]]
            assert len(refs) == 1 and item["source_sha256"] in refs[0]["notes"]
    summary = json.loads((plan_path.parent / "records/summary.json").read_text())
    assert statuses == summary["claims"]
    assert changed == summary["proposed_changed"]


def test_medium_inventory_slices_are_contiguous_and_unique():
    assert BATCHES
    end = 0
    paths = set()
    for path in BATCHES:
        start, stop = map(int, path.parent.name.rsplit("-", 2)[1:])
        assert start == end and stop > start
        items = json.loads(path.read_text())["records"]
        targets = {r["path"] for r in items}
        assert len(targets) == len(items) and not targets.intersection(paths)
        paths.update(targets)
        end = stop


@pytest.mark.parametrize("mutation", ["ingredient", "history"])
def test_rehashing_an_unreviewed_successor_does_not_bypass_source_audit(mutation):
    item = copy.deepcopy(
        next(r for r in json.loads(AUDIT.J261_PLAN.read_text())["records"] if r["key"] == "J151")
    )
    forged = yaml.safe_load(item["after_text"])
    if mutation == "ingredient":
        forged["ingredients"][0]["preferred_term"] = "Deliberately wrong test ingredient"
    else:
        forged["curation_history"][0]["notes"] = "Overwritten earlier history"
    item["after_text"] = yaml.safe_dump(forged)
    raw = item["after_text"].encode()
    item["after_sha256"] = hashlib.sha256(raw).hexdigest()
    with pytest.raises(AssertionError):
        AUDIT.invert_chain(raw, [item])


def test_medium829_registry_uses_only_applied_successor():
    current = REPORTS / "20261009-desulfurobacterium-family/plan-v2.json"
    assert FOLLOWUPS.count(current) == 1
    assert current.with_name("plan.json") not in FOLLOWUPS
    receipt = json.loads(current.with_name("apply.json").read_text())
    assert receipt["terminal"] and not receipt.get("error")
    assert receipt["plan_sha256"] == hashlib.sha256(current.read_bytes()).hexdigest()
    assert receipt["only_reviewed_records_changed"]


@pytest.mark.parametrize("mutation", [None, "quantity", "evidence", "history"])
def test_medium829_registry_independently_checks_rehashed_successor(mutation, monkeypatch):
    item = copy.deepcopy(
        next(
            r
            for r in json.loads(AUDIT.DESULFUROBACTERIUM_PLAN.read_text())["records"]
            if r["key"] == "K829"
        )
    )
    current = yaml.safe_load(item["after_text"])
    if mutation == "quantity":
        current["ingredients"][0]["concentration"]["value"] = "9999"
    elif mutation == "evidence":
        current["ingredients"][0]["evidence"][-1]["snippet"] = "Unsupported test quote"
    elif mutation == "history":
        current["curation_history"][0]["notes"] = "Overwritten historical event"
    item["after_text"] = yaml.safe_dump(current)
    raw = item["after_text"].encode()
    item["after_sha256"] = hashlib.sha256(raw).hexdigest()
    monkeypatch.setattr(AUDIT, "counts", Counter())
    if mutation:
        with pytest.raises(AssertionError):
            AUDIT.invert_chain(raw, [item])
    else:
        assert AUDIT.invert_chain(raw, [item]) == yaml.safe_load(item["before_text"])
        assert set(AUDIT.counts) == {"new_evidence", "new_references", "new_curation_history"}
        assert AUDIT.counts["new_curation_history"] == 1


def test_oteb_registry_uses_applied_plan_and_counts_only_provenance(monkeypatch):
    current = REPORTS / "20261009-oteb-family/plan.json"
    assert FOLLOWUPS.count(current) == 1
    receipt = json.loads(current.with_name("apply.json").read_text())
    assert receipt["terminal"] and not receipt.get("error")
    assert receipt["plan_sha256"] == hashlib.sha256(current.read_bytes()).hexdigest()
    assert receipt["only_reviewed_records_changed"]
    monkeypatch.setattr(AUDIT, "counts", Counter())
    for item in json.loads(current.read_text())["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        assert AUDIT.invert_chain(raw, [item]) == yaml.safe_load(item["before_text"])
    assert AUDIT.counts == {
        "new_evidence": 154,
        "new_references": 9,
        "new_curation_history": 6,
    }


def test_halobacteria_registry_uses_applied_plan_and_counts_only_new_provenance(monkeypatch):
    current = REPORTS / "20261009-halobacteria-family/applied-plan.json"
    assert FOLLOWUPS.count(current) == 1
    applied = json.loads(current.read_text())
    proposal = current.with_name("plan-v2.json")
    receipt = json.loads(current.with_name("apply.json").read_text())
    assert receipt["terminal"] and not receipt["errors"]
    assert receipt["only_reviewed_records_changed"]
    assert receipt["applied_plan_sha256"] == hashlib.sha256(current.read_bytes()).hexdigest()
    assert applied["source_plan_sha256"] == hashlib.sha256(proposal.read_bytes()).hexdigest()
    assert applied["records"] == json.loads(proposal.read_text())["records"]
    assert len(applied["records"]) == 5
    monkeypatch.setattr(AUDIT, "counts", Counter())
    successors = json.loads(AUDIT.HALOBACTERIA_VARIANTS_PLAN.read_text())["records"]
    for item in applied["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        expected, _ = followup_result_hash(item, successors)
        assert hashlib.sha256(raw).hexdigest() == expected
        chain = followup_chain(item, successors)
        if chain:
            prior_counts = AUDIT.counts.copy()
            assert AUDIT.invert_chain(raw, chain) == yaml.safe_load(item["after_text"])
            AUDIT.counts.clear()
            AUDIT.counts.update(prior_counts)
        assert AUDIT.invert_chain(item["after_text"].encode(), [item]) == yaml.safe_load(
            item["before_text"]
        )
    assert AUDIT.counts == {"new_evidence": 94, "new_references": 11, "new_curation_history": 5}


def test_halobacteria_variant_registry_counts_only_applied_provenance(monkeypatch):
    current = AUDIT.HALOBACTERIA_VARIANTS_PLAN
    assert FOLLOWUPS.count(current) == 1
    assert current.with_name("plan.json") not in FOLLOWUPS
    assert current.with_name("plan-v2.json") not in FOLLOWUPS
    applied = json.loads(current.read_text())
    receipt = json.loads(current.with_name("apply.json").read_text())
    assert receipt["terminal"] and not receipt["errors"]
    assert receipt["only_reviewed_records_changed"]
    assert receipt["applied_plan_sha256"] == hashlib.sha256(current.read_bytes()).hexdigest()
    assert (
        applied["source_plan_sha256"]
        == hashlib.sha256(current.with_name("plan-v2.json").read_bytes()).hexdigest()
    )
    assert len(applied["records"]) == 16
    monkeypatch.setattr(AUDIT, "counts", Counter())
    for item in applied["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        assert AUDIT.invert_chain(raw, [item]) == yaml.safe_load(item["before_text"])
    assert AUDIT.counts == {"new_evidence": 335, "new_references": 45, "new_curation_history": 16}


@pytest.mark.parametrize("key", ["J1132", "M1212", "S3823", "J168", "M159", "M160"])
@pytest.mark.parametrize("mutation", ["quantity", "evidence", "history"])
def test_halobacteria_variant_registry_rejects_rehashed_mutations(key, mutation, monkeypatch):
    item = copy.deepcopy(
        next(
            r
            for r in json.loads(AUDIT.HALOBACTERIA_VARIANTS_PLAN.read_text())["records"]
            if r["key"] == key
        )
    )
    doc = yaml.safe_load(item["after_text"])
    nodes = (
        doc["solutions"][0]["composition"]
        if key in {"J1132", "M1212"}
        else doc["composition"] if key == "S3823" else doc["ingredients"]
    )
    if mutation == "quantity":
        nodes[0]["concentration"] = {"value": "9999", "unit": "G_PER_L"}
    elif mutation == "evidence":
        nodes[0]["evidence"][0]["snippet"] = "Unsupported test quote"
    else:
        doc["curation_history"][0]["notes"] = "Overwritten historical event"
    item["after_text"] = yaml.safe_dump(doc)
    raw = item["after_text"].encode()
    item["after_sha256"] = hashlib.sha256(raw).hexdigest()
    monkeypatch.setattr(AUDIT, "counts", Counter())
    with pytest.raises(AssertionError):
        AUDIT.invert_chain(raw, [item])


@pytest.mark.parametrize("key", ["J168", "J1007", "M159", "M160", "M1064"])
@pytest.mark.parametrize("mutation", ["quantity", "evidence", "history"])
def test_halobacteria_registry_rejects_rehashed_source_mutations(key, mutation, monkeypatch):
    item = copy.deepcopy(
        next(
            r for r in json.loads(AUDIT.HALOBACTERIA_PLAN.read_text())["records"] if r["key"] == key
        )
    )
    current = yaml.safe_load(item["after_text"])
    if mutation == "quantity":
        current["ingredients"][0]["concentration"] = {"value": "9999", "unit": "G_PER_L"}
    elif mutation == "evidence":
        current["ingredients"][0]["evidence"][0]["snippet"] = "Unsupported test quote"
    else:
        current["curation_history"][0]["notes"] = "Overwritten historical event"
    item["after_text"] = yaml.safe_dump(current)
    raw = item["after_text"].encode()
    item["after_sha256"] = hashlib.sha256(raw).hexdigest()
    monkeypatch.setattr(AUDIT, "counts", Counter())
    with pytest.raises(AssertionError):
        AUDIT.invert_chain(raw, [item])


def test_synthrophomonas_registry_counts_only_applied_changes_and_new_provenance(monkeypatch):
    current = REPORTS / "20261009-synthrophomonas-family/applied-plan.json"
    assert FOLLOWUPS.count(current) == 1
    applied = json.loads(current.read_text())
    proposal = current.with_name("plan-v2.json")
    receipt = json.loads(current.with_name("apply.json").read_text())
    assert receipt["terminal"] and not receipt["errors"]
    assert receipt["only_reviewed_records_changed"]
    assert receipt["applied_plan_sha256"] == hashlib.sha256(current.read_bytes()).hexdigest()
    assert applied["source_plan_sha256"] == hashlib.sha256(proposal.read_bytes()).hexdigest()
    assert applied["records"] == [
        item
        for item in json.loads(proposal.read_text())["records"]
        if item["before_sha256"] != item["after_sha256"]
    ]
    assert len(applied["records"]) == 21 and applied["unchanged_reviewed_keys"] == ["S608"]
    monkeypatch.setattr(AUDIT, "counts", Counter())
    successors = [r for path in FOLLOWUPS for r in json.loads(path.read_text())["records"]]
    for item in applied["records"]:
        assert_current_record_and_count_original(item, successors, monkeypatch)
    assert AUDIT.counts == {"new_evidence": 186, "new_references": 6, "new_curation_history": 21}


@pytest.mark.parametrize("key", ["K212", "D212", "B2805", "S595"])
@pytest.mark.parametrize("mutation", ["quantity", "evidence", "history"])
def test_synthrophomonas_registry_rejects_rehashed_source_mutations(key, mutation, monkeypatch):
    item = copy.deepcopy(
        next(
            r
            for r in json.loads(AUDIT.SYNTHROPHOMONAS_PLAN.read_text())["records"]
            if r["key"] == key
        )
    )
    current = yaml.safe_load(item["after_text"])
    if mutation == "quantity":
        node = current
        for part in item["lineage"][0]["pointer"]:
            node = node[part]
        node["concentration"] = {"value": "9999", "unit": "G_PER_L"}
    elif mutation == "evidence":
        container = current["composition"][0] if key.startswith("S") else current
        container["evidence"][0]["snippet"] = "Unsupported test quote"
    else:
        current["curation_history"][0]["notes"] = "Overwritten historical event"
    item["after_text"] = yaml.safe_dump(current)
    raw = item["after_text"].encode()
    item["after_sha256"] = hashlib.sha256(raw).hexdigest()
    monkeypatch.setattr(AUDIT, "counts", Counter())
    with pytest.raises(AssertionError):
        AUDIT.invert_chain(raw, [item])


def test_methanofollis_registry_uses_applied_plan_and_counts_only_new_provenance(monkeypatch):
    current = REPORTS / "20261009-methanofollis-family/plan.json"
    assert FOLLOWUPS.count(current) == 1
    receipt = json.loads(current.with_name("apply.json").read_text())
    assert receipt["terminal"] and not receipt.get("error")
    assert receipt["plan_sha256"] == hashlib.sha256(current.read_bytes()).hexdigest()
    assert receipt["only_reviewed_records_changed"]
    monkeypatch.setattr(AUDIT, "counts", Counter())
    successors = [r for path in FOLLOWUPS for r in json.loads(path.read_text())["records"]]
    for item in json.loads(current.read_text())["records"]:
        assert_current_record_and_count_original(item, successors, monkeypatch)
    assert AUDIT.counts == {"new_evidence": 118, "new_references": 6, "new_curation_history": 6}


@pytest.mark.parametrize("mutation", [None, "quantity", "evidence", "history"])
def test_methanofollis_registry_rejects_rehashed_source_mutations(mutation, monkeypatch):
    item = copy.deepcopy(
        next(
            r
            for r in json.loads(AUDIT.METHANOFOLLIS_PLAN.read_text())["records"]
            if r["key"] == "K161"
        )
    )
    current = yaml.safe_load(item["after_text"])
    if mutation == "quantity":
        current["ingredients"][0]["concentration"]["value"] = "9999"
    elif mutation == "evidence":
        current["ingredients"][0]["evidence"][0]["snippet"] = "Unsupported test quote"
    elif mutation == "history":
        current["curation_history"][0]["notes"] = "Overwritten historical event"
    item["after_text"] = yaml.safe_dump(current)
    raw = item["after_text"].encode()
    item["after_sha256"] = hashlib.sha256(raw).hexdigest()
    monkeypatch.setattr(AUDIT, "counts", Counter())
    if mutation:
        with pytest.raises(AssertionError):
            AUDIT.invert_chain(raw, [item])
    else:
        assert AUDIT.invert_chain(raw, [item]) == yaml.safe_load(item["before_text"])
        assert AUDIT.counts == {"new_evidence": 46, "new_references": 2, "new_curation_history": 1}


def test_rumen_registry_uses_applied_plan_and_counts_only_new_provenance(monkeypatch):
    current = REPORTS / "20261009-rumen-bacteria-family/plan.json"
    assert FOLLOWUPS.count(current) == 1
    receipt = json.loads(current.with_name("apply.json").read_text())
    assert receipt["terminal"] and not receipt.get("error")
    assert receipt["plan_sha256"] == hashlib.sha256(current.read_bytes()).hexdigest()
    assert receipt["only_reviewed_records_changed"]
    monkeypatch.setattr(AUDIT, "counts", Counter())
    for item in json.loads(current.read_text())["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        assert AUDIT.invert_chain(raw, [item]) == yaml.safe_load(item["before_text"])
    assert AUDIT.counts == {"new_evidence": 214, "new_references": 15, "new_curation_history": 13}


@pytest.mark.parametrize("mutation", [None, "quantity", "evidence", "history"])
def test_rumen_registry_rejects_rehashed_source_mutations(mutation, monkeypatch):
    item = copy.deepcopy(
        next(r for r in json.loads(AUDIT.RUMEN_PLAN.read_text())["records"] if r["key"] == "K330")
    )
    current = yaml.safe_load(item["after_text"])
    if mutation == "quantity":
        current["ingredients"][0]["concentration"]["value"] = "9999"
    elif mutation == "evidence":
        current["ingredients"][0]["evidence"][0]["snippet"] = "Unsupported test quote"
    elif mutation == "history":
        current["curation_history"][0]["notes"] = "Overwritten historical event"
    item["after_text"] = yaml.safe_dump(current)
    raw = item["after_text"].encode()
    item["after_sha256"] = hashlib.sha256(raw).hexdigest()
    monkeypatch.setattr(AUDIT, "counts", Counter())
    if mutation:
        with pytest.raises(AssertionError):
            AUDIT.invert_chain(raw, [item])
    else:
        assert AUDIT.invert_chain(raw, [item]) == yaml.safe_load(item["before_text"])
        assert AUDIT.counts == {"new_evidence": 30, "new_references": 2, "new_curation_history": 1}


def test_ruminococcus_registry_uses_applied_plan_and_counts_only_new_provenance(monkeypatch):
    current = REPORTS / "20261009-ruminococcus-albus-family/plan.json"
    assert FOLLOWUPS.count(current) == 1
    receipt = json.loads(current.with_name("apply.json").read_text())
    assert receipt["terminal"] and not receipt.get("error")
    assert receipt["plan_sha256"] == hashlib.sha256(current.read_bytes()).hexdigest()
    assert receipt["only_reviewed_records_changed"]
    monkeypatch.setattr(AUDIT, "counts", Counter())
    for item in json.loads(current.read_text())["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        assert AUDIT.invert_chain(raw, [item]) == yaml.safe_load(item["before_text"])
    assert AUDIT.counts == {"new_evidence": 155, "new_references": 16, "new_curation_history": 10}


@pytest.mark.parametrize("mutation", [None, "quantity", "evidence", "history"])
def test_ruminococcus_registry_rejects_rehashed_source_mutations(mutation, monkeypatch):
    item = copy.deepcopy(
        next(
            r
            for r in json.loads(AUDIT.RUMINOCOCCUS_PLAN.read_text())["records"]
            if r["key"] == "K436"
        )
    )
    current = yaml.safe_load(item["after_text"])
    if mutation == "quantity":
        current["ingredients"][0]["concentration"]["value"] = "9999"
    elif mutation == "evidence":
        current["ingredients"][0]["evidence"][0]["snippet"] = "Unsupported test quote"
    elif mutation == "history":
        current["curation_history"][0]["notes"] = "Overwritten historical event"
    item["after_text"] = yaml.safe_dump(current)
    raw = item["after_text"].encode()
    item["after_sha256"] = hashlib.sha256(raw).hexdigest()
    monkeypatch.setattr(AUDIT, "counts", Counter())
    if mutation:
        with pytest.raises(AssertionError):
            AUDIT.invert_chain(raw, [item])
    else:
        assert AUDIT.invert_chain(raw, [item]) == yaml.safe_load(item["before_text"])
        assert AUDIT.counts == {"new_evidence": 22, "new_references": 2, "new_curation_history": 1}


@pytest.mark.parametrize("mutation", [None, "quantity", "evidence", "history"])
def test_oteb_registry_independently_checks_rehashed_successor(mutation, monkeypatch):
    item = copy.deepcopy(
        next(r for r in json.loads(AUDIT.OTEB_PLAN.read_text())["records"] if r["key"] == "K1245")
    )
    current = yaml.safe_load(item["after_text"])
    quantified = next(node for node in current["ingredients"] if "concentration" in node)
    if mutation == "quantity":
        quantified["concentration"]["value"] = "9999"
    elif mutation == "evidence":
        current["ingredients"][0]["evidence"][-1]["snippet"] = "Unsupported test quote"
    elif mutation == "history":
        current["curation_history"][0]["notes"] = "Overwritten historical event"
    item["after_text"] = yaml.safe_dump(current)
    raw = item["after_text"].encode()
    item["after_sha256"] = hashlib.sha256(raw).hexdigest()
    monkeypatch.setattr(AUDIT, "counts", Counter())
    if mutation:
        with pytest.raises(AssertionError):
            AUDIT.invert_chain(raw, [item])
    else:
        assert AUDIT.invert_chain(raw, [item]) == yaml.safe_load(item["before_text"])
        assert AUDIT.counts == {
            "new_evidence": 30,
            "new_references": 2,
            "new_curation_history": 1,
        }
