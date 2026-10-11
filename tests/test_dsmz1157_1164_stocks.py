"""Stock-stage source arithmetic, preservation and guarded writes."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_dsmz1157_1164_stocks as repair

spec = importlib.util.spec_from_file_location("stock1157_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())


@pytest.mark.parametrize("item", PLAN["records"], ids=lambda r: r["key"])
def test_frozen_preview_and_independent_inversion(item):
    before = repair.runner.load_yaml(item["before_text"])
    after, claims, resolutions = repair.build(before, item["key"], PLAN["created_at"])
    assert repair.runner.render(item["before_text"], after).decode() == item["after_text"]
    assert claims == item["claims"] and resolutions == item["claim_resolutions"]
    assert audit.check(before, after, item)["stock_nodes_relocated"] == (
        4 if item["key"].startswith("1157") else 1
    )


@pytest.mark.parametrize("item", PLAN["records"], ids=lambda r: r["key"])
def test_rejects_unreviewed_baseline(item):
    before = repair.runner.load_yaml(item["before_text"])
    field = "composition" if item["kind"] == "solution" else "ingredients"
    before[field][0]["concentration"]["value"] = "999"
    with pytest.raises(ValueError, match="baseline"):
        repair.build(before, item["key"], PLAN["created_at"])


@pytest.mark.parametrize(
    "mutation", ["url", "hash", "status", "mapping", "pdf", "amount", "attribute", "step"]
)
def test_rejects_source_drift(mutation):
    group = copy.deepcopy(repair.frozen()["1157-medium"][1])
    if mutation in {"url", "hash", "status"}:
        group["medium_metadata"][
            {"url": "url", "hash": "sha256", "status": "http_status"}[mutation]
        ] = "invalid"
    elif mutation == "mapping":
        group["mapping"]["medium_id"] = "1158"
    elif mutation == "pdf":
        group["pdf"]["pages"] = ["No stock row"]
    else:
        data = json.loads(group["solution_raw"])
        if mutation == "step":
            data["data"]["steps"][0]["step"] = "Add before sterilization"
        else:
            data["data"]["recipe"][4][mutation] = 999
        group["solution_raw"] = json.dumps(data)
        group["solution_metadata"]["sha256"] = repair.runner.sha(group["solution_raw"].encode())
    with pytest.raises(ValueError):
        repair.checked_source(group, "medium")


@pytest.mark.parametrize(
    "mutation",
    [
        "dose",
        "strength",
        "percent",
        "water",
        "solvent",
        "scope",
        "snippet",
        "history",
        "nonstock",
        "reference",
        "mapping",
        "dropped_claim",
    ],
)
def test_independent_audit_rejects_unsafe_edits(mutation):
    item = copy.deepcopy(PLAN["records"][0])
    before, after = [repair.runner.load_yaml(item[k + "_text"]) for k in ("before", "after")]
    stock = after["solutions"][0]
    node = stock["composition"][0]
    if mutation == "dose":
        stock["concentration"]["unit"] = "ML_PER_L"
    elif mutation == "strength":
        node["concentration"]["value"] = "5"
    elif mutation == "percent":
        after["solutions"][1]["composition"][0]["concentration"] = {
            "value": "50",
            "unit": "PERCENT_W_V",
        }
    elif mutation == "water":
        after["ingredients"][-1]["concentration"]["unit"] = "PERCENT_V_V"
    elif mutation == "solvent":
        stock["composition"].append({"preferred_term": "Water"})
    elif mutation == "scope":
        node["notes"] = "Measured final volume is 1 L."
    elif mutation == "snippet":
        node["evidence"][0]["snippet"] = "Riboflavin 5 g/L"
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif mutation == "nonstock":
        after["ingredients"][0]["concentration"]["value"] = "999"
    elif mutation == "reference":
        after["references"][-1]["year"] = 2008
    elif mutation == "mapping":
        node["term"]["id"] = "CHEBI:2509"
    else:
        item["claims"] = item["claims"][1:]
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


@pytest.mark.parametrize("mutation", ["drops", "percent", "link", "flag", "old_quote"])
def test_iron_and_legacy_evidence_not_silently_reinterpreted(mutation):
    item = PLAN["records"][4]
    before, after = [repair.runner.load_yaml(item[k + "_text"]) for k in ("before", "after")]
    if mutation == "drops":
        after["solutions"][0]["concentration"] = {"value": "0.00035", "unit": "L"}
    elif mutation == "percent":
        after["solutions"][0]["composition"][0]["concentration"] = {
            "value": "0.5",
            "unit": "PERCENT_W_V",
        }
    elif mutation == "link":
        after["variant_children"][0]["path"] = before["variant_children"][0]["path"]
    elif mutation == "flag":
        after["high_metal"] = False
    else:
        after["ingredients"][0]["evidence"][0]["explanation"] = "old explanation discarded"
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
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 6
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 6


def test_late_conflict_prevents_all_writes(tmp_path):
    plan = fixture_repo(tmp_path)
    last = tmp_path / PLAN["records"][-1]["path"]
    last.write_text(last.read_text() + "\n# concurrent change\n")
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(tmp_path, plan, "apply")
    for item in PLAN["records"][:-1]:
        assert (tmp_path / item["path"]).read_text() == item["before_text"]
