from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2922_lbs_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2922_lbs_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2922")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _target_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": repair_module.TARGET.stem,
        "original_name": "LBS medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2922",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "LBS medium",
            },
        },
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "high_metal": True,
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_lbs_groundings_units_and_ph(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_target(_target_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert repaired["physical_state"] == "LIQUID"
    assert repaired["ph_value"] == 7.5
    assert "solutions" not in repaired
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients["Tris, pH 7.5"]["term"] == {
        "id": "CHEBI:9754",
        "label": "tris",
    }
    assert "term" not in ingredients["Tryptone"]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.repair_target(_target_doc(repair_module))
    twice = repair_module.repair_target(once)

    assert twice == once


def test_repair_adds_flags_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_target(_target_doc(repair_module))
    twice = repair_module.repair_target(once)

    assert twice == once
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert once["references"] == [
        {"reference": repair_module.TOGO_M2922},
        {"reference": repair_module.TOGO_API},
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


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _target_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_target(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _target_doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_target(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _target_doc(repair_module)
    doc["ingredients"][0]["concentration"]["value"] = "2"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_target(doc)
