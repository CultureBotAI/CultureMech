from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_1298_score15.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_nbrc_1298_score15", SCRIPT)
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
        "name": "1298",
        "original_name": "1298",
        "description": "1298. NBRC 1296.",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "curation_history": [{"action": repair_module.REQUIRED_ACTION}],
    }


def test_repair_document_adds_nbrc_identity_ph_and_reference(
    repair_module,
) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert repaired["name"] == repair_module.TITLE
    assert repaired["original_name"] == repair_module.TITLE
    assert repaired["ph_value"] == 7.0
    assert repaired["media_term"] == {
        "preferred_term": "NBRC Medium 1296",
        "term": {"id": "nbrc.medium:1296", "label": "NBRC Medium 1296"},
    }
    assert repaired["references"] == [{"reference": repair_module.NBRC_URL}]
    assert repaired["notes"] == repair_module.NOTES


def test_repair_document_replaces_macconkey_with_source_formula(
    repair_module,
) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))
    ingredients = {row["preferred_term"]: row for row in repaired["ingredients"]}

    assert (
        repair_module._signature(repaired["ingredients"], "ingredients")
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert "Peptone" not in ingredients
    assert "Nutrient Broth Powder (Kyokuto*)" in ingredients
    assert "term" not in ingredients["Nutrient Broth Powder (Kyokuto*)"]
    assert ingredients["Pyruvic acid sodium salt"]["term"]["id"] == "CHEBI:50144"
    assert ingredients["Distilled water"]["term"]["id"] == "CHEBI:15377"
    assert ingredients["Agar (if needed)"]["term"]["id"] == "CHEBI:2509"
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
        "has_unmapped_ingredients",
    ]


def test_repair_document_adds_source_preparation(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert repaired["preparation_steps"][1]["description"] == "Adjust pH to 7.0."


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

    with pytest.raises(ValueError, match="expected 'CultureMech:007470'"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_missing_recovery_decision(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["curation_history"] = []

    with pytest.raises(ValueError, match="missing recovery action"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_name_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["name"] = "NBRC Medium 1298"

    with pytest.raises(ValueError, match="NBRC title/name drifted"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_ingredient_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["ingredients"][0] = _ingredient("Peptone", "18.0", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_document(doc)


def test_target_record_matches_nbrc_1296_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    repaired = repair_module.repair_document(doc)

    assert doc["id"] == repair_module.TARGET_ID
    assert doc["name"] in {"1298", repair_module.TITLE}
    assert repair_module._signature(doc["ingredients"], "ingredients") in {
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    }
    assert repaired["media_term"]["term"]["id"] == "nbrc.medium:1296"
