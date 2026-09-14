from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2255_half_marine_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2255_half_marine")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2255_half_marine")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "strength_marine_medium",
        "original_name": "1/2 Strength Marine Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2255",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "1/2 Strength Marine Medium",
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "kg_microbe_match": "mediadive.medium:12",
    }


def _parent_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_PARENT_ID,
        "name": "marine_broth_2216",
        "original_name": "Marine Broth 2216",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [],
        "media_term": {
            "preferred_term": "TOGO Medium M33",
            "term": {
                "id": repair_module.EXPECTED_PARENT_MEDIA_TERM,
                "label": "Marine Broth 2216",
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "variant_children": [
            {
                "path": "data/normalized_yaml/bacterial/quarter_strength_marine_broth_2216.yaml",
                "relationship": "CONCENTRATION_VARIANT",
                "id": "CultureMech:007635",
                "name": "quarter_strength_marine_broth_2216",
                "notes": "existing child",
            }
        ],
    }


def test_repair_corrects_water_units_and_exits_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert (
        repair_module._signature(repaired["ingredients"], "ingredients")
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert "ph_range" not in repaired
    assert "kg_microbe_match" not in repaired
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_grounds_water_and_agar_but_keeps_marine_broth_opaque(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = {row["preferred_term"]: row for row in repaired["ingredients"]}

    assert ingredients[repair_module.WATER]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert ingredients[repair_module.AGAR]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert "term" not in ingredients[repair_module.MARINE_BROTH]


def test_repair_adds_parent_variant_link_and_source_metadata(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["parent_media"] == repair_module.PARENT_MEDIA
    assert twice["variant_relationship"] == "CONCENTRATION_VARIANT"
    assert twice["variant_modifications"] == [
        "Uses 18.7 g/L Marine Broth 2216 (BD 279110).",
        "Adds 15.0 g/L Agar if solid medium is needed.",
    ]
    assert [step["action"] for step in twice["preparation_steps"]] == [
        "MIX",
        "AUTOCLAVE",
    ]
    assert twice["sterilization"] == repair_module.STERILIZATION
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
    assert "DSMZ Soil Extract Medium" in matching_events[0]["notes"]


def test_repair_parent_adds_single_child_pointer(repair_module) -> None:
    parent = repair_module.repair_parent(_parent_doc(repair_module))
    twice = repair_module.repair_parent(parent)

    children = [
        child for child in twice["variant_children"] if child.get("id") == repair_module.EXPECTED_ID
    ]
    assert children == [repair_module.PARENT_CHILD]

    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.PARENT_ACTION
        )
    ]
    assert len(matching_events) == 1
    assert "optional agar" in matching_events[0]["notes"]


def test_plan_repairs_targets_child_and_parent_records(repair_module) -> None:
    target = repair_module.NORMALIZED / repair_module.TARGET
    parent = repair_module.NORMALIZED / repair_module.PARENT

    assert repair_module.plan_repairs() == {
        target: repair_module.repair_record(yaml.safe_load(target.read_text(encoding="utf-8"))),
        parent: repair_module.repair_parent(yaml.safe_load(parent.read_text(encoding="utf-8"))),
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M2256"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_imported_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("DI Water", "1000.0", "ML_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_kg_match(repair_module) -> None:
    doc = _doc(repair_module)
    doc["kg_microbe_match"] = "mediadive.medium:13"

    with pytest.raises(ValueError, match="unexpected kg_microbe_match"):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_parent_id(repair_module) -> None:
    parent = _parent_doc(repair_module)
    parent["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_PARENT_ID):
        repair_module.repair_parent(parent)


def test_repair_rejects_drifted_parent_child_pointer(repair_module) -> None:
    parent = _parent_doc(repair_module)
    parent["variant_children"].append(
        {
            **repair_module.PARENT_CHILD,
            "relationship": "SUPPLEMENTED_VARIANT",
        }
    )

    with pytest.raises(ValueError, match="child pointer drifted"):
        repair_module.repair_parent(parent)


def test_corpus_record_matches_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
