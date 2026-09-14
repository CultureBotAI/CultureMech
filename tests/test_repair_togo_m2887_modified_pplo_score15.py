from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2887_modified_pplo_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2887_modified_pplo_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2887")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "modified_pleuropneumonia_like_organism_pplo_medium",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2887",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": [
            "incomplete_composition",
            "needs_manual_curation",
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_restores_pplo_liter_and_horse_serum_percent(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert ingredients[repair_module.PPLO_MEDIUM]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients[repair_module.HORSE_SERUM]["concentration"] == {
        "value": "20.0",
        "unit": "PERCENT_V_V",
    }


def test_repair_keeps_activity_unit_as_variable(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    penicillin = _by_name(repaired["ingredients"])[repair_module.PENICILLIN]

    assert penicillin["concentration"] == {"value": "variable", "unit": "VARIABLE"}
    assert "200 IU/ml" in penicillin["notes"]
    assert "schema has no unit for activity units" in penicillin["notes"]


def test_repair_grounds_simple_components_and_yeast_extract(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients[repair_module.YEAST_EXTRACT]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients[repair_module.THALLIUM_ACETATE]["term"] == {
        "id": "CHEBI:75192",
        "label": "thallium(I) acetate",
    }
    assert ingredients[repair_module.PENICILLIN]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:17334",
        "label": "penicillin",
    }

    for name in (repair_module.HORSE_SERUM, repair_module.PPLO_MEDIUM):
        assert "term" not in ingredients[name]
        assert "mediaingredientmech_chebi_term" not in ingredients[name]


def test_repair_adds_reference_flags_and_scores_below_review_threshold(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert "ph_value" not in repaired
    assert repaired["references"] == [{"reference": repair_module.TOGO_M2887}]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_is_idempotent(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repair_module.repair_record(repaired) == repaired
