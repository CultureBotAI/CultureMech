"""Challenge both ingredient graphs, identity restoration and guarded application."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_m258_m260_stocks as repair

spec = importlib.util.spec_from_file_location("m258_m260_audit", repair.HERE / "audit.py")
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
    assert stats["old_quantity_slots"] == {"M258": 29, "M260": 18}[key]
    assert stats["source_rows"] == {"M258": 53, "M260": 33}[key]
    assert stats["quantity_corrections"] == 1
    assert stats["new_quantity_slots"] == {"M258": 3, "M260": 2}[key]


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
        "duplicate_note",
    ],
)
def test_audit_rejects_unsupported_changes(key, mutation):
    item, before, after = records(key)
    trace = next(
        n
        for _, n in audit.walk(after)
        if n.get("preferred_term") == "Trace minerals (see Medium [M142])"
    )
    mass = after["ingredients"][1]
    if mutation == "water_total":
        after["ingredients"][0]["concentration"]["value"] = "1000"
    elif mutation == "water_units":
        after["ingredients"][0]["concentration"]["unit"] = "G_PER_L"
    elif mutation in {"mass_rate", "stock_rate"}:
        node = mass if mutation == "mass_rate" else trace["composition"][1]
        node["concentration"] = {"value": "1", "unit": "G_PER_L"}
    elif mutation == "milligram":
        node = (
            next(
                n
                for _, n in audit.walk(after)
                if "Source batch input: 0.5 mg." in n.get("notes", "")
            )
            if key == "M260"
            else after["ingredients"][3]
        )
        node["notes"] = node["notes"].replace(" mg.", " g.")
    elif mutation == "dose_units":
        trace["concentration"]["unit"] = "ML_PER_L"
    elif mutation == "trace_preparation":
        trace["preparation_notes"] = "Adjust receiving medium to pH 7.0."
    elif mutation == "stock_members":
        trace["composition"].pop()
    elif mutation == "flatten":
        after["ingredients"].extend(trace.pop("composition"))
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
    else:
        after["ingredients"][0]["notes"] = after["ingredients"][0]["notes"].replace(
            "earlier duplicate-summing note is superseded", "summing note is valid"
        )
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "mutation",
    [
        "lb_returned",
        "alpha_removed",
        "alpha_identity",
        "alpha_amount",
        "old_provenance",
        "rumen_double_dose",
        "rumen_force",
        "naoh_dose",
        "naoh_strength",
        "fatty_ph",
        "reducer_dose",
        "reducer_strength",
        "reducer_mass",
        "reducer_scope",
        "vitamins",
        "gas",
    ],
)
def test_m258_identity_and_preparation_boundaries(mutation):
    item, before, after = records("M258")
    fatty, rumen, reducer = after["solutions"][3], after["solutions"][0], after["solutions"][4]
    if mutation == "lb_returned":
        after["ingredients"].append(copy.deepcopy(before["ingredients"][23]))
    elif mutation == "alpha_removed":
        fatty["composition"].pop()
    elif mutation == "alpha_identity":
        fatty["composition"][4]["term"] = {"id": "CHEBI:37070", "label": "2-methylbutyric acid"}
    elif mutation == "alpha_amount":
        fatty["composition"][4]["notes"] = fatty["composition"][4]["notes"].replace("0.5 g", "5 g")
    elif mutation == "old_provenance":
        after["notes"] = after["notes"].replace(
            "Superseded historical provenance (not a current formulation claim):", ""
        )
    elif mutation == "rumen_double_dose":
        rumen["composition"][0]["concentration"] = {"value": "0.3", "unit": "L"}
    elif mutation == "rumen_force":
        rumen["preparation_notes"] = rumen["preparation_notes"].replace("25,000 x g", "25,000 rpm")
    elif mutation in {"naoh_dose", "naoh_strength"}:
        fatty["solutions"][0]["concentration"] = {
            "value": "1",
            "unit": "L" if mutation == "naoh_dose" else "MOLAR",
        }
    elif mutation == "fatty_ph":
        fatty["preparation_notes"] = "Adjust main medium to pH 7.5."
    elif mutation == "reducer_dose":
        reducer["concentration"] = {"value": "0.01", "unit": "L"}
    elif mutation == "reducer_strength":
        reducer["composition"][0]["concentration"] = {"value": "5", "unit": "PERCENT_W_V"}
    elif mutation == "reducer_mass":
        reducer["composition"][0]["notes"] = reducer["composition"][0]["notes"].replace(
            "0.5 g", "5 g"
        )
    elif mutation == "reducer_scope":
        reducer["composition"][0]["notes"] = reducer["composition"][0]["notes"].replace(
            "contribution specified for the receiving medium batch", "mass for preparing stock"
        )
    elif mutation == "vitamins":
        after["solutions"][2]["preparation_notes"] = "Autoclave with entire M190 medium."
    else:
        after["ingredients"][-1]["concentration"] = {"value": "0", "unit": "G_PER_L"}
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "mutation", ["trace_root", "trace_dose", "stock_water", "borrowed_preparation"]
)
def test_m260_nested_seawater_boundary(mutation):
    item, before, after = records("M260")
    seawater = after["solutions"][0]
    if mutation == "trace_root":
        after["solutions"].extend(seawater.pop("solutions"))
    elif mutation == "trace_dose":
        seawater["solutions"][0]["concentration"]["value"] = "0.001"
    elif mutation == "stock_water":
        seawater["composition"][0]["concentration"]["value"] = "0.1"
    else:
        seawater["preparation_notes"] = "Stand overnight under hydrogen."
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize("key,source,si,ri", [("M258", "M258", 2, 4), ("M260", "M260", 1, 7)])
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
