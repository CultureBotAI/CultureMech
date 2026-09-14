from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m3282_rcm_broth_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m3282_rcm_broth")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m3282_rcm_broth")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "rcm_broth",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M3282",
            "term": {"id": repair_module.EXPECTED_MEDIA_TERM, "label": "RCM Broth"},
        },
        "notes": "Source: JCM",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_water_adds_ph_and_grounds_components(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert repaired["physical_state"] == "LIQUID"
    assert repaired["ph_value"] == 6.8
    assert "ph_range" not in repaired
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert "Glucosev" not in ingredients
    assert ingredients["Glucose"]["term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert ingredients["Bacto peptone (BD-Difco)"]["term"] == {
        "id": "MICRO:0000178",
        "label": "Peptone",
    }
    assert ingredients["Beef extract (BD-Difco)"]["term"] == {
        "id": "FOODON:03302088",
        "label": "beef extract",
    }
    assert ingredients["L-Cysteine·HCl·H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:91248",
        "label": "L-cysteine hydrochloride hydrate",
    }
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_adds_roles_preparation_references_and_event_once(
    repair_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)
    ingredients = _by_name(twice["ingredients"])

    assert ingredients["L-Cysteine·HCl·H2O"]["nutritional_roles"] == [
        "AMINO_ACID_SOURCE",
        "SULFUR_SOURCE",
    ]
    assert ingredients["L-Cysteine·HCl·H2O"]["physicochemical_roles"] == [
        "REDUCING_AGENT",
    ]
    assert ingredients["Sodium acetate"]["physicochemical_roles"] == ["BUFFER"]
    assert twice["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert twice["sterilization"] == repair_module.STERILIZATION
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
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


def test_plan_repairs_targets_rcm_broth(repair_module) -> None:
    plans = repair_module.plan_repairs()

    assert set(plans) == {
        repair_module.NORMALIZED / repair_module.TARGET,
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:009696"):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M2758"

    with pytest.raises(ValueError, match="expected media term TOGO:M3282"):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Water", "1", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"] = [{"preferred_term": "Unexpected stock"}]

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
    assert "solutions" not in doc
