from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_malt_agar_score15.py"
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
    return _load_script(SCRIPT, "repair_jcm_malt_agar_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_malt_agar")


def _ingredient(name: str, value: str, unit: str) -> dict:
    row = {"preferred_term": name, "concentration": {"value": value, "unit": unit}}
    if name == "Agar":
        row["term"] = {"id": "CHEBI:2509", "label": "agar"}
        row["mediaingredientmech_chebi_term"] = {"id": "CHEBI:2509", "label": "agar"}
    return row


def _doc(repair_module, target) -> dict:
    label = "2% MALT AGAR" if target.malt_grams == "20" else "4% MALT AGAR"
    return {
        "id": target.identifier,
        "name": target.path.stem,
        "original_name": label,
        "category": "fungal",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": target.ph_value,
        "media_term": {
            "preferred_term": f"JCM Medium {target.medium_no}",
            "term": {"id": target.media_term_id, "label": label},
        },
        "notes": f"Source: JCM | Link: {target.source_url}",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURES[target.path]
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "ADJUST_PH",
                "description": f"Adjust pH to {target.ph_value:.1f}.",
            }
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "kg_microbe_match": "mediadive.medium:12",
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


@pytest.mark.parametrize("target", tuple(_load_script(SCRIPT, "repair_jcm_targets").TARGETS))
def test_repair_adds_jcm_water_row(repair_module, scorer_module, target) -> None:
    repaired = repair_module.repair_record(target, _doc(repair_module, target))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(repaired["ingredients"]) == (
        repair_module.FINAL_INGREDIENT_SIGNATURES[target.path]
    )
    assert set(ingredients) == {
        name
        for name, _value, _unit in repair_module.FINAL_INGREDIENT_SIGNATURES[target.path]
    }
    assert ingredients["Malt extract (BD-Difco)"]["concentration"] == {
        "value": target.malt_grams,
        "unit": "G_PER_L",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert "kg_microbe_match" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(target.path), repaired)]) == []


@pytest.mark.parametrize("target", tuple(_load_script(SCRIPT, "repair_jcm_groundings").TARGETS))
def test_repair_grounds_agar_and_water_only(repair_module, target) -> None:
    repaired = repair_module.repair_record(target, _doc(repair_module, target))
    ingredients = _by_name(repaired["ingredients"])

    assert "term" not in ingredients["Malt extract (BD-Difco)"]
    assert "mediaingredientmech_chebi_term" not in ingredients["Malt extract (BD-Difco)"]
    for name, (identifier, label) in repair_module.GROUNDINGS.items():
        assert ingredients[name]["term"] == {"id": identifier, "label": label}
        assert ingredients[name]["mediaingredientmech_chebi_term"] == {
            "id": identifier,
            "label": label,
        }


@pytest.mark.parametrize("target", tuple(_load_script(SCRIPT, "repair_jcm_refs").TARGETS))
def test_repair_adds_reference_flags_and_event_once(repair_module, target) -> None:
    once = repair_module.repair_record(target, _doc(repair_module, target))
    twice = repair_module.repair_record(target, once)

    assert twice == once
    assert once["references"] == [{"reference": reference} for reference in target.references]
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


def test_plan_repairs_target_records(repair_module) -> None:
    expected = {}
    for target in repair_module.TARGETS:
        target_path = repair_module.NORMALIZED / target.path
        expected[target_path] = repair_module.repair_record(
            target,
            yaml.safe_load(target_path.read_text(encoding="utf-8")),
        )

    assert repair_module.plan_repairs() == expected


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.identifier):
        repair_module.repair_record(target, doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "mediadive.medium:J20"

    with pytest.raises(ValueError, match=target.media_term_id):
        repair_module.repair_record(target, doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["ingredients"][0]["preferred_term"] = "Malt"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(target, doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["solutions"] = [
        {
            "preferred_term": "Distilled water",
            "concentration": {"value": "1000", "unit": "ML_PER_L"},
        }
    ]

    with pytest.raises(ValueError, match="unexpected solutions"):
        repair_module.repair_record(target, doc)
