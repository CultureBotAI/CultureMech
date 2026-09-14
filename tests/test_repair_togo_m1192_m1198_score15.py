from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1192_m1198_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m1192_m1198_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1192_m1198")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
    }


def _doc(repair_module, target) -> dict:
    if target == repair_module.M1192:
        ingredients = [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.M1192_IMPORTED_INGREDIENT_SIGNATURE
        ]
        solutions = [
            _solution(name, value, unit)
            for name, value, unit, _ in repair_module.M1192_IMPORTED_SOLUTION_SIGNATURES
        ]
    else:
        ingredients = [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.M1198_IMPORTED_INGREDIENT_SIGNATURE
        ]
        solutions = [
            _solution(name, value, unit)
            for name, value, unit, _ in repair_module.M1198_IMPORTED_SOLUTION_SIGNATURES
        ]

    return {
        "id": target.record_id,
        "name": target.title.lower().replace("-", "_").replace(" ", "_"),
        "original_name": target.title,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": ingredients,
        "media_term": {
            "preferred_term": f"TOGO Medium {target.media_term.removeprefix('TOGO:')}",
            "term": {"id": target.media_term, "label": target.title},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": solutions,
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_m1192_expands_sw25_solution(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.M1192),
        repair_module.M1192,
    )

    assert repaired["ph_value"] == 7.5
    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["composition_type"] == "SEMI_DEFINED"

    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])
    sw25_components = _by_name(solutions["SW-25 solution"]["composition"])

    assert ingredients["Agar"]["concentration"] == {
        "value": "20.0",
        "unit": "G_PER_L",
    }
    assert ingredients["Agar"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert "term" not in ingredients["Casamino acids (BD-Difco)"]
    assert "term" not in ingredients["Yeast extract"]
    assert sw25_components["NaCl"]["concentration"] == {
        "value": "195.0",
        "unit": "G_PER_L",
    }
    assert sw25_components["MgCl2 x 6H2O"]["term"] == {
        "id": "CHEBI:86345",
        "label": "magnesium dichloride hexahydrate",
    }
    assert sw25_components["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }


def test_repair_m1198_corrects_main_solution_and_ethane(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.M1198),
        repair_module.M1198,
    )

    assert repaired["medium_type"] == "DEFINED"
    assert repaired["composition_type"] == "DEFINED"
    assert repaired["ph_value"] == 8.0
    assert repaired["sterilization"]["temperature"] == {
        "value": 110.0,
        "unit": "CELSIUS",
    }

    ingredients = _by_name(repaired["ingredients"])
    assert ingredients["NH4NO3"]["concentration"] == {
        "value": "0.0996016",
        "unit": "G_PER_L",
    }
    assert ingredients["Fe(III)-EDTA"]["concentration"] == {
        "value": "0.00249004",
        "unit": "G_PER_L",
    }
    assert ingredients["Ethane"]["concentration"] == {
        "value": "10-50",
        "unit": "PERCENT_V_V",
    }
    assert "term" not in ingredients["Ethane"]


def test_repair_m1198_expands_cross_referenced_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.M1198),
        repair_module.M1198,
    )
    solutions = _by_name(repaired["solutions"])
    vitamins = _by_name(solutions["Vitamin mixture"]["composition"])
    metals = _by_name(solutions["Metal mixture"]["composition"])
    seawater = _by_name(solutions["Artificial seawater"]["composition"])

    assert solutions["Vitamin mixture"]["concentration"] == {
        "value": "2.5",
        "unit": "ML_PER_L",
    }
    assert vitamins["Thiamine HCl"]["concentration"] == {
        "value": "200.0",
        "unit": "MG_PER_L",
    }
    assert metals["CuSO4 x 5H2O"]["term"] == {
        "id": "CHEBI:31440",
        "label": "copper(II) sulfate pentahydrate",
    }
    assert "term" not in metals["MnCl2 x 6H2O"]
    assert seawater["SrCl2 x 6H2O"]["concentration"] == {
        "value": "17.0",
        "unit": "MG_PER_L",
    }
    assert seawater["SrCl2 x 6H2O"]["term"] == {
        "id": "CHEBI:36385",
        "label": "strontium dichloride hexahydrate",
    }


def test_repair_record_drops_all_targets_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    parsed = []
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(repair_module, target), target)
        parsed.append((str(target.path), repaired))

        assert scorer_module.score_record(repaired) == (0, [])
        assert repaired["data_quality_flags"] == [
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        ]

    assert scorer_module.score_parsed(parsed) == []


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(
        _doc(repair_module, repair_module.M1198),
        repair_module.M1198,
    )
    twice = repair_module.repair_record(once, repair_module.M1198)

    assert twice["references"] == [
        {"reference": url} for url in repair_module._references(repair_module.M1198)
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
    assert matching_events[0]["source"] == "; ".join(
        repair_module._references(repair_module.M1198)
    )


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module, repair_module.M1192)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:007718"):
        repair_module.repair_record(doc, repair_module.M1192)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module, repair_module.M1198)
    doc["media_term"]["term"]["id"] = "TOGO:M1192"

    with pytest.raises(ValueError, match="expected media term TOGO:M1198"):
        repair_module.repair_record(doc, repair_module.M1198)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module, repair_module.M1192)
    doc["ingredients"][0] = _ingredient("Tap water", "1", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, repair_module.M1192)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module, repair_module.M1198)
    doc["solutions"][0] = _solution("Vitamin mixture (see Medium [M1196])", "3", "G_PER_L")

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, repair_module.M1198)
