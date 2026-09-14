from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_285_307_score35.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _doc(target) -> dict:
    return {
        "id": target.expected_id,
        "name": target.path.stem,
        "original_name": target.path.stem.replace("_", " ").upper(),
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": f"KOMODO Medium {target.komodo_id}",
            "term": {
                "id": target.expected_media_term,
                "label": target.path.stem,
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
    return _load_script(SCRIPT, "repair_komodo_285_307_score35")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_285_307")


def test_repair_record_adds_sulfate_free_syntrophus_components(repair, scorer) -> None:
    target = repair.TARGETS[0]
    once = repair.repair_record(_doc(target), target)
    twice = repair.repair_record(once, target)
    names = {ingredient["preferred_term"] for ingredient in once["ingredients"]}

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["ph_value"] == 7.2
    assert len(once["ingredients"]) == 30
    assert "Na2SO4" not in names
    assert "Butyric acid" not in names
    assert _ingredient(once, "sodium benzoate")["concentration"] == {
        "value": "2.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "sodium benzoate")["term"] == {
        "id": "CHEBI:113455",
        "label": "sodium benzoate",
    }


def test_repair_record_adds_syntrophobacter_wolinii_components(repair, scorer) -> None:
    target = repair.TARGETS[1]
    once = repair.repair_record(_doc(target), target)
    twice = repair.repair_record(once, target)
    names = {ingredient["preferred_term"] for ingredient in once["ingredients"]}

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert len(once["ingredients"]) == 31
    assert "Butyric acid" not in names
    assert _ingredient(once, "Na2SO4")["concentration"] == {
        "value": "2.783300",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "sodium propionate")["concentration"] == {
        "value": "1.500000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "sodium propionate")["term"] == {
        "id": "CHEBI:132106",
        "label": "sodium propionate",
    }


def test_repair_record_adds_shared_212_and_320_components(repair) -> None:
    repaired = repair.repair_record(_doc(repair.TARGETS[0]), repair.TARGETS[0])

    assert "term" not in _ingredient(repaired, "Trypticase")
    assert "term" not in _ingredient(repaired, "Rumen fluid, clarified")
    assert _ingredient(repaired, "HCl")["concentration"] == {
        "value": "0.002485",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Pyridoxine-HCl")["concentration"] == {
        "value": "0.0000308",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Distilled water")["concentration"] == {
        "value": "900.000",
        "unit": "ML_PER_L",
    }


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair.TARGETS[1]), repair.TARGETS[1])

    assert repaired["references"] == [
        {"reference": repair.TARGETS[1].komodo_url},
        {"reference": repair.DSMZ_307_URL},
        {"reference": repair.DSMZ_212_URL},
        {"reference": repair.DSMZ_320_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    target = repair.TARGETS[0]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:004742"):
        repair.repair_record(doc, target)


def test_repair_record_rejects_wrong_source(repair) -> None:
    target = repair.TARGETS[0]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "komodo.medium:307"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:285"):
        repair.repair_record(doc, target)
