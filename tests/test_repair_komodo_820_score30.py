from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_820_score30.py"
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
        "name": "aeropyrum_jxt_medium",
        "original_name": "AEROPYRUM-JXT medium",
        "category": "archaea",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_range": {"min": 7.0, "max": 7.2},
        "media_term": {
            "preferred_term": "KOMODO Medium 820",
            "term": {"id": repair.EXPECTED_MEDIA_TERM, "label": "AEROPYRUM-JXT medium"},
        },
        "notes": "Source: KOMODO ModelSEED | ID: 820 | DSMZ Medium: 820",
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
    return _load_script(SCRIPT, "repair_komodo_820_score30")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_820")


def test_repair_record_expands_dsmz_514_and_820(repair, scorer) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["medium_type"] == "COMPLEX"
    assert once["composition_type"] == "UNDEFINED"
    assert once["physical_state"] == "LIQUID"
    assert once["ph_range"] == {"min": 7.0, "max": 7.2}
    assert len(once["ingredients"]) == 18
    assert _ingredient(once, "Bacto peptone")["concentration"] == {
        "value": "5.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "Na2S2O3 x 5 H2O")["concentration"] == {
        "value": "1.000000",
        "unit": "G_PER_L",
    }


def test_repair_record_converts_marine_broth_milligram_salts(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "SrCl2")["concentration"] == {
        "value": "0.034000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "H3BO3")["concentration"] == {
        "value": "0.022000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na-silicate")["concentration"] == {
        "value": "0.004000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "NaF")["concentration"] == {
        "value": "0.002400",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "(NH4)NO3")["concentration"] == {
        "value": "0.001600",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2HPO4")["concentration"] == {
        "value": "0.008000",
        "unit": "G_PER_L",
    }


def test_repair_record_preserves_anhydrous_mgcl2(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "MgCl2")["concentration"] == {
        "value": "5.900000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "MgCl2")["term"] == {
        "id": "CHEBI:6636",
        "label": "magnesium dichloride",
    }


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_820_URL},
        {"reference": repair.DSMZ_820_URL},
        {"reference": repair.DSMZ_514_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert "mediaingredientmech_chebi_term" not in _ingredient(
        repaired,
        "Bacto peptone",
    )


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:006547"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:514"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:820"):
        repair.repair_record(doc)
