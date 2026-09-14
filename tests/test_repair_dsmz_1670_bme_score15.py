from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_1670_bme_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"
CONCENTRATION_AUDIT = REPO / "scripts" / "audit_concentration_plausibility.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_dsmz_1670_bme_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_1670_bme")


@pytest.fixture(scope="module")
def audit_module():
    return _load_script(
        CONCENTRATION_AUDIT,
        "audit_concentration_plausibility_for_dsmz_1670_bme",
    )


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _parent_doc(repair_module) -> dict:
    return {
        "id": repair_module.PARENT_ID,
        "name": "bme_ctvm2_cell_line_medium_occidentia_massiliensis",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "DSMZ Medium 1670",
            "term": {
                "id": repair_module.MEDIA_TERM,
                "label": "BME/CTVM2 cell line medium (Occidentia massiliensis)",
            },
        },
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_PARENT_INGREDIENTS
        ],
        "curation_history": [],
    }


def _solution_doc(repair_module) -> dict:
    return {
        "id": repair_module.SOLUTION_ID,
        "preferred_term": "Main sol. 1670",
        "term": {
            "id": repair_module.SOLUTION_TERM,
            "label": "Main sol. 1670",
        },
        "composition": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_SOLUTION_COMPOSITION
        ],
        "ingredients": [_ingredient("See source for composition", "variable", "VARIABLE")],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_parent_converts_101_ml_batch_volumes(
    repair_module,
    scorer_module,
    audit_module,
) -> None:
    repaired = repair_module.repair_parent(_parent_doc(repair_module))

    ingredients = _by_name(repaired["ingredients"])
    assert ingredients["L-15 (Leibovitz) medium"]["concentration"] == {
        "value": "693.069307",
        "unit": "ML_PER_L",
    }
    assert ingredients["Tryptose phosphate broth"]["concentration"] == {
        "value": "99.009901",
        "unit": "ML_PER_L",
    }
    assert ingredients["Foetal calf serum"]["concentration"] == {
        "value": "198.019802",
        "unit": "ML_PER_L",
    }
    assert ingredients["Foetal calf serum"]["term"] == {
        "id": "mediadive.compound:954",
        "label": "Fetal bovine serum",
    }
    assert repaired["temperature_value"] == 28.0
    assert scorer_module.score_record(repaired) == (0, [])
    assert audit_module.audit_parsed([(str(repair_module.PARENT_PATH), repaired)]) == []


def test_repair_represents_200_mm_glutamine_as_stock_solution(repair_module) -> None:
    repaired = repair_module.repair_parent(_parent_doc(repair_module))

    assert len(repaired["solutions"]) == 1
    stock = repaired["solutions"][0]
    assert stock["preferred_term"] == "200 mM L-glutamine stock"
    assert stock["concentration"] == {"value": "9.90099", "unit": "ML_PER_L"}

    composition = _by_name(stock["composition"])
    assert composition["L-Glutamine"]["concentration"] == {
        "value": "200.0",
        "unit": "MILLIMOLAR",
    }
    assert composition["L-Glutamine"]["term"] == {
        "id": "CHEBI:18050",
        "label": "L-glutamine",
    }


def test_repair_solution_drops_placeholder_and_uses_same_composition(repair_module) -> None:
    repaired = repair_module.repair_solution(_solution_doc(repair_module))

    assert "ingredients" not in repaired
    assert [row["preferred_term"] for row in repaired["composition"]] == [
        name for name, _value, _unit in repair_module.FINAL_INGREDIENTS
    ]
    assert repaired["solutions"] == [repair_module._glutamine_stock()]
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    normalized = tmp_path / "normalized"
    parent = normalized / repair_module.PARENT_PATH
    solution = normalized / repair_module.SOLUTION_PATH
    parent.parent.mkdir(parents=True)
    parent.write_text(repair_module.dump_record(_parent_doc(repair_module)), encoding="utf-8")
    solution.write_text(
        repair_module.dump_record(_solution_doc(repair_module)),
        encoding="utf-8",
    )

    first = repair_module.plan_repairs(normalized)
    assert {path.relative_to(normalized) for path in first} == {
        repair_module.PARENT_PATH,
        repair_module.SOLUTION_PATH,
    }
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    assert repair_module.plan_repairs(normalized) == {}


def test_repair_rejects_wrong_targets(repair_module) -> None:
    parent = _parent_doc(repair_module)
    parent["id"] = "CultureMech:999999"
    with pytest.raises(ValueError, match="expected id CultureMech:001155"):
        repair_module.repair_parent(parent)

    solution = _solution_doc(repair_module)
    solution["term"]["id"] = "mediadive.solution:9999"
    with pytest.raises(ValueError, match="expected solution term mediadive.solution:3465"):
        repair_module.repair_solution(solution)
