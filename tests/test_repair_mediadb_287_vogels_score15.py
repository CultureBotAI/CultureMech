from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_mediadb_287_vogels_score15.py"
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
    return _load_script(SCRIPT, "repair_mediadb_287_vogels_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_mediadb_287_vogels")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "vogels_medium_n",
        "original_name": "Vogels Medium N",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.INGREDIENT_SIGNATURE
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "DISSOLVE",
                "description": "Dissolve all ingredients in distilled water.",
            }
        ],
        "curation_history": [],
        "media_term": {
            "preferred_term": "MediaDB Medium 287",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "Vogels Medium N",
            },
        },
        "notes": "Source: MediaDB",
        "applications": ["Cultivation of genome-sequenced organisms"],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_grounds_components_and_exits_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["ph_value"] == 5.8
    assert repaired["temperature_value"] == 25.0
    assert "preparation_steps" not in repaired
    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.INGREDIENT_SIGNATURE
    )
    assert all("mediaingredientmech_chebi_term" in row for row in repaired["ingredients"])
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_uses_expected_chebi_terms(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    for name, expected in repair_module.GROUNDINGS.items():
        assert ingredients[name]["term"] == {
            "id": expected[0],
            "label": expected[1],
        }
        assert ingredients[name]["mediaingredientmech_chebi_term"] == {
            "id": expected[0],
            "label": expected[1],
        }


def test_repair_adds_neurospora_or74a_culture_context(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["organism_culture_type"] == "isolate"
    assert repaired["target_organisms"] == [
        {
            "preferred_term": "Neurospora crassa OR74A",
            "term": {
                "id": "NCBITaxon:5141",
                "label": "Neurospora crassa",
            },
            "strain": "OR74A",
            "evidence": [
                {
                    "reference": repair_module.MEDIA,
                    "supports": "SUPPORT",
                    "explanation": (
                        "MediaDB Medium 287 lists Neurospora crassa OR74A as "
                        "an organism for Vogels medium n."
                    ),
                },
                {
                    "reference": repair_module.GROWTH,
                    "supports": "SUPPORT",
                    "explanation": (
                        "MediaDB growth-data record 605 reports Neurospora "
                        "crassa OR74A on Vogels medium n at pH 5.8 and 25 C."
                    ),
                },
            ],
        }
    ]


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
    ]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert events == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": "; ".join(repair_module.REFERENCES),
            "notes": (
                "Grounded all 12 mM components from MediaDB Medium 287, added "
                "the MediaDB pH 5.8 and 25 C growth conditions, and curated the "
                "Neurospora crassa OR74A organism-medium relationship."
            ),
        }
    ]


def test_plan_repairs_targets_vogels_medium_n(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET

    assert repair_module.plan_repairs() == {
        path: repair_module.repair_record(yaml.safe_load(path.read_text(encoding="utf-8"))),
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "MEDIADB:288"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Orthophosphate", "1.0", "MILLIMOLAR")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_corpus_record_matches_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") == (
        repair_module.INGREDIENT_SIGNATURE
    )
