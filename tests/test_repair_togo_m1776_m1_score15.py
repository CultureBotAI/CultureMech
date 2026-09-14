from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1776_m1_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m1776_m1_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1776")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "name": "Unknown solution",
    }


def _target_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": repair_module.TARGET.stem,
        "original_name": "M1 Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M1776",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "M1 Medium",
            },
        },
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_SOLUTION_SIGNATURE
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_moves_seawater_and_grounds_m1_components(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_target(_target_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert "solutions" not in repaired
    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert "ph_value" not in repaired
    assert "temperature_value" not in repaired
    assert ingredients["Seawater"]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert "term" not in ingredients["Seawater"]
    assert ingredients["Starch"]["term"] == {
        "id": "CHEBI:28017",
        "label": "starch",
    }
    assert ingredients["Agar (if needed)"]["term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert ingredients["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "peptone",
    }
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )
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
    assert once["references"] == [
        {"reference": repair_module.TOGO_M1776},
        {"reference": repair_module.NBRC_992},
        {"reference": repair_module.TOGO_API},
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
    doc = _target_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_target(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _target_doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_target(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _target_doc(repair_module)
    doc["solutions"][0]["preferred_term"] = "Seawater"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_target(doc)
