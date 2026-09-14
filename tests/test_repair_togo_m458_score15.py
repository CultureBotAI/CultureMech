from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m458_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m458_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m458")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "b_medium",
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
            "preferred_term": "TOGO Medium M458",
            "term": {"id": repair_module.EXPECTED_MEDIA_TERM, "label": repair_module.TITLE},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _parent_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_PARENT_ID,
        "name": "b_medium",
        "original_name": "B MEDIUM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": 7.7,
        "media_term": {
            "preferred_term": "JCM Medium J458",
            "term": {"id": repair_module.EXPECTED_PARENT_MEDIA_TERM, "label": "B MEDIUM"},
        },
        "notes": "Source: JCM",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_PARENT_INGREDIENT_SIGNATURE
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "ADJUST_PH",
                "description": "Adjust pH to 7.5 - 7.8.",
            }
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_formula_units_and_ph_range(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert "ph_value" not in repaired
    assert repaired["ph_range"] == repair_module.PH_RANGE
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "500.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Seawater"]["concentration"] == {
        "value": "500.0",
        "unit": "ML_PER_L",
    }


def test_repair_preserves_grounded_and_opaque_components(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["MgSO4 x 7H2O"]["term"] == {
        "id": "CHEBI:31795",
        "label": "magnesium sulfate heptahydrate",
    }
    assert ingredients["Bacto agar (BD-Difco)"]["term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert "term" not in ingredients["Casamino acids (BD-Difco)"]
    assert "term" not in ingredients["Bacto peptone (BD-Difco)"]
    assert "term" not in ingredients["Seawater"]


def test_repair_links_togo_record_to_jcm_duplicate(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert repaired["parent_media"] == repair_module.PARENT_MEDIA
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [
        repair_module.VARIANT_MODIFICATIONS,
    ]


def test_repair_adds_preparation_references_flags_and_event_once(
    repair_module,
    scorer_module,
) -> None:
    once = repair_module.repair_target(_doc(repair_module))
    twice = repair_module.repair_target(once)

    assert twice["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert twice["references"] == [{"reference": url} for url in repair_module.REFERENCES]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert scorer_module.score_record(twice) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), twice)]) == []

    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert "7.5-7.8" in matching_events[0]["notes"]


def test_repair_parent_adds_distilled_water_and_links_child_once(
    repair_module,
    scorer_module,
) -> None:
    once = repair_module.repair_parent(_parent_doc(repair_module))
    twice = repair_module.repair_parent(once)

    assert (
        repair_module._signature(
            twice["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert twice["variant_children"] == [repair_module.TOGO_CHILD]
    assert "ph_value" not in twice
    assert twice["ph_range"] == repair_module.PH_RANGE
    assert scorer_module.score_record(twice) == (0, [])

    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.PARENT_ACTION
        )
    ]
    assert len(matching_events) == 1


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected CultureMech:009845"):
        repair_module.repair_target(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M455"

    with pytest.raises(ValueError, match="expected media term TOGO:M458"):
        repair_module.repair_target(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Water", "500", "G_PER_L")

    with pytest.raises(ValueError, match="target ingredient signature drifted"):
        repair_module.repair_target(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"] = [{"preferred_term": "Unexpected solution"}]

    with pytest.raises(ValueError, match="target solution signature drifted"):
        repair_module.repair_target(doc)


def test_repair_parent_rejects_ingredient_drift(repair_module) -> None:
    doc = _parent_doc(repair_module)
    doc["ingredients"][0] = _ingredient("Bacto peptone (BD-Difco)", "2", "G_PER_L")

    with pytest.raises(ValueError, match="parent ingredient signature drifted"):
        repair_module.repair_parent(doc)


def test_target_records_match_repair_contract(repair_module) -> None:
    target = yaml.safe_load(
        (repair_module.NORMALIZED / repair_module.TARGET).read_text(encoding="utf-8")
    )
    parent = yaml.safe_load(
        (repair_module.NORMALIZED / repair_module.PARENT).read_text(encoding="utf-8")
    )

    assert target["id"] == repair_module.EXPECTED_ID
    assert parent["id"] == repair_module.EXPECTED_PARENT_ID
    assert repair_module._source_term_id(target) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._source_term_id(parent) == repair_module.EXPECTED_PARENT_MEDIA_TERM
    assert repair_module._signature(target["ingredients"], "ingredients") in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
    assert repair_module._signature(parent["ingredients"], "ingredients") in (
        repair_module.IMPORTED_PARENT_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
