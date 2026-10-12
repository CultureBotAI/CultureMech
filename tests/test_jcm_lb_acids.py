"""Challenge three ingredient graphs, liquid inputs and identity restoration and guarded application."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_jcm_lb_acids as repair

spec = importlib.util.spec_from_file_location("jcm_lb_acids_audit", repair.HERE / "audit.py")
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
    assert stats["old_quantity_slots"] == {"J266": 38, "J675": 16, "J1203": 19}[key]
    assert stats["source_rows"] == {"J266": 47, "J675": 20, "J1203": 18}[key]
    assert stats["new_quantity_slots"] == {"J266": 12, "J675": 8, "J1203": 2}[key]


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "water_total",
        "water_units",
        "mass_rate",
        "lb_returned",
        "genuine_removed",
        "grounding",
        "history",
        "quote",
        "year",
        "duplicate_evidence",
        "missing_claim",
        "preparation",
        "provenance",
        "lineage",
        "ph",
        "acid_removed",
        "acid_grounding",
        "acid_amount",
        "dose_units",
        "stock_members",
    ],
)
def test_audit_rejects_unsupported_changes(key, mutation):
    item, before, after = records(key)
    nodes = [
        n
        for p, n in audit.walk(after)
        if p[-2:-1] in {("ingredients",), ("composition",)} and "preferred_term" in n
    ]
    water = next(n for n in nodes if n["preferred_term"] == "Distilled water")
    acid = next(n for n in nodes if "Methylbutyric" in n["preferred_term"])
    mass = next(n for n in after["ingredients"] if "Source batch input:" in n.get("notes", ""))
    if mutation == "water_total":
        water["concentration"]["value"] = "999"
    elif mutation == "water_units":
        water["concentration"]["unit"] = "G_PER_L"
    elif mutation == "mass_rate":
        mass["concentration"] = {"value": "1", "unit": "G_PER_L"}
    elif mutation == "lb_returned":
        after["ingredients"].append(copy.deepcopy(before["ingredients"][repair.LB[key][0]]))
    elif mutation == "genuine_removed":
        after["ingredients"].remove(
            next(n for n in after["ingredients"] if n["preferred_term"] == "Yeast extract")
        )
    elif mutation == "grounding":
        next(n for n in nodes if "term" in n)["term"]["id"] = "CHEBI:0000000"
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
        after["preparation_steps"][0]["description"] += " Add 1 L water."
    elif mutation == "provenance":
        after["notes"] = after["notes"].replace(
            "Superseded historical provenance (not a current formulation claim):", ""
        )
    elif mutation == "lineage":
        item["lineage"].pop()
    elif mutation == "ph":
        after["ph_value"] = 7.5
    elif mutation == "acid_removed":
        acid["preferred_term"] = "LB Broth"
    elif mutation == "acid_grounding":
        acid["term"] = {"id": "CHEBI:37070", "label": "2-methylbutyric acid"}
    elif mutation == "acid_amount":
        acid["concentration"]["value"] = "999"
    elif mutation == "dose_units":
        next(n for n in after["solutions"] if "concentration" in n)["concentration"][
            "unit"
        ] = "ML_PER_L"
    else:
        next(n for n in after["solutions"] if n["composition"])["composition"].pop()
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "mutation",
    [
        "merged_main",
        "trace_rate",
        "trace_preparation",
        "fatty_ph",
        "reducer_dose",
        "reducer_basis",
        "reducer_batch",
        "rumen_double_dose",
        "metadata_conflict",
    ],
)
def test_j266_stock_stage_and_ph(mutation):
    item, before, after = records("J266")
    trace, fatty, reducer = after["solutions"][1], after["solutions"][3], after["solutions"][4]
    if mutation == "merged_main":
        next(n for n in after["ingredients"] if n["preferred_term"] == "NaCl")[
            "notes"
        ] += " Source batch input: 1.6 g."
    elif mutation == "trace_rate":
        trace["composition"][1]["concentration"]["value"] = "0.13"
    elif mutation == "trace_preparation":
        trace["preparation_notes"] = "Adjust main medium to pH 7.0."
    elif mutation == "fatty_ph":
        fatty["preparation_notes"] = "Adjust main medium to pH 7.5."
    elif mutation == "reducer_dose":
        reducer["concentration"] = {"value": "0.01", "unit": "L"}
    elif mutation == "reducer_basis":
        reducer["composition"][0]["concentration"] = {"value": "5", "unit": "PERCENT_W_V"}
    elif mutation == "reducer_batch":
        reducer["composition"][0]["notes"] = reducer["composition"][0]["notes"].replace(
            "contribution specified for the receiving medium batch", "mass for making stock"
        )
    elif mutation == "rumen_double_dose":
        after["solutions"][0]["composition"].append(
            {"preferred_term": "Rumen fluid", "concentration": {"value": "0.3", "unit": "L"}}
        )
    else:
        after["notes"] = after["notes"].replace(
            "API metadata min_pH/max_pH 7.5 conflicts", "API metadata 7.5 is final pH"
        )
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "mutation", ["late_missing", "late_units", "fatty_dose", "acid_density", "genuine_tryptone"]
)
def test_j675_late_inputs_and_liquid_acids(mutation):
    item, before, after = records("J675")
    if mutation == "late_missing":
        after["ingredients"].pop()
    elif mutation == "late_units":
        after["ingredients"][-1]["notes"] = after["ingredients"][-1]["notes"].replace(
            "500 mg", "500 g"
        )
    elif mutation == "fatty_dose":
        after["solutions"][2]["concentration"]["value"] = "1"
    elif mutation == "acid_density":
        after["solutions"][2]["composition"][0]["concentration"] = {
            "value": "10",
            "unit": "G_PER_L",
        }
    else:
        after["ingredients"][0]["notes"] = after["ingredients"][0]["notes"].replace("5 g", "10 g")
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "mutation",
    [
        "resazurin_percent",
        "resazurin_mass",
        "glucose_dose",
        "glucose_stock_rate",
        "legacy_link",
        "water_final",
    ],
)
def test_j1203_ambiguous_strength_and_separate_glucose(mutation):
    item, before, after = records("J1203")
    resazurin, glucose = after["solutions"]
    if mutation == "resazurin_percent":
        resazurin["composition"][0]["concentration"] = {"value": "0.05", "unit": "PERCENT_W_V"}
    elif mutation == "resazurin_mass":
        resazurin["concentration"] = {"value": "1", "unit": "G_PER_L"}
    elif mutation == "glucose_dose":
        glucose["concentration"] = {"value": "0.01", "unit": "L"}
    elif mutation == "glucose_stock_rate":
        glucose["composition"][0]["concentration"] = {"value": "2", "unit": "G_PER_L"}
    elif mutation == "legacy_link":
        next(n for n in after["ingredients"] if n["preferred_term"] == "iso-Valeric acid").pop(
            "mediaingredientmech_term"
        )
    else:
        next(n for n in after["ingredients"] if n["preferred_term"] == "Distilled water")[
            "concentration"
        ]["value"] = "1.002"
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize("key,si,ri", [("J266", 1, 2), ("J675", 3, 2), ("J1203", 0, 10)])
@pytest.mark.parametrize("mutation", ["amount", "unit"])
def test_source_amount_disagreement_blocks_preview(key, si, ri, mutation):
    r = repair.Review(repair.runner.load_yaml(ITEMS[key]["before_text"]), key)
    row = r.rows(key, si)[ri]
    row["amount" if mutation == "amount" else "unit"] = (
        999 if mutation == "amount" else ("g" if row["unit"] == "ml" else "ml")
    )
    with pytest.raises(ValueError):
        r.leaf(["ingredients"], key, si, ri)


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
