from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2240_pplo_calf_serum_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2240_pplo_calf_serum_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2240")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "medium_containing_pplo_broth_calf_serum_glucose_penicillin_g_and_tris_hc1",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2240",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": [
            "incomplete_composition",
            "needs_manual_curation",
        ],
        "kg_microbe_match": "mediadive.medium:21",
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_percent_units_and_adds_ph(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["ph_value"] == 7.6
    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert ingredients["Glucose"]["concentration"] == {
        "value": "0.2",
        "unit": "PERCENT_W_V",
    }
    assert ingredients["Calf serum (Gibco)"]["concentration"] == {
        "value": "1.0",
        "unit": "PERCENT_V_V",
    }
    assert ingredients["PPLO broth (Difco)"]["concentration"] == {
        "value": "2.2",
        "unit": "PERCENT_W_V",
    }


def test_repair_keeps_activity_unit_as_variable(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    penicillin = _by_name(repaired["ingredients"])["Penicillin G"]

    assert penicillin["concentration"] == {"value": "variable", "unit": "VARIABLE"}
    assert "400 units(U)/ml" in penicillin["notes"]
    assert "schema has no unit for activity units" in penicillin["notes"]


def test_repair_grounds_only_defined_simple_components(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Glucose"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert ingredients["Penicillin G"]["term"] == {
        "id": "CHEBI:51765",
        "label": "benzylpenicillin sodium",
    }

    for name in ("Tris-HC1 (pH 7.6)", "Calf serum (Gibco)", "PPLO broth (Difco)"):
        assert "term" not in ingredients[name]
        assert "mediaingredientmech_chebi_term" not in ingredients[name]

    assert "single-molecule ontology grounding" in ingredients[
        "Tris-HC1 (pH 7.6)"
    ]["notes"]
    assert "opaque complex component" in ingredients["Calf serum (Gibco)"]["notes"]


def test_repair_adds_reference_flags_and_event_once(
    repair_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice == once
    assert once["references"] == [{"reference": repair_module.TOGO_M2240}]
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert "Sarcina Medium" in matching_events[0]["notes"]


def test_repair_removes_false_kg_microbe_match(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert "kg_microbe_match" not in repaired
    assert "preparation_steps" not in repaired
    assert "sterilization" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_rejects_unexpected_kg_microbe_match(
    repair_module,
) -> None:
    doc = _doc(repair_module)
    doc["kg_microbe_match"] = "mediadive.medium:J163"

    with pytest.raises(ValueError, match="unexpected kg_microbe_match"):
        repair_module.repair_record(doc)
