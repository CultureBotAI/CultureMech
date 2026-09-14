from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m3279_alkaline_diluted_ams_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m3279_alkaline_diluted_ams_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m3279")


def _component(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
    }


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "alkaline_diluted_ams_medium",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M3279",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO M3279",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_base_formula_ph_and_gas_phase(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["medium_type"] == "DEFINED"
    assert repaired["composition_type"] == "DEFINED"
    assert repaired["ph_value"] == 8.0
    assert "ph_range" not in repaired
    assert repaired["aeration"] == "methane-air (80:20, v/v)"
    assert repaired["incubation_atmosphere"] == "MICROAEROPHILIC"
    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert "Methane gas" not in ingredients
    assert "Air" not in ingredients
    assert ingredients["NH4Cl"]["nutritional_roles"] == ["NITROGEN_SOURCE"]
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_expands_jcm_815_stock_solutions(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    trace = _by_name(solutions["Trace element solution"]["composition"])
    iron = _by_name(solutions["Iron stock solution"]["composition"])
    phosphate = _by_name(solutions["Phosphate buffer stock solution"]["composition"])

    assert repair_module._solution_signatures(repaired) == (
        repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert solutions["Trace element solution"]["concentration"] == {
        "value": "0.1",
        "unit": "ML_PER_L",
    }
    assert solutions["Iron stock solution"]["concentration"] == {
        "value": "0.1",
        "unit": "ML_PER_L",
    }
    assert solutions["Iron stock solution"]["term"] == {
        "id": "mediadive.solution:4767",
        "label": "Iron stock solution 4.5 g/L",
    }
    assert solutions["Phosphate buffer stock solution"]["concentration"] == {
        "value": "1.0",
        "unit": "ML_PER_L",
    }
    assert trace["ZnSO4 x 7 H2O"]["term"] == {
        "id": "CHEBI:32312",
        "label": "zinc sulfate heptahydrate",
    }
    assert trace["NiCl2 x 6 H2O"]["term"] == {
        "id": "CHEBI:53542",
        "label": "nickel chloride hexahydrate",
    }
    assert iron["EDTA x Fe(III)"]["term"] == {
        "id": "CHEBI:30729",
        "label": "ethylenediaminetetraacetatoferrate(1-)",
    }
    assert phosphate["KH2PO4"]["physicochemical_roles"] == ["BUFFER"]
    assert phosphate["Na2HPO4 x 2 H2O"]["physicochemical_roles"] == ["BUFFER"]


def test_repair_adds_preparation_sterilization_references_and_event_once(
    repair_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert [step["action"] for step in twice["preparation_steps"]] == [
        "DISSOLVE",
        "AUTOCLAVE",
        "AUTOCLAVE",
        "MIX",
        "ADJUST_PH",
        "ALIQUOT",
        "FILTER_STERILIZE",
    ]
    assert twice["sterilization"] == repair_module.STERILIZATION
    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
    ]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == "; ".join(repair_module.REFERENCES)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M815"

    with pytest.raises(ValueError, match="expected media term TOGO:M3279"):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _component("Tap water", "1", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["preferred_term"] = "Trace element solution"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_togo_m3279_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
    assert repair_module._solution_signatures(doc) in (
        repair_module.IMPORTED_SOLUTION_SIGNATURES,
        repair_module.FINAL_SOLUTION_SIGNATURES,
    )
