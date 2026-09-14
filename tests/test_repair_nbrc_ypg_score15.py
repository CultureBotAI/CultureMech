from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_ypg_score15.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_nbrc_ypg_score15", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return load_script()


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
    }


def _minimal_doc(repair_module) -> dict:
    return {
        "id": repair_module.TARGET_ID,
        "name": "ypg_medium",
        "original_name": repair_module.TITLE,
        "description": "YPG Medium. NBRC No. 802.",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "DISSOLVE",
                "description": "Dissolve ingredients in 1000 ml distilled water",
            },
            {
                "step_number": 2,
                "action": "ADJUST_PH",
                "description": "Adjust pH to 7.0",
            },
            {
                "step_number": 3,
                "action": "AUTOCLAVE",
                "description": "Autoclave at 121°C for 15 minutes",
            },
        ],
        "curation_history": [
            {
                "curator": "nbrc-import",
                "action": "Imported from NBRC",
                "notes": f"Source: {repair_module.LEGACY_NBRC_URL}",
            }
        ],
        "kg_microbe_match": "mediadive.medium:7",
    }


def test_repair_document_preserves_legacy_identity_without_media_term(
    repair_module,
) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert repaired["name"] == repair_module.TITLE
    assert repaired["original_name"] == repair_module.TITLE
    assert repaired["ph_value"] == 7.0
    assert "media_term" not in repaired
    assert "ph_range" not in repaired
    assert repaired["kg_microbe_match"] == "mediadive.medium:7"
    assert repaired["references"] == [{"reference": repair_module.LEGACY_NBRC_URL}]
    assert repaired["notes"] == repair_module.NOTES


def test_repair_document_grounds_source_components(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))
    ingredients = {row["preferred_term"]: row for row in repaired["ingredients"]}

    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    }
    assert "mediaingredientmech_chebi_term" not in ingredients["Yeast extract"]
    assert ingredients["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "peptone",
    }
    assert "mediaingredientmech_chebi_term" not in ingredients["Peptone"]
    assert ingredients["Glucose"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert ingredients["Agar"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
        "legacy_source_url_unavailable",
    ]


def test_repair_document_replaces_generic_preparation(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert "121 C" in repaired["preparation_steps"][2]["description"]


def test_repair_document_adds_reference_and_event_once(repair_module) -> None:
    once = repair_module.repair_document(_minimal_doc(repair_module))
    twice = repair_module.repair_document(once)

    assert twice["references"] == [{"reference": repair_module.LEGACY_NBRC_URL}]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == repair_module.LEGACY_NBRC_URL


def test_repair_document_rejects_wrong_id(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected 'CultureMech:007512'"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_missing_nbrc_import(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["curation_history"] = []

    with pytest.raises(ValueError, match="missing legacy NBRC 802 import event"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_name_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["original_name"] = "Different Medium"

    with pytest.raises(ValueError, match="NBRC YPG title drifted"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_ingredient_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["ingredients"][0] = _ingredient("Yeast extract", "6.0", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_document(doc)


def test_target_record_matches_nbrc_ypg_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    repaired = repair_module.repair_document(doc)

    assert doc["id"] == repair_module.TARGET_ID
    assert doc["original_name"] == repair_module.TITLE
    assert repair_module._signature(
        doc["ingredients"], "ingredients"
    ) == repair_module.IMPORTED_INGREDIENT_SIGNATURE
    assert repaired["ph_value"] == 7.0
