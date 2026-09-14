from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_676_score30.py"
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
        "name": "mab1_medium",
        "original_name": "mAB1-MEDIUM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.2,
        "media_term": {
            "preferred_term": "KOMODO Medium 676",
            "term": {
                "id": repair.EXPECTED_MEDIA_TERM,
                "label": "mAB1-MEDIUM",
            },
        },
        "notes": "Source: KOMODO ModelSEED | ID: 676 | DSMZ Medium: 676",
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
    return _load_script(SCRIPT, "repair_komodo_676_score30")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_676")


def test_repair_record_expands_mab1_medium(repair, scorer) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["medium_type"] == "COMPLEX"
    assert once["composition_type"] == "UNDEFINED"
    assert once["ph_value"] == 7.2
    assert len(once["ingredients"]) == 38


def test_repair_record_omits_succinate_and_adds_676_substrates(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "Na2SO4")["concentration"] == {
        "value": "2.935421",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "NaHCO3")["concentration"] == {
        "value": "4.892368",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2S x 9 H2O")["concentration"] == {
        "value": "0.645793",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "sodium benzoate")["concentration"] == {
        "value": "0.146771",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "sodium dithionite")["concentration"] == {
        "value": "0.009785",
        "unit": "G_PER_L",
    }
    assert "Na2-succinate" not in {
        ingredient["preferred_term"] for ingredient in repaired["ingredients"]
    }


def test_repair_record_scales_vitamins_and_selenite_tungstate(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "Biotin")["concentration"] == {
        "value": "0.0000391",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Pyridoxine-HCl")["concentration"] == {
        "value": "0.000196",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Vitamin B12")["term"] == {
        "id": "CHEBI:176843",
        "label": "vitamin B12",
    }
    assert _ingredient(repaired, "Na2SeO3 x 5 H2O")["concentration"] == {
        "value": "0.00000294",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2WO4 x 2 H2O")["concentration"] == {
        "value": "0.00000391",
        "unit": "G_PER_L",
    }


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_676_URL},
        {"reference": repair.DSMZ_676_URL},
        {"reference": repair.DSMZ_293_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_141_URL},
        {"reference": repair.DSMZ_385_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:006272"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:293"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:676"):
        repair.repair_record(doc)
