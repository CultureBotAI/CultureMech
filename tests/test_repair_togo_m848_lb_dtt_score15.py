from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m848_lb_dtt_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m848_lb_dtt_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_m848")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _medium_doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": "lb_luria_bertani_broth_with_1_mm_dtt",
        "original_name": "LB (LURIA-BERTANI) BROTH WITH 1 mM DTT",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in target.imported_ingredients
        ],
        "media_term": {
            "preferred_term": "source medium",
            "term": {"id": target.source_term, "label": "LB Broth with DTT"},
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": [
            "incomplete_composition",
            "needs_manual_curation",
            "resolved_reference",
        ],
    }


def _solution_doc(repair_module) -> dict:
    return {
        "id": "CultureMech:013706",
        "preferred_term": "Main sol. J813",
        "term": {
            "id": "mediadive.solution:4761",
            "label": "Main sol. J813",
        },
        "composition": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_SOLUTION_COMPOSITION
        ],
        "preparation_notes": (
            "Adjust pH to 7.0.\n\nAfter autoclaving, aseptically add 1 mM "
            "(final conc.) 1,4-dithiothreitol (DTT)."
        ),
        "curation_history": [],
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.PLACEHOLDER_INGREDIENTS
        ],
        "data_quality_flags": ["incomplete_composition"],
        "category": "bacterial",
    }


def _repair_medium(repair_module, path: Path) -> dict:
    target = next(target for target in repair_module.TARGETS if target.path == path)
    return repair_module.repair_medium_record(_medium_doc(target), target)


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_jcm_j813_becomes_canonical_parent(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair_medium(repair_module, repair_module.JCM_J813_PATH)

    assert repaired["ph_range"] == {"min": 7.0, "max": 7.0}
    assert "ph_value" not in repaired
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_COMPOSITION
    )
    assert repaired["variant_children"] == [repair_module.M848_CHILD]
    assert "parent_media" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_togo_m848_links_to_jcm_source_duplicate(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair_medium(repair_module, repair_module.TOGO_M848_PATH)

    assert repaired["parent_media"] == repair_module.J813_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.M848_CHILD["notes"]]
    assert "variant_children" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_corrects_water_dtt_and_grounds_source_ingredients(
    repair_module,
) -> None:
    repaired = _repair_medium(repair_module, repair_module.TOGO_M848_PATH)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Distilled water"]["term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert ingredients["Tryptone (BD-Difco)"]["term"] == {
        "id": "MICRO:0000182",
        "label": "Tryptone",
    }
    assert ingredients["Yeast extract (BD-Difco)"]["term"] == {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    }
    assert ingredients["1,4-dithiothreitol (DTT)"]["concentration"] == {
        "value": "1.0",
        "unit": "MILLIMOLAR",
    }
    assert ingredients["1,4-dithiothreitol (DTT)"]["physicochemical_roles"] == [
        "REDUCING_AGENT",
    ]


def test_solution_helper_lifts_basal_composition_and_drops_placeholder(
    repair_module,
) -> None:
    repaired = repair_module.repair_solution_record(_solution_doc(repair_module))

    assert "ingredients" not in repaired
    assert (
        repair_module._signature(
            repaired["composition"],
            "composition",
        )
        == repair_module.BASAL_COMPOSITION
    )
    assert repaired["composition"][-1]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert "dithiothreitol" not in repaired["preparation_notes"]
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]


def test_repair_adds_references_flags_and_event_once(
    repair_module,
) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.TOGO_M848_PATH
    )
    once = repair_module.repair_medium_record(_medium_doc(target), target)
    twice = repair_module.repair_medium_record(once, target)

    assert twice == once
    assert once["references"] == [{"reference": reference} for reference in target.references]
    assert once["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair_module.CURATOR and event.get("action") == target.action
    ]
    assert len(matching_events) == 1
    assert repair_module.TOGO_M848 in matching_events[0]["source"]
    assert "dithiothreitol" in matching_events[0]["notes"]


def test_repair_rejects_wrong_medium_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _medium_doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_medium_record(doc, target)


def test_repair_rejects_medium_ingredient_drift(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.TOGO_M848_PATH
    )
    doc = _medium_doc(target)
    doc["ingredients"].pop()

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_medium_record(doc, target)


def test_repair_rejects_solution_composition_drift(repair_module) -> None:
    doc = _solution_doc(repair_module)
    doc["composition"].pop()

    with pytest.raises(ValueError, match="composition signature drifted"):
        repair_module.repair_solution_record(doc)
