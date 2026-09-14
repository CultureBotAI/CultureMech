from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1645_bl_agar_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m1645_bl_agar_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1645")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
        "name": "Unknown solution",
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "bl_agar",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M1645",
            "term": {"id": repair_module.EXPECTED_MEDIA_TERM, "label": "BL Agar"},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in repair_module.IMPORTED_SOLUTION_SIGNATURE
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_nbrc_order_and_liquid_units(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "UNDEFINED"
    assert repaired["physical_state"] == "SOLID_AGAR"
    assert "ph_value" not in repaired
    assert "ph_range" not in repaired
    assert "temperature_value" not in repaired
    assert "temperature_range" not in repaired
    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert "solutions" not in repaired


def test_repair_grounds_blood_and_water_only(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Defibrinated horse blood"]["term"] == {
        "id": "UBERON:0000178",
        "label": "blood",
    }
    assert "mediaingredientmech_chebi_term" not in ingredients[
        "Defibrinated horse blood"
    ]
    assert ingredients["Distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }


def test_repair_keeps_nissui_bl_agar_opaque(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["BL Agar*"] == {
        "preferred_term": "BL Agar*",
        "concentration": {"value": "58.0", "unit": "G_PER_L"},
        "source": repair_module.SOURCE,
        "notes": (
            "NBRC Medium 848 lists 58 g/L BL Agar and notes that the "
            "asterisk marks Nissui Pharmaceutical Co. Ltd.; this commercial "
            "BL Agar product is retained as an opaque base/solidifying "
            "component."
        ),
    }


def test_repair_adds_nbrc_preparation_steps(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert "sterilization" not in repaired
    assert [step["action"] for step in repaired["preparation_steps"]] == [
        "AUTOCLAVE",
        "COOL",
        "MIX",
        "POUR_PLATES",
    ]
    assert "without horse blood" in repaired["preparation_steps"][0]["description"]
    assert "5% v/v" in repaired["preparation_steps"][2]["description"]


def test_repair_record_drops_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["references"] == [
        {"reference": url} for url in repair_module.REFERENCES
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
    assert "corrected water and horse blood liquid units" in matching_events[0][
        "notes"
    ]
    assert "Nissui" in matching_events[0]["notes"]


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:wrong"

    with pytest.raises(ValueError, match="expected media term"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_component_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"].pop()

    with pytest.raises(ValueError, match="composition signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["preferred_term"] = "wrong"

    with pytest.raises(ValueError, match="composition signature drifted"):
        repair_module.repair_record(doc)


def test_script_is_idempotent_on_dumped_yaml(tmp_path: Path, repair_module) -> None:
    normalized = tmp_path / "normalized"
    target = normalized / repair_module.TARGET
    target.parent.mkdir(parents=True)
    target.write_text(yaml.safe_dump(_doc(repair_module), sort_keys=False))

    first = repair_module.plan_repairs(normalized)[target]
    target.write_text(yaml.safe_dump(first, sort_keys=False))
    second = repair_module.plan_repairs(normalized)[target]

    assert second == first
