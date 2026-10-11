"""Adversarial checks of HCl strength, stock dose, evidence and guarded writes."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_fecl2_stock_concentration as repair

spec = importlib.util.spec_from_file_location("fecl2_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())
ITEM = PLAN["records"][0]


def test_source_backed_result_and_complete_inversion():
    before = repair.runner.load_yaml(ITEM["before_text"])
    original = copy.deepcopy(before)
    after, claims = repair.build(before, PLAN["created_at"])
    assert before == original
    assert after == repair.runner.load_yaml(ITEM["after_text"])
    assert claims == ITEM["claims"]
    assert audit.check(before, after, ITEM)["new_evidence"] == 3


@pytest.mark.parametrize("key", ["id", "composition", "source_data"])
def test_baseline_drift_refused(key):
    before = repair.runner.load_yaml(ITEM["before_text"])
    before[key] = "changed"
    with pytest.raises(ValueError, match="baseline"):
        repair.build(before, PLAN["created_at"])


@pytest.mark.parametrize("key", ["url", "response_url", "http_status", "sha256"])
def test_capture_drift_refused(key):
    context = copy.deepcopy(repair.frozen())
    context["sources"]["S3846"]["metadata"][key] = "changed"
    with pytest.raises(ValueError, match="capture drift"):
        repair.sources(context)


@pytest.mark.parametrize(
    "key,value", [("amount", 100), ("unit", "g"), ("attribute", "25%"), ("compound_id", 99)]
)
def test_source_semantics_checked_beyond_hash(key, value):
    context = copy.deepcopy(repair.frozen())
    source = context["sources"]["S3846"]
    body = json.loads(source["raw"])
    body["data"]["recipe"][0][key] = value
    source["raw"] = json.dumps(body)
    source["metadata"]["sha256"] = repair.runner.sha(source["raw"].encode())
    with pytest.raises(ValueError, match="formulation drift"):
        repair.sources(context)


@pytest.mark.parametrize(
    "mutation",
    [
        "dose",
        "strength",
        "final_volume",
        "quote",
        "locator",
        "iron",
        "water",
        "history",
        "grounding",
        "year",
        "source",
        "extra_stock",
    ],
)
def test_independent_audit_rejects_wrong_claims(mutation):
    before = repair.runner.load_yaml(ITEM["before_text"])
    after = repair.runner.load_yaml(ITEM["after_text"])
    stock = after["solutions"][0]
    acid = stock["composition"][0]
    if mutation == "dose":
        stock["concentration"] = {"value": "10", "unit": "ML_PER_L"}
    elif mutation == "strength":
        acid["concentration"] = {"value": "0.077", "unit": "MOLAR"}
    elif mutation == "final_volume":
        after["concentration"] = {"value": "1", "unit": "L"}
    elif mutation == "quote":
        acid["evidence"][0]["snippet"] = "fabricated"
    elif mutation == "locator":
        after["composition"][0]["evidence"][0]["explanation"] = before["composition"][1][
            "evidence"
        ][0]["explanation"]
    elif mutation == "iron":
        after["composition"][0]["concentration"]["value"] = "15"
    elif mutation == "water":
        after["composition"][1]["concentration"]["unit"] = "ML_PER_L"
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "changed"
    elif mutation == "grounding":
        acid["chebi_term"]["id"] = "CHEBI:15377"
    elif mutation == "year":
        after["references"][-1]["year"] = 2026
    elif mutation == "source":
        acid["evidence"][1]["explanation"] = acid["evidence"][0]["explanation"]
    elif mutation == "extra_stock":
        stock["solutions"] = [{"preferred_term": "Unreviewed extra stock"}]
    with pytest.raises(AssertionError):
        audit.check(before, after, ITEM)


def fixture_repo(tmp_path):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    target = tmp_path / ITEM["path"]
    target.parent.mkdir(parents=True)
    target.write_text(ITEM["before_text"])
    subprocess.run(["git", "add", ITEM["path"]], cwd=tmp_path, check=True)
    return target


def stub_head(monkeypatch):
    original = subprocess.check_output

    def output(args, **kwargs):
        if args == ["git", "rev-parse", "HEAD"]:
            return PLAN["commit"] + "\n"
        return original(args, **kwargs)

    monkeypatch.setattr(subprocess, "check_output", output)


def test_preview_apply_readback_and_noop(tmp_path, monkeypatch):
    target = fixture_repo(tmp_path)
    stub_head(monkeypatch)
    plan_path = tmp_path / "plan.json"
    plan, result = repair.process(tmp_path, plan_path, "preview")
    assert target.read_text() == ITEM["before_text"]
    assert result["changed"] == 0
    repair.process(tmp_path, plan_path, "apply")
    applied = target.read_bytes()
    assert repair.process(tmp_path, plan_path, "verify")[1]["already_applied"] == 1
    assert repair.process(tmp_path, plan_path, "apply")[1]["changed"] == 0
    assert target.read_bytes() == applied == plan["records"][0]["after_text"].encode()


def test_concurrent_edit_refused(tmp_path, monkeypatch):
    target = fixture_repo(tmp_path)
    stub_head(monkeypatch)
    plan_path = tmp_path / "plan.json"
    repair.process(tmp_path, plan_path, "preview")
    target.write_text(ITEM["before_text"] + "\n# concurrent note\n")
    current = target.read_bytes()
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(tmp_path, plan_path, "apply")
    assert target.read_bytes() == current


def test_symlink_refused(tmp_path, monkeypatch):
    target = fixture_repo(tmp_path)
    stub_head(monkeypatch)
    original = target.with_suffix(".original")
    target.rename(original)
    target.symlink_to(original)
    with pytest.raises(ValueError, match="Symlink"):
        repair.process(tmp_path, tmp_path / "plan.json", "preview")
