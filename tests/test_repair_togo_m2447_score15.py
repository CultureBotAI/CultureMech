from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2447_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2447_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2447")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "lb_agar_miller",
        "original_name": "LB Agar, Miller",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2447",
            "term": {"id": repair_module.EXPECTED_MEDIA_TERM, "label": "LB Agar, Miller"},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_di_water_and_adds_ph_range(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "UNDEFINED"
    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["ph_range"] == {"min": 6.8, "max": 7.2}
    assert "ph_value" not in repaired
    assert (
        repair_module._component_signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert ingredients["DI Water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }


def test_repair_grounds_all_disclosed_components(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Agar"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert ingredients["DI Water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert ingredients["Sodium Chloride"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:26710",
        "label": "sodium chloride",
    }
    assert ingredients["Tryptone"]["term"] == {
        "id": "MICRO:0000182",
        "label": "tryptone",
    }
    assert ingredients["Yeast Extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }


def test_repair_adds_only_disclosed_autoclave_step(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "AUTOCLAVE",
            "description": "Autoclave at 121 degrees C.",
        },
    ]
    assert "sterilization" not in repaired
    assert "temperature_value" not in repaired
    assert "temperature_range" not in repaired


def test_repair_record_drops_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
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
    assert "water unit artifact" in matching_events[0]["notes"]


def test_repair_removes_stale_variant_links(repair_module) -> None:
    doc = _doc(repair_module)
    doc["parent_media"] = {"id": "CultureMech:wrong"}
    doc["variant_relationship"] = "SOURCE_DUPLICATE"
    doc["variant_modifications"] = ["stale"]
    repaired = repair_module.repair_target(doc)

    assert "parent_media" not in repaired
    assert "variant_relationship" not in repaired
    assert "variant_modifications" not in repaired


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
    doc["ingredients"][2] = _ingredient("DI Water", "1.0", "L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_target(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"] = [
        {
            "preferred_term": "LB Agar stock",
            "concentration": {"value": "40", "unit": "G_PER_L"},
            "composition": [],
        }
    ]

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_target(doc)


def test_target_record_matches_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._component_signature(doc["ingredients"], "ingredients") in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
    assert "solutions" not in doc
