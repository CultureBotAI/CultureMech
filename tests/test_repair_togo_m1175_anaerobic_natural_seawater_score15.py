from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1175_anaerobic_natural_seawater_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m1175_anaerobic_natural_seawater")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1175")


def _component(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
    }


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
        "name": "Unknown solution",
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "anaerobic_natural_seawater_medium",
        "original_name": "Anaerobic Natural Seawater Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M1175",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "Anaerobic Natural Seawater Medium",
            },
        },
        "notes": "Source: TOGO M1175",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_jcm_1102_base_and_drops_from_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["ph_value"] == 7.0
    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "250.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Natural seawater (filtrated)"]["concentration"] == {
        "value": "750.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Resazurin"]["concentration"] == {
        "value": "0.5",
        "unit": "MG_PER_L",
    }
    assert ingredients["N2"]["term"] == {"id": "CHEBI:17997", "label": "dinitrogen"}
    assert "term" not in ingredients["Tryptone"]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_expands_reducer_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    assert repair_module._solution_signatures(repaired) == (repair_module.FINAL_SOLUTION_SIGNATURES)
    assert solutions["5% L-Cysteine HCl H2O solution"]["concentration"] == {
        "value": "6.0",
        "unit": "ML_PER_L",
    }
    assert solutions["5% Na2S x 9H2O solution"]["concentration"] == {
        "value": "6.0",
        "unit": "ML_PER_L",
    }
    assert solutions["5% L-Cysteine HCl H2O solution"]["composition"][0]["term"] == {
        "id": "CHEBI:91248",
        "label": "L-cysteine hydrochloride hydrate",
    }
    assert solutions["5% Na2S x 9H2O solution"]["composition"][0]["term"] == {
        "id": "CHEBI:76209",
        "label": "sodium sulfide nonahydrate",
    }


def test_repair_adds_preparation_references_flags_and_event_once(
    repair_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert [step["action"] for step in twice["preparation_steps"]] == [
        "MIX",
        "ADJUST_PH",
        "COOL",
        "ALIQUOT",
        "AUTOCLAVE",
        "MIX",
    ]
    assert twice["sterilization"] == repair_module.STERILIZATION
    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
    ]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
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
    assert matching_events[0]["source"] == "; ".join(repair_module.REFERENCES)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M1176"

    with pytest.raises(ValueError, match="expected media term TOGO:M1175"):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _component("Tap water", "250", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0] = _solution("5% Na2S x 9H2O solution", "6", "G_PER_L")

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_togo_m1175_repair_contract(repair_module) -> None:
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
