from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_815_score15.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_nbrc_815_score15", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return load_script()


def _ingredient(name: str, value: str, unit: str, term_id: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "term": {"id": term_id, "label": name},
    }


def _minimal_doc(repair_module) -> dict:
    return {
        "id": repair_module.TARGET_ID,
        "name": "815",
        "original_name": "815",
        "description": "815. NBRC 814.",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient("Pancreatic digest of casein", "17.0", "G_PER_L", "MICRO:0000182"),
            _ingredient("Peptic digest of soybean meal", "3.0", "G_PER_L", "FOODON:03315720"),
            _ingredient("Glucose", "2.5", "G_PER_L", "CHEBI:17234"),
            _ingredient("Sodium chloride", "5.0", "G_PER_L", "CHEBI:26710"),
            _ingredient("Dipotassium phosphate", "2.5", "G_PER_L", "CHEBI:131527"),
            _ingredient("Agar", "15.0", "G_PER_L", "CHEBI:2509"),
        ],
        "curation_history": [{"action": repair_module.REQUIRED_ACTION}],
        "notes": "pH 7.0 - 7.2",
    }


def test_repair_document_adds_nbrc_identity_reference_and_ph_range(
    repair_module,
) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert repaired["name"] == repair_module.TITLE
    assert repaired["original_name"] == repair_module.TITLE
    assert repaired["media_term"] == {
        "preferred_term": "NBRC Medium 814",
        "term": {"id": "nbrc.medium:814", "label": "NBRC Medium 814"},
    }
    assert repaired["ph_range"] == repair_module.PH_RANGE
    assert "ph_value" not in repaired
    assert repaired["references"] == [{"reference": repair_module.NBRC_URL}]
    assert repaired["notes"] == repair_module.NOTES


def test_repair_document_preserves_expanded_composition(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))
    ingredients = {row["preferred_term"]: row for row in repaired["ingredients"]}

    assert (
        repair_module._signature(repaired["ingredients"], "ingredients")
        == repair_module.CURATED_INGREDIENT_SIGNATURE
    )
    assert ingredients["Pancreatic digest of casein"]["term"]["id"] == "MICRO:0000182"
    assert ingredients["Peptic digest of soybean meal"]["term"]["id"] == "FOODON:03315720"
    assert ingredients["Glucose"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert ingredients["Dipotassium phosphate"]["term"] == {
        "id": "CHEBI:131527",
        "label": "dipotassium hydrogen phosphate",
    }
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_document_adds_reference_and_event_once(repair_module) -> None:
    once = repair_module.repair_document(_minimal_doc(repair_module))
    twice = repair_module.repair_document(once)

    assert twice["references"] == [{"reference": repair_module.NBRC_URL}]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == repair_module.NBRC_URL


def test_repair_document_rejects_wrong_id(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected 'CultureMech:007495'"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_missing_recovery_decision(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["curation_history"] = []

    with pytest.raises(ValueError, match="missing recovery action"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_name_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["name"] = "NBRC Medium 815"

    with pytest.raises(ValueError, match="NBRC title/name drifted"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_ingredient_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["ingredients"][0] = _ingredient(
        "Pancreatic digest of casein", "16.0", "G_PER_L", "MICRO:0000182"
    )

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_document(doc)


def test_target_record_matches_nbrc_814_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    repaired = repair_module.repair_document(doc)

    assert doc["id"] == repair_module.TARGET_ID
    assert doc["name"] in {"815", repair_module.TITLE}
    assert repair_module._signature(doc["ingredients"], "ingredients") == (
        repair_module.CURATED_INGREDIENT_SIGNATURE
    )
    assert repaired["media_term"]["term"]["id"] == "nbrc.medium:814"
