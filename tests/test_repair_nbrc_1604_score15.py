from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_1604_score15.py"
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
    return _load_script(SCRIPT, "repair_nbrc_1604_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_nbrc_1604")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "togo_medium_m3052",
        "original_name": "(Unnamed medium)",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in repair_module.LEGACY_INGREDIENTS
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M3052",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "TOGO Medium M3052",
            },
        },
        "notes": "Source: NBRC - NBRC_M1604",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_nests_nbrc_1604_stock_additions(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert "ph_value" not in repaired
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENTS
    )
    assert (
        repair_module._solution_signatures(
            repaired["solutions"],
            "solutions",
        )
        == repair_module.FINAL_SOLUTIONS
    )
    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_corrects_water_and_grounded_basal_rows(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients["MgSO4 7H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:31795",
        "label": "magnesium sulfate heptahydrate",
    }
    assert ingredients["Agar"]["physicochemical_roles"] == ["SOLIDIFYING_AGENT"]


def test_repair_preserves_casitone_as_sourced_opaque_component(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    casitone = _by_name(repaired["ingredients"])["Casitone"]

    assert "term" not in casitone
    assert "opaque complex component" in casitone["notes"]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_converts_microliter_stock_additions_to_ml_per_l(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    assert solutions["Biotin (1 ug/uL)"]["concentration"] == {
        "value": "0.01",
        "unit": "ML_PER_L",
    }
    assert solutions["Resazurin (1 mg/L)"]["concentration"] == {
        "value": "0.1",
        "unit": "ML_PER_L",
    }
    assert solutions["Thiamine (0.05 ug/mL)"]["concentration"] == {
        "value": "0.1",
        "unit": "ML_PER_L",
    }
    assert solutions["Glucose (0.1981 g/mL)"]["composition"][0] == {
        "preferred_term": "Glucose",
        "concentration": {"value": "198.1", "unit": "MG_PER_ML"},
        "source": repair_module.SOURCE,
        "notes": "NBRC Medium 1604 specifies this stock as Glucose (0.1981 g/mL).",
        "term": {"id": "CHEBI:17234", "label": "glucose"},
        "mediaingredientmech_chebi_term": {"id": "CHEBI:17234", "label": "glucose"},
    }


def test_repair_adds_source_stated_preparation_steps(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert "temperature_value" not in repaired
    assert "temperature_range" not in repaired
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_target(_doc(repair_module))
    twice = repair_module.repair_target(once)

    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
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
    assert "nested the Resazurin" in matching_events[0]["notes"]


def test_plan_repairs_target_record(repair_module) -> None:
    target_path = repair_module.NORMALIZED / repair_module.TARGET
    expected_target = repair_module.repair_target(
        yaml.safe_load(target_path.read_text(encoding="utf-8"))
    )

    assert repair_module.plan_repairs() == {target_path: expected_target}


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_target(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M2079"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_target(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Distilled water", "1.0", "L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_target(doc)


def test_target_record_matches_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in {
        repair_module.LEGACY_INGREDIENTS,
        repair_module.FINAL_INGREDIENTS,
    }
    assert repair_module._solution_signatures(doc.get("solutions"), "solutions") in {
        (),
        repair_module.FINAL_SOLUTIONS,
    }
