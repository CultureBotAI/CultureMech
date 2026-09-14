from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m721_m722_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m721_m722_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_m721_m722")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": "mjy_medium_for_pyrolinea_marinus",
        "original_name": "MJY Medium For Pyrolinea Marinus",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in target.imported_ingredients
        ],
        "media_term": {
            "preferred_term": "source medium",
            "term": {"id": target.source_term, "label": "MJY"},
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _ingredient(name, value, unit) for name, value, unit in target.imported_solutions
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def _repair(repair_module, path: Path) -> dict:
    target = next(target for target in repair_module.TARGETS if target.path == path)
    return repair_module.repair_record(_doc(target), target)


def test_jcm_j700_becomes_canonical_nested_parent(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair(repair_module, repair_module.JCM_J700_PATH)

    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert (
        repair_module._signature(
            repaired["solutions"],
            "solutions",
        )
        == repair_module.FINAL_BASE_SOLUTION_SIGNATURE
    )
    assert repaired["ph_range"] == {"min": 6.0, "max": 6.5}
    assert "ph_value" not in repaired
    assert repaired["variant_children"] == [
        repair_module.M721_CHILD,
        repair_module.M722_CHILD,
    ]
    assert "parent_media" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_togo_m721_links_to_jcm_source_duplicate(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M721_PATH)

    assert repaired["parent_media"] == repair_module.JCM_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.M721_VARIANT_MODIFICATION]
    assert "variant_children" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_togo_m722_adds_rumen_fluid_as_supplement(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M722_PATH)

    assert (
        repair_module._signature(
            repaired["solutions"],
            "solutions",
        )
        == repair_module.FINAL_RUMEN_SOLUTION_SIGNATURE
    )
    assert repaired["solutions"][-1] == {
        "preferred_term": "Rumen fluid, clarified",
        "concentration": {"value": "20.0", "unit": "ML_PER_L"},
        "source": "TOGO M722 / TOGO M258 / JCM Medium 266",
        "notes": (
            "TOGO M722 adds 20.0 ml/L Rumen fluid, clarified from "
            "TOGO M258/JCM Medium 266 after cooling."
        ),
        "preparation_notes": (
            "TOGO M258/JCM Medium 266 prepares clarified rumen fluid by "
            "preheating rumen content at 120 C for 15 min and using the "
            "supernatant after centrifuging at 25,000 x g for 15 min."
        ),
    }
    assert repaired["parent_media"] == repair_module.JCM_SUPPLEMENT_PARENT
    assert repaired["variant_relationship"] == "SUPPLEMENTED_VARIANT"
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_expands_mj_n_seawater_and_percent_stocks(repair_module) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M721_PATH)
    solutions = _by_name(repaired["solutions"])
    seawater = _by_name(solutions["MJ(-N) synthetic seawater"]["composition"])
    bicarbonate = solutions["8% NaHCO3 solution"]["composition"][0]
    sulfide = solutions["5% Na2S x 9 H2O solution"]["composition"][0]

    assert seawater["NaCl"]["concentration"] == {"value": "30.0", "unit": "G_PER_L"}
    assert seawater["Na2SeO3 x 5 H2O"]["concentration"] == {
        "value": "0.5",
        "unit": "MG_PER_L",
    }
    assert seawater["Fe(NH4)2(SO4)2 x 6 H2O"]["term"] == {
        "id": "CHEBI:76181",
        "label": "ferrous ammonium sulfate hexahydrate",
    }
    assert "term" not in seawater["Trace minerals"]
    assert bicarbonate["concentration"] == {"value": "8.0", "unit": "PERCENT_W_V"}
    assert bicarbonate["physicochemical_roles"] == ["BUFFER"]
    assert sulfide["concentration"] == {"value": "5.0", "unit": "PERCENT_W_V"}
    assert sulfide["physicochemical_roles"] == ["REDUCING_AGENT"]


def test_repair_removes_gas_pseudo_ingredients(repair_module) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M722_PATH)
    ingredients = _by_name(repaired["ingredients"])
    descriptions = "\n".join(step["description"] for step in repaired["preparation_steps"])

    assert set(ingredients) == {"Yeast extract", "NH4Cl", "NaNO3"}
    assert "Carbon dioxide gas" not in ingredients
    assert "Nitrogen gas" not in ingredients
    assert "N2-CO2 (4:1, v/v)" in descriptions
    assert "200 kPa N2-CO2" in descriptions


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.TOGO_M722_PATH
    )
    once = repair_module.repair_record(_doc(target), target)
    twice = repair_module.repair_record(once, target)

    assert twice == once
    assert once["references"] == [{"reference": reference} for reference in target.references]
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair_module.CURATOR and event.get("action") == target.action
    ]
    assert len(matching_events) == 1
    assert "Rumen fluid, clarified" in matching_events[0]["notes"]


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.TOGO_M721_PATH
    )
    doc = _doc(target)
    doc["ingredients"].pop()

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_solution_drift(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.TOGO_M722_PATH
    )
    doc = _doc(target)
    doc["solutions"][0]["preferred_term"] = "synthetic seawater"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, target)
