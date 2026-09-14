from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_208_384_score35.py"
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
        "original_name": Path(target.path).stem,
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": target.expected_media_term.replace(
                "komodo.medium:",
                "KOMODO Medium ",
            ),
            "term": {
                "id": target.expected_media_term,
                "label": Path(target.path).stem,
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
    return _load_script(SCRIPT, "repair_komodo_208_384_score35")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_208_384")


def test_repair_record_adds_desulfovibrio_baarsii_components(
    repair,
    scorer,
) -> None:
    target = repair.TARGETS[0]

    once = repair.repair_record(_doc(target), target)
    twice = repair.repair_record(once, target)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["medium_type"] == "DEFINED"
    assert once["composition_type"] == "DEFINED"
    assert once["ph_range"] == {"min": 7.1, "max": 7.4}
    assert len(once["ingredients"]) == 35
    assert _ingredient(once, "NaCl")["concentration"] == {
        "value": "7.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "MgCl2 x 6 H2O")["concentration"] == {
        "value": "0.600000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "Na-butyrate")["term"] == {
        "id": "CHEBI:64103",
        "label": "sodium butyrate",
    }
    assert _ingredient(once, "Na-caproate")["term"] == {
        "id": "CHEBI:114126",
        "label": "sodium hexanoate",
    }
    assert _ingredient(once, "Na-octanoate")["term"] == {
        "id": "CHEBI:132100",
        "label": "sodium octanoate",
    }


def test_repair_record_adds_desulfovibrio_carbinolicus_components(
    repair,
    scorer,
) -> None:
    target = repair.TARGETS[1]

    repaired = repair.repair_record(_doc(target), target)
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

    assert scorer.score_record(repaired) == (0, [])
    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "UNDEFINED"
    assert repaired["ph_range"] == {"min": 7.1, "max": 7.4}
    assert len(repaired["ingredients"]) == 35
    assert "Sodium propionate" not in names
    assert _ingredient(repaired, "Ethanol")["concentration"] == {
        "value": "0.700000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Ethanol")["term"] == {
        "id": "CHEBI:16236",
        "label": "ethanol",
    }
    assert _ingredient(repaired, "Yeast extract")["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert _ingredient(repaired, "Casamino acid")["term"] == {
        "id": "FOODON:03315719",
        "label": "mammalian milk protein (hydrolyzed)",
    }
    assert "mediaingredientmech_chebi_term" not in _ingredient(
        repaired,
        "Yeast extract",
    )
    assert "mediaingredientmech_chebi_term" not in _ingredient(
        repaired,
        "Casamino acid",
    )


def test_repair_record_scales_medium_193_inherited_components(repair) -> None:
    for target in repair.TARGETS:
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


def test_repair_record_adds_record_specific_references(repair) -> None:
    medium_208 = repair.repair_record(_doc(repair.TARGETS[0]), repair.TARGETS[0])
    medium_384 = repair.repair_record(_doc(repair.TARGETS[1]), repair.TARGETS[1])

    assert medium_208["references"] == [
        {"reference": repair.KOMODO_208_URL},
        {"reference": repair.DSMZ_208_URL},
        {"reference": repair.DSMZ_193_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_141_URL},
    ]
    assert medium_384["references"] == [
        {"reference": repair.KOMODO_384_URL},
        {"reference": repair.DSMZ_384_URL},
        {"reference": repair.DSMZ_194_URL},
        {"reference": repair.DSMZ_193_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_141_URL},
    ]
    assert medium_208["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    target = repair.TARGETS[0]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:004368"):
        repair.repair_record(doc, target)


def test_repair_record_rejects_wrong_source(repair) -> None:
    target = repair.TARGETS[1]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "komodo.medium:208"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:384"):
        repair.repair_record(doc, target)
