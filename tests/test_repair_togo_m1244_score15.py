from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1244_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m1244_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1244")


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
        "id": repair_module.RECORD_ID,
        "name": "nas_02_medium",
        "original_name": "NAS-02 Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M1244",
            "term": {"id": repair_module.MEDIA_TERM, "label": "NAS-02 Medium"},
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


def test_repair_normalizes_main_solution_and_ph(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["ph_value"] == 5.2
    assert repaired["composition_type"] == "SEMI_DEFINED"

    ingredients = _by_name(repaired["ingredients"])
    assert "Nitrogen gas" not in ingredients
    assert ingredients["KH2PO4"]["concentration"] == {
        "value": "2.85442",
        "unit": "G_PER_L",
    }
    assert ingredients["Na2S2O3 x 5H2O"]["term"] == {
        "id": "CHEBI:32150",
        "label": "sodium thiosulfate pentahydrate",
    }
    assert ingredients["N2"]["term"] == {
        "id": "CHEBI:17997",
        "label": "dinitrogen",
    }


def test_repair_expands_modified_allen_trace_solution(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    trace = _by_name(solutions["Modified Allen's trace metal solution"]["composition"])

    assert solutions["Modified Allen's trace metal solution"]["concentration"] == {
        "value": "1.0",
        "unit": "ML_PER_L",
    }
    assert trace["Na2B4O7 x 10H2O"]["term"] == {
        "id": "CHEBI:131366",
        "label": "disodium tetraborate decahydrate",
    }
    assert trace["VOSO4 x nH2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:87020",
        "label": "vanadyl sulfate hydrate",
    }


def test_repair_expands_post_autoclave_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    magnesium = _by_name(solutions["5% (w/v) MgSO4 x 7H2O solution"]["composition"])
    yeast = _by_name(solutions["10% (w/v) Yeast extract solution"]["composition"])
    cysteine = _by_name(solutions["25 mM L-Cysteine HCl solution"]["composition"])
    iron = _by_name(solutions["130 mM FeCl2 solution"]["composition"])

    assert magnesium["MgSO4 x 7H2O"]["concentration"] == {
        "value": "50.0",
        "unit": "G_PER_L",
    }
    assert yeast["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert cysteine["L-Cysteine HCl"]["concentration"] == {
        "value": "25.0",
        "unit": "MILLIMOLAR",
    }
    assert iron["FeCl2"]["concentration"] == {
        "value": "130.0",
        "unit": "MILLIMOLAR",
    }


def test_repair_expands_trace_vitamins_from_jcm_197(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    vitamins = _by_name(solutions["Trace vitamins"]["composition"])

    assert solutions["Trace vitamins"]["concentration"] == {
        "value": "10.0",
        "unit": "ML_PER_L",
    }
    assert vitamins["Biotin"]["concentration"] == {
        "value": "2.0",
        "unit": "MG_PER_L",
    }
    assert vitamins["Vitamin B12"]["concentration"] == {
        "value": "0.1",
        "unit": "MG_PER_L",
    }
    assert vitamins["Lipoic acid"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:16494",
        "label": "lipoic acid",
    }


def test_repair_drops_m1244_out_of_review_ranking(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
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

    with pytest.raises(ValueError, match="expected id CultureMech:007774"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M1221"

    with pytest.raises(ValueError, match="expected media term TOGO:M1244"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Tap water", "1", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0] = _solution("Other stock", "1", "G_PER_L")

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)
