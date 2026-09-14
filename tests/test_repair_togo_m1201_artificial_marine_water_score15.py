from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1201_artificial_marine_water_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m1201_artificial_marine_water_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1201")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
    }


def _doc(repair_module) -> dict:
    return {
        "id": "CultureMech:007728",
        "name": "artficial_marine_water_medium",
        "original_name": "Artficial Marine Water Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M1201",
            "term": {"id": "TOGO:M1201", "label": "Artficial Marine Water Medium"},
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


def test_repair_expands_artificial_marine_water_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["medium_type"] == "DEFINED"
    assert repaired["composition_type"] == "DEFINED"

    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert "Nitrogen gas" not in ingredients
    assert ingredients["NaCl"]["concentration"] == {
        "value": "24.5052",
        "unit": "G_PER_L",
    }
    assert ingredients["Resazurin"]["concentration"] == {
        "value": "0.942507",
        "unit": "MG_PER_L",
    }
    assert solutions["1 M MgCl2 x 6H2O solution"]["concentration"] == {
        "value": "40.0",
        "unit": "ML_PER_L",
    }
    assert solutions["1 M CaCl2 x 2H2O solution"]["concentration"] == {
        "value": "10.0",
        "unit": "ML_PER_L",
    }
    assert solutions["8% NaHCO3 solution"]["composition"][0]["concentration"] == {
        "value": "80.0",
        "unit": "G_PER_L",
    }
    assert solutions["5% Na2S x 9H2O solution"]["composition"][0]["term"] == {
        "id": "CHEBI:76209",
        "label": "sodium sulfide nonahydrate",
    }
    assert solutions["1 M Glucose solution"]["preparation_notes"] == "Filter-sterilize separately."


def test_repair_expands_jcm_187_and_431_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    fecl2 = _by_name(solutions["FeCl2 solution"]["composition"])
    trace = _by_name(solutions["Trace element solution"]["composition"])
    selenite = _by_name(solutions["Selenite-tungstate solution"]["composition"])

    assert fecl2["HCl"]["concentration"] == {"value": "10.0", "unit": "ML_PER_L"}
    assert fecl2["FeCl2 x 4H2O"]["term"] == {
        "id": "CHEBI:86249",
        "label": "iron dichloride tetrahydrate",
    }
    assert trace["Na2MoO4 x 2H2O"]["concentration"] == {
        "value": "36.0",
        "unit": "MG_PER_L",
    }
    assert "term" not in trace["NiCl2 x 6H2O"]
    assert selenite["Na2SeO3 x 5H2O"]["term"] == {
        "id": "CHEBI:131361",
        "label": "disodium selenite pentahydrate",
    }


def test_repair_expands_jcm_403_vitamin_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    vitamins = _by_name(solutions["Vitamin solution"]["composition"])
    thiamine = _by_name(solutions["Thiamine solution"]["composition"])
    b12 = _by_name(solutions["Vitamin B12 solution"]["composition"])

    assert vitamins["p-Aminobenzoic acid"]["concentration"] == {
        "value": "40.0",
        "unit": "MG_PER_L",
    }
    assert "term" not in vitamins["Sodium phosphate buffer (10 mM, pH 7.1)"]
    assert thiamine["Thiamine HCl"]["concentration"] == {
        "value": "100.0",
        "unit": "MG_PER_L",
    }
    assert "term" not in thiamine["Sodium phosphate buffer (25 mM, pH 3.4)"]
    assert b12["Vitamin B12"]["concentration"] == {
        "value": "50.0",
        "unit": "MG_PER_L",
    }


def test_repair_record_drops_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["references"] == [{"reference": url} for url in repair_module._references()]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == "; ".join(repair_module._references())


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:007728"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M1200"

    with pytest.raises(ValueError, match="expected media term TOGO:M1201"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Tap water", "1", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0] = _solution("FeCl2 solution", "3", "G_PER_L")

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)
