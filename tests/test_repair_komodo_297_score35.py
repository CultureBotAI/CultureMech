from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_297_score35.py"
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
        "name": repair.TARGET.stem,
        "original_name": "ILYOBACTER TARTARICUS MEDIUM",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 297",
            "term": {
                "id": repair.EXPECTED_MEDIA_TERM,
                "label": "ILYOBACTER TARTARICUS MEDIUM",
            },
        },
        "notes": "Source: KOMODO ModelSEED",
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
    return _load_script(SCRIPT, "repair_komodo_297_score35")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_297")


def test_repair_record_adds_ilyobacter_tartaricus_components(repair, scorer) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)
    names = {ingredient["preferred_term"] for ingredient in once["ingredients"]}

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["ph_value"] == 7.2
    assert len(once["ingredients"]) == 22
    assert _ingredient(once, "NaCl")["concentration"] == {
        "value": "19.980020",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "MgCl2 x 6 H2O")["concentration"] == {
        "value": "2.997003",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "sodium L-tartrate")["concentration"] == {
        "value": "2.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "sodium L-tartrate")["term"] == {
        "id": "CHEBI:63017",
        "label": "sodium L-tartrate",
    }
    assert "Na2-succinate" not in names
    assert "Disodium succinate" not in names


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_297_URL},
        {"reference": repair.DSMZ_297_URL},
        {"reference": repair.DSMZ_293_URL},
        {"reference": repair.DSMZ_320_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:004761"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:562"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:297"):
        repair.repair_record(doc)
