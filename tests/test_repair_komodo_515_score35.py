from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_515_score35.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _minimal_doc() -> dict:
    return {
        "id": "CultureMech:005871",
        "name": "acetonema_medium",
        "original_name": "ACETONEMA medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 515",
            "term": {
                "id": "komodo.medium:515",
                "label": "ACETONEMA medium",
            },
        },
        "notes": (
            "Source: KOMODO ModelSEED | ID: 515 | DSMZ Medium: 515 "
            "(mediadive.medium:515) | Aerobic: No"
        ),
        "ingredients": [],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
    }


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for ingredient in doc["ingredients"]:
        if ingredient["preferred_term"] == preferred_term:
            return ingredient
    raise AssertionError(f"missing ingredient {preferred_term!r}")


def test_repair_record_adds_acetonema_components() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_515_score35")

    repaired = repair.repair_record(_minimal_doc())

    assert repaired["notes"] == repair.NOTES
    assert repaired["ph_value"] == 7.0
    assert len(repaired["ingredients"]) == 36
    assert repaired["ingredients"][0]["preferred_term"] == "K2HPO4"
    assert repaired["ingredients"][-1] == {
        "preferred_term": "Distilled water",
        "source": repair.SOURCE_311,
        "notes": (
            "Archived DSMZ Medium 311 lists 1000 mL distilled water before "
            "addition of 10 mL vitamin stock and 1 mL SL-10 trace stock."
        ),
        "concentration": {"value": "1000.000", "unit": "ML_PER_L"},
        "term": {"id": "CHEBI:15377", "label": "water"},
        "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
    }


def test_repair_record_applies_515_substitutions() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_515_score35_substitutions")

    repaired = repair.repair_record(_minimal_doc())
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

    assert "Betaine x H2O" not in names
    assert "Cysteine-HCl x H2O" not in names
    assert "Na2S x 9 H2O" not in names
    assert _ingredient(repaired, "D-Glucose")["source"] == repair.SOURCE_515
    assert _ingredient(repaired, "D-Glucose")["concentration"] == {
        "value": "2.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Dithiothreitol")["source"] == repair.SOURCE_515
    assert _ingredient(repaired, "Dithiothreitol")["concentration"] == {
        "value": "1.000",
        "unit": "MILLIMOLAR",
    }


def test_repair_record_scales_base_trace_and_vitamin_stocks() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_515_score35_stocks")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "NaCl")["concentration"] == {
        "value": "2.225519",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "NaHCO3")["concentration"] == {
        "value": "3.956479",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "CoCl2 x 6 H2O")["concentration"] == {
        "value": "0.000188",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "D-Ca-pantothenate")["concentration"] == {
        "value": "0.0000495",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Vitamin B12")["concentration"] == {
        "value": "0.000000989",
        "unit": "G_PER_L",
    }


def test_repair_record_grounds_substitutions_and_gases() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_515_score35_terms")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "D-Glucose")["term"] == {
        "id": "CHEBI:17634",
        "label": "D-glucose",
    }
    assert _ingredient(repaired, "Dithiothreitol")["term"] == {
        "id": "CHEBI:18320",
        "label": "1,4-dithiothreitol",
    }
    assert _ingredient(repaired, "CO2")["term"] == {
        "id": "CHEBI:16526",
        "label": "carbon dioxide",
    }
    assert _ingredient(repaired, "N2")["term"] == {
        "id": "CHEBI:17997",
        "label": "dinitrogen",
    }
    assert "term" not in _ingredient(repaired, "Casitone")


def test_repair_record_scores_as_complete_and_is_idempotent() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_515_score35_idempotent")
    scorer = _load_script(SCORER, "score_review_need_for_komodo_515")

    once = repair.repair_record(_minimal_doc())
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
        "has_unmapped_ingredients",
    ]
    assert twice["references"] == [
        {"reference": repair.KOMODO_515_URL},
        {"reference": repair.DSMZ_515_URL},
        {"reference": repair.DSMZ_311_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_141_URL},
    ]
    events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair.CURATOR
        and event.get("action") == repair.ACTION
    ]
    assert len(events) == 1


def test_repair_record_rejects_wrong_id() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_515_score35_wrong_id")
    doc = _minimal_doc()
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:005871"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_515_score35_wrong_source")
    doc = _minimal_doc()
    doc["media_term"]["term"]["id"] = "mediadive.medium:515"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:515"):
        repair.repair_record(doc)
