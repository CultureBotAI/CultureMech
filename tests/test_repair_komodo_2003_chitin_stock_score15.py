from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_2003_chitin_stock_score15.py"
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
    return _load_script(SCRIPT, "repair_komodo_2003_chitin_stock_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_chitin_stock")


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.RECORD_ID,
        "name": repair_module.PATH.stem,
        "original_name": "Chitin stock solution (medium 766)",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 6.5,
        "notes": "pH buffer: KOH | Source: KOMODO ModelSEED | ID: 2003",
        "media_term": {
            "preferred_term": "KOMODO Medium 2003",
            "term": {
                "id": repair_module.MEDIA_TERM,
                "label": "Chitin stock solution (medium 766)",
            },
        },
        "ingredients": [
            {
                "preferred_term": "KOH",
                "concentration": {"value": "variable", "unit": "VARIABLE"},
            }
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_adds_dsmz_766_chitin_stock_reagents_and_scores_clean(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENTS
    )
    assert ingredients["Chitin"]["concentration"] == {
        "value": "16.6667",
        "unit": "G_PER_L",
    }
    assert ingredients["Hydrochloric acid, 37%"]["concentration"] == {
        "value": "166.6667",
        "unit": "ML_PER_L",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "833.3333",
        "unit": "ML_PER_L",
    }
    assert ingredients["Potassium hydroxide, 5 M"]["term"] == {
        "id": "CHEBI:32035",
        "label": "potassium hydroxide",
    }
    assert scorer_module.score_parsed(
        [(str(repair_module.PATH), repaired)]
    ) == []


def test_repair_replaces_preparation_steps_and_adds_event_once(
    repair_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert [step["action"] for step in twice["preparation_steps"]] == [
        "COOL",
        "MIX",
        "FILTER",
        "MIX",
        "ADJUST_PH",
        "FILTER",
    ]
    assert twice["references"] == [{"reference": repair_module.DSMZ_766}]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
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
    assert matching_events[0]["source"] == repair_module.DSMZ_766


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "komodo.medium:2004"

    with pytest.raises(ValueError, match="expected media term komodo.medium:2003"):
        repair_module.repair_record(doc)


def test_repair_rejects_component_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"]["value"] = "1"

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
