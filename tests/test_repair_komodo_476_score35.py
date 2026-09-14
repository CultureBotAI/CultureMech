from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_476_score35.py"
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
        "id": "CultureMech:005590",
        "name": "desulfobacterium_anilini_medium",
        "original_name": "DESULFOBACTERIUM ANILINI MEDIUM",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 476",
            "term": {
                "id": "komodo.medium:476",
                "label": "DESULFOBACTERIUM ANILINI MEDIUM",
            },
        },
        "notes": (
            "Source: KOMODO ModelSEED | ID: 476 | DSMZ Medium: 476 "
            "(mediadive.medium:476) | Aerobic: Yes"
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


def test_repair_record_adds_desulfobacterium_anilini_components() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_476_score35")

    repaired = repair.repair_record(_minimal_doc())

    assert repaired["notes"] == repair.NOTES
    assert repaired["ph_range"] == {"min": 7.1, "max": 7.4}
    assert len(repaired["ingredients"]) == 39
    assert repaired["ingredients"][0]["preferred_term"] == "Na2SO4"
    assert repaired["ingredients"][-1] == {
        "preferred_term": "Distilled water",
        "source": repair.SOURCE_193,
        "notes": (
            "Archived DSMZ Medium 193 lists 990 mL direct distilled water "
            "across solutions A, C, D, and F before stock additions and "
            "before Archived DSMZ Medium 476 replaces the dissolved acetate "
            "with a phenol stock."
        ),
        "concentration": {"value": "990.000", "unit": "ML_PER_L"},
        "term": {"id": "CHEBI:15377", "label": "water"},
        "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
    }


def test_repair_record_replaces_acetate_with_phenol() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_476_score35_phenol")

    repaired = repair.repair_record(_minimal_doc())
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

    assert "Na-acetate x 3 H2O" not in names
    assert "Na-acetate" not in names
    assert _ingredient(repaired, "Phenol")["source"] == repair.SOURCE_476
    assert _ingredient(repaired, "Phenol")["term"] == {
        "id": "CHEBI:15882",
        "label": "phenol",
    }
    assert _ingredient(repaired, "Phenol")["concentration"] == {
        "value": "1.000",
        "unit": "MILLIMOLAR",
    }


def test_repair_record_scales_193_base_and_sl10_stocks() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_476_score35_base")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "NaCl")["concentration"] == {
        "value": "6.979063",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "NaHCO3")["concentration"] == {
        "value": "4.985045",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "HCl")["concentration"] == {
        "value": "0.002493",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "FeCl2 x 4 H2O")["concentration"] == {
        "value": "0.001496",
        "unit": "G_PER_L",
    }


def test_repair_record_adds_selenite_tungstate_stock() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_476_score35_selenite")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "NaOH")["source"] == repair.SOURCE_385
    assert _ingredient(repaired, "NaOH")["term"] == {
        "id": "CHEBI:32145",
        "label": "sodium hydroxide",
    }
    assert _ingredient(repaired, "Na2SeO3 x 5 H2O")["term"] == {
        "id": "CHEBI:131361",
        "label": "disodium selenite pentahydrate",
    }
    assert _ingredient(repaired, "Na2SeO3 x 5 H2O")["concentration"] == {
        "value": "0.00000299",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2WO4 x 2 H2O")["term"] == {
        "id": "CHEBI:63939",
        "label": "sodium tungstate dihydrate",
    }
    assert _ingredient(repaired, "Na2WO4 x 2 H2O")["concentration"] == {
        "value": "0.00000399",
        "unit": "G_PER_L",
    }


def test_repair_record_merges_vitamins_from_141_and_351() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_476_score35_vitamins")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "Biotin")["concentration"] == {
        "value": "0.000120",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Thiamine-HCl x 2 H2O")["concentration"] == {
        "value": "0.000349",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Nicotinic acid amide")["term"] == {
        "id": "CHEBI:17154",
        "label": "nicotinamide",
    }
    assert _ingredient(repaired, "Pyridoxal hydrochloride")["term"] == {
        "id": "CHEBI:131529",
        "label": "pyridoxal hydrochloride",
    }
    assert _ingredient(repaired, "Ca-pantothenate")["concentration"] == {
        "value": "0.0000997",
        "unit": "G_PER_L",
    }


def test_repair_record_scores_as_complete_and_is_idempotent() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_476_score35_idempotent")
    scorer = _load_script(SCORER, "score_review_need_for_komodo_476")

    once = repair.repair_record(_minimal_doc())
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert twice["references"] == [
        {"reference": repair.KOMODO_476_URL},
        {"reference": repair.DSMZ_476_URL},
        {"reference": repair.DSMZ_193_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_141_URL},
        {"reference": repair.DSMZ_385_URL},
        {"reference": repair.DSMZ_351_URL},
    ]
    events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair.CURATOR
        and event.get("action") == repair.ACTION
    ]
    assert len(events) == 1


def test_repair_record_rejects_wrong_id() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_476_score35_wrong_id")
    doc = _minimal_doc()
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:005590"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_476_score35_wrong_source")
    doc = _minimal_doc()
    doc["media_term"]["term"]["id"] = "mediadive.medium:476"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:476"):
        repair.repair_record(doc)
