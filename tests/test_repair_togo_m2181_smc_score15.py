from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2181_smc_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2181_smc")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2181_smc")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(signature) -> dict:
    name, value, unit, composition = signature
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "composition": [
            _ingredient(component, amount, component_unit)
            for component, amount, component_unit in composition
        ],
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "smc_medium",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "solutions": [
            _solution(signature) for signature in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2181",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition", "needs_manual_curation"],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_smc_units_and_stocks(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["ph_value"] == 7.5
    assert (
        repair_module._signature(repaired["ingredients"], "ingredients")
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repair_module._solution_signatures(repaired) == repair_module.FINAL_SOLUTION_SIGNATURES
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_grounds_defined_components_and_keeps_opaque_inputs(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients[repair_module.SORBITOL]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:30911",
        "label": "glucitol",
    }
    assert ingredients[repair_module.TRYPTONE]["term"] == {
        "id": "MICRO:0000182",
        "label": "Tryptone",
    }
    assert "mediaingredientmech_chebi_term" not in ingredients[repair_module.TRYPTONE]
    assert ingredients[repair_module.HORSE_SERUM]["term"] == {
        "id": "MICRO:0001235",
        "label": "Horse serum",
    }
    assert "mediaingredientmech_chebi_term" not in ingredients[repair_module.HORSE_SERUM]
    assert "term" not in ingredients[repair_module.PPLO]


def test_repair_expands_disclosed_percent_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    phenol_red = _by_name(solutions[repair_module.PHENOL_RED_STOCK]["composition"])
    arginine = _by_name(solutions[repair_module.ARGININE_STOCK]["composition"])
    fructose = _by_name(solutions[repair_module.FRUCTOSE_STOCK]["composition"])
    glucose = _by_name(solutions[repair_module.GLUCOSE_STOCK]["composition"])
    sucrose = _by_name(solutions[repair_module.SUCROSE_STOCK]["composition"])

    assert phenol_red["Phenol red"]["term"] == {
        "id": "CHEBI:31991",
        "label": "phenol red",
    }
    assert arginine["L-Arginine HCl"]["term"] == {
        "id": "CHEBI:31235",
        "label": "L-Arginine x HCl",
    }
    assert fructose["Fructose"]["concentration"] == {
        "value": "50.0",
        "unit": "PERCENT_W_V",
    }
    assert glucose["Glucose"]["term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert sucrose["Sucrose"]["term"] == {
        "id": "CHEBI:17992",
        "label": "sucrose",
    }
    assert solutions[repair_module.YEAST_STOCK]["composition"] == []


def test_repair_adds_preparation_steps_flags_references_and_event_once(
    repair_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["sterilization"] == {"method": "AUTOCLAVE"}
    assert [step["action"] for step in twice["preparation_steps"]] == [
        "MIX",
        "ADJUST_PH",
        "AUTOCLAVE",
        "FILTER_STERILIZE",
        "MIX",
    ]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
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
    assert "ATCC Medium 668" in matching_events[0]["notes"]


def test_plan_repairs_targets_smc_record(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET

    assert repair_module.plan_repairs() == {
        path: repair_module.repair_record(yaml.safe_load(path.read_text(encoding="utf-8")))
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M2226"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Tap water", "650", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["concentration"] = {"value": "20", "unit": "ML_PER_L"}

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_corpus_record_matches_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
    assert repair_module._solution_signatures(doc) in (
        repair_module.IMPORTED_SOLUTION_SIGNATURES,
        repair_module.FINAL_SOLUTION_SIGNATURES,
    )
