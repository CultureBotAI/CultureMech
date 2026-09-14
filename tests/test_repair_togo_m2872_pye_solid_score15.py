from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2872_pye_solid_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2872_pye_solid")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2872")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "pye_solid_medium",
        "original_name": "PYE Solid medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2872",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "PYE Solid medium",
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": ["has_unmapped_ingredients", "needs_manual_curation"],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_grounds_pye_solid_and_leaves_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert "solutions" not in repaired
    assert "ph_value" not in repaired
    assert "ph_range" not in repaired
    assert "temperature_value" not in repaired
    assert "temperature_range" not in repaired
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_grounds_all_components(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Bacto peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "Bacto peptone",
    }
    assert "mediaingredientmech_chebi_term" not in ingredients["Bacto peptone"]
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    }
    assert "mediaingredientmech_chebi_term" not in ingredients["Yeast extract"]
    assert ingredients["MgSO4"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:32599",
        "label": "magnesium sulfate",
    }
    assert ingredients["CaCl2"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:3312",
        "label": "calcium dichloride",
    }
    assert ingredients["Agar"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

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
    assert matching_events[0]["source"] == "; ".join(repair_module.REFERENCES)


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:009406"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M2873"

    with pytest.raises(ValueError, match="expected media term TOGO:M2872"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_signature_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"]["value"] = "1.0"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_unexpected_solutions(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"] = [{"preferred_term": "Unexpected"}]

    with pytest.raises(ValueError, match="unexpected solutions block"):
        repair_module.repair_record(doc)
