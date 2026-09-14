from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_777_score30.py"
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
        "name": "sporomusa_silvacetica_medium",
        "original_name": "SPOROMUSA SILVACETICA medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_range": {"min": 6.5, "max": 6.7},
        "media_term": {
            "preferred_term": "KOMODO Medium 777",
            "term": {
                "id": repair.EXPECTED_MEDIA_TERM,
                "label": "SPOROMUSA SILVACETICA medium",
            },
        },
        "notes": "Source: KOMODO ModelSEED | ID: 777 | DSMZ Medium: 777",
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
    return _load_script(SCRIPT, "repair_komodo_777_score30")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_777")


def test_repair_record_expands_sporomusa_silvacetica_medium(
    repair,
    scorer,
) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["medium_type"] == "COMPLEX"
    assert once["composition_type"] == "UNDEFINED"
    assert once["ph_range"] == {"min": 6.5, "max": 6.7}
    assert len(once["ingredients"]) == 37


def test_repair_record_applies_777_substrate_changes(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "Yeast extract")["concentration"] == {
        "value": "1.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Casitone")["concentration"] == {
        "value": "1.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "D-Fructose")["concentration"] == {
        "value": "5.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "NaHCO3")["concentration"] == {
        "value": "1.500000",
        "unit": "G_PER_L",
    }
    assert "Betaine x H2O" not in {
        ingredient["preferred_term"] for ingredient in repaired["ingredients"]
    }


def test_repair_record_retains_311_reductants_and_stocks(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "Cysteine-HCl x H2O")["concentration"] == {
        "value": "0.296736",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2S x 9 H2O")["concentration"] == {
        "value": "0.296736",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "NaHSeO3")["concentration"] == {
        "value": "0.100",
        "unit": "MICROMOLAR",
    }
    assert _ingredient(repaired, "Biotin")["concentration"] == {
        "value": "0.0000198",
        "unit": "G_PER_L",
    }


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_777_URL},
        {"reference": repair.DSMZ_777_URL},
        {"reference": repair.DSMZ_311_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_141_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert "mediaingredientmech_chebi_term" not in _ingredient(repaired, "Casitone")


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:006435"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:311"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:777"):
        repair.repair_record(doc)
