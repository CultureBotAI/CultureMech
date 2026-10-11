"""Challenge all five ingredient graphs, reducing stocks and guarded application."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_reducing_stages as repair

spec = importlib.util.spec_from_file_location("reducing_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())
ITEMS = {r["key"]: r for r in PLAN["records"]}


def records(key):
    item = copy.deepcopy(ITEMS[key])
    return (
        item,
        repair.runner.load_yaml(item["before_text"]),
        repair.runner.load_yaml(item["after_text"]),
    )


@pytest.mark.parametrize("key", ITEMS)
def test_projection_and_independent_source_audit(key):
    item, before, expected = records(key)
    original = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == original and after == expected
    assert claims == item["claims"] and lineage == item["lineage"]
    stats = audit.check(before, after, item)
    assert (
        stats["old_quantity_slots"]
        == {"M225": 20, "M229": 20, "M234": 21, "M236": 29, "M243": 23}[key]
    )
    assert stats["source_rows"] == {"M225": 45, "M229": 36, "M234": 46, "M236": 45, "M243": 50}[key]
    assert stats["quantity_corrections"] == 1
    assert (
        stats["new_quantity_slots"] == {"M225": 2, "M229": 2, "M234": 2, "M236": 3, "M243": 4}[key]
    )
    assert (
        stats["unsupported_quantity_slots_removed"]
        == {"M225": 17, "M229": 17, "M234": 18, "M236": 25, "M243": 18}[key]
    )


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "water_total",
        "water_units",
        "mass_rate",
        "stock_rate",
        "milligram",
        "dose_units",
        "trace_preparation",
        "stock_members",
        "flatten",
        "gas",
        "grounding",
        "history",
        "quote",
        "year",
        "duplicate_evidence",
        "missing_claim",
        "preparation",
        "pressure",
        "lineage",
        "foreign_grounding",
        "reducer_dose",
        "reducer_strength",
        "reducer_mass",
        "reducer_scope",
    ],
)
def test_audit_rejects_unsupported_changes(key, mutation):
    item, before, after = records(key)
    trace = next(n for n in after["solutions"] if "[M142]" in n["preferred_term"])
    reducer = next(n for n in after["solutions"] if "separately prepared" in n["preferred_term"])
    mass = after["ingredients"][1]
    resazurin = next(n for n in after["ingredients"] if n["preferred_term"] == "Resazurin")
    if mutation == "water_total":
        after["ingredients"][0]["concentration"]["value"] = "1000"
    elif mutation == "water_units":
        after["ingredients"][0]["concentration"]["unit"] = "G_PER_L"
    elif mutation in {"mass_rate", "stock_rate"}:
        node = mass if mutation == "mass_rate" else trace["composition"][1]
        node["concentration"] = {"value": "1", "unit": "G_PER_L"}
    elif mutation == "milligram":
        resazurin["notes"] = resazurin["notes"].replace(" mg.", " g.")
    elif mutation == "dose_units":
        trace["concentration"]["unit"] = "ML_PER_L"
    elif mutation == "trace_preparation":
        trace["preparation_notes"] = "Adjust receiving medium to pH 7.0."
    elif mutation == "stock_members":
        trace["composition"].pop()
    elif mutation == "flatten":
        after["ingredients"].extend(trace.pop("composition"))
    elif mutation == "gas":
        after["ingredients"][-1]["concentration"] = {"value": "0", "unit": "G_PER_L"}
    elif mutation == "grounding":
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
    elif mutation == "preparation":
        after["preparation_steps"][0]["description"] += " Stand overnight."
    elif mutation == "pressure":
        after["notes"] += "\nPressurize to 100 kPa."
    elif mutation == "lineage":
        item["lineage"].pop()
    elif mutation == "foreign_grounding":
        trace["composition"][0]["term"] = copy.deepcopy(after["ingredients"][0]["term"])
    elif mutation == "reducer_dose":
        reducer["concentration"] = {"value": "0.01", "unit": "L"}
    elif mutation == "reducer_strength":
        reducer["composition"][0]["concentration"] = {"value": "5", "unit": "PERCENT_W_V"}
    elif mutation == "reducer_mass":
        reducer["composition"][0]["notes"] = reducer["composition"][0]["notes"].replace(
            "0.5 g", "5 g"
        )
    else:
        reducer["composition"][0]["notes"] = reducer["composition"][0]["notes"].replace(
            "contribution specified for the receiving medium batch", "mass for the stock batch"
        )
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "key,mutation",
    [
        ("M229", "nacl"),
        ("M229", "nacl_history"),
        ("M236", "water3"),
        ("M243", "water3"),
        ("M236", "acid"),
        ("M236", "filter"),
        ("M236", "sulfur"),
        ("M236", "sulfur_link"),
        ("M243", "vitamins"),
        ("M225", "vitamins"),
        ("M234", "vitamins"),
    ],
)
def test_recipe_specific_scope(key, mutation):
    item, before, after = records(key)
    if mutation.startswith("nacl"):
        local = next(n for n in after["solutions"] if "Artificial" in n["preferred_term"])
        salt = next(n for n in local["composition"] if n["preferred_term"] == "NaCl")
        salt["notes"] = (
            salt["notes"].replace("27.7 g", "47.7 g")
            if mutation == "nacl"
            else salt["notes"].replace(
                "earlier duplicate-summing note is superseded", "summing note is valid"
            )
        )
    elif mutation == "water3":
        local = after["solutions"][0]
        local["composition"][0]["concentration"]["value"] = "3"
    elif mutation == "acid":
        acid = next(n for n in after["ingredients"] if n["preferred_term"] == "H2SO4")
        acid["notes"] = acid["notes"].replace(
            "later readjustment explicitly uses sterile 1 N H2SO4", "all steps use 1 M H2SO4"
        )
    elif mutation == "filter":
        after["preparation_steps"][1]["action"] = "FILTER_STERILIZE"
    elif mutation.startswith("sulfur"):
        sulfur = next(n for n in after["ingredients"] if n["preferred_term"] == "Sulfur (powder)")
        if mutation == "sulfur_link":
            sulfur.pop("mediaingredientmech_term")
        else:
            sulfur["notes"] = sulfur["notes"].replace("3 successive days", "1 day")
    else:
        vitamins = next(n for n in after["solutions"] if "[M190]" in n["preferred_term"])
        vitamins["preparation_notes"] = "Autoclave with the entire M190 medium."
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "key,source,si,ri", [("M229", "M229", 1, 2), ("M236", "M236", 2, 4), ("M243", "M243", 0, 6)]
)
@pytest.mark.parametrize("mutation", ["amount", "form", "ambiguous"])
def test_original_table_conflict_blocks_preview(key, source, si, ri, mutation):
    r = repair.Review(repair.runner.load_yaml(ITEMS[key]["before_text"]), key)
    p = r.leaf(["ingredients"], source, si, ri)
    name = r.rows(source, si)[ri]["component_name"].replace("\u30fb", "\u00b7")
    original = "JCM" + repair.NUMBERS[source]
    unit = r.rows(source, si)[ri]["unit"]
    replacement = (
        name + " 999 " + unit + (" " + name if mutation == "ambiguous" else " altered")
        if mutation != "form"
        else name + " altered"
    )
    r.data[original] = r.data[original].replace(name, replacement)
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
    assert repair.process(tmp_path, plan_path, "apply")[1]["changed"] == 5
    after = [p.read_bytes() for p in targets]
    assert repair.process(tmp_path, plan_path, "verify")[1]["already_applied"] == 5
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
