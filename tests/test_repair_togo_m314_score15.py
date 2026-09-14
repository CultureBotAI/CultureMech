from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m314_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m314_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m314")


@pytest.fixture(scope="module")
def m298_doc():
    path = REPO / "data" / "normalized_yaml" / "bacterial" / "TOGO_M298_PE_Medium.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "composition": [],
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "togo_medium_m314",
        "original_name": "(Unnamed medium)",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in repair_module.LEGACY_INGREDIENTS
        ],
        "solutions": [
            _solution("Basal salts solution (see Medium [M298])", "5", "G_PER_L"),
            _solution("Phosphate solution (see Medium [M298])", "10", "G_PER_L"),
            _solution("Vitamin solution (see Medium [M298])", "1", "G_PER_L"),
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M314",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "TOGO Medium M314",
            },
        },
        "notes": "Source: JCM - JCM_M319",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_expands_m298_solution_references(repair_module, scorer_module, m298_doc) -> None:
    repaired = repair_module.repair_target(_doc(repair_module), m298_doc)

    assert repaired["ph_value"] == 7.2
    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert (
        repair_module._component_signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENTS
    )
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_converts_imported_milliliters_to_stock_solutions(repair_module, m298_doc) -> None:
    repaired = repair_module.repair_target(_doc(repair_module), m298_doc)
    solutions = _by_name(repaired["solutions"])

    assert set(solutions) == {
        "Basal salts solution",
        "Phosphate solution",
        "Vitamin solution",
    }
    assert solutions["Basal salts solution"]["concentration"] == {
        "value": "5",
        "unit": "ML_PER_L",
    }
    assert solutions["Phosphate solution"]["concentration"] == {
        "value": "10",
        "unit": "ML_PER_L",
    }
    assert solutions["Vitamin solution"]["concentration"] == {
        "value": "1",
        "unit": "ML_PER_L",
    }


def test_repair_nests_trace_elements_inside_basal_salts(repair_module, m298_doc) -> None:
    repaired = repair_module.repair_target(_doc(repair_module), m298_doc)
    basal = _by_name(repaired["solutions"])["Basal salts solution"]
    nested = _by_name(basal["solutions"])

    assert set(nested) == {"Trace elements solution"}
    assert nested["Trace elements solution"]["concentration"] == {
        "value": "10",
        "unit": "ML_PER_L",
    }
    trace_components = _by_name(nested["Trace elements solution"]["composition"])
    assert trace_components["Na2MoO4 x 2 H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:75213",
        "label": "sodium molybdate dihydrate",
    }


def test_repair_corrects_water_and_defined_component_groundings(repair_module, m298_doc) -> None:
    repaired = repair_module.repair_target(_doc(repair_module), m298_doc)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients["Na2S2O3・5H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:32150",
        "label": "sodium thiosulfate pentahydrate",
    }
    assert "term" not in ingredients["Yeast extract (BD-Difco)"]
    assert "term" not in ingredients["Casamino acids (BD-Difco)"]


def test_repair_adds_source_stated_preparation_steps(repair_module, m298_doc) -> None:
    repaired = repair_module.repair_target(_doc(repair_module), m298_doc)

    assert "temperature_value" not in repaired
    assert "temperature_range" not in repaired
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)


def test_repair_adds_references_and_event_once(repair_module, m298_doc) -> None:
    once = repair_module.repair_target(_doc(repair_module), m298_doc)
    twice = repair_module.repair_target(once, m298_doc)

    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
    ]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
        "legacy_source_url_unavailable",
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert "expanded Basal salts" in matching_events[0]["notes"]


def test_plan_repairs_target_record(repair_module) -> None:
    target_path = repair_module.NORMALIZED / repair_module.TARGET
    m298 = yaml.safe_load((repair_module.NORMALIZED / repair_module.M298).read_text())
    expected_target = repair_module.repair_target(
        yaml.safe_load(target_path.read_text(encoding="utf-8")),
        m298,
    )

    assert repair_module.plan_repairs() == {target_path: expected_target}


def test_repair_rejects_wrong_id(repair_module, m298_doc) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_target(doc, m298_doc)


def test_repair_rejects_wrong_media_term(repair_module, m298_doc) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M315"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_target(doc, m298_doc)


def test_repair_rejects_solution_drift(repair_module, m298_doc) -> None:
    doc = _doc(repair_module)
    doc["solutions"][1] = _solution("Phosphate solution (see Medium [M298])", "5", "G_PER_L")

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_target(doc, m298_doc)


def test_repair_rejects_m298_drift(repair_module, m298_doc) -> None:
    del _by_name(m298_doc["solutions"])["Trace elements solution"]["composition"][:]

    with pytest.raises(ValueError, match="lacks composition"):
        repair_module.repair_target(_doc(repair_module), m298_doc)


def test_target_record_matches_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    m298 = yaml.safe_load((repair_module.NORMALIZED / repair_module.M298).read_text())
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._component_signature(doc["ingredients"], "ingredients") in {
        repair_module.LEGACY_INGREDIENTS,
        repair_module.FINAL_INGREDIENTS,
    }
    assert repair_module._solution_signatures(doc.get("solutions"), "solutions") in {
        repair_module.LEGACY_SOLUTIONS,
        repair_module._solution_signatures(repair_module._solutions(m298), "solutions"),
    }
