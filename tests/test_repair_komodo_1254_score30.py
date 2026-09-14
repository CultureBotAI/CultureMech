from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_1254_score30.py"
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
        "name": "nautilia_nitratireducens_medium",
        "original_name": "NAUTILIA NITRATIREDUCENS MEDIUM",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.0,
        "media_term": {
            "preferred_term": "KOMODO Medium 1254",
            "term": {
                "id": repair.EXPECTED_MEDIA_TERM,
                "label": "NAUTILIA NITRATIREDUCENS MEDIUM",
            },
        },
        "notes": "Source: KOMODO ModelSEED | ID: 1254 | DSMZ Medium: 1254",
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
    return _load_script(SCRIPT, "repair_komodo_1254_score30")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_1254")


def test_repair_record_expands_nautilia_nitratireducens_medium(
    repair,
    scorer,
) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["medium_type"] == "DEFINED"
    assert once["composition_type"] == "DEFINED"
    assert once["ph_value"] == 7.0
    assert len(once["ingredients"]) == 30


def test_repair_record_combines_main_and_trace_components(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "NaCl")["concentration"] == {
        "value": "19.811881",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "CaCl2 x 2 H2O")["concentration"] == {
        "value": "0.743564",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "NiCl2 x 6 H2O")["term"] == {
        "id": "CHEBI:53542",
        "label": "nickel chloride hexahydrate",
    }


def test_repair_record_adds_1254_specific_salts_and_buffer(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "KNO3")["term"] == {
        "id": "CHEBI:63043",
        "label": "potassium nitrate",
    }
    assert _ingredient(repaired, "PIPES")["term"] == {
        "id": "CHEBI:39033",
        "label": "PIPES",
    }
    assert _ingredient(repaired, "Na2WO4 x 2 H2O")["concentration"] == {
        "value": "0.000099",
        "unit": "G_PER_L",
    }


def test_repair_record_adds_gas_phase_components(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "H2")["source"] == repair.SOURCE_1254
    assert _ingredient(repaired, "CO2")["source"] == repair.SOURCE_1254
    assert "80% H2 plus 20% CO2" in _ingredient(repaired, "H2")["notes"]


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_1254_URL},
        {"reference": repair.DSMZ_1254_URL},
        {"reference": repair.DSMZ_141_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:004015"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:141"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:1254"):
        repair.repair_record(doc)
