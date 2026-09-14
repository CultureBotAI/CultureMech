from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_409_score35.py"
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
    return _load_script(SCRIPT, "repair_komodo_409_score35")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_409")


def test_repair_record_adds_syntrophus_buswellii_components(repair, scorer) -> None:
    target = repair.TARGETS_BY_ID["CultureMech:005230"]
    once = repair.repair_record(_doc(repair, target))
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["ph_range"] == {"min": 7.1, "max": 7.4}
    assert len(once["ingredients"]) == 36
    assert once["ingredients"][0]["preferred_term"] == "Na2SO4"
    assert _ingredient(once, "sodium benzoate")["concentration"] == {
        "value": "3.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "Sodium acetate")["term"] == {
        "id": "CHEBI:32954",
        "label": "sodium acetate",
    }


def test_repair_record_omits_sulfate_for_dsm_4156_b_and_c(
    repair,
    scorer,
) -> None:
    target = repair.TARGETS_BY_ID["CultureMech:005229"]
    repaired = repair.repair_record(_doc(repair, target))
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

    assert scorer.score_record(repaired) == (0, [])
    assert len(repaired["ingredients"]) == 35
    assert "Na2SO4" not in names
    assert "sodium propionate" not in names
    assert "Sodium propionate" not in names


def test_repair_record_reduces_sulfide_and_adds_reductants(repair) -> None:
    target = repair.TARGETS_BY_ID["CultureMech:005230"]
    repaired = repair.repair_record(_doc(repair, target))

    assert _ingredient(repaired, "Na2S x 9 H2O")["concentration"] == {
        "value": "0.060000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2SeO3 x 5 H2O")["term"] == {
        "id": "CHEBI:131361",
        "label": "disodium selenite pentahydrate",
    }
    assert _ingredient(repaired, "Na2S2O4")["term"] == {
        "id": "CHEBI:66870",
        "label": "sodium dithionite",
    }


def test_repair_record_adds_references_and_flags(repair) -> None:
    target = repair.TARGETS_BY_ID["CultureMech:005230"]
    repaired = repair.repair_record(_doc(repair, target))

    assert repaired["references"] == [
        {"reference": target.komodo_url},
        {"reference": repair.DSMZ_409_URL},
        {"reference": repair.DSMZ_194_URL},
        {"reference": repair.DSMZ_193_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_141_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    target = repair.TARGETS_BY_ID["CultureMech:005230"]
    doc = _doc(repair, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    target = repair.TARGETS_BY_ID["CultureMech:005230"]
    doc = _doc(repair, target)
    doc["media_term"]["term"]["id"] = "komodo.medium:725"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:409"):
        repair.repair_record(doc)
