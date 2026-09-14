from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_349_score35.py"
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
        "id": "CultureMech:005062",
        "name": "acetobacterium_2_medium",
        "original_name": "ACETOBACTERIUM 2 medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 349",
            "term": {"id": "komodo.medium:349", "label": "ACETOBACTERIUM 2 medium"},
        },
        "notes": (
            "Source: KOMODO ModelSEED | ID: 349 | DSMZ Medium: 349 "
            "(mediadive.medium:349) | Aerobic: No"
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


def test_repair_record_adds_acetobacterium_2_components() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_349_score35")

    repaired = repair.repair_record(_minimal_doc())

    assert repaired["notes"] == repair.NOTES
    assert len(repaired["ingredients"]) == 34
    assert repaired["ingredients"][0]["preferred_term"] == "NH4Cl"
    assert repaired["ingredients"][-1] == {
        "preferred_term": "Distilled water",
        "source": repair.SOURCE_135,
        "notes": "Archived DSMZ Medium 135 lists 1000 mL distilled water.",
        "concentration": {"value": "1000.000", "unit": "ML_PER_L"},
        "term": {"id": "CHEBI:15377", "label": "water"},
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:15377",
            "label": "water",
        },
    }


def test_repair_record_applies_349_variant_instruction() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_349_score35_variant")

    repaired = repair.repair_record(_minimal_doc())
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

    assert "D-Fructose" not in names
    assert _ingredient(repaired, "Ethylene glycol")["concentration"] == {
        "value": "1.250000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "NaCl")["concentration"] == {
        "value": "20.019231",
        "unit": "G_PER_L",
    }


def test_repair_record_scales_2012_trace_and_vitamin_stocks() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_349_score35_scaled")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "MgSO4 x 7 H2O")["concentration"] == {
        "value": "0.153846",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Nitrilotriacetic acid")["concentration"] == {
        "value": "0.028846",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2SeO3 x 5 H2O")["concentration"] == {
        "value": "0.00000577",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Biotin")["concentration"] == {
        "value": "0.000038",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Vitamin B12")["concentration"] == {
        "value": "0.00000192",
        "unit": "G_PER_L",
    }


def test_repair_record_grounds_variant_and_hydrated_trace_components() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_349_score35_terms")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "Ethylene glycol")["term"] == {
        "id": "CHEBI:30742",
        "label": "ethylene glycol",
    }
    assert _ingredient(repaired, "KAl(SO4)2 x 12 H2O")["term"] == {
        "id": "CHEBI:86465",
        "label": "potassium aluminium sulfate dodecahydrate",
    }
    assert _ingredient(repaired, "CoSO4 x 7 H2O")["term"] == {
        "id": "CHEBI:91244",
        "label": "cobalt(2+) sulfate heptahydrate",
    }
    assert _ingredient(repaired, "NiCl2 x 6 H2O")["term"] == {
        "id": "CHEBI:53542",
        "label": "nickel chloride hexahydrate",
    }


def test_repair_record_scores_as_complete_and_is_idempotent() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_349_score35_idempotent")
    scorer = _load_script(SCORER, "score_review_need_for_komodo_349")

    once = repair.repair_record(_minimal_doc())
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (5, ["no pH and no temperature"])
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair.CURATOR
        and event.get("action") == "RESOLVED_KOMODO_349_SCORE35"
    ]
    assert len(events) == 1


def test_repair_record_rejects_wrong_id() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_349_score35_wrong_id")
    doc = _minimal_doc()
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:005062"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_349_score35_wrong_source")
    doc = _minimal_doc()
    doc["media_term"]["term"]["id"] = "mediadive.medium:349"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:349"):
        repair.repair_record(doc)
