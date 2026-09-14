from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m787_mycoplasma_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m787_mycoplasma_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_m787")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": "mycoplasma_medium",
        "original_name": "Mycoplasma Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": 7.4,
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_ingredients
        ],
        "media_term": {
            "preferred_term": "source medium",
            "term": {"id": target.source_term, "label": "Mycoplasma Medium"},
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": [
            "incomplete_composition",
            "needs_manual_curation",
            "resolved_reference",
        ],
        "solutions": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_solutions
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def _repair(repair_module, path: Path) -> dict:
    target = next(target for target in repair_module.TARGETS if target.path == path)
    return repair_module.repair_record(_doc(target), target)


def test_jcm_j761_becomes_canonical_nested_parent(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair(repair_module, repair_module.JCM_J761_PATH)

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert repair_module._signature(
        repaired["solutions"],
        "solutions",
    ) == repair_module.FINAL_SOLUTION_SIGNATURE
    assert repaired["ph_range"] == {"min": 7.2, "max": 7.6}
    assert "ph_value" not in repaired
    assert repaired["variant_children"] == [repair_module.M787_CHILD]
    assert "parent_media" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_togo_m787_links_to_jcm_source_duplicate(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M787_PATH)

    assert repaired["parent_media"] == repair_module.J761_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.J761_PARENT["notes"]]
    assert "variant_children" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_corrects_volume_additions_and_nests_yeast_stock(
    repair_module,
) -> None:
    repaired = _repair(repair_module, repair_module.TOGO_M787_PATH)
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "700.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Horse serum"]["concentration"] == {
        "value": "200.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Agar"]["physicochemical_roles"] == ["SOLIDIFYING_AGENT"]
    assert solutions["25% Yeast Extract Solution"] == {
        "preferred_term": "25% Yeast Extract Solution",
        "concentration": {"value": "100.0", "unit": "ML_PER_L"},
        "source": "TOGO M787 / JCM Medium 761",
        "notes": (
            "TOGO M787 / JCM Medium 761 adds 100.0 ml/L "
            "25% Yeast Extract Solution."
        ),
        "composition": [
            {
                "preferred_term": "Yeast extract",
                "concentration": {"value": "25.0", "unit": "PERCENT_W_V"},
                "source": "TOGO M787 / JCM Medium 761",
                "notes": (
                    "TOGO M787 / JCM Medium 761 specifies "
                    "25% Yeast Extract Solution as 25.0% w/v."
                ),
                "term": {
                    "id": "FOODON:03315426",
                    "label": "yeast extract",
                },
                "nutritional_roles": [
                    "NITROGEN_SOURCE",
                    "PROTEIN_SOURCE",
                    "VITAMIN_SOURCE",
                ],
            }
        ],
    }


def test_repair_adds_references_flags_sterilization_and_event_once(
    repair_module,
) -> None:
    target = next(
        target
        for target in repair_module.TARGETS
        if target.path == repair_module.TOGO_M787_PATH
    )
    once = repair_module.repair_record(_doc(target), target)
    twice = repair_module.repair_record(once, target)

    assert twice == once
    assert once["references"] == [
        {"reference": reference} for reference in target.references
    ]
    assert once["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    assert once["sterilization"] == repair_module.STERILIZATION
    matching_events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair_module.CURATOR
        and event.get("action") == target.action
    ]
    assert len(matching_events) == 1
    assert repair_module.MEDIADIVE_J761 in matching_events[0]["source"]
    assert "25% Yeast Extract Solution" in matching_events[0]["notes"]


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = next(
        target
        for target in repair_module.TARGETS
        if target.path == repair_module.TOGO_M787_PATH
    )
    doc = _doc(target)
    doc["ingredients"][0]["preferred_term"] = "Tap water"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_solution_drift(repair_module) -> None:
    target = next(
        target
        for target in repair_module.TARGETS
        if target.path == repair_module.TOGO_M787_PATH
    )
    doc = _doc(target)
    doc["solutions"].append(_ingredient("Horse serum", "200", "G_PER_L"))

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, target)
