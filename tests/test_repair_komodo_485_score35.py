from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_485_score35.py"
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
        "id": "CultureMech:005608",
        "name": "metallosphaera_medium",
        "original_name": "METALLOSPHAERA medium",
        "category": "archaea",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 485",
            "term": {"id": "komodo.medium:485", "label": "METALLOSPHAERA medium"},
        },
        "notes": (
            "Source: KOMODO ModelSEED | ID: 485 | DSMZ Medium: 485 "
            "(mediadive.medium:485) | Aerobic: No"
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


def test_repair_record_adds_komodo_metallosphaera_components() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_485_score35")

    repaired = repair.repair_record(_minimal_doc())

    assert repaired["notes"] == repair.NOTES
    assert [row["preferred_term"] for row in repaired["ingredients"]] == [
        "KH2PO4",
        "VOSO4 x 2 H2O",
        "sulfitic ore (e.g. pyrite)",
        "CaCl2 x 2 H2O",
        "Yeast extract",
        "MnCl2 x 4 H2O",
        "CuCl2 x 2 H2O",
        "(NH4)2SO4",
        "Na2MoO4 x 2 H2O",
        "FeCl3 x 6 H2O",
        "MgSO4 x 7 H2O",
        "H2O",
        "ZnSO4 x 7 H2O",
        "Na2B4O7 x 10 H2O",
        "CoSO4",
        "H2SO4",
    ]
    assert _ingredient(repaired, "sulfitic ore (e.g. pyrite)")["concentration"] == {
        "value": "20.00",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "H2O")["term"] == {"id": "CHEBI:15377", "label": "water"}
    assert "concentration" not in _ingredient(repaired, "H2O")
    assert _ingredient(repaired, "H2SO4")["term"] == {
        "id": "CHEBI:26836",
        "label": "sulfuric acid",
    }
    assert "concentration" not in _ingredient(repaired, "H2SO4")
    assert _ingredient(repaired, "Yeast extract")["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }


def test_repair_record_grounds_explicit_hydrates() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_485_score35_hydrates")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "VOSO4 x 2 H2O")["term"] == {
        "id": "CHEBI:87009",
        "label": "vanadyl sulfate dihydrate",
    }
    assert _ingredient(repaired, "MnCl2 x 4 H2O")["term"] == {
        "id": "CHEBI:86368",
        "label": "manganese(II) chloride tetrahydrate",
    }
    assert _ingredient(repaired, "CuCl2 x 2 H2O")["term"] == {
        "id": "CHEBI:86318",
        "label": "copper(II) chloride dihydrate",
    }
    assert _ingredient(repaired, "CoSO4")["term"] == {
        "id": "CHEBI:53470",
        "label": "cobalt(2+) sulfate",
    }


def test_repair_record_scores_as_complete_and_is_idempotent() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_485_score35_idempotent")
    scorer = _load_script(SCORER, "score_review_need_for_komodo_485")

    once = repair.repair_record(_minimal_doc())
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (5, ["no pH and no temperature"])
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
        "has_unmapped_ingredients",
    ]
    assert twice["references"] == [{"reference": repair.SOURCE_URL}]
    events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair.CURATOR and event.get("action") == repair.ACTION
    ]
    assert len(events) == 1


def test_repair_record_rejects_wrong_id() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_485_score35_wrong_id")
    doc = _minimal_doc()
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:005608"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_485_score35_wrong_source")
    doc = _minimal_doc()
    doc["media_term"]["term"]["id"] = "mediadive.medium:485"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:485"):
        repair.repair_record(doc)
