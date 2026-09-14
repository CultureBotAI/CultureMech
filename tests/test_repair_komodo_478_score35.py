from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_478_score35.py"
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
        "id": "CultureMech:005592",
        "name": "acetobacterium_sp_komac1_medium",
        "original_name": "ACETOBACTERIUM SP. KoMAc1 medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 478",
            "term": {
                "id": "komodo.medium:478",
                "label": "ACETOBACTERIUM SP. KoMAc1 medium",
            },
        },
        "notes": (
            "Source: KOMODO ModelSEED | ID: 478 | DSMZ Medium: 478 "
            "(mediadive.medium:478) | Aerobic: No"
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


def test_repair_record_adds_komac1_components() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_478_score35")

    repaired = repair.repair_record(_minimal_doc())

    assert repaired["notes"] == repair.NOTES
    assert repaired["ph_range"] == {"min": 7.1, "max": 7.4}
    assert len(repaired["ingredients"]) == 32
    assert repaired["ingredients"][0]["preferred_term"] == "Na2SO4"
    assert repaired["ingredients"][-1] == {
        "preferred_term": "Distilled water",
        "source": repair.SOURCE_193,
        "notes": "Archived DSMZ Medium 193 lists 870 mL distilled water for Solution A.",
        "concentration": {"value": "870.000", "unit": "ML_PER_L"},
        "term": {"id": "CHEBI:15377", "label": "water"},
        "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
    }


def test_repair_record_applies_194_and_478_substitutions() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_478_score35_substitutions")

    repaired = repair.repair_record(_minimal_doc())
    names = {ingredient["preferred_term"] for ingredient in repaired["ingredients"]}

    assert "Na-acetate x 3 H2O" not in names
    assert "Na-propionate" not in names
    assert _ingredient(repaired, "NaCl")["concentration"] == {
        "value": "1.000000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "MgCl2 x 6 H2O")["concentration"] == {
        "value": "0.400000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Methoxyacetate")["source"] == repair.SOURCE_478
    assert _ingredient(repaired, "Methoxyacetate")["concentration"] == {
        "value": "0.900000",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Yeast extract")["concentration"] == {
        "value": "0.500000",
        "unit": "G_PER_L",
    }


def test_repair_record_scales_trace_and_vitamin_stocks() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_478_score35_stocks")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "CoCl2 x 6 H2O")["concentration"] == {
        "value": "0.000190",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2MoO4 x 2 H2O")["concentration"] == {
        "value": "0.0000360",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Vitamin B12")["concentration"] == {
        "value": "0.000000999",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "D-Ca-pantothenate")["concentration"] == {
        "value": "0.0000500",
        "unit": "G_PER_L",
    }


def test_repair_record_grounds_methoxyacetate_and_hydrates() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_478_score35_terms")

    repaired = repair.repair_record(_minimal_doc())

    assert _ingredient(repaired, "Methoxyacetate")["term"] == {
        "id": "CHEBI:132097",
        "label": "methoxyacetate",
    }
    assert _ingredient(repaired, "MgCl2 x 6 H2O")["term"] == {
        "id": "CHEBI:86345",
        "label": "magnesium dichloride hexahydrate",
    }
    assert _ingredient(repaired, "FeCl2 x 4 H2O")["term"] == {
        "id": "CHEBI:86249",
        "label": "iron dichloride tetrahydrate",
    }
    assert _ingredient(repaired, "CuCl2 x 2 H2O")["term"] == {
        "id": "CHEBI:86318",
        "label": "copper(II) chloride dihydrate",
    }


def test_repair_record_scores_as_complete_and_is_idempotent() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_478_score35_idempotent")
    scorer = _load_script(SCORER, "score_review_need_for_komodo_478")

    once = repair.repair_record(_minimal_doc())
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert twice["references"] == [
        {"reference": repair.KOMODO_478_URL},
        {"reference": repair.DSMZ_478_URL},
        {"reference": repair.DSMZ_194_URL},
        {"reference": repair.DSMZ_193_URL},
        {"reference": repair.DSMZ_320_URL},
        {"reference": repair.DSMZ_141_URL},
    ]
    events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair.CURATOR
        and event.get("action") == repair.ACTION
    ]
    assert len(events) == 1


def test_repair_record_rejects_wrong_id() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_478_score35_wrong_id")
    doc = _minimal_doc()
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:005592"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source() -> None:
    repair = _load_script(SCRIPT, "repair_komodo_478_score35_wrong_source")
    doc = _minimal_doc()
    doc["media_term"]["term"]["id"] = "mediadive.medium:478"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:478"):
        repair.repair_record(doc)
