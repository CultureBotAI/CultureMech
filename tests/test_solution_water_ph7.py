"""Source, plan, preservation, and concurrency guards for the inspected water batch."""

import copy
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_solution_water_ph7 as repair  # noqa: E402

CTX = repair.context()
CASES = repair.selected(CTX)
SPEC = importlib.util.spec_from_file_location("water_ph7_audit", repair.FOLDER / "audit.py")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


@pytest.mark.parametrize("case", CASES, ids=lambda c: str(c["solution_id"]))
def test_each_inspected_record_has_exact_water_evidence_and_full_inversion(case):
    before = repair.load_yaml(case["before_text"])
    after, claims = repair.review(
        before, case["source_raw"], case["source_metadata"], "2026-10-08T01:00:00+00:00"
    )
    item = {
        **case,
        "action": repair.ACTION,
        "claims": claims,
        "source_sha256": case["source_metadata"]["sha256"],
    }
    assert AUDIT.check(before, after, item, case["source_raw"])["quantity_corrections"] == 1
    assert repair.load_yaml(repair.shared.render(case["before_text"], after)) == after
    assert before == repair.load_yaml(case["before_text"])


@pytest.mark.parametrize(
    "change",
    [
        "makeup",
        "additional_step",
        "missing_steps",
        "conditional_water",
        "water_attribute",
        "water_unit",
        "water_amount",
        "source_volume",
        "water_label",
        "duplicate_water",
        "stock_row",
        "local_preparation",
        "local_notes",
        "water_notes",
        "prior_evidence",
        "per_volume",
        "old_amount",
        "root_id",
        "label",
        "inventory",
    ],
)
def test_changed_context_is_refused(change):
    case = CASES[0]
    doc = repair.load_yaml(case["before_text"])
    source = json.loads(case["source_raw"])
    data = source["data"]
    water = data["recipe"][-1]
    node = doc["composition"][-1]
    if change == "makeup":
        data["steps"][0]["step"] = "Make up to 1 L; adjust pH to 7.0."
    elif change == "additional_step":
        data["steps"].append({"recipe_order": None, "step": "Add stock."})
    elif change == "missing_steps":
        data.pop("steps")
    elif change == "conditional_water":
        water["condition"] = "as needed"
    elif change == "water_attribute":
        water["attribute"] = "make up to"
    elif change == "water_unit":
        water["unit"] = "g"
    elif change == "water_amount":
        water["amount"] = 900
    elif change == "source_volume":
        data["volume"] = 900
    elif change == "water_label":
        water["compound"] = "Sea water"
    elif change == "duplicate_water":
        data["recipe"].append(copy.deepcopy(water))
    elif change == "stock_row":
        data["recipe"][0]["solution_id"] = 100
    elif change == "local_preparation":
        doc["preparation_notes"] += " Make up to final volume."
    elif change == "local_notes":
        doc["notes"] = "Different batch size"
    elif change == "water_notes":
        node["notes"] = "final volume"
    elif change == "prior_evidence":
        node["evidence"] = [{"reference": "https://example.org/old"}]
    elif change == "per_volume":
        node["concentration"]["per_volume"] = "per liter"
    elif change == "old_amount":
        node["concentration"]["value"] = "100"
    elif change == "root_id":
        doc["term"]["id"] = "mediadive.solution:999"
    elif change == "label":
        node["term"]["label"] = "Sea water"
    elif change == "inventory":
        doc["composition"].pop(0)
    raw = json.dumps(source, indent=2)
    meta = {**case["source_metadata"], "sha256": repair.sha(raw.encode())}
    with pytest.raises(ValueError):
        repair.review(doc, raw, meta, "2026-10-08T01:00:00+00:00")


def test_general_reviewer_still_withholds_preparation_dependent_water():
    case = CASES[0]
    source = json.loads(case["source_raw"])["data"]
    value, status, _ = repair.shared.decide(
        source, source["recipe"][-1], {"value": "1000", "unit": "PERCENT_V_V"}
    )
    assert value is None and status == "unsupported"


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


def test_real_plan_validates_applies_and_reapplies_without_new_history(sandbox):
    root, plan, cache = sandbox
    repair.validate_plan(root, plan, CTX, cache)
    assert repair.shared.apply(root, plan, cache, adapter=repair.adapter()) == {
        "changed": 52,
        "already_applied": 0,
    }
    repair.validate_plan(root, plan, CTX, cache)
    assert repair.shared.apply(root, plan, cache, adapter=repair.adapter()) == {
        "changed": 0,
        "already_applied": 52,
    }
    assert (
        repair.shared.verify(root, plan, cache, adapter=repair.adapter())["verified_new_snippets"]
        == 52
    )


@pytest.mark.parametrize(
    "change",
    [
        "subset",
        "case_path",
        "id",
        "before",
        "after",
        "snippet",
        "timestamp",
        "source_hash",
        "source_meta",
        "source_bytes",
    ],
)
def test_frozen_plan_or_capture_tampering_is_refused(sandbox, change):
    root, plan, cache = sandbox
    item = plan["records"][0]
    if change == "subset":
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
    elif change == "timestamp":
        plan["created_at"] = "2026-10-08T02:00:00+00:00"
    elif change == "source_hash":
        item["source_sha256"] = "0" * 64
    elif change == "source_meta":
        path = cache / f"{item['solution_id']}.metadata.json"
        meta = json.loads(path.read_text())
        meta["accessed_at"] = "2026-10-08T02:00:00+00:00"
        path.write_text(json.dumps(meta))
    elif change == "source_bytes":
        path = cache / f"{item['solution_id']}.json"
        path.write_text(path.read_text() + "\n")
    with pytest.raises(ValueError):
        repair.validate_plan(root, plan, CTX, cache)
    assert (root / CASES[0]["path"]).read_text() == CASES[0]["before_text"]


def test_late_target_concurrent_edit_blocks_all_pending_writes(sandbox):
    root, plan, cache = sandbox
    last = root / plan["records"][-1]["path"]
    last.write_text(last.read_text() + "\n# concurrent user edit\n")
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.shared.apply(root, plan, cache, adapter=repair.adapter())
    assert (root / CASES[0]["path"]).read_text() == CASES[0]["before_text"]
