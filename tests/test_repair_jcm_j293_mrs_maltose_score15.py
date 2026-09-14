from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_j293_mrs_maltose_score15.py"
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
    return _load_script(SCRIPT, "repair_jcm_j293_mrs_maltose_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_j293")


def _ingredient(name: str, value: str, unit: str) -> dict:
    row = {"preferred_term": name, "concentration": {"value": value, "unit": unit}}
    if name == "Maltose":
        row["term"] = {"id": "CHEBI:17306", "label": "maltose"}
        row["mediaingredientmech_chebi_term"] = {"id": "CHEBI:17306", "label": "maltose"}
    return row


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": repair_module.TARGET.stem,
        "original_name": "MRS MALTOSE MEDIUM",
        "category": "fungal",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 6.5,
        "media_term": {
            "preferred_term": "JCM Medium J293",
            "term": {"id": repair_module.EXPECTED_MEDIA_TERM, "label": "MRS MALTOSE MEDIUM"},
        },
        "notes": "Source: JCM | Link: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=293",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "preparation_steps": [
            {"step_number": 1, "action": "ADJUST_PH", "description": "Adjust pH to 6.5."}
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_adds_j293_water_row(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(repaired["ingredients"]) == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert set(ingredients) == {
        name for name, _value, _unit in repair_module.FINAL_INGREDIENT_SIGNATURE
    }
    assert ingredients["Lactobacilli MRS broth (BD-Difco)"]["concentration"] == {
        "value": "55",
        "unit": "G_PER_L",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_grounds_maltose_and_water_only(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert "term" not in ingredients["Lactobacilli MRS broth (BD-Difco)"]
    assert "mediaingredientmech_chebi_term" not in ingredients["Lactobacilli MRS broth (BD-Difco)"]
    for name, (identifier, label) in repair_module.GROUNDINGS.items():
        assert ingredients[name]["term"] == {"id": identifier, "label": label}
        assert ingredients[name]["mediaingredientmech_chebi_term"] == {
            "id": identifier,
            "label": label,
        }


def test_repair_adds_reference_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice == once
    assert once["references"] == [{"reference": reference} for reference in repair_module.REFERENCES]
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


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "mediadive.medium:J20"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["preferred_term"] = "MRS broth"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"] = [
        {
            "preferred_term": "Distilled water",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
        }
    ]

    with pytest.raises(ValueError, match="unexpected solutions"):
        repair_module.repair_record(doc)
