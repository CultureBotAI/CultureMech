from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2974_bhi_tt_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2974_bhi_tt_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2974_bhi_tt")


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.RECORD_ID,
        "name": repair_module.PATH.stem,
        "original_name": (
            "brain-heart infusion broth (supplemented with 0.1% Tris base "
            "and 0.001% thiamine monophosphate)"
        ),
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            {
                "preferred_term": name,
                "concentration": {"value": value, "unit": unit},
            }
            for name, value, unit in repair_module.IMPORTED_INGREDIENTS
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2974",
            "term": {"id": repair_module.MEDIA_TERM, "label": "BHI-TT"},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_converts_one_liter_bhi_to_volume_and_grounds_thiamine(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENTS
    )
    assert ingredients["brain-heart infusion broth (Difco Laboratories)"][
        "concentration"
    ] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["thiamine monophosphate"]["term"] == {
        "id": "CHEBI:9533",
        "label": "thiamine(1+) monophosphate",
    }
    assert scorer_module.score_parsed(
        [(str(repair_module.PATH), repaired)]
    ) == []


def test_repair_adds_provenance_flags_references_and_event_once(
    repair_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["notes"] == repair_module.NOTES
    assert twice["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert twice["references"] == [{"reference": repair_module.TOGO_M2974}]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
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
    assert matching_events[0]["source"] == repair_module.TOGO_M2974


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M2975"

    with pytest.raises(ValueError, match="expected media term TOGO:M2974"):
        repair_module.repair_record(doc)


def test_repair_rejects_component_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"]["value"] = "0.2"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
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
