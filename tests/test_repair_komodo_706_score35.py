from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_706_score35.py"
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
        "original_name": "SYNTROPHOBACTER PFENNIGII MEDIUM",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_range": {"min": 7.2, "max": 7.4},
        "notes": "pH buffer: bicarbonate | Source: KOMODO ModelSEED",
        "media_term": {
            "preferred_term": "KOMODO Medium 706",
            "term": {
                "id": repair.EXPECTED_MEDIA_TERM,
                "label": "SYNTROPHOBACTER PFENNIGII MEDIUM",
            },
        },
        "ingredients": [
            {
                "preferred_term": "bicarbonate",
                "notes": "Extracted from recipe notes (pH buffer)",
                "data_quality_flags": ["extracted_from_notes"],
                "concentration": {"value": "variable", "unit": "VARIABLE"},
            }
        ],
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
    return _load_script(SCRIPT, "repair_komodo_706_score35")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_706")


def test_repair_record_expands_syntrophobacter_medium(repair, scorer) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)
    names = {ingredient["preferred_term"] for ingredient in once["ingredients"]}

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["ph_range"] == {"min": 7.2, "max": 7.4}
    assert len(once["ingredients"]) == 32
    assert "bicarbonate" not in names
    assert "2,3-butanediol" not in names
    assert _ingredient(once, "Na2SO4")["concentration"] == {
        "value": "0.700000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "Sodium propionate")["term"] == {
        "id": "CHEBI:132106",
        "label": "sodium propionate",
    }


def test_repair_record_expands_503_vitamins_and_reductants(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "Vitamin B12")["source"] == repair.SOURCE_503
    assert _ingredient(repaired, "D(+)-Biotin")["concentration"] == {
        "value": "0.0000200",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "sulfide")["term"] == {
        "id": "CHEBI:15138",
        "label": "sulfide(2-)",
    }
    assert _ingredient(repaired, "Na2S2O4")["concentration"] == {
        "value": "0.010-0.020",
        "unit": "G_PER_L",
    }


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_706_URL},
        {"reference": repair.DSMZ_706_URL},
        {"reference": repair.DSMZ_298_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_503_URL},
        {"reference": repair.DSMZ_383_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:006338"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:707"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:706"):
        repair.repair_record(doc)
