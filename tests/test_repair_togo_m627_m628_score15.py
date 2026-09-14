from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m627_m628_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m627_m628_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_m627_m628")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target, *, name: str = "cys_medium") -> dict:
    return {
        "id": target.record_id,
        "name": name,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_signature
        ],
        "media_term": {
            "preferred_term": "source medium",
            "term": {
                "id": target.source_term,
                "label": "CYS MEDIUM",
            },
        },
        "high_metal": True,
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "data_quality_flags": ["incomplete_composition", "resolved_reference"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_base_togo_record_corrects_stocks_and_parentage(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[2]
    repaired = repair_module.repair_record(_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.BASE_FINAL
    assert repaired["ph_value"] == 7.5
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "900.0",
        "unit": "ML_PER_L",
    }
    assert "term" not in ingredients["N-Z-Case (Wako)"]
    assert solutions["Na2MoO4 x 2 H2O stock"]["concentration"] == {
        "value": "0.1",
        "unit": "ML_PER_L",
    }
    assert "high_metal" not in repaired
    assert repaired["parent_media"] == repair_module.JCM_J618_PARENT
    assert "variant_children" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_ymo722_togo_record_links_jcm_619_duplicate(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[3]
    repaired = repair_module.repair_record(_doc(target, name="cys_medium_for_ymo722"), target)
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.SALINITY_FINAL
    assert ingredients["NaCl"]["concentration"]["value"] == "16.0"
    assert repaired["parent_media"] == repair_module.TOGO_M628_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_jcm_618_corrects_scaling_and_adds_children_once(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[0]
    once = repair_module.repair_record(_doc(target), target)
    twice = repair_module.repair_record(once, target)

    assert twice == once
    assert repair_module._signature(twice["ingredients"], "ingredients") == (
        repair_module.BASE_FINAL
    )
    assert twice["variant_children"] == [
        repair_module.JCM_J619_CHILD,
        repair_module.TOGO_M627_CHILD,
    ]
    assert "parent_media" not in twice
    assert scorer_module.score_record(twice) == (0, [])


def test_repair_jcm_619_becomes_salinity_variant_parent(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGETS[1]
    once = repair_module.repair_record(_doc(target, name="cys_medium_for_ymo722"), target)
    twice = repair_module.repair_record(once, target)

    assert twice == once
    assert twice["parent_media"] == repair_module.JCM_J619_PARENT
    assert twice["variant_children"] == [repair_module.TOGO_M628_CHILD]
    assert twice["variant_relationship"] == "SALINITY_VARIANT"
    assert scorer_module.score_record(twice) == (0, [])


def test_repair_inlines_trace_stock_compositions(repair_module) -> None:
    target = repair_module.TARGETS[2]
    repaired = repair_module.repair_record(_doc(target), target)
    solutions = _by_name(repaired["solutions"])

    assert len(solutions) == 7
    assert solutions["Na2MoO4 x 2 H2O stock"]["composition"][0] == {
        "preferred_term": "Na2MoO4 x 2 H2O",
        "concentration": {"value": "12.0", "unit": "G_PER_L"},
        "source": "TOGO M627 / JCM Medium 618",
        "notes": (
            "Na2MoO4 x 2 H2O stock is represented as a 12.0 g/L Na2MoO4 x "
            "2 H2O stock."
        ),
        "term": {"id": "CHEBI:75213", "label": "sodium molybdate dihydrate"},
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:75213",
            "label": "sodium molybdate dihydrate",
        },
        "nutritional_roles": ["TRACE_ELEMENT"],
    }
    assert solutions["VOSO4 x n H2O stock"]["composition"][0]["term"] == {
        "id": "CHEBI:87020",
        "label": "vanadyl sulfate hydrate",
    }
    assert solutions["NiCl2 x 6 H2O stock"]["composition"][0]["term"] == {
        "id": "CHEBI:53542",
        "label": "nickel chloride hexahydrate",
    }


def test_repair_adds_sterilization_references_flags_and_events(
    repair_module,
) -> None:
    target = repair_module.TARGETS[2]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["sterilization"] == repair_module.STERILIZATION
    assert repaired["references"] == [
        {"reference": repair_module.TOGO_M627},
        {"reference": repair_module.JCM_618},
        {"reference": repair_module.MEDIADIVE_J618},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]

    matching_events = [
        event
        for event in repaired["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == target.action
        )
    ]
    assert len(matching_events) == 1
    assert "100 uL trace-metal additions" in matching_events[0]["notes"]
