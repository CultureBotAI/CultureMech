from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2214_modified_m17_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2214_modified_m17_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2214")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "modified_m17_medium",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2214",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_splits_mgso4_stock_and_scores_cleanly(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["ph_range"] == {"min": 7.1, "max": 7.2}
    assert repair_module._signature(
        repaired["ingredients"], "ingredients"
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert repair_module._solution_signature(
        repaired["solutions"], "solutions"
    ) == repair_module.FINAL_SOLUTION_SIGNATURE
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_corrects_solution_and_water_units(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    solution = repaired["solutions"][0]
    stock = _by_name(solution["composition"])

    assert ingredients[repair_module.WATER]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert solution["concentration"] == {"value": "1.0", "unit": "ML_PER_L"}
    assert stock[repair_module.MGSO4]["concentration"] == {
        "value": "1.0",
        "unit": "MOLAR",
    }


def test_repair_grounds_all_components(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    stock = _by_name(repaired["solutions"][0]["composition"])

    assert stock[repair_module.MGSO4]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:31795",
        "label": "magnesium sulfate heptahydrate",
    }
    assert ingredients[repair_module.GLYCEROPHOSPHATE][
        "mediaingredientmech_chebi_term"
    ] == {
        "id": "CHEBI:132089",
        "label": "sodium glycerol 2-phosphate",
    }
    assert ingredients[repair_module.POLYPEPTONE]["term"] == {
        "id": "FOODON:03315306",
        "label": "Polypeptone",
    }
    assert ingredients[repair_module.PHYTONE_PEPTONE]["term"] == {
        "id": "FOODON:03315720",
        "label": "Soy peptone",
    }


def test_repair_adds_autoclave_evidence(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["preparation_steps"][1] == {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "duration": "15 min",
        "description": "Dispense 10 ml portions and autoclave at 121 C for 15 min.",
    }
    assert repaired["sterilization"] == repair_module.STERILIZATION


def test_repair_is_idempotent(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repair_module.repair_record(repaired) == repaired
