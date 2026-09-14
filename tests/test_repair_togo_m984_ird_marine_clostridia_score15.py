from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m984_ird_marine_clostridia_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m984_ird_marine_clostridia_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m984")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "notes": "Cross-reference to Medium M953",
        "concentration": {"value": value, "unit": unit},
        "name": "Unknown solution",
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": repair_module.TARGET.stem,
        "original_name": "IRD Marine Clostridia Medium-2",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M984",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "IRD Marine Clostridia Medium-2",
            },
        },
        "notes": "Original source: JCM - JCM_M938",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _composition in (
                repair_module.IMPORTED_SOLUTION_SIGNATURE
            )
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_expands_jcm_909_and_trace_minerals(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])
    trace = _by_name(solutions["Trace minerals"]["composition"])

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repair_module._solution_signature(repaired["solutions"], "solutions") == (
        repair_module.FINAL_SOLUTION_SIGNATURE
    )
    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert ingredients["sodium acetate"]["term"] == {
        "id": "CHEBI:32954",
        "label": "sodium acetate",
    }
    assert "term" not in ingredients["Trypticase peptone (BD-BBL)"]
    assert ingredients["Resazurin"]["concentration"] == {
        "value": "1.0",
        "unit": "MG_PER_L",
    }
    assert solutions["8% NaHCO3 solution"]["composition"][0]["concentration"] == {
        "value": "8.0",
        "unit": "PERCENT_W_V",
    }
    assert solutions["1 M Glucose solution"]["composition"][0]["term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert trace["Na2MoO4 x 2 H2O"]["term"] == {
        "id": "CHEBI:75213",
        "label": "sodium molybdate dihydrate",
    }
    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_adds_preparation_sterilization_references_and_event_once(
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
        {"reference": repair_module.TOGO_M984},
        {"reference": repair_module.JCM_938},
        {"reference": repair_module.TOGO_M953},
        {"reference": repair_module.JCM_909},
        {"reference": repair_module.TOGO_M142},
        {"reference": repair_module.JCM_151},
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
    doc["media_term"]["term"]["id"] = "TOGO:M999"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"] = {"value": "1.64", "unit": "G_PER_L"}

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["concentration"] = {"value": "1000.0", "unit": "ML_PER_L"}

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)
