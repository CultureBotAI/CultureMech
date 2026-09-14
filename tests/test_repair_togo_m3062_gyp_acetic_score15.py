from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m3062_gyp_acetic_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m3062_gyp_acetic_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m3062")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": repair_module.TARGET.stem,
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "solutions": [
            {
                "preferred_term": name,
                "composition": [
                    _ingredient(
                        component_name,
                        component_value,
                        component_unit,
                    )
                    for component_name, component_value, component_unit in composition
                ],
                "concentration": {"value": value, "unit": unit},
                "name": "Unknown solution",
            }
            for name, value, unit, composition in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M3062",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_nbrc_order_units_ph_and_empty_agar_solution(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "UNDEFINED"
    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["ph_value"] == 6.0
    assert "ph_range" not in repaired
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert "solutions" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_grounds_discrete_components(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Glucose"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert ingredients["Distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert ingredients["Agar (if needed)"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert ingredients["Yeast Extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }


def test_repair_keeps_peptone_opaque(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Peptone"] == {
        "preferred_term": "Peptone",
        "concentration": {"value": "2.0", "unit": "G_PER_L"},
        "source": repair_module.SOURCE,
        "notes": (
            "NBRC Medium 1636 lists 2 g/L Peptone; this protein digest is "
            "retained as an opaque complex component."
        ),
    }


def test_repair_adds_only_source_stated_ph_step(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert "temperature_value" not in repaired
    assert "temperature_range" not in repaired
    assert "sterilization" not in repaired
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 6.0.",
        }
    ]


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
    ]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
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
    assert "restored the migrated agar row" in matching_events[0]["notes"]


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M3063"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Distilled water", "1.0", "L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["preferred_term"] = "Agar (if needed)"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_togo_m3062_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
    assert repair_module._solution_signatures(doc) in (
        repair_module.IMPORTED_SOLUTION_SIGNATURES,
        repair_module.FINAL_SOLUTION_SIGNATURES,
    )
