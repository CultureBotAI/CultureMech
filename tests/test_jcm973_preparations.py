"""Reject wrong volume stages, invented quantities and untracked curation drift."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_jcm973_preparations as repair
import repair_togo_first_pair_concentrations as previous

spec = importlib.util.spec_from_file_location("jcm973_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())


@pytest.mark.parametrize("item", PLAN["records"], ids=lambda r: r["key"])
def test_preview_source_arithmetic_and_inversion(item):
    before = repair.runner.load_yaml(item["before_text"])
    after, claims = repair.build(before, item["key"], PLAN["created_at"])
    assert after == repair.runner.load_yaml(item["after_text"])
    assert claims == item["claims"]
    counts = audit.check(before, after, item)
    assert counts["stock_stage_concentrations_rebased"] == 1
    assert counts["unsupported_quantity_slots_removed"] == (7 if item["key"] == "M1024" else 6)


@pytest.mark.parametrize("item", PLAN["records"], ids=lambda r: r["key"])
def test_whole_baseline_drift_rejected(item):
    before = repair.runner.load_yaml(item["before_text"])
    before["id"] = "CultureMech:000001"
    with pytest.raises(ValueError, match="baseline"):
        repair.build(before, item["key"], PLAN["created_at"])


@pytest.mark.parametrize("field", ["url", "response_url", "http_status", "sha256"])
def test_capture_drift_rejected(field):
    context = copy.deepcopy(repair.frozen())
    context["sources"]["medium"]["metadata"][field] = "wrong"
    with pytest.raises(ValueError, match="Capture drift"):
        repair.sources(context)


@pytest.mark.parametrize(
    "mutation", ["volume", "g_l", "hydrate", "amount", "conditional", "preparation"]
)
def test_semantic_source_drift_rejected_even_with_updated_capture_hash(mutation):
    context = copy.deepcopy(repair.frozen())
    source = context["sources"]["solution"]
    data = json.loads(source["raw"])
    body = data["data"]
    if mutation == "volume":
        body["volume"] = 1000
    elif mutation == "preparation":
        body["steps"][0]["step"] = body["steps"][0]["step"].replace("in 500 ml", "up to 500 ml")
    else:
        field, value = {
            "g_l": ("g_l", 40.1),
            "hydrate": ("compound", "MgCl2"),
            "amount": ("amount", 41),
            "conditional": ("optional", 1),
        }[mutation]
        body["recipe"][0][field] = value
    source["raw"] = json.dumps(data)
    source["metadata"]["sha256"] = repair.runner.sha(source["raw"].encode())
    with pytest.raises(ValueError, match="drift"):
        repair.sources(context)


@pytest.mark.parametrize(
    "mutation",
    [
        "stock_strength",
        "dose",
        "base_volume",
        "makeup_water",
        "base_water",
        "salt",
        "agar",
        "quote",
        "history",
        "identity",
        "year",
        "ph",
    ],
)
def test_independent_audit_rejects_wrong_science(mutation):
    item = copy.deepcopy(PLAN["records"][1])
    before, after = [repair.runner.load_yaml(item[k + "_text"]) for k in ("before", "after")]
    magnesium, base = after["solutions"]
    if mutation == "stock_strength":
        magnesium["composition"][0]["concentration"]["value"] = "203"
    elif mutation in {"dose", "base_volume"}:
        (magnesium if mutation == "dose" else base)["concentration"] = {"value": "0.5", "unit": "L"}
    elif mutation == "makeup_water":
        magnesium["composition"][1]["concentration"] = {"value": "0.5", "unit": "L"}
    elif mutation == "base_water":
        base["composition"][0]["concentration"]["unit"] = "ML_PER_L"
    elif mutation in {"salt", "agar"}:
        node = next(
            n
            for n in base["composition"]
            if n["preferred_term"] == ("NaCl" if mutation == "salt" else "agar")
        )
        node["concentration"] = {"value": "20", "unit": "G_PER_L"}
    elif mutation == "quote":
        base["composition"][0]["evidence"][0]["snippet"] = "invented"
    elif mutation == "history":
        after["curation_history"][0]["curator"] = "rewritten"
    elif mutation == "identity":
        magnesium["composition"][0]["term"]["id"] = "CHEBI:2509"
    elif mutation == "year":
        after["references"][0]["year"] = 2026
    else:
        after["ph_value"] = 7.0
    for c in item["claims"]:
        c["new"] = audit.get(after, c["pointer"][:-1]).get(c["pointer"][-1])
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


def fixture_repo(tmp_path, plan=PLAN):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    for item in plan["records"]:
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    subprocess.run(["git", "-C", str(tmp_path), "add", "data"], check=True)
    path = tmp_path / "plan.json"
    path.write_text(json.dumps(plan))
    return path


def test_apply_noop_verify(tmp_path):
    plan = fixture_repo(tmp_path)
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 4
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 4


def test_concurrent_edit_prevents_all_writes(tmp_path):
    plan = fixture_repo(tmp_path)
    target = tmp_path / PLAN["records"][-1]["path"]
    target.write_text(target.read_text() + "\n# concurrent edit\n")
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(tmp_path, plan, "apply")
    for item in PLAN["records"][:-1]:
        assert (tmp_path / item["path"]).read_text() == item["before_text"]


def test_historical_togo_followup_verification_cannot_overwrite_repairs(tmp_path):
    old = json.loads((previous.HERE / "plan.json").read_text())
    path = fixture_repo(tmp_path, old)
    previous.process(tmp_path, path, "apply")
    for item in PLAN["records"][:2]:
        (tmp_path / item["path"]).write_text(item["after_text"])
    assert previous.process(tmp_path, path, "verify", PLAN["records"])[1]["followed_records"] == 2
    with pytest.raises(ValueError, match="Concurrent edit"):
        previous.process(tmp_path, path, "apply")
    with pytest.raises(ValueError, match="verify-only"):
        previous.process(tmp_path, path, "apply", PLAN["records"])
    item = PLAN["records"][0]
    (tmp_path / item["path"]).write_text(item["after_text"] + "\n")
    with pytest.raises(ValueError, match="Follow-up result drift"):
        previous.process(tmp_path, path, "verify", PLAN["records"])
