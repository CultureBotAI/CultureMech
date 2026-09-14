from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1830_alb_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m1830_alb_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1830_alb")


def _component(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
    }


def _doc(repair_module) -> dict:
    return {
        "id": "CultureMech:008403",
        "name": "alb_medium",
        "original_name": "ALB Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M1830",
            "term": {"id": "TOGO:M1830", "label": "ALB Medium"},
        },
        "notes": "Source: TOGO M1830",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            {
                "preferred_term": "Na2CO3*",
                "composition": [],
                "concentration": {"value": "2", "unit": "G_PER_L"},
                "notes": "Role: Buffer",
                "name": "Unknown solution",
            }
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_promotes_nbrc_formula_to_direct_grounded_components(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert "solutions" not in repaired
    assert "CO2" not in _by_name(repaired["ingredients"])
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert scorer_module.score_parsed([("bacterial/alb_medium.yaml", repaired)]) == []


def test_repair_corrects_water_sodium_carbonate_and_roles(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Tryptone"]["term"] == {
        "id": "MICRO:0000182",
        "label": "tryptone",
    }
    assert ingredients["Yeast extract"]["nutritional_roles"] == [
        "PROTEIN_SOURCE",
        "VITAMIN_SOURCE",
    ]
    assert ingredients["Na2CO3"]["term"] == {
        "id": "CHEBI:29377",
        "label": "sodium carbonate",
    }
    assert ingredients["Na2CO3"]["physicochemical_roles"] == ["BUFFER"]
    assert ingredients["Agar (if needed)"]["physicochemical_roles"] == ["SOLIDIFYING_AGENT"]


def test_repair_adds_ph_atmosphere_preparation_sterilization_and_refs(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["ph_range"] == repair_module.PH_RANGE
    assert repaired["aeration"] == "air containing 5% CO2"
    assert repaired["incubation_atmosphere"] == "AEROBIC"
    assert [step["action"] for step in repaired["preparation_steps"]] == [
        "DISSOLVE",
        "DISSOLVE",
        "ADJUST_PH",
        "AUTOCLAVE",
        "MIX",
        "MIX",
    ]
    assert repaired["sterilization"] == repair_module.STERILIZATION
    assert repaired["references"] == [
        {"reference": repair_module.TOGO_M1830},
        {"reference": repair_module.NBRC_1063},
    ]


def test_repair_is_idempotent_and_adds_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice == once
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert repair_module.NBRC_1063 in matching_events[0]["source"]


def test_repair_rejects_wrong_source(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M999999"

    with pytest.raises(ValueError, match="TOGO:M1830"):
        repair_module.repair_record(doc)


def test_repair_rejects_empty_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["preferred_term"] = "NaHCO3"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)
