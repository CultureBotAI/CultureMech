from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_892_score15.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_nbrc_892_score15", SCRIPT)
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
        "name": "892",
        "original_name": "892",
        "description": "892. NBRC 891.",
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
                "description": "Dissolve ingredients in distilled water",
            },
            {
                "step_number": 2,
                "action": "ADJUST_PH",
                "description": "Adjust pH if needed",
            },
            {
                "step_number": 3,
                "action": "DISSOLVE",
                "description": "Sterilize by autoclaving",
            },
        ],
        "curation_history": [{"action": repair_module.REQUIRED_ACTION}],
        "notes": "pH 7.1-7.5",
    }


def test_repair_document_adds_nbrc_identity_reference_and_ph_range(
    repair_module,
) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert repaired["name"] == repair_module.TITLE
    assert repaired["original_name"] == repair_module.TITLE
    assert repaired["media_term"] == {
        "preferred_term": "NBRC Medium 891",
        "term": {"id": "nbrc.medium:891", "label": "NBRC Medium 891"},
    }
    assert repaired["ph_range"] == repair_module.PH_RANGE
    assert repaired["references"] == [{"reference": repair_module.NBRC_URL}]
    assert repaired["notes"] == repair_module.NOTES


def test_repair_document_grounds_source_components(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))
    ingredients = {row["preferred_term"]: row for row in repaired["ingredients"]}

    assert repair_module._signature(
        repaired["ingredients"], "ingredients"
    ) == repair_module.IMPORTED_INGREDIENT_SIGNATURE
    assert ingredients["Casein peptone"]["term"] == {
        "id": "FOODON:03315719",
        "label": "Casein peptone",
    }
    assert ingredients["Soybean peptone"]["term"] == {
        "id": "FOODON:03315720",
        "label": "Soy peptone",
    }
    assert "mediaingredientmech_term" not in ingredients["Casein peptone"]
    assert "mediaingredientmech_term" not in ingredients["Soybean peptone"]
    assert ingredients["NaCl"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:26710",
        "label": "sodium chloride",
    }
    assert ingredients["Agar"]["term"]["id"] == "CHEBI:2509"
    assert ingredients["Distilled water"]["term"]["id"] == "CHEBI:15377"
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_document_replaces_generic_preparation(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["sterilization"] = {"method": "AUTOCLAVE"}

    repaired = repair_module.repair_document(doc)

    assert "sterilization" not in repaired
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert "autoclaving" not in str(repaired["preparation_steps"])


def test_repair_document_adds_reference_and_event_once(repair_module) -> None:
    once = repair_module.repair_document(_minimal_doc(repair_module))
    twice = repair_module.repair_document(once)

    assert twice["references"] == [{"reference": repair_module.NBRC_URL}]
    assert repair_module._signature(
        twice["ingredients"], "ingredients"
    ) == repair_module.IMPORTED_INGREDIENT_SIGNATURE
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

    with pytest.raises(ValueError, match="expected 'CultureMech:007502'"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_missing_recovery_decision(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["curation_history"] = []

    with pytest.raises(ValueError, match="missing recovery action"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_name_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["name"] = "NBRC Medium 892"

    with pytest.raises(ValueError, match="NBRC title/name drifted"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_ingredient_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["ingredients"][0] = _ingredient("Casein peptone", "14", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_document(doc)


def test_target_record_matches_nbrc_891_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    repaired = repair_module.repair_document(doc)

    assert doc["id"] == repair_module.TARGET_ID
    assert doc["name"] in {"892", repair_module.TITLE}
    assert repair_module._signature(
        doc["ingredients"], "ingredients"
    ) == repair_module.IMPORTED_INGREDIENT_SIGNATURE
    assert repaired["media_term"]["term"]["id"] == "nbrc.medium:891"
