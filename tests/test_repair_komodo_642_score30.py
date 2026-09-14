from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_642_score30.py"
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
        "name": "clostridium_estertheticum_medium",
        "original_name": "CLOSTRIDIUM ESTERTHETICUM medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 6.8,
        "media_term": {
            "preferred_term": "KOMODO Medium 642",
            "term": {
                "id": repair.EXPECTED_MEDIA_TERM,
                "label": "CLOSTRIDIUM ESTERTHETICUM medium",
            },
        },
        "notes": "Source: KOMODO ModelSEED | ID: 642 | DSMZ Medium: 642",
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
    return _load_script(SCRIPT, "repair_komodo_642_score30")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_642")


def test_repair_record_expands_clostridium_estertheticum_medium(
    repair,
    scorer,
) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["medium_type"] == "COMPLEX"
    assert once["composition_type"] == "UNDEFINED"
    assert once["physical_state"] == "LIQUID"
    assert once["ph_value"] == 6.8
    assert len(once["ingredients"]) == 12


def test_repair_record_applies_dsmz_642_supplements(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "sodium bicarbonate")["concentration"] == {
        "value": "2.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Glucose")["concentration"] == {
        "value": "15.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "CO2")["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert _ingredient(repaired, "N2")["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }


def test_repair_record_expands_komodo_rcm_base(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "Agar")["term"]["id"] == "CHEBI:2509"
    assert _ingredient(repaired, "Cysteine hydrochloride")["term"]["id"] == "CHEBI:91247"
    assert _ingredient(repaired, "Lab-Lemco powder")["term"] == {
        "id": "FOODON:03302088",
        "label": "beef extract",
    }
    assert _ingredient(repaired, "Soluble starch")["term"] == {
        "id": "CHEBI:28017",
        "label": "starch",
    }
    assert _ingredient(repaired, "Peptone")["concentration"] == {
        "value": "10.000000",
        "unit": "G_PER_L",
    }


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_642_URL},
        {"reference": repair.DSMZ_642_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:006182"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:575"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:642"):
        repair.repair_record(doc)
