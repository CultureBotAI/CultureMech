from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_164_score35.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _minimal_doc(target) -> dict:
    return {
        "id": target.expected_id,
        "name": Path(target.path).stem,
        "original_name": "METHANOSARCINA (thermophilic) medium",
        "category": "archaea",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 164",
            "term": {"id": target.expected_media_term, "label": "METHANOSARCINA"},
        },
        "notes": "Source: KOMODO ModelSEED | ID: 164 | Aerobic: No",
        "ingredients": [],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
    }


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for ingredient in doc["ingredients"]:
        if ingredient["preferred_term"] == preferred_term:
            return ingredient
    raise AssertionError(f"missing ingredient {preferred_term!r}")


def test_repair_record_adds_base_thermophilic_components() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_164_score35")
    target = repair.TARGETS[0]

    repaired = repair.repair_record(_minimal_doc(target), target)

    assert repaired["notes"] == target.notes
    assert len(repaired["ingredients"]) == 35
    assert repaired["ingredients"][0]["preferred_term"] == "K2HPO4"
    assert repaired["ingredients"][-1] == {
        "preferred_term": "Rumen fluid, clarified",
        "source": repair.SOURCE_164,
        "notes": (
            "DSMZ/KOMODO Medium 164 applies 50.000 ML_PER_L "
            "Rumen fluid, clarified."
        ),
        "concentration": {"value": "50.000", "unit": "ML_PER_L"},
    }


def test_repair_record_adds_sludge_replacement_components() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_164_score35_sludge")
    target = repair.TARGETS[1]

    repaired = repair.repair_record(_minimal_doc(target), target)

    assert len(repaired["ingredients"]) == 35
    assert repaired["ingredients"][-1] == {
        "preferred_term": "Sludge fluid (medium 119)",
        "source": repair.SOURCE_164,
        "notes": (
            "DSMZ/KOMODO Medium 164 sludge variant applies 50.000 ML_PER_L "
            "Sludge fluid (medium 119)."
        ),
        "concentration": {"value": "50.000", "unit": "ML_PER_L"},
    }


def test_repair_record_scales_referenced_stock_solutions() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_164_score35_stocks")
    target = repair.TARGETS[0]

    repaired = repair.repair_record(_minimal_doc(target), target)

    assert _ingredient(repaired, "NaHCO3")["concentration"] == {
        "value": "2.000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Biotin")["concentration"] == {
        "value": "0.00002",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Vitamin B12")["concentration"] == {
        "value": "0.000001",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "HCl")["concentration"] == {
        "value": "0.0025",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "NiCl2 x 6 H2O")["concentration"] == {
        "value": "0.000024",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Methanol")["concentration"] == {
        "value": "10.000",
        "unit": "ML_PER_L",
    }


def test_repair_record_grounds_hydrates_and_vitamins() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_164_score35_terms")
    target = repair.TARGETS[0]

    repaired = repair.repair_record(_minimal_doc(target), target)

    assert _ingredient(repaired, "Thiamine-HCl x 2 H2O")["term"] == {
        "id": "CHEBI:132751",
        "label": "Thiamine-HCl x 2 H2O",
    }
    assert _ingredient(repaired, "D-Ca-pantothenate")["term"] == {
        "id": "CHEBI:31345",
        "label": "Calcium pantothenate",
    }
    assert _ingredient(repaired, "NiCl2 x 6 H2O")["term"] == {
        "id": "CHEBI:53542",
        "label": "nickel chloride hexahydrate",
    }
    assert _ingredient(repaired, "Methanol")["term"] == {
        "id": "CHEBI:17790",
        "label": "methanol",
    }
    assert "term" not in _ingredient(repaired, "Casitone")


def test_repair_record_scores_as_complete_and_is_idempotent() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_164_score35_idempotent")
    scorer = _load_script(SCORER, "score_review_need_for_komodo_164")

    for target in repair.TARGETS:
        once = repair.repair_record(_minimal_doc(target), target)
        twice = repair.repair_record(once, target)

        assert once == twice
        assert scorer.score_record(twice) == (5, ["no pH and no temperature"])
        assert twice["data_quality_flags"] == [
            "has_ontology_mappings",
            "ingredients_curated",
            "has_unmapped_ingredients",
        ]
        events = [
            event
            for event in twice["curation_history"]
            if event.get("curator") == repair.CURATOR and event.get("action") == target.action
        ]
        assert len(events) == 1


def test_repair_record_rejects_wrong_id() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_164_score35_wrong_id")
    target = repair.TARGETS[0]
    doc = _minimal_doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:004191"):
        repair.repair_record(doc, target)


def test_repair_record_rejects_wrong_source() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_164_score35_wrong_source")
    target = repair.TARGETS[0]
    doc = _minimal_doc(target)
    doc["media_term"]["term"]["id"] = "mediadive.medium:164"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:164"):
        repair.repair_record(doc, target)
