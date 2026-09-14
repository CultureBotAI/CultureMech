from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m3039_m3040_hgam_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m3039_m3040_hgam_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_hgam")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
        "name": "Unknown solution",
    }


def _hgam_doc(repair_module, target) -> dict:
    return {
        "id": target.record_id,
        "name": "hgam",
        "original_name": "HGAM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": target.physical_state,
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_ingredient_signature
        ],
        "media_term": {
            "preferred_term": "TOGO Medium",
            "term": {"id": target.source_term, "label": "HGAM"},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_SOLUTION_SIGNATURE
        ],
    }


def _stale_doc(repair_module, target) -> dict:
    return {
        "id": target.record_id,
        "name": "stale_child",
        "original_name": "Stale child",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [_ingredient("Distilled water", "1", "G_PER_L")],
        "media_term": {"term": {"id": "TOGO:stale", "label": "Stale"}},
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "parent_media": dict(repair_module.STALE_PARENT),
        "variant_relationship": "SOURCE_DUPLICATE",
        "variant_modifications": list(repair_module.STALE_VARIANT_MODIFICATIONS),
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_m3039_restores_solid_hgam_formula_and_true_child(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.HGAM_TARGETS[0]
    repaired = repair_module.repair_hgam_record(
        _hgam_doc(repair_module, target),
        target,
    )
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["ph_value"] == 7.3
    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.M3039_FINAL_INGREDIENTS
    )
    assert "term" not in ingredients["Nissui Modified GAM Broth"]
    assert ingredients["Agar (if needed)"]["term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert "solutions" not in repaired
    assert "parent_media" not in repaired
    assert repaired["variant_children"] == [repair_module.M3040_CHILD]
    assert scorer_module.score_record(repaired) == (0, [])


def test_m3040_restores_anaerobic_liquid_hgam_variant(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.HGAM_TARGETS[1]
    repaired = repair_module.repair_hgam_record(
        _hgam_doc(repair_module, target),
        target,
    )
    ingredient_names = {row["preferred_term"] for row in repaired["ingredients"]}

    assert repaired["physical_state"] == "LIQUID"
    assert ingredient_names == {"Nissui Modified GAM Broth", "Distilled water"}
    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.M3040_FINAL_INGREDIENTS
    )
    assert repaired["aeration"] == "N2 atmosphere during anaerobic liquid dispensing"
    assert repaired["sterilization"] == repair_module.M3040_STERILIZATION
    assert repaired["preparation_steps"][2]["action"] == "ALIQUOT"
    assert repaired["parent_media"] == repair_module.M3040_PARENT
    assert repaired["variant_relationship"] == "PHYSICAL_STATE_VARIANT"
    assert repaired["variant_modifications"] == [
        repair_module.M3040_VARIANT_MODIFICATION
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_hgam_repair_adds_flags_references_and_events_once(repair_module) -> None:
    target = repair_module.HGAM_TARGETS[1]
    once = repair_module.repair_hgam_record(
        _hgam_doc(repair_module, target),
        target,
    )
    twice = repair_module.repair_hgam_record(once, target)

    assert twice == once
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert once["references"] == [
        {"reference": reference} for reference in target.references
    ]
    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == target.action
        )
    ]
    assert len(matching_events) == 1


@pytest.mark.parametrize("target", [0, 1])
def test_repair_removes_stale_hgam_sparse_links(repair_module, target) -> None:
    link_target = repair_module.STALE_LINK_TARGETS[target]
    once = repair_module.repair_stale_link_record(
        _stale_doc(repair_module, link_target),
        link_target,
    )
    twice = repair_module.repair_stale_link_record(once, link_target)

    assert twice == once
    assert "parent_media" not in once
    assert "variant_relationship" not in once
    assert "variant_modifications" not in once
    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == link_target.action
        )
    ]
    assert len(matching_events) == 1


def test_hgam_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.HGAM_TARGETS[0]
    doc = _hgam_doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_hgam_record(doc, target)


def test_hgam_repair_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.HGAM_TARGETS[0]
    doc = _hgam_doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=target.source_term):
        repair_module.repair_hgam_record(doc, target)


def test_hgam_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.HGAM_TARGETS[1]
    doc = _hgam_doc(repair_module, target)
    doc["ingredients"][0]["concentration"] = {"value": "1.0", "unit": "L"}

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_hgam_record(doc, target)


def test_hgam_repair_rejects_solution_drift(repair_module) -> None:
    target = repair_module.HGAM_TARGETS[0]
    doc = _hgam_doc(repair_module, target)
    doc["solutions"][0]["preferred_term"] = "Different product"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_hgam_record(doc, target)


def test_stale_link_repair_rejects_new_parent(repair_module) -> None:
    target = repair_module.STALE_LINK_TARGETS[0]
    doc = _stale_doc(repair_module, target)
    doc["parent_media"]["id"] = "CultureMech:new"

    with pytest.raises(ValueError, match="parent_media drifted"):
        repair_module.repair_stale_link_record(doc, target)
