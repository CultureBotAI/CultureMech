from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2226_pplo_horse_yeast_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2226_pplo_horse_yeast")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2226")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "pplo_broth_without_cv_ph_7_8_with_horse_serum_not_inactivated_and_yeast_extract",
        "original_name": (
            "PPLO broth without CV (pH 7.8) with horse serum (not inactivated) " "and yeast extract"
        ),
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2226",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": (
                    "PPLO broth without CV (pH 7.8) with horse serum "
                    "(not inactivated) and yeast extract"
                ),
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": ["has_unmapped_ingredients"],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_ml_units_and_leaves_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["ph_value"] == 7.8
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert "solutions" not in repaired
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_grounds_supported_components_and_keeps_pplo_ungrounded(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert "term" not in ingredients["PPLO broth"]
    assert "mediaingredientmech_chebi_term" not in ingredients["PPLO broth"]

    assert ingredients["Distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert ingredients["Distilled water"]["term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert ingredients["Horse serum"]["term"] == {
        "id": "MICRO:0001235",
        "label": "Horse serum",
    }
    assert "mediaingredientmech_chebi_term" not in ingredients["Horse serum"]
    assert ingredients["Fresh Baker’s Yeast Extract (GIBCO 18180)"]["term"] == {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    }
    assert (
        "mediaingredientmech_chebi_term"
        not in ingredients["Fresh Baker’s Yeast Extract (GIBCO 18180)"]
    )


def test_repair_adds_aseptic_preparation_steps(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Prepare sterile basal medium containing PPLO Broth w/o CV and " "distilled water."
            ),
        },
        {
            "step_number": 2,
            "action": "MIX",
            "description": (
                "Aseptically add horse serum and Fresh Baker’s Yeast Extract " "(GIBCO 18180)."
            ),
        },
    ]


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice == once
    assert twice["data_quality_flags"] == [
        "has_unmapped_ingredients",
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

    with pytest.raises(ValueError, match="expected id CultureMech:008814"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M2227"

    with pytest.raises(ValueError, match="expected media term TOGO:M2226"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_signature_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"]["value"] = "1000"

    with pytest.raises(ValueError, match="recipe signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_unexpected_solutions(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"] = [
        {"preferred_term": "Unexpected", "concentration": {"value": "1", "unit": "G_PER_L"}}
    ]

    with pytest.raises(ValueError, match="recipe signature drifted"):
        repair_module.repair_record(doc)
