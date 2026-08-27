from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_ccap_missing_compositions.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_ccap_missing_compositions", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return load_script()


def test_nss_recipe_preserves_stock_boundaries_and_mim_identity(repair_module) -> None:
    recipe = repair_module.RECIPES["nss"]

    assert [row["preferred_term"] for row in recipe["ingredients"]] == [
        "Tricine",
        "Filtered natural seawater",
    ]
    assert [row["preferred_term"] for row in recipe["solutions"]] == [
        "Extra salts (ASW stock 1)",
        "Vitamin solution",
        "Soil Extract 1 (SE1)",
    ]
    assert [row["concentration"] for row in recipe["solutions"]] == [
        {"value": "7.50", "unit": "ML_PER_L"},
        {"value": "5.00", "unit": "ML_PER_L"},
        {"value": "12.50", "unit": "ML_PER_L"},
    ]
    salts = recipe["solutions"][0]["composition"]
    assert salts[0]["preferred_term"] == "NaNO3"
    assert salts[0]["term"] == {"id": "CHEBI:63005", "label": "sodium nitrate"}
    inositol = next(
        row for row in recipe["solutions"][1]["composition"] if row["preferred_term"] == "Inositol"
    )
    assert inositol["term"] == {"id": "CHEBI:24848", "label": "inositol"}
    assert recipe["ph_range"] == {"min": 7.6, "max": 7.8}


def test_wmy_and_2sna_values_match_reviewed_sources(repair_module) -> None:
    wmy = repair_module.RECIPES["wmy"]
    concentrations = {row["preferred_term"]: row["concentration"] for row in wmy["ingredients"]}
    assert concentrations["Yeast extract"] == {"value": "0.002", "unit": "G_PER_L"}
    assert concentrations["Malt extract"] == {"value": "0.002", "unit": "G_PER_L"}
    assert wmy["ph_range"] == {"min": 6.0, "max": 7.0}

    sna = repair_module.RECIPES["2sna"]
    assert sna["physical_state"] == "SOLID_AGAR"
    assert repair_module.ingredient_signature(sna["ingredients"]) == (
        ("Nutrient agar (Oxoid CM3)", "28.0", "G_PER_L"),
        ("NaCl", "35.0", "G_PER_L"),
        ("Filtered natural seawater", "1", "L"),
    )


def test_empty_record_repair_removes_incomplete_flag(repair_module) -> None:
    target = next(target for target in repair_module.TARGETS if target.recipe_key == "wmy")
    doc = {
        "id": target.record_id,
        "notes": "Source: CCAP",
        "ingredients": [],
        "preparation_steps": [{"step_number": 1, "action": "MIX", "description": "Coming soon"}],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
    }

    repaired, changed = repair_module.repair_document(doc, target)

    assert changed
    assert "data_quality_flags" not in repaired
    assert repair_module.source_note(target) in repaired["notes"]
    assert repaired["curation_history"][-1]["action"] == repair_module.ACTION
    assert repaired["ingredients"] == repair_module.RECIPES["wmy"]["ingredients"]


def test_flattened_nss_guard_and_idempotence(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.precondition == "flattened_nss"
    )
    doc = {
        "id": target.record_id,
        "notes": "Source: CCAP",
        "ingredients": [
            {
                "preferred_term": name,
                "concentration": {"value": value, "unit": unit},
            }
            for name, value, unit in repair_module.FLATTENED_NSS_SIGNATURE
        ],
        "curation_history": [],
    }

    repaired, changed = repair_module.repair_document(doc, target)
    repaired["solutions"][0]["composition"][0]["curation_metadata"] = {"mapping_quality": "MANUAL"}
    second, changed_again = repair_module.repair_document(repaired, target)

    assert changed
    assert not changed_again
    assert second == repaired


def test_flattened_nss_drift_is_rejected(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.precondition == "flattened_nss"
    )
    doc = {
        "id": target.record_id,
        "ingredients": [
            {
                "preferred_term": name,
                "concentration": {"value": value, "unit": unit},
            }
            for name, value, unit in repair_module.FLATTENED_NSS_SIGNATURE
        ],
    }
    doc["ingredients"][0]["concentration"]["value"] = "14"

    with pytest.raises(ValueError, match="signature drifted"):
        repair_module.repair_document(doc, target)


def test_source_hash_mismatch_is_rejected(repair_module, tmp_path: Path) -> None:
    for name in repair_module.SOURCE_FILES:
        (tmp_path / name).write_bytes(b"not the reviewed source")

    with pytest.raises(ValueError, match="SHA-256"):
        repair_module.validate_source_files(tmp_path)


def test_target_records_are_in_guarded_pre_or_post_state(repair_module) -> None:
    repair_module._validate_inventory()
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.relative_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert doc["id"] == target.record_id
        if repair_module.history_has_action(doc):
            repair_module._assert_applied(doc, target)
        else:
            repair_module._validate_precondition(copy.deepcopy(doc), target)
