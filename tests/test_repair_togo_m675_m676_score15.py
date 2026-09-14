from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m675_m676_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m675_m676_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_m675_m676")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": "pelagicoccus_agar",
        "original_name": "Pelagicoccus Agar",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": target.physical_state,
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in target.imported_signature
        ],
        "media_term": {
            "preferred_term": "source medium",
            "term": {"id": target.source_term, "label": "Pelagicoccus Agar"},
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _togo_m676_doc(repair_module, target) -> dict:
    doc = _doc(target)
    doc["solutions"] = [
        _ingredient(name, value, unit) for name, value, unit in repair_module.IMPORTED_M676_SOLUTION
    ]
    return doc


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_jcm_659_restores_agar_formula_solution_and_children(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])
    artificial_seawater = repaired["solutions"][0]
    composition = _by_name(artificial_seawater["composition"])

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.AGAR_FINAL
    )
    assert "term" not in ingredients["Marine agar 2216 (BD-Difco)"]
    assert "mediaingredientmech_chebi_term" not in ingredients["R2A agar (BD-Difco)"]
    assert artificial_seawater["concentration"] == {
        "value": "750.0",
        "unit": "ML_PER_L",
    }
    assert artificial_seawater["culturemech_term"] == {
        "id": "CultureMech:013514",
        "label": "Artificial seawater",
    }
    assert composition["NaCl"]["term"] == {
        "id": "CHEBI:26710",
        "label": "sodium chloride",
    }
    assert repaired["variant_children"] == [
        repair_module.M675_CHILD,
        repair_module.M676_CHILD,
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_togo_m675_becomes_jcm_659_source_duplicate(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[1]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.AGAR_FINAL
    )
    assert repaired["solutions"][0]["preferred_term"] == "Artificial seawater"
    assert repaired["ph_value"] == 7.5
    assert repaired["parent_media"] == repair_module.JCM_J659_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.M675_VARIANT_MODIFICATION]
    assert scorer_module.score_record(repaired) == (0, [])


def test_togo_m676_becomes_jcm_659_liquid_variant(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[2]
    repaired = repair_module.repair_record(_togo_m676_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["physical_state"] == "LIQUID"
    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.LIQUID_FINAL
    )
    assert ingredients["Marine broth 2216 (BD-Difco)"]["concentration"] == {
        "value": "37.4",
        "unit": "G_PER_L",
    }
    assert repaired["solutions"][0]["composition"][0]["preferred_term"] == "NaCl"
    assert repaired["parent_media"] == repair_module.JCM_J659_LIQUID_PARENT
    assert repaired["variant_relationship"] == "PHYSICAL_STATE_VARIANT"
    assert repaired["variant_modifications"] == [repair_module.M676_VARIANT_MODIFICATION]
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_sets_shared_conditions_sterilization_and_flags(
    repair_module,
) -> None:
    target = repair_module.TARGETS[1]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert repaired["sterilization"] == repair_module.STERILIZATION
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    target = repair_module.TARGETS[2]
    once = repair_module.repair_record(_togo_m676_doc(repair_module, target), target)
    twice = repair_module.repair_record(once, target)

    assert twice == once
    assert once["references"] == [{"reference": reference} for reference in target.references]
    matching_events = [
        event
        for event in once["curation_history"]
        if event.get("curator") == repair_module.CURATOR and event.get("action") == target.action
    ]
    assert len(matching_events) == 1
    assert "empty Artificial seawater cross-reference" in matching_events[0]["notes"]


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[1]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[1]
    doc = _doc(target)
    doc["ingredients"].pop()

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)
