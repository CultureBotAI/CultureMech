"""Pinned source, write guards and independent water-input checks."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_dsmz803_1046_1065_water as repair

spec = importlib.util.spec_from_file_location("water_input_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())


@pytest.mark.parametrize("item", PLAN["records"], ids=lambda r: r["key"])
def test_frozen_preview_and_independent_inversion(item):
    before = repair.runner.load_yaml(item["before_text"])
    after, claims = repair.build(before, item["key"], PLAN["created_at"])
    assert repair.runner.render(item["before_text"], after).decode() == item["after_text"]
    assert claims == item["claims"]
    assert audit.check(before, after, item)["quantity_corrections"] == 1


@pytest.mark.parametrize("item", PLAN["records"], ids=lambda r: r["key"])
def test_rejects_unreviewed_baseline(item):
    before = repair.runner.load_yaml(item["before_text"])
    field = "composition" if item["kind"] == "solution" else "ingredients"
    before[field][0]["concentration"]["value"] = "999"
    with pytest.raises(ValueError, match="baseline"):
        repair.build(before, item["key"], PLAN["created_at"])


@pytest.mark.parametrize("mutation", ["url", "hash", "status", "mapping", "pdf", "pair"])
def test_rejects_source_drift(mutation):
    group = copy.deepcopy(repair.frozen()["803-medium"][1])
    if mutation in {"url", "hash", "status"}:
        key = {"url": "url", "hash": "sha256", "status": "http_status"}[mutation]
        group["medium_metadata"][key] = "invalid"
    elif mutation == "mapping":
        group["mapping"]["medium_id"] = "804"
    elif mutation == "pdf":
        group["pdf"]["pages"] = ["No water row"]
    else:
        source = json.loads(group["solution_raw"])
        source["data"]["recipe"][-1]["amount"] = 500
        group["solution_raw"] = json.dumps(source)
        group["solution_metadata"]["sha256"] = repair.runner.sha(group["solution_raw"].encode())
    with pytest.raises(ValueError):
        repair.checked_source(group, "medium")


@pytest.mark.parametrize(
    "mutation", ["unit", "value", "scope", "snippet", "history", "nonwater", "reference", "mapping"]
)
def test_independent_audit_rejects_unsafe_edits(mutation):
    item = copy.deepcopy(PLAN["records"][0])
    before, after = [repair.runner.load_yaml(item[k + "_text"]) for k in ("before", "after")]
    node = after["ingredients"][8]
    if mutation == "unit":
        node["concentration"]["unit"] = "ML_PER_L"
    elif mutation == "value":
        node["concentration"]["value"] = "1000"
    elif mutation == "scope":
        node["notes"] = "Measured final volume is 1 L."
    elif mutation == "snippet":
        node["evidence"][1]["snippet"] = "Tap water 500 ml"
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif mutation == "nonwater":
        after["ingredients"][0]["concentration"]["value"] = "999"
    elif mutation == "reference":
        after["references"][-1]["year"] = 2007
    else:
        node["term"]["id"] = "CHEBI:2509"
    claim = next(c for c in item["claims"] if c["status"] == "correct")
    claim["new"] = node["concentration"]
    claim["corroboration"] = node["evidence"][1]
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


def fixture_repo(tmp_path):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    for item in PLAN["records"]:
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    subprocess.run(["git", "-C", str(tmp_path), "add", "data"], check=True)
    plan = tmp_path / "plan.json"
    plan.write_text(json.dumps(PLAN))
    return plan


def test_apply_noop_and_readback(tmp_path):
    plan = fixture_repo(tmp_path)
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 9
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 9


def test_late_conflict_prevents_all_writes(tmp_path):
    plan = fixture_repo(tmp_path)
    last = tmp_path / PLAN["records"][-1]["path"]
    last.write_text(last.read_text() + "\n# concurrent change\n")
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(tmp_path, plan, "apply")
    for item in PLAN["records"][:-1]:
        assert (tmp_path / item["path"]).read_text() == item["before_text"]
