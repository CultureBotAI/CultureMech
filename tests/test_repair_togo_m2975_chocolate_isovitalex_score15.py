from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2975_chocolate_isovitalex_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2975_chocolate_isovitalex_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2975")


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.RECORD_ID,
        "name": repair_module.PATH.stem,
        "original_name": "chocolate agar plates (supplemented with 1% isovitalex)",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": "TOGO Medium M2975",
            "term": {
                "id": repair_module.MEDIA_TERM,
                "label": "chocolate agar plates (supplemented with 1% isovitalex)",
            },
        },
        "ingredients": [
            {
                "preferred_term": "isovitalex (BD Biosciences)",
                "concentration": {"value": "1", "unit": "PERCENT_W_V"},
            },
            {
                "preferred_term": "CO2",
                "concentration": {"value": "variable", "unit": "VARIABLE"},
            },
            {
                "preferred_term": "chocolate agar plates",
                "concentration": {"value": "variable", "unit": "VARIABLE"},
            },
        ],
        "notes": "Source: https://togomedium.org/medium/M2975",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def test_repair_keeps_source_components_and_scores_clean(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENTS
    )
    assert repaired["temperature_value"] == 37.0
    assert [row["preferred_term"] for row in repaired["ingredients"]] == [
        "IsoVitaleX (BD Biosciences)",
        "Chocolate agar plates",
    ]
    assert repaired["ingredients"][0]["concentration"] == {
        "value": "1.0",
        "unit": "PERCENT_V_V",
    }
    assert scorer_module.score_parsed(
        [(str(repair_module.PATH), repaired)]
    ) == []


def test_repair_adds_flags_reference_and_event_once(
    repair_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["references"] == [{"reference": repair_module.TOGO_M2975}]
    assert twice["data_quality_flags"] == [
        "ingredients_curated",
        "has_unmapped_ingredients",
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
    assert matching_events[0]["source"] == repair_module.TOGO_M2975


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M2976"

    with pytest.raises(ValueError, match="expected media term TOGO:M2975"):
        repair_module.repair_record(doc)


def test_repair_rejects_component_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"]["value"] = "2"

    with pytest.raises(ValueError, match="composition signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.PATH
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.RECORD_ID
    assert repair_module._source_term_id(doc) == repair_module.MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in {
        repair_module.IMPORTED_INGREDIENTS,
        repair_module.FINAL_INGREDIENTS,
    }
