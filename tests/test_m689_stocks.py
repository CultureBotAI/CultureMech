"""M689 scientific-scope and guarded-application regression tests."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_m689_stocks as repair

spec = importlib.util.spec_from_file_location("m689_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())
ITEM = PLAN["records"][0]


def test_projection_and_independent_audit():
    before = repair.runner.load_yaml(ITEM["before_text"])
    original = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, "M689", PLAN["created_at"])
    assert before == original
    assert after == repair.runner.load_yaml(ITEM["after_text"])
    assert claims == ITEM["claims"] and lineage == ITEM["lineage"]
    result = audit.check(before, after, ITEM)
    assert result["old_quantity_slots"] == 11 and result["source_rows"] == 47
    assert result["stock_dose_basis_corrections"] == 4
    assert result["unsupported_quantity_slots_removed"] == 6


@pytest.mark.parametrize(
    "mutation",
    [
        "batch_rate",
        "resazurin_mass",
        "dose_mass",
        "dose_absolute",
        "trace_dose",
        "acid_dose",
        "acid_strength",
        "percent_basis",
        "vitamin_scope",
        "vitamin_preparation",
        "mineral_preparation",
        "mineral_extra",
        "mineral_missing",
        "chemical_form",
        "annotation",
        "history",
        "quote",
        "year",
        "final_volume",
        "titrant",
        "gas",
        "missing_claim",
        "duplicate_evidence",
    ],
)
def test_independent_audit_rejects_unreviewed_changes(mutation):
    item = copy.deepcopy(ITEM)
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    acid = after["solutions"][0]["solutions"][0]
    if mutation == "batch_rate":
        after["ingredients"][2]["concentration"] = {"value": "2", "unit": "G_PER_L"}
    elif mutation == "resazurin_mass":
        n = after["ingredients"][1]
        n["notes"] = n["notes"].replace("0.5 mg", "0.5 g")
    elif mutation in {"dose_mass", "dose_absolute"}:
        after["solutions"][0]["concentration"]["unit"] = (
            "G_PER_L" if mutation == "dose_mass" else "L"
        )
    elif mutation == "trace_dose":
        after["solutions"][2]["concentration"]["value"] = "10"
    elif mutation == "acid_dose":
        acid["concentration"]["unit"] = "ML_PER_L"
    elif mutation == "acid_strength":
        acid["composition"][0]["concentration"]["value"] = "25"
    elif mutation == "percent_basis":
        acid["composition"][0]["concentration"] = {"value": "25", "unit": "PERCENT_W_V"}
    elif mutation == "vitamin_scope":
        after["solutions"][3]["composition"] = copy.deepcopy(after["solutions"][2]["composition"])
    elif mutation == "vitamin_preparation":
        after["solutions"][3]["preparation_notes"] = "Autoclave vitamins."
    elif mutation == "mineral_preparation":
        after["solutions"][2]["preparation_notes"] = "Adjust the receiving medium to pH 6.5."
    elif mutation == "mineral_extra":
        after["solutions"][2]["composition"].append(copy.deepcopy(after["ingredients"][0]))
    elif mutation == "mineral_missing":
        after["solutions"][2]["composition"].pop()
    elif mutation == "chemical_form":
        after["solutions"][0]["composition"][1]["preferred_term"] = "FeCl2"
    elif mutation == "annotation":
        after["ingredients"][0]["term"]["id"] = "CHEBI:0000000"
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "overwritten"
    elif mutation == "quote":
        after["ingredients"][1]["evidence"][0]["snippet"] = "fabricated"
    elif mutation == "year":
        after["references"][0]["year"] = 2026
    elif mutation == "final_volume":
        after["preparation_steps"][0]["description"] = "Make up the final medium to one liter."
    elif mutation == "titrant":
        after["ingredients"][6]["concentration"] = {"value": "0", "unit": "G_PER_L"}
    elif mutation == "gas":
        after["ingredients"][5]["concentration"] = {"value": "1", "unit": "G_PER_L"}
    elif mutation == "missing_claim":
        item["claims"] = [
            c for c in item["claims"] if c["old_pointer"] != ["ingredients", 0, "concentration"]
        ]
    elif mutation == "duplicate_evidence":
        after["evidence"].append(copy.deepcopy(after["evidence"][0]))
    with pytest.raises((AssertionError, KeyError)):
        audit.check(before, after, item)


def fixture_repo(tmp_path, monkeypatch):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    target = tmp_path / ITEM["path"]
    target.parent.mkdir(parents=True)
    target.write_text(ITEM["before_text"])
    subprocess.run(["git", "add", "data"], cwd=tmp_path, check=True)
    original = subprocess.check_output

    def output(args, **kwargs):
        return (
            PLAN["commit"] + "\n"
            if args == ["git", "rev-parse", "HEAD"]
            else original(args, **kwargs)
        )

    monkeypatch.setattr(subprocess, "check_output", output)
    return target


def test_guarded_preview_apply_verify_noop(tmp_path, monkeypatch):
    target = fixture_repo(tmp_path, monkeypatch)
    plan = tmp_path / "plan.json"
    before = target.read_bytes()
    repair.process(tmp_path, plan, "preview")
    assert target.read_bytes() == before
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 1
    applied = target.read_bytes()
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 1
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert target.read_bytes() == applied


@pytest.mark.parametrize("mutation", ["concurrent", "forged_plan", "symlink"])
def test_fail_closed_application(tmp_path, monkeypatch, mutation):
    target = fixture_repo(tmp_path, monkeypatch)
    plan_path = tmp_path / "plan.json"
    plan, _ = repair.process(tmp_path, plan_path, "preview")
    if mutation == "concurrent":
        target.write_text(target.read_text() + "\n# concurrent edit\n")
    elif mutation == "forged_plan":
        plan["records"][0]["claims"].pop()
        plan_path.write_text(json.dumps(plan))
    else:
        elsewhere = tmp_path / "other.yaml"
        target.rename(elsewhere)
        target.symlink_to(elsewhere)
    current = target.read_bytes()
    with pytest.raises(ValueError):
        repair.process(tmp_path, plan_path, "apply")
    assert target.read_bytes() == current
