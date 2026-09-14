from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m3294_hm_buffer_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m3294_hm_buffer_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m3294")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


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
        "name": "hm_buffer",
        "original_name": "HM Buffer",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M3294",
            "term": {"id": repair_module.EXPECTED_MEDIA_TERM, "label": "HM Buffer"},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _composition in (repair_module.IMPORTED_SOLUTION_SIGNATURE)
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_normalizes_source_volumes_and_expands_stocks(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repair_module._solution_signature(repaired["solutions"], "solutions") == (
        repair_module.FINAL_SOLUTION_SIGNATURE
    )
    assert repaired["medium_type"] == "DEFINED"
    assert repaired["composition_type"] == "DEFINED"
    assert repaired["ph_value"] == 7.4
    assert ingredients["UPW"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["UPW"]["term"] == {"id": "CHEBI:15377", "label": "water"}
    assert solutions["0.5 M HEPES"]["concentration"] == {
        "value": "50.0",
        "unit": "ML_PER_L",
    }
    assert solutions["0.5 M HEPES"]["composition"][0]["term"] == {
        "id": "CHEBI:46756",
        "label": "HEPES",
    }
    assert solutions["0.5 M CaCl2 solution"]["composition"][0]["term"] == {
        "id": "CHEBI:3312",
        "label": "calcium dichloride",
    }
    assert solutions["0.6 M MgCl2 solution"]["concentration"] == {
        "value": "3.33",
        "unit": "ML_PER_L",
    }
    assert solutions["0.6 M MgCl2 solution"]["composition"][0]["concentration"] == {
        "value": "0.6",
        "unit": "MOLAR",
    }
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_adds_preparation_flags_references_and_event_once(
    repair_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice == once
    assert once["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert once["sterilization"] == repair_module.STERILIZATION
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert once["references"] == [
        {"reference": repair_module.TOGO_M3294},
        {"reference": repair_module.NBRC_1663},
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


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"] = {
        "value": "50.0",
        "unit": "ML_PER_L",
    }

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["concentration"] = {"value": "6.0", "unit": "ML_PER_L"}

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)
