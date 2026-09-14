from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_culturebotht_nutrient_broth_score15.py"
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
    return _load_script(SCRIPT, "repair_culturebotht_nutrient_broth_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_culturebotht_nutrient_broth")


def _component(
    name: str,
    value: str,
    unit: str,
    term: dict[str, str] | None = None,
) -> dict:
    row = {"preferred_term": name, "concentration": {"value": value, "unit": unit}}
    if term:
        row["term"] = term
    return row


def _doc() -> dict:
    return {
        "id": "CultureMech:015471",
        "name": "nutrient broth",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _component("Bacto Peptone", "15", "G_PER_L"),
            _component("Yeast Extract", "3", "G_PER_L"),
            _component("D-Glucose", "1", "G_PER_L", {"id": "CHEBI:17634", "label": "D-glucose"}),
            _component(
                "Sodium Chloride",
                "6",
                "G_PER_L",
                {"id": "CHEBI:26710", "label": "sodium chloride"},
            ),
        ],
        "description": "Nutrient broth medium",
        "notes": "Source: FEBA media definitions",
        "category": "bacterial",
        "source_data": {
            "origin": "CultureBotHT",
            "notes": (
                "database_id: nutrient broth; " "url: https://github.com/CultureBotAI/CultureBotHT"
            ),
        },
        "curation_history": [],
        "data_quality_flags": [],
        "kg_microbe_match": "mediadive.medium:681",
    }


def _ingredient_by_name(doc: dict) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in doc["ingredients"]}


def test_culturebotht_nutrient_broth_exits_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_document(_doc())

    assert scorer_module.score_parsed([("bacterial/nutrient_broth.yaml", repaired)]) == []
    assert repaired["sources"] == [
        {
            "database": "CultureBotHT",
            "database_id": "nutrient broth",
            "url": "https://github.com/CultureBotAI/CultureBotHT",
        }
    ]
    assert repaired["references"] == [
        {"reference": "CultureBotHT:nutrient broth"},
        {"reference": "https://github.com/CultureBotAI/CultureBotHT"},
    ]
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]
    assert "kg_microbe_match" not in repaired

    ingredients = _ingredient_by_name(repaired)
    assert ingredients["Bacto Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "Bacto peptone",
    }
    assert ingredients["Yeast Extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    }


def test_culturebotht_nutrient_broth_requires_import_signature(
    repair_module,
) -> None:
    doc = _doc()
    doc["ingredients"] = doc["ingredients"][:3]

    with pytest.raises(ValueError, match="ingredient list drifted"):
        repair_module.repair_document(doc)
