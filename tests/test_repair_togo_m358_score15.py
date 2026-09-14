from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m358_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m358_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m358")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str, composition: list[dict] | None = None) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "composition": list(composition or []),
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "py4sr_agar",
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
            "preferred_term": "TOGO Medium M358",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit, list(composition))
            for name, value, unit, composition in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
    }


def _parent_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_PARENT_ID,
        "name": "py4s_agar",
        "original_name": "PY4S AGAR",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": 6.7,
        "media_term": {
            "preferred_term": "JCM Medium J363",
            "term": {
                "id": repair_module.EXPECTED_PARENT_MEDIA_TERM,
                "label": "PY4S AGAR",
            },
        },
        "notes": "Source: JCM",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_PARENT_INGREDIENT_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit, list(composition))
            for name, value, unit, composition in repair_module.IMPORTED_PARENT_SOLUTION_SIGNATURES
        ],
        "variant_children": [
            {
                "path": "data/normalized_yaml/bacterial/xylanobacter_medium.yaml",
                "relationship": "PH_VARIANT",
                "id": "CultureMech:002873",
                "name": "xylanobacter_medium",
                "notes": "Adjusts PY4S Agar from JCM Medium 363 to pH 6.0.",
            },
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_represents_py4sr_as_plant_extract_supplement(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    plant_extract = repaired["solutions"][0]
    components = _by_name(plant_extract["composition"])

    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["ph_value"] == 6.7
    assert repaired["ingredients"] == []
    assert (
        repair_module._solution_signatures(
            repaired["solutions"],
            "solutions",
        )
        == repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert plant_extract["concentration"] == {"value": "50.0", "unit": "ML_PER_L"}
    assert "term" not in components["Rice straw"]
    assert components["Distilled water"]["term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }


def test_repair_links_py4sr_to_py4s_parent(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert repaired["parent_media"] == repair_module.PARENT_MEDIA
    assert repaired["variant_relationship"] == "SUPPLEMENTED_VARIANT"
    assert repaired["variant_modifications"] == [
        repair_module.VARIANT_MODIFICATIONS,
    ]


def test_repair_py4sr_adds_references_preparation_and_flags(
    repair_module,
    scorer_module,
) -> None:
    once = repair_module.repair_target(_doc(repair_module))
    twice = repair_module.repair_target(once)

    assert twice["references"] == [{"reference": url} for url in repair_module.TARGET_REFERENCES]
    assert twice["preparation_steps"] == list(repair_module.TARGET_PREPARATION_STEPS)
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
    assert "50 ml/L supplement" in matching_events[0]["notes"]


def test_repair_parent_restores_jcm_363_formula(repair_module) -> None:
    repaired = repair_module.repair_parent(_parent_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["ph_value"] == 6.7
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_PARENT_INGREDIENT_SIGNATURE
    )
    assert ingredients["Trypticase peptone (BD-BBL)"]["concentration"] == {
        "value": "10.0",
        "unit": "G_PER_L",
    }
    assert ingredients["Bacto agar (BD-Difco)"]["term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "850.0",
        "unit": "ML_PER_L",
    }


def test_repair_parent_expands_stock_solutions(repair_module) -> None:
    repaired = repair_module.repair_parent(_parent_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    salt_i = _by_name(solutions["Salt Solution I"]["composition"])
    salt_ii = _by_name(solutions["Salt Solution II"]["composition"])
    resazurin = _by_name(solutions["0.1% (w/v) resazurin-Na"]["composition"])
    carbonate = _by_name(solutions["8% (w/v) Na2CO3"]["composition"])

    assert (
        repair_module._solution_signatures(
            repaired["solutions"],
            "solutions",
        )
        == repair_module.FINAL_PARENT_SOLUTION_SIGNATURES
    )
    assert solutions["Salt Solution I"]["concentration"] == {
        "value": "75.0",
        "unit": "ML_PER_L",
    }
    assert salt_i["K2HPO4"]["term"] == {
        "id": "CHEBI:131527",
        "label": "dipotassium hydrogen phosphate",
    }
    assert salt_ii["CaCl2"]["term"] == {
        "id": "CHEBI:3312",
        "label": "calcium dichloride",
    }
    assert "term" not in salt_ii["MgSO4 x H2O"]
    assert resazurin["Sodium resazurin"]["concentration"] == {
        "value": "1.0",
        "unit": "G_PER_L",
    }
    assert carbonate["Na2CO3"]["concentration"] == {
        "value": "80.0",
        "unit": "G_PER_L",
    }


def test_repair_parent_links_togo_child_once(repair_module) -> None:
    once = repair_module.repair_parent(_parent_doc(repair_module))
    twice = repair_module.repair_parent(once)

    assert twice["variant_children"] == [
        {
            "path": "data/normalized_yaml/bacterial/xylanobacter_medium.yaml",
            "relationship": "PH_VARIANT",
            "id": "CultureMech:002873",
            "name": "xylanobacter_medium",
            "notes": "Adjusts PY4S Agar from JCM Medium 363 to pH 6.0.",
        },
        repair_module.TOGO_CHILD,
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.LINK_ACTION
        )
    ]
    assert len(matching_events) == 1


def test_repair_parent_adds_quality_metadata_and_scores_zero(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_parent(_parent_doc(repair_module))

    assert repaired["preparation_steps"] == list(repair_module.PARENT_PREPARATION_STEPS)
    assert repaired["sterilization"] == repair_module.PARENT_STERILIZATION
    assert repaired["references"] == [{"reference": url} for url in repair_module.PARENT_REFERENCES]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_rejects_wrong_target_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_target(doc)


def test_repair_rejects_wrong_target_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_target(doc)


def test_repair_rejects_target_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Plant residue extract", "50.0", "ML_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_target(doc)


def test_repair_rejects_target_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0] = _solution("Plant residue extract", "50.0", "ML_PER_L")

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_target(doc)


def test_repair_rejects_wrong_parent_id(repair_module) -> None:
    doc = _parent_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_PARENT_ID):
        repair_module.repair_parent(doc)


def test_parent_record_matches_py4s_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.PARENT
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_PARENT_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_PARENT_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in (
        repair_module.IMPORTED_PARENT_INGREDIENT_SIGNATURE,
        repair_module.FINAL_PARENT_INGREDIENT_SIGNATURE,
    )
    assert repair_module._solution_signatures(doc["solutions"], "solutions") in (
        repair_module.IMPORTED_PARENT_SOLUTION_SIGNATURES,
        repair_module.FINAL_PARENT_SOLUTION_SIGNATURES,
    )


def test_target_record_matches_togo_m358_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        (),
    )
    assert repair_module._solution_signatures(doc["solutions"], "solutions") in (
        repair_module.IMPORTED_SOLUTION_SIGNATURES,
        repair_module.FINAL_SOLUTION_SIGNATURES,
    )
