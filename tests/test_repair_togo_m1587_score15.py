from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1587_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m1587_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1587")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "jxt_medium",
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
            "preferred_term": "TOGO Medium M1587",
            "term": {"id": repair_module.EXPECTED_MEDIA_TERM, "label": repair_module.TITLE},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "kg_microbe_match": "mediadive.medium:1090",
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_seawater_unit_and_adds_ph_range(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "UNDEFINED"
    assert repaired["physical_state"] == "LIQUID"
    assert repaired["ph_range"] == {"min": 7.0, "max": 7.2}
    assert "ph_value" not in repaired
    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE

    assert _by_name(repaired["ingredients"])["Sea water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }


def test_repair_grounds_disclosed_products_and_thiosulfate(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Na2S2O3·5H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:32150",
        "label": "sodium thiosulfate pentahydrate",
    }
    assert ingredients["Bacto Yeast Extract (Difco)"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients["Trypticase Peptone (BBL)"]["term"] == {
        "id": "MICRO:0000175",
        "label": "Trypticase peptone",
    }


def test_repair_keeps_seawater_ungrounded(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert _by_name(repaired["ingredients"])["Sea water"] == {
        "preferred_term": "Sea water",
        "concentration": {"value": "1.0", "unit": "L"},
        "source": repair_module.SOURCE,
        "notes": (
            "NBRC Medium 395 lists 1 L sea water and allows filtered natural "
            "seawater or artificial seawater such as Aquamarine from Yashima; "
            "the seawater input is retained as an opaque complex component."
        ),
    }


def test_repair_adds_only_source_stated_thiosulfate_filtration(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert "temperature_value" not in repaired
    assert "temperature_range" not in repaired
    assert "sterilization" not in repaired
    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "FILTER_STERILIZE",
            "description": (
                "Separately sterilize a Na2S2O3·5H2O solution by filtration "
                "and aseptically add it to the medium."
            ),
        }
    ]


def test_repair_record_drops_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (0, [])
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
    assert "Corrected the seawater unit" in matching_events[0]["notes"]


def test_repair_preserves_kg_microbe_match(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["kg_microbe_match"] == "mediadive.medium:1090"


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Seawater", "1", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"] = [
        {
            "preferred_term": "Thiosulfate solution",
            "concentration": {"value": "1", "unit": "G_PER_L"},
            "composition": [],
        }
    ]

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_togo_m1587_repair_contract(
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
    assert "solutions" not in doc
