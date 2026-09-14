from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_324_score30.py"
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
        "name": "methanolobus_ii_medium",
        "original_name": "METHANOLOBUS II medium",
        "category": "archaea",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_range": {"min": 6.8, "max": 7.0},
        "media_term": {
            "preferred_term": "KOMODO Medium 324",
            "term": {"id": repair.EXPECTED_MEDIA_TERM, "label": "METHANOLOBUS II medium"},
        },
        "notes": "Source: KOMODO ModelSEED | ID: 324 | DSMZ Medium: 324",
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
    return _load_script(SCRIPT, "repair_komodo_324_score30")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_324")


def test_repair_record_expands_dsmz_141_and_324(repair, scorer) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["medium_type"] == "COMPLEX"
    assert once["composition_type"] == "UNDEFINED"
    assert once["ph_range"] == {"min": 6.8, "max": 7.0}
    assert len(once["ingredients"]) == 41
    assert _ingredient(once, "Methanol")["concentration"] == {
        "value": "0.500000",
        "unit": "PERCENT_V_V",
    }
    assert _ingredient(once, "N2")["concentration"]["unit"] == "VARIABLE"
    assert _ingredient(once, "CO2")["concentration"]["unit"] == "VARIABLE"


def test_repair_record_scales_dsmz_141_trace_stock(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "NaCl")["concentration"] == {
        "value": "17.656863",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "MgSO4 x 7 H2O")["concentration"] == {
        "value": "3.411765",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "CaCl2 x 2 H2O")["concentration"] == {
        "value": "0.138235",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2SeO3 x 5 H2O")["concentration"] == {
        "value": "0.000002941",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "KOH")["concentration"]["unit"] == "VARIABLE"


def test_repair_record_scales_dsmz_141_vitamin_stock(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "Biotin")["concentration"] == {
        "value": "0.000019608",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Pyridoxine-HCl")["concentration"] == {
        "value": "0.000098",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Vitamin B12")["concentration"] == {
        "value": "0.000000980",
        "unit": "G_PER_L",
    }


def test_repair_record_preserves_dsmz_141_specific_salts(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "MgCl2 x 6 H2O")["term"] == {
        "id": "CHEBI:86345",
        "label": "magnesium dichloride hexahydrate",
    }
    assert _ingredient(repaired, "Fe(NH4)2(SO4)2 x 7 H2O")["term"] == {
        "id": "CHEBI:131378",
        "label": "Fe(NH4)2(SO4)2 x 7 H2O",
    }
    assert _ingredient(repaired, "Na-acetate")["concentration"] == {
        "value": "0.980392",
        "unit": "G_PER_L",
    }


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_324_URL},
        {"reference": repair.DSMZ_324_URL},
        {"reference": repair.DSMZ_141_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert "mediaingredientmech_chebi_term" not in _ingredient(
        repaired,
        "Trypticase",
    )


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:005015"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:141"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:324"):
        repair.repair_record(doc)
