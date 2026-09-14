from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_682_score35.py"
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
        "id": "CultureMech:006282",
        "name": "desulfotomaculum_sp_medium_ii",
        "original_name": "DESULFOTOMACULUM SP. MEDIUM II",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 682",
            "term": {
                "id": "komodo.medium:682",
                "label": "DESULFOTOMACULUM SP. MEDIUM II",
            },
        },
        "notes": (
            "Source: KOMODO ModelSEED | ID: 682 | DSMZ Medium: 682 "
            "(mediadive.medium:682) | Aerobic: No"
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


def test_repair_record_adds_desulfotomaculum_sp_ii_components() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_682_score35")

    repaired = repair.repair_record(_minimal_doc())

    assert repaired["notes"] == repair.NOTES
    assert repaired["ph_range"] == {"min": 7.1, "max": 7.4}
    assert len(repaired["ingredients"]) == 35
    assert repaired["ingredients"][0] == {
        "preferred_term": "Na2SO4",
        "source": repair.SOURCE_682,
        "notes": "Archived DSMZ Medium 682 lowers the sodium sulfate amount to 0.7 g/L.",
        "concentration": {"value": "0.700000", "unit": "G_PER_L"},
        "term": {"id": "CHEBI:32149", "label": "sodium sulfate"},
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:32149",
            "label": "sodium sulfate",
        },
    }
    assert repaired["ingredients"][-1]["concentration"] == {
        "value": "990.000",
        "unit": "ML_PER_L",
    }


def test_repair_record_applies_194_and_682_substitutions() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_682_score35_substitutions")

    repaired = repair.repair_record(_minimal_doc())
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

    assert "Na-acetate x 3 H2O" not in names
    assert "Na-propionate" not in names
    assert "Sodium propionate" not in names
    assert _ingredient(repaired, "NaCl")["source"] == repair.SOURCE_194
    assert _ingredient(repaired, "NaCl")["concentration"] == {
        "value": "1.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "MgCl2 x 6 H2O")["concentration"] == {
        "value": "0.400000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "3,4,5-trimethoxybenzoate")["source"] == (repair.SOURCE_682)
    assert _ingredient(repaired, "3,4,5-trimethoxybenzoate")["term"] == {
        "id": "CHEBI:454991",
        "label": "3,4,5-trimethoxybenzoic acid",
    }
    assert _ingredient(repaired, "3,4,5-trimethoxybenzoate")["concentration"] == {
        "value": "2.000",
        "unit": "MILLIMOLAR",
    }


def test_repair_record_scales_193_base_and_sl10_stocks() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_682_score35_base")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "KCl")["concentration"] == {
        "value": "0.499002",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "NaHCO3")["concentration"] == {
        "value": "4.990020",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "HCl")["concentration"] == {
        "value": "0.002495",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2S x 9 H2O")["concentration"] == {
        "value": "0.399202",
        "unit": "G_PER_L",
    }


def test_repair_record_merges_vitamins_from_141_and_503() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_682_score35_vitamins")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "Biotin")["source"] == repair.SOURCE_141
    assert _ingredient(repaired, "Biotin")["concentration"] == {
        "value": "0.0000200",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "D(+)-Biotin")["source"] == repair.SOURCE_503
    assert _ingredient(repaired, "D(+)-Biotin")["term"] == {
        "id": "CHEBI:15956",
        "label": "biotin",
    }
    assert _ingredient(repaired, "Pyridoxine-HCl")["concentration"] == {
        "value": "0.000399",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Nicotinic acid")["concentration"] == {
        "value": "0.000250",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Vitamin B12")["concentration"] == {
        "value": "0.000101",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Calcium pantothenate")["concentration"] == {
        "value": "0.0000998",
        "unit": "G_PER_L",
    }


def test_repair_record_scores_as_complete_and_is_idempotent() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_682_score35_idempotent")
    scorer = _load_script(SCORER, "score_review_need_for_komodo_682")

    once = repair.repair_record(_minimal_doc())
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert twice["references"] == [
        {"reference": repair.KOMODO_682_URL},
        {"reference": repair.DSMZ_682_URL},
        {"reference": repair.DSMZ_194_URL},
        {"reference": repair.DSMZ_193_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_141_URL},
        {"reference": repair.DSMZ_503_URL},
    ]
    events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair.CURATOR and event.get("action") == repair.ACTION
    ]
    assert len(events) == 1


def test_repair_record_rejects_wrong_id() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_682_score35_wrong_id")
    doc = _minimal_doc()
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:006282"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_682_score35_wrong_source")
    doc = _minimal_doc()
    doc["media_term"]["term"]["id"] = "mediadive.medium:682"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:682"):
        repair.repair_record(doc)
