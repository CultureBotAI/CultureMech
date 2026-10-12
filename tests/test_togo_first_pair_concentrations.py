"""Adversarial source, batch-volume, variant, provenance and write-guard checks."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_togo_first_pair_concentrations as repair

spec = importlib.util.spec_from_file_location("togo_first_pair_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())


@pytest.mark.parametrize("item", PLAN["records"], ids=lambda r: r["key"])
def test_preview_and_independent_audit(item):
    before = repair.runner.load_yaml(item["before_text"])
    after, claims = repair.build(before, item["key"], PLAN["created_at"])
    assert after == repair.runner.load_yaml(item["after_text"])
    assert claims == item["claims"]
    assert audit.check(before, after, item)["quantity_corrections"] == (
        4 if item["key"] in repair.MIDS[:2] else 0
    )


@pytest.mark.parametrize("item", PLAN["records"], ids=lambda r: r["key"])
def test_baseline_drift_rejected(item):
    before = repair.runner.load_yaml(item["before_text"])
    before["ingredients"][0]["concentration"]["value"] = "999"
    with pytest.raises(ValueError, match="baseline"):
        repair.build(before, item["key"], PLAN["created_at"])


@pytest.mark.parametrize("field", ["url", "response_url", "http_status", "sha256"])
def test_source_capture_drift_rejected(field):
    context = copy.deepcopy(repair.frozen())
    context["sources"]["M1001"]["metadata"][field] = "wrong"
    with pytest.raises(ValueError, match="Source capture"):
        repair.checked_source(context, "M1001")


@pytest.mark.parametrize(
    "mutation",
    ["unit", "volume", "stock", "history", "note", "snippet", "mapping", "invented_year", "agar"],
)
def test_independent_audit_rejects_wrong_science_or_unrelated_edits(mutation):
    item = copy.deepcopy(PLAN["records"][1])
    before, after = [repair.runner.load_yaml(item[k + "_text"]) for k in ("before", "after")]
    node = after["ingredients"][0]
    if mutation == "unit":
        node["concentration"]["unit"] = "ML_PER_L"
    elif mutation == "volume":
        node["concentration"]["value"] = "233"
    elif mutation == "stock":
        after["solutions"][1]["composition"][0]["concentration"]["value"] = "0.005"
    elif mutation == "history":
        after["curation_history"][0]["curator"] = "rewritten"
    elif mutation == "note":
        node["notes"] = "Final volume is 1 L."
    elif mutation == "snippet":
        node["evidence"][0]["snippet"] = "invented quote"
    elif mutation == "mapping":
        node["term"]["id"] = "CHEBI:2509"
    elif mutation == "invented_year":
        after["references"][1]["year"] = 2026
    else:
        after["ingredients"][6]["concentration"]["value"] = "10"
    for c in item["claims"]:
        c["new"] = audit.get(after, c["pointer"])["concentration"]
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


def test_missing_original_and_conflicting_preparation_never_silently_corrected():
    for item in PLAN["records"][2:]:
        assert item["before_text"] == item["after_text"]
        assert all(c["status"] == "unsupported" for c in item["claims"])
        assert all("500 ml" in c["explanation"] for c in item["claims"])


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


def test_apply_noop_and_verify(tmp_path):
    plan = fixture_repo(tmp_path)
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 2
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied_or_unchanged"] == 4


def test_late_concurrent_edit_prevents_all_writes(tmp_path):
    plan = fixture_repo(tmp_path)
    target = tmp_path / PLAN["records"][-1]["path"]
    target.write_text(target.read_text() + "\n# concurrent edit\n")
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(tmp_path, plan, "apply")
    for item in PLAN["records"][:-1]:
        assert (tmp_path / item["path"]).read_text() == item["before_text"]


def test_source_reordering_and_agar_variant_are_not_interchangeable():
    for mid, expected in [("M1001", False), ("M1002", True)]:
        doc = repair.runner.load_yaml(
            next(r["after_text"] for r in PLAN["records"] if r["key"] == mid)
        )
        assert any(n["preferred_term"] == "agar" for n in doc["ingredients"]) is expected
        assert all(s["concentration"]["unit"] == "L" for s in doc["solutions"])
