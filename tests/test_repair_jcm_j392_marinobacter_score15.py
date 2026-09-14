from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_j392_marinobacter_score15.py"
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
    return _load_script(SCRIPT, "repair_jcm_j392_marinobacter_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_j392")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": repair_module.TARGET.stem,
        "original_name": "MARINOBACTER ALKALIPHILUS MEDIUM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "JCM Medium J392",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "MARINOBACTER ALKALIPHILUS MEDIUM",
            },
        },
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_restores_water_and_groundings(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert ingredients["Marine broth 2216 (BD-Difco)"] == {
        "preferred_term": "Marine broth 2216 (BD-Difco)",
        "concentration": {"value": "37.4", "unit": "G_PER_L"},
        "source": repair_module.SOURCE,
        "notes": "JCM Medium 392 lists 37.4 g/L Marine broth 2216 (BD-Difco).",
    }
    assert ingredients["Na2SiO3"]["term"] == {
        "id": "CHEBI:60720",
        "label": "sodium silicate",
    }
    assert ingredients["Na2CO3"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:29377",
        "label": "sodium carbonate",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_splits_autoclave_steps(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert [step["action"] for step in repaired["preparation_steps"]] == [
        "MIX",
        "AUTOCLAVE",
        "AUTOCLAVE",
        "MIX",
    ]
    assert repaired["sterilization"]["method"] == "AUTOCLAVE"
    assert "separately" in repaired["sterilization"]["notes"]


def test_repair_adds_flags_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_target(_doc(repair_module))
    twice = repair_module.repair_target(once)

    assert twice == once
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert once["references"] == [{"reference": repair_module.JCM_392}]
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
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_target(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "mediadive.medium:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_target(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"]["unit"] = "ML_PER_L"

    with pytest.raises(ValueError, match="ingredient signature"):
        repair_module.repair_target(doc)


def test_target_record_matches_jcm_j392_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
