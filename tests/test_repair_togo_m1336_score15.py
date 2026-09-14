from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1336_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m1336_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1336")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "anaerobaculum_medium",
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
            "preferred_term": "TOGO Medium M1336",
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


def test_repair_corrects_base_formula_and_conditions(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert repaired["ph_value"] == 7.0
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert ingredients["Resazurin"]["concentration"] == {
        "value": "0.5",
        "unit": "MG_PER_L",
    }
    assert ingredients["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "peptone",
    }
    assert "term" not in ingredients["Trypticase peptone"]


def test_repair_expands_salt_solution_from_jcm_676(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    salt = _by_name(solutions["Salt solution"]["composition"])

    assert solutions["Salt solution"]["concentration"] == {
        "value": "40.0",
        "unit": "ML_PER_L",
    }
    assert salt["CaCl2 x 2H2O"]["term"] == {
        "id": "CHEBI:86158",
        "label": "calcium chloride dihydrate",
    }
    assert salt["NaHCO3"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:32139",
        "label": "sodium hydrogencarbonate",
    }


def test_repair_expands_cysteine_glucose_and_thiosulfate_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    assert (
        repair_module._solution_signatures(
            repaired,
        )
        == repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert solutions["5% L-Cysteine HCl H2O solution"]["composition"][0] == {
        "preferred_term": "L-Cysteine HCl H2O",
        "concentration": {"value": "5.0", "unit": "PERCENT_W_V"},
        "source": repair_module.SOURCE,
        "notes": (
            "5% L-Cysteine HCl H2O solution is represented from the stock "
            "label as 5.0 % w/v L-Cysteine HCl H2O."
        ),
        "term": {
            "id": "CHEBI:91248",
            "label": "L-cysteine hydrochloride hydrate",
        },
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:91248",
            "label": "L-cysteine hydrochloride hydrate",
        },
    }
    assert solutions["1 M Glucose solution"]["concentration"] == {
        "value": "6.0",
        "unit": "ML_PER_L",
    }
    assert solutions["1 M Na2S2O3 solution"]["composition"][0]["term"] == {
        "id": "CHEBI:132112",
        "label": "sodium thiosulfate",
    }


def test_repair_adds_preparation_metadata(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["sterilization"]["method"] == "AUTOCLAVE"
    assert [step["action"] for step in repaired["preparation_steps"]] == [
        "MIX",
        "ADJUST_PH",
        "ALIQUOT",
        "AUTOCLAVE",
        "COOL",
        "MIX",
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
    assert "JCM Medium 676 salt solution" in matching_events[0]["notes"]


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
    doc["ingredients"][0] = _ingredient("Water", "960", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["preferred_term"] = "Salt solution"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_togo_m1336_repair_contract(
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
