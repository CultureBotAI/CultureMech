from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_787_score30.py"
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
        "name": "acetobacterium_dehalogenans_medium",
        "original_name": "ACETOBACTERIUM DEHALOGENANS medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.4,
        "media_term": {
            "preferred_term": "KOMODO Medium 787",
            "term": {
                "id": repair.EXPECTED_MEDIA_TERM,
                "label": "ACETOBACTERIUM DEHALOGENANS medium",
            },
        },
        "notes": "Source: KOMODO ModelSEED | ID: 787 | DSMZ Medium: 787",
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
    return _load_script(SCRIPT, "repair_komodo_787_score30")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_787")


def test_repair_record_expands_acetobacterium_dehalogenans_medium(
    repair,
    scorer,
) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["medium_type"] == "COMPLEX"
    assert once["composition_type"] == "UNDEFINED"
    assert once["ph_value"] == 7.4
    assert len(once["ingredients"]) == 36


def test_repair_record_omits_fructose_and_sulfide(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert all(i["preferred_term"] != "Fructose" for i in repaired["ingredients"])
    assert all(i["preferred_term"] != "Na2S x 9 H2O" for i in repaired["ingredients"])


def test_repair_record_scales_base_trace_and_stock_components(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "NH4Cl")["concentration"] == {
        "value": "0.927759",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Nitrilotriacetic acid")["concentration"] == {
        "value": "0.026163",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "NaHCO3")["concentration"] == {
        "value": "9.689922",
        "unit": "G_PER_L",
    }


def test_repair_record_adds_sodium_syringate(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "Na-syringate")["term"] == {
        "id": "CHEBI:132110",
        "label": "sodium syringate",
    }
    assert _ingredient(repaired, "Na-syringate")["concentration"] == {
        "value": "0.872093",
        "unit": "G_PER_L",
    }


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_787_URL},
        {"reference": repair.DSMZ_787_URL},
        {"reference": repair.DSMZ_135_URL},
        {"reference": repair.DSMZ_141_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:006488"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:135"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:787"):
        repair.repair_record(doc)
