from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_313_score35.py"
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
        "id": "CultureMech:004988",
        "name": "acetobacterium_carbinolicum_medium",
        "original_name": "ACETOBACTERIUM CARBINOLICUM medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 313",
            "term": {
                "id": "komodo.medium:313",
                "label": "ACETOBACTERIUM CARBINOLICUM medium",
            },
        },
        "notes": (
            "Source: KOMODO ModelSEED | ID: 313 | DSMZ Medium: 313 "
            "(mediadive.medium:313) | Aerobic: No"
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


def test_repair_record_adds_acetobacterium_carbinolicum_components() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_313_score35")

    repaired = repair.repair_record(_minimal_doc())

    assert repaired["notes"] == repair.NOTES
    assert repaired["ph_range"] == {"min": 7.0, "max": 7.2}
    assert len(repaired["ingredients"]) == 27
    assert repaired["ingredients"][0]["preferred_term"] == "NaCl"
    assert repaired["ingredients"][-1] == {
        "preferred_term": "Distilled water",
        "source": repair.SOURCE_124,
        "notes": "Archived DSMZ Medium 124 lists 1000 mL distilled water for Solution A.",
        "concentration": {"value": "1000.000", "unit": "ML_PER_L"},
        "term": {"id": "CHEBI:15377", "label": "water"},
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:15377",
            "label": "water",
        },
    }


def test_repair_record_applies_313_ethanol_variant() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_313_score35_variant")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "Ethanol")["source"] == repair.SOURCE_313
    assert _ingredient(repaired, "Ethanol")["concentration"] == {
        "value": "20.000",
        "unit": "MILLIMOLAR",
    }


def test_repair_record_normalizes_124_base_and_solution_b() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_313_score35_base")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "Na2SO4")["concentration"] == {
        "value": "2.806324",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na-acetate")["concentration"] == {
        "value": "1.383399",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2S x 9 H2O")["source"] == (repair.SOURCE_124_SOLUTION_B)
    assert _ingredient(repaired, "Na2S x 9 H2O")["concentration"] == {
        "value": "0.355731",
        "unit": "G_PER_L",
    }


def test_repair_record_scales_trace_and_vitamin_stocks() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_313_score35_stocks")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "FeCl2 x 4 H2O")["concentration"] == {
        "value": "0.001482",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "HCl")["concentration"] == {
        "value": "0.049407",
        "unit": "MILLIMOLAR",
    }
    assert _ingredient(repaired, "p-Aminobenzoic acid")["concentration"] == {
        "value": "0.0000395",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "D(+)-Biotin")["concentration"] == {
        "value": "0.00000988",
        "unit": "G_PER_L",
    }


def test_repair_record_grounds_acetate_butyrate_and_hydrates() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_313_score35_terms")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "Na-acetate")["term"] == {
        "id": "CHEBI:32954",
        "label": "sodium acetate",
    }
    assert _ingredient(repaired, "Na-butyrate")["term"] == {
        "id": "CHEBI:64103",
        "label": "sodium butyrate",
    }
    assert _ingredient(repaired, "MgCl2 x 6 H2O")["term"] == {
        "id": "CHEBI:86345",
        "label": "magnesium dichloride hexahydrate",
    }
    assert _ingredient(repaired, "NiCl2 x 6 H2O")["term"] == {
        "id": "CHEBI:53542",
        "label": "nickel chloride hexahydrate",
    }


def test_repair_record_scores_as_complete_and_is_idempotent() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_313_score35_idempotent")
    scorer = _load_script(SCORER, "score_review_need_for_komodo_313")

    once = repair.repair_record(_minimal_doc())
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert twice["references"] == [
        {"reference": repair.KOMODO_313_URL},
        {"reference": repair.DSMZ_313_URL},
        {"reference": repair.DSMZ_124_URL},
    ]
    events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair.CURATOR and event.get("action") == repair.ACTION
    ]
    assert len(events) == 1


def test_repair_record_rejects_wrong_id() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_313_score35_wrong_id")
    doc = _minimal_doc()
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:004988"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_313_score35_wrong_source")
    doc = _minimal_doc()
    doc["media_term"]["term"]["id"] = "mediadive.medium:313"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:313"):
        repair.repair_record(doc)
