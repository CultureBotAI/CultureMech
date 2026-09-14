from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1066_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m1066_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1066")


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
        "name": "clostridium_swellfunianum_medium",
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
            "preferred_term": "TOGO Medium M1066",
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


def test_repair_moves_clostridium_swellfunianum_medium_into_solutions(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    assert repaired["physical_state"] == "LIQUID"
    assert repaired["ph_value"] == 7.3
    assert repaired["ingredients"] == []
    assert set(solutions) == {
        "Sol. 1",
        "Sol. 2",
        "1% CaCl2 x 2H2O solution",
        "2% MgCl2 x 6H2O solution",
        "1% Resazurin solution",
        "Trace element solution SL-10",
        "Trace vitamins",
        "10% (w/v) NaHCO3 solution",
        "20% (w/v) Glucose solution",
        "3% (w/v) Na2S x 9H2O solution",
    }
    assert solutions["Sol. 1"]["concentration"] == {
        "value": "5.0",
        "unit": "ML_PER_L",
    }
    assert solutions["Sol. 2"]["concentration"] == {
        "value": "0.2",
        "unit": "ML_PER_L",
    }
    assert (
        repair_module._signature(
            solutions["Sol. 1"]["composition"],
            "Sol. 1",
        )
        == repair_module.SOLUTION_1_SIGNATURE
    )
    assert (
        repair_module._signature(
            solutions["Sol. 2"]["composition"],
            "Sol. 2",
        )
        == repair_module.SOLUTION_2_SIGNATURE
    )


def test_repair_expands_m1066_percent_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    sol_1_components = _by_name(solutions["Sol. 1"]["composition"])
    sol_2_components = _by_name(solutions["Sol. 2"]["composition"])

    cacl2 = solutions["1% CaCl2 x 2H2O solution"]
    mgcl2 = solutions["2% MgCl2 x 6H2O solution"]
    resazurin = solutions["1% Resazurin solution"]
    nahco3 = solutions["10% (w/v) NaHCO3 solution"]
    glucose = solutions["20% (w/v) Glucose solution"]
    na2s = solutions["3% (w/v) Na2S x 9H2O solution"]

    assert sol_1_components["1% CaCl2 x 2H2O solution"]["concentration"] == {
        "value": "33.0",
        "unit": "ML_PER_L",
    }
    assert sol_2_components["3% (w/v) Na2S x 9H2O solution"]["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert "composition" not in sol_2_components["3% (w/v) Na2S x 9H2O solution"]
    assert (
        repair_module._signature(
            cacl2["composition"],
            "1% CaCl2 x 2H2O solution",
        )
        == repair_module.CACL2_STOCK_SIGNATURE
    )
    assert (
        repair_module._signature(
            mgcl2["composition"],
            "2% MgCl2 x 6H2O solution",
        )
        == repair_module.MGCL2_STOCK_SIGNATURE
    )
    assert (
        repair_module._signature(
            resazurin["composition"],
            "1% Resazurin solution",
        )
        == repair_module.RESAZURIN_STOCK_SIGNATURE
    )
    assert (
        repair_module._signature(
            nahco3["composition"],
            "10% (w/v) NaHCO3 solution",
        )
        == repair_module.NAHCO3_STOCK_SIGNATURE
    )
    assert (
        repair_module._signature(
            glucose["composition"],
            "20% (w/v) Glucose solution",
        )
        == repair_module.GLUCOSE_STOCK_SIGNATURE
    )
    assert (
        repair_module._signature(
            na2s["composition"],
            "3% (w/v) Na2S x 9H2O solution",
        )
        == repair_module.NA2S_STOCK_SIGNATURE
    )
    assert na2s["composition"][0]["term"] == {
        "id": "CHEBI:76209",
        "label": "sodium sulfide nonahydrate",
    }


def test_repair_expands_trace_element_solution_sl10(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    trace_element = _by_name(repaired["solutions"])["Trace element solution SL-10"]
    components = _by_name(trace_element["composition"])

    assert (
        repair_module._signature(
            trace_element["composition"],
            "Trace element solution SL-10",
        )
        == repair_module.TRACE_ELEMENT_SIGNATURE
    )
    assert trace_element["concentration"] == {
        "value": "1.0",
        "unit": "ML_PER_L",
    }
    assert components["FeCl2 x 4H2O"]["concentration"] == {
        "value": "1.5",
        "unit": "G_PER_L",
    }
    assert components["Na2MoO4 x 2H2O"]["term"] == {
        "id": "CHEBI:75213",
        "label": "sodium molybdate dihydrate",
    }
    assert components["ZnCl2"]["term"] == {
        "id": "CHEBI:49976",
        "label": "zinc dichloride",
    }


def test_repair_expands_m190_trace_vitamins(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    trace_vitamins = _by_name(repaired["solutions"])["Trace vitamins"]
    components = _by_name(trace_vitamins["composition"])

    assert (
        repair_module._signature(
            trace_vitamins["composition"],
            "Trace vitamins",
        )
        == repair_module.TRACE_VITAMINS_SIGNATURE
    )
    assert components["Vitamin B12"]["concentration"] == {
        "value": "0.1",
        "unit": "MG_PER_L",
    }
    assert components["Thiamine HCl"]["term"] == {
        "id": "CHEBI:49105",
        "label": "thiamine hydrochloride",
    }
    assert "Nicotinamide" not in components


def test_repair_record_drops_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (0, [])
    assert (
        scorer_module.score_parsed(
            [("bacterial/TOGO_M1066_Clostridium_Swellfunianum_Medium.yaml", repaired)]
        )
        == []
    )
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
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

    with pytest.raises(ValueError, match="expected id CultureMech:007583"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M1007"

    with pytest.raises(ValueError, match="expected media term TOGO:M1066"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Solution 1", "5", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["concentration"] = {"value": "33", "unit": "ML_PER_L"}

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_togo_m1066_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        (),
    )
    assert repair_module._solution_signatures(doc) in (
        repair_module.IMPORTED_SOLUTION_SIGNATURES,
        repair_module.FINAL_SOLUTION_SIGNATURES,
    )
