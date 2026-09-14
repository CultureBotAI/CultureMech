from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1200_m1204_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m1200_m1204_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1200_m1204")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
    }


def _doc(repair_module, target) -> dict:
    return {
        "id": target.record_id,
        "name": target.title.lower().replace(" ", "_"),
        "original_name": target.title,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module._imported_ingredient_signature(target)
        ],
        "media_term": {
            "preferred_term": f"TOGO Medium {target.media_term.removeprefix('TOGO:')}",
            "term": {"id": target.media_term, "label": target.title},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in repair_module._imported_solution_signatures(target)
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_m1200_expands_brackish_medium_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.M1200),
        repair_module.M1200,
    )

    assert repaired["medium_type"] == "DEFINED"
    assert repaired["composition_type"] == "DEFINED"

    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])
    selenite = _by_name(solutions["Selenite-tungstate solution"]["composition"])
    trace = _by_name(solutions["Trace element solution"]["composition"])

    assert "Nitrogen gas" not in ingredients
    assert ingredients["NaCl"]["concentration"] == {
        "value": "12.8586",
        "unit": "G_PER_L",
    }
    assert ingredients["Resazurin"]["concentration"] == {
        "value": "0.98912",
        "unit": "MG_PER_L",
    }
    assert solutions["1 M MgCl2 x 6H2O solution"]["concentration"] == {
        "value": "15.0",
        "unit": "ML_PER_L",
    }
    assert selenite["Na2SeO3 x 5H2O"]["term"] == {
        "id": "CHEBI:131361",
        "label": "disodium selenite pentahydrate",
    }
    assert "term" not in trace["NiCl2 x 6H2O"]


def test_repair_m1202_uses_freshwater_i_fructose(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.M1202),
        repair_module.M1202,
    )

    solutions = _by_name(repaired["solutions"])
    fructose = _by_name(solutions["1 M Fructose solution"]["composition"])

    assert solutions["1 M MgCl2 x 6H2O solution"]["concentration"] == {
        "value": "2.5",
        "unit": "ML_PER_L",
    }
    assert solutions["1 M CaCl2 x 2H2O solution"]["concentration"] == {
        "value": "1.0",
        "unit": "ML_PER_L",
    }
    assert fructose["Fructose"]["concentration"] == {
        "value": "1.0",
        "unit": "MOLAR",
    }
    assert fructose["Fructose"]["term"]["id"] == "CHEBI:28757"


def test_repair_m1203_expands_complex_glycerin_variant(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.M1203),
        repair_module.M1203,
    )

    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "SEMI_DEFINED"

    solutions = _by_name(repaired["solutions"])
    yeast = _by_name(solutions["10% Yeast extract solution"]["composition"])
    glycerin = _by_name(solutions["1 M Glycerin solution"]["composition"])

    assert yeast["Yeast extract"]["concentration"] == {
        "value": "100.0",
        "unit": "G_PER_L",
    }
    assert "term" not in yeast["Yeast extract"]
    assert glycerin["Glycerol"]["term"] == {
        "id": "CHEBI:17754",
        "label": "glycerol",
    }


def test_repair_m1204_uses_sodium_lactate_substitution(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.M1204),
        repair_module.M1204,
    )

    solutions = _by_name(repaired["solutions"])
    assert "1 M Glycerin solution" not in solutions

    lactate = _by_name(solutions["1 M sodium lactate solution"]["composition"])
    assert lactate["Sodium lactate"]["term"] == {
        "id": "CHEBI:75228",
        "label": "sodium lactate",
    }


def test_repair_expands_m401_vitamin_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.M1200),
        repair_module.M1200,
    )
    solutions = _by_name(repaired["solutions"])
    vitamins = _by_name(solutions["Vitamin solution"]["composition"])
    thiamine = _by_name(solutions["Thiamine solution"]["composition"])
    b12 = _by_name(solutions["Vitamin B12 solution"]["composition"])

    assert vitamins["p-Aminobenzoic acid"]["concentration"] == {
        "value": "40.0",
        "unit": "MG_PER_L",
    }
    assert thiamine["Thiamine HCl"]["concentration"] == {
        "value": "100.0",
        "unit": "MG_PER_L",
    }
    assert b12["Vitamin B12"]["concentration"] == {
        "value": "50.0",
        "unit": "MG_PER_L",
    }


def test_repair_record_drops_all_targets_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    parsed = []
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(repair_module, target), target)
        parsed.append((str(target.path), repaired))

        assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
        assert repaired["data_quality_flags"] == [
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        ]

    assert scorer_module.score_parsed(parsed) == []


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(
        _doc(repair_module, repair_module.M1204),
        repair_module.M1204,
    )
    twice = repair_module.repair_record(once, repair_module.M1204)

    assert twice["references"] == [
        {"reference": url} for url in repair_module._references(repair_module.M1204)
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
        repair_module._references(repair_module.M1204)
    )


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module, repair_module.M1200)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:007727"):
        repair_module.repair_record(doc, repair_module.M1200)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module, repair_module.M1202)
    doc["media_term"]["term"]["id"] = "TOGO:M1200"

    with pytest.raises(ValueError, match="expected media term TOGO:M1202"):
        repair_module.repair_record(doc, repair_module.M1202)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module, repair_module.M1203)
    doc["ingredients"][0] = _ingredient("Tap water", "1", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, repair_module.M1203)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module, repair_module.M1204)
    doc["solutions"][0] = _solution("FeCl2 solution", "3", "G_PER_L")

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, repair_module.M1204)
