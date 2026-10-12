"""Challenge exact formulation identity, dimensions, evidence and write guards."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_bsk_formulations as repair

spec = importlib.util.spec_from_file_location("bsk_formulation_audit", repair.HERE / "audit.py")
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
def test_complete_source_projection_and_old_quantity_accounting(key):
    item, before, expected = records(key)
    snapshot = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == snapshot and after == expected
    assert claims == item["claims"] and lineage == item["lineage"]
    result = audit.check(before, after, item)
    assert result["old_quantity_slots"] == (14 if key == "M2410" else 13)
    assert result["new_evidence"] == {"M2410": 13, "D1829": 27, "J173": 29}[key]
    assert result["source_rows"] == (13 if key == "J173" else 12)


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "water",
        "dose",
        "lb",
        "history",
        "grounding",
        "snippet",
        "year",
        "duplicate_evidence",
        "claim",
        "lineage",
        "ph",
        "procedure",
        "notes",
        "source_identity",
        "title",
    ],
)
def test_audit_rejects_corruption(key, mutation):
    item, before, after = records(key)
    water = next(n for p, n in audit.walk(after) if "water" in n.get("preferred_term", "").lower())
    if mutation == "water":
        water["concentration"] = {"value": "100", "unit": "G_PER_L"}
    elif mutation == "dose":
        after["solutions"][0]["concentration"] = {"value": "0.5", "unit": "L"}
    elif mutation == "lb":
        after["ingredients"].append(copy.deepcopy(before["ingredients"][repair.LB[key][0]]))
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif mutation == "grounding":
        water["term"] = {"id": "CHEBI:123", "label": "water"}
    elif mutation == "snippet":
        water["evidence"][0]["snippet"] = "invented"
    elif mutation == "year":
        after["references"][0]["year"] = 1984
    elif mutation == "duplicate_evidence":
        after["evidence"].append(copy.deepcopy(after["evidence"][0]))
    elif mutation == "claim":
        item["claims"].pop()
    elif mutation == "lineage":
        item["lineage"].pop()
    elif mutation == "ph":
        after["ph_value"] = 7.6
    elif mutation == "procedure":
        after["preparation_steps"][0]["description"] += " Make up to one final liter."
    elif mutation == "notes":
        after["notes"] = after["notes"].replace(
            "Superseded historical provenance (not a current formulation claim):", ""
        )
    elif mutation == "source_identity":
        after["media_term"]["term"]["id"] = "TOGO:M194"
    else:
        after["references"][0]["title"] = "BSK medium"
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "mutation",
    [
        "serum_mass",
        "serum_factor",
        "albumin_factor",
        "makeup_dose",
        "naoh_dose",
        "filter_pore",
        "genuine_yeast",
        "makeup_order",
    ],
)
def test_dsmz_explicit_final_volume_and_makeup(mutation):
    item, before, after = records("D1829")
    if mutation == "serum_mass":
        after["ingredients"][9]["concentration"]["unit"] = "G_PER_L"
    elif mutation == "serum_factor":
        after["ingredients"][9]["concentration"]["value"] = "8.56"
    elif mutation == "albumin_factor":
        after["ingredients"][8]["concentration"]["value"] = "0.85"
    elif mutation == "makeup_dose":
        after["ingredients"][11]["concentration"] = {"value": "0.1", "unit": "L"}
    elif mutation == "naoh_dose":
        after["solutions"][0]["concentration"] = {"value": "1", "unit": "MOLAR"}
    elif mutation == "filter_pore":
        after["preparation_steps"][2]["action"] = "FILTER_STERILIZE"
    elif mutation == "makeup_order":
        after["preparation_steps"][0]["description"] = "Make up to 100 ml before adding titrant."
    else:
        after["ingredients"][6]["concentration"]["value"] = "5"
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "mutation",
    [
        "milligrams",
        "a_dose",
        "b_dose",
        "normality",
        "serum_unheated",
        "serum_per_liter",
        "cmrl",
        "legacy_grounding",
        "autoclave_scope",
        "genuine_yeast",
    ],
)
def test_jcm_stock_scope_and_unusual_source_mass(mutation):
    item, before, after = records("J173")
    a, b, titrant, serum = after["solutions"]
    if mutation == "milligrams":
        b["composition"][0]["concentration"]["value"] = "25"
    elif mutation == "a_dose":
        a["concentration"] = {"value": "0.5", "unit": "L"}
    elif mutation == "b_dose":
        b["concentration"] = {"value": "0.1", "unit": "L"}
    elif mutation == "normality":
        titrant["composition"][0]["concentration"] = {"value": "1", "unit": "MOLAR"}
    elif mutation == "serum_unheated":
        serum["notes"] = "Use unheated serum."
    elif mutation == "serum_per_liter":
        serum["concentration"] = {"value": "40", "unit": "ML_PER_L"}
    elif mutation == "cmrl":
        a["composition"][0]["notes"] = a["composition"][0]["notes"].replace(
            "with glutamate", "without glutamine"
        )
    elif mutation == "legacy_grounding":
        a["composition"][6].pop("mediaingredientmech_term")
    elif mutation == "autoclave_scope":
        after["preparation_steps"][2]["description"] = "Autoclave the complete medium."
    else:
        a["composition"][8]["concentration"]["value"] = "5"
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "mutation",
    [
        "batch_mass",
        "gelatin_percent",
        "gelatin_mass",
        "serum_percent",
        "serum_dose",
        "serum_heated",
        "normality",
        "filter_pore",
        "cmrl_composition",
        "array_order",
        "altitude",
    ],
)
def test_togo_does_not_import_other_bsk_formulations(mutation):
    item, before, after = records("M2410")
    cmrl, titrant, gelatin, serum = after["solutions"]
    if mutation == "batch_mass":
        after["ingredients"][4]["concentration"] = {"value": "50", "unit": "G_PER_L"}
    elif mutation == "gelatin_percent":
        gelatin["composition"][0]["concentration"] = {"value": "7", "unit": "PERCENT_W_V"}
    elif mutation == "gelatin_mass":
        gelatin["composition"][0]["notes"] = "Add 14 g gelatin."
    elif mutation == "serum_percent":
        serum["concentration"] = {"value": "6", "unit": "PERCENT_V_V"}
    elif mutation == "serum_dose":
        serum["concentration"] = {"value": "0.04", "unit": "L"}
    elif mutation == "serum_heated":
        serum["notes"] = "Heat at 56 C for 45 min."
    elif mutation == "normality":
        titrant["composition"][0]["concentration"] = {"value": "1", "unit": "MOLAR"}
    elif mutation == "filter_pore":
        after["preparation_steps"][5]["action"] = "FILTER_STERILIZE"
    elif mutation == "cmrl_composition":
        cmrl["composition"] = [{"preferred_term": "glutamate"}]
    elif mutation == "array_order":
        after["preparation_steps"][2]["description"] = "Follow API item order."
    else:
        after["notes"] = after["notes"].replace("1,200m", "200m")
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "key,si,ri", [("D1829", 0, 8), ("D1829", 0, 9), ("J173", 1, 1), ("J173", 2, 0)]
)
def test_original_provider_conflict_blocks(key, si, ri):
    review = repair.Review(repair.runner.load_yaml(ITEMS[key]["before_text"]), key)
    review.row(si, ri)["amount"] = 999
    with pytest.raises(ValueError, match="Original/provider amount conflict"):
        review.original_row(["notes"], si, ri, [])


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


def test_guarded_preview_apply_readback_noop(tmp_path, monkeypatch):
    targets = fixture_repo(tmp_path, monkeypatch)
    path = tmp_path / "plan.json"
    before = [p.read_bytes() for p in targets]
    repair.process(tmp_path, path, "preview")
    assert [p.read_bytes() for p in targets] == before
    assert repair.process(tmp_path, path, "apply")[1]["changed"] == 3
    after = [p.read_bytes() for p in targets]
    assert repair.process(tmp_path, path, "verify")[1]["already_applied"] == 3
    assert repair.process(tmp_path, path, "apply")[1]["changed"] == 0
    assert [p.read_bytes() for p in targets] == after


@pytest.mark.parametrize("mutation", ["concurrent", "forged_plan", "symlink"])
def test_all_target_guards_before_first_write(tmp_path, monkeypatch, mutation):
    targets = fixture_repo(tmp_path, monkeypatch)
    target, path = targets[-1], tmp_path / "plan.json"
    plan, _ = repair.process(tmp_path, path, "preview")
    if mutation == "concurrent":
        target.write_text(target.read_text() + "\n# concurrent edit\n")
    elif mutation == "forged_plan":
        plan["records"][-1]["claims"].pop()
        path.write_text(json.dumps(plan))
    else:
        elsewhere = tmp_path / "other.yaml"
        target.rename(elsewhere)
        target.symlink_to(elsewhere)
    before = [p.read_bytes() for p in targets]
    with pytest.raises(ValueError):
        repair.process(tmp_path, path, "apply")
    assert [p.read_bytes() for p in targets] == before
