"""Regression checks for the final 633 exact KOMODO follow-up paths."""

import hashlib
import importlib.util
import json
from pathlib import Path

import pytest
import yaml
from review_solution_concentration_evidence import followup_chain, followup_result_hash

from tests.test_medium_concentration_batch import AUDIT, FOLLOWUPS

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "reports/ingredient_concentration_curation"
FOLDER = BASE / "20261008-komodo-media-3000-3633"
WITHHELD = {
    "1081",
    "1085",
    "1091",
    "1106",
    "1111",
    "1130",
    "1157",
    "1164",
    "1175",
    "1184",
    "1185",
    "1204",
    "1216",
    "1233",
    "1248",
    "1265",
    "1270",
    "1274",
    "1288",
    "1309",
}


def test_exact_cohort_and_persisted_claims():
    plan = json.loads((FOLDER / "plan.json").read_text())
    captures = json.loads((FOLDER / "source-captures.json").read_text())
    context = {
        r["path"]: r for r in json.loads((FOLDER / "inspected-candidate-context.json").read_text())
    }
    assert captures["terminal"]
    assert len(plan["records"]) == len({r["path"] for r in plan["records"]}) == 633
    assert [r["path"] for r in plan["records"]] == [r["path"] for r in captures["records"]]
    successors = [
        r
        for path in FOLLOWUPS
        for r in json.loads(path.read_text())["records"]
        if r["before_sha256"] != r["after_sha256"]
    ]
    changed = supported = 0
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        expected, _ = followup_result_hash(item, successors)
        assert hashlib.sha256(raw).hexdigest() == expected
        chain = followup_chain(item, successors)
        doc = AUDIT.invert_chain(raw, chain) if chain else yaml.load(raw, Loader=yaml.CSafeLoader)
        assert not item["failure"] and not item["baseline_errors"] and not item["post_errors"]
        report = FOLDER / "records" / (item["path"].removeprefix("data/normalized_yaml/") + ".md")
        lines = report.read_text().splitlines()
        assert [s for s in lines if s.startswith("- Record:")] == ["- Record: " + item["path"]]
        assert not any(s.startswith("- State: preview") for s in lines)
        assert sum(s.startswith("| `") for s in lines) == len(item["claims"])
        accepted = [c for c in item["claims"] if c["status"] in {"add", "correct", "evidence_only"}]
        assert bool(accepted) == (item["before_sha256"] != item["after_sha256"])
        if not accepted:
            continue
        changed += 1
        original = context[item["path"]]
        assert doc["id"] == item["id"] == original["local"]["id"]
        assert doc["curation_history"][:-1] == original["local"]["curation_history"]
        assert doc["curation_history"][-1]["curator"] == "codex"
        assert doc["references"][-1]["title"] == plan["mapping_title"]
        assert doc["evidence"][-1]["snippet"] == item["mapping"]["snippet"]
        for claim in accepted:
            assert claim["status"] == "evidence_only" and claim["old"] == claim["new"]
            node = doc["ingredients"][claim["pointer"][1]]
            evidence = node["evidence"][-1]
            assert node["concentration"] == claim["new"]
            assert evidence["snippet"] == claim["snippet"]
            assert evidence["snippet"] in original["source_raw"]
            assert evidence["reference"] == original["source_metadata"]["url"] == claim["reference"]
            assert evidence["supports"] == "SUPPORT"
            assert claim["field"] in evidence["explanation"]
            assert item["source_sha256"] in evidence["explanation"]
            supported += 1
    assert (changed, supported) == (38, 226)


@pytest.mark.parametrize("mid", sorted(WITHHELD))
def test_withholdings_are_source_pinned_and_unchanged(mid):
    plan = json.loads((FOLDER / "plan.json").read_text())
    assert {d["medium_id"] for d in plan["withholdings"]} == WITHHELD
    decision = next(d for d in plan["withholdings"] if d["medium_id"] == mid)
    item = next(r for r in plan["records"] if r["id"] == decision["id"])
    context = next(
        r
        for r in json.loads((FOLDER / "inspected-candidate-context.json").read_text())
        if r["path"] == item["path"]
    )
    assert (
        decision["source_sha256"]
        == item["source_sha256"]
        == hashlib.sha256(context["source_raw"].encode()).hexdigest()
    )
    value = json.loads(context["source_raw"])
    for key in decision["source_pointer"]:
        value = value[key]
    if isinstance(value, str):
        assert decision["snippet"] == value
    else:
        assert json.loads(decision["snippet"]) == value
        assert decision["snippet"] in context["source_raw"]
    assert item["before_sha256"] == item["after_sha256"]
    assert all(c["status"] == "conflict" for c in item["claims"] if c["pointer"] is not None)


def test_1159_inconsistent_api_agar_not_endorsed():
    plan = json.loads((FOLDER / "plan.json").read_text())
    item = next(r for r in plan["records"] if r["komodo_id"] == "1159")
    claim = next(
        c for c in item["claims"] if c["ingredient"] == "Agar" and c["pointer"] is not None
    )
    assert claim["status"] == "conflict" and claim["new"] is None
    assert claim["old"] == {"value": "15", "unit": "G_PER_L"}


@pytest.mark.parametrize("count", [-1, 0, 500])
def test_auditor_rejects_invalid_or_wrong_cohort_size(tmp_path, count):
    spec = importlib.util.spec_from_file_location(
        "komodo_final_audit", BASE / "20261007-komodo-media-0000-0500/audit.py"
    )
    auditor = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(auditor)
    assert auditor.check.__defaults__[-1] == 500
    (tmp_path / "plan.json").write_text(json.dumps({"records": [{}] * 633}))
    with pytest.raises(AssertionError):
        auditor.check(tmp_path, tmp_path / "unused.html", False, tmp_path, count)
