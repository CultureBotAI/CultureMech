from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2696_score25.py"


def _load_repair():
    spec = importlib.util.spec_from_file_location("repair_togo_m2696_score25", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["repair_togo_m2696_score25"] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _minimal_doc() -> dict:
    return {
        "id": "CultureMech:009248",
        "name": "togo_medium_m2696",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            {
                "preferred_term": "Yeast extract (Difco)",
                "concentration": {"value": "0.2", "unit": "PERCENT_W_V"},
            },
            {
                "preferred_term": "Trypticase (BBL)",
                "concentration": {"value": "1", "unit": "PERCENT_W_V"},
            },
            {
                "preferred_term": "Antifoam (Union Carbide Corp., SAG-471)",
                "concentration": {"value": "variable", "unit": "VARIABLE"},
            },
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2696",
            "term": {"id": "TOGO:M2696", "label": "TOGO Medium M2696"},
        },
        "notes": "Source: https://togomedium.org/medium/M2696",
        "curation_history": [],
    }


def test_repair_record_adds_source_notes_groundings_and_flags() -> None:
    repair = _load_repair()

    repaired = repair.repair_record(_minimal_doc())

    assert repaired["notes"] == repair.NOTES
    assert repaired["ingredients"] == [
        {
            "preferred_term": "Yeast extract (Difco)",
            "concentration": {"value": "0.2", "unit": "PERCENT_W_V"},
            "source": "TOGO M2696",
            "term": {"id": "FOODON:03315426", "label": "Yeast extract"},
            "notes": "TOGO M2696 lists 0.2% Yeast extract from Difco.",
        },
        {
            "preferred_term": "Trypticase (BBL)",
            "concentration": {"value": "1", "unit": "PERCENT_W_V"},
            "source": "TOGO M2696",
            "term": {"id": "MICRO:0000175", "label": "Trypticase peptone"},
            "notes": "TOGO M2696 lists 1% Trypticase from BBL.",
        },
        {
            "preferred_term": "Antifoam (Union Carbide Corp., SAG-471)",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": "TOGO M2696",
            "notes": (
                "TOGO M2696 lists Union Carbide SAG-471 antifoam without stating "
                "an amount."
            ),
        },
    ]
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
