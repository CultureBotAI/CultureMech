from __future__ import annotations

import copy
import importlib.util
import sys
from dataclasses import replace
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_833_family.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_dsmz_833_family", SCRIPT)
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
    repair_module.validate_mim_terms(repair_module.MIM_SSSOM)
    assert len(repair_module.TARGETS) == 3
    assert len(repair_module.MIM_TERMS) == 41


def test_final_volume_scaling_uses_1003_ml_batch(repair_module) -> None:
    recipe = repair_module.recipe_for(repair_module.TARGETS[0])
    direct = {row["preferred_term"]: row["concentration"] for row in recipe["ingredients"]}
    assert direct["Na2SO4"] == {"value": "0.697906", "unit": "G_PER_L"}
    assert direct["Distilled water"] == {
        "value": "887.337986",
        "unit": "ML_PER_L",
    }
    assert 0.70 / 1.003 == pytest.approx(0.697906, abs=1e-6)
    assert 890 / 1.003 == pytest.approx(887.337986, abs=1e-6)


def test_embedded_solution_a_stocks_remain_structured(repair_module) -> None:
    recipe = repair_module.recipe_for(repair_module.TARGETS[0])
    trace = _solution(recipe, "Trace element solution SL-10")
    assert trace["concentration"] == {"value": "0.997009", "unit": "ML_PER_L"}
    manganese = next(
        row for row in trace["composition"] if row["preferred_term"] == "MnCl2 x 4 H2O"
    )
    assert manganese["concentration"] == {"value": "0.100", "unit": "G_PER_L"}
    resazurin = _solution(recipe, "Sodium resazurin solution (0.1% w/v)")
    assert resazurin["concentration"] == {"value": "0.498504", "unit": "ML_PER_L"}


def test_distinct_vitamin_stocks_are_not_merged(repair_module) -> None:
    recipe = repair_module.recipe_for(repair_module.TARGETS[0])
    wolin = _solution(recipe, "Solution C1: Wolin's vitamin solution (10x)")
    seven = _solution(recipe, "Solution C2: seven vitamins solution")
    wolin_b12 = next(row for row in wolin["composition"] if row["preferred_term"] == "Vitamin B12")
    seven_b12 = next(row for row in seven["composition"] if row["preferred_term"] == "Vitamin B12")
    assert wolin_b12["concentration"] == {"value": "0.001", "unit": "G_PER_L"}
    assert seven_b12["concentration"] == {"value": "0.100", "unit": "G_PER_L"}


def test_solution_d_to_h_math(repair_module) -> None:
    recipe = repair_module.recipe_for(repair_module.TARGETS[0])
    carbonate = _solution(recipe, "Solution D: Na2CO3 solution")
    assert carbonate["concentration"] == {"value": "34.895314", "unit": "ML_PER_L"}
    assert carbonate["composition"][0]["concentration"] == {
        "value": "50.0",
        "unit": "G_PER_L",
    }
    iron = _solution(recipe, "Solution G: FeSO4 in 0.1 N H2SO4")
    assert iron["composition"][0]["concentration"] == {
        "value": "10.0",
        "unit": "G_PER_L",
    }


def test_source_duplicates_are_reciprocal(repair_module) -> None:
    recipes = {target.relative_path: repair_module.recipe_for(target) for target in repair_module.TARGETS}
    assert {row["id"] for row in recipes[repair_module.CANONICAL_PATH]["variant_children"]} == {
        "CultureMech:006625",
        "CultureMech:009034",
    }
    for path in (repair_module.KOMODO_PATH, repair_module.TOGO_PATH):
        assert recipes[path]["parent_media"]["id"] == "CultureMech:001990"
        assert recipes[path]["variant_relationship"] == "SOURCE_DUPLICATE"


def test_repair_is_guarded_and_idempotent(repair_module) -> None:
    base_target = repair_module.TARGETS[0]
    doc = {
        "id": base_target.record_id,
        "ingredients": [],
        "solutions": [],
        "curation_history": [],
    }
    target = replace(base_target, expected_pre_hash=repair_module.composition_hash(doc))
    repaired, changed = repair_module.repair_document(doc, target)
    second, changed_again = repair_module.repair_document(copy.deepcopy(repaired), target)
    assert changed
    assert not changed_again
    assert second == repaired


def test_source_hash_mismatch_is_rejected(repair_module, tmp_path: Path) -> None:
    (tmp_path / repair_module.SOURCE_FILE).write_bytes(b"not the reviewed source")
    with pytest.raises(ValueError, match="SHA-256"):
        repair_module.validate_source_file(tmp_path)


def test_target_records_are_in_guarded_pre_or_post_state(repair_module) -> None:
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.relative_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert doc["id"] == target.record_id
        if repair_module.history_has_action(doc):
            repair_module._assert_applied(doc, target)
        else:
            repair_module._validate_precondition(copy.deepcopy(doc), target)
