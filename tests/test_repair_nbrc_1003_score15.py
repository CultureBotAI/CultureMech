from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_1003_score15.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_nbrc_1003_score15", SCRIPT)
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
        "name": "1003",
        "original_name": "1003",
        "description": "1003. NBRC 1002.",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient("MgSO4·7H2O", "0.5", "G_PER_L"),
            _ingredient("(NH4)2SO4", "0.4", "G_PER_L"),
            _ingredient("K2HPO4", "0.2", "G_PER_L"),
            _ingredient("KCl", "0.1", "G_PER_L"),
            _ingredient("Distilled water", "1", "L"),
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "DISSOLVE",
                "description": "Dissolve ingredients in distilled water",
            },
        ],
        "curation_history": [{"action": repair_module.REQUIRED_ACTION}],
    }


def test_repair_document_adds_nbrc_identity_and_reference(repair_module) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert repaired["name"] == "Acidimicrobium Medium"
    assert repaired["original_name"] == "Acidimicrobium Medium"
    assert repaired["media_term"] == {
        "preferred_term": "NBRC Medium 1002",
        "term": {"id": "nbrc.medium:1002", "label": "NBRC Medium 1002"},
    }
    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert repaired["references"] == [{"reference": repair_module.NBRC_URL}]
    assert repaired["notes"] == repair_module.NOTES


def test_repair_document_grounds_recovered_and_variant_components(
    repair_module,
) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))
    ingredients = {row["preferred_term"]: row for row in repaired["ingredients"]}

    assert ingredients["MgSO4·7H2O"]["term"] == {
        "id": "CHEBI:31795",
        "label": "magnesium sulfate heptahydrate",
    }
    assert ingredients["(NH4)2SO4"]["term"]["id"] == "CHEBI:62946"
    assert ingredients["K2HPO4"]["term"]["id"] == "CHEBI:131527"
    assert ingredients["KCl"]["term"]["id"] == "CHEBI:32588"
    assert ingredients["H2SO4"]["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert ingredients["H2SO4"]["term"]["id"] == "CHEBI:26836"
    assert ingredients["FeSO4·7H2O"]["term"] == {
        "id": "CHEBI:75836",
        "label": "iron(2+) sulfate heptahydrate",
    }
    assert ingredients["Yeast extract"]["term"]["id"] == "FOODON:03315426"
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_document_adds_source_preparation_and_variants(
    repair_module,
) -> None:
    repaired = repair_module.repair_document(_minimal_doc(repair_module))

    assert repaired["ph_value"] == 2.0
    assert repaired["sterilization"] == {"method": "AUTOCLAVE"}
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert repaired["variants"] == list(repair_module.VARIANTS)
    assert repaired["variants"][0]["modifications"] == [
        "Add 10 mg/L FeSO4·7H2O to the medium.",
        (
            "After autoclaving, add yeast extract from a sterile stock solution to "
            "0.25 g/L final concentration."
        ),
    ]
    assert repaired["variants"][1]["modifications"] == [
        "Add 13.9 g/L FeSO4·7H2O to the medium.",
        "Adjust medium pH to 1.7 with H2SO4 prior to autoclaving.",
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

    with pytest.raises(ValueError, match="expected 'CultureMech:007449'"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_unrecovered_record(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["curation_history"] = []

    with pytest.raises(ValueError, match="missing recovery action"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_name_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["name"] = "NBRC Medium 1003"

    with pytest.raises(ValueError, match="NBRC title/name drifted"):
        repair_module.repair_document(doc)


def test_repair_document_rejects_ingredient_drift(repair_module) -> None:
    doc = _minimal_doc(repair_module)
    doc["ingredients"][0] = _ingredient("MgSO4", "0.5", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_document(doc)


def test_target_record_matches_recovered_nbrc_1002_formula(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET_PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    repaired = repair_module.repair_document(doc)

    assert doc["id"] == repair_module.TARGET_ID
    assert doc["name"] in {"1003", "Acidimicrobium Medium"}
    assert repair_module._signature(doc["ingredients"], "ingredients") in {
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    }
    assert repaired["media_term"]["term"]["id"] == "nbrc.medium:1002"
    assert repair_module._signature(
        repaired["ingredients"], "ingredients"
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
