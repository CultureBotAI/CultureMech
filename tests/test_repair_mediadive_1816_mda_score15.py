from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_mediadive_1816_mda_score15.py"
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
    return _load_script(SCRIPT, "repair_mediadive_1816_mda_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_mediadive_1816_mda")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _medium_doc(repair_module) -> dict:
    return {
        "id": repair_module.MEDIUM_ID,
        "name": "mda",
        "original_name": "MDA",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": "DSMZ Medium 1816",
            "term": {"id": repair_module.MEDIA_TERM, "label": "MDA"},
        },
        "notes": "Source: DSMZ",
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_MEDIUM_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _solution_doc(repair_module) -> dict:
    return {
        "id": repair_module.SOLUTION_ID,
        "preferred_term": "Main sol. 1816",
        "term": {
            "id": repair_module.SOLUTION_TERM,
            "label": "Main sol. 1816",
        },
        "composition": [
            _component(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_SOLUTION_SIGNATURE
        ],
        "preparation_notes": "Original volume: 500 mL",
        "curation_history": [],
        "ingredients": [_component("See source for composition", "variable", "VARIABLE")],
        "data_quality_flags": ["incomplete_composition"],
        "category": "bacterial",
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_medium_scales_500_ml_source_and_maps_known_terms(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_medium(_medium_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(
        repaired["ingredients"], "ingredients"
    ) == repair_module.FINAL_MEDIUM_SIGNATURE
    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert ingredients["Malt extract"]["term"] == {
        "id": "FOODON:03301056",
        "label": "malt extract",
    }
    assert ingredients["Bacto peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "Bacto peptone",
    }
    assert ingredients["Glycerol"]["concentration"] == {
        "value": "2",
        "unit": "ML_PER_L",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert ingredients["(-)-Chloramphenicol"]["term"] == {
        "id": "CHEBI:17698",
        "label": "chloramphenicol",
    }
    assert "term" not in ingredients["Desicatted Ox-bile"]
    assert "term" not in ingredients["Olive oil"]
    assert scorer_module.score_parsed([(str(repair_module.MEDIUM_PATH), repaired)]) == []


def test_repair_solution_fixes_liquid_units_and_drops_placeholder(
    repair_module,
) -> None:
    repaired = repair_module.repair_solution(_solution_doc(repair_module))
    composition = _by_name(repaired["composition"])

    assert repair_module._signature(
        repaired["composition"], "composition"
    ) == repair_module.FINAL_SOLUTION_SIGNATURE
    assert composition["Glycerol"]["concentration"] == {
        "value": "2.0",
        "unit": "ML_PER_L",
    }
    assert composition["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert composition["Tween 40"]["chebi_term"] == {
        "id": "CHEBI:53423",
        "label": "polysorbate 40",
    }
    assert composition["Distilled water"]["term"] == {
        "id": "mediadive.compound:4",
        "label": "Distilled water",
    }
    assert "ingredients" not in repaired
    assert "incomplete_composition" not in repaired["data_quality_flags"]


def test_repair_adds_flags_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_medium(_medium_doc(repair_module))
    twice = repair_module.repair_medium(once)

    assert twice == once
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
        "has_unmapped_ingredients",
    ]
    assert once["references"] == [
        {"reference": repair_module.MEDIADIVE_1816},
        {"reference": repair_module.MEDIADIVE_SOLUTION_6326},
    ]
    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1


def test_solution_repair_is_idempotent(repair_module) -> None:
    once = repair_module.repair_solution(_solution_doc(repair_module))
    twice = repair_module.repair_solution(once)

    assert twice == once
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _medium_doc(repair_module)
    doc["media_term"]["term"]["id"] = "mediadive.medium:9999"

    with pytest.raises(ValueError, match=repair_module.MEDIA_TERM):
        repair_module.repair_medium(doc)


def test_repair_rejects_wrong_solution_term(repair_module) -> None:
    doc = _solution_doc(repair_module)
    doc["term"]["id"] = "mediadive.solution:9999"

    with pytest.raises(ValueError, match=repair_module.SOLUTION_TERM):
        repair_module.repair_solution(doc)


def test_repair_rejects_medium_ingredient_drift(repair_module) -> None:
    doc = _medium_doc(repair_module)
    doc["ingredients"][0]["concentration"]["value"] = "19"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_medium(doc)
