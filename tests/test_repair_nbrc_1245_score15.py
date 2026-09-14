from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_1245_score15.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_nbrc_1245_score15", SCRIPT)
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
    ingredients = [
        _ingredient(name, value, unit)
        for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
    ]
    ingredients[0]["term"] = {"id": "UBERON:0000955", "label": "brain"}
    ingredients[1]["term"] = {"id": "UBERON:0000948", "label": "heart"}
    ingredients[2]["term"] = {"id": "MICRO:0000180", "label": "proteose peptone"}

    return {
        "id": repair_module.TARGET_ID,
        "name": "1245",
        "original_name": "1245",
        "description": "1245. NBRC 1243.",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": ingredients,
        "curation_history": [{"action": repair_module.REQUIRED_ACTION}],
    }


def test_repair_document_adds_nbrc_identity_and_reference(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert repaired["name"] == repair_module.TITLE
    assert repaired["original_name"] == repair_module.TITLE
    assert "ph_value" not in repaired
    assert repaired["media_term"] == {
        "preferred_term": "NBRC Medium 1243",
        "term": {"id": "nbrc.medium:1243", "label": "NBRC Medium 1243"},
    }
    assert repaired["references"] == [{"reference": repair_module.NBRC_URL}]
    assert repaired["notes"] == repair_module.NOTES


def test_repair_document_keeps_bhi_expansion_and_adds_nbrc_rows(
    repair_module,
) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))
    ingredients = {row["preferred_term"]: row for row in repaired["ingredients"]}

    assert (
        repair_module._signature(repaired["ingredients"], "ingredients")
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert ingredients["Calf brains"]["term"]["id"] == "UBERON:0000955"
    assert ingredients["Dextrose"]["term"]["id"] == "CHEBI:17634"
    assert ingredients["Dextrose"]["mediaingredientmech_chebi_term"]["id"] == "CHEBI:17634"
    assert ingredients["NaCl"]["concentration"] == {
        "value": "20",
        "unit": "G_PER_L",
    }
    assert ingredients["NaCl"]["term"]["id"] == "CHEBI:26710"
    assert ingredients["Distilled water"]["term"]["id"] == "CHEBI:15377"
    assert ingredients["Agar (if needed)"]["term"]["id"] == "CHEBI:2509"
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_document_adds_source_preparation(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert repaired["sterilization"] == {"method": "AUTOCLAVE"}
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert repaired["preparation_steps"][0]["description"] == (
        "Dissolve 37 g Bacto Brain Heart Infusion and 20 g NaCl in 1 L "
        "distilled water; add 15 g agar if solid medium is needed."
    )


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

    with pytest.raises(ValueError, match="expected 'CultureMech:007466'"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_missing_recovery_decision(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["curation_history"] = []

    with pytest.raises(ValueError, match="missing recovery action"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_name_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["name"] = "NBRC Medium 1245"

    with pytest.raises(ValueError, match="NBRC title/name drifted"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_ingredient_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["ingredients"][0] = _ingredient("Calf brains", "1", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_document(doc)


def test_target_record_matches_nbrc_1243_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    repaired = repair_module.repair_document(doc)

    assert doc["id"] == repair_module.TARGET_ID
    assert doc["name"] in {"1245", repair_module.TITLE}
    assert repair_module._signature(doc["ingredients"], "ingredients") in {
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    }
    assert repaired["media_term"]["term"]["id"] == "nbrc.medium:1243"
