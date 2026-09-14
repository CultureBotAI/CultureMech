from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_1481_bbm_score20.py"


def _load_repair():
    spec = importlib.util.spec_from_file_location("repair_jcm_1481_bbm_score20", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["repair_jcm_1481_bbm_score20"] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _minimal_doc() -> dict:
    return {
        "id": "CultureMech:015878",
        "id_lineage_token": "legacy:3f3c608ec49092c7f74774bb653ad791d1cd571799ba35dc9473f24b46758545",
        "name": "bold_s_basal_medium_bbm",
        "original_name": "Bold's Basal Medium (BBM)",
        "category": "algae",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": "JCM Medium J1481",
            "term": {"id": "jcm.grmd:1481", "label": "Bold's Basal Medium (BBM)"},
        },
        "notes": ("Source: JCM | Link: " "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1481"),
        "ingredients": [
            {
                "preferred_term": "Agar",
                "concentration": {"value": "20", "unit": "G_PER_L"},
                "term": {"id": "CHEBI:2509", "label": "agar"},
                "mediaingredientmech_chebi_term": {"id": "CHEBI:2509", "label": "agar"},
            },
            {
                "preferred_term": "Distilled water",
                "concentration": {"value": "980", "unit": "ML_PER_L"},
                "term": {"id": "CHEBI:15377", "label": "water"},
                "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
            },
        ],
        "curation_history": [],
    }


def test_repair_record_adds_omitted_bbm_stock_and_preparation_steps() -> None:
    repair = _load_repair()

    repaired = repair.repair_record(_minimal_doc())

    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "UNDEFINED"
    assert repaired["notes"] == repair.NOTES
    assert repaired["ingredients"] == [
        {
            "preferred_term": "Agar",
            "concentration": {"value": "20", "unit": "G_PER_L"},
            "source": "JCM Medium 1481",
            "term": {"id": "CHEBI:2509", "label": "agar"},
            "mediaingredientmech_chebi_term": {"id": "CHEBI:2509", "label": "agar"},
            "notes": "JCM Medium 1481 lists 20 g agar per liter.",
        },
        {
            "preferred_term": "Distilled water",
            "concentration": {"value": "980", "unit": "ML_PER_L"},
            "source": "JCM Medium 1481",
            "term": {"id": "CHEBI:15377", "label": "water"},
            "mediaingredientmech_chebi_term": {"id": "CHEBI:15377", "label": "water"},
            "notes": "JCM Medium 1481 lists 980 ml distilled water per liter.",
        },
        {
            "preferred_term": (
                "Sigma-Aldrich Bold Modified Basal Freshwater Nutrient Solution, 50x"
            ),
            "concentration": {"value": "20", "unit": "ML_PER_L"},
            "source": "JCM Medium 1481",
            "notes": (
                "JCM Medium 1481 says to add 20 ml of this 50x commercial BBM "
                "stock after autoclaving."
            ),
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
