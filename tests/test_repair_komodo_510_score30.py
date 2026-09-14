from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_510_score30.py"
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
        "name": "stygiolobus_medium",
        "original_name": "STYGIOLOBUS medium",
        "category": "archaea",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_range": {"min": 2.5, "max": 3.0},
        "media_term": {
            "preferred_term": "KOMODO Medium 510",
            "term": {"id": repair.EXPECTED_MEDIA_TERM, "label": "STYGIOLOBUS medium"},
        },
        "notes": "Source: KOMODO ModelSEED | ID: 510 | DSMZ Medium: 510",
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
    return _load_script(SCRIPT, "repair_komodo_510_score30")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_510")


def test_repair_record_expands_dsmz_510_chain(repair, scorer) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["medium_type"] == "COMPLEX"
    assert once["composition_type"] == "UNDEFINED"
    assert once["ph_range"] == {"min": 2.5, "max": 3.0}
    assert len(once["ingredients"]) == 19
    assert _ingredient(once, "Yeast extract")["concentration"] == {
        "value": "0.200000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "Sulfur (powder)")["concentration"] == {
        "value": "5.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "Resazurin")["concentration"] == {
        "value": "0.000500",
        "unit": "G_PER_L",
    }


def test_repair_record_converts_medium_88_milligram_salts(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "FeCl3 x 6 H2O")["concentration"] == {
        "value": "0.020000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2B4O7 x 10 H2O")["concentration"] == {
        "value": "0.004500",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "VOSO4 x 2 H2O")["term"] == {
        "id": "CHEBI:87009",
        "label": "vanadyl sulfate dihydrate",
    }
    assert _ingredient(repaired, "CoSO4")["concentration"] == {
        "value": "0.000010",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "H2SO4")["concentration"]["unit"] == "VARIABLE"


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_510_URL},
        {"reference": repair.DSMZ_510_URL},
        {"reference": repair.DSMZ_358_URL},
        {"reference": repair.DSMZ_88_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert "mediaingredientmech_chebi_term" not in _ingredient(
        repaired,
        "Yeast extract",
    )


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:005712"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:358"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:510"):
        repair.repair_record(doc)
