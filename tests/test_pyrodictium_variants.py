"""Source, duplicate-dose and variant-boundary regression tests."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_pyrodictium_variants as repair

spec = importlib.util.spec_from_file_location("pyrodictium_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())
ITEMS = {r["key"]: r for r in PLAN["records"]}


@pytest.mark.parametrize("key", ITEMS)
def test_projection_and_source_audit(key):
    item = ITEMS[key]
    before = repair.runner.load_yaml(item["before_text"])
    original = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == original
    assert after == repair.runner.load_yaml(item["after_text"])
    assert claims == item["claims"] and lineage == item["lineage"]
    stats = audit.check(before, after, item)
    assert stats["old_quantity_slots"] == (10 if key == "M197" else 11)
    assert stats["source_rows"] == {"M196": 38, "M197": 36, "M198": 37}[key]
    assert stats["stock_dose_basis_corrections"] == 3


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "resazurin_rate",
        "resazurin_mass",
        "dose_mass",
        "base_rate",
        "trace_rate",
        "sulfide_absolute",
        "sulfide_double",
        "percent_basis",
        "stock_mass_rate",
        "stock_extra",
        "stock_missing",
        "stock_preparation",
        "gas",
        "chemical_annotation",
        "history",
        "quote",
        "year",
        "duplicate_evidence",
        "missing_claim",
        "wrong_atmosphere",
    ],
)
def test_independent_audit_rejects_unreviewed_changes(key, mutation):
    item = copy.deepcopy(ITEMS[key])
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    if mutation == "resazurin_rate":
        after["ingredients"][0]["concentration"] = {"value": "1", "unit": "MG_PER_L"}
    elif mutation == "resazurin_mass":
        n = after["ingredients"][0]
        n["notes"] = n["notes"].replace("1 mg", "1 g")
    elif mutation == "dose_mass":
        after["solutions"][2]["concentration"]["unit"] = "G_PER_L"
    elif mutation == "base_rate":
        after["solutions"][0]["concentration"] = {"value": "1000", "unit": "ML_PER_L"}
    elif mutation == "trace_rate":
        after["solutions"][1]["concentration"] = {"value": "10", "unit": "ML_PER_L"}
    elif mutation == "sulfide_absolute":
        after["solutions"][2]["concentration"] = {"value": "0.01", "unit": "L"}
    elif mutation == "sulfide_double":
        after["solutions"][2]["concentration"]["value"] = "20"
    elif mutation == "percent_basis":
        after["solutions"][2]["composition"] = [
            {"preferred_term": "Na2S", "concentration": {"value": "5", "unit": "PERCENT_W_V"}}
        ]
    elif mutation == "stock_mass_rate":
        after["solutions"][0]["composition"][1]["concentration"] = {
            "value": "3.5",
            "unit": "G_PER_L",
        }
    elif mutation == "stock_extra":
        after["solutions"][0]["composition"].append(copy.deepcopy(after["ingredients"][0]))
    elif mutation == "stock_missing":
        after["solutions"][1]["composition"].pop()
    elif mutation == "stock_preparation":
        after["solutions"][1]["preparation_notes"] = "Adjust the receiving medium to pH 7.0."
    elif mutation == "gas":
        after["ingredients"][-1]["concentration"] = {"value": "0", "unit": "G_PER_L"}
    elif mutation == "chemical_annotation":
        after["ingredients"][0]["term"]["id"] = "CHEBI:0000000"
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "overwritten"
    elif mutation == "quote":
        after["ingredients"][0]["evidence"][0]["snippet"] = "invented"
    elif mutation == "year":
        after["references"][0]["year"] = 2026
    elif mutation == "duplicate_evidence":
        after["evidence"].append(copy.deepcopy(after["evidence"][0]))
    elif mutation == "missing_claim":
        item["claims"] = [
            c for c in item["claims"] if c["old_pointer"] != ["ingredients", 0, "concentration"]
        ]
    elif mutation == "wrong_atmosphere":
        step = after["preparation_steps"][2]
        step["description"] = step["description"].replace("H2-CO2", "H2-CO4")
    with pytest.raises((AssertionError, KeyError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "key,mutation",
    [
        ("M196", "duplicate_stock"),
        ("M196", "duplicate_annotation"),
        ("M196", "parent_yeast_rate"),
        ("M196", "self_child"),
        ("M196", "missing_child"),
        ("M197", "wrong_parent"),
        ("M197", "parent_yeast"),
        ("M198", "parent_yeast"),
        ("M198", "tungstate_unit"),
        ("M198", "tungstate_hydrate"),
        ("M198", "citric_acid"),
        ("M198", "omission_lost"),
    ],
)
def test_variant_and_duplicate_specific_failures(key, mutation):
    item = ITEMS[key]
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    if mutation == "duplicate_stock":
        after["solutions"].append(copy.deepcopy(after["solutions"][2]))
    elif mutation == "duplicate_annotation":
        after["solutions"][2]["notes"] = "Consolidated without retaining the old annotation."
    elif mutation == "parent_yeast_rate":
        after["ingredients"][2]["concentration"] = {"value": "2", "unit": "G_PER_L"}
    elif mutation == "self_child":
        after["variant_children"][0]["id"] = before["id"]
    elif mutation == "missing_child":
        after["variant_children"].pop()
    elif mutation == "wrong_parent":
        after["parent_media"]["path"] = ITEMS["M198"]["path"]
    elif mutation == "parent_yeast":
        next(n for n in after["ingredients"] if n["preferred_term"] == "Yeast extract (BD-Difco)")[
            "concentration"
        ]["value"] = "2"
    elif mutation == "tungstate_unit":
        after["ingredients"][1]["concentration"]["unit"] = "G_PER_L"
    elif mutation == "tungstate_hydrate":
        after["ingredients"][1]["preferred_term"] = "Na2WO4"
    elif mutation == "citric_acid":
        after["ingredients"].append(
            {"preferred_term": "Citric acid", "concentration": {"value": "0", "unit": "G_PER_L"}}
        )
    elif mutation == "omission_lost":
        after["variant_modifications"].pop()
    with pytest.raises((AssertionError, KeyError, IndexError)):
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
    before = [p.read_bytes() for p in targets]
    repair.process(tmp_path, plan, "preview")
    assert [p.read_bytes() for p in targets] == before
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 3
    after = [p.read_bytes() for p in targets]
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 3
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert [p.read_bytes() for p in targets] == after


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
    current = [p.read_bytes() for p in targets]
    with pytest.raises(ValueError):
        repair.process(tmp_path, plan_path, "apply")
    assert [p.read_bytes() for p in targets] == current
