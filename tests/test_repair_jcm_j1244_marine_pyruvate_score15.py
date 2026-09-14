from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_j1244_marine_pyruvate_score15.py"
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
    return _load_script(SCRIPT, "repair_jcm_j1244_marine_pyruvate_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_j1244")


def _term(identifier: str, label: str) -> dict:
    return {"id": identifier, "label": label}


def _ingredient(name: str, value: str, unit: str) -> dict:
    row = {"preferred_term": name, "concentration": {"value": value, "unit": unit}}
    if name == "Sodium pyruvate":
        row["term"] = _term("CHEBI:50144", "sodium pyruvate")
        row["mediaingredientmech_chebi_term"] = _term("CHEBI:50144", "sodium pyruvate")
    return row


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "marine_broth_2216_with_pyruvate",
        "original_name": "MARINE BROTH 2216 WITH PYRUVATE",
        "category": "specialized",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 8.0,
        "media_term": {
            "preferred_term": "JCM Medium J1244",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "MARINE BROTH 2216 WITH PYRUVATE",
            },
        },
        "notes": "Source: JCM",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "AUTOCLAVE",
                "description": "Mix components and adjust pH to 8.0. Autoclave.",
            }
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "kg_microbe_match": "mediadive.medium:J1244",
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_j1244_restores_water_and_pyruvate_stock(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])
    pyruvate = solutions["1.0 M Sodium pyruvate solution"]["composition"][0]

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repair_module._signature(repaired["solutions"], "solutions") == (
        repair_module.FINAL_SOLUTION_SIGNATURE
    )
    assert "term" not in ingredients["Marine broth 2216 (BD-Difco)"]
    assert ingredients["Distilled water"]["term"] == _term("CHEBI:15377", "water")
    assert pyruvate["concentration"] == {"value": "1.0", "unit": "MOLAR"}
    assert pyruvate["term"] == _term("CHEBI:50144", "sodium pyruvate")
    assert repaired["sterilization"] == {"method": "AUTOCLAVE"}
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_j1244_adds_references_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice == once
    assert repair_module.dump_record(twice) == repair_module.dump_record(once)
    assert once["references"] == [
        {"reference": repair_module.MEDIADIVE_PAGE},
        {"reference": repair_module.MEDIADIVE_REST},
    ]
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
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


def test_plan_repairs_target_record(repair_module) -> None:
    target_path = repair_module.NORMALIZED / repair_module.TARGET
    expected_target = repair_module.repair_record(
        yaml.safe_load(target_path.read_text(encoding="utf-8"))
    )

    assert repair_module.plan_repairs() == {target_path: expected_target}


def test_j1244_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_j1244_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "mediadive.medium:J999"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_j1244_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["preferred_term"] = "Marine broth"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)
