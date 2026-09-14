from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2583_score25.py"


def _load_repair():
    spec = importlib.util.spec_from_file_location("repair_togo_m2583_score25", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["repair_togo_m2583_score25"] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _minimal_doc() -> dict:
    return {
        "id": "CultureMech:009151",
        "name": "mueller_hinton_medium_with_10_rabbit_serum",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            {
                "preferred_term": "DI Water",
                "concentration": {"value": "900", "unit": "G_PER_L"},
            },
            {
                "preferred_term": "Mueller Hinton Broth (BD 211443)",
                "concentration": {"value": "22", "unit": "G_PER_L"},
            },
            {
                "preferred_term": "Rabbit serum",
                "concentration": {"value": "100", "unit": "G_PER_L"},
            },
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2583",
            "term": {
                "id": "TOGO:M2583",
                "label": "Mueller Hinton Medium with 10% Rabbit Serum",
            },
        },
        "notes": "Source: https://togomedium.org/medium/M2583",
        "curation_history": [],
    }


def test_repair_record_corrects_units_groundings_and_preparation_steps() -> None:
    repair = _load_repair()

    repaired = repair.repair_record(_minimal_doc())

    assert repaired["notes"] == repair.NOTES
    assert repaired["ingredients"] == [
        {
            "preferred_term": "DI Water",
            "concentration": {"value": "900", "unit": "ML_PER_L"},
            "source": "TOGO M2583",
            "term": {"id": "CHEBI:15377", "label": "water"},
            "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
            "notes": "TOGO M2583 lists 900 ml DI Water.",
        },
        {
            "preferred_term": "Mueller Hinton Broth (BD 211443)",
            "concentration": {"value": "22", "unit": "G_PER_L"},
            "source": "TOGO M2583",
            "notes": (
                "TOGO M2583 lists 22 g Mueller Hinton Broth from BD catalog 211443 "
                "without disclosing the broth composition."
            ),
        },
        {
            "preferred_term": "Rabbit serum",
            "concentration": {"value": "100", "unit": "ML_PER_L"},
            "source": "TOGO M2583",
            "notes": "TOGO M2583 says to aseptically add 100 ml of sterile rabbit serum.",
        },
    ]
    assert repaired["preparation_steps"] == repair.PREPARATION_STEPS
    assert repaired["sterilization"] == {"method": "AUTOCLAVE"}
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
        "has_unmapped_ingredients",
    ]


def test_repair_record_adds_reference_and_is_idempotent() -> None:
    repair = _load_repair()

    once = repair.repair_record(_minimal_doc())
    twice = repair.repair_record(once)

    assert once == twice
    assert twice["references"] == [{"reference": repair.SOURCE_URL}]
    events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair.CURATOR and event.get("action") == repair.ACTION
    ]
    assert len(events) == 1
