from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_4002_salt_solution_592_score15.py"
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
    return _load_script(SCRIPT, "repair_komodo_4002_salt_solution_592")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_4002_salt_solution_592")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "salt_solution_medium_592",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 2.0,
        "notes": (
            "pH buffer: H2SO4 | Source: KOMODO ModelSEED | ID: 4002 | "
            "DSMZ Medium: 4002 (mediadive.medium:4002) | Aerobic: No | "
            "SubMedium: Yes"
        ),
        "media_term": {
            "preferred_term": "KOMODO Medium 4002",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_restores_dsmz_trace_elements_stock(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["medium_type"] == "DEFINED"
    assert repaired["composition_type"] == "DEFINED"
    assert repaired["physical_state"] == "LIQUID"
    assert repaired["ph_value"] == 2.0
    assert (
        repair_module._signature(repaired["ingredients"], "ingredients")
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Dissolve the trace-elements stock components in distilled water "
                "and bring to 100.000 ml."
            ),
        },
        {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": "Adjust to pH 2.0 with H2SO4.",
        },
    ]
    assert "mediadive.solution:4002 Main sol. J298" in repaired["notes"]
    assert "Trace elements" in repaired["notes"]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_scales_100_ml_source_to_per_litre_units(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["MnCl2 x 4 H2O"]["concentration"] == {
        "value": "18",
        "unit": "G_PER_L",
    }
    assert ingredients["Na2B4O7 x 10 H2O"]["concentration"] == {
        "value": "44",
        "unit": "G_PER_L",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert "100.000 ml" in ingredients["MnCl2 x 4 H2O"]["notes"]


def test_repair_grounds_all_stock_components(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    for ingredient in repaired["ingredients"]:
        assert ingredient["mediaingredientmech_chebi_term"] == ingredient["term"]
    assert {ingredient["term"]["id"] for ingredient in repaired["ingredients"]} == {
        "CHEBI:86368",
        "CHEBI:131366",
        "CHEBI:32312",
        "CHEBI:49553",
        "CHEBI:75213",
        "CHEBI:87009",
        "CHEBI:15377",
        "CHEBI:26836",
    }


def test_repair_models_h2so4_as_grounded_variable_adjuster(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    h2so4 = _by_name(repaired["ingredients"])["H2SO4"]

    assert h2so4 == {
        "preferred_term": "H2SO4",
        "concentration": {"value": "variable", "unit": "VARIABLE"},
        "source": repair_module.SOURCE,
        "notes": (
            "DSMZ Medium 592 Trace elements instructs adjustment to pH 2.0 "
            "with H2SO4 and gives no amount."
        ),
        "term": {"id": "CHEBI:26836", "label": "sulfuric acid"},
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:26836",
            "label": "sulfuric acid",
        },
    }
    assert "data_quality_flags" not in h2so4


def test_repair_adds_flags_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
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
    assert "H2SO4-only pH-buffer stub" in matching_events[0]["notes"]


def test_plan_repairs_target_record(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET

    assert repair_module.plan_repairs() == {
        path: repair_module.repair_record(yaml.safe_load(path.read_text(encoding="utf-8")))
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "komodo.medium:592"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Trace elements", "1", "ML_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"] = [
        {
            "preferred_term": "Main sol. J298",
            "concentration": {"value": "2", "unit": "ML_PER_L"},
            "composition": [],
        }
    ]

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_corpus_record_matches_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    signature = repair_module._signature(doc["ingredients"], "ingredients")

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert signature in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
