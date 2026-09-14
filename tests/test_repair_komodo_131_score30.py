from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_131_score30.py"
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
        "name": "methanobacterium_thermoautotrophicum_medium",
        "original_name": "METHANOBACTERIUM THERMOAUTOTROPHICUM MEDIUM",
        "category": "archaea",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.2,
        "media_term": {
            "preferred_term": "KOMODO Medium 131",
            "term": {
                "id": repair.EXPECTED_MEDIA_TERM,
                "label": "METHANOBACTERIUM THERMOAUTOTROPHICUM MEDIUM",
            },
        },
        "notes": "Source: KOMODO ModelSEED",
        "ingredients": [],
        "data_quality_flags": ["incomplete_composition"],
        "curation_history": [],
    }


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for ingredient in doc["ingredients"]:
        if ingredient["preferred_term"] == preferred_term:
            return ingredient
    raise AssertionError(f"missing ingredient {preferred_term!r}")


@pytest.fixture
def repair():
    return _load_script(SCRIPT, "repair_komodo_131_score30")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_131")


def test_repair_record_expands_dsmz_131_stock_solutions(repair, scorer) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert len(once["ingredients"]) == 33
    assert _ingredient(once, "NaCl")["concentration"] == {
        "value": "0.610000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "MgSO4 x 7 H2O")["concentration"] == {
        "value": "0.182000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "Vitamin B12")["concentration"] == {
        "value": "0.000000100",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "H2")["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_131_URL},
        {"reference": repair.DSMZ_131_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:004074"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:131_6216"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:131"):
        repair.repair_record(doc)
