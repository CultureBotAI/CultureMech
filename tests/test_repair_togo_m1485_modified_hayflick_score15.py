from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1485_modified_hayflick_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m1485_modified_hayflick_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1485")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "modified_hayflick_medium",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M1485",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _component(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_SOLUTION_SIGNATURE
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_splits_merged_water_and_stock_solution(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["ph_value"] == 7.8
    assert "temperature_value" not in repaired
    assert (
        repair_module._signature(repaired["ingredients"], "ingredients")
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert (
        repair_module._signature(repaired["solutions"], "solutions")
        == repair_module.FINAL_SOLUTION_SIGNATURE
    )
    assert (
        repair_module._signature(
            repaired["solutions"][0]["composition"], "solutions[0].composition"
        )
        == repair_module.YEAST_STOCK_SIGNATURE
    )
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_corrects_stock_addition_volumes(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients[repair_module.CALF_THYMUS_DNA]["concentration"] == {
        "value": "12.0",
        "unit": "ML_PER_L",
    }
    assert ingredients[repair_module.THALLIUM_ACETATE]["concentration"] == {
        "value": "10.0",
        "unit": "ML_PER_L",
    }
    assert ingredients[repair_module.PENICILLIN_G]["concentration"] == {
        "value": "25.0",
        "unit": "ML_PER_L",
    }


def test_repair_grounds_machine_usable_components(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    stock = _by_name(repaired["solutions"][0]["composition"])

    assert ingredients[repair_module.WATER]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert ingredients[repair_module.BACTO_AGAR]["term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert ingredients[repair_module.HORSE_SERUM]["term"] == {
        "id": "MICRO:0001235",
        "label": "Horse serum",
    }
    assert stock[repair_module.BAKERS_YEAST]["term"] == {
        "id": "FOODON:03413797",
        "label": "Baker's yeast",
    }


def test_repair_keeps_catalog_and_source_qualified_products_unmapped(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    for name in (repair_module.HEART_INFUSION, repair_module.CALF_THYMUS_DNA):
        assert "term" not in ingredients[name]
        assert "intentionally unmapped" in ingredients[name]["notes"] or (
            "opaque" in ingredients[name]["notes"]
        )


def test_repair_adds_preparation_steps(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["sterilization"] == repair_module.STERILIZATION
    assert repaired["preparation_steps"] == repair_module.PREPARATION_STEPS


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice == once
    assert once["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
    ]
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert "Split the merged water row" in matching_events[0]["notes"]
