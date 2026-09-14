from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_488_score35.py"
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
        "original_name": "DESULFOVIBRIO ALCOHOLOVORANS medium",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 488",
            "term": {
                "id": target.expected_media_term,
                "label": "DESULFOVIBRIO ALCOHOLOVORANS medium",
            },
        },
        "notes": "Source: KOMODO ModelSEED | ID: 488 | DSMZ Medium: 488",
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
    return _load_script(SCRIPT, "repair_komodo_488_score35")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_488")


def test_repair_record_adds_medium_63_branch_components(repair, scorer) -> None:
    target = repair.TARGETS[0]

    once = repair.repair_record(_doc(target), target)
    twice = repair.repair_record(once, target)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["medium_type"] == "COMPLEX"
    assert once["composition_type"] == "UNDEFINED"
    assert once["ph_value"] == 7.8
    assert len(once["ingredients"]) == 16
    assert _ingredient(once, "1,2-propanediol")["term"] == {
        "id": "CHEBI:16997",
        "label": "propane-1,2-diol",
    }
    assert _ingredient(once, "1,2-propanediol")["source"] == repair.SOURCE_488
    assert _ingredient(once, "Na2SeO3 x 5 H2O")["concentration"] == {
        "value": "3.0",
        "unit": "MICROG_PER_L",
    }
    assert _ingredient(once, "DL-Na-lactate")["concentration"] == {
        "value": "2.00",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "Yeast extract")["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert "mediaingredientmech_chebi_term" not in _ingredient(
        once,
        "Yeast extract",
    )
    assert _ingredient(once, "NaOH")["concentration"]["unit"] == "VARIABLE"
    assert once["ingredients"][-1]["concentration"] == {
        "value": "1000.000",
        "unit": "ML_PER_L",
    }


def test_repair_record_adds_medium_194_branch_components(repair, scorer) -> None:
    target = repair.TARGETS[1]

    repaired = repair.repair_record(_doc(target), target)
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

    assert scorer.score_record(repaired) == (0, [])
    assert repaired["ph_range"] == {"min": 7.1, "max": 7.4}
    assert len(repaired["ingredients"]) == 35
    assert "Na-acetate x 3 H2O" not in names
    assert _ingredient(repaired, "NaCl")["source"] == repair.SOURCE_194
    assert _ingredient(repaired, "NaCl")["concentration"] == {
        "value": "1.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "MgCl2 x 6 H2O")["concentration"] == {
        "value": "0.400000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Sodium propionate")["concentration"] == {
        "value": "1.500000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "1,2-propanediol")["source"] == repair.SOURCE_488


def test_repair_record_scales_194_branch_inherited_stocks(repair) -> None:
    target = repair.TARGETS[1]
    repaired = repair.repair_record(_doc(target), target)

    assert _ingredient(repaired, "Na2SO4")["concentration"] == {
        "value": "2.997003",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "HCl")["concentration"] == {
        "value": "0.002498",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "NaHCO3")["concentration"] == {
        "value": "4.995005",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2S x 9 H2O")["concentration"] == {
        "value": "0.399600",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Vitamin B12")["concentration"] == {
        "value": "0.000000999",
        "unit": "G_PER_L",
    }


def test_repair_record_adds_branch_specific_references(repair) -> None:
    medium_63 = repair.repair_record(_doc(repair.TARGETS[0]), repair.TARGETS[0])
    medium_194 = repair.repair_record(_doc(repair.TARGETS[1]), repair.TARGETS[1])

    assert medium_63["references"] == [
        {"reference": repair.KOMODO_488_URL},
        {"reference": repair.DSMZ_488_URL},
        {"reference": repair.DSMZ_63_URL},
    ]
    assert medium_194["references"] == [
        {"reference": repair.KOMODO_488_REPLACE_URL},
        {"reference": repair.DSMZ_488_URL},
        {"reference": repair.DSMZ_194_URL},
        {"reference": repair.DSMZ_193_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_141_URL},
    ]
    assert medium_63["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    target = repair.TARGETS[0]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:005613"):
        repair.repair_record(doc, target)


def test_repair_record_rejects_wrong_source(repair) -> None:
    target = repair.TARGETS[1]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "komodo.medium:488"

    with pytest.raises(
        ValueError,
        match="missing expected media term komodo.medium:488_replace",
    ):
        repair.repair_record(doc, target)
