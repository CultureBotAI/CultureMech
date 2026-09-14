from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1070_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m1070_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1070")


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
        "name": "acidithrix_ferrooydans_medium",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "SEMI_DEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M1070",
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


def test_repair_preserves_main_m1070_components(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert repaired["physical_state"] == "LIQUID"
    assert repaired["ph_value"] == 2.5
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert ingredients["Glucose"]["term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert "term" not in ingredients["Yeast extract"]


def test_repair_expands_ubs_trace_and_nisew_solutions(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    assert set(solutions) == {
        "UBS solution",
        "Trace minerals",
        "Ni-Se-W solution",
        "1 M FeSO4 solution (pH 2.0)",
    }
    assert (
        repair_module._signature(
            solutions["UBS solution"]["composition"],
            "UBS solution",
        )
        == repair_module.UBS_SIGNATURE
    )
    assert (
        repair_module._signature(
            solutions["Trace minerals"]["composition"],
            "Trace minerals",
        )
        == repair_module.TRACE_MINERALS_SIGNATURE
    )
    assert (
        repair_module._signature(
            solutions["Ni-Se-W solution"]["composition"],
            "Ni-Se-W solution",
        )
        == repair_module.NISEW_SIGNATURE
    )


def test_repair_adds_expected_stock_groundings(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    ubs_components = _by_name(solutions["UBS solution"]["composition"])
    trace_components = _by_name(solutions["Trace minerals"]["composition"])
    nisew_components = _by_name(solutions["Ni-Se-W solution"]["composition"])

    assert ubs_components["(NH4)2SO4"]["term"] == {
        "id": "CHEBI:62946",
        "label": "ammonium sulfate",
    }
    assert "term" not in ubs_components["Ca(NO3)2 x 4H2O"]
    assert trace_components["AlK(SO4)2"]["term"] == {
        "id": "CHEBI:86463",
        "label": "potassium aluminium sulfate",
    }
    assert trace_components["MnSO4 x n H2O"]["term"] == {
        "id": "CHEBI:86360",
        "label": "manganese(II) sulfate hydrate",
    }
    assert nisew_components["NiCl2 x 6H2O"]["term"] == {
        "id": "CHEBI:53542",
        "label": "nickel chloride hexahydrate",
    }
    assert "term" not in nisew_components["Na2SeO3"]


def test_repair_models_1_m_feso4_stock(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    stock = _by_name(repaired["solutions"])["1 M FeSO4 solution (pH 2.0)"]

    assert stock["concentration"] == {"value": "5.0", "unit": "ML_PER_L"}
    assert (
        repair_module._signature(
            stock["composition"],
            "1 M FeSO4 solution (pH 2.0)",
        )
        == repair_module.FESO4_STOCK_SIGNATURE
    )
    assert stock["composition"][0]["term"] == {
        "id": "CHEBI:75832",
        "label": "iron(2+) sulfate (anhydrous)",
    }


def test_repair_record_drops_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (0, [])
    assert (
        scorer_module.score_parsed(
            [("bacterial/TOGO_M1070_Acidithrix_Ferrooydans_Medium.yaml", repaired)]
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

    with pytest.raises(ValueError, match="expected id CultureMech:007588"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M1007"

    with pytest.raises(ValueError, match="expected media term TOGO:M1070"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Water", "1", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["concentration"] = {"value": "100", "unit": "ML_PER_L"}

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_togo_m1070_repair_contract(repair_module) -> None:
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
