from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1250_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m1250_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1250")


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.RECORD_ID,
        "name": "lb_luria_bertani_agar_with_kanamycin_and_rifampicin",
        "original_name": "LB (Luria-Bertani) Agar With Kanamycin And Rifampicin",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            {
                "preferred_term": preferred_term,
                "concentration": {"value": value, "unit": unit},
            }
            for preferred_term, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M1250",
            "term": {
                "id": repair_module.MEDIA_TERM,
                "label": "LB (Luria-Bertani) Agar With Kanamycin And Rifampicin",
            },
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_antibiotic_masses_and_groundings(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert "Kanamycin sulfate (dissolved in distilled water)" not in ingredients
    assert "Rifampicin (dissolved in methanol)" not in ingredients
    assert ingredients["Kanamycin sulfate"]["concentration"] == {
        "value": "0.05",
        "unit": "G_PER_L",
    }
    assert ingredients["Kanamycin sulfate"]["term"] == {
        "id": "CHEBI:6109",
        "label": "kanamycin A sulfate",
    }
    assert ingredients["Rifampicin"]["concentration"] == {
        "value": "0.025",
        "unit": "G_PER_L",
    }
    assert ingredients["Rifampicin"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:28077",
        "label": "rifampicin",
    }


def test_repair_preserves_disclosed_bd_difco_products_unmapped(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert ingredients["Tryptone (BD-Difco)"]["source"] == "MediaDive J1168"
    assert ingredients["Yeast extract (BD-Difco)"]["concentration"] == {
        "value": "5",
        "unit": "G_PER_L",
    }
    assert "term" not in ingredients["Tryptone (BD-Difco)"]
    assert "term" not in ingredients["Yeast extract (BD-Difco)"]


def test_repair_adds_ph_preparation_and_drops_record_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["ph_value"] == 7.0
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust the LB agar base to pH 7.0 before autoclaving.",
        },
        {
            "step_number": 2,
            "action": "FILTER_STERILIZE",
            "description": (
                "After autoclaving, aseptically add the kanamycin sulfate and "
                "rifampicin antibiotics as filter-sterilized stocks."
            ),
        },
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["references"] == [{"reference": url} for url in repair_module._references()]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == "; ".join(repair_module._references())


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.RECORD_ID):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=repair_module.MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"]["value"] = "1001"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_unexpected_solutions(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"] = [{"preferred_term": "Antibiotic stock"}]

    with pytest.raises(ValueError, match="unexpected solutions"):
        repair_module.repair_record(doc)
