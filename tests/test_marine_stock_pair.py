"""Guard deaggregation, source units, stock membership and evidence for M208/M209."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_marine_stock_pair as repair

spec = importlib.util.spec_from_file_location("marine_pair_audit", repair.HERE / "audit.py")
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
    assert stats["old_quantity_slots"] == {"M208": 30, "M209": 31}[key]
    assert stats["source_rows"] == {"M208": 45, "M209": 57}[key]
    assert stats["quantity_corrections"] == 1
    assert stats["new_quantity_slots"] == {"M208": 2, "M209": 3}[key]
    assert stats["stock_nodes_relocated"] == {"M208": 14, "M209": 9}[key]


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "main_water_total",
        "main_water_unit",
        "stock_water_total",
        "stock_water_unit",
        "water_history",
        "main_rate",
        "stock_rate",
        "milligram_mass",
        "stock_dose_mass",
        "stock_dose_rate",
        "trace_amount",
        "trace_preparation",
        "missing_stock_row",
        "extra_stock_row",
        "flatten_stock",
        "gas",
        "normality",
        "annotation",
        "history",
        "quote",
        "year",
        "duplicate_evidence",
        "missing_claim",
        "atmosphere",
        "filtration",
        "pressure",
        "extra_root",
        "water_lineage",
        "foreign_grounding",
    ],
)
def test_independent_audit_rejects_unsupported_changes(key, mutation):
    item = copy.deepcopy(ITEMS[key])
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    local = after["solutions"][0 if key == "M208" else 1]
    trace = after["solutions"][1 if key == "M208" else 0]
    water = after["ingredients"][0]
    mass = after["ingredients"][1]
    iodide = next(n for n in local["composition"] if n["preferred_term"] == "KI")
    acid = next(n for n in after["ingredients"] if n["preferred_term"] == "H2SO4")
    if mutation in {"main_water_total", "stock_water_total"}:
        node = water if mutation.startswith("main") else local["composition"][0]
        node["concentration"]["value"] = "866" if key == "M208" else "971"
    elif mutation in {"main_water_unit", "stock_water_unit"}:
        node = water if mutation.startswith("main") else local["composition"][0]
        node["concentration"]["unit"] = "G_PER_L"
    elif mutation == "water_history":
        water["notes"] = "Source batch input only"
    elif mutation in {"main_rate", "stock_rate"}:
        node = mass if mutation == "main_rate" else iodide
        node["concentration"] = {"value": "1", "unit": "G_PER_L"}
    elif mutation == "milligram_mass":
        iodide["notes"] = iodide["notes"].replace(" mg.", " g.")
    elif mutation in {"stock_dose_mass", "stock_dose_rate"}:
        local["concentration"]["unit"] = "G_PER_L" if mutation.endswith("mass") else "ML_PER_L"
    elif mutation == "trace_amount":
        trace["composition"][1]["notes"] = trace["composition"][1]["notes"].replace("3 g.", "30 g.")
    elif mutation == "trace_preparation":
        trace["preparation_notes"] = "Adjust receiving medium to pH 7.0."
    elif mutation == "missing_stock_row":
        local["composition"].pop()
    elif mutation == "extra_stock_row":
        local["composition"].append(copy.deepcopy(mass))
    elif mutation == "flatten_stock":
        after["ingredients"].extend(local.pop("composition"))
    elif mutation == "gas":
        after["ingredients"][-1]["concentration"] = {"value": "0", "unit": "G_PER_L"}
    elif mutation == "normality":
        acid["concentration"] = {"value": "1", "unit": "MOLAR"}
    elif mutation == "annotation":
        mass["term"]["id"] = "CHEBI:0000000"
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "overwritten"
    elif mutation == "quote":
        mass["evidence"][0]["snippet"] = "invented"
    elif mutation == "year":
        after["references"][0]["year"] = 2026
    elif mutation == "duplicate_evidence":
        after["evidence"].append(copy.deepcopy(after["evidence"][0]))
    elif mutation == "missing_claim":
        item["claims"] = [
            c for c in item["claims"] if c["old_pointer"] != ["ingredients", 0, "concentration"]
        ]
    elif mutation == "atmosphere":
        after["preparation_steps"][1]["description"] += " Use air instead."
    elif mutation == "filtration":
        after["preparation_steps"][0 if key == "M208" else 1]["action"] = "FILTER_STERILIZE"
    elif mutation == "pressure":
        after["notes"] += "\nPressurize to 100 kPa."
    elif mutation == "water_lineage":
        item["lineage"] = [n for n in item["lineage"] if n["pointer"] != ["ingredients", 0]]
    elif mutation == "foreign_grounding":
        trace["composition"][0]["term"] = copy.deepcopy(water["term"])
    else:
        after["parent_media"] = {"id": "CultureMech:008584"}
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "key,mutation",
    [
        ("M208", "normalize_ratio"),
        ("M208", "normalize_formula"),
        ("M208", "lose_conflict"),
        ("M208", "lose_acid_strength"),
        ("M208", "inherit_sulfide"),
        ("M209", "inherit_acid_strength"),
        ("M209", "sulfide_dose"),
        ("M209", "sulfide_strength"),
        ("M209", "sulfide_mass"),
        ("M209", "single_ph"),
        ("M209", "vitamin_preparation"),
        ("M209", "vitamin_mixup"),
        ("M209", "legacy_flag"),
        ("M209", "legacy_mim"),
    ],
)
def test_recipe_specific_boundaries(key, mutation):
    item = ITEMS[key]
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    acid = next(n for n in after["ingredients"] if n["preferred_term"] == "H2SO4")
    if mutation == "normalize_ratio":
        after["preparation_steps"][1]["description"] = after["preparation_steps"][1][
            "description"
        ].replace("80:20:1", "79.2:19.8:1")
    elif mutation == "normalize_formula":
        after["ingredients"][4]["preferred_term"] = "Na2WO4\u30fb2H2O"
    elif mutation == "lose_conflict":
        after["ingredients"][4]["notes"] = after["ingredients"][4]["notes"].replace(
            "formula discrepancy is unresolved", "grounding verified"
        )
    elif mutation == "lose_acid_strength":
        acid["notes"] = acid["notes"].replace("1 N H2SO4", "H2SO4")
    elif mutation == "inherit_acid_strength":
        acid["notes"] += " 1 N H2SO4"
    elif mutation == "inherit_sulfide":
        after["solutions"].append({"preferred_term": "Sulfide solution", "composition": []})
    elif mutation == "sulfide_dose":
        after["solutions"][3]["concentration"] = {"value": "0.01", "unit": "L"}
    elif mutation == "sulfide_strength":
        after["solutions"][3]["composition"][0]["concentration"] = {
            "value": "5",
            "unit": "PERCENT_W_V",
        }
    elif mutation == "sulfide_mass":
        n = after["solutions"][3]["composition"][0]
        n["notes"] = n["notes"].replace("0.5 g", "5 g")
    elif mutation == "single_ph":
        after["preparation_steps"][3]["description"] = after["preparation_steps"][3][
            "description"
        ].replace("6.5", "6.0")
    elif mutation == "vitamin_preparation":
        after["solutions"][2]["preparation_notes"] = "Autoclave with medium JCM197."
    elif mutation == "vitamin_mixup":
        after["solutions"][2]["composition"] = copy.deepcopy(after["solutions"][0]["composition"])
    elif mutation == "legacy_mim":
        after["solutions"][1]["composition"][2].pop("mediaingredientmech_term")
    else:
        after["high_metal"] = False
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "key,source,si,ri", [("M208", "M208", 1, 8), ("M209", "M209", 1, 2), ("M209", "M190", 1, 7)]
)
@pytest.mark.parametrize("mutation", ["amount", "ambiguous", "form"])
def test_original_table_disagreement_blocks_preview(key, source, si, ri, mutation):
    r = repair.Review(repair.runner.load_yaml(ITEMS[key]["before_text"]), key)
    p = r.leaf(["ingredients"], source, si, ri)
    original = "JCM" + repair.NUMBERS[source]
    name = r.rows(source, si)[ri]["component_name"].replace("\u30fb", "\u00b7")
    r.data[original] = r.data[original].replace(
        name, name + " 999 mg " + name if mutation == "ambiguous" else name + " altered"
    )
    if mutation == "amount":
        r.data[original] = (
            r.data[original]
            .replace(name + " altered", name)
            .replace({"M208": "8.1 mg", "M209": "40.0 mg", "M190": "0.1 mg"}[source], "999 mg")
        )
    with pytest.raises(ValueError):
        r.original_amount(p, source, si, ri)


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
    assert repair.process(tmp_path, plan_path, "apply")[1]["changed"] == 2
    after = [p.read_bytes() for p in targets]
    assert repair.process(tmp_path, plan_path, "verify")[1]["already_applied"] == 2
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
