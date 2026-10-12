"""Offline integrity of the applied batch, not a substitute for source retrieval."""

import hashlib
import json
from collections import Counter
from decimal import Decimal
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports/ingredient_concentration_curation"
BATCHES = sorted(REPORTS.glob("20261007-mediadive-solutions-*-*/plan.json"))
ACTION = "CURATED_SOLUTION_CONCENTRATION_SOURCE_EVIDENCE"


@pytest.mark.parametrize("plan_path", BATCHES, ids=lambda path: path.parent.name)
def test_batch_claims_reports_history_and_data_are_consistent(plan_path):
    batch = plan_path.parent
    plan = json.loads(plan_path.read_text())
    start, stop = map(int, batch.name.rsplit("-", 2)[1:])
    inventory = json.loads((REPORTS / "20261007-source-inventory.json").read_text())
    expected = inventory["records"][start:stop]
    assert len(plan["records"]) == stop - start
    assert len({r["path"] for r in plan["records"]}) == stop - start
    assert [r["path"] for r in plan["records"]] == [r["path"] for r in expected]
    for item, original in zip(plan["records"], expected, strict=True):
        for key in ("path", "id", "solution_id", "name", "before_sha256"):
            assert item[key] == original[key]
    summary = json.loads((batch / "records/summary.json").read_text())
    assert summary["records"] == stop - start
    assert summary["failed"] == summary["schema_blocked"] == 0
    supported = Counter()
    decisions = Counter()
    changed = 0
    for item in plan["records"]:
        assert not item["failure"]
        assert not item["baseline_errors"] and not item["post_errors"]
        assert item["merge_fingerprint_unchanged"]
        relative = item["path"].removeprefix("data/normalized_yaml/")
        report = (batch / "records" / (relative + ".md")).read_text().splitlines()
        assert [line for line in report if line.startswith("- Record:")] == [
            f"- Record: {item['path']}"
        ]
        assert sum(line.startswith("| `") for line in report) == len(item["claims"])
        raw = (ROOT / item["path"]).read_bytes()
        doc = yaml.load(raw, Loader=yaml.CSafeLoader)
        assert doc["id"] == item["id"]
        decisions.update(c["status"] for c in item["claims"])
        if item["before_sha256"] == item["after_sha256"]:
            assert not any(
                c["status"] in {"add", "correct", "evidence_only"} for c in item["claims"]
            )
            continue
        changed += 1
        events = [
            e
            for e in doc["curation_history"]
            if e.get("action") == ACTION and e["timestamp"] == plan["created_at"]
        ]
        assert len(events) == 1 and events[0]["curator"] == "codex"
        latest_is_batch = doc["curation_history"][-1] == events[0]
        if latest_is_batch:
            assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        for claim in item["claims"]:
            if claim["status"] not in {"add", "correct", "evidence_only"}:
                if latest_is_batch and claim["pointer"] is not None:
                    node = doc
                    for key in claim["pointer"]:
                        node = node[key]
                    assert node.get("concentration") == claim["old"]
                continue
            supported[claim["status"]] += 1
            row = json.loads(claim["snippet"])
            assert claim["reference"] == (
                f"https://mediadive.dsmz.de/rest/solution/{item['solution_id']}"
            )
            assert row["optional"] == 0
            assert not row.get("condition") and not row.get("attribute")
            assert row.get("solution_id") is None
            if claim["status"] == "correct":
                assert row["compound_id"] == 4 and row["unit"] == "ml"
                assert claim["old"]["unit"] == "PERCENT_V_V"
                assert claim["new"]["unit"] == "L"
                assert Decimal(claim["new"]["value"]) == Decimal(str(row["amount"])) / 1000
            if claim["status"] == "evidence_only":
                assert claim["old"] == claim["new"]
            if claim["new"]["unit"] == "G_PER_L":
                assert row["unit"] in {"g", "mg", "ug", "\u00b5g", "\u03bcg"}
                assert Decimal(claim["new"]["value"]) == Decimal(str(row["g_l"]))
            if not latest_is_batch:
                continue  # Later evidence-backed curation may supersede this snapshot.
            node = doc
            for key in claim["pointer"]:
                node = node[key]
            assert node["concentration"] == claim["new"]
            assert node["term"]["id"] == f"mediadive.compound:{row['compound_id']}"
            entries = [e for e in node["evidence"] if e["reference"] == claim["reference"]]
            assert len(entries) == 1
            assert entries[0]["snippet"] == claim["snippet"]
            assert entries[0]["supports"] == "SUPPORT"
            assert claim["field"] in entries[0]["explanation"]
            assert item["source_sha256"] in entries[0]["explanation"]
            references = [r for r in doc["references"] if r["reference"] == claim["reference"]]
            assert len(references) == 1
            assert item["source_sha256"] in references[0]["notes"]
    assert changed == summary["proposed_changed"]
    assert decisions == summary["claims"]
    assert supported == {
        key: value for key, value in decisions.items() if key in {"add", "correct", "evidence_only"}
    }


def test_batch_inventory_slices_are_contiguous_without_duplicate_targets():
    assert BATCHES
    next_offset = 0
    targets = set()
    for plan_path in BATCHES:
        start, stop = map(int, plan_path.parent.name.rsplit("-", 2)[1:])
        assert start == next_offset and stop > start
        plan = json.loads(plan_path.read_text())
        paths = {r["path"] for r in plan["records"]}
        assert not targets.intersection(paths)
        targets.update(paths)
        next_offset = stop
