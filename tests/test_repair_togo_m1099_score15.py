from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1099_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m1099_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1099")


def _ingredient(name: str, value: str, unit: str) -> dict:
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
        "name": "vxg_gellan",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M1099",
            "term": {"id": repair_module.EXPECTED_MEDIA_TERM, "label": repair_module.TITLE},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_preserves_main_m1099_components(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert repaired["physical_state"] == "LIQUID"
    assert repaired["ph_value"] == 5.5
    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "960.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Gellan gum"]["term"] == {
        "id": "CHEBI:85248",
        "label": "gellan gum",
    }


def test_repair_expands_molar_salt_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    assert set(solutions) == {
        "30 mM CaCl2 x 2H2O solution",
        "1 M MgCl2 x 6H2O solution",
        "20 mM MgSO4 x 7H2O solution",
        "20 mM (NH4)2HPO4 solution",
        "Selenite-tungstate solution",
        "Trace element solution SL-10",
    }
    assert repair_module._signature(
        solutions["30 mM CaCl2 x 2H2O solution"]["composition"],
        "30 mM CaCl2 x 2H2O solution",
    ) == repair_module.CACL2_STOCK_SIGNATURE
    assert repair_module._signature(
        solutions["1 M MgCl2 x 6H2O solution"]["composition"],
        "1 M MgCl2 x 6H2O solution",
    ) == repair_module.MGCL2_STOCK_SIGNATURE
    assert repair_module._signature(
        solutions["20 mM MgSO4 x 7H2O solution"]["composition"],
        "20 mM MgSO4 x 7H2O solution",
    ) == repair_module.MGSO4_STOCK_SIGNATURE
    assert repair_module._signature(
        solutions["20 mM (NH4)2HPO4 solution"]["composition"],
        "20 mM (NH4)2HPO4 solution",
    ) == repair_module.AMMONIUM_HPO4_STOCK_SIGNATURE


def test_repair_expands_cross_referenced_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    selenite = solutions["Selenite-tungstate solution"]
    trace_element = solutions["Trace element solution SL-10"]
    selenite_components = _by_name(selenite["composition"])
    trace_components = _by_name(trace_element["composition"])

    assert repair_module._signature(
        selenite["composition"],
        "Selenite-tungstate solution",
    ) == repair_module.SELENITE_TUNGSTATE_SIGNATURE
    assert repair_module._signature(
        trace_element["composition"],
        "Trace element solution SL-10",
    ) == repair_module.TRACE_ELEMENT_SIGNATURE
    assert selenite_components["Na2SeO3 x 5H2O"]["term"] == {
        "id": "CHEBI:131361",
        "label": "disodium selenite pentahydrate",
    }
    assert trace_components["FeCl2 x 4H2O"]["concentration"] == {
        "value": "1.5",
        "unit": "G_PER_L",
    }
    assert trace_components["Na2MoO4 x 2H2O"]["term"] == {
        "id": "CHEBI:75213",
        "label": "sodium molybdate dihydrate",
    }


def test_repair_record_drops_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (0, [])
    assert (
        scorer_module.score_parsed(
            [("bacterial/TOGO_M1099_VXG_Gellan.yaml", repaired)]
        )
        == []
    )
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["references"] == [{"reference": url} for url in repair_module.REFERENCES]
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


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:007616"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M1007"

    with pytest.raises(ValueError, match="expected media term TOGO:M1099"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Water", "960", "ML_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["concentration"] = {"value": "10", "unit": "ML_PER_L"}

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_togo_m1099_repair_contract(repair_module) -> None:
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
