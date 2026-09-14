from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m873_syfac_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"
PLACEHOLDER_INGREDIENTS = (("See source for composition", "variable", "VARIABLE"),)


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m873_syfac_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_m873")


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
        "name": "syfac_medium",
        "original_name": "Syfac Medium",
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
            "term": {"id": target.source_term, "label": target.source_name},
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


def _solution_doc(record_id: str, composition: tuple) -> dict:
    return {
        "id": record_id,
        "preferred_term": "solution",
        "term": {
            "id": "mediadive.solution:0000",
            "label": "solution",
        },
        "composition": [
            _ingredient(name, value, unit)
            for name, value, unit in composition
        ],
        "preparation_notes": "Original volume",
        "curation_history": [],
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in PLACEHOLDER_INGREDIENTS
        ],
        "data_quality_flags": ["incomplete_composition"],
        "category": "bacterial",
    }


def _repair_medium(repair_module, path: Path) -> dict:
    target = next(target for target in repair_module.TARGETS if target.path == path)
    return repair_module.repair_medium_record(_medium_doc(target), target)


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_jcm_j837_becomes_canonical_parent(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair_medium(repair_module, repair_module.MEDIADIVE_J837_PATH)

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.DIRECT_COMPOSITION
    assert repair_module._solution_signature(
        repaired["solutions"],
        "solutions",
    ) == repair_module.FINAL_SOLUTIONS
    assert repaired["variant_children"] == [repair_module.M873_CHILD]
    assert "parent_media" not in repaired
    assert "has_unmapped_ingredients" in repaired["data_quality_flags"]
    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed([("bacterial/syfac_medium.yaml", repaired)]) == []


def test_togo_m873_links_to_jcm_source_duplicate(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair_medium(repair_module, repair_module.TOGO_M873_PATH)

    assert repaired["parent_media"] == repair_module.J837_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.M873_CHILD["notes"]]
    assert "variant_children" not in repaired
    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed(
        [("bacterial/TOGO_M873_Syfac_Medium.yaml", repaired)]
    ) == []


def test_repair_corrects_main_units_and_groundings(repair_module) -> None:
    repaired = _repair_medium(repair_module, repair_module.TOGO_M873_PATH)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "925.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Resazurin"]["concentration"] == {
        "value": "0.5",
        "unit": "MG_PER_L",
    }
    assert ingredients["Resazurin"]["physicochemical_roles"] == [
        "REDOX_INDICATOR",
    ]
    assert ingredients["Sea salts (Sigma)"]["concentration"] == {
        "value": "35.0",
        "unit": "G_PER_L",
    }
    assert "term" not in ingredients["Sea salts (Sigma)"]
    assert ingredients["Yeast extract (BD-Difco)"]["term"] == {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    }
    assert ingredients["Carbon dioxide gas"]["term"] == {
        "id": "CHEBI:16526",
        "label": "carbon dioxide",
    }


def test_repair_expands_wolfe_and_trace_vitamin_stocks(repair_module) -> None:
    repaired = _repair_medium(repair_module, repair_module.TOGO_M873_PATH)
    solutions = _by_name(repaired["solutions"])
    wolfe = _by_name(solutions["Wolfe's mineral elixir"]["composition"])
    vitamins = _by_name(solutions["Trace vitamins"]["composition"])

    assert solutions["Wolfe's mineral elixir"]["term"] == {
        "id": "mediadive.solution:4221",
        "label": "Wolfe's mineral elixir",
    }
    assert solutions["Wolfe's mineral elixir"]["culturemech_term"] == {
        "id": "CultureMech:013242",
        "label": "Wolfe's mineral elixir",
    }
    assert wolfe["MnSO4 x n H2O"]["term"] == {
        "id": "CHEBI:86360",
        "label": "manganese(II) sulfate",
    }
    assert wolfe["AlK(SO4)2 x 12 H2O"]["term"] == {
        "id": "CHEBI:86465",
        "label": "potassium aluminium sulfate dodecahydrate",
    }
    assert wolfe["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert vitamins["Vitamin B12"]["concentration"] == {
        "value": "0.1",
        "unit": "MG_PER_L",
    }


def test_repair_expands_percent_and_molar_stocks(repair_module) -> None:
    repaired = _repair_medium(repair_module, repair_module.TOGO_M873_PATH)
    solutions = _by_name(repaired["solutions"])

    bicarbonate = _by_name(solutions["8% NaHCO3 solution"]["composition"])
    acetate = _by_name(solutions["1 M Sodium acetate solution"]["composition"])
    fumarate = _by_name(solutions["1 M Sodium fumarate solution"]["composition"])
    sulfide = _by_name(solutions["5% Na2S x 9 H2O solution"]["composition"])

    assert solutions["8% NaHCO3 solution"]["term"] == {
        "id": "CHEBI:32139",
        "label": "sodium hydrogencarbonate",
    }
    assert bicarbonate["NaHCO3"]["concentration"] == {
        "value": "80.0",
        "unit": "G_PER_L",
    }
    assert acetate["Sodium acetate"]["concentration"] == {
        "value": "1.0",
        "unit": "MOLAR",
    }
    assert fumarate["Sodium fumarate"]["concentration"] == {
        "value": "1.0",
        "unit": "MOLAR",
    }
    assert sulfide["Na2S x 9 H2O"]["concentration"] == {
        "value": "50.0",
        "unit": "G_PER_L",
    }


def test_solution_4801_uses_flat_asserted_additions(repair_module) -> None:
    doc = _solution_doc(
        "CultureMech:013742",
        repair_module.IMPORTED_SOLUTION_4801_COMPOSITION,
    )
    repaired = repair_module.repair_solution_4801_record(doc)
    composition = _by_name(repaired["composition"])

    assert "ingredients" not in repaired
    assert repair_module._signature(
        repaired["composition"],
        "composition",
    ) == repair_module.SOLUTION_4801_COMPOSITION
    assert composition["Sea salts (Sigma)"]["concentration"] == {
        "value": "35.0",
        "unit": "G_PER_L",
    }
    assert "term" not in composition["Sea salts (Sigma)"]
    assert composition["Wolfe's mineral elixir"]["culturemech_term"] == {
        "id": "CultureMech:013242",
        "label": "Wolfe's mineral elixir",
    }
    assert composition["1 M Sodium fumarate solution"]["term"] == {
        "id": "CHEBI:115156",
        "label": "disodium fumarate",
    }
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]


def test_solution_4221_corrects_wolfe_water_unit(repair_module) -> None:
    doc = _solution_doc(
        "CultureMech:013242",
        repair_module.IMPORTED_SOLUTION_4221_COMPOSITION,
    )
    repaired = repair_module.repair_solution_4221_record(doc)
    composition = _by_name(repaired["composition"])

    assert "ingredients" not in repaired
    assert repair_module._signature(
        repaired["composition"],
        "composition",
    ) == repair_module.WOLFE_COMPOSITION
    assert composition["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    target = next(
        target
        for target in repair_module.TARGETS
        if target.path == repair_module.TOGO_M873_PATH
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
        "has_unmapped_ingredients",
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair_module.CURATOR
        and event.get("action") == target.action
    ]
    assert len(matching_events) == 1
    assert repair_module.TOGO_M873 in matching_events[0]["source"]
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
        if target.path == repair_module.TOGO_M873_PATH
    )
    doc = _medium_doc(target)
    doc["solutions"].pop()

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_medium_record(doc, target)


def test_repair_rejects_solution_composition_drift(repair_module) -> None:
    doc = _solution_doc(
        "CultureMech:013742",
        repair_module.IMPORTED_SOLUTION_4801_COMPOSITION,
    )
    doc["composition"].pop()

    with pytest.raises(ValueError, match="composition signature drifted"):
        repair_module.repair_solution_4801_record(doc)
