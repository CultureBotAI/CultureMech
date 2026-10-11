"""Challenge hydrolysate identity, source scope, quantities and guarded writes."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_lactalbumin_formulations as repair

spec = importlib.util.spec_from_file_location("lactalbumin_audit", repair.HERE / "audit.py")
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
def test_complete_projection_old_slots_and_source_rows(key):
    item, before, expected = records(key)
    snapshot = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == snapshot and after == expected
    assert claims == item["claims"] and lineage == item["lineage"]
    result = audit.check(before, after, item)
    assert result["old_quantity_slots"] == (13 if key == "M2287" else 12)
    assert result["new_evidence"] == {"D1021": 27, "K1021": 18, "K1021_16929": 20, "M2287": 12}[key]
    assert result["source_rows"] == {"D1021": 12, "K1021": 12, "K1021_16929": 15, "M2287": 11}[key]


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "water_mass",
        "false_lb",
        "history",
        "identity",
        "grounding",
        "snippet",
        "duplicate_evidence",
        "year",
        "title",
        "claim",
        "lineage",
        "old_quantity",
        "provenance",
    ],
)
def test_independent_audit_rejects_corruption(key, mutation):
    item, before, after = records(key)
    water = next(n for p, n in audit.walk(after) if n.get("preferred_term") == "Distilled water")
    if mutation == "water_mass":
        water["concentration"] = {"value": "1", "unit": "G_PER_L"}
    elif mutation == "false_lb":
        after["ingredients"].append(copy.deepcopy(before["ingredients"][repair.LB[key][0]]))
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif mutation == "identity":
        after["media_term"]["term"]["id"] = "TOGO:M2410"
    elif mutation == "grounding":
        water["term"] = {"id": "CHEBI:123", "label": "invented"}
    elif mutation == "snippet":
        water["evidence"][0]["snippet"] = "invented"
    elif mutation == "duplicate_evidence":
        after["evidence"].append(copy.deepcopy(after["evidence"][0]))
    elif mutation == "year":
        after["references"][0]["year"] = 2007
    elif mutation == "title":
        after["references"][0]["title"] = "Different recipe"
    elif mutation == "claim":
        item["claims"].pop()
    elif mutation == "lineage":
        item["lineage"].pop()
    elif mutation == "old_quantity":
        item["claims"][0]["old"] = {"value": "100", "unit": "G_PER_L"}
    else:
        after["notes"] = after["notes"].replace(
            "Superseded historical provenance (not a current formulation claim):", ""
        )
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "mutation",
    [
        "root_ph",
        "final_stock_rate",
        "base_dose",
        "serum_dose",
        "both_hydrolysates",
        "serum_autoclave",
        "filter_pore",
        "liquid_agar",
        "duplicate_link",
    ],
)
def test_dsmz_stock_boundaries_and_explicit_alternative(mutation):
    item, before, after = records("D1021")
    base, serum = after["solutions"]
    if mutation == "root_ph":
        after["ph_value"] = 8.0
    elif mutation == "final_stock_rate":
        base["solutions"][0]["composition"][0]["concentration"]["value"] = "4.96"
    elif mutation == "base_dose":
        base["concentration"] = {"value": "1", "unit": "L"}
    elif mutation == "serum_dose":
        serum["concentration"] = {"value": "200", "unit": "G_PER_L"}
    elif mutation == "both_hydrolysates":
        base["solutions"][0]["composition"].append(
            {
                "preferred_term": "Casein hydrolysate",
                "concentration": {"value": "9", "unit": "G_PER_L"},
            }
        )
    elif mutation == "serum_autoclave":
        after["preparation_steps"][1][
            "description"
        ] = "Autoclave the combined medium including serum."
    elif mutation == "filter_pore":
        after["variants"][0]["modifications"][0] = "Filter through a 0.22 micrometer membrane."
    elif mutation == "liquid_agar":
        after["variants"][0]["modifications"][1] = "Agar concentration is exactly zero."
    else:
        after["variant_children"][0]["relationship"] = "SOURCE_DUPLICATE"
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize("key", ["K1021", "K1021_16929"])
@pytest.mark.parametrize(
    "mutation",
    [
        "hydrolysate",
        "copied_stock_rate",
        "serum_mass",
        "serum_molarity",
        "water_dose",
        "duplicate_link",
        "rounding",
        "heated_serum",
    ],
)
def test_komodo_actual_source_rates_not_copied_dsmz_stock(key, mutation):
    item, before, after = records(key)
    if mutation == "hydrolysate":
        after["ingredients"][9]["preferred_term"] = "Lactalbumin hydrolysate"
    elif mutation == "copied_stock_rate":
        after["ingredients"][0]["concentration"]["value"] = "6.88889"
    elif mutation == "serum_mass":
        after["ingredients"][11]["concentration"] = {"value": "200", "unit": "G_PER_L"}
    elif mutation == "serum_molarity":
        after["ingredients"][11]["concentration"] = {"value": "0.20", "unit": "MOLAR"}
    elif mutation == "water_dose":
        after["ingredients"][10]["concentration"] = {"value": "1", "unit": "L"}
    elif mutation == "duplicate_link":
        after["parent_media"]["relationship"] = "SOURCE_DUPLICATE"
    elif mutation == "rounding":
        after["ingredients"][3]["concentration"]["value"] = "0.096"
    else:
        after["ingredients"][11]["notes"] += " Heat inactivate at 56 C."
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize("mutation", ["gas_zero", "gas_fraction", "lost_gas", "inherited_ph"])
def test_strain_variant_unknown_gases_are_not_duplicate_or_zero(mutation):
    item, before, after = records("K1021_16929")
    if mutation == "gas_zero":
        after["ingredients"][12]["concentration"] = {"value": "0", "unit": "MOLAR"}
    elif mutation == "gas_fraction":
        after["ingredients"][12]["concentration"] = {"value": "20", "unit": "PERCENT_V_V"}
    elif mutation == "lost_gas":
        after["ingredients"].pop()
    else:
        after["ph_value"] = 8.0
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize(
    "mutation",
    [
        "serum_basis",
        "base_dose",
        "dilution",
        "root_rates",
        "casein",
        "hydration",
        "water_final_volume",
    ],
)
def test_togo_preserves_pre_serum_recipe_without_assumed_percent_basis(mutation):
    item, before, after = records("M2287")
    base = after["solutions"][0]
    if mutation == "serum_basis":
        after["ingredients"][0]["concentration"] = {"value": "5", "unit": "PERCENT_W_V"}
    elif mutation == "base_dose":
        base["concentration"] = {"value": "1", "unit": "L"}
    elif mutation == "dilution":
        base["composition"][2]["concentration"]["value"] = "114"
    elif mutation == "root_rates":
        after["ingredients"].append(base["composition"].pop())
    elif mutation == "casein":
        base["composition"][9]["preferred_term"] = "Casein hydrolysate"
    elif mutation == "hydration":
        base["composition"][6]["preferred_term"] = "CaCl2 x 2 H2O"
    else:
        base["composition"][0][
            "notes"
        ] = "Make complete serum-supplemented medium up to exactly 1 L."
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


def test_guarded_preview_apply_readback_noop(tmp_path, monkeypatch):
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
def test_all_target_guards_precede_writes(tmp_path, monkeypatch, mutation):
    targets = fixture_repo(tmp_path, monkeypatch)
    path, target = tmp_path / "plan.json", targets[-1]
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


def test_context_hash_guard(monkeypatch):
    monkeypatch.setattr(repair, "CONTEXT_SHA", "0" * 64)
    with pytest.raises(ValueError, match="Inspected context drift"):
        repair.frozen()
