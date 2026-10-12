"""Guard source-specific stock rates, sulfide stages, and evidence preservation."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_filtered_sulfide_media as repair

spec = importlib.util.spec_from_file_location("filtered_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())
ITEMS = {r["key"]: r for r in PLAN["records"]}


@pytest.mark.parametrize("key", ITEMS)
def test_projection_and_independent_source_audit(key):
    item = ITEMS[key]
    before = repair.runner.load_yaml(item["before_text"])
    original = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == original and after == repair.runner.load_yaml(item["after_text"])
    assert claims == item["claims"] and lineage == item["lineage"]
    stats = audit.check(before, after, item)
    assert stats["old_quantity_slots"] == {"M199": 23, "M206": 19, "M207": 21}[key]
    assert stats["source_rows"] == {"M199": 37, "M206": 33, "M207": 35}[key]
    assert stats["stock_nodes_relocated"] == (13 if key == "M199" else 1)


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "main_rate",
        "main_mass",
        "dose_mass",
        "dose_per_liter",
        "sulfide_dose",
        "sulfide_strength",
        "sulfide_mass",
        "stock_water_rate",
        "stock_mass_rate",
        "stock_missing",
        "stock_extra",
        "stock_preparation",
        "gas",
        "annotation",
        "history",
        "quote",
        "year",
        "duplicate_evidence",
        "missing_claim",
        "wrong_atmosphere",
        "wrong_filtration",
        "pressure",
        "root_extra",
    ],
)
def test_independent_audit_rejects_unsupported_changes(key, mutation):
    item = copy.deepcopy(ITEMS[key])
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    trace = after["solutions"][1 if key == "M199" else 0]
    sulfide = after["solutions"][-1]
    resazurin = next(n for n in after["ingredients"] if n["preferred_term"] == "Resazurin")
    if mutation == "main_rate":
        resazurin["concentration"] = {"value": "1", "unit": "MG_PER_L"}
    elif mutation == "main_mass":
        resazurin["notes"] = resazurin["notes"].replace("1 mg", "1 g")
    elif mutation == "dose_mass":
        trace["concentration"]["unit"] = "G_PER_L"
    elif mutation == "dose_per_liter":
        trace["concentration"] = {"value": "10", "unit": "ML_PER_L"}
    elif mutation == "sulfide_dose":
        sulfide["concentration"] = {"value": "10", "unit": "ML_PER_L"}
    elif mutation == "sulfide_strength":
        sulfide["composition"][0]["concentration"] = {"value": "5", "unit": "PERCENT_W_V"}
    elif mutation == "sulfide_mass":
        n = sulfide["composition"][0]
        n["notes"] = n["notes"].replace("0.5 g", "5 g")
    elif mutation == "stock_water_rate":
        trace["composition"][0]["concentration"] = {"value": "1000", "unit": "ML_PER_L"}
    elif mutation == "stock_mass_rate":
        trace["composition"][1]["concentration"] = {"value": "3", "unit": "G_PER_L"}
    elif mutation == "stock_missing":
        trace["composition"].pop()
    elif mutation == "stock_extra":
        trace["composition"].append(copy.deepcopy(resazurin))
    elif mutation == "stock_preparation":
        trace["preparation_notes"] = "Adjust receiving medium to pH 7.0."
    elif mutation == "gas":
        after["ingredients"][-1]["concentration"] = {"value": "0", "unit": "G_PER_L"}
    elif mutation == "annotation":
        resazurin["term"]["id"] = "CHEBI:0000000"
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "overwritten"
    elif mutation == "quote":
        resazurin["evidence"][0]["snippet"] = "invented"
    elif mutation == "year":
        after["references"][0]["year"] = 2026
    elif mutation == "duplicate_evidence":
        after["evidence"].append(copy.deepcopy(after["evidence"][0]))
    elif mutation == "missing_claim":
        item["claims"] = [
            c for c in item["claims"] if c["old_pointer"] != ["ingredients", 0, "concentration"]
        ]
    elif mutation == "wrong_atmosphere":
        after["preparation_steps"][1]["description"] += " Use air instead."
    elif mutation == "wrong_filtration":
        after["preparation_steps"][1]["action"] = "AUTOCLAVE"
    elif mutation == "pressure":
        after["notes"] += "\nPressurize all media to 200 kPa."
    else:
        after["parent_media"] = {"id": "CultureMech:008584"}
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "key,mutation",
    [
        ("M199", "iodide_unit"),
        ("M199", "iodide_parent_rate"),
        ("M199", "salt_parent_rate"),
        ("M199", "stock_flattened"),
        ("M206", "acid_strength_lost"),
        ("M206", "water_final_volume"),
        ("M207", "acid_strength_inherited"),
        ("M207", "sulfide_strength_inherited"),
    ],
)
def test_recipe_specific_boundaries(key, mutation):
    item = ITEMS[key]
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    if mutation.startswith("iodide"):
        node = after["solutions"][0]["composition"][10]
        node["concentration"]["unit" if mutation == "iodide_unit" else "value"] = (
            "G_PER_L" if mutation == "iodide_unit" else "0.05"
        )
    elif mutation == "salt_parent_rate":
        after["solutions"][0]["composition"][2]["concentration"]["value"] = "13.85"
    elif mutation == "stock_flattened":
        after["ingredients"].extend(after["solutions"][0].pop("composition"))
    elif mutation.startswith("acid_strength"):
        acid = next(n for n in after["ingredients"] if n["preferred_term"] == "H2SO4")
        acid["notes"] = (
            acid["notes"].replace("1 N H2SO4", "H2SO4")
            if key == "M206"
            else acid["notes"] + " 1 N H2SO4"
        )
    elif mutation == "water_final_volume":
        after["ingredients"][0]["concentration"] = {"value": "1", "unit": "L"}
    else:
        after["solutions"][-1]["preparation_notes"] = repair.STEPS["M206"][2][1]
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize("mutation", ["amount", "ambiguous"])
def test_original_table_disagreement_blocks_preview(mutation):
    r = repair.Review(repair.runner.load_yaml(ITEMS["M206"]["before_text"]), "M206")
    text = r.data["JCM213"]
    replacement = (
        "Resazurin 2.0 mg" if mutation == "amount" else "Resazurin 1.0 mg Resazurin 1.0 mg"
    )
    r.data["JCM213"] = text.replace("Resazurin 1.0 mg", replacement)
    with pytest.raises(ValueError):
        r.direct(6)


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


def test_guarded_apply_verify_and_noop(tmp_path, monkeypatch):
    targets = fixture_repo(tmp_path, monkeypatch)
    plan_path = tmp_path / "plan.json"
    before = [p.read_bytes() for p in targets]
    repair.process(tmp_path, plan_path, "preview")
    assert [p.read_bytes() for p in targets] == before
    assert repair.process(tmp_path, plan_path, "apply")[1]["changed"] == 3
    after = [p.read_bytes() for p in targets]
    assert repair.process(tmp_path, plan_path, "verify")[1]["already_applied"] == 3
    assert repair.process(tmp_path, plan_path, "apply")[1]["changed"] == 0
    assert [p.read_bytes() for p in targets] == after


@pytest.mark.parametrize("mutation", ["concurrent", "forged_plan", "symlink"])
def test_all_target_guards_before_any_write(tmp_path, monkeypatch, mutation):
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
