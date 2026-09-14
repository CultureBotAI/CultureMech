from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2408_leptospira_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2408_leptospira_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2408")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "modified_leptospira_medium",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2408",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _component(name, value, unit)
            for name, value, unit, _composition, _solutions in (
                repair_module.IMPORTED_SOLUTION_SIGNATURE
            )
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_nests_supplement_and_hemin_stock(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["ph_range"] == {"min": 7.2, "max": 7.4}
    assert "ph_value" not in repaired
    assert (
        repair_module._signature(repaired["ingredients"], "ingredients")
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert (
        repair_module._solution_signature(repaired["solutions"], "solutions")
        == repair_module.FINAL_SOLUTION_SIGNATURE
    )
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_corrects_milliliter_additions(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    supplement_a = repaired["solutions"][0]
    hemin_stock = supplement_a["solutions"][0]
    supplement_components = _by_name(supplement_a["composition"])
    hemin_components = _by_name(hemin_stock["composition"])

    assert ingredients[repair_module.DI_WATER]["concentration"] == {
        "value": "900.0",
        "unit": "ML_PER_L",
    }
    assert supplement_a["concentration"] == {"value": "100.0", "unit": "ML_PER_L"}
    assert supplement_components[repair_module.RABBIT_SERUM]["concentration"] == {
        "value": "100.0",
        "unit": "ML_PER_L",
    }
    assert hemin_stock["concentration"] == {"value": "2.5", "unit": "ML_PER_L"}
    assert hemin_components[repair_module.NAOH_STOCK]["concentration"] == {
        "value": "10.0",
        "unit": "ML_PER_L",
    }
    assert hemin_components[repair_module.DI_WATER]["concentration"] == {
        "value": "990.0",
        "unit": "ML_PER_L",
    }


def test_repair_grounds_machine_usable_components(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    supplement_components = _by_name(repaired["solutions"][0]["composition"])
    hemin_components = _by_name(repaired["solutions"][0]["solutions"][0]["composition"])

    assert ingredients[repair_module.NACL]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:26710",
        "label": "sodium chloride",
    }
    assert ingredients[repair_module.BEEF_EXTRACT]["term"] == {
        "id": "FOODON:03302088",
        "label": "Beef extract",
    }
    assert ingredients[repair_module.PEPTONE]["term"] == {
        "id": "MICRO:0000178",
        "label": "Peptone",
    }
    assert supplement_components[repair_module.RABBIT_SERUM]["term"] == {
        "id": "MICRO:0002392",
        "label": "Rabbit serum",
    }
    assert hemin_components[repair_module.HEMIN]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:50385",
        "label": "hemin",
    }
    assert "term" not in hemin_components[repair_module.NAOH_STOCK]


def test_repair_is_idempotent(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repair_module.repair_record(repaired) == repaired
