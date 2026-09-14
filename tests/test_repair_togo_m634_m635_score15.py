from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m634_m635_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m634_m635_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_m634_m635")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": "modified_thermus_medium_with_3_nacl",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.8,
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_signature
        ],
        "media_term": {
            "preferred_term": "source medium",
            "term": {
                "id": target.source_term,
                "label": "MODIFIED THERMUS MEDIUM WITH 3% NaCl",
            },
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "data_quality_flags": ["incomplete_composition", "resolved_reference"],
        "curation_history": [],
    }


def _togo_doc(repair_module, target) -> dict:
    doc = _doc(target)
    doc["solutions"] = [
        _ingredient(name, value, unit)
        for name, value, unit in repair_module.IMPORTED_SOLUTION
    ]
    return doc


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_jcm_624_inlines_castenholz_solution_and_children(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(target), target)
    solutions = _by_name(repaired["solutions"])
    castenholz = solutions["Castenholz basal salt solution (see Medium No. 273)"]
    composition = _by_name(castenholz["composition"])

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.BASE_FINAL
    )
    assert castenholz["concentration"] == {"value": "10.0", "unit": "ML_PER_L"}
    assert composition["CaSO4 x 2 H2O"]["term"] == {
        "id": "CHEBI:32583",
        "label": "calcium sulfate dihydrate",
    }
    assert composition["Nitsch's trace elements"]["concentration"] == {
        "value": "10.0",
        "unit": "ML_PER_L",
    }
    assert repaired["variant_children"] == [
        repair_module.M634_CHILD,
        repair_module.M635_CHILD,
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_togo_m634_links_jcm_parent_and_m636_child(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[1]
    repaired = repair_module.repair_record(_togo_doc(repair_module, target), target)

    assert repaired["parent_media"] == repair_module.JCM_J624_PARENT
    assert repaired["variant_children"] == [repair_module.M636_CHILD]
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.BASE_FINAL
    )
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_togo_m635_becomes_agar_variant(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[2]
    repaired = repair_module.repair_record(_togo_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["physical_state"] == "SOLID_AGAR"
    assert ingredients["Agar"]["concentration"] == {
        "value": "20.0",
        "unit": "G_PER_L",
    }
    assert ingredients["Agar"]["physicochemical_roles"] == ["SOLIDIFYING_AGENT"]
    assert repaired["parent_media"] == repair_module.JCM_J624_AGAR_PARENT
    assert repaired["variant_relationship"] == "PHYSICAL_STATE_VARIANT"
    assert repaired["variant_modifications"] == [
        repair_module.AGAR_VARIANT_MODIFICATION
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_sets_shared_conditions_sterilization_and_flags(
    repair_module,
) -> None:
    target = repair_module.TARGETS[1]
    repaired = repair_module.repair_record(_togo_doc(repair_module, target), target)

    assert repaired["ph_value"] == 7.8
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert repaired["sterilization"] == repair_module.STERILIZATION
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    target = repair_module.TARGETS[1]
    once = repair_module.repair_record(_togo_doc(repair_module, target), target)
    twice = repair_module.repair_record(once, target)

    assert twice == once
    assert once["references"] == [
        {"reference": reference} for reference in target.references
    ]
    matching_events = [
        event
        for event in once["curation_history"]
        if event.get("curator") == repair_module.CURATOR
        and event.get("action") == target.action
    ]
    assert len(matching_events) == 1
    assert "M636 supplemented child backlink" in matching_events[0]["notes"]


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[1]
    doc = _togo_doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[1]
    doc = _togo_doc(repair_module, target)
    doc["ingredients"].pop()

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)
