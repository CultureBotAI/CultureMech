"""Challenge preparation boundaries, unknown bases, evidence and guarded writes."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_dsmz_albumin_preparations as repair

spec = importlib.util.spec_from_file_location("dsmz_albumin_audit", repair.HERE / "audit.py")
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
def test_complete_projection_and_old_quantity_accounting(key):
    item, before, expected = records(key)
    snapshot = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == snapshot and after == expected
    assert claims == item["claims"] and lineage == item["lineage"]
    result = audit.check(before, after, item)
    assert result["old_quantity_slots"] == {"K403": 18, "D403": 17, "K751": 11, "D751": 11}[key]
    assert result["new_evidence"] == (33 if key.endswith("403") else 24)


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "water_value",
        "water_unit",
        "dose",
        "dose_per_liter",
        "lb_returned",
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
        "source_link",
    ],
)
def test_audit_rejects_corruption(key, mutation):
    item, before, after = records(key)
    water = next(n for p, n in audit.walk(after) if n.get("preferred_term", "").endswith("water"))
    if mutation == "water_value":
        water["concentration"]["value"] = "1.243"
    elif mutation == "water_unit":
        water["concentration"]["unit"] = "G_PER_L"
    elif mutation == "dose":
        after["solutions"][0]["concentration"]["value"] = "9.99"
    elif mutation == "dose_per_liter":
        after["solutions"][0]["concentration"]["unit"] = "ML_PER_L"
    elif mutation == "lb_returned":
        after["ingredients"].append(copy.deepcopy(before["ingredients"][repair.LB[key][0]]))
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "overwritten"
    elif mutation == "grounding":
        water["term"] = {"id": "CHEBI:123", "label": "water"}
    elif mutation == "snippet":
        water["evidence"][0]["snippet"] = "invented"
    elif mutation == "year":
        after["references"][0]["year"] = 2007
    elif mutation == "duplicate_evidence":
        after["evidence"].append(copy.deepcopy(after["evidence"][0]))
    elif mutation == "claim":
        item["claims"].pop()
    elif mutation == "lineage":
        item["lineage"].pop()
    elif mutation == "ph":
        after["ph_value"] = 7.6
    elif mutation == "procedure":
        after["preparation_steps"][0]["description"] += " Make to a final liter."
    elif mutation == "notes":
        after["notes"] = after["notes"].replace(
            "Superseded historical provenance (not a current formulation claim):", ""
        )
    else:
        after["media_term"]["term"]["id"] = "mediadive.medium:J220"
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize("key", ["K403", "D403"])
@pytest.mark.parametrize(
    "mutation",
    [
        "gelatin_strength",
        "albumin_strength",
        "albumin_mass",
        "albumin_alternative",
        "stock_scope",
        "cmrl_composition",
        "serum_molarity",
        "serum_extra_dose",
        "titrant_dose",
        "titrant_strength",
        "autoclave_cycle",
        "ph_scope",
        "water_merge",
    ],
)
def test_bsk_scopes_and_alternatives(key, mutation):
    item, before, after = records(key)
    a, b, c, d = after["solutions"]
    if mutation == "gelatin_strength":
        b["composition"][0]["concentration"]["value"] = "14"
    elif mutation == "albumin_strength":
        c["composition"][0]["concentration"]["value"] = "35"
    elif mutation == "albumin_mass":
        c["composition"][0]["notes"] = c["composition"][0]["notes"].replace("50.05", "50.0")
    elif mutation == "albumin_alternative":
        c["preparation_notes"] = c["preparation_notes"].replace("or use", "and add")
    elif mutation == "stock_scope":
        a["composition"][0]["notes"] = a["composition"][0]["notes"].replace(
            "not a receiving-medium concentration", "final-medium concentration"
        )
    elif mutation == "cmrl_composition":
        a["solutions"][0]["composition"] = [{"preferred_term": "Glucose"}]
    elif mutation == "serum_molarity":
        d["concentration"] = {"value": "526320", "unit": "MILLIMOLAR"}
    elif mutation == "serum_extra_dose":
        d["composition"] = [
            {"preferred_term": "Rabbit serum", "concentration": {"value": "0.086", "unit": "L"}}
        ]
    elif mutation == "titrant_dose":
        a["solutions"][1]["concentration"] = {"value": "0.005", "unit": "L"}
    elif mutation == "titrant_strength":
        a["solutions"][1]["composition"][0]["concentration"]["value"] = "0.05"
    elif mutation == "autoclave_cycle":
        b["preparation_notes"] = b["preparation_notes"].replace("115", "121")
    elif mutation == "ph_scope":
        a["preparation_notes"] = a["preparation_notes"].replace("7.6", "7.0")
    else:
        a["composition"][-1]["concentration"]["value"] = "1.243"
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize("key", ["K751", "D751"])
@pytest.mark.parametrize(
    "mutation",
    [
        "jcm_glucose",
        "percent_basis",
        "normality",
        "hemin_filter",
        "albumin_autoclave",
        "fraction",
        "cysteine_salt",
        "liquid_phosphate",
        "liquid_added_to_base",
        "liquid_variant_missing",
        "parent_link",
        "batch_mass",
    ],
)
def test_sc_is_not_jcm220_and_variant_is_separate(key, mutation):
    item, before, after = records(key)
    hemin, albumin, glucose, cysteine = after["solutions"]
    if mutation == "jcm_glucose":
        glucose["concentration"]["value"] = "0.001"
    elif mutation == "percent_basis":
        albumin["composition"][0]["concentration"] = {"value": "20", "unit": "PERCENT_W_V"}
    elif mutation == "normality":
        hemin["solutions"][0]["composition"][0]["concentration"] = {
            "value": "0.05",
            "unit": "MOLAR",
        }
    elif mutation == "hemin_filter":
        hemin["preparation_notes"] = glucose["preparation_notes"]
    elif mutation == "albumin_autoclave":
        albumin["preparation_notes"] = "Autoclave."
    elif mutation == "fraction":
        albumin["composition"][0]["notes"] = albumin["composition"][0]["notes"].replace(
            "fraction V", "fraction IV"
        )
    elif mutation == "cysteine_salt":
        cysteine["composition"][0]["preferred_term"] = "L-cysteine hydrochloride"
    elif mutation == "liquid_phosphate":
        after["variants"][0]["modifications"][1] = "Use KH2PO4 0.5 g."
    elif mutation == "liquid_added_to_base":
        after["ingredients"][2]["concentration"] = {"value": "0.5", "unit": "G_PER_L"}
    elif mutation == "liquid_variant_missing":
        after.pop("variants")
    elif mutation == "parent_link":
        after.pop("parent_media" if key == "K751" else "variant_children")
    else:
        after["ingredients"][0]["notes"] = after["ingredients"][0]["notes"].replace("17 g", "17 mg")
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "key,si,ri", [("D403", 1, 6), ("K403", 1, 0), ("D751", 0, 8), ("K751", 0, 4)]
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


def test_guarded_preview_apply_readback_and_noop(tmp_path, monkeypatch):
    targets = fixture_repo(tmp_path, monkeypatch)
    path = tmp_path / "plan.json"
    before = [p.read_bytes() for p in targets]
    repair.process(tmp_path, path, "preview")
    assert [p.read_bytes() for p in targets] == before
    assert repair.process(tmp_path, path, "apply")[1]["changed"] == 4
    after = [p.read_bytes() for p in targets]
    assert repair.process(tmp_path, path, "verify")[1]["already_applied"] == 4
    assert repair.process(tmp_path, path, "apply")[1]["changed"] == 0
    assert [p.read_bytes() for p in targets] == after


@pytest.mark.parametrize("mutation", ["concurrent", "forged_plan", "symlink"])
def test_all_target_guards_precede_first_write(tmp_path, monkeypatch, mutation):
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
