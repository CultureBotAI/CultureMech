from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_sag_missing_compositions.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_sag_missing_compositions", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return load_script()


def _solution(recipe: dict, name: str) -> dict:
    return next(row for row in recipe["solutions"] if row["preferred_term"] == name)


def _ingredient(recipe: dict, name: str) -> dict:
    return next(row for row in recipe["ingredients"] if row["preferred_term"] == name)


def test_inventory_covers_all_29_sag_sources(repair_module) -> None:
    repair_module._validate_inventory()
    assert len(repair_module.TARGETS) == 29
    assert len(repair_module.SOURCES) == 29
    assert len(repair_module.RECIPES) == 29
    assert {target.source_key for target in repair_module.TARGETS} == set(repair_module.SOURCES)


def test_selected_identities_exist_in_actual_mim_sssom(repair_module) -> None:
    def walk(rows: list[dict]):
        for row in rows:
            yield row
            yield from walk(row.get("composition") or [])

    for recipe in repair_module.RECIPES.values():
        for row in walk((recipe.get("ingredients") or []) + (recipe.get("solutions") or [])):
            term = row.get("term")
            chebi = row.get("mediaingredientmech_chebi_term")
            if term and str(term["id"]).startswith("CHEBI:"):
                assert chebi == term
            else:
                assert chebi is None

    if not repair_module.MIM_SSSOM.is_file():
        pytest.skip("authoritative MIM SSSOM sibling is unavailable")
    repair_module.validate_mim_terms(repair_module.MIM_SSSOM)


def test_shared_sag_stock_math_preserves_stock_boundary(repair_module) -> None:
    basal = repair_module.RECIPES["basal"]
    assert _ingredient(basal, "Deionized or distilled water")["concentration"] == {
        "value": "905",
        "unit": "ML_PER_L",
    }
    nitrate = _solution(basal, "KNO3 stock solution")
    assert nitrate["concentration"] == {"value": "20", "unit": "ML_PER_L"}
    assert nitrate["composition"][0]["concentration"] == {
        "value": "10",
        "unit": "G_PER_L",
    }

    micro = _solution(basal, "SAG medium 1 micronutrient solution")
    concentrations = {row["preferred_term"]: row["concentration"] for row in micro["composition"]}
    assert concentrations["ZnSO4 x 7 H2O"] == {
        "value": "1",
        "unit": "MG_PER_L",
    }
    assert concentrations["FeSO4 x 7 H2O"] == {
        "value": "700",
        "unit": "MG_PER_L",
    }


def test_half_batch_and_primary_stock_calculations(repair_module) -> None:
    spirulina = repair_module.RECIPES["spirulina"]
    solution_i = _solution(spirulina, "Spirulina solution I")
    assert solution_i["concentration"] == {"value": "500", "unit": "ML_PER_L"}
    assert solution_i["composition"][0]["concentration"] == {
        "value": "27.22",
        "unit": "G_PER_L",
    }

    f2 = repair_module.RECIPES["enriched_seawater"]
    trace = _solution(f2, "f/2 micronutrient working stock solution")
    copper = next(row for row in trace["composition"] if row["preferred_term"] == "CuSO4 x 5 H2O")
    assert copper["concentration"] == {"value": "9.8", "unit": "MG_PER_L"}
    assert all("Na2SiO3" not in row["preferred_term"] for row in f2["solutions"])
    assert "diatom" in " ".join(row["description"] for row in f2["preparation_steps"]).lower()


def test_soil_water_note_is_typed_source_duplicate(repair_module) -> None:
    medium = repair_module.RECIPES["soil_water"]
    note = repair_module.RECIPES["soil_water_note"]

    assert medium["physical_state"] == "BIPHASIC"
    assert medium["sterilization"]["method"] == "TYNDALLIZATION"
    assert medium["variant_children"][0]["id"] == "CultureMech:000205"
    assert note["parent_media"]["id"] == "CultureMech:000212"
    assert note["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repair_module.recipe_projection(note)["ingredients"] == (
        repair_module.recipe_projection(medium)["ingredients"]
    )


def test_complex_source_examples(repair_module) -> None:
    wc = repair_module.RECIPES["wc"]
    bicarbonate = _solution(wc, "NaHCO3 stock solution")
    assert bicarbonate["composition"][0]["term"] == {
        "id": "CHEBI:32139",
        "label": "sodium hydrogencarbonate",
    }

    pes = repair_module.RECIPES["pes"]
    enrichment = _solution(pes, "PES ES-enrichment solution")
    ferrous = next(
        row
        for row in enrichment["composition"]
        if row["preferred_term"] == "Fe(NH4)2(SO4)2 x 6 H2O"
    )
    assert ferrous["concentration"] == {
        "value": "175.5",
        "unit": "MG_PER_L",
    }

    tom = repair_module.RECIPES["bold_modified_basal_tom"]
    assert _ingredient(tom, "Glucose")["concentration"] == {
        "value": "15",
        "unit": "G_PER_L",
    }
    assert tom["ph_range"] == {"min": 7.1, "max": 7.1}
    assert "not asserted" in tom["preparation_steps"][3]["description"]


def test_ambiguous_identity_is_not_invented(repair_module) -> None:
    recipe = repair_module.RECIPES["dunaliella_acid"]
    ammonium_nitrate = _ingredient(recipe, "NH4NO3")
    assert "term" not in ammonium_nitrate
    assert "mediaingredientmech_chebi_term" not in ammonium_nitrate


def test_repair_is_guarded_and_idempotent(repair_module) -> None:
    target = next(target for target in repair_module.TARGETS if target.recipe_key == "basal")
    doc = {
        "id": target.record_id,
        "notes": "SAG source retained",
        "ingredients": [],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
    }

    repaired, changed = repair_module.repair_document(doc, target)
    repaired["ingredients"][0]["curation_metadata"] = {"mapping_quality": "MANUAL"}
    second, changed_again = repair_module.repair_document(repaired, target)

    assert changed
    assert not changed_again
    assert second == repaired
    assert "data_quality_flags" not in repaired
    assert repaired["curation_history"][-1]["action"] == repair_module.ACTION


def test_precondition_drift_is_rejected(repair_module) -> None:
    target = next(target for target in repair_module.TARGETS if target.recipe_key == "basal")
    doc = {
        "id": target.record_id,
        "ingredients": [repair_module.ingredient("KNO3", "1", "G_PER_L")],
        "data_quality_flags": ["incomplete_composition"],
    }
    with pytest.raises(ValueError, match="no longer composition-empty"):
        repair_module.repair_document(doc, target)


def test_source_hash_mismatch_is_rejected(repair_module, tmp_path: Path) -> None:
    for source in repair_module.SOURCES.values():
        (tmp_path / source.file_name).write_bytes(b"not the reviewed source")

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
