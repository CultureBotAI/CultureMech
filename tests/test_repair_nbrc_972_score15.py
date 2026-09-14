from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_972_score15.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_nbrc_972_score15", SCRIPT)
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


def _minimal_solution(name: str, signature: tuple) -> dict:
    return {
        "preferred_term": name,
        "composition": [
            _ingredient(ingredient, value, unit)
            for ingredient, value, unit in signature
        ],
    }


def _minimal_doc(repair_module) -> dict:
    return {
        "id": repair_module.TARGET_ID,
        "name": "972",
        "original_name": "972",
        "description": "972. NBRC 971.",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "curation_history": [{"action": repair_module.REQUIRED_ACTION}],
        "solutions": [
            _minimal_solution("Solution A.", repair_module.SOLUTION_SIGNATURES[0][1]),
            _minimal_solution("Solution B.", repair_module.SOLUTION_SIGNATURES[1][1]),
        ],
    }


def test_repair_document_adds_nbrc_identity_and_reference(
    repair_module,
) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert repaired["name"] == repair_module.TITLE
    assert repaired["original_name"] == repair_module.TITLE
    assert repaired["media_term"] == {
        "preferred_term": "NBRC Medium 971",
        "term": {"id": "nbrc.medium:971", "label": "NBRC Medium 971"},
    }
    assert "ph_value" not in repaired
    assert "ph_range" not in repaired
    assert repaired["references"] == [{"reference": repair_module.NBRC_URL}]
    assert repaired["notes"] == repair_module.NOTES


def test_repair_document_grounds_defined_components(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))
    ingredients = {row["preferred_term"]: row for row in repaired["ingredients"]}
    solution_a = {
        row["preferred_term"]: row for row in repaired["solutions"][0]["composition"]
    }
    solution_b = {
        row["preferred_term"]: row for row in repaired["solutions"][1]["composition"]
    }

    assert ingredients["MgSO4·7H2O"]["term"] == {
        "id": "CHEBI:31795",
        "label": "magnesium sulfate heptahydrate",
    }
    assert ingredients["Agar (if needed)"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert solution_a["CaCl2"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:3312",
        "label": "calcium dichloride",
    }
    assert solution_a["Ferric ammonium citrate"]["term"]["id"] == "CHEBI:31604"
    assert solution_b["Sucrose"]["term"]["id"] == "CHEBI:17992"
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_document_adds_source_preparation_without_ph_adjustment(
    repair_module,
) -> None:
    doc = _minimal_doc(repair_module)
    doc["sterilization"] = {"method": "AUTOCLAVE"}

    repaired = repair_module.repair_document(doc)

    assert "sterilization" not in repaired
    assert "ph_value" not in repaired
    assert "ph_range" not in repaired
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert "pH unadjusted" in repaired["preparation_steps"][0]["description"]


def test_repair_document_adds_reference_and_event_once(repair_module) -> None:
    once = repair_module.repair_document(_minimal_doc(repair_module))
    twice = repair_module.repair_document(once)

    assert twice["references"] == [{"reference": repair_module.NBRC_URL}]
    assert repair_module._solution_signatures(twice) == (
        repair_module.SOLUTION_SIGNATURES
    )
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

    with pytest.raises(ValueError, match="expected 'CultureMech:007509'"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_missing_recovery_decision(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["curation_history"] = []

    with pytest.raises(ValueError, match="missing recovery action"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_name_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["name"] = "NBRC Medium 972"

    with pytest.raises(ValueError, match="NBRC title/name drifted"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_ingredient_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["ingredients"][0] = _ingredient("KH2PO4", "4.5", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_solution_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["solutions"][0]["composition"][1] = _ingredient(
        "CaCl2",
        "0.4",
        "G_PER_L",
    )

    with pytest.raises(ValueError, match="nested solution signature drifted"):
        repair_module.repair_document(doc)


def test_target_record_matches_nbrc_971_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    repaired = repair_module.repair_document(doc)

    assert doc["id"] == repair_module.TARGET_ID
    assert doc["name"] in {"972", repair_module.TITLE}
    assert repair_module._signature(
        doc["ingredients"], "ingredients"
    ) == repair_module.IMPORTED_INGREDIENT_SIGNATURE
    assert repair_module._solution_signatures(doc) == repair_module.SOLUTION_SIGNATURES
    assert repaired["media_term"]["term"]["id"] == "nbrc.medium:971"
