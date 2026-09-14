from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1338_marine_pyruvate_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m1338_marine_pyruvate_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1338")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _target_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": repair_module.TARGET.stem,
        "original_name": "Marine Broth 2216 With Pyruvate",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M1338",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "Marine Broth 2216 With Pyruvate",
            },
        },
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _component(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_SOLUTION_SIGNATURE
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_restores_togo_formula_and_scores_zero(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_target(_target_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repair_module._signature(repaired["solutions"], "solutions") == (
        repair_module.FINAL_SOLUTION_SIGNATURE
    )
    assert repaired["ph_value"] == 8.0
    assert ingredients["Marine Broth 2216 (BD-Difco)"]["concentration"] == {
        "value": "37.4",
        "unit": "G_PER_L",
    }
    assert "term" not in ingredients["Marine Broth 2216 (BD-Difco)"]
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert ingredients["Distilled water"]["term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert solutions["1.0 M Sodium pyruvate solution"]["composition"] == [
        {
            "preferred_term": "Sodium pyruvate",
            "concentration": {"value": "1.0", "unit": "MOLAR"},
            "term": {"id": "CHEBI:50144", "label": "sodium pyruvate"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:50144",
                "label": "sodium pyruvate",
            },
        }
    ]
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert repaired["sterilization"] == {"method": "AUTOCLAVE"}
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.repair_target(_target_doc(repair_module))
    twice = repair_module.repair_target(once)

    assert twice == once


def test_repair_adds_flags_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_target(_target_doc(repair_module))
    twice = repair_module.repair_target(once)

    assert twice == once
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert once["references"] == [{"reference": repair_module.TOGO_M1338}]
    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _target_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_target(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _target_doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:other"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_target(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _target_doc(repair_module)
    doc["ingredients"][0]["concentration"]["unit"] = "ML_PER_L"

    with pytest.raises(ValueError, match="ingredient signature"):
        repair_module.repair_target(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _target_doc(repair_module)
    doc["solutions"][0]["concentration"]["unit"] = "ML_PER_L"

    with pytest.raises(ValueError, match="solution signature"):
        repair_module.repair_target(doc)
