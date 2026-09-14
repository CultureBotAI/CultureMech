from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_942_e_coli_feed_score15.py"
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
    return _load_script(SCRIPT, "repair_dsmz_942_e_coli_feed_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_942")


def _component(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
    }


def _medium_doc(repair_module) -> dict:
    return {
        "id": "CultureMech:002118",
        "name": "agar_with_e_coli_as_feed",
        "original_name": "AGAR WITH E. COLI AS FEED",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": 7.2,
        "media_term": {
            "preferred_term": "DSMZ Medium 942",
            "term": {
                "id": "mediadive.medium:942",
                "label": "AGAR WITH E. COLI AS FEED",
            },
        },
        "notes": "Source: DSMZ",
        "ingredients": [
            _component(*component)
            for component in repair_module.IMPORTED_MEDIA_SIGNATURE
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "AUTOCLAVE",
                "description": "Adjust pH to 7.2, autoclave and pour plates.",
            },
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "kg_microbe_match": "mediadive.medium:49",
    }


def _solution_doc(repair_module) -> dict:
    return {
        "id": "CultureMech:011348",
        "preferred_term": "Main sol. 942",
        "term": {"id": "mediadive.solution:1939", "label": "Main sol. 942"},
        "composition": [
            _component(*component)
            for component in repair_module.IMPORTED_SOLUTION_SIGNATURE
        ],
        "preparation_notes": "Adjust pH to 7.2, autoclave and pour plates.",
        "ingredients": [_component("See source for composition", "variable", "VARIABLE")],
        "data_quality_flags": ["incomplete_composition"],
        "category": "bacterial",
        "curation_history": [],
    }


def test_dsmz_942_medium_is_marked_curated_and_kept_two_component(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_medium(_medium_doc(repair_module))

    assert repair_module._signature(
        repaired["ingredients"], "ingredients"
    ) == repair_module.FINAL_MEDIA_SIGNATURE
    assert "kg_microbe_match" not in repaired
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert repaired["sterilization"] == repair_module.STERILIZATION
    assert [step["action"] for step in repaired["preparation_steps"]] == [
        "MIX",
        "ADJUST_PH",
        "AUTOCLAVE",
        "POUR_PLATES",
        "MIX",
        "AUTOCLAVE",
        "MIX",
    ]
    assert repaired["references"] == [{"reference": repair_module.DSMZ_942}]
    assert scorer_module.score_parsed([("bacterial/dsmz_942.yaml", repaired)]) == []


def test_mediadive_1939_solution_water_and_placeholder_are_repaired(
    repair_module,
) -> None:
    repaired = repair_module.repair_solution(_solution_doc(repair_module))

    assert repair_module._signature(
        repaired["composition"], "composition"
    ) == repair_module.FINAL_SOLUTION_SIGNATURE
    assert repaired["composition"][2]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert repaired["composition"][2]["term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert "ingredients" not in repaired
    assert "data_quality_flags" not in repaired


def test_repairs_are_idempotent(repair_module) -> None:
    for function, doc in (
        (repair_module.repair_medium, _medium_doc(repair_module)),
        (repair_module.repair_solution, _solution_doc(repair_module)),
    ):
        once = function(doc)
        twice = function(once)
        assert twice == once


def test_dsmz_942_medium_rejects_wrong_source(repair_module) -> None:
    doc = _medium_doc(repair_module)
    doc["media_term"]["term"]["id"] = "mediadive.medium:49"

    with pytest.raises(ValueError, match="mediadive.medium:942"):
        repair_module.repair_medium(doc)


def test_solution_1939_rejects_composition_drift(repair_module) -> None:
    doc = _solution_doc(repair_module)
    doc["composition"][0]["preferred_term"] = "Unknown"

    with pytest.raises(ValueError, match="solution composition signature drifted"):
        repair_module.repair_solution(doc)
