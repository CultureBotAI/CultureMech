from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_r2a_family.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_jcm_r2a_family", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return load_script()


def test_inventory_and_selected_identities(repair_module) -> None:
    repair_module._validate_inventory()
    assert len(repair_module.TARGETS) == 3
    assert len(repair_module.MIM_TERMS) == 11
    if not repair_module.MIM_SSSOM.is_file():
        pytest.skip("authoritative MIM SSSOM sibling is unavailable")
    repair_module.validate_mim_terms(repair_module.MIM_SSSOM)


def test_jcm_346_and_1091_include_printed_water(repair_module) -> None:
    for target in repair_module.TARGETS[:2]:
        recipe = repair_module.recipe_for(target)
        water = next(
            row for row in recipe["ingredients"] if row["preferred_term"] == "Distilled water"
        )
        assert water["concentration"] == {"value": "1.0", "unit": "L"}
        assert recipe["sterilization"] == {"method": "AUTOCLAVE"}
        assert recipe["physical_state"] == "SOLID_AGAR"


def test_five_x_source_values_are_consistent(repair_module) -> None:
    recipe = repair_module.recipe_for(repair_module.TARGETS[1])
    values = {row["preferred_term"]: row["concentration"]["value"] for row in recipe["ingredients"]}
    assert values["Yeast extract"] == "2.5"
    assert values["Sodium pyruvate"] == "1.5"
    assert values["MgSO4 x 7 H2O"] == "0.25"
    assert values["Agar"] == "15.0"


def test_ph9_variant_preserves_unspecified_carbonate_volume(repair_module) -> None:
    recipe = repair_module.recipe_for(repair_module.TARGETS[2])
    carbonate = recipe["solutions"][0]
    assert carbonate["concentration"] == {"value": "variable", "unit": "VARIABLE"}
    assert carbonate["composition"][0]["term"] == {
        "id": "CHEBI:29377",
        "label": "sodium carbonate",
    }
    assert carbonate["composition"][0]["concentration"] == {
        "value": "100",
        "unit": "G_PER_L",
    }
    assert recipe["physical_state"] == "SOLID_AGAR"
    assert recipe["ph_value"] == 9.0


def test_variant_relationships_are_reciprocal(repair_module) -> None:
    recipes = {
        target.relative_path: repair_module.recipe_for(target) for target in repair_module.TARGETS
    }
    children = recipes[repair_module.BASE_PATH]["variant_children"]
    assert {(row["id"], row["relationship"]) for row in children} == {
        ("CultureMech:002271", "CONCENTRATION_VARIANT"),
        ("CultureMech:002475", "PH_VARIANT"),
    }
    assert recipes[repair_module.FIVE_X_PATH]["parent_media"]["id"] == "CultureMech:002706"
    assert recipes[repair_module.PH9_PATH]["parent_media"]["id"] == "CultureMech:002706"


def test_repair_is_guarded_and_idempotent(repair_module) -> None:
    target = repair_module.TARGETS[2]
    doc = {
        "id": target.record_id,
        "notes": "Source retained",
        "ingredients": [],
        "data_quality_flags": ["incomplete_composition", "source_information_unavailable"],
        "curation_history": [],
    }
    repaired, changed = repair_module.repair_document(doc, target)
    second, changed_again = repair_module.repair_document(copy.deepcopy(repaired), target)
    assert changed
    assert not changed_again
    assert second == repaired
    assert "data_quality_flags" not in repaired


def test_parsed_precondition_drift_is_rejected(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = {"id": target.record_id, "ingredients": []}
    with pytest.raises(ValueError, match="pre-state drifted"):
        repair_module.repair_document(doc, target)


def test_source_hash_mismatch_is_rejected(repair_module, tmp_path: Path) -> None:
    for file_name in repair_module.SOURCE_FILES:
        (tmp_path / file_name).write_bytes(b"not the reviewed source")
    with pytest.raises(ValueError, match="SHA-256"):
        repair_module.validate_source_files(tmp_path)


def test_target_records_are_in_guarded_pre_or_post_state(repair_module) -> None:
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.relative_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert doc["id"] == target.record_id
        if repair_module.history_has_action(doc):
            repair_module._assert_applied(doc, target)
        else:
            repair_module._validate_precondition(copy.deepcopy(doc), target)
