"""Challenge source support, reagent scope and guarded J201/J220 application."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_jcm_albumin_inputs as repair

spec = importlib.util.spec_from_file_location("albumin_audit", repair.HERE / "audit.py")
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
def test_projection_and_full_source_audit(key):
    item, before, expected = records(key)
    untouched = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == untouched and after == expected
    assert claims == item["claims"] and lineage == item["lineage"]
    stats = audit.check(before, after, item)
    assert stats["old_quantity_slots"] == 11 and stats["source_rows"] == 10
    assert stats["new_evidence"] == {"J201": 11, "J220": 24}[key]
    assert stats["new_quantity_slots"] == 2


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "water_amount",
        "water_unit",
        "mass_rate",
        "lb_returned",
        "albumin_removed",
        "albumin_grounding",
        "fraction",
        "dose",
        "dose_unit",
        "history",
        "grounding",
        "quote",
        "year",
        "duplicate_evidence",
        "claim",
        "lineage",
        "ph",
        "preparation",
        "provenance",
        "invented_original",
    ],
)
def test_independent_audit_rejects_wrong_claims(key, mutation):
    item, before, after = records(key)
    water = next(n for n in after["ingredients"] if n["preferred_term"] == "Distilled water")
    albumin = after["ingredients"][1] if key == "J201" else after["solutions"][1]["composition"][0]
    if mutation == "water_amount":
        water["concentration"]["value"] = "1.036"
    elif mutation == "water_unit":
        water["concentration"]["unit"] = "G_PER_L"
    elif mutation == "mass_rate":
        after["ingredients"][0]["concentration"] = {"value": "5", "unit": "G_PER_L"}
    elif mutation == "lb_returned":
        after["ingredients"].append(copy.deepcopy(before["ingredients"][repair.LB[key][0]]))
    elif mutation == "albumin_removed":
        albumin["preferred_term"] = "LB Broth"
    elif mutation == "albumin_grounding":
        albumin["term"] = {"id": "CHEBI:123", "label": "albumin"}
    elif mutation == "fraction":
        albumin["notes"] = albumin["notes"].replace("raction V", "raction IV")
    elif mutation == "dose":
        after["solutions"][0]["concentration"]["value"] = "100"
    elif mutation == "dose_unit":
        after["solutions"][0]["concentration"]["unit"] = "ML_PER_L"
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif mutation == "grounding":
        next(n for n in after["ingredients"] if "term" in n)["term"]["id"] = "CHEBI:000000"
    elif mutation == "quote":
        after["ingredients"][0]["evidence"][0]["snippet"] = "invented"
    elif mutation == "year":
        after["references"][0]["year"] = 2026
    elif mutation == "duplicate_evidence":
        after["evidence"].append(copy.deepcopy(after["evidence"][0]))
    elif mutation == "claim":
        item["claims"].pop()
    elif mutation == "lineage":
        item["lineage"].pop()
    elif mutation == "ph":
        after["ph_value"] = 7.0
    elif mutation == "preparation":
        after["preparation_steps"][0]["description"] += " Make to one liter."
    elif mutation == "provenance":
        after["notes"] = after["notes"].replace(
            "Superseded historical provenance (not a current formulation claim):", ""
        )
    else:
        after["references"].append(
            {
                "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=201",
                "title": "Medium data",
                "notes": "Verified original recipe",
            }
        )
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "mutation",
    [
        "gelatin_strength",
        "serum_percent",
        "serum_dose",
        "late_order",
        "cmrl_expanded",
        "pore",
        "access_gap",
        "legacy_link",
        "albumin_rate",
    ],
)
def test_j201_provider_only_and_late_preparation(mutation):
    item, before, after = records("J201")
    cmrl, gelatin, serum = after["solutions"]
    if mutation == "gelatin_strength":
        gelatin["composition"][0]["concentration"] = {"value": "7", "unit": "PERCENT_W_V"}
    elif mutation == "serum_percent":
        serum["concentration"] = {"value": "6", "unit": "PERCENT_V_V"}
    elif mutation == "serum_dose":
        serum["concentration"] = {"value": "0.06", "unit": "L"}
    elif mutation == "late_order":
        serum["notes"] = serum["notes"].replace("after filtration", "before filtration")
    elif mutation == "cmrl_expanded":
        cmrl["composition"].append({"preferred_term": "Glucose"})
    elif mutation == "pore":
        after["preparation_steps"][0]["action"] = "FILTER_STERILIZE"
    elif mutation == "access_gap":
        after["references"][0]["notes"] = "Original recipe verified."
    elif mutation == "legacy_link":
        next(n for n in after["ingredients"] if "mediaingredientmech_term" in n).pop(
            "mediaingredientmech_term"
        )
    else:
        after["ingredients"][1]["concentration"] = {"value": "50", "unit": "G_PER_L"}
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "mutation",
    [
        "hemin_strength",
        "normality_molarity",
        "solvent_dose",
        "solvent_missing",
        "stock_filter",
        "albumin_strength",
        "cysteine_form",
        "corn_grounding",
    ],
)
def test_j220_stock_strengths_and_solvent(mutation):
    item, before, after = records("J220")
    hemin, albumin, glucose, cysteine = after["solutions"]
    solvent = hemin["solutions"][0]
    if mutation == "hemin_strength":
        hemin["composition"][0]["concentration"] = {"value": "0.1", "unit": "PERCENT_W_V"}
    elif mutation == "normality_molarity":
        solvent["composition"][0]["concentration"] = {"value": "0.05", "unit": "MOLAR"}
    elif mutation == "solvent_dose":
        solvent["concentration"] = {"value": "0.015", "unit": "L"}
    elif mutation == "solvent_missing":
        hemin.pop("solutions")
    elif mutation == "stock_filter":
        glucose["preparation_notes"] = "Autoclave the glucose solution."
    elif mutation == "albumin_strength":
        albumin["composition"][0]["concentration"] = {"value": "20", "unit": "PERCENT_W_V"}
    elif mutation == "cysteine_form":
        cysteine["composition"][0]["preferred_term"] = "L-cysteine hydrochloride"
    else:
        after["ingredients"][0]["term"]["id"] = "CHEBI:9999999"
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize("ri", range(10))
def test_j220_amount_conflict_blocks_original_corroboration(ri):
    review = repair.Review(repair.runner.load_yaml(ITEMS["J220"]["before_text"]), "J220")
    review.rows("J220", 0)[ri]["amount"] = 999
    with pytest.raises(ValueError, match="Original/API amount conflict"):
        review.original(["notes"], ri, [])


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
