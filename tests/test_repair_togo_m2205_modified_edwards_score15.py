from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2205_modified_edwards_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2205_modified_edwards_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2205")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "modified_edwards_medium",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2205",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": [
            "incomplete_composition",
            "needs_manual_curation",
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_adds_source_ph_and_temperature(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["ph_value"] == 7.6
    assert repaired["temperature_value"] == 37.0
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )


def test_repair_grounds_chemicals_and_complex_products(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["NaOAc"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:32954",
        "label": "sodium acetate",
    }
    assert ingredients["Horse serum"]["term"] == {
        "id": "MICRO:0001235",
        "label": "Horse serum",
    }
    assert ingredients["Tryptose"]["term"] == {
        "id": "MICRO:0000183",
        "label": "Tryptose",
    }


def test_repair_keeps_yeast_dialysate_unmapped(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    yeast_dialysate = _by_name(repaired["ingredients"])["Yeast dialysate"]

    assert "term" not in yeast_dialysate
    assert "mediaingredientmech_chebi_term" not in yeast_dialysate
    assert "intentionally unmapped" in yeast_dialysate["notes"]


def test_repair_adds_references_flags_and_event_once(
    repair_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice == once
    assert once["references"] == [{"reference": repair_module.TOGO_M2205}]
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
    assert "Yeast dialysate" in matching_events[0]["notes"]


def test_repair_record_drops_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []
