from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_279_score35.py"
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
        "id": "CultureMech:004706",
        "name": "methanocorpusculum_medium",
        "original_name": "METHANOCORPUSCULUM medium",
        "category": "archaea",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 279",
            "term": {"id": "komodo.medium:279", "label": "METHANOCORPUSCULUM medium"},
        },
        "notes": (
            "Source: KOMODO ModelSEED | ID: 279 | DSMZ Medium: 279 "
            "(mediadive.medium:279) | Aerobic: No"
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


def test_repair_record_adds_komodo_methanocorpusculum_components() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_279_score35")

    repaired = repair.repair_record(_minimal_doc())

    assert repaired["notes"] == repair.NOTES
    assert [row["preferred_term"] for row in repaired["ingredients"]] == [
        "KH2PO4",
        "CoCl2 x 6 H2O",
        "HCl",
        "CaCl2 x 2 H2O",
        "Na2S x 9 H2O",
        "ZnCl2",
        "2-Methylbutyric acid",
        "NH4Cl",
        "CO2",
        "CuCl2 x 2 H2O",
        "Na2MoO4 x 2 H2O",
        "H3BO3",
        "NiCl2 x 6 H2O",
        "Isovaleric acid",
        "Isobutyric acid",
        "MgSO4 x 7 H2O",
        "H2O",
        "Cysteine-HCl x H2O",
        "Resazurin",
        "Na-formate",
        "NaHCO3",
        "Yeast extract",
        "MnCl2 x 4 H2O",
        "Na-acetate",
        "Valeric acid",
        "FeSO4 x 7 H2O",
        "H2",
        "Distilled water",
        "FeCl2 x 4 H2O",
        "NaCl",
        "NaOH",
        "sludge from an anaerobic digester",
    ]
    assert _ingredient(repaired, "sludge from an anaerobic digester")["concentration"] == {
        "value": "49.46",
        "unit": "G_PER_L",
    }
    assert "term" not in _ingredient(repaired, "sludge from an anaerobic digester")


def test_repair_record_preserves_null_amount_components_without_concentrations() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_279_score35_nulls")

    repaired = repair.repair_record(_minimal_doc())

    for preferred_term in ("CO2", "H2O", "H2", "Distilled water", "NaOH"):
        assert "concentration" not in _ingredient(repaired, preferred_term)
    assert _ingredient(repaired, "CO2")["term"] == {"id": "CHEBI:16526", "label": "carbon dioxide"}
    assert _ingredient(repaired, "H2O")["term"] == {"id": "CHEBI:15377", "label": "water"}
    assert _ingredient(repaired, "H2")["term"] == {"id": "CHEBI:18276", "label": "dihydrogen"}
    assert _ingredient(repaired, "Distilled water")["term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert _ingredient(repaired, "NaOH")["term"] == {
        "id": "CHEBI:32145",
        "label": "sodium hydroxide",
    }


def test_repair_record_grounds_explicit_hydrates_and_volatile_acids() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_279_score35_hydrates")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "CoCl2 x 6 H2O")["term"] == {
        "id": "CHEBI:53503",
        "label": "cobalt chloride hexahydrate",
    }
    assert _ingredient(repaired, "NiCl2 x 6 H2O")["term"] == {
        "id": "CHEBI:53542",
        "label": "nickel chloride hexahydrate",
    }
    assert _ingredient(repaired, "FeCl2 x 4 H2O")["term"] == {
        "id": "CHEBI:86249",
        "label": "iron dichloride tetrahydrate",
    }
    assert _ingredient(repaired, "Cysteine-HCl x H2O")["term"] == {
        "id": "CHEBI:91248",
        "label": "L-cysteine hydrochloride hydrate",
    }
    assert _ingredient(repaired, "2-Methylbutyric acid")["term"] == {
        "id": "CHEBI:37070",
        "label": "2-methylbutyric acid",
    }
    assert _ingredient(repaired, "Isovaleric acid")["term"] == {
        "id": "CHEBI:28484",
        "label": "isovaleric acid",
    }
    assert _ingredient(repaired, "Isobutyric acid")["term"] == {
        "id": "CHEBI:16135",
        "label": "isobutyric acid",
    }
    assert _ingredient(repaired, "Valeric acid")["term"] == {
        "id": "CHEBI:17418",
        "label": "valeric acid",
    }


def test_repair_record_scores_as_complete_and_is_idempotent() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_279_score35_idempotent")
    scorer = _load_script(SCORER, "score_review_need_for_komodo_279")

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
    repair = _load_script(SCRIPT, "repair_komodo_279_score35_wrong_id")
    doc = _minimal_doc()
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:004706"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_279_score35_wrong_source")
    doc = _minimal_doc()
    doc["media_term"]["term"]["id"] = "mediadive.medium:279"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:279"):
        repair.repair_record(doc)
