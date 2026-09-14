from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_1224_widdel_glycerin_score15.py"
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
    return _load_script(SCRIPT, "repair_jcm_1224_widdel_glycerin_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_1224_widdel_glycerin")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "widdel_freshwater_medium_with_glycerin",
        "original_name": "WIDDEL FRESHWATER MEDIUM WITH GLYCERIN",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "JCM Medium J1224",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "WIDDEL FRESHWATER MEDIUM WITH GLYCERIN",
            },
        },
        "notes": "Source: JCM",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": [
            "incomplete_composition",
            "source_information_unavailable",
        ],
    }


def _parent_doc(repair_module) -> dict:
    return {
        "id": repair_module.PARENT_ID,
        "name": "widdel_freshwater_medium_with_lactate",
        "original_name": "WIDDEL FRESHWATER MEDIUM WITH LACTATE",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "JCM Medium J1223",
            "term": {
                "id": repair_module.PARENT_MEDIA_TERM,
                "label": "WIDDEL FRESHWATER MEDIUM WITH LACTATE",
            },
        },
        "ingredients": [],
        "curation_history": [],
        "variant_children": [
            {"id": "CultureMech:099999", "name": "unrelated", "path": "data/normalized_yaml/bacterial/x.yaml"}
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_expands_widdel_glycerin_and_scores_cleanly(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])
    glycerin = _by_name(solutions["1 M glycerin solution"]["composition"])

    assert repaired["medium_type"] == "DEFINED"
    assert repaired["composition_type"] == "DEFINED"
    assert repaired["ph_value"] == 7.5
    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert ingredients["CaCl2 x 2 H2O"]["term"] == {
        "id": "CHEBI:86158",
        "label": "calcium chloride dihydrate",
    }
    assert ingredients["MgCl2 x 6 H2O"]["term"] == {
        "id": "CHEBI:86345",
        "label": "magnesium dichloride hexahydrate",
    }
    assert ingredients["N2"]["term"] == {"id": "CHEBI:17997", "label": "dinitrogen"}
    assert glycerin["Glycerol"]["concentration"] == {"value": "1.0", "unit": "MOLAR"}
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_expands_jcm_301_trace_and_jcm_431_selenite_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    trace = _by_name(solutions["Trace element solution"]["composition"])
    selenite = _by_name(solutions["Selenite-tungstate solution"]["composition"])

    assert trace["Nitrilotriacetic acid"]["concentration"] == {
        "value": "12.8",
        "unit": "G_PER_L",
    }
    assert trace["ZnSO4 x 7 H2O"]["term"] == {
        "id": "CHEBI:32312",
        "label": "zinc sulfate heptahydrate",
    }
    assert trace["NaOH"]["concentration"] == {"value": "variable", "unit": "VARIABLE"}
    assert trace["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert selenite["Na2SeO3 x 5 H2O"]["term"] == {
        "id": "CHEBI:131361",
        "label": "disodium selenite pentahydrate",
    }


def test_repair_expands_jcm_403_vitamin_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    vitamins = _by_name(solutions["Vitamin solution"]["composition"])
    thiamine = _by_name(solutions["Thiamine solution"]["composition"])
    b12 = _by_name(solutions["Vitamin B12 solution"]["composition"])

    assert vitamins["p-Aminobenzoic acid"]["concentration"] == {
        "value": "40.0",
        "unit": "MG_PER_L",
    }
    assert "term" not in vitamins["Sodium phosphate buffer (10 mM, pH 7.1)"]
    assert thiamine["Thiamine HCl"]["concentration"] == {
        "value": "100.0",
        "unit": "MG_PER_L",
    }
    assert "term" not in thiamine["Sodium phosphate buffer (25 mM, pH 3.4)"]
    assert b12["Vitamin B12"]["concentration"] == {
        "value": "50.0",
        "unit": "MG_PER_L",
    }


def test_repair_adds_variant_references_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice == once
    assert once["parent_media"] == repair_module.PARENT_MEDIA
    assert once["variant_relationship"] == "SUBSTITUTED_COMPONENT_VARIANT"
    assert once["variant_modifications"] == repair_module.VARIANT_MODIFICATIONS
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert {row["reference"] for row in once["references"]} == set(repair_module._references())

    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == "; ".join(repair_module._references())


def test_repair_adds_child_reference_to_parent_idempotently(repair_module) -> None:
    once = repair_module.repair_parent(_parent_doc(repair_module))
    twice = repair_module.repair_parent(once)

    assert twice == once
    assert once["variant_children"] == [
        {"id": "CultureMech:099999", "name": "unrelated", "path": "data/normalized_yaml/bacterial/x.yaml"},
        repair_module.CHILD_REFERENCE,
    ]


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:002391"):
        repair_module.repair_record(doc)
