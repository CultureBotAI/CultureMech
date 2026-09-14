from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_72_score35.py"
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
        "original_name": "THIOBACILLUS FERROOXIDANS MEDIUM WITH TETRATHIONATE",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 72",
            "term": {
                "id": repair.EXPECTED_MEDIA_TERM,
                "label": "THIOBACILLUS FERROOXIDANS MEDIUM WITH TETRATHIONATE",
            },
        },
        "notes": "Source: KOMODO ModelSEED",
        "ingredients": [],
        "data_quality_flags": ["incomplete_composition"],
        "curation_history": [],
    }


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for ingredient in doc["ingredients"]:
        if ingredient["preferred_term"] == preferred_term:
            return ingredient
    raise AssertionError(f"missing ingredient {preferred_term!r}")


@pytest.fixture
def repair():
    return _load_script(SCRIPT, "repair_komodo_72_score35")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_72")


def test_repair_record_adds_tetrathionate_components(repair, scorer) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)
    names = {ingredient["preferred_term"] for ingredient in once["ingredients"]}

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert len(once["ingredients"]) == 6
    assert "Na2S2O3 x 5 H2O" not in names
    assert once["ph_range"] == {"min": 4.4, "max": 4.7}
    assert _ingredient(once, "KH2PO4")["concentration"] == {
        "value": "3.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "MgSO4 x 7 H2O")["term"] == {
        "id": "CHEBI:31795",
        "label": "magnesium sulfate heptahydrate",
    }
    assert _ingredient(once, "K2S4O6")["concentration"] == {
        "value": "5.000000",
        "unit": "G_PER_L",
    }


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_72_URL},
        {"reference": repair.DSMZ_72_URL},
        {"reference": repair.DSMZ_71_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:006372"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:71"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:72"):
        repair.repair_record(doc)
