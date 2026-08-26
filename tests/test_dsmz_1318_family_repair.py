from __future__ import annotations

import copy
import importlib.util
import sys
from dataclasses import replace
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_1318_family.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_dsmz_1318_family", SCRIPT)
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
    assert len(repair_module.MIM_TERMS) == 37


def test_final_volume_scaling_uses_1004_ml_batch(repair_module) -> None:
    recipe = repair_module.recipe_for(repair_module.TARGETS[0])
    direct = {row["preferred_term"]: row["concentration"] for row in recipe["ingredients"]}
    assert direct["MgCl2 x 6 H2O"] == {"value": "0.398406", "unit": "G_PER_L"}
    assert direct["Distilled water"] == {
        "value": "996.015936",
        "unit": "ML_PER_L",
    }
    assert 0.40 / 1.004 == pytest.approx(0.398406, abs=1e-6)


def test_trace_and_resazurin_stocks_are_structured(repair_module) -> None:
    recipe = repair_module.recipe_for(repair_module.TARGETS[0])
    trace = _solution(recipe, "Trace element solution SL-10")
    assert trace["concentration"] == {"value": "0.996016", "unit": "ML_PER_L"}
    assert len(trace["composition"]) == 10
    resazurin = _solution(recipe, "Sodium resazurin solution (0.1% w/v)")
    assert resazurin["concentration"] == {"value": "0.498008", "unit": "ML_PER_L"}


def test_distinct_vitamin_stocks_are_not_merged(repair_module) -> None:
    recipe = repair_module.recipe_for(repair_module.TARGETS[0])
    wolin = _solution(recipe, "Wolin's vitamin solution (10x)")
    seven = _solution(recipe, "Seven vitamins solution")
    wolin_b12 = next(row for row in wolin["composition"] if row["preferred_term"] == "Vitamin B12")
    seven_b12 = next(row for row in seven["composition"] if row["preferred_term"] == "Vitamin B12")
    assert wolin_b12["concentration"] == {"value": "0.001", "unit": "G_PER_L"}
    assert seven_b12["concentration"] == {"value": "0.100", "unit": "G_PER_L"}
    assert wolin_b12["term"] == {"id": "CHEBI:176843", "label": "vitamin B12"}


def test_unspecified_addition_stock_strengths_are_not_invented(repair_module) -> None:
    recipe = repair_module.recipe_for(repair_module.TARGETS[0])
    direct = {row["preferred_term"]: row for row in recipe["ingredients"]}
    for name in ("Na2CO3", "L-Cysteine HCl x H2O", "DL-Dithiothreitol"):
        assert name in direct
        assert "does not specify" in direct[name]["notes"]


def test_source_duplicates_are_reciprocal(repair_module) -> None:
    recipes = {target.relative_path: repair_module.recipe_for(target) for target in repair_module.TARGETS}
    assert {row["id"] for row in recipes[repair_module.CANONICAL_PATH]["variant_children"]} == {
        "CultureMech:004073",
        "CultureMech:009130",
    }
    for path in (repair_module.KOMODO_PATH, repair_module.TOGO_PATH):
        assert recipes[path]["parent_media"]["id"] == "CultureMech:000776"


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
