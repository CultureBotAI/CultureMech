from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_197_score35.py"
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
        "id": "CultureMech:004258",
        "name": "desulfococcus_medium",
        "original_name": "DESULFOCOCCUS MEDIUM",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 197",
            "term": {"id": "komodo.medium:197", "label": "DESULFOCOCCUS MEDIUM"},
        },
        "notes": (
            "Source: KOMODO ModelSEED | ID: 197 | DSMZ Medium: 197 "
            "(mediadive.medium:197) | Aerobic: No"
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


def test_repair_record_adds_desulfococcus_components() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_197_score35")

    repaired = repair.repair_record(_minimal_doc())

    assert repaired["notes"] == repair.NOTES
    assert repaired["ph_range"] == {"min": 7.1, "max": 7.4}
    assert len(repaired["ingredients"]) == 34
    assert repaired["ingredients"][0]["preferred_term"] == "Na2SO4"
    assert repaired["ingredients"][-1]["preferred_term"] == "Distilled water"


def test_repair_record_replaces_acetate_with_benzoate_and_selenite() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_197_score35_substitutions")

    repaired = repair.repair_record(_minimal_doc())
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

    assert "Na-acetate x 3 H2O" not in names
    assert "Na-acetate" not in names
    assert _ingredient(repaired, "Sodium benzoate")["source"] == repair.SOURCE_197
    assert _ingredient(repaired, "Sodium benzoate")["term"] == {
        "id": "CHEBI:113455",
        "label": "sodium benzoate",
    }
    assert _ingredient(repaired, "Sodium benzoate")["concentration"] == {
        "value": "0.600000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2SeO3 x 5 H2O")["concentration"] == {
        "value": "3.0",
        "unit": "MICROG_PER_L",
    }


def test_repair_record_scales_193_base_trace_and_vitamin_stocks() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_197_score35_stocks")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "NaCl")["concentration"] == {
        "value": "6.993007",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "FeCl2 x 4 H2O")["concentration"] == {
        "value": "0.001499",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "NaHCO3")["concentration"] == {
        "value": "4.995005",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "D-Ca-pantothenate")["concentration"] == {
        "value": "0.0000500",
        "unit": "G_PER_L",
    }


def test_repair_record_scores_as_complete_and_is_idempotent() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_197_score35_idempotent")
    scorer = _load_script(SCORER, "score_review_need_for_komodo_197")

    once = repair.repair_record(_minimal_doc())
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert twice["references"] == [
        {"reference": repair.KOMODO_197_URL},
        {"reference": repair.DSMZ_197_URL},
        {"reference": repair.DSMZ_193_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_141_URL},
    ]


def test_repair_record_rejects_wrong_id() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_197_score35_wrong_id")
    doc = _minimal_doc()
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:004258"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_197_score35_wrong_source")
    doc = _minimal_doc()
    doc["media_term"]["term"]["id"] = "mediadive.medium:197"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:197"):
        repair.repair_record(doc)
