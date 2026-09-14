from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2223_m2888_hayflick_broths_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2223_m2888_hayflick_broths_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_hayflick_broths")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    return {
        "id": target.expected_id,
        "name": target.path.stem,
        "original_name": target.title,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in target.imported_signature
        ],
        "media_term": {
            "preferred_term": (f"TOGO Medium {target.expected_media_term.removeprefix('TOGO:')}"),
            "term": {"id": target.expected_media_term, "label": target.title},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


@pytest.mark.parametrize("target_name", ["TARGET_M2223", "TARGET_M2888"])
def test_repair_normalizes_ml_l_and_condition_slots(
    repair_module,
    scorer_module,
    target_name: str,
) -> None:
    target = getattr(repair_module, target_name)
    repaired = repair_module.repair_record(_doc(target), target)

    assert (
        repair_module._signature(repaired["ingredients"], "ingredients") == target.final_signature
    )
    assert repaired["ph_value"] == 7.8
    assert repaired["temperature_value"] == 37.0
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(target.path), repaired)]) == []


def test_repair_grounds_horse_serum_variant(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module.TARGET_M2223),
        repair_module.TARGET_M2223,
    )
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["heat-inactivated horse serum"]["concentration"] == {
        "value": "200.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["heat-inactivated horse serum"]["term"] == {
        "id": "MICRO:0001235",
        "label": "Horse serum",
    }


def test_repair_keeps_fetal_bovine_serum_unmapped(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module.TARGET_M2888),
        repair_module.TARGET_M2888,
    )
    ingredients = _by_name(repaired["ingredients"])
    fetal_bovine_serum = ingredients["Fetal bovine serum (Flow), heat-inactivated"]

    assert "term" not in fetal_bovine_serum
    assert "mediaingredientmech_chebi_term" not in fetal_bovine_serum
    assert "NCIT:C113696" in fetal_bovine_serum["notes"]


@pytest.mark.parametrize("target_name", ["TARGET_M2223", "TARGET_M2888"])
def test_repair_grounds_common_machine_usable_components(
    repair_module,
    target_name: str,
) -> None:
    target = getattr(repair_module, target_name)
    repaired = repair_module.repair_record(_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients[target.glucose_name]["term"] == {
        "id": "CHEBI:17634",
        "label": "D-glucose",
    }
    assert ingredients[repair_module.YEAST]["term"] == {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    }
    assert ingredients[target.penicillin_name]["term"] == {
        "id": "CHEBI:51765",
        "label": "benzylpenicillin sodium",
    }


@pytest.mark.parametrize("target_name", ["TARGET_M2223", "TARGET_M2888"])
def test_repair_keeps_stock_solution_and_pplo_unmapped(
    repair_module,
    target_name: str,
) -> None:
    target = getattr(repair_module, target_name)
    repaired = repair_module.repair_record(_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])

    for name in (target.phenol_red_name, repair_module.PPLO_FINAL):
        assert "term" not in ingredients[name]
        assert "mediaingredientmech_chebi_term" not in ingredients[name]


@pytest.mark.parametrize("target_name", ["TARGET_M2223", "TARGET_M2888"])
def test_repair_adds_references_flags_and_event_once(
    repair_module,
    target_name: str,
) -> None:
    target = getattr(repair_module, target_name)
    once = repair_module.repair_record(_doc(target), target)
    twice = repair_module.repair_record(once, target)

    assert twice == once
    assert once["references"] == [{"reference": target.togo_url}]
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert "Corrected the imported ml/L and water units" in matching_events[0]["notes"]
