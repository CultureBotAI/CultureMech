from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_290_score30.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _doc(repair) -> dict:
    return {
        "id": repair.EXPECTED_ID,
        "name": "desulfococcus_niacini_medium",
        "original_name": "DESULFOCOCCUS NIACINI MEDIUM",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.4,
        "media_term": {
            "preferred_term": "KOMODO Medium 290",
            "term": {
                "id": repair.EXPECTED_MEDIA_TERM,
                "label": "DESULFOCOCCUS NIACINI MEDIUM",
            },
        },
        "notes": "Source: KOMODO ModelSEED | ID: 290 | DSMZ Medium: 290",
        "ingredients": [],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
    }


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for ingredient in doc["ingredients"]:
        if ingredient["preferred_term"] == preferred_term:
            return ingredient
    raise AssertionError(f"missing ingredient {preferred_term!r}")


@pytest.fixture
def repair():
    return _load_script(SCRIPT, "repair_komodo_290_score30")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_290")


def test_repair_record_expands_desulfococcus_niacini_medium(
    repair,
    scorer,
) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["medium_type"] == "DEFINED"
    assert once["composition_type"] == "DEFINED"
    assert once["ph_value"] == 7.4
    assert len(once["ingredients"]) == 35


def test_repair_record_applies_290_component_changes(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert all(
        ingredient["preferred_term"] != "Sodium propionate"
        for ingredient in repaired["ingredients"]
    )
    assert all(
        ingredient["preferred_term"] != "1,2-propanediol" for ingredient in repaired["ingredients"]
    )
    assert _ingredient(repaired, "NaCl")["concentration"] == {
        "value": "13.500000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "MgCl2 x 6 H2O")["concentration"] == {
        "value": "2.200000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Sodium pyruvate")["concentration"] == {
        "value": "1.250000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na-malate")["term"] == {
        "id": "CHEBI:91261",
        "label": "sodium malate",
    }


def test_repair_record_preserves_290_selenite_addition(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "Na2SeO3 x 5 H2O")["concentration"] == {
        "value": "3.0",
        "unit": "MICROG_PER_L",
    }
    assert _ingredient(repaired, "Na2SeO3 x 5 H2O")["source"] == repair.SOURCE_290


def test_repair_record_inherits_desulfobulbus_trace_and_vitamin_stocks(
    repair,
) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "FeCl2 x 4 H2O")["concentration"] == {
        "value": "0.001499",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Vitamin B12")["concentration"] == {
        "value": "0.000000999",
        "unit": "G_PER_L",
    }


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_290_URL},
        {"reference": repair.DSMZ_290_URL},
        {"reference": repair.DSMZ_193_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_141_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:004752"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:193"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:290"):
        repair.repair_record(doc)
