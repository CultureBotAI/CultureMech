from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m379_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m379_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m379")


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
        "name": "glycerol_soil_medium",
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
            "preferred_term": "TOGO Medium M379",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _parent_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_PARENT_ID,
        "name": "glycerol_soil_medium",
        "original_name": "GLYCEROL-SOIL MEDIUM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": 7.0,
        "media_term": {
            "preferred_term": "JCM Medium J384",
            "term": {
                "id": repair_module.EXPECTED_PARENT_MEDIA_TERM,
                "label": "GLYCEROL-SOIL MEDIUM",
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


def test_repair_corrects_formula_and_water_units(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "UNDEFINED"
    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["ph_value"] == 7.0
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert ingredients["Tap water"]["concentration"] == {
        "value": "850.0",
        "unit": "ML_PER_L",
    }


def test_repair_moves_soil_extract_to_nested_solution(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    soil_extract = repaired["solutions"][0]
    composition = _by_name(soil_extract["composition"])

    assert (
        repair_module._solution_signatures(
            repaired["solutions"],
            "solutions",
        )
        == repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert soil_extract["concentration"] == {"value": "150.0", "unit": "ML_PER_L"}
    assert composition["Tap water"]["term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert "term" not in composition["Air-dried garden soil"]


def test_repair_keeps_source_disclosed_products_unmapped(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Glycerol"]["term"] == {
        "id": "CHEBI:17754",
        "label": "glycerol",
    }
    assert ingredients["Agar"]["term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert "term" not in ingredients["Bacto peptone (BD-Difco)"]
    assert "mediaingredientmech_chebi_term" not in ingredients["Beef extract (BD-Difco)"]


def test_repair_links_togo_record_to_jcm_duplicate(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert repaired["parent_media"] == repair_module.PARENT_MEDIA
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [
        repair_module.VARIANT_MODIFICATIONS,
    ]


def test_repair_adds_preparation_sterilization_references_and_flags(
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
    assert "moved Soil extract to a 150 ml/L nested solution" in matching_events[0]["notes"]


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
            and event.get("action") == repair_module.LINK_ACTION
        )
    ]
    assert len(matching_events) == 1


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
    doc["ingredients"][1] = _ingredient("Tap water", "850.0", "ML_PER_L")

    with pytest.raises(ValueError, match="target ingredient signature drifted"):
        repair_module.repair_target(doc)


def test_repair_rejects_parent_ingredient_drift(repair_module) -> None:
    doc = _parent_doc(repair_module)
    doc["ingredients"][3] = _ingredient("Soil extract", "150.0", "ML_PER_L")

    with pytest.raises(ValueError, match="parent ingredient signature drifted"):
        repair_module.repair_parent(doc)


def test_parent_record_matches_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.PARENT
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_PARENT_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_PARENT_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in (
        repair_module.IMPORTED_PARENT_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
    assert repair_module._solution_signatures(doc.get("solutions"), "solutions") in (
        (),
        repair_module.FINAL_SOLUTION_SIGNATURES,
    )


def test_target_record_matches_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
    assert repair_module._solution_signatures(doc.get("solutions"), "solutions") in (
        (),
        repair_module.FINAL_SOLUTION_SIGNATURES,
    )
