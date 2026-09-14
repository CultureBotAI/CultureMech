from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m455_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m455_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m455")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "alkali_reinforced_clostridial_agar",
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
            "preferred_term": "TOGO Medium M455",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
    }


def _parent_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_PARENT_ID,
        "name": "alkali_reinforced_clostridial_agar",
        "original_name": "ALKALI-REINFORCED CLOSTRIDIAL AGAR",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": 10.0,
        "media_term": {
            "preferred_term": "JCM Medium J455",
            "term": {
                "id": repair_module.EXPECTED_PARENT_MEDIA_TERM,
                "label": "ALKALI-REINFORCED CLOSTRIDIAL AGAR",
            },
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
                "description": (
                    "After autoclaving, aseptically add 100 ml of a 10% Na2CO3 "
                    "solution to the medium. Check final pH to be about 10.0."
                ),
            }
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "kg_microbe_match": "mediadive.medium:12",
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_formula_units_and_conditions(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["composition_type"] == "UNDEFINED"
    assert repaired["ph_value"] == 10.0
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "900.0",
        "unit": "ML_PER_L",
    }
    assert "term" not in ingredients["Reinforced clostridial agar (Sigma)"]
    assert "opaque complex component" in ingredients["Reinforced clostridial agar (Sigma)"]["notes"]


def test_repair_expands_sodium_carbonate_solution(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    carbonate = _by_name(solutions["10% Na2CO3 solution"]["composition"])

    assert (
        repair_module._solution_signatures(
            repaired["solutions"],
            "solutions",
        )
        == repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert carbonate["Na2CO3"]["concentration"] == {
        "value": "10.0",
        "unit": "PERCENT_W_V",
    }
    assert carbonate["Na2CO3"]["term"] == {
        "id": "CHEBI:29377",
        "label": "sodium carbonate",
    }


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
    assert twice["sterilization"] == repair_module.STERILIZATION
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
    assert "final pH is checked to be about 10.0" in matching_events[0]["notes"]


def test_repair_parent_updates_formula_and_links_child_once(
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
    assert (
        repair_module._solution_signatures(
            twice["solutions"],
            "solutions",
        )
        == repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert twice["variant_children"] == [repair_module.TOGO_CHILD]
    assert twice["references"] == [{"reference": url} for url in repair_module.REFERENCES]
    assert "kg_microbe_match" not in twice
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

    with pytest.raises(ValueError, match="expected CultureMech:009842"):
        repair_module.repair_target(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M382"

    with pytest.raises(ValueError, match="expected media term TOGO:M455"):
        repair_module.repair_target(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Water", "900", "G_PER_L")

    with pytest.raises(ValueError, match="target ingredient signature drifted"):
        repair_module.repair_target(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["concentration"] = {"value": "100", "unit": "ML_PER_L"}

    with pytest.raises(ValueError, match="target solution signature drifted"):
        repair_module.repair_target(doc)


def test_repair_parent_rejects_ingredient_drift(repair_module) -> None:
    doc = _parent_doc(repair_module)
    doc["ingredients"][0] = _ingredient("Reinforced clostridial agar", "51", "G_PER_L")

    with pytest.raises(ValueError, match="parent ingredient signature drifted"):
        repair_module.repair_parent(doc)


def test_repair_parent_rejects_unexpected_kg_microbe_match(repair_module) -> None:
    doc = _parent_doc(repair_module)
    doc["kg_microbe_match"] = "mediadive.medium:J455"

    with pytest.raises(ValueError, match="unexpected kg_microbe_match"):
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
