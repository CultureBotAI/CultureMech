from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_777_14980_score35.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _doc(repair) -> dict:
    return {
        "id": repair.EXPECTED_ID,
        "name": "medium_777_modified_for_dsm_14980",
        "original_name": "MEDIUM 777 MODIFIED FOR DSM 14980",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 777_14980",
            "term": {
                "id": repair.EXPECTED_MEDIA_TERM,
                "label": "MEDIUM 777 MODIFIED FOR DSM 14980",
            },
        },
        "notes": "Source: KOMODO ModelSEED | ID: 777_14980",
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
    return _load_script(SCRIPT, "repair_komodo_777_14980_score35")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_777_14980")


def test_repair_record_expands_dsm_14980_variant(repair, scorer) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (5, ["no pH and no temperature"])
    assert len(once["ingredients"]) == 38
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_record_applies_777_14980_carbon_sources(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "D-Glucose")["concentration"] == {
        "value": "8.00",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "D-Glucose")["term"] == {
        "id": "CHEBI:17634",
        "label": "D-glucose",
    }
    assert _ingredient(repaired, "Na-pyruvate")["concentration"] == {
        "value": "2.00",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na-pyruvate")["term"] == {
        "id": "CHEBI:50144",
        "label": "sodium pyruvate",
    }


def test_repair_record_keeps_casitone_unmapped_and_omits_fructose(repair) -> None:
    repaired = repair.repair_record(_doc(repair))
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

    assert _ingredient(repaired, "Yeast extract")["concentration"] == {
        "value": "2.98",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Casitone")["concentration"] == {
        "value": "2.98",
        "unit": "G_PER_L",
    }
    assert "term" not in _ingredient(repaired, "Casitone")
    assert "D-Fructose" not in names
    assert "Betaine x H2O" not in names


def test_repair_record_links_parent_variant(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["parent_media"] == {
        "path": repair.PARENT,
        "relationship": "STRAIN_SPECIFIC_VARIANT",
        "id": "CultureMech:006435",
        "name": "sporomusa_silvacetica_medium",
    }
    assert repaired["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"


def test_repair_record_adds_references_and_history_once(repair) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)

    assert twice["references"] == [
        {"reference": repair.KOMODO_777_14980_URL},
        {"reference": repair.DSMZ_777_URL},
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (event.get("curator") == repair.CURATOR and event.get("action") == repair.ACTION)
    ]
    assert len(matching_events) == 1


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:006434"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:777"

    with pytest.raises(ValueError, match="expected source term komodo.medium:777_14980"):
        repair.repair_record(doc)


def test_repair_record_rejects_ingredient_drift(repair) -> None:
    doc = _doc(repair)
    doc["ingredients"] = [{"preferred_term": "unexpected"}]

    with pytest.raises(ValueError, match="ingredient list drifted"):
        repair.repair_record(doc)
