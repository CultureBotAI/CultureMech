from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m94_soil_extract_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m94_soil_extract_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_m94")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _medium_doc(repair_module) -> dict:
    return {
        "id": "CultureMech:010373",
        "name": "nutrient_agar_with_25_soil_extract",
        "original_name": "Nutrient Agar With 25% Soil Extract",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M94",
            "term": {
                "id": "TOGO:M94",
                "label": "Nutrient Agar With 25% Soil Extract",
            },
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_togo_m94_moves_soil_extract_to_nested_solution(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_togo_m94(_medium_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])
    soil_extract = solutions["Soil extract"]
    soil_components = _by_name(soil_extract["composition"])

    assert repaired["ph_value"] == 7.0
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert (
        repair_module._solution_signatures(
            repaired["solutions"],
            "solutions",
        )
        == repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert ingredients["Tap water"]["concentration"] == {
        "value": "750.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "Peptone",
    }
    assert ingredients["Beef extract"]["term"] == {
        "id": "FOODON:03302088",
        "label": "Beef extract",
    }
    assert ingredients["Agar"]["physicochemical_roles"] == ["SOLIDIFYING_AGENT"]
    assert soil_extract["concentration"] == {"value": "250.0", "unit": "ML_PER_L"}
    assert "term" not in soil_components["Air-dried garden soil"]
    assert soil_components["Tap water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_togo_m94_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_togo_m94(_medium_doc(repair_module))
    twice = repair_module.repair_togo_m94(once)

    assert twice == once
    assert twice["references"] == [
        {"reference": repair_module.TOGO_M94},
        {"reference": repair_module.JCM_102},
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair_module.CURATOR
        and event.get("action") == repair_module.ACTION
    ]
    assert len(matching_events) == 1


def test_togo_m94_repair_rejects_wrong_id(repair_module) -> None:
    doc = _medium_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="CultureMech:010373"):
        repair_module.repair_togo_m94(doc)


def test_togo_m94_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _medium_doc(repair_module)
    doc["ingredients"][0]["concentration"]["value"] = "750"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_togo_m94(doc)
