from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m3010_pyg_medium_k_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m3010_pyg_medium_k")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m3010")


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
        "name": "pyg_medium_k",
        "original_name": "PYG Medium (K)",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M3010",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "PYG Medium (K)",
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
        "data_quality_flags": ["has_unmapped_ingredients", "needs_manual_curation"],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_units_and_leaves_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert (
        repair_module._solution_signatures(
            repaired["solutions"],
        )
        == repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert repaired["ph_range"] == {"min": 7.0, "max": 7.2}
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_grounds_main_ingredients(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Trypticase peptone"]["term"] == {
        "id": "MICRO:0000175",
        "label": "Trypticase peptone",
    }
    assert "mediaingredientmech_chebi_term" not in ingredients["Trypticase peptone"]
    assert ingredients["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "Peptone",
    }
    assert "mediaingredientmech_chebi_term" not in ingredients["Peptone"]
    assert ingredients["L-Cysteine x HCl x H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:91248",
        "label": "L-cysteine hydrochloride hydrate",
    }
    assert ingredients["Resazurin"]["concentration"] == {
        "value": "1.0",
        "unit": "MG_PER_L",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "940.0",
        "unit": "ML_PER_L",
    }


def test_repair_expands_and_grounds_cross_referenced_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    salt = _by_name(solutions["Salt solution"]["composition"])
    assert salt["MgSO4 x 7H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:31795",
        "label": "magnesium sulfate heptahydrate",
    }
    assert salt["CaCl2 x 2H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:86158",
        "label": "calcium chloride dihydrate",
    }
    assert salt["NaHCO3"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:32139",
        "label": "sodium hydrogencarbonate",
    }

    hemin = _by_name(solutions["Hemin solution"]["composition"])
    assert hemin["Hemin"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:50385",
        "label": "hemin",
    }
    assert hemin["1 N NaOH"]["concentration"] == {
        "value": "10.0",
        "unit": "ML_PER_L",
    }

    menadione = _by_name(solutions["Menadione solution"]["composition"])
    assert menadione["Menadione"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:28869",
        "label": "menadione",
    }
    assert menadione["Ethanol"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:16236",
        "label": "ethanol",
    }


def test_repair_adds_preparation_references_flags_and_event_once(
    repair_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice == once
    assert twice["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
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
    assert matching_events[0]["source"] == "; ".join(repair_module.REFERENCES)


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:009528"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M3011"

    with pytest.raises(ValueError, match="expected media term TOGO:M3010"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_signature_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"]["value"] = "1000"

    with pytest.raises(ValueError, match="recipe signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["preferred_term"] = "Unexpected stock"

    with pytest.raises(ValueError, match="recipe signature drifted"):
        repair_module.repair_record(doc)
