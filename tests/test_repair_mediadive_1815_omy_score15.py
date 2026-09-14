from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_mediadive_1815_omy_score15.py"
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
    return _load_script(SCRIPT, "repair_mediadive_1815_omy")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_mediadive_1815_omy")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "omy",
        "original_name": "OMY",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": "DSMZ Medium 1815",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "OMY",
            },
        },
        "notes": "Source: DSMZ",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "kg_microbe_match": "mediadive.medium:12",
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_adds_water_and_lowers_review_score(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._ingredient_signature(
        repaired["ingredients"],
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])


def test_repair_grounds_safe_mim_decisions(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Malt extract broth"]["term"] == {
        "id": "FOODON:03301056",
        "label": "malt extract",
    }
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    }
    assert ingredients["Agar"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert ingredients["Distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert "term" not in ingredients["Oat flakes"]
    assert "mediaingredientmech_chebi_term" not in ingredients["Malt extract broth"]
    assert "mediaingredientmech_chebi_term" not in ingredients["Yeast extract"]


def test_repair_adds_preparation_steps(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "HEAT",
            "description": (
                "Briefly boil oat flakes with water, then add malt extract broth, "
                "yeast extract, and agar."
            ),
        },
        {
            "step_number": 2,
            "action": "AUTOCLAVE",
            "description": "Autoclave the completed medium.",
        },
    ]


def test_repair_removes_false_kg_microbe_match(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert "kg_microbe_match" not in repaired


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert twice["references"] == [{"reference": repair_module.MEDIADIVE_1815}]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == repair_module.MEDIADIVE_1815


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:001248"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "mediadive.medium:1816"

    with pytest.raises(ValueError, match="expected media term mediadive.medium:1815"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_signature_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"]["value"] = "16"

    with pytest.raises(ValueError, match="ingredient/solution signature drifted"):
        repair_module.repair_record(doc)
