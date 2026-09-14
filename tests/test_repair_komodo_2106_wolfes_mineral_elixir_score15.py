from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_2106_wolfes_mineral_elixir_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"
RECORD_KINDS = REPO / "scripts" / "record_kinds.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_komodo_2106_wolfes_mineral_elixir")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(
        SCORER,
        "score_review_need_for_komodo_2106_wolfes_mineral_elixir",
    )


@pytest.fixture(scope="module")
def record_kinds_module():
    return _load_script(
        RECORD_KINDS,
        "record_kinds_for_komodo_2106_wolfes_mineral_elixir",
    )


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "wolfes_mineral_elixir_medium_792",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 1.0,
        "notes": (
            "pH buffer: H2SO4 | Source: KOMODO ModelSEED | ID: 2106 | "
            "DSMZ Medium: 2106 (mediadive.medium:2106) | Aerobic: No | "
            "SubMedium: Yes"
        ),
        "media_term": {
            "preferred_term": "KOMODO Medium 2106",
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


def test_repair_restores_dsmz_wolfes_mineral_elixir(
    repair_module,
    record_kinds_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["record_kind"] == "SOLUTION"
    assert record_kinds_module.is_solution_record(repaired)
    assert repaired["ph_value"] == 1.0
    assert (
        repair_module._signature(repaired["ingredients"], "ingredients")
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repaired["notes"].startswith("KOMODO Medium 2106 is a SubMedium")
    assert "MediaDive solution 1605" in repaired["notes"]
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": (
                "First adjust the Wolfe's mineral elixir stock to pH 1.0 " "with diluted H2SO4."
            ),
        },
        {
            "step_number": 2,
            "action": "MIX",
            "description": (
                "Add and dissolve the Wolfe's mineral elixir salts in " "1000.0 ml distilled water."
            ),
        },
    ]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_preserves_dsmz_source_units(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["MgSO4 x 7 H2O"]["concentration"] == {
        "value": "30.00",
        "unit": "G_PER_L",
    }
    assert ingredients["(NH4)2Ni(SO4)2 x 6 H2O"]["concentration"] == {
        "value": "2.80",
        "unit": "G_PER_L",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }


def test_repair_grounds_all_formula_components(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    for ingredient in repaired["ingredients"]:
        assert ingredient["mediaingredientmech_chebi_term"] == ingredient["term"]

    assert {ingredient["term"]["id"] for ingredient in repaired["ingredients"]} == {
        "CHEBI:31795",
        "CHEBI:86364",
        "CHEBI:26710",
        "CHEBI:75836",
        "CHEBI:53503",
        "CHEBI:86158",
        "CHEBI:32312",
        "CHEBI:31440",
        "CHEBI:86465",
        "CHEBI:33118",
        "CHEBI:75213",
        "CHEBI:86149",
        "CHEBI:63939",
        "CHEBI:77775",
        "CHEBI:15377",
        "CHEBI:26836",
    }


def test_repair_assigns_trace_roles(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["FeSO4 x 7 H2O"]["nutritional_roles"] == ["IRON_SOURCE"]
    for name in {
        "MnSO4 x H2O",
        "CoCl2 x 6 H2O",
        "ZnSO4 x 7 H2O",
        "CuSO4 x 5 H2O",
        "AlK(SO4)2 x 12 H2O",
        "H3BO3",
        "Na2MoO4 x 2 H2O",
        "(NH4)2Ni(SO4)2 x 6 H2O",
        "Na2WO4 x 2 H2O",
        "Na2SeO4",
    }:
        assert ingredients[name]["nutritional_roles"] == ["TRACE_ELEMENT"]


def test_repair_keeps_h2so4_as_grounded_variable_adjuster(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    h2so4 = _by_name(repaired["ingredients"])["H2SO4"]

    assert h2so4 == {
        "preferred_term": "H2SO4",
        "concentration": {"value": "variable", "unit": "VARIABLE"},
        "source": repair_module.SOURCE,
        "notes": (
            "DSMZ Medium 792 instructs first adjusting Wolfe's mineral "
            "elixir to pH 1.0 with diluted H2SO4; the amount is retained "
            "as variable because it is titrated to pH."
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
        "ingredients_curated",
        "has_ontology_mappings",
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


def test_plan_repairs_targets_record(repair_module) -> None:
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
    doc["media_term"]["term"]["id"] = "komodo.medium:792"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("HCl", "variable", "VARIABLE")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)
