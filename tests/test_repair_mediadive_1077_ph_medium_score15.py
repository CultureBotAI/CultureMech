from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_mediadive_1077_ph_medium_score15.py"
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
    return _load_script(SCRIPT, "repair_mediadive_1077_ph_medium")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_mediadive_1077")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "ph_medium",
        "original_name": "PH MEDIUM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.8,
        "media_term": {
            "preferred_term": "DSMZ Medium 1077",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "PH MEDIUM",
            },
        },
        "notes": "Source: DSMZ",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "preparation_steps": [{"step_number": 1, "action": "MIX", "description": "stale"}],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "kg_microbe_match": "mediadive.medium:1077",
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_restores_source_stock_structure_and_leaves_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    solution_2 = solutions["Solution 2"]
    nested_solution_2 = _by_name(solution_2["solutions"])

    assert repaired["ingredients"] == []
    assert (
        repair_module._solution_signatures(
            repaired["solutions"],
        )
        == repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert solutions["Solution 1"]["concentration"] == {
        "value": "800.0",
        "unit": "ML_PER_L",
    }
    assert solution_2["concentration"] == {
        "value": "200.0",
        "unit": "ML_PER_L",
    }
    assert nested_solution_2["Yeast Extract Solution (25%, autoclaved)"]["concentration"] == {
        "value": "46.8",
        "unit": "ML_PER_L",
    }
    assert nested_solution_2["Fish sperm DNA solution (filter-sterilized)"]["concentration"] == {
        "value": "9.35",
        "unit": "ML_PER_L",
    }
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_grounds_supported_components(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solution_1 = _by_name(repaired["solutions"])["Solution 1"]
    solution_2 = _by_name(repaired["solutions"])["Solution 2"]
    solution_1_components = _by_name(solution_1["composition"])
    solution_2_components = _by_name(solution_2["composition"])
    yeast_stock = _by_name(solution_2["solutions"])["Yeast Extract Solution (25%, autoclaved)"]
    yeast_stock_components = _by_name(yeast_stock["composition"])

    assert "term" not in solution_1_components["PPLO broth"]
    assert solution_2_components["Horse serum"]["term"] == {
        "id": "MICRO:0001235",
        "label": "Horse serum",
    }
    assert "mediaingredientmech_chebi_term" not in solution_2_components["Horse serum"]
    assert yeast_stock_components["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    }
    assert solution_1_components["Distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }


def test_repair_keeps_subsolution_ph_as_preparation_steps(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert "ph_value" not in repaired
    assert "ph_range" not in repaired
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Prepare Solution 1, adjust it to pH 6.5, and autoclave it.",
        },
        {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Prepare Solution 2 and adjust it to pH 7.8.",
        },
        {
            "step_number": 3,
            "action": "MIX",
            "description": "Combine 80 ml Solution 1 with 20 ml Solution 2.",
        },
    ]


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

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
    assert matching_events[0]["source"] == "; ".join(repair_module.REFERENCES)


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:000511"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "mediadive.medium:1078"

    with pytest.raises(ValueError, match="expected media term mediadive.medium:1077"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_signature_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"]["value"] = "20"

    with pytest.raises(ValueError, match="ingredient/solution signature drifted"):
        repair_module.repair_record(doc)
