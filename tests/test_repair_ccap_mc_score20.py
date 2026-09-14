from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_ccap_mc_score20.py"


def _load_repair():
    spec = importlib.util.spec_from_file_location("repair_ccap_mc_score20", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["repair_ccap_mc_score20"] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _minimal_doc() -> dict:
    return {
        "id": "CultureMech:000086",
        "name": "mc",
        "category": "algae",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "references": [{"reference": "CCAP:MC"}],
        "ingredients": [
            {
                "preferred_term": "Na HPO .7H O",
                "concentration": {"value": "2.5", "unit": "G_PER_L"},
            },
            {
                "preferred_term": "KH PO",
                "term": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"},
                "concentration": {"value": "0.8", "unit": "G_PER_L"},
            },
            {
                "preferred_term": (
                    "Aseptically add the foetal calf serum to a final concentration of"
                ),
                "concentration": {"value": "10", "unit": "PERCENT_W_V"},
            },
        ],
        "data_quality_flags": [
            "has_ontology_mappings",
            "ingredients_curated",
            "curation_method:automated_expert_mapping",
        ],
        "curation_history": [],
    }


def test_repair_record_replaces_malformed_ccap_mc_ingredients() -> None:
    repair = _load_repair()

    repaired = repair.repair_record(_minimal_doc())

    assert repaired["notes"] == repair.NOTES
    assert repaired["ph_value"] == 6.9
    assert repaired["storage"] == {"temperature": {"value": 4.0, "unit": "CELSIUS"}}
    assert repaired["sterilization"] == {
        "method": "AUTOCLAVE",
        "pressure": 10.0,
        "duration": "15 minutes",
        "notes": "CCAP instructs pressure cooking at 10 psi for 15 minutes.",
    }
    assert [row["preferred_term"] for row in repaired["ingredients"]] == [
        "Deionized water",
        "Casein digest (Casitone, cat. no. 225930)",
        "Na2HPO4.7H2O",
        "KH2PO4",
        "Yeast extract (Oxoid LP0021)",
        "D-glucose",
        "Liver digest (Oxoid LP0027)",
        "Sterile foetal calf serum (Gamma-Irradiated, cat. no. 10109-155)",
    ]
    assert repaired["ingredients"][0]["concentration"] == {
        "value": "900",
        "unit": "ML_PER_L",
    }
    assert repaired["ingredients"][3]["term"] == {
        "id": "CHEBI:63036",
        "label": "potassium dihydrogen phosphate",
    }
    assert repaired["ingredients"][4]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert repaired["ingredients"][5]["term"] == {
        "id": "CHEBI:17634",
        "label": "D-glucose",
    }
    assert repaired["ingredients"][-1]["concentration"] == {
        "value": "100",
        "unit": "ML_PER_L",
    }
    assert repaired["preparation_steps"] == repair.PREPARATION_STEPS
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
    assert twice["references"] == [
        {"reference": "CCAP:MC"},
        {"reference": repair.SOURCE_URL},
    ]
    events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair.CURATOR and event.get("action") == repair.ACTION
    ]
    assert len(events) == 1
