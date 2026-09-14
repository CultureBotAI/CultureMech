from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m681_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m681_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_m681")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "nutrient_broth",
        "original_name": "Nutrient Broth",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M681",
            "term": {"id": repair_module.EXPECTED_MEDIA_TERM, "label": "Nutrient Broth"},
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "data_quality_flags": ["incomplete_composition", "resolved_reference"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_togo_m681_corrects_jcm_formula(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repaired["ph_value"] == 7.0
    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["physical_state"] == "LIQUID"
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_togo_m681_sets_groundings_and_roles(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "peptone",
    }
    assert ingredients["Peptone"]["nutritional_roles"] == ["NITROGEN_SOURCE"]
    assert ingredients["Beef extract"]["term"] == {
        "id": "FOODON:03302088",
        "label": "beef extract",
    }
    assert ingredients["Beef extract"]["nutritional_roles"] == ["NITROGEN_SOURCE"]
    assert "mediaingredientmech_chebi_term" not in ingredients["Peptone"]
    assert "mediaingredientmech_chebi_term" not in ingredients["Beef extract"]
    assert ingredients["Distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }


def test_repair_togo_m681_adds_default_jcm_autoclaving(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert repaired["preparation_steps"] == [
        dict(step) for step in repair_module.PREPARATION_STEPS
    ]
    assert repaired["sterilization"] == repair_module.STERILIZATION
    assert [step["action"] for step in repaired["preparation_steps"]] == [
        "MIX",
        "ADJUST_PH",
        "AUTOCLAVE",
    ]


def test_repair_togo_m681_sets_flags_references_and_event_once(
    repair_module,
) -> None:
    once = repair_module.repair_target(_doc(repair_module))
    twice = repair_module.repair_target(once)

    assert twice == once
    assert once["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
    ]
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    matching_events = [
        event
        for event in once["curation_history"]
        if event.get("curator") == repair_module.CURATOR
        and event.get("action") == repair_module.ACTION
    ]
    assert len(matching_events) == 1
    assert "distilled-water unit" in matching_events[0]["notes"]


def test_repair_togo_m681_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_target(doc)


def test_repair_togo_m681_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"].pop()

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_target(doc)
