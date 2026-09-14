from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_1021_score15.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_nbrc_1021_score15", SCRIPT)
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


def _solution(name: str, signature) -> dict:
    return {
        "preferred_term": name,
        "composition": [
            _ingredient(row_name, value, unit)
            for row_name, value, unit in signature
        ],
    }


def _minimal_doc(repair_module) -> dict:
    return {
        "id": repair_module.TARGET_ID,
        "name": "1021",
        "original_name": "1021",
        "description": "1021. NBRC 1020.",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "solutions": [
            _solution(name, signature)
            for name, signature in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
        "curation_history": [{"action": repair_module.REQUIRED_ACTION}],
    }


def test_repair_document_adds_nbrc_identity_and_reference(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert repaired["name"] == "Methanofollis ethanolicus medium"
    assert repaired["original_name"] == "Methanofollis ethanolicus medium"
    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert repaired["media_term"] == {
        "preferred_term": "NBRC Medium 1020",
        "term": {"id": "nbrc.medium:1020", "label": "NBRC Medium 1020"},
    }
    assert repaired["references"] == [{"reference": repair_module.NBRC_URL}]
    assert repaired["notes"] == repair_module.NOTES


def test_repair_document_grounds_top_level_chemicals(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))
    ingredients = {row["preferred_term"]: row for row in repaired["ingredients"]}

    assert ingredients["Yeast extract"]["term"]["id"] == "FOODON:03315426"
    assert ingredients["MgCl2·6H2O"]["term"] == {
        "id": "CHEBI:86345",
        "label": "magnesium dichloride hexahydrate",
    }
    assert ingredients["CaCl2·2H2O"]["term"]["id"] == "CHEBI:86158"
    assert ingredients["Na2S·9H2O"]["term"]["id"] == "CHEBI:76209"
    assert ingredients["Cysteine-HCl"]["term"]["id"] == "CHEBI:91247"
    assert "has_unmapped_ingredients" in repaired["data_quality_flags"]


def test_repair_document_grounds_nested_stocks_and_adds_koh(
    repair_module,
) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))
    rows = {
        row["preferred_term"]: row
        for solution in repaired["solutions"]
        for row in solution["composition"]
    }

    assert rows["Pyridoxine-HCl"]["term"]["id"] == "CHEBI:30961"
    assert rows["Ca-pantothenate"]["term"]["id"] == "CHEBI:31345"
    assert rows["Lipoic acid"]["term"]["id"] == "CHEBI:16494"
    assert rows["Nitrilotriacetic acid (NTA)"]["term"]["id"] == "CHEBI:44557"
    assert rows["FeCl3·6H2O"]["term"]["id"] == "CHEBI:86254"
    assert rows["MnCl2·4H2O"]["term"]["id"] == "CHEBI:86368"
    assert rows["CoCl2·6H2O"]["term"]["id"] == "CHEBI:53503"
    assert rows["CuCl2·2H2O"]["term"]["id"] == "CHEBI:86318"
    assert rows["Na2MoO4·2H2O"]["term"]["id"] == "CHEBI:75213"
    assert rows["Na2WO4"]["term"]["id"] == "CHEBI:63940"
    assert rows["NiCl2·6H2O"]["term"]["id"] == "CHEBI:53542"
    assert rows["KOH"]["concentration"] == {"value": "variable", "unit": "VARIABLE"}
    assert rows["KOH"]["term"]["id"] == "CHEBI:32035"


def test_repair_document_adds_source_preparation(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert repaired["sterilization"] == {"method": "AUTOCLAVE"}
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert repaired["preparation_steps"][1]["description"] == (
        "Flush the medium with N2/CO2 (80/20)."
    )
    assert "KOH" in repaired["preparation_steps"][-1]["description"]


def test_repair_document_adds_reference_and_event_once(repair_module) -> None:
    once = repair_module.repair_document(_minimal_doc(repair_module))
    twice = repair_module.repair_document(once)

    assert repair_module._solution_signatures(twice) == (
        repair_module.FINAL_SOLUTION_SIGNATURES
    )
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

    with pytest.raises(ValueError, match="expected 'CultureMech:007450'"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_unrecovered_record(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["curation_history"] = []

    with pytest.raises(ValueError, match="missing recovery action"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_name_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["name"] = "NBRC Medium 1021"

    with pytest.raises(ValueError, match="NBRC title/name drifted"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_solution_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["solutions"][1]["composition"][0] = _ingredient("NTA", "12.8", "G_PER_L")

    with pytest.raises(ValueError, match="nested solution signature drifted"):
        repair_module.repair_document(doc)


def test_target_record_matches_recovered_nbrc_1020_formula(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    repaired = repair_module.repair_document(doc)

    assert doc["id"] == repair_module.TARGET_ID
    assert doc["name"] in {"1021", "Methanofollis ethanolicus medium"}
    assert repair_module._signature(
        doc["ingredients"], "ingredients"
    ) == repair_module.IMPORTED_INGREDIENT_SIGNATURE
    assert repair_module._solution_signatures(doc) in {
        repair_module.IMPORTED_SOLUTION_SIGNATURES,
        repair_module.FINAL_SOLUTION_SIGNATURES,
    }
    assert repaired["media_term"]["term"]["id"] == "nbrc.medium:1020"
