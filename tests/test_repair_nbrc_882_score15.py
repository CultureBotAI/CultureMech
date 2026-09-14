from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_882_score15.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_nbrc_882_score15", SCRIPT)
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
            _ingredient(ingredient, value, unit) for ingredient, value, unit in signature
        ],
    }


def _minimal_doc(repair_module) -> dict:
    return {
        "id": repair_module.TARGET_ID,
        "name": "882",
        "original_name": "882",
        "description": "882. NBRC 881.",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "curation_history": [{"action": repair_module.REQUIRED_ACTION}],
        "solutions": [
            _minimal_solution(
                "Tween 80 solution",
                repair_module.TWEEN_80_SIGNATURE,
            ),
            _minimal_solution(
                "Salts solution",
                repair_module.SALTS_SIGNATURE,
            ),
        ],
    }


def test_repair_document_adds_nbrc_identity_reference_and_ph(
    repair_module,
) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert repaired["name"] == repair_module.TITLE
    assert repaired["original_name"] == repair_module.TITLE
    assert repaired["media_term"] == {
        "preferred_term": "NBRC Medium 881",
        "term": {"id": "nbrc.medium:881", "label": "NBRC Medium 881"},
    }
    assert repaired["ph_value"] == 6.0
    assert repaired["references"] == [{"reference": repair_module.NBRC_URL}]
    assert repaired["notes"] == repair_module.NOTES


def test_repair_document_adds_and_grounds_solid_components(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))
    ingredients = {row["preferred_term"]: row for row in repaired["ingredients"]}
    solutions = {row["preferred_term"]: row for row in repaired["solutions"]}
    tween = {row["preferred_term"]: row for row in solutions["Tween 80 solution"]["composition"]}
    salts = {row["preferred_term"]: row for row in solutions["Salts solution"]["composition"]}

    assert (
        repair_module._signature(repaired["ingredients"], "ingredients")
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repair_module._solution_signatures(repaired) == (
        repair_module.IMPORTED_SOLUTION_SIGNATURES
    )
    assert ingredients["Agar"]["concentration"] == {
        "value": "15",
        "unit": "G_PER_L",
    }
    assert ingredients["CaCO3"]["term"]["id"] == "CHEBI:3311"
    assert ingredients["Glucose"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert "term" not in ingredients["Bacto Yeast Extract (Difco)"]
    assert "term" not in ingredients["Hipolypepton*"]
    assert "term" not in ingredients["Tween 80 solution**"]
    assert "term" not in ingredients["Salts solution***"]
    assert tween["Tween 80"]["term"]["id"] == "CHEBI:53426"
    assert salts["MgSO4·7H2O"]["term"]["id"] == "CHEBI:31795"
    assert salts["MnSO4·4H2O"]["term"]["id"] == "CHEBI:86358"
    assert salts["FeSO4·7H2O"]["term"]["id"] == "CHEBI:75836"
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_document_adds_source_preparation(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert "sterilization" not in repaired
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert "15 g/L agar" in repaired["preparation_steps"][1]["description"]
    assert "12 N HCl" in repaired["preparation_steps"][2]["description"]


def test_repair_document_adds_reference_and_event_once(repair_module) -> None:
    once = repair_module.repair_document(_minimal_doc(repair_module))
    twice = repair_module.repair_document(once)

    assert twice["references"] == [{"reference": repair_module.NBRC_URL}]
    assert (
        repair_module._signature(twice["ingredients"], "ingredients")
        == repair_module.FINAL_INGREDIENT_SIGNATURE
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

    with pytest.raises(ValueError, match="expected 'CultureMech:007501'"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_missing_recovery_decision(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["curation_history"] = []

    with pytest.raises(ValueError, match="missing recovery action"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_name_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["name"] = "NBRC Medium 882"

    with pytest.raises(ValueError, match="NBRC title/name drifted"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_ingredient_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["ingredients"][0] = _ingredient("Glucose", "11", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_solution_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["solutions"][1]["composition"][0] = _ingredient(
        "MgSO4·7H2O",
        "39",
        "G_PER_L",
    )

    with pytest.raises(ValueError, match="nested solution signature drifted"):
        repair_module.repair_document(doc)


def test_target_record_matches_nbrc_881_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    repaired = repair_module.repair_document(doc)

    assert doc["id"] == repair_module.TARGET_ID
    assert doc["name"] in {"882", repair_module.TITLE}
    assert repair_module._signature(doc["ingredients"], "ingredients") in {
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    }
    assert repair_module._solution_signatures(repaired) == (
        repair_module.IMPORTED_SOLUTION_SIGNATURES
    )
    assert repaired["media_term"]["term"]["id"] == "nbrc.medium:881"
