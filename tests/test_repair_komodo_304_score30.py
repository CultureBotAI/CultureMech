from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_304_score30.py"
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
        "name": Path(target.path).stem,
        "original_name": "METHANOSARCINA ACETIVORANS medium",
        "category": "archaea",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.0,
        "media_term": {
            "preferred_term": "KOMODO Medium 304",
            "term": {
                "id": target.expected_media_term,
                "label": "METHANOSARCINA ACETIVORANS medium",
            },
        },
        "notes": "Source: KOMODO ModelSEED | ID: 304 | DSMZ Medium: 304",
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
    return _load_script(SCRIPT, "repair_komodo_304_score30")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_304")


def test_repair_record_adds_trimethylamine_branch_components(repair, scorer) -> None:
    target = repair.TARGETS[0]

    once = repair.repair_record(_doc(target), target)
    twice = repair.repair_record(once, target)
    names = {ingredient["preferred_term"] for ingredient in once["ingredients"]}

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["medium_type"] == "COMPLEX"
    assert once["composition_type"] == "UNDEFINED"
    assert len(once["ingredients"]) == 28
    assert "Trimethylamine-HCl" in names
    assert "Methanol" not in names
    assert _ingredient(once, "Trimethylamine-HCl")["concentration"] == {
        "value": "2.970297",
        "unit": "G_PER_L",
    }


def test_repair_record_adds_methanol_branch_components(repair, scorer) -> None:
    target = repair.TARGETS[1]

    repaired = repair.repair_record(_doc(target), target)
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

    assert scorer.score_record(repaired) == (0, [])
    assert len(repaired["ingredients"]) == 28
    assert "Methanol" in names
    assert "Trimethylamine-HCl" not in names
    assert _ingredient(repaired, "Methanol")["concentration"] == {
        "value": "4.950495",
        "unit": "G_PER_L",
    }


def test_repair_record_scales_dsmz_304_trace_stock(repair) -> None:
    repaired = repair.repair_record(_doc(repair.TARGETS[0]), repair.TARGETS[0])

    assert _ingredient(repaired, "NaCl")["concentration"] == {
        "value": "23.178218",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "MgSO4 x 7 H2O")["concentration"] == {
        "value": "9.386139",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "CaCl2 x 2 H2O")["concentration"] == {
        "value": "0.139604",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2SeO3 x 5 H2O")["concentration"] == {
        "value": "0.000002970",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "KOH")["concentration"]["unit"] == "VARIABLE"
    assert _ingredient(repaired, "HCl")["concentration"]["unit"] == "VARIABLE"


def test_repair_record_adds_branch_specific_references_and_flags(repair) -> None:
    base = repair.repair_record(_doc(repair.TARGETS[0]), repair.TARGETS[0])
    replacement = repair.repair_record(_doc(repair.TARGETS[1]), repair.TARGETS[1])

    assert base["references"] == [
        {"reference": repair.KOMODO_304_URL},
        {"reference": repair.DSMZ_304_URL},
        {"reference": repair.DSMZ_141_URL},
    ]
    assert replacement["references"] == [
        {"reference": repair.KOMODO_304_REPLACE_URL},
        {"reference": repair.DSMZ_304_URL},
        {"reference": repair.DSMZ_141_URL},
    ]
    assert base["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert "mediaingredientmech_chebi_term" not in _ingredient(base, "Yeast extract")


def test_repair_record_rejects_wrong_id(repair) -> None:
    target = repair.TARGETS[0]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:004832"):
        repair.repair_record(doc, target)


def test_repair_record_rejects_wrong_source(repair) -> None:
    target = repair.TARGETS[1]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "komodo.medium:304"

    with pytest.raises(
        ValueError,
        match="missing expected media term komodo.medium:304_replace",
    ):
        repair.repair_record(doc, target)
