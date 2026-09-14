from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m3270_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m3270_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m3270")


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
        "name": "tmbs4_medium",
        "original_name": "Tmbs4 Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M3270",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "Tmbs4 Medium",
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
    }


def _parent_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_PARENT_ID,
        "name": "tmbs4_medium",
        "original_name": "TMBS4 MEDIUM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "DSMZ Medium 559",
            "term": {
                "id": repair_module.EXPECTED_PARENT_MEDIA_TERM,
                "label": "TMBS4 MEDIUM",
            },
        },
        "notes": "Source: DSMZ",
        "ingredients": [],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "variant_children": [
            {
                "path": "data/normalized_yaml/bacterial/KOMODO_559_TMBS4_medium.yaml",
                "relationship": "SOURCE_DUPLICATE",
                "id": "CultureMech:006010",
                "name": "tmbs4_medium",
            }
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_base_formula_and_ph_range(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert repaired["physical_state"] == "LIQUID"
    assert repaired["ph_range"] == {"min": 7.2, "max": 7.4}
    assert "ph_value" not in repaired
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "930.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Resazurin"]["concentration"] == {
        "value": "0.5",
        "unit": "MG_PER_L",
    }
    assert ingredients["Nitrogen gas"]["notes"].startswith("JCM Medium 1408 uses an N2-CO2")
    assert "Syringic acid" not in ingredients


def test_repair_expands_shared_jcm_stocks(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    trace = _by_name(solutions["Trace element solution"]["composition"])
    selenite = _by_name(solutions["Selenite-tungstate solution"]["composition"])
    vitamins = _by_name(solutions["Trace vitamins"]["composition"])

    assert solutions["FeCl2 solution"]["concentration"] == {
        "value": "1.0",
        "unit": "ML_PER_L",
    }
    assert "term" not in trace["NiCl2 x 6H2O"]
    assert selenite["Na2SeO3 x 5H2O"]["term"] == {
        "id": "CHEBI:131361",
        "label": "disodium selenite pentahydrate",
    }
    assert vitamins["Lipoic acid"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:16494",
        "label": "lipoic acid",
    }


def test_repair_expands_tmbs4_specific_stocks(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    thiosulfate = _by_name(solutions["5% Sodium thiosulfate solution"]["composition"])
    yeast = _by_name(solutions["10% Yeast extract solution"]["composition"])
    syringate = _by_name(solutions["Syringate solution"]["composition"])
    dtt = _by_name(solutions["0.1 M Dithiothreitol solution"]["composition"])
    dithionite = _by_name(solutions["2.5% Sodium dithionite solution"]["composition"])

    assert thiosulfate["Sodium thiosulfate"]["concentration"] == {
        "value": "50.0",
        "unit": "G_PER_L",
    }
    assert "term" not in yeast["Yeast extract"]
    assert syringate["Syringic acid"]["concentration"] == {
        "value": "60.0",
        "unit": "G_PER_L",
    }
    assert syringate["NaOH"]["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert dtt["Dithiothreitol"]["concentration"] == {
        "value": "0.1",
        "unit": "MOLAR",
    }
    assert dithionite["Sodium dithionite"]["term"] == {
        "id": "CHEBI:66870",
        "label": "sodium dithionite",
    }


def test_repair_adds_preparation_without_naoh_standalone_solution(
    repair_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    solution_names = {row["preferred_term"] for row in repaired["solutions"]}

    assert "2N NaOH solution" not in solution_names
    assert len(repaired["preparation_steps"]) == 5
    assert repaired["preparation_steps"][2]["action"] == "MIX"
    assert repaired["sterilization"] == repair_module.STERILIZATION


def test_repair_links_togo_record_to_dsmz_parent(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert repaired["parent_media"] == repair_module.PARENT_MEDIA
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [
        repair_module.VARIANT_MODIFICATIONS,
    ]


def test_repair_record_drops_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_target(_doc(repair_module))
    twice = repair_module.repair_target(once)

    assert twice["references"] == [{"reference": url} for url in repair_module.REFERENCES]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert "water and stock-addition unit artifacts" in matching_events[0]["notes"]


def test_repair_parent_adds_togo_child_once(repair_module) -> None:
    once = repair_module.repair_parent(_parent_doc(repair_module))
    twice = repair_module.repair_parent(once)

    assert twice["variant_children"] == [
        {
            "path": "data/normalized_yaml/bacterial/KOMODO_559_TMBS4_medium.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:006010",
            "name": "tmbs4_medium",
        },
        repair_module.TOGO_CHILD,
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.LINK_ACTION
        )
    ]
    assert len(matching_events) == 1


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_target(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_target(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"] = {"value": "1.0", "unit": "L"}

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_target(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["concentration"] = {"value": "1.0", "unit": "ML_PER_L"}

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_target(doc)


def test_repair_parent_rejects_wrong_parent_id(repair_module) -> None:
    doc = _parent_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_PARENT_ID):
        repair_module.repair_parent(doc)
