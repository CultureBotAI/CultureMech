from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m154_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m154_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m154")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "composition": [],
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "pplo_glucose_broth",
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
            "preferred_term": "TOGO Medium M154",
            "term": {"id": repair_module.EXPECTED_MEDIA_TERM, "label": repair_module.TITLE},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_liquid_units_and_ph(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "UNDEFINED"
    assert repaired["physical_state"] == "LIQUID"
    assert repaired["ph_value"] == 7.6
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )

    water = _by_name(repaired["ingredients"])["Distilled water"]
    serum = _by_name(repaired["ingredients"])["Sterile horse serum"]
    assert water["concentration"] == {"value": "700.0", "unit": "ML_PER_L"}
    assert serum["concentration"] == {"value": "200.0", "unit": "ML_PER_L"}


def test_repair_grounds_discrete_components(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    phenol = repaired["solutions"][0]["composition"][0]

    assert ingredients["Glucose"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert ingredients["Penicillin"]["term"] == {
        "id": "CHEBI:17334",
        "label": "penicillin",
    }
    assert phenol["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:31991",
        "label": "phenol red",
    }


def test_repair_keeps_pplo_serum_and_yeast_extract_solution_opaque(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert "term" not in ingredients["PPLO broth (BD-Difco)"]
    assert "term" not in ingredients["Sterile horse serum"]
    assert (
        solutions["25% Solution of fresh baker's yeast extract (Gibco 360-8180)"]["composition"]
        == []
    )


def test_repair_keeps_penicillin_as_variable_activity_amount(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    penicillin = _by_name(repaired["ingredients"])["Penicillin"]
    assert penicillin["concentration"] == {"value": "variable", "unit": "VARIABLE"}
    assert "1,000,000 U" in penicillin["notes"]


def test_repair_represents_phenol_red_stock_solution(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repair_module._solution_signatures(repaired) == (repair_module.FINAL_SOLUTION_SIGNATURES)
    phenol_solution = repaired["solutions"][0]
    assert phenol_solution["concentration"] == {
        "value": "5.0",
        "unit": "ML_PER_L",
    }
    assert phenol_solution["composition"][0]["concentration"] == {
        "value": "0.4",
        "unit": "PERCENT_W_V",
    }


def test_repair_does_not_invent_temperature_or_sterilization(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert "temperature_value" not in repaired
    assert "temperature_range" not in repaired
    assert "sterilization" not in repaired
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 7.6.",
        }
    ]


def test_repair_record_drops_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["references"] == [{"reference": url} for url in repair_module.REFERENCES]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert "Corrected ml import artifacts" in matching_events[0]["notes"]


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Water", "700", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0] = _solution("Phenol red solution", "5", "G_PER_L")

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_togo_m154_repair_contract(
    repair_module,
) -> None:
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
