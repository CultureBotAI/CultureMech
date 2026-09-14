from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_686_score35.py"
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
        "original_name": "PROPIONIGENIUM MARIS medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 686",
            "term": {
                "id": repair.EXPECTED_MEDIA_TERM,
                "label": "PROPIONIGENIUM MARIS medium",
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
    return _load_script(SCRIPT, "repair_komodo_686_score35")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_686")


def test_repair_record_adds_propionigenium_maris_components(repair, scorer) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)
    names = {ingredient["preferred_term"] for ingredient in once["ingredients"]}

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["ph_range"] == {"min": 7.2, "max": 7.4}
    assert len(once["ingredients"]) == 33
    assert "Na2-succinate" not in names
    assert _ingredient(once, "NaCl")["concentration"] == {
        "value": "20.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "MgCl2 x 6 H2O")["concentration"] == {
        "value": "3.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "Disodium succinate")["term"] == {
        "id": "CHEBI:63675",
        "label": "sodium succinate (anhydrous)",
    }
    assert _ingredient(once, "Yeast extract")["concentration"] == {
        "value": "0.500000",
        "unit": "G_PER_L",
    }


def test_repair_record_expands_fwm_stocks(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "Vitamin B12")["concentration"] == {
        "value": "0.0000987",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "NaOH")["source"] == repair.SOURCE_385
    assert _ingredient(repaired, "Na2SeO3 x 5 H2O")["term"] == {
        "id": "CHEBI:131361",
        "label": "disodium selenite pentahydrate",
    }
    assert _ingredient(repaired, "Na2WO4 x 2 H2O")["term"] == {
        "id": "CHEBI:63939",
        "label": "sodium tungstate dihydrate",
    }
    assert "term" not in _ingredient(repaired, "Yeast extract")


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_686_URL},
        {"reference": repair.DSMZ_686_URL},
        {"reference": repair.DSMZ_504_URL},
        {"reference": repair.DSMZ_503_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_385_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:006291"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:307"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:686"):
        repair.repair_record(doc)
