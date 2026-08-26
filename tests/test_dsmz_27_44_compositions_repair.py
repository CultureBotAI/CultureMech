from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_27_44_compositions.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_dsmz_27_44_compositions", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return load_script()


def _solution(recipe: dict, name: str) -> dict:
    return next(row for row in recipe["solutions"] if row["preferred_term"] == name)


def test_inventory_and_selected_identities(repair_module) -> None:
    repair_module._validate_inventory()
    assert len(repair_module.TARGETS) == 3
    assert len(repair_module.MIM_TERMS) == 20
    if not repair_module.MIM_SSSOM.is_file():
        pytest.skip("authoritative MIM SSSOM sibling is unavailable")
    repair_module.validate_mim_terms(repair_module.MIM_SSSOM)


def test_stock_boundaries_and_effective_concentrations(repair_module) -> None:
    target = repair_module.TARGETS[0]
    recipe = repair_module.recipe_for(target)

    vitamin = _solution(recipe, "Vitamin B12 solution (10 mg in 100 ml water)")
    assert vitamin["concentration"] == {"value": "0.40", "unit": "ML_PER_L"}
    assert vitamin["composition"][0]["concentration"] == {
        "value": "0.10",
        "unit": "G_PER_L",
    }
    assert 0.10 * 0.40 / 1000 == pytest.approx(0.00004)

    resazurin = _solution(recipe, "Resazurin solution (0.1%)")
    assert resazurin["concentration"] == {"value": "0.50", "unit": "ML_PER_L"}
    assert 1.00 * 0.50 / 1000 == pytest.approx(0.0005)

    trace = _solution(recipe, "Trace element solution SL-6")
    assert trace["concentration"] == {"value": "1.00", "unit": "ML_PER_L"}
    zinc = next(row for row in trace["composition"] if row["preferred_term"] == "ZnSO4 x 7 H2O")
    assert zinc["concentration"] == {"value": "0.10", "unit": "G_PER_L"}


def test_vitamin_b12_is_not_narrowed_to_cyanocobalamin(repair_module) -> None:
    recipe = repair_module.recipe_for(repair_module.TARGETS[0])
    vitamin = _solution(recipe, "Vitamin B12 solution (10 mg in 100 ml water)")
    row = vitamin["composition"][0]
    assert row["term"] == {"id": "CHEBI:176843", "label": "vitamin B12"}
    assert row["mediaingredientmech_chebi_term"] == row["term"]


def test_explicit_duplicate_relationships_are_reciprocal(repair_module) -> None:
    recipes = {
        target.relative_path: repair_module.recipe_for(target) for target in repair_module.TARGETS
    }
    canonical = recipes[repair_module.CANONICAL_PATH]
    assert {row["id"] for row in canonical["variant_children"]} == {
        "CultureMech:004707",
        "CultureMech:001559",
    }
    for path in (repair_module.KOMODO_PATH, repair_module.DSMZ44_PATH):
        assert recipes[path]["parent_media"]["id"] == "CultureMech:001375"
        assert recipes[path]["variant_relationship"] == "SOURCE_DUPLICATE"


def test_repair_is_guarded_and_idempotent(repair_module) -> None:
    target = repair_module.TARGETS[2]
    doc = {
        "id": target.record_id,
        "notes": "Source retained",
        "ingredients": [],
        "data_quality_flags": ["incomplete_composition"],
        "curation_history": [],
    }
    repaired, changed = repair_module.repair_document(doc, target)
    second, changed_again = repair_module.repair_document(copy.deepcopy(repaired), target)

    assert changed
    assert not changed_again
    assert second == repaired
    assert "data_quality_flags" not in repaired
    assert repaired["curation_history"][-1]["action"] == repair_module.ACTION


def test_flattened_precondition_drift_is_rejected(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = {
        "id": target.record_id,
        "ingredients": [repair_module.ingredient("Yeast extract", "0.3", "G_PER_L")],
    }
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
