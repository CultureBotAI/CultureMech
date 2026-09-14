from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2270_m2910_lb_difco_lennox_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2270_m2910_lb_difco_lennox_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_lb_base")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _target_doc(spec) -> dict:
    return {
        "id": spec.expected_id,
        "name": spec.target.stem,
        "original_name": spec.original_name,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in spec.signature
        ],
        "media_term": {
            "preferred_term": f"TOGO Medium {spec.expected_media_term.removeprefix('TOGO:')}",
            "term": {
                "id": spec.expected_media_term,
                "label": spec.original_name,
            },
        },
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_lb_base_records_drop_below_queue_threshold(
    repair_module,
    scorer_module,
) -> None:
    for spec in repair_module.SPECS:
        repaired = repair_module.repair_target(_target_doc(spec), spec)
        ingredients = _by_name(repaired["ingredients"])

        assert repair_module._signature(repaired["ingredients"], "ingredients") == (
            spec.signature
        )
        assert repaired["composition_type"] == "SEMI_DEFINED"
        assert repaired["physical_state"] == "LIQUID"
        assert "solutions" not in repaired
        assert "ph_value" not in repaired
        assert "temperature_value" not in repaired
        assert ingredients["Tryptone"]["concentration"] == {
            "value": "10",
            "unit": "G_PER_L",
        }
        assert "term" not in ingredients["Tryptone"]
        assert any(
            row.get("term") == {
                "id": "FOODON:03315426",
                "label": "yeast extract",
            }
            for row in ingredients.values()
        )
        assert scorer_module.score_parsed([(str(spec.target), repaired)]) == []


def test_repair_is_idempotent(repair_module) -> None:
    for spec in repair_module.SPECS:
        once = repair_module.repair_target(_target_doc(spec), spec)
        twice = repair_module.repair_target(once, spec)

        assert twice == once


def test_repair_adds_flags_references_and_event_once(repair_module) -> None:
    for spec in repair_module.SPECS:
        once = repair_module.repair_target(_target_doc(spec), spec)
        twice = repair_module.repair_target(once, spec)

        assert twice == once
        assert once["data_quality_flags"] == [
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        ]
        assert once["references"] == [{"reference": spec.togo_url}]
        matching_events = [
            event
            for event in once["curation_history"]
            if (
                event.get("curator") == repair_module.CURATOR
                and event.get("action") == repair_module.ACTION
            )
        ]
        assert len(matching_events) == 1


def test_repair_rejects_wrong_id(repair_module) -> None:
    spec = repair_module.SPECS[0]
    doc = _target_doc(spec)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=spec.expected_id):
        repair_module.repair_target(doc, spec)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    spec = repair_module.SPECS[0]
    doc = _target_doc(spec)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=spec.expected_media_term):
        repair_module.repair_target(doc, spec)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    spec = repair_module.SPECS[0]
    doc = _target_doc(spec)
    doc["ingredients"][0]["concentration"]["value"] = "2"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_target(doc, spec)
