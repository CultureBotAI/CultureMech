from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_ccap_duplicate_compositions.py"


def load_script():
    spec = importlib.util.spec_from_file_location(
        "repair_ccap_duplicate_compositions", SCRIPT
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return load_script()


def test_ch_uses_three_calculated_stock_recipes(repair_module) -> None:
    recipe = repair_module.RECIPES["ch"]

    assert [row["preferred_term"] for row in recipe["ingredients"]] == [
        "Deionized water"
    ]
    assert [row["concentration"] for row in recipe["solutions"]] == [
        {"value": "5.0", "unit": "ML_PER_L"},
        {"value": "5.0", "unit": "ML_PER_L"},
        {"value": "5.0", "unit": "ML_PER_L"},
    ]
    assert [
        solution["composition"][0]["concentration"]
        for solution in recipe["solutions"]
    ] == [
        {"value": "20", "unit": "G_PER_L"},
        {"value": "0.8", "unit": "G_PER_L"},
        {"value": "1.2", "unit": "G_PER_L"},
    ]
    assert recipe["composition_type"] == "DEFINED"


def test_merds_and_ses_keep_referenced_media_and_stocks_nested(repair_module) -> None:
    merds = repair_module.RECIPES["merds"]
    assert [row["preferred_term"] for row in merds["solutions"]] == [
        "SES medium",
        "NaNO3 stock solution",
        "Na2HPO4.2H2O stock solution",
    ]
    assert merds["solutions"][1]["composition"][0]["concentration"] == {
        "value": "75",
        "unit": "G_PER_L",
    }
    assert merds["solutions"][2]["composition"][0]["term"] == {
        "id": "CHEBI:91258",
        "label": "disodium hydrogenphosphate dihydrate",
    }

    ses = repair_module.RECIPES["ses"]
    assert len(ses["solutions"]) == 4
    assert ses["solutions"][-1]["preferred_term"] == "Soil Extract 2 (SE2)"
    assert ses["solutions"][-1]["composition"] == []


def test_soil_media_use_biphasic_and_per_vessel_semantics(repair_module) -> None:
    sw = repair_module.RECIPES["sw"]
    assert sw["physical_state"] == "BIPHASIC"
    assert all(
        row["concentration"] == {"value": "variable", "unit": "VARIABLE"}
        for row in sw["ingredients"]
    )

    amp = repair_module.RECIPES["sw_amp"]
    assert amp["ingredients"][0]["concentration"] == {
        "value": "0.01 g per vessel",
        "unit": "VARIABLE",
    }
    assert amp["ingredients"][0]["term"] == {
        "id": "CHEBI:149425",
        "label": "ammonium magnesium phosphate",
    }
    assert amp["ph_range"] == {"min": 7.0, "max": 8.0}

    se2 = repair_module.RECIPES["se2"]
    assert se2["ph_value"] == 7.1
    assert se2["physical_state"] == "LIQUID"


def test_every_recipe_has_complete_component_objects(repair_module) -> None:
    for recipe in repair_module.RECIPES.values():
        assert recipe["ingredients"] or recipe["solutions"]
        assert all(row.get("concentration") for row in recipe["ingredients"])
        assert all(row.get("concentration") for row in recipe["solutions"])
        assert all(row.get("preferred_term") for row in recipe["ingredients"])
        assert all(row.get("preferred_term") for row in recipe["solutions"])


def test_empty_and_existing_guards_repair_to_same_recipe(repair_module) -> None:
    empty_target = next(
        target
        for target in repair_module.TARGETS
        if target.recipe_key == "yel" and target.precondition == "empty"
    )
    existing_target = next(
        target
        for target in repair_module.TARGETS
        if target.recipe_key == "yel" and target.precondition == "existing"
    )
    empty_doc = {
        "id": empty_target.record_id,
        "notes": "Source: CCAP",
        "ingredients": [],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
    }
    existing_doc = {
        "id": existing_target.record_id,
        "notes": "Source: CCAP",
        "ingredients": [
            {
                "preferred_term": name,
                "concentration": {"value": value, "unit": unit},
            }
            for name, value, unit in repair_module.EXISTING_SIGNATURES[
                existing_target.relative_path
            ]
        ],
        "curation_history": [],
    }

    repaired_empty, changed_empty = repair_module.repair_document(
        empty_doc, empty_target
    )
    repaired_existing, changed_existing = repair_module.repair_document(
        existing_doc, existing_target
    )

    assert changed_empty and changed_existing
    assert repair_module.recipe_projection(
        repaired_empty
    ) == repair_module.recipe_projection(repaired_existing)
    second, changed_again = repair_module.repair_document(
        copy.deepcopy(repaired_existing), existing_target
    )
    assert not changed_again
    assert second == repaired_existing


def test_source_hash_mismatch_is_rejected(repair_module, tmp_path: Path) -> None:
    for name in repair_module.SOURCE_FILES:
        (tmp_path / name).write_bytes(b"not the reviewed PDF")

    with pytest.raises(ValueError, match="SHA-256"):
        repair_module.validate_source_files(tmp_path)


def test_target_inventory_is_ten_exact_pairs(repair_module) -> None:
    repair_module._validate_inventory()
    by_recipe = {}
    for target in repair_module.TARGETS:
        by_recipe.setdefault(target.recipe_key, []).append(target)

    assert set(by_recipe) == {
        "ch",
        "merds",
        "mw",
        "sw",
        "sw_amp",
        "sw_ca",
        "se1",
        "se2",
        "ses",
        "yel",
    }
    assert all(len(targets) == 2 for targets in by_recipe.values())
    assert all(
        {target.precondition for target in targets} == {"empty", "existing"}
        for targets in by_recipe.values()
    )


def test_target_records_are_in_guarded_pre_or_post_state(repair_module) -> None:
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.relative_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert doc["id"] == target.record_id
        if repair_module.history_has_action(doc):
            repair_module._assert_applied(doc, target)
        else:
            repair_module._validate_precondition(copy.deepcopy(doc), target)
