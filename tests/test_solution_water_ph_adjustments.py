"""Inspected-source boundaries and lossless edits across all selected pH groups."""

import copy
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_solution_water_ph_adjustments as repair  # noqa: E402

CTX = repair.context()
CASES = repair.water.selected(CTX)
ADAPTER = repair.adapter(CTX)
SPEC = importlib.util.spec_from_file_location(
    "water_ph_adjustments_audit", repair.FOLDER / "audit.py"
)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


@pytest.mark.parametrize("case", CASES, ids=lambda c: str(c["solution_id"]))
def test_individually_inspected_water_input_has_exact_evidence_and_full_inversion(case):
    before = repair.load_yaml(case["before_text"])
    after, claims = ADAPTER.reviewer(
        before, case["source_raw"], case["source_metadata"], "2026-10-08T02:00:00+00:00"
    )
    item = {
        **case,
        "action": repair.ACTION,
        "claims": claims,
        "source_sha256": case["source_metadata"]["sha256"],
    }
    assert AUDIT.check(before, after, item, case)["quantity_corrections"] == 1
    assert repair.load_yaml(repair.shared.render(case["before_text"], after)) == after
    source = json.loads(case["source_raw"])["data"]
    water = next(r for r in source["recipe"] if r["compound_id"] == 4)
    assert repair.shared.decide(source, water, claims[0]["old"])[1] == "unsupported"
    assert before == repair.load_yaml(case["before_text"])


@pytest.mark.parametrize(
    "change",
    [
        "water_amount",
        "water_optional",
        "water_attribute",
        "preparation",
        "extra_step",
        "source_id",
        "local_notes",
        "local_amount",
        "prior_evidence",
        "metadata",
    ],
)
def test_uninspected_context_or_record_drift_is_refused(change):
    case = CASES[0]
    doc = repair.load_yaml(case["before_text"])
    source = json.loads(case["source_raw"])
    meta = copy.deepcopy(case["source_metadata"])
    water = next(r for r in source["data"]["recipe"] if r["compound_id"] == 4)
    node = next(n for n in doc["composition"] if n["term"]["id"] == "mediadive.compound:4")
    if change == "water_amount":
        water["amount"] = 900
    elif change == "water_optional":
        water["optional"] = 1
    elif change == "water_attribute":
        water["attribute"] = "make up to volume"
    elif change == "preparation":
        source["data"]["steps"][0]["step"] = "Make up to 1 L."
    elif change == "extra_step":
        source["data"]["steps"].append({"recipe_order": None, "step": "Add 1 L stock."})
    elif change == "source_id":
        source["data"]["id"] = 999999
    elif change == "local_notes":
        doc["notes"] = "different formulation"
    elif change == "local_amount":
        node["concentration"]["value"] = "900"
    elif change == "prior_evidence":
        node["evidence"] = [{"reference": "https://example.org/older-evidence"}]
    elif change == "metadata":
        meta["accessed_at"] = "2020-01-01"
    raw = (
        case["source_raw"]
        if source == json.loads(case["source_raw"])
        else json.dumps(source, indent=2)
    )
    meta["sha256"] = repair.sha(raw.encode())
    with pytest.raises(ValueError):
        ADAPTER.reviewer(doc, raw, meta, "2026-10-08T02:00:00+00:00")


def test_caller_cannot_turn_mutated_context_into_an_approval():
    ctx = copy.deepcopy(CTX)
    ctx["records"][0]["source_metadata"]["accessed_at"] = "2020-01-01"
    with pytest.raises(ValueError, match="Context object changed"):
        repair.adapter(ctx)


def test_helper_rejects_makeup_instruction_even_when_parameter_matches_source():
    case = CASES[0]
    source = json.loads(case["source_raw"])
    source["data"]["steps"][0]["step"] = "Make up to 1 L; adjust pH to 7.2."
    raw = json.dumps(source, indent=2)
    with pytest.raises(ValueError, match="Unreviewed preparation"):
        repair.water.review_input(
            repair.load_yaml(case["before_text"]),
            raw,
            {**case["source_metadata"], "sha256": repair.sha(raw.encode())},
            "2026-10-08T02:00:00+00:00",
            preparation=source["data"]["steps"][0]["step"],
            amount_ml=1000,
            old_quantity=case["candidate"]["old"],
            action=repair.ACTION,
        )


@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    root = tmp_path.resolve()
    plan = json.loads((repair.FOLDER / "plan.json").read_text())
    cache = root / "sources"
    cache.mkdir()
    for case in CASES:
        path = root / case["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(case["before_text"])
        (cache / f"{case['solution_id']}.json").write_text(case["source_raw"])
        (cache / f"{case['solution_id']}.metadata.json").write_text(
            json.dumps(case["source_metadata"])
        )
    tracked = "\0".join(c["path"] for c in CASES) + "\0"

    def ls_files(command, **kwargs):
        assert command == ["git", "ls-files", "-z", "data/normalized_yaml"]
        return tracked.encode()

    monkeypatch.setattr(repair.shared.subprocess, "check_output", ls_files)
    return root, plan, cache


def test_real_plan_applies_and_reapplies_without_duplicate_provenance(sandbox):
    root, plan, cache = sandbox
    repair.validate_plan(root, plan, CTX, cache)
    assert repair.shared.apply(root, plan, cache, adapter=ADAPTER) == {
        "changed": 107,
        "already_applied": 0,
    }
    repair.validate_plan(root, plan, CTX, cache)
    assert repair.shared.apply(root, plan, cache, adapter=ADAPTER) == {
        "changed": 0,
        "already_applied": 107,
    }
    assert repair.shared.verify(root, plan, cache, adapter=ADAPTER)["verified_new_snippets"] == 107
    plan["records"][0]["claims"][0]["explanation"] += " invented claim"
    with pytest.raises(ValueError, match="Plan claims drift"):
        repair.validate_plan(root, plan, CTX, cache)


@pytest.mark.parametrize(
    "change",
    ["membership", "case_path", "id", "before", "after", "snippet", "source_hash", "timestamp"],
)
def test_frozen_plan_tampering_is_refused(sandbox, change):
    root, plan, cache = sandbox
    item = plan["records"][0]
    if change == "membership":
        plan["records"].pop()
    elif change == "case_path":
        item["path"] = item["path"].upper()
    elif change == "id":
        item["id"] = "CultureMech:999999"
    elif change == "before":
        item["before_text"] += "\n"
    elif change == "after":
        item["after_text"] += "\n"
    elif change == "snippet":
        item["claims"][0]["snippet"] = "invented"
    elif change == "source_hash":
        item["source_sha256"] = "0" * 64
    elif change == "timestamp":
        plan["created_at"] = "2020-01-01T00:00:00+00:00"
    with pytest.raises(ValueError):
        repair.validate_plan(root, plan, CTX, cache)


def test_last_target_concurrent_edit_prevents_every_pending_write(sandbox):
    root, plan, cache = sandbox
    last = root / plan["records"][-1]["path"]
    last.write_text(last.read_text() + "\n# concurrent edit\n")
    with pytest.raises(ValueError):
        repair.shared.apply(root, plan, cache, adapter=ADAPTER)
    for item in plan["records"][:-1]:
        assert (root / item["path"]).read_text() == item["before_text"]
