"""Adversarial scientific-scope and guarded-application checks for four recipes."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_basal_makeup_stages as repair

spec = importlib.util.spec_from_file_location("basal_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())
ITEMS = {item["key"]: item for item in PLAN["records"]}


@pytest.mark.parametrize("key", ITEMS)
def test_projection_and_source_audit(key):
    item = ITEMS[key]
    before = repair.runner.load_yaml(item["before_text"])
    original = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == original
    assert after == repair.runner.load_yaml(item["after_text"])
    assert claims == item["claims"] and lineage == item["lineage"]
    result = audit.check(before, after, item)
    assert result["old_quantity_slots"] == (14 if key == "M809" else 17)
    assert result["source_rows"] == (40 if key == "M809" else 31)


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "makeup_water",
        "base_dose",
        "final_dilution",
        "flat_duplicate",
        "stock_dose_unit",
        "trace_scope",
        "trace_extra",
        "trace_missing",
        "trace_preparation",
        "percent_basis",
        "annotation",
        "gas",
        "history",
        "quote",
        "year",
        "missing_claim",
        "duplicate_evidence",
        "preparation",
    ],
)
def test_independent_audit_rejects_unreviewed_changes(key, mutation):
    item = copy.deepcopy(ITEMS[key])
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    base = after["solutions"][0]
    trace = next(s for s in base["solutions"] if "M142" in s["preferred_term"])
    if mutation == "makeup_water":
        base["composition"][0]["concentration"] = {"value": "1", "unit": "L"}
    elif mutation == "base_dose":
        base["concentration"] = {"value": "1", "unit": "L"}
    elif mutation == "final_dilution":
        base["composition"][1]["concentration"]["value"] = "0.001"
    elif mutation == "flat_duplicate":
        after["ingredients"].append(copy.deepcopy(base["composition"][1]))
    elif mutation == "stock_dose_unit":
        after["solutions"][1]["concentration"]["unit"] = "G_PER_L"
    elif mutation == "trace_scope":
        trace["composition"][1]["concentration"] = {"value": "3", "unit": "G_PER_L"}
    elif mutation == "trace_extra":
        trace["composition"].append(copy.deepcopy(base["composition"][1]))
    elif mutation == "trace_missing":
        trace["composition"].pop()
    elif mutation == "trace_preparation":
        trace["preparation_notes"] = "Adjust the final medium to pH 6.5."
    elif mutation == "percent_basis":
        after["solutions"][1]["composition"].append(
            {
                "preferred_term": "Unverified",
                "concentration": {"value": "10", "unit": "PERCENT_W_V"},
            }
        )
    elif mutation == "annotation":
        base["composition"][0]["term"]["id"] = "CHEBI:0000000"
    elif mutation == "gas":
        base["composition"][-1]["concentration"] = {"value": "0", "unit": "G_PER_L"}
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif mutation == "quote":
        base["composition"][1]["evidence"][0]["snippet"] = "invented"
    elif mutation == "year":
        after["references"][0]["year"] = 2026
    elif mutation == "missing_claim":
        item["claims"] = [
            c for c in item["claims"] if c["old_pointer"] != ["ingredients", 0, "concentration"]
        ]
    elif mutation == "duplicate_evidence":
        after["evidence"].append(copy.deepcopy(after["evidence"][0]))
    elif mutation == "preparation":
        after["preparation_steps"][0][
            "description"
        ] = "Make up final supplemented medium to one liter."
    with pytest.raises((AssertionError, KeyError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "key,mutation",
    [
        ("M809", "water_double_count"),
        ("M809", "reducer_rate"),
        ("M809", "per_liter"),
        ("M823", "resazurin"),
        ("M853", "resazurin"),
        ("M853", "parent_ph"),
        ("M853", "extra_calcium"),
        ("M853", "wrong_parent"),
        ("M823", "wrong_child"),
        ("M975", "koh_dose"),
        ("M975", "koh_strength"),
        ("M975", "glucose_strength"),
    ],
)
def test_specific_stage_and_variant_failures(key, mutation):
    item = ITEMS[key]
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    base = after["solutions"][0]
    if mutation == "water_double_count":
        after["solutions"][2]["composition"][0]["term"] = before["ingredients"][0]["term"]
    elif mutation == "reducer_rate":
        after["solutions"][2]["composition"][1]["concentration"] = {
            "value": "20",
            "unit": "G_PER_L",
        }
    elif mutation == "per_liter":
        after["solutions"][1]["concentration"] = {"value": "25", "unit": "ML_PER_L"}
    elif mutation == "resazurin":
        next(n for n in base["composition"] if n["preferred_term"] == "Resazurin")["concentration"][
            "unit"
        ] = "G_PER_L"
    elif mutation == "parent_ph":
        after["ph_value"] = 7.0
    elif mutation == "extra_calcium":
        base["composition"].append(
            {"preferred_term": "CaCl2", "concentration": {"value": "0.2", "unit": "G_PER_L"}}
        )
    elif mutation == "wrong_parent":
        after["parent_media"]["id"] = "CultureMech:010269"
    elif mutation == "wrong_child":
        after["variant_children"][0]["path"] = ITEMS["M823"]["path"]
    elif mutation == "koh_dose":
        base["solutions"][1]["concentration"] = {"value": "10", "unit": "ML_PER_L"}
    elif mutation == "koh_strength":
        base["solutions"][1]["composition"][0]["concentration"]["value"] = "1"
    elif mutation == "glucose_strength":
        after["solutions"][3]["composition"][0]["concentration"]["value"] = "0.02"
    with pytest.raises((AssertionError, KeyError)):
        audit.check(before, after, item)


def fixture_repo(tmp_path, monkeypatch):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    targets = []
    for item in ITEMS.values():
        target = tmp_path / item["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(item["before_text"])
        targets.append(target)
    subprocess.run(["git", "add", "data"], cwd=tmp_path, check=True)
    original = subprocess.check_output

    def output(args, **kwargs):
        return (
            PLAN["commit"] + "\n"
            if args == ["git", "rev-parse", "HEAD"]
            else original(args, **kwargs)
        )

    monkeypatch.setattr(subprocess, "check_output", output)
    return targets


def test_guarded_preview_apply_verify_noop(tmp_path, monkeypatch):
    targets = fixture_repo(tmp_path, monkeypatch)
    plan = tmp_path / "plan.json"
    before = [t.read_bytes() for t in targets]
    repair.process(tmp_path, plan, "preview")
    assert [t.read_bytes() for t in targets] == before
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 4
    applied = [t.read_bytes() for t in targets]
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 4
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert [t.read_bytes() for t in targets] == applied


@pytest.mark.parametrize("mutation", ["concurrent", "forged_plan", "symlink"])
def test_all_targets_preflight_before_any_write(tmp_path, monkeypatch, mutation):
    targets = fixture_repo(tmp_path, monkeypatch)
    target = targets[-1]
    plan_path = tmp_path / "plan.json"
    plan, _ = repair.process(tmp_path, plan_path, "preview")
    if mutation == "concurrent":
        target.write_text(target.read_text() + "\n# concurrent edit\n")
    elif mutation == "forged_plan":
        plan["records"][-1]["claims"].pop()
        plan_path.write_text(json.dumps(plan))
    else:
        elsewhere = tmp_path / "other.yaml"
        target.rename(elsewhere)
        target.symlink_to(elsewhere)
    current = [t.read_bytes() for t in targets]
    with pytest.raises(ValueError):
        repair.process(tmp_path, plan_path, "apply")
    assert [t.read_bytes() for t in targets] == current
