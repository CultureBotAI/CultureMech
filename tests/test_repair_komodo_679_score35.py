from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_679_score35.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _doc(repair, target) -> dict:
    return {
        "id": target.expected_id,
        "name": target.path.stem,
        "original_name": target.path.stem,
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": f"KOMODO Medium {target.media_term.removeprefix('komodo.medium:')}",
            "term": {
                "id": target.media_term,
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
    return _load_script(SCRIPT, "repair_komodo_679_score35")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_679")


def test_repair_record_adds_base_sb_sw_components(repair, scorer) -> None:
    target = repair.TARGETS_BY_ID["CultureMech:006278"]
    once = repair.repair_record(_doc(repair, target))
    twice = repair.repair_record(once)
    names = {ingredient["preferred_term"] for ingredient in once["ingredients"]}

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["ph_value"] == 7.2
    assert len(once["ingredients"]) == 21
    assert once["ingredients"][0]["preferred_term"] == "KH2PO4"
    assert _ingredient(once, "NH4Cl")["concentration"] == {
        "value": "0.249750",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "Na2S x 9 H2O")["concentration"] == {
        "value": "0.359640",
        "unit": "G_PER_L",
    }
    assert "2,3-butanediol" not in names
    assert "sodium crotonate" not in names
    assert "Sodium pyruvate" not in names
    assert "Na2S2O4" not in names


def test_repair_record_adds_buswellii_crotonate_variant(repair, scorer) -> None:
    target = repair.TARGETS_BY_ID["CultureMech:006276"]
    repaired = repair.repair_record(_doc(repair, target))
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

    assert scorer.score_record(repaired) == (0, [])
    assert len(repaired["ingredients"]) == 30
    assert _ingredient(repaired, "sodium crotonate")["concentration"] == {
        "value": "10.000000",
        "unit": "MILLIMOLAR",
    }
    assert _ingredient(repaired, "sodium crotonate")["term"] == {
        "id": "CHEBI:35899",
        "label": "crotonate",
    }
    assert "Sodium pyruvate" not in names


def test_repair_record_adds_wolinii_pyruvate_variant(repair, scorer) -> None:
    target = repair.TARGETS_BY_ID["CultureMech:006277"]
    repaired = repair.repair_record(_doc(repair, target))
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

    assert scorer.score_record(repaired) == (0, [])
    assert len(repaired["ingredients"]) == 30
    assert _ingredient(repaired, "Sodium pyruvate")["concentration"] == {
        "value": "1.250000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Sodium pyruvate")["term"] == {
        "id": "CHEBI:50144",
        "label": "sodium pyruvate",
    }
    assert "sodium crotonate" not in names


def test_repair_record_adds_vitamins_and_dithionite_to_variants(repair) -> None:
    target = repair.TARGETS_BY_ID["CultureMech:006276"]
    repaired = repair.repair_record(_doc(repair, target))

    assert _ingredient(repaired, "Vitamin B12")["source"] == repair.SOURCE_503
    assert _ingredient(repaired, "D(+)-Biotin")["term"] == {
        "id": "CHEBI:15956",
        "label": "biotin",
    }
    assert _ingredient(repaired, "Thiamine-HCl x 2 H2O")["source"] == repair.SOURCE_503
    assert _ingredient(repaired, "Na2S2O4")["concentration"] == {
        "value": "0.010-0.020",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2S2O4")["term"] == {
        "id": "CHEBI:66870",
        "label": "sodium dithionite",
    }


def test_repair_record_adds_references_and_flags(repair) -> None:
    base_target = repair.TARGETS_BY_ID["CultureMech:006278"]
    variant_target = repair.TARGETS_BY_ID["CultureMech:006276"]

    base = repair.repair_record(_doc(repair, base_target))
    variant = repair.repair_record(_doc(repair, variant_target))

    assert base["references"] == [
        {"reference": base_target.komodo_url},
        {"reference": repair.DSMZ_679_URL},
        {"reference": repair.DSMZ_298_URL},
        {"reference": repair.DSMZ_320_URL},
    ]
    assert variant["references"] == [
        {"reference": variant_target.komodo_url},
        {"reference": repair.DSMZ_679_URL},
        {"reference": repair.DSMZ_298_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_503_URL},
        {"reference": repair.DSMZ_383_URL},
    ]
    assert variant["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    target = repair.TARGETS_BY_ID["CultureMech:006278"]
    doc = _doc(repair, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    target = repair.TARGETS_BY_ID["CultureMech:006278"]
    doc = _doc(repair, target)
    doc["media_term"]["term"]["id"] = "komodo.medium:725"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:679"):
        repair.repair_record(doc)
