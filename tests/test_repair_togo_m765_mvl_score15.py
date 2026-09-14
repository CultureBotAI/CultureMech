from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m765_mvl_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m765_mvl_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_m765")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": "mvl_medium",
        "original_name": "MVL Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_ingredients
        ],
        "media_term": {
            "preferred_term": "source medium",
            "term": {"id": target.source_term, "label": "MVL"},
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_solutions
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def _repair(repair_module, path: Path) -> dict:
    target = next(target for target in repair_module.TARGETS if target.path == path)
    return repair_module.repair_record(_doc(target), target)


def test_jcm_j740_becomes_canonical_nested_parent(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair(repair_module, repair_module.JCM_J740_PATH)

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert repair_module._signature(
        repaired["solutions"],
        "solutions",
    ) == repair_module.FINAL_SOLUTION_SIGNATURE
    assert repaired["variant_children"] == [repair_module.M765_CHILD]
    assert "parent_media" not in repaired
    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])


def test_togo_m765_links_to_jcm_source_duplicate(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M765_PATH)

    assert repaired["parent_media"] == repair_module.J740_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.J740_PARENT["notes"]]
    assert "variant_children" not in repaired
    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])


def test_repair_scales_main_solution_and_nests_percent_stocks(
    repair_module,
) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M765_PATH)
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "819.001",
        "unit": "ML_PER_L",
    }
    assert solutions["Mineral solution 1"]["concentration"] == {
        "value": "61.4251",
        "unit": "ML_PER_L",
    }
    assert solutions["Mineral solution 2"]["concentration"] == {
        "value": "61.4251",
        "unit": "ML_PER_L",
    }
    assert solutions["0.1% Resazurin solution"]["concentration"] == {
        "value": "0.819001",
        "unit": "ML_PER_L",
    }
    assert solutions["8% Na2CO3 solution"]["concentration"] == {
        "value": "40.95",
        "unit": "ML_PER_L",
    }
    assert solutions["3% L-Cysteine HCl x H2O solution"]["composition"][0] == {
        "preferred_term": "L-Cysteine HCl x H2O",
        "concentration": {"value": "3.0", "unit": "PERCENT_W_V"},
        "source": "TOGO M765 / JCM Medium 740",
        "notes": (
            "TOGO M765 / JCM Medium 740 specifies "
            "3% L-Cysteine HCl x H2O solution as 3.0% w/v."
        ),
        "term": {
            "id": "CHEBI:91248",
            "label": "L-cysteine hydrochloride hydrate",
        },
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:91248",
            "label": "L-cysteine hydrochloride hydrate",
        },
        "physicochemical_roles": ["REDUCING_AGENT"],
    }


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    target = next(
        target
        for target in repair_module.TARGETS
        if target.path == repair_module.TOGO_M765_PATH
    )
    once = repair_module.repair_record(_doc(target), target)
    twice = repair_module.repair_record(once, target)

    assert twice == once
    assert once["references"] == [
        {"reference": reference} for reference in target.references
    ]
    assert once["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair_module.CURATOR
        and event.get("action") == target.action
    ]
    assert len(matching_events) == 1
    assert "MediaDive J740" in matching_events[0]["notes"]


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = next(
        target
        for target in repair_module.TARGETS
        if target.path == repair_module.TOGO_M765_PATH
    )
    doc = _doc(target)
    doc["ingredients"].pop()

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_solution_drift(repair_module) -> None:
    target = next(
        target
        for target in repair_module.TARGETS
        if target.path == repair_module.TOGO_M765_PATH
    )
    doc = _doc(target)
    doc["solutions"][0]["preferred_term"] = "sodium carbonate"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, target)
