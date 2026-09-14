from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_560_score35.py"
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
        "id": "CultureMech:006012",
        "name": "mtp4_medium",
        "original_name": "MTP4 MEDIUM",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 560",
            "term": {
                "id": "komodo.medium:560",
                "label": "MTP4 MEDIUM",
            },
        },
        "notes": (
            "Source: KOMODO ModelSEED | ID: 560 | DSMZ Medium: 560 "
            "(mediadive.medium:560) | Aerobic: Yes"
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


def test_repair_record_adds_mtp4_components() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_560_score35")

    repaired = repair.repair_record(_minimal_doc())

    assert repaired["notes"] == repair.NOTES
    assert repaired["ph_range"] == {"min": 7.1, "max": 7.4}
    assert len(repaired["ingredients"]) == 34
    assert repaired["ingredients"][0]["preferred_term"] == "KH2PO4"
    assert repaired["ingredients"][-1] == {
        "preferred_term": "Distilled water",
        "source": repair.SOURCE_193,
        "notes": (
            "Archived DSMZ Medium 193 lists 990 mL direct distilled water "
            "across solutions A, C, D, and F before stock additions and "
            "before Archived DSMZ Medium 560 omits sulfate and acetate."
        ),
        "concentration": {"value": "990.000", "unit": "ML_PER_L"},
        "term": {"id": "CHEBI:15377", "label": "water"},
        "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
    }


def test_repair_record_applies_195_branch_and_560_omissions() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_560_score35_branch")

    repaired = repair.repair_record(_minimal_doc())
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

    assert "Na2SO4" not in names
    assert "Na-acetate x 3 H2O" not in names
    assert "Na-acetate" not in names
    assert _ingredient(repaired, "NaCl")["source"] == repair.SOURCE_195
    assert _ingredient(repaired, "NaCl")["concentration"] == {
        "value": "21.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "MgCl2 x 6 H2O")["concentration"] == {
        "value": "3.100000",
        "unit": "G_PER_L",
    }


def test_repair_record_adds_560_substrates_and_reductants() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_560_score35_substrates")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "Methanol")["term"] == {
        "id": "CHEBI:17790",
        "label": "methanol",
    }
    assert _ingredient(repaired, "Methanol")["concentration"] == {
        "value": "20.000-30.000",
        "unit": "MILLIMOLAR",
    }
    assert _ingredient(repaired, "Methanethiol")["term"] == {
        "id": "CHEBI:16007",
        "label": "methanethiol",
    }
    assert _ingredient(repaired, "Methanethiol")["concentration"] == {
        "value": "20.000-40.000",
        "unit": "ML_PER_L",
    }
    assert "mediaingredientmech_chebi_term" not in _ingredient(repaired, "Methanethiol")
    assert _ingredient(repaired, "Na2S x 9 H2O")["source"] == repair.SOURCE_560
    assert _ingredient(repaired, "Na2S x 9 H2O")["concentration"] == {
        "value": "0.400000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2S2O4")["concentration"] == {
        "value": "0.010-0.020",
        "unit": "G_PER_L",
    }


def test_repair_record_scales_193_base_and_stocks() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_560_score35_base")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "KCl")["concentration"] == {
        "value": "0.499500",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "NaHCO3")["concentration"] == {
        "value": "4.995005",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "HCl")["concentration"] == {
        "value": "0.002498",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Vitamin B12")["concentration"] == {
        "value": "0.000000999",
        "unit": "G_PER_L",
    }


def test_repair_record_scores_as_complete_and_is_idempotent() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_560_score35_idempotent")
    scorer = _load_script(SCORER, "score_review_need_for_komodo_560")

    once = repair.repair_record(_minimal_doc())
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert twice["references"] == [
        {"reference": repair.KOMODO_560_URL},
        {"reference": repair.DSMZ_560_URL},
        {"reference": repair.DSMZ_195_URL},
        {"reference": repair.DSMZ_193_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_141_URL},
    ]
    events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair.CURATOR and event.get("action") == repair.ACTION
    ]
    assert len(events) == 1


def test_repair_record_rejects_wrong_id() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_560_score35_wrong_id")
    doc = _minimal_doc()
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:006012"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_560_score35_wrong_source")
    doc = _minimal_doc()
    doc["media_term"]["term"]["id"] = "mediadive.medium:560"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:560"):
        repair.repair_record(doc)
