from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m684_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m684_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_m684")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(
    *,
    target,
    name: str = "ym_broth",
    original_name: str = "YM Broth",
) -> dict:
    return {
        "id": target.record_id,
        "name": name,
        "original_name": original_name,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in target.imported_signature
        ],
        "media_term": {
            "preferred_term": "source medium",
            "term": {"id": target.source_term, "label": original_name},
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "data_quality_flags": ["incomplete_composition", "resolved_reference"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def _repair(repair_module, path: Path) -> dict:
    target = next(target for target in repair_module.TARGETS if target.path == path)
    return repair_module.repair_target(_doc(target=target), target)


def test_jcm_parent_restores_recipe_and_links_togo_child(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair(repair_module, repair_module.JCM_J666_PATH)

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repaired["ph_value"] == 6.2
    assert repaired["variant_children"] == [repair_module.M684_CHILD]
    assert "parent_media" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_togo_m684_links_to_jcm_duplicate(repair_module, scorer_module) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M684_PATH)

    assert repaired["ph_value"] == 6.2
    assert repaired["parent_media"] == repair_module.JCM_J666_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.M684_VARIANT_MODIFICATION]
    assert "variant_children" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_nbrc_m1599_is_repaired_but_unlinked(repair_module, scorer_module) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M1599_PATH)

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert "ph_value" not in repaired
    assert "sterilization" not in repaired
    assert "parent_media" not in repaired
    assert "variant_relationship" not in repaired
    assert "variant_modifications" not in repaired
    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed([(str(repair_module.TOGO_M1599_PATH), repaired)]) == []


def test_repair_sets_groundings_roles_and_chebi_mirrors(repair_module) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M684_PATH)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Glucose"]["term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert ingredients["Glucose"]["nutritional_roles"] == ["CARBON_SOURCE"]
    assert ingredients["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "peptone",
    }
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients["Malt extract"]["term"] == {
        "id": "FOODON:03301056",
        "label": "malt extract",
    }
    assert ingredients["Malt extract"]["nutritional_roles"] == [
        "CARBON_SOURCE",
        "NITROGEN_SOURCE",
    ]
    assert "mediaingredientmech_chebi_term" not in ingredients["Peptone"]
    assert "mediaingredientmech_chebi_term" not in ingredients["Malt extract"]
    assert ingredients["Distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.JCM_J666_PATH
    )
    once = repair_module.repair_target(_doc(target=target), target)
    twice = repair_module.repair_target(once, target)

    assert twice == once
    assert once["references"] == [{"reference": reference} for reference in target.references]
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    matching_events = [
        event
        for event in once["curation_history"]
        if event.get("curator") == repair_module.CURATOR and event.get("action") == target.action
    ]
    assert len(matching_events) == 1
    assert "Distilled water" in matching_events[0]["notes"]


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(target=target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_target(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(target=target)
    doc["ingredients"].pop()

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_target(doc, target)
