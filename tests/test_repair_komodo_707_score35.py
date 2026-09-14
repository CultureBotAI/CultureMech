from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_707_score35.py"
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
        "original_name": "THERMODESULFORHABDUS MEDIUM",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 6.8,
        "media_term": {
            "preferred_term": "KOMODO Medium 707",
            "term": {
                "id": repair.EXPECTED_MEDIA_TERM,
                "label": "THERMODESULFORHABDUS MEDIUM",
            },
        },
        "notes": "Source: KOMODO ModelSEED",
        "ingredients": [
            {
                "preferred_term": "sodium",
                "notes": "Extracted from recipe notes",
                "concentration": {"value": "variable", "unit": "VARIABLE"},
            }
        ],
        "curation_history": [],
    }


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for ingredient in doc["ingredients"]:
        if ingredient["preferred_term"] == preferred_term:
            return ingredient
    raise AssertionError(f"missing ingredient {preferred_term!r}")


@pytest.fixture
def repair():
    return _load_script(SCRIPT, "repair_komodo_707_score35")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_707")


def test_repair_record_adds_thermodesulforhabdus_components(
    repair, scorer
) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)
    names = {ingredient["preferred_term"] for ingredient in once["ingredients"]}

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert len(once["ingredients"]) == 23
    assert "sodium" not in names
    assert _ingredient(once, "Na-acetate x 3 H2O")["term"] == {
        "id": "CHEBI:32138",
        "label": "sodium acetate trihydrate",
    }
    assert _ingredient(once, "Na2SO4")["concentration"] == {
        "value": "7.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "NaHCO3")["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert _ingredient(once, "sodium sulfide")["term"] == {
        "id": "CHEBI:76208",
        "label": "sodium sulfide (anhydrous)",
    }
    assert _ingredient(once, "Na2S2O4")["concentration"] == {
        "value": "0.050000",
        "unit": "G_PER_L",
    }


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_707_URL},
        {"reference": repair.DSMZ_707_URL},
        {"reference": repair.DSMZ_320_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:006339"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:706"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:707"):
        repair.repair_record(doc)
