from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_724_score35.py"
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
        "id": "CultureMech:006367",
        "name": "desulfomicrobium_whb_medium",
        "original_name": "DESULFOMICROBIUM WHB MEDIUM",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 724",
            "term": {
                "id": "komodo.medium:724",
                "label": "DESULFOMICROBIUM WHB MEDIUM",
            },
        },
        "notes": (
            "Source: KOMODO ModelSEED | ID: 724 | DSMZ Medium: 724 "
            "(mediadive.medium:724) | Aerobic: No"
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


def test_repair_record_adds_desulfomicrobium_whb_components() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_724_score35")

    repaired = repair.repair_record(_minimal_doc())

    assert repaired["notes"] == repair.NOTES
    assert repaired["ph_range"] == {"min": 7.1, "max": 7.4}
    assert len(repaired["ingredients"]) == 38
    assert repaired["ingredients"][0]["preferred_term"] == "Na2SO4"
    assert repaired["ingredients"][-1] == {
        "preferred_term": "Distilled water",
        "source": repair.SOURCE_193,
        "notes": (
            "Archived DSMZ Medium 193 lists 990 mL direct distilled water "
            "across solutions A, C, D, and F before stock additions and "
            "before Archived DSMZ Medium 724 supplies sodium lactate as the "
            "substrate."
        ),
        "concentration": {"value": "990.000", "unit": "ML_PER_L"},
        "term": {"id": "CHEBI:15377", "label": "water"},
        "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
    }


def test_repair_record_applies_195_overrides_and_724_substrate() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_724_score35_overrides")

    repaired = repair.repair_record(_minimal_doc())
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

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
    assert _ingredient(repaired, "Sodium lactate")["source"] == repair.SOURCE_724
    assert _ingredient(repaired, "Sodium lactate")["term"] == {
        "id": "CHEBI:75228",
        "label": "sodium lactate",
    }
    assert _ingredient(repaired, "Sodium lactate")["concentration"] == {
        "value": "4.000000",
        "unit": "G_PER_L",
    }


def test_repair_record_scales_193_base_and_sl10_stocks() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_724_score35_base")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "KCl")["concentration"] == {
        "value": "0.498504",
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
    repair = _load_script(SCRIPT, "repair_komodo_724_score35_selenite")

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


def test_repair_record_merges_vitamins_from_141_and_503() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_724_score35_vitamins")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "Biotin")["source"] == repair.SOURCE_141
    assert _ingredient(repaired, "Biotin")["concentration"] == {
        "value": "0.0000199",
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
        "value": "0.000249",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Vitamin B12")["concentration"] == {
        "value": "0.000101",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Calcium pantothenate")["concentration"] == {
        "value": "0.0000997",
        "unit": "G_PER_L",
    }


def test_repair_record_scores_as_complete_and_is_idempotent() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_724_score35_idempotent")
    scorer = _load_script(SCORER, "score_review_need_for_komodo_724")

    once = repair.repair_record(_minimal_doc())
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert twice["references"] == [
        {"reference": repair.KOMODO_724_URL},
        {"reference": repair.DSMZ_724_URL},
        {"reference": repair.DSMZ_195_URL},
        {"reference": repair.DSMZ_193_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_141_URL},
        {"reference": repair.DSMZ_385_URL},
        {"reference": repair.DSMZ_503_URL},
    ]
    events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair.CURATOR
        and event.get("action") == repair.ACTION
    ]
    assert len(events) == 1


def test_repair_record_rejects_wrong_id() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_724_score35_wrong_id")
    doc = _minimal_doc()
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:006367"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_724_score35_wrong_source")
    doc = _minimal_doc()
    doc["media_term"]["term"]["id"] = "mediadive.medium:724"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:724"):
        repair.repair_record(doc)
