from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m3215_seed_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m3215_seed")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m3215_seed")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "seed_medium",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M3215",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_restores_togo_seed_signature(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert (
        repair_module._signature(repaired["ingredients"], "ingredients")
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "UNDEFINED"
    assert repaired["physical_state"] == "LIQUID"
    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_corrects_water_unit_and_keeps_trypton_opaque(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients[repair_module.WATER]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients[repair_module.WATER]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert "term" not in ingredients[repair_module.TRYPTON]
    assert "mediaingredientmech_chebi_term" not in ingredients[repair_module.TRYPTON]
    assert "source-spelled complex component" in ingredients[repair_module.TRYPTON]["notes"]


def test_repair_grounds_nonopaque_components(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients[repair_module.YEAST_EXTRACT]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients[repair_module.BEEF_EXTRACT]["term"] == {
        "id": "FOODON:03302088",
        "label": "beef extract",
    }
    assert ingredients[repair_module.NACL]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:26710",
        "label": "sodium chloride",
    }


def test_repair_adds_flags_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert "TOGO Medium M3215 lists Seed medium" in twice["notes"]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert "grounded yeast extract and beef extract" in matching_events[0]["notes"]


def test_plan_repairs_target_record(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET

    assert repair_module.plan_repairs() == {
        path: repair_module.repair_record(yaml.safe_load(path.read_text(encoding="utf-8")))
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M3233"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Tap water", "1", "L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"] = [
        {
            "preferred_term": "Nutrient stock",
            "concentration": {"value": "10", "unit": "ML_PER_L"},
            "composition": [],
        }
    ]

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_corpus_record_matches_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    signature = repair_module._signature(doc["ingredients"], "ingredients")

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert signature in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
