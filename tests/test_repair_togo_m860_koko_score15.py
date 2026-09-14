from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m860_koko_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m860_koko_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_m860")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(signature) -> dict:
    name, value, unit, composition = signature
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "composition": [
            _ingredient(component_name, component_value, component_unit)
            for component_name, component_value, component_unit in composition
        ],
    }


def _medium_doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": "koko_medium",
        "original_name": "KOKO Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_ingredients
        ],
        "solutions": [_solution(row) for row in target.imported_solutions],
        "media_term": {
            "preferred_term": "source medium",
            "term": {"id": target.source_term, "label": "KOKO Medium"},
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": [
            "incomplete_composition",
            "needs_manual_curation",
            "resolved_reference",
        ],
    }


def _solution_doc(repair_module) -> dict:
    return {
        "id": "CultureMech:013726",
        "preferred_term": "Main sol. J825",
        "term": {
            "id": "mediadive.solution:4784",
            "label": "Main sol. J825",
        },
        "composition": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_SOLUTION_4784_COMPOSITION
        ],
        "preparation_notes": (
            "Mix components thoroughly and adjust pH to 7.0. Autoclave the "
            "medium under a N2 atmosphere. Add the following solutions from "
            "sterile anaerobic stocks."
        ),
        "curation_history": [],
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.PLACEHOLDER_INGREDIENTS
        ],
        "data_quality_flags": ["incomplete_composition"],
        "category": "bacterial",
    }


def _repair_medium(repair_module, path: Path) -> dict:
    target = next(target for target in repair_module.TARGETS if target.path == path)
    return repair_module.repair_medium_record(_medium_doc(target), target)


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_jcm_j825_becomes_canonical_parent(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair_medium(repair_module, repair_module.JCM_J825_PATH)

    assert repaired["ph_range"] == {"min": 7.0, "max": 7.0}
    assert "ph_value" not in repaired
    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.DIRECT_COMPOSITION
    assert repair_module._solution_signature(
        repaired["solutions"],
        "solutions",
    ) == repair_module.FINAL_SOLUTIONS
    assert repaired["variant_children"] == [repair_module.M860_CHILD]
    assert "parent_media" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_togo_m860_links_to_jcm_source_duplicate(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair_medium(repair_module, repair_module.TOGO_M860_PATH)

    assert repaired["parent_media"] == repair_module.J825_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.M860_CHILD["notes"]]
    assert "variant_children" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_corrects_main_units_and_groundings(repair_module) -> None:
    repaired = _repair_medium(repair_module, repair_module.TOGO_M860_PATH)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "930.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Resazurin"]["concentration"] == {
        "value": "0.5",
        "unit": "MG_PER_L",
    }
    assert ingredients["Resazurin"]["physicochemical_roles"] == [
        "REDOX_INDICATOR",
    ]
    assert ingredients["Tryptone (BD-Difco)"]["term"] == {
        "id": "MICRO:0000182",
        "label": "Tryptone",
    }
    assert ingredients["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "Peptone",
    }
    assert ingredients["N2"]["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }


def test_repair_expands_cross_referenced_stock_compositions(repair_module) -> None:
    repaired = _repair_medium(repair_module, repair_module.TOGO_M860_PATH)
    solutions = _by_name(repaired["solutions"])
    sl4 = _by_name(solutions["Trace element solution SL-4"]["composition"])
    vitamins = _by_name(solutions["Trace vitamins"]["composition"])

    assert solutions["Trace element solution SL-4"]["concentration"] == {
        "value": "10.0",
        "unit": "ML_PER_L",
    }
    assert solutions["Trace element solution SL-4"]["culturemech_term"] == {
        "id": "CultureMech:013111",
        "label": "Trace element solution SL-4",
    }
    assert sl4["EDTA"]["physicochemical_roles"] == ["CHELATOR"]
    assert sl4["NiCl2 x 6 H2O"]["concentration"] == {
        "value": "0.002",
        "unit": "G_PER_L",
    }
    assert sl4["NiCl2 x 6 H2O"]["term"] == {
        "id": "CHEBI:53542",
        "label": "nickel chloride hexahydrate",
    }
    assert sl4["Distilled water"]["concentration"] == {
        "value": "900.0",
        "unit": "ML_PER_L",
    }
    assert vitamins["Biotin"]["concentration"] == {
        "value": "2.0",
        "unit": "MG_PER_L",
    }
    assert vitamins["Vitamin B12"]["concentration"] == {
        "value": "0.1",
        "unit": "MG_PER_L",
    }


def test_repair_expands_percent_stocks(repair_module) -> None:
    repaired = _repair_medium(repair_module, repair_module.TOGO_M860_PATH)
    solutions = _by_name(repaired["solutions"])

    bicarbonate = _by_name(solutions["8% NaHCO3 solution"]["composition"])
    glucose = _by_name(solutions["10% Glucose solution"]["composition"])
    sulfide = _by_name(solutions["3% Na2S x 9 H2O solution"]["composition"])
    cysteine = _by_name(
        solutions["3% L-Cysteine HCl x H2O solution"]["composition"],
    )

    assert solutions["8% NaHCO3 solution"]["term"] == {
        "id": "CHEBI:32139",
        "label": "sodium hydrogencarbonate",
    }
    assert solutions["3% Na2S x 9 H2O solution"]["term"] == {
        "id": "CHEBI:76209",
        "label": "sodium sulfide nonahydrate",
    }
    assert bicarbonate["NaHCO3"]["concentration"] == {
        "value": "80.0",
        "unit": "G_PER_L",
    }
    assert glucose["Glucose"]["concentration"] == {
        "value": "100.0",
        "unit": "G_PER_L",
    }
    assert sulfide["Na2S x 9 H2O"]["concentration"] == {
        "value": "30.0",
        "unit": "G_PER_L",
    }
    assert cysteine["L-Cysteine HCl x H2O"]["physicochemical_roles"] == [
        "REDUCING_AGENT",
    ]


def test_solution_helper_uses_flat_asserted_additions(repair_module) -> None:
    repaired = repair_module.repair_solution_record(_solution_doc(repair_module))
    composition = _by_name(repaired["composition"])

    assert "ingredients" not in repaired
    assert repair_module._signature(
        repaired["composition"],
        "composition",
    ) == repair_module.SOLUTION_4784_COMPOSITION
    assert composition["Resazurin"]["concentration"] == {
        "value": "0.5",
        "unit": "MG_PER_L",
    }
    assert composition["Distilled water"]["concentration"] == {
        "value": "930.0",
        "unit": "ML_PER_L",
    }
    assert composition["Trace element solution SL-4"]["culturemech_term"] == {
        "id": "CultureMech:013111",
        "label": "Trace element solution SL-4",
    }
    assert composition["10% Glucose solution"]["term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    target = next(
        target
        for target in repair_module.TARGETS
        if target.path == repair_module.TOGO_M860_PATH
    )
    once = repair_module.repair_medium_record(_medium_doc(target), target)
    twice = repair_module.repair_medium_record(once, target)

    assert twice == once
    assert once["references"] == [
        {"reference": reference} for reference in target.references
    ]
    assert once["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair_module.CURATOR
        and event.get("action") == target.action
    ]
    assert len(matching_events) == 1
    assert repair_module.TOGO_M860 in matching_events[0]["source"]
    assert "resazurin" in matching_events[0]["notes"]


def test_repair_rejects_wrong_medium_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _medium_doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_medium_record(doc, target)


def test_repair_rejects_medium_solution_drift(repair_module) -> None:
    target = next(
        target
        for target in repair_module.TARGETS
        if target.path == repair_module.TOGO_M860_PATH
    )
    doc = _medium_doc(target)
    doc["solutions"].pop()

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_medium_record(doc, target)


def test_repair_rejects_solution_composition_drift(repair_module) -> None:
    doc = _solution_doc(repair_module)
    doc["composition"].pop()

    with pytest.raises(ValueError, match="composition signature drifted"):
        repair_module.repair_solution_record(doc)
