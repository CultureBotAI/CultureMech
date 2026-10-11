"""Challenge albumin identity, exact stock strength, batch doses and guarded writes."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_albumin_counterparts as repair

spec = importlib.util.spec_from_file_location("counterparts_audit", repair.HERE / "audit.py")
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
def test_complete_source_projection(key):
    item, before, expected = records(key)
    unchanged = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == unchanged and after == expected
    assert claims == item["claims"] and lineage == item["lineage"]
    result = audit.check(before, after, item)
    assert result["old_quantity_slots"] == {"M194": 14, "M213": 12, "M244": 18, "J252": 16}[key]
    assert result["new_evidence"] == {"M194": 11, "M213": 24, "M244": 34, "J252": 32}[key]


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "water_value",
        "water_unit",
        "mass_rate",
        "batch_mass",
        "lb_returned",
        "history",
        "grounding",
        "quote",
        "year",
        "evidence_duplicate",
        "claim",
        "lineage",
        "ph",
        "procedure",
        "pore_size",
        "provenance",
        "invented_original",
    ],
)
def test_independent_audit_rejects_corruption(key, mutation):
    item, before, after = records(key)
    water = next(n for n in after["ingredients"] if n["preferred_term"] == "Distilled water")
    mass = next(n for n in after["ingredients"] if "Source batch input:" in n.get("notes", ""))
    if mutation == "water_value":
        water["concentration"]["value"] = "1.234"
    elif mutation == "water_unit":
        water["concentration"]["unit"] = "G_PER_L"
    elif mutation == "mass_rate":
        mass["concentration"] = {"value": "1", "unit": "G_PER_L"}
    elif mutation == "batch_mass":
        mass["notes"] = mass["notes"].replace("Source batch input:", "Unsupported amount:")
    elif mutation == "lb_returned":
        after["ingredients"].append(copy.deepcopy(before["ingredients"][repair.LB[key][0]]))
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif mutation == "grounding":
        water["term"] = {"id": "CHEBI:123", "label": "water"}
    elif mutation == "quote":
        water["evidence"][0]["snippet"] = "invented"
    elif mutation == "year":
        after["references"][0]["year"] = 2026
    elif mutation == "evidence_duplicate":
        after["evidence"].append(copy.deepcopy(after["evidence"][0]))
    elif mutation == "claim":
        item["claims"].pop()
    elif mutation == "lineage":
        item["lineage"].pop()
    elif mutation == "ph":
        after["ph_value"] = 7.0
    elif mutation == "procedure":
        after["preparation_steps"][0]["description"] += " Make up to one liter."
    elif mutation == "pore_size":
        next(s for s in after["preparation_steps"] if s["action"] == "FILTER")[
            "action"
        ] = "FILTER_STERILIZE"
    elif mutation == "provenance":
        after["notes"] = after["notes"].replace(
            "Superseded historical provenance (not a current formulation claim):", ""
        )
    else:
        after["references"].append(
            {
                "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=201",
                "title": "Medium data",
                "notes": "Original verified",
            }
        )
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "mutation",
    [
        "gelatin_percent",
        "serum_percent",
        "serum_dose",
        "cmrl_composition",
        "serum_order",
        "fraction",
        "original_gap",
    ],
)
def test_m194_unknown_bases_and_product_integrity(mutation):
    item, before, after = records("M194")
    gelatin, cmrl, serum = after["solutions"]
    if mutation == "gelatin_percent":
        gelatin["composition"][0]["concentration"] = {"value": "7", "unit": "PERCENT_W_V"}
    elif mutation == "serum_percent":
        serum["concentration"] = {"value": "6", "unit": "PERCENT_V_V"}
    elif mutation == "serum_dose":
        serum["concentration"] = {"value": "0.06", "unit": "L"}
    elif mutation == "cmrl_composition":
        cmrl["composition"].append({"preferred_term": "Glucose"})
    elif mutation == "serum_order":
        serum["notes"] = serum["notes"].replace(
            "after medium filtration", "before medium filtration"
        )
    elif mutation == "fraction":
        next(n for n in after["ingredients"] if "albumin" in n["preferred_term"])[
            "preferred_term"
        ] = "Bovine albumin, Fraction IV"
    else:
        after["notes"] = after["notes"].replace(
            "TOGO-provider-backed, not original-page corroborated", "Original verified"
        )
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "mutation",
    [
        "hemin_strength",
        "solvent_strength",
        "solvent_dose",
        "solvent_missing",
        "hemin_filter",
        "glucose_filter",
        "albumin_strength",
        "cysteine_identity",
    ],
)
def test_m213_stock_scopes(mutation):
    item, before, after = records("M213")
    glucose, cysteine, albumin, hemin = after["solutions"]
    solvent = hemin["solutions"][0]
    if mutation == "hemin_strength":
        hemin["composition"][0]["concentration"] = {"value": "0.1", "unit": "PERCENT_W_V"}
    elif mutation == "solvent_strength":
        solvent["composition"][0]["concentration"] = {"value": "0.05", "unit": "MOLAR"}
    elif mutation == "solvent_dose":
        solvent["concentration"] = {"value": "0.015", "unit": "L"}
    elif mutation == "solvent_missing":
        hemin.pop("solutions")
    elif mutation == "hemin_filter":
        hemin["preparation_notes"] = glucose["preparation_notes"]
    elif mutation == "glucose_filter":
        glucose["preparation_notes"] = "Autoclave."
    elif mutation == "albumin_strength":
        albumin["composition"][0]["concentration"] = {"value": "20", "unit": "PERCENT_W_V"}
    else:
        cysteine["composition"][0]["preferred_term"] = "L-cysteine hydrochloride"
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize("key", ["M244", "J252"])
@pytest.mark.parametrize(
    "mutation",
    [
        "strength_value",
        "strength_basis",
        "strength_removed",
        "dose_value",
        "dose_per_liter",
        "dose_arithmetic",
        "yeast_percent",
        "sulfide_dose",
        "genuine_yeast_removed",
        "albumin_autoclave",
        "ph_temperature",
        "metal_flag",
    ],
)
def test252_explicit_strength_and_derived_dose(key, mutation):
    item, before, after = records(key)
    yeast, albumin, sulfide = after["solutions"]
    component = albumin["composition"][0]
    if mutation == "strength_value":
        component["concentration"]["value"] = "1"
    elif mutation == "strength_basis":
        component["concentration"]["unit"] = "PERCENT_W_W"
    elif mutation == "strength_removed":
        component.pop("concentration")
    elif mutation == "dose_value":
        albumin["concentration"]["value"] = "0.1"
    elif mutation == "dose_per_liter":
        albumin["concentration"]["unit"] = "ML_PER_L"
    elif mutation == "dose_arithmetic":
        albumin["notes"] = albumin["notes"].replace(
            "1 g / explicit stock strength", "10 g / explicit stock strength"
        )
    elif mutation == "yeast_percent":
        yeast["composition"][0]["concentration"] = {"value": "10", "unit": "PERCENT_W_V"}
    elif mutation == "sulfide_dose":
        sulfide["concentration"] = {"value": "0.01", "unit": "L"}
    elif mutation == "genuine_yeast_removed":
        yeast["composition"].clear()
    elif mutation == "albumin_autoclave":
        albumin["preparation_notes"] = yeast["preparation_notes"]
    elif mutation == "ph_temperature":
        after["preparation_steps"][2]["description"] = "Adjust pH to 7.6 at room temperature."
    else:
        after["high_metal"] = False
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "key,ri",
    [(key, ri) for key, size in (("M213", 10), ("M244", 15), ("J252", 15)) for ri in range(size)],
)
def test_original_amount_conflict_blocks_corroboration(key, ri):
    review = repair.Review(repair.runner.load_yaml(ITEMS[key]["before_text"]), key)
    row = review.rows(key, 0)[ri]
    row["amount" if key == "J252" else "volume"] = 999
    with pytest.raises(ValueError, match="Original/provider amount conflict"):
        review.original_amount(["notes"], ri, [])


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
    assert repair.process(tmp_path, plan_path, "apply")[1]["changed"] == 4
    after = [p.read_bytes() for p in targets]
    assert repair.process(tmp_path, plan_path, "verify")[1]["already_applied"] == 4
    assert repair.process(tmp_path, plan_path, "apply")[1]["changed"] == 0
    assert [p.read_bytes() for p in targets] == after


@pytest.mark.parametrize("mutation", ["concurrent", "forged_plan", "symlink"])
def test_all_target_guards_before_any_write(tmp_path, monkeypatch, mutation):
    targets = fixture_repo(tmp_path, monkeypatch)
    target, plan_path = targets[-1], tmp_path / "plan.json"
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
    before = [p.read_bytes() for p in targets]
    with pytest.raises(ValueError):
        repair.process(tmp_path, plan_path, "apply")
    assert [p.read_bytes() for p in targets] == before
