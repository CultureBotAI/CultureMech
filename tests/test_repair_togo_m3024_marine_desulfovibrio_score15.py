from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m3024_marine_desulfovibrio_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m3024_marine_desulfovibrio_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m3024")


def _component(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": repair_module.TARGET.stem,
        "original_name": "Marine Desulfovibrio Complex Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M3024",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "Marine Desulfovibrio Complex Medium",
            },
        },
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            {
                "preferred_term": name,
                "concentration": {"value": value, "unit": unit},
                "composition": [
                    _component(child_name, child_value, child_unit)
                    for child_name, child_value, child_unit in children
                ],
                "name": "Unknown solution",
            }
            for name, value, unit, children in repair_module.IMPORTED_SOLUTION_SIGNATURE
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_restores_direct_components_and_units(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "945.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Resazurin"]["concentration"] == {
        "value": "0.5",
        "unit": "MG_PER_L",
    }
    assert ingredients["Yeast extract (BD-Difco)"]["term"] == {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    }
    assert "term" not in ingredients["Sea salts (Sigma)"]
    assert "N2" not in ingredients
    assert "Nitrogen gas" not in ingredients
    assert "Carbon dioxide gas" not in ingredients
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_restores_stock_solutions(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    assert repair_module._solution_signature(
        repaired["solutions"],
    ) == repair_module.FINAL_SOLUTION_SIGNATURE
    assert solutions["Wolfe's mineral elixir"]["concentration"] == {
        "value": "1.0",
        "unit": "ML_PER_L",
    }
    wolfe = _by_name(solutions["Wolfe's mineral elixir"]["composition"])
    assert wolfe["NaCl"]["term"] == {"id": "CHEBI:26710", "label": "sodium chloride"}
    assert wolfe["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert solutions["1 M Sodium lactate solution"]["composition"] == [
        {
            "preferred_term": "Sodium lactate",
            "concentration": {"value": "1.0", "unit": "MOLAR"},
            "source": repair_module.SOURCE,
            "notes": f"{repair_module.SOURCE} lists 1.0 M Sodium lactate.",
            "term": {"id": "CHEBI:75228", "label": "sodium lactate"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:75228",
                "label": "sodium lactate",
            },
            "nutritional_roles": ["CARBON_SOURCE"],
        }
    ]
    vitamins = _by_name(solutions["Trace vitamins"]["composition"])
    assert vitamins["Vitamin B12"]["concentration"] == {
        "value": "0.1",
        "unit": "MG_PER_L",
    }
    sulfide = _by_name(solutions["5% Na2S x 9 H2O solution"]["composition"])
    assert sulfide["Na2S x 9 H2O"]["concentration"] == {
        "value": "50.0",
        "unit": "G_PER_L",
    }


def test_repair_records_anaerobic_handling_as_steps(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert [step["action"] for step in repaired["preparation_steps"]] == [
        "MIX",
        "AUTOCLAVE",
        "FILTER_STERILIZE",
        "MIX",
        "MIX",
    ]
    assert "N2-CO2 (4:1, v/v)" in repaired["preparation_steps"][4]["description"]
    assert repaired["sterilization"]["method"] == "AUTOCLAVE"
    assert "filter-sterilized" in repaired["sterilization"]["notes"]


def test_repair_adds_flags_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_target(_doc(repair_module))
    twice = repair_module.repair_target(once)

    assert twice == once
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert once["references"] == [{"reference": url} for url in repair_module.REFERENCES]
    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_target(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:other"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_target(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"]["unit"] = "ML_PER_L"

    with pytest.raises(ValueError, match="ingredient signature"):
        repair_module.repair_target(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0] = _component("Wolfe's mineral elixir", "1", "ML_PER_L")

    with pytest.raises(ValueError, match="solution signature"):
        repair_module.repair_target(doc)


def test_target_record_matches_togo_m3024_repair_contract(
    repair_module,
) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
    assert repair_module._solution_signature(doc.get("solutions")) in (
        repair_module.IMPORTED_SOLUTION_SIGNATURE,
        repair_module.FINAL_SOLUTION_SIGNATURE,
    )
