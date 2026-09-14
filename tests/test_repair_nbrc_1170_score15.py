from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_1170_score15.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_nbrc_1170_score15", SCRIPT)
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
        "name": "1170",
        "original_name": "1170",
        "description": "1170. NBRC 1169.",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "curation_history": [{"action": repair_module.REQUIRED_ACTION}],
        "solutions": [
            _minimal_solution("Vitamin solution", repair_module.VITAMIN_SIGNATURE),
            _minimal_solution(
                "Trace elements solution",
                repair_module.IMPORTED_TRACE_SIGNATURE,
            ),
        ],
    }


def test_repair_document_adds_nbrc_identity_ph_and_reference(
    repair_module,
) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert repaired["name"] == repair_module.TITLE
    assert repaired["original_name"] == repair_module.TITLE
    assert repaired["ph_value"] == 7.4
    assert repaired["media_term"] == {
        "preferred_term": "NBRC Medium 1169",
        "term": {"id": "nbrc.medium:1169", "label": "NBRC Medium 1169"},
    }
    assert repaired["references"] == [{"reference": repair_module.NBRC_URL}]
    assert repaired["notes"] == repair_module.NOTES


def test_repair_document_adds_na2co3_naoh_and_groundings(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))
    ingredients = {row["preferred_term"]: row for row in repaired["ingredients"]}
    vitamins = {row["preferred_term"]: row for row in repaired["solutions"][0]["composition"]}
    trace = {row["preferred_term"]: row for row in repaired["solutions"][1]["composition"]}

    assert repair_module._signature(
        repaired["ingredients"], "ingredients"
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert repair_module._solution_signatures(repaired) == (
        repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert ingredients["Coenzyme M"]["term"]["id"] == "CHEBI:17905"
    assert ingredients["Bacto Yeast Extract (Difco)"]["term"]["id"] == (
        "FOODON:03315426"
    )
    assert ingredients["Na2CO3"]["term"]["id"] == "CHEBI:29377"
    assert trace["NaOH"]["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert trace["NaOH"]["term"]["id"] == "CHEBI:32145"
    assert trace["CuCl2·2H2O"]["term"]["id"] == "CHEBI:86318"
    assert trace["NiCl2·6H2O"]["term"]["id"] == "CHEBI:53542"
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
    assert "N2/CO2" in repaired["preparation_steps"][1]["description"]


def test_repair_document_adds_reference_and_event_once(repair_module) -> None:
    once = repair_module.repair_document(_minimal_doc(repair_module))
    twice = repair_module.repair_document(once)

    assert twice["references"] == [{"reference": repair_module.NBRC_URL}]
    assert repair_module._solution_signatures(twice) == (
        repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert len(
        [
            event
            for event in twice["curation_history"]
            if (
                event.get("curator") == repair_module.CURATOR
                and event.get("action") == repair_module.ACTION
            )
        ]
    ) == 1


def test_repair_document_rejects_wrong_id(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected 'CultureMech:007461'"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_missing_recovery_decision(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["curation_history"] = []

    with pytest.raises(ValueError, match="missing recovery action"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_name_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["name"] = "NBRC Medium 1170"

    with pytest.raises(ValueError, match="NBRC title/name drifted"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_ingredient_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["ingredients"][0] = _ingredient("NH4Cl", "0.3", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_solution_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["solutions"][1]["composition"][0] = _ingredient(
        "Nitrilotriacetic acid (NTA)", "1.28", "G_PER_L"
    )

    with pytest.raises(ValueError, match="nested solution signature drifted"):
        repair_module.repair_document(doc)


def test_target_record_matches_nbrc_1169_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    repaired = repair_module.repair_document(doc)

    assert doc["id"] == repair_module.TARGET_ID
    assert doc["name"] in {"1170", repair_module.TITLE}
    assert repair_module._signature(doc["ingredients"], "ingredients") in {
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    }
    assert repair_module._solution_signatures(repaired) == (
        repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert repaired["media_term"]["term"]["id"] == "nbrc.medium:1169"
