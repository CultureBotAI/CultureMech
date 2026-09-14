from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m382_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m382_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m382")


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
        "name": "pygv_agar",
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
            "preferred_term": "TOGO Medium M382",
            "term": {"id": repair_module.EXPECTED_MEDIA_TERM, "label": repair_module.TITLE},
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
        "name": "pygv_agar",
        "original_name": "PYGV AGAR",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": 7.5,
        "media_term": {
            "preferred_term": "JCM Medium J387",
            "term": {
                "id": repair_module.EXPECTED_PARENT_MEDIA_TERM,
                "label": "PYGV AGAR",
            },
        },
        "notes": "Source: JCM",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_PARENT_INGREDIENT_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_formula_and_conditions(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert repaired["ph_value"] == 7.5
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "960.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["KOH"]["term"] == {
        "id": "CHEBI:32035",
        "label": "potassium hydroxide",
    }
    assert ingredients["KOH"]["notes"] == (
        "JCM Medium 387 adjusts the medium to pH 7.5 with sterile KOH, if necessary."
    )


def test_repair_expands_jcm_304_solutions(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    mineral = _by_name(solutions["Mineral salt solution"]["composition"])
    glucose = _by_name(solutions["2.5% Glucose solution"]["composition"])

    assert (
        repair_module._solution_signatures(
            repaired["solutions"],
            "solutions",
        )
        == repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert mineral["FeSO4 x 7H2O"]["concentration"] == {
        "value": "99.0",
        "unit": "MG_PER_L",
    }
    assert "term" not in mineral["Metals 44"]
    assert glucose["Glucose"]["term"] == {"id": "CHEBI:17234", "label": "glucose"}


def test_repair_expands_jcm_304_vitamins(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    vitamins = _by_name(_by_name(repaired["solutions"])["Vitamin solution"]["composition"])

    assert vitamins["Vitamin B12"]["concentration"] == {
        "value": "0.1",
        "unit": "MG_PER_L",
    }
    assert vitamins["Pyridoxine HCl"]["term"] == {
        "id": "CHEBI:30961",
        "label": "pyridoxine hydrochloride",
    }
    assert vitamins["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
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
    assert twice["references"] == [{"reference": url} for url in repair_module.TARGET_REFERENCES]
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
    assert "final pH is 7.5" in matching_events[0]["notes"]


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
    assert twice["references"] == [{"reference": url} for url in repair_module.PARENT_REFERENCES]
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

    with pytest.raises(ValueError, match="expected CultureMech:009763"):
        repair_module.repair_target(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M379"

    with pytest.raises(ValueError, match="expected media term TOGO:M382"):
        repair_module.repair_target(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Water", "960", "G_PER_L")

    with pytest.raises(ValueError, match="target ingredient signature drifted"):
        repair_module.repair_target(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["concentration"] = {"value": "10", "unit": "ML_PER_L"}

    with pytest.raises(ValueError, match="target solution signature drifted"):
        repair_module.repair_target(doc)


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
