from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_327_score35.py"
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
        "id": "CultureMech:005020",
        "name": "anaerobic_acetoin_medium",
        "original_name": "ANAEROBIC ACETOIN medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 327",
            "term": {
                "id": "komodo.medium:327",
                "label": "ANAEROBIC ACETOIN medium",
            },
        },
        "notes": (
            "Source: KOMODO ModelSEED | ID: 327 | DSMZ Medium: 327 "
            "(mediadive.medium:327) | Aerobic: No"
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


def test_repair_record_adds_anaerobic_acetoin_components() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_327_score35")

    repaired = repair.repair_record(_minimal_doc())

    assert repaired["notes"] == repair.NOTES
    assert repaired["ph_value"] == 7.2
    assert len(repaired["ingredients"]) == 30
    assert repaired["ingredients"][0]["preferred_term"] == "KH2PO4"
    assert repaired["ingredients"][-1] == {
        "preferred_term": "Distilled water",
        "source": repair.SOURCE_212,
        "notes": (
            "Archived DSMZ Medium 212 lists 900 mL direct distilled water "
            "across solutions A-D before adding mineral, trace, vitamin, "
            "and rumen-fluid stocks."
        ),
        "concentration": {"value": "900.000", "unit": "ML_PER_L"},
        "term": {"id": "CHEBI:15377", "label": "water"},
        "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
    }


def test_repair_record_applies_213_and_327_substitutions() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_327_score35_substitutions")

    repaired = repair.repair_record(_minimal_doc())
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

    assert "Na2SO4" not in names
    assert "Butyric acid" not in names
    assert _ingredient(repaired, "Acetoin")["source"] == repair.SOURCE_327
    assert _ingredient(repaired, "Acetoin")["concentration"] == {
        "value": "1.500000",
        "unit": "G_PER_L",
    }


def test_repair_record_scales_212_base_and_mineral_stocks() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_327_score35_base")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "KH2PO4")["concentration"] == {
        "value": "0.497018",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "MgCl2 x 6 H2O")["concentration"] == {
        "value": "0.328032",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Rumen fluid, clarified")["concentration"] == {
        "value": "49.701789",
        "unit": "ML_PER_L",
    }
    assert _ingredient(repaired, "NaHCO3")["concentration"] == {
        "value": "3.479125",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Cysteine-HCl x H2O")["concentration"] == {
        "value": "0.298211",
        "unit": "G_PER_L",
    }


def test_repair_record_scales_trace_and_vitamin_stocks() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_327_score35_stocks")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "HCl")["concentration"] == {
        "value": "0.002485",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "FeCl2 x 4 H2O")["concentration"] == {
        "value": "0.001491",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "CoCl2 x 6 H2O")["concentration"] == {
        "value": "0.000189",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Pantothenic acid")["concentration"] == {
        "value": "0.00000308",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Pyridoxine-HCl")["concentration"] == {
        "value": "0.0000308",
        "unit": "G_PER_L",
    }


def test_repair_record_grounds_defined_substrates_salts_and_gases() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_327_score35_terms")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "Acetoin")["term"] == {
        "id": "CHEBI:15688",
        "label": "acetoin",
    }
    assert _ingredient(repaired, "MgCl2 x 6 H2O")["term"] == {
        "id": "CHEBI:86345",
        "label": "magnesium dichloride hexahydrate",
    }
    assert _ingredient(repaired, "Cysteine-HCl x H2O")["term"] == {
        "id": "CHEBI:91248",
        "label": "L-cysteine hydrochloride hydrate",
    }
    assert _ingredient(repaired, "Na2S x 9 H2O")["term"] == {
        "id": "CHEBI:76209",
        "label": "sodium sulfide nonahydrate",
    }
    assert _ingredient(repaired, "CO2")["term"] == {
        "id": "CHEBI:16526",
        "label": "carbon dioxide",
    }
    assert _ingredient(repaired, "N2")["term"] == {
        "id": "CHEBI:17997",
        "label": "dinitrogen",
    }
    assert "term" not in _ingredient(repaired, "Trypticase")
    assert "term" not in _ingredient(repaired, "Rumen fluid, clarified")


def test_repair_record_scores_as_complete_and_is_idempotent() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_327_score35_idempotent")
    scorer = _load_script(SCORER, "score_review_need_for_komodo_327")

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
        {"reference": repair.KOMODO_327_URL},
        {"reference": repair.DSMZ_327_URL},
        {"reference": repair.DSMZ_213_URL},
        {"reference": repair.DSMZ_212_URL},
        {"reference": repair.DSMZ_320_URL},
    ]
    events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair.CURATOR
        and event.get("action") == repair.ACTION
    ]
    assert len(events) == 1


def test_repair_record_rejects_wrong_id() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_327_score35_wrong_id")
    doc = _minimal_doc()
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:005020"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_327_score35_wrong_source")
    doc = _minimal_doc()
    doc["media_term"]["term"]["id"] = "mediadive.medium:327"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:327"):
        repair.repair_record(doc)
