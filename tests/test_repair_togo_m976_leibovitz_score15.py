from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m976_leibovitz_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m976_leibovitz_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_m976")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _media_doc(repair_module, *, togo: bool) -> dict:
    if togo:
        identifier = "CultureMech:010402"
        term_id = "TOGO:M976"
        signature = repair_module.TOGO_IMPORTED
    else:
        identifier = "CultureMech:003278"
        term_id = "mediadive.medium:J930"
        signature = repair_module.J930_IMPORTED

    return {
        "id": identifier,
        "name": "leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl",
        "original_name": "Leibovitz's L-15 Medium With 10% FBS And 1.5% NaCl",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [_component(*row) for row in signature],
        "media_term": {
            "preferred_term": term_id,
            "term": {"id": term_id, "label": "Leibovitz L-15 FBS"},
        },
        "notes": "Source",
        "kg_microbe_match": "mediadive.medium:74",
        "curation_history": [],
    }


def _solution_doc(repair_module) -> dict:
    return {
        "id": "CultureMech:013867",
        "preferred_term": "Main sol. J930",
        "term": {"id": "mediadive.solution:4941", "label": "Main sol. J930"},
        "composition": [_component(*row) for row in repair_module.SOLUTION_IMPORTED],
        "ingredients": [_component("See source for composition", "variable", "VARIABLE")],
        "data_quality_flags": ["incomplete_composition"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_togo_m976_units_groundings_and_parent_are_repaired(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_togo(_media_doc(repair_module, togo=True))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(
        repaired["ingredients"], "ingredients"
    ) == repair_module.FINAL_SIGNATURE
    assert ingredients["Leibovitz's L-15 medium"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients["Fetal bovine serum"]["term"] == {
        "id": "mediadive.compound:954",
        "label": "Fetal bovine serum",
    }
    assert "kg_microbe_match" not in repaired
    assert repaired["sterilization"] == {
        "method": "FILTER",
        "notes": "0.22 um PES filter",
    }
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["parent_media"]["relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert scorer_module.score_parsed([("bacterial/m976.yaml", repaired)]) == []


def test_mediadive_j930_units_groundings_and_child_are_repaired(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_j930(_media_doc(repair_module, togo=False))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(
        repaired["ingredients"], "ingredients"
    ) == repair_module.FINAL_SIGNATURE
    assert ingredients["NaCl"]["concentration"] == {
        "value": "15.0",
        "unit": "G_PER_L",
    }
    assert repaired["variant_children"][0]["relationship"] == "SOURCE_DUPLICATE"
    assert scorer_module.score_parsed([("bacterial/j930.yaml", repaired)]) == []


def test_mediadive_4941_solution_is_repaired(repair_module) -> None:
    repaired = repair_module.repair_solution(_solution_doc(repair_module))
    components = _by_name(repaired["composition"])

    assert repair_module._signature(
        repaired["composition"], "composition"
    ) == repair_module.FINAL_SIGNATURE
    assert components["NaCl"]["chebi_term"] == {
        "id": "CHEBI:26710",
        "label": "sodium chloride",
    }
    assert "ingredients" not in repaired
    assert "data_quality_flags" not in repaired


def test_repairs_are_idempotent(repair_module) -> None:
    for function, doc in (
        (repair_module.repair_togo, _media_doc(repair_module, togo=True)),
        (repair_module.repair_j930, _media_doc(repair_module, togo=False)),
        (repair_module.repair_solution, _solution_doc(repair_module)),
    ):
        once = function(doc)
        twice = function(once)
        assert twice == once


def test_m976_rejects_wrong_source(repair_module) -> None:
    doc = _media_doc(repair_module, togo=True)
    doc["media_term"]["term"]["id"] = "TOGO:wrong"

    with pytest.raises(ValueError, match="TOGO:M976"):
        repair_module.repair_togo(doc)


def test_solution_rejects_composition_drift(repair_module) -> None:
    doc = _solution_doc(repair_module)
    doc["composition"][0]["preferred_term"] = "Unknown"

    with pytest.raises(ValueError, match="solution composition signature drifted"):
        repair_module.repair_solution(doc)
