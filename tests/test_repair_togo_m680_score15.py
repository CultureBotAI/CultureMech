from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m680_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m680_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_m680")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(
    *,
    record_id: str,
    media_term: str,
    signature: tuple[tuple[str, str, str], ...],
) -> dict:
    return {
        "id": record_id,
        "name": "mbg_20",
        "original_name": "MBG-20",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [_ingredient(name, value, unit) for name, value, unit in signature],
        "media_term": {
            "preferred_term": "source medium",
            "term": {"id": media_term, "label": "MBG-20"},
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "data_quality_flags": ["incomplete_composition", "resolved_reference"],
        "curation_history": [],
    }


def _togo_doc(repair_module) -> dict:
    return _doc(
        record_id=repair_module.EXPECTED_ID,
        media_term=repair_module.EXPECTED_MEDIA_TERM,
        signature=repair_module.IMPORTED_INGREDIENT_SIGNATURE,
    )


def _parent_doc(repair_module) -> dict:
    return _doc(
        record_id=repair_module.EXPECTED_PARENT_ID,
        media_term=repair_module.EXPECTED_PARENT_MEDIA_TERM,
        signature=repair_module.IMPORTED_PARENT_INGREDIENT_SIGNATURE,
    )


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_togo_m680_adds_jcm_formula_and_parent(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_togo(_togo_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repaired["ph_value"] == 7.0
    assert ingredients["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "peptone",
    }
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert "term" not in ingredients["Sea salts (Sigma)"]
    assert repaired["parent_media"] == repair_module.PARENT_MEDIA
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_parent_adds_distilled_water_and_child(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_parent(_parent_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert repaired["variant_children"] == [repair_module.TOGO_CHILD]
    assert "parent_media" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_keeps_split_sterilization_in_preparation_steps(
    repair_module,
) -> None:
    repaired = repair_module.repair_togo(_togo_doc(repair_module))

    assert repaired["preparation_steps"] == [dict(step) for step in repair_module.PREPARATION_STEPS]
    assert [step["action"] for step in repaired["preparation_steps"]] == [
        "ADJUST_PH",
        "DISSOLVE",
        "FILTER_STERILIZE",
        "AUTOCLAVE",
        "MIX",
        "MIX",
    ]
    assert "sterilization" not in repaired


def test_repair_sets_flags_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_togo(_togo_doc(repair_module))
    twice = repair_module.repair_togo(once)

    assert twice == once
    assert once["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
    ]
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    matching_events = [
        event
        for event in once["curation_history"]
        if event.get("curator") == repair_module.CURATOR
        and event.get("action") == repair_module.ACTION
    ]
    assert len(matching_events) == 1
    assert "distilled-water unit" in matching_events[0]["notes"]


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _togo_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_togo(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _togo_doc(repair_module)
    doc["ingredients"].pop()

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_togo(doc)
