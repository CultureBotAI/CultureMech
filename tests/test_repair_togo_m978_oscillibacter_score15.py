from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m978_oscillibacter_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m978_oscillibacter_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_m978")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def _media_doc(repair_module, *, togo: bool) -> dict:
    if togo:
        identifier = "CultureMech:010404"
        source_term = "TOGO:M978"
        ingredients = repair_module.TOGO_IMPORTED_INGREDIENTS
        solutions = repair_module.TOGO_IMPORTED_SOLUTIONS
    else:
        identifier = "CultureMech:003280"
        source_term = "mediadive.medium:J932"
        ingredients = repair_module.MEDIADIVE_J932_IMPORTED
        solutions = ()

    return {
        "id": identifier,
        "name": "oscillibacter_gh_medium",
        "original_name": "Oscillibacter GH Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [_component(*row) for row in ingredients],
        "solutions": [_component(*row) for row in solutions],
        "media_term": {
            "preferred_term": source_term,
            "term": {"id": source_term, "label": "Oscillibacter GH Medium"},
        },
        "notes": "Source",
        "curation_history": [],
    }


def _solution_doc(repair_module) -> dict:
    return {
        "id": "CultureMech:013869",
        "preferred_term": "Main sol. J932",
        "term": {"id": "mediadive.solution:4943", "label": "Main sol. J932"},
        "composition": [
            _component(*row) for row in repair_module.SOLUTION_4943_IMPORTED
        ],
        "ingredients": [_component("See source for composition", "variable", "VARIABLE")],
        "data_quality_flags": ["incomplete_composition"],
        "curation_history": [],
    }


def test_togo_m978_stocks_water_ph_and_n2_are_repaired(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[1]
    repaired = repair_module.repair_media_record(_media_doc(repair_module, togo=True), target)
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert repair_module._signature(
        repaired["ingredients"], "ingredients"
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert repair_module._signature(
        repaired["solutions"], "solutions"
    ) == repair_module.FINAL_SOLUTION_SIGNATURE
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "988.142",
        "unit": "ML_PER_L",
    }
    assert repaired["ph_value"] == 6.0
    assert "N2" not in ingredients
    assert solutions["Trace vitamins"]["composition"][-1]["preferred_term"] == (
        "Distilled water"
    )
    assert repaired["parent_media"]["relationship"] == "SOURCE_DUPLICATE"
    assert scorer_module.score_parsed([("bacterial/m978.yaml", repaired)]) == []


def test_mediadive_j932_flattened_stocks_are_nested(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_media_record(
        _media_doc(repair_module, togo=False), target
    )
    solutions = _by_name(repaired["solutions"])
    trace = _by_name(solutions["Trace element solution"]["composition"])

    assert repaired["variant_children"][0]["relationship"] == "SOURCE_DUPLICATE"
    assert solutions["FeCl2 solution"]["concentration"] == {
        "value": "0.988142",
        "unit": "ML_PER_L",
    }
    assert trace["CoCl2 x 6 H2O"] == {
        "preferred_term": "CoCl2 x 6 H2O",
        "concentration": {"value": "190.0", "unit": "MG_PER_L"},
        "source": "JCM Medium 187",
        "notes": "JCM Medium 187 lists 190.0 mg/L CoCl2 x 6 H2O.",
        "term": {
            "id": "CHEBI:53503",
            "label": "cobalt chloride hexahydrate",
        },
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:53503",
            "label": "cobalt chloride hexahydrate",
        },
        "nutritional_roles": ["TRACE_ELEMENT"],
    }


def test_mediadive_4943_main_solution_is_repaired(repair_module) -> None:
    repaired = repair_module.repair_solution_4943(_solution_doc(repair_module))

    assert repair_module._signature(
        repaired["composition"], "composition"
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert repair_module._signature(
        repaired["solutions"], "solutions"
    ) == repair_module.FINAL_SOLUTION_SIGNATURE
    assert repaired["composition"][3]["concentration"]["unit"] == "ML_PER_L"
    assert "ingredients" not in repaired
    assert "data_quality_flags" not in repaired


def test_repairs_are_idempotent(repair_module) -> None:
    for function, doc in (
        (
            lambda source: repair_module.repair_media_record(
                source, repair_module.TARGETS[0]
            ),
            _media_doc(repair_module, togo=False),
        ),
        (
            lambda source: repair_module.repair_media_record(
                source, repair_module.TARGETS[1]
            ),
            _media_doc(repair_module, togo=True),
        ),
        (repair_module.repair_solution_4943, _solution_doc(repair_module)),
    ):
        once = function(doc)
        twice = function(once)
        assert twice == once


def test_m978_rejects_wrong_source(repair_module) -> None:
    doc = _media_doc(repair_module, togo=True)
    doc["media_term"]["term"]["id"] = "TOGO:wrong"

    with pytest.raises(ValueError, match="TOGO:M978"):
        repair_module.repair_media_record(doc, repair_module.TARGETS[1])


def test_solution_4943_rejects_composition_drift(repair_module) -> None:
    doc = _solution_doc(repair_module)
    doc["composition"][0]["preferred_term"] = "Unknown"

    with pytest.raises(ValueError, match="solution 4943 composition signature drifted"):
        repair_module.repair_solution_4943(doc)
