from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_721_score30.py"
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
        "name": "desulfovibrio_aespoeensis_medium",
        "original_name": "DESULFOVIBRIO AESPOEENSIS MEDIUM",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_range": {"min": 7.3, "max": 7.5},
        "media_term": {
            "preferred_term": "KOMODO Medium 721",
            "term": {
                "id": repair.EXPECTED_MEDIA_TERM,
                "label": "DESULFOVIBRIO AESPOEENSIS MEDIUM",
            },
        },
        "notes": "Source: KOMODO ModelSEED | ID: 721 | DSMZ Medium: 721",
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
    return _load_script(SCRIPT, "repair_komodo_721_score30")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_721")


def test_repair_record_expands_desulfovibrio_aespoeensis_medium(
    repair,
    scorer,
) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["medium_type"] == "DEFINED"
    assert once["composition_type"] == "DEFINED"
    assert once["ph_range"] == {"min": 7.3, "max": 7.5}
    assert len(once["ingredients"]) == 38


def test_repair_record_applies_721_substrates_and_extra_stocks(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "sodium lactate")["concentration"] == {
        "value": "2.500000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2SeO3 x 5 H2O")["concentration"] == {
        "value": "0.00000598",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2WO4 x 2 H2O")["concentration"] == {
        "value": "0.00000797",
        "unit": "G_PER_L",
    }


def test_repair_record_combines_141_and_503_vitamins(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "Pyridoxine-HCl")["concentration"] == {
        "value": "0.000399",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Thiamine-HCl x 2 H2O")["concentration"] == {
        "value": "0.000249",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Vitamin B12")["term"] == {
        "id": "CHEBI:176843",
        "label": "vitamin B12",
    }


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_721_URL},
        {"reference": repair.DSMZ_721_URL},
        {"reference": repair.DSMZ_193_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_141_URL},
        {"reference": repair.DSMZ_385_URL},
        {"reference": repair.DSMZ_503_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:006364"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:193"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:721"):
        repair.repair_record(doc)
