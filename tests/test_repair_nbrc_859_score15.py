from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_859_score15.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_nbrc_859_score15", SCRIPT)
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
        "name": "859",
        "original_name": "859",
        "description": "859. NBRC 857.",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "curation_history": [{"action": repair_module.REQUIRED_ACTION}],
        "solutions": [
            _minimal_solution(
                "KP buffer",
                repair_module.KP_BUFFER_SIGNATURE,
            ),
            _minimal_solution(
                "Trace elements solution",
                repair_module.IMPORTED_TRACE_SIGNATURE,
            ),
            _minimal_solution(
                "Vitamin solution",
                repair_module.VITAMIN_SIGNATURE,
            ),
        ],
    }


def test_repair_document_adds_nbrc_identity_reference_and_unadjusted_ph(
    repair_module,
) -> None:
    doc = _minimal_doc(repair_module)
    doc["ph_value"] = 7.0
    repaired = repair_module.repair_document(doc)

    assert repaired["name"] == repair_module.TITLE
    assert repaired["original_name"] == repair_module.TITLE
    assert repaired["media_term"] == {
        "preferred_term": "NBRC Medium 857",
        "term": {"id": "nbrc.medium:857", "label": "NBRC Medium 857"},
    }
    assert "pH is unadjusted" in repaired["notes"]
    assert "ph_value" not in repaired
    assert "ph_range" not in repaired
    assert repaired["references"] == [{"reference": repair_module.NBRC_URL}]


def test_repair_document_grounds_nested_stocks(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))
    ingredients = {row["preferred_term"]: row for row in repaired["ingredients"]}
    solutions = {row["preferred_term"]: row for row in repaired["solutions"]}
    kp_buffer = {
        row["preferred_term"]: row for row in solutions["KP buffer"]["composition"]
    }
    trace = {
        row["preferred_term"]: row
        for row in solutions["Trace elements solution"]["composition"]
    }
    vitamins = {
        row["preferred_term"]: row
        for row in solutions["Vitamin solution"]["composition"]
    }

    assert repair_module._signature(
        repaired["ingredients"], "ingredients"
    ) == repair_module.IMPORTED_INGREDIENT_SIGNATURE
    assert repair_module._solution_signatures(repaired) == (
        repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert ingredients["Na2S2O3"]["term"]["id"] == "CHEBI:132112"
    assert ingredients["Na2S·9H2O"]["term"]["id"] == "CHEBI:76209"
    assert "term" not in ingredients["KP buffer*"]
    assert "term" not in ingredients["Trace elements solution**"]
    assert "term" not in ingredients["Vitamin solution***"]
    assert kp_buffer["K2HPO4"]["term"]["id"] == "CHEBI:131527"
    assert trace["FeCl3·6H2O"]["term"]["id"] == "CHEBI:86254"
    assert trace["CuCl2·2H2O"]["term"]["id"] == "CHEBI:86318"
    assert trace["NaOH"]["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert trace["KAl(SO4)2·12H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:86465",
        "label": "potassium aluminium sulfate dodecahydrate",
    }
    assert vitamins["Pyridoxine-HCl"]["term"]["id"] == "CHEBI:30961"
    assert vitamins["Ca-pantothenate"]["term"]["id"] == "CHEBI:31345"
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_document_adds_anaerobic_preparation(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert repaired["sterilization"] == {"method": "AUTOCLAVE"}
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert "H2/CO2" in repaired["preparation_steps"][0]["description"]
    assert repaired["preparation_steps"][2]["action"] == "FILTER_STERILIZE"
    assert "150 kPa" in repaired["preparation_steps"][3]["description"]


def test_repair_document_adds_reference_and_event_once(repair_module) -> None:
    once = repair_module.repair_document(_minimal_doc(repair_module))
    twice = repair_module.repair_document(once)

    assert twice["references"] == [{"reference": repair_module.NBRC_URL}]
    assert repair_module._solution_signatures(twice) == (
        repair_module.FINAL_SOLUTION_SIGNATURES
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

    with pytest.raises(ValueError, match="expected 'CultureMech:007499'"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_missing_recovery_decision(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["curation_history"] = []

    with pytest.raises(ValueError, match="missing recovery action"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_name_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["name"] = "NBRC Medium 859"

    with pytest.raises(ValueError, match="NBRC title/name drifted"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_ingredient_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["ingredients"][0] = _ingredient("KP buffer*", "12", "ML_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_solution_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["solutions"][0]["composition"][0] = _ingredient(
        "KH2PO4",
        "120",
        "G_PER_L",
    )

    with pytest.raises(ValueError, match="nested solution signature drifted"):
        repair_module.repair_document(doc)


def test_target_record_matches_nbrc_857_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    repaired = repair_module.repair_document(doc)

    assert doc["id"] == repair_module.TARGET_ID
    assert doc["name"] in {"859", repair_module.TITLE}
    assert repair_module._signature(doc["ingredients"], "ingredients") == (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE
    )
    assert repair_module._solution_signatures(repaired) == (
        repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert repaired["media_term"]["term"]["id"] == "nbrc.medium:857"
