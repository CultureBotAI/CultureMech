from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2578_spiroplasma_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2578_spiroplasma")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2578_spiroplasma")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(signature) -> dict:
    name, value, unit, composition = signature
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "composition": [
            _ingredient(component, amount, component_unit)
            for component, amount, component_unit in composition
        ],
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "spiroplasma_medium",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2578",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(signature) for signature in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_units_stocks_and_exits_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["ph_range"] == {"min": 7.25, "max": 7.45}
    assert (
        repair_module._signature(repaired["ingredients"], "ingredients")
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repair_module._solution_signatures(repaired) == (repair_module.FINAL_SOLUTION_SIGNATURES)
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_grounds_defined_components_and_keeps_opaque_inputs(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])
    mgs_components = _by_name(solutions[repair_module.MGS_STOCK]["composition"])
    yeast_components = _by_name(solutions[repair_module.YEAST_EXTRACT_STOCK]["composition"])

    assert ingredients[repair_module.AGAR]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert ingredients[repair_module.TRYPTONE]["term"] == {
        "id": "MICRO:0000182",
        "label": "Tryptone",
    }
    assert ingredients[repair_module.FBS]["term"] == {
        "id": "mediadive.compound:954",
        "label": "Fetal bovine serum",
    }
    assert mgs_components[repair_module.CMRL]["term"] == {
        "id": "mediadive.compound:1680",
        "label": "CMRL 1066",
    }
    assert "term" not in ingredients[repair_module.PPLO]
    assert (
        "term"
        not in _by_name(solutions[repair_module.TC_YEASTOLATE_STOCK]["composition"])[
            repair_module.TC_YEASTOLATE
        ]
    )
    assert "term" not in yeast_components[repair_module.BAKERS_YEAST]


def test_repair_restores_declared_cmrl_and_yeast_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    mgs_components = _by_name(solutions[repair_module.MGS_STOCK]["composition"])
    yeast_components = _by_name(solutions[repair_module.YEAST_EXTRACT_STOCK]["composition"])

    assert mgs_components[repair_module.MGS_WATER]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert mgs_components[repair_module.CMRL]["concentration"] == {
        "value": "98.0",
        "unit": "G_PER_L",
    }
    assert yeast_components[repair_module.YEAST_WATER]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert yeast_components[repair_module.BAKERS_YEAST]["concentration"] == {
        "value": "250.0",
        "unit": "G_PER_L",
    }


def test_repair_adds_references_flags_and_single_event(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["sterilization"] == repair_module.STERILIZATION
    assert [step["action"] for step in twice["preparation_steps"]] == [
        "MIX",
        "ADJUST_PH",
        "AUTOCLAVE",
        "FILTER_STERILIZE",
        "MIX",
    ]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
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
    assert "Mycoplasma Growth Supplement" in matching_events[0]["notes"]


def test_plan_repairs_targets_spiroplasma_record(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET

    assert repair_module.plan_repairs() == {
        path: repair_module.repair_record(yaml.safe_load(path.read_text(encoding="utf-8")))
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M2579"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_imported_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Deionized water", "700.0", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["concentration"] = {"value": "20.0", "unit": "ML_PER_L"}

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_corpus_record_matches_repair_contract(repair_module) -> None:
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
