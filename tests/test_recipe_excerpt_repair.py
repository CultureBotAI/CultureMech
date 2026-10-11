"""The reviewed excerpt repair cannot change formulation or earlier history."""

import copy
import importlib.util
import json
from pathlib import Path

import pytest
import yaml

FOLDER = (
    Path(__file__).parents[1]
    / "reports/ingredient_concentration_curation/20261008-recipe-reference-validator"
)
if not (FOLDER / "excerpt-plan.json").exists():
    pytest.skip("Local pinned excerpt plan is unavailable", allow_module_level=True)
SPEC = importlib.util.spec_from_file_location("excerpt_repair", FOLDER / "repair_excerpts.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


@pytest.fixture(params=[0, 1])
def reviewed(request):
    item = json.loads((FOLDER / "excerpt-plan.json").read_text())["records"][request.param]
    return yaml.safe_load(item["before_text"]), yaml.safe_load(item["after_text"]), item


def test_only_excerpt_and_event_changed(reviewed):
    before, after, item = reviewed
    assert MODULE.check(before, after, item) == {
        "corrected_evidence_snippets": 1,
        "new_curation_history": 1,
    }


@pytest.mark.parametrize("mutation", ["snippet", "reference", "quantity", "history", "id"])
def test_independent_audit_rejects_other_changes(reviewed, mutation):
    before, after, item = reviewed
    bad = copy.deepcopy(after)
    if mutation == "snippet":
        bad["evidence"][2]["snippet"] += " fabricated suffix"
    elif mutation == "reference":
        bad["evidence"][2]["reference"] += "0"
    elif mutation == "quantity":
        bad["solutions"][0]["concentration"]["value"] = "999"
    elif mutation == "history":
        bad["curation_history"][0]["notes"] = "rewritten history"
    else:
        bad["id"] = "CultureMech:999999"
    with pytest.raises(AssertionError):
        MODULE.check(before, bad, item)


def fixture_tree(tmp_path, monkeypatch):
    plan = json.loads((FOLDER / "excerpt-plan.json").read_text())
    for item in plan["records"]:
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    monkeypatch.setattr(MODULE, "ROOT", tmp_path)
    return plan


def test_apply_verify_and_noop(tmp_path, monkeypatch):
    plan = fixture_tree(tmp_path, monkeypatch)
    assert MODULE.apply(plan) == {"changed": 2, "verified": 0}
    assert MODULE.apply(plan, verify=True) == {"changed": 0, "verified": 2}
    assert MODULE.apply(plan) == {"changed": 0, "verified": 2}


def test_drift_blocks_the_whole_batch(tmp_path, monkeypatch):
    plan = fixture_tree(tmp_path, monkeypatch)
    last = tmp_path / plan["records"][-1]["path"]
    last.write_text(last.read_text() + "\n# concurrent edit\n")
    first = tmp_path / plan["records"][0]["path"]
    before = first.read_bytes()
    with pytest.raises(AssertionError, match="Record drift"):
        MODULE.apply(plan)
    assert first.read_bytes() == before


def test_duplicate_target_plan_is_rejected(tmp_path, monkeypatch):
    plan = fixture_tree(tmp_path, monkeypatch)
    plan["records"] = [plan["records"][0], plan["records"][0]]
    with pytest.raises(AssertionError):
        MODULE.apply(plan)
