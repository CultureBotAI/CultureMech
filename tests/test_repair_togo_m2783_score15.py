from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2783_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2783_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2783")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "nutrient_broth",
        "original_name": "Nutrient broth",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2783",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "Nutrient broth",
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_stock_and_water_units(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert (
        repair_module._signature(
            repaired["solutions"],
            "solutions",
        )
        == repair_module.FINAL_SOLUTION_SIGNATURE
    )
    assert _by_name(repaired["ingredients"])["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert _by_name(repaired["solutions"])["20% Glucose"]["concentration"] == {
        "value": "25.0",
        "unit": "ML_PER_L",
    }
    assert _by_name(repaired["solutions"])["1M MgSO4"]["concentration"] == {
        "value": "1.0",
        "unit": "ML_PER_L",
    }


def test_repair_grounds_machine_usable_components(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert ingredients["Nutrient broth"]["notes"].endswith(
        "complex product remains intentionally unmapped."
    )
    assert "term" not in ingredients["Nutrient broth"]
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients["K2HPO4 (anhydrous)"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:131527",
        "label": "dipotassium hydrogen phosphate",
    }
    assert ingredients["KH2PO4"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:63036",
        "label": "potassium dihydrogen phosphate",
    }
    assert solutions["20% Glucose"]["term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert solutions["1M MgSO4"]["term"] == {
        "id": "CHEBI:32599",
        "label": "magnesium sulfate",
    }


def test_repair_adds_m2783_preparation_step(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert "ph_value" not in repaired
    assert "sterilization" not in repaired


def test_repair_record_drops_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
        "has_unmapped_ingredients",
    ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_target(_doc(repair_module))
    twice = repair_module.repair_target(once)

    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert "1 M MgSO4, 20% glucose, and distilled-water units" in matching_events[0]["notes"]


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:000000"

    with pytest.raises(ValueError, match="expected id"):
        repair_module.repair_target(doc)
