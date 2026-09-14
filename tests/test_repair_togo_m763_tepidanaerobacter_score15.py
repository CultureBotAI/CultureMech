from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m763_tepidanaerobacter_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m763_tepidanaerobacter_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m763")


@pytest.fixture(scope="module")
def audit_module():
    return _load_script(
        CONCENTRATION_AUDIT,
        "audit_concentration_plausibility_for_togo_m763",
    )


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
    }


def _doc(repair_module, target) -> dict:
    return {
        "id": target.record_id,
        "name": "bm_for_tepidanaerobacter_acetoxydans",
        "original_name": "BM For Tepidanaerobacter Acetoxydans",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "SEMI_DEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_ingredients
        ],
        "media_term": {
            "preferred_term": target.media_term,
            "term": {"id": target.media_term, "label": "BM For Tepidanaerobacter"},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in target.imported_solutions
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_expands_jcm_738_formula(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.JCM_TARGET),
        repair_module.JCM_TARGET,
    )

    ingredients = _by_name(repaired["ingredients"])
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "830.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Resazurin"]["concentration"] == {
        "value": "0.5",
        "unit": "MG_PER_L",
    }
    assert ingredients["CaCl2 x 2H2O"]["term"] == {
        "id": "CHEBI:86158",
        "label": "calcium chloride dihydrate",
    }
    assert ingredients["MgCl2 x 6H2O"]["term"] == {
        "id": "CHEBI:86345",
        "label": "magnesium dichloride hexahydrate",
    }


def test_repair_expands_togo_m763_solution_wrappers(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.TOGO_TARGET),
        repair_module.TOGO_TARGET,
    )

    solutions = _by_name(repaired["solutions"])
    assert set(solutions) == {
        "Trace metal solution (TOGO Medium M288)",
        "Selenite-tungstate solution (TOGO Medium M431)",
        "8% NaHCO3 solution",
        "0.1 M glucose solution",
        "5% Na2S x 9H2O solution",
        "Phosphate solution (TOGO Medium M762)",
        "Trace vitamins (TOGO Medium M190)",
    }
    assert all(sol["concentration"]["unit"] == "ML_PER_L" for sol in solutions.values())

    trace = _by_name(solutions["Trace metal solution (TOGO Medium M288)"]["composition"])
    selenite = _by_name(
        solutions["Selenite-tungstate solution (TOGO Medium M431)"]["composition"]
    )

    assert trace["AlCl3"]["term"] == {
        "id": "CHEBI:30114",
        "label": "aluminium trichloride",
    }
    assert trace["FeCl2 x 4H2O"]["concentration"] == {
        "value": "2.0",
        "unit": "G_PER_L",
    }
    assert selenite["Na2SeO3 x 5H2O"]["concentration"] == {
        "value": "6.0",
        "unit": "MG_PER_L",
    }


def test_repair_converts_100_ml_phosphate_stock_to_per_liter(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.JCM_TARGET),
        repair_module.JCM_TARGET,
    )

    phosphate = _by_name(
        _by_name(repaired["solutions"])["Phosphate solution (TOGO Medium M762)"][
            "composition"
        ]
    )
    assert phosphate["KH2PO4"]["concentration"] == {
        "value": "4.1",
        "unit": "G_PER_L",
    }
    assert phosphate["Na2HPO4"]["concentration"] == {
        "value": "4.3",
        "unit": "G_PER_L",
    }
    assert "100 ml" in phosphate["KH2PO4"]["notes"]


def test_repair_expands_percent_molar_and_vitamin_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.JCM_TARGET),
        repair_module.JCM_TARGET,
    )

    solutions = _by_name(repaired["solutions"])
    bicarbonate = _by_name(solutions["8% NaHCO3 solution"]["composition"])
    glucose = _by_name(solutions["0.1 M glucose solution"]["composition"])
    sulfide = _by_name(solutions["5% Na2S x 9H2O solution"]["composition"])
    vitamins = _by_name(solutions["Trace vitamins (TOGO Medium M190)"]["composition"])

    assert bicarbonate["NaHCO3"]["concentration"] == {
        "value": "8.0",
        "unit": "PERCENT_W_V",
    }
    assert glucose["Glucose"]["concentration"] == {
        "value": "0.1",
        "unit": "MOLAR",
    }
    assert sulfide["Na2S x 9H2O"]["physicochemical_roles"] == ["REDUCING_AGENT"]
    assert vitamins["Pyridoxine HCl"]["concentration"] == {
        "value": "10.0",
        "unit": "MG_PER_L",
    }


def test_repair_links_jcm_parent_and_togo_source_duplicate(repair_module) -> None:
    jcm = repair_module.repair_record(
        _doc(repair_module, repair_module.JCM_TARGET),
        repair_module.JCM_TARGET,
    )
    togo = repair_module.repair_record(
        _doc(repair_module, repair_module.TOGO_TARGET),
        repair_module.TOGO_TARGET,
    )

    assert jcm["variant_children"] == [repair_module.TOGO_CHILD]
    assert togo["parent_media"] == repair_module.JCM_PARENT
    assert togo["variant_relationship"] == "SOURCE_DUPLICATE"
    assert togo["variant_modifications"] == [
        "Same JCM Medium 738 formulation as the MediaDive J738 source record."
    ]


def test_repair_drops_records_from_review_and_concentration_audits(
    repair_module,
    scorer_module,
    audit_module,
) -> None:
    parsed = []
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(repair_module, target), target)
        parsed.append((str(target.path), repaired))
        assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
        assert repaired["data_quality_flags"] == [
            "has_ontology_mappings",
            "ingredients_curated",
        ]

    assert scorer_module.score_parsed(parsed) == []
    assert audit_module.audit_parsed(parsed) == []


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(
        _doc(repair_module, repair_module.JCM_TARGET),
        repair_module.JCM_TARGET,
    )
    twice = repair_module.repair_record(once, repair_module.JCM_TARGET)

    events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair_module.CURATOR
        and event.get("action") == repair_module.ACTION
    ]
    assert len(events) == 1
    assert len(twice["references"]) == len(repair_module.JCM_TARGET.references)
