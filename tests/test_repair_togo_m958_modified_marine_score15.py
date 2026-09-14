from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m958_modified_marine_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m958_modified_marine_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_m958")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(signature) -> dict:
    name, value, unit, composition = signature
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "composition": [
            _component(component_name, component_value, component_unit)
            for component_name, component_value, component_unit in composition
        ],
    }


def _medium_doc(repair_module, *, record: str) -> dict:
    params = {
        "m958": (
            "CultureMech:010382",
            "TOGO:M958",
            repair_module.M958_IMPORTED,
            (),
        ),
        "m1345": (
            "CultureMech:007881",
            "TOGO:M1345",
            repair_module.M1345_IMPORTED,
            (),
        ),
        "m1274": (
            "CultureMech:007807",
            "TOGO:M1274",
            repair_module.M1274_IMPORTED,
            repair_module.M1274_IMPORTED_SOLUTIONS,
        ),
    }[record]
    record_id, source_id, ingredients, solutions = params
    return {
        "id": record_id,
        "name": "modified_marine_agar_2216",
        "original_name": "Modified Marine Agar 2216",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _component(name, value, unit) for name, value, unit in ingredients
        ],
        "solutions": [_solution(signature) for signature in solutions],
        "media_term": {
            "preferred_term": source_id,
            "term": {"id": source_id, "label": "Modified Marine Agar 2216"},
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_m958_water_unit_and_ph_are_repaired(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_m958(_medium_doc(repair_module, record="m958"))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["ph_value"] == 7.5
    assert repair_module._signature(
        repaired["ingredients"], "ingredients"
    ) == repair_module.M958_FINAL
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients["Malt extract (BD-Difco)"]["term"] == {
        "id": "FOODON:03301056",
        "label": "malt extract",
    }
    assert ingredients["Malt extract (BD-Difco)"]["nutritional_roles"] == [
        "CARBON_SOURCE",
        "NITROGEN_SOURCE",
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_m1345_uses_phytone_specific_signature(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_m1345(_medium_doc(repair_module, record="m1345"))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["ph_value"] == 7.5
    assert repair_module._signature(
        repaired["ingredients"], "ingredients"
    ) == repair_module.M1345_FINAL
    assert ingredients["Phytone peptone (BD-Difco)"]["term"] == {
        "id": "FOODON:03315720",
        "label": "Soy peptone",
    }
    assert scorer_module.score_record(repaired) == (0, [])


def test_m1274_expands_trace_vitamins_and_carbonate_stock(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_m1274(_medium_doc(repair_module, record="m1274"))
    solutions = _by_name(repaired["solutions"])

    assert repaired["ph_value"] == 9.0
    assert repair_module._signature(
        repaired["ingredients"], "ingredients"
    ) == repair_module.M1274_FINAL
    assert repair_module._solution_signatures(
        repaired["solutions"], "solutions"
    ) == repair_module.M1274_FINAL_SOLUTIONS
    assert solutions["Trace vitamins"]["concentration"] == {
        "value": "10.0",
        "unit": "ML_PER_L",
    }
    assert solutions["10% Na2CO3 solution"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:29377",
        "label": "sodium carbonate",
    }
    assert "physicochemical_roles" not in solutions["10% Na2CO3 solution"]
    assert solutions["10% Na2CO3 solution"]["composition"][0][
        "physicochemical_roles"
    ] == ["BUFFER"]
    assert _by_name(repaired["ingredients"])["NaCl"]["physicochemical_roles"] == [
        "OSMOTIC_AGENT"
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_repairs_are_idempotent(repair_module) -> None:
    for function, record in (
        (repair_module.repair_m958, "m958"),
        (repair_module.repair_m1345, "m1345"),
        (repair_module.repair_m1274, "m1274"),
    ):
        once = function(_medium_doc(repair_module, record=record))
        twice = function(once)
        assert twice == once


def test_m958_rejects_wrong_source(repair_module) -> None:
    doc = _medium_doc(repair_module, record="m958")
    doc["media_term"]["term"]["id"] = "TOGO:wrong"

    with pytest.raises(ValueError, match="TOGO:M958"):
        repair_module.repair_m958(doc)


def test_m1274_rejects_solution_drift(repair_module) -> None:
    doc = _medium_doc(repair_module, record="m1274")
    doc["solutions"][0]["preferred_term"] = "Trace vitamins"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_m1274(doc)
