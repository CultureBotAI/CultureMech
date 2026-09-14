from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1546_m2996_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m1546_m2996_score20")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1546_m2996")


def _doc(update) -> dict:
    return {
        "id": update.expected_id,
        "name": Path(update.path).stem,
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "TOGO Medium",
            "term": {"id": update.expected_source_term, "label": "TOGO Medium"},
        },
        "notes": "old notes",
        "ingredients": [
            {"preferred_term": name}
            for name in sorted(update.expected_ingredients)
        ],
        "curation_history": [],
    }


def test_marine_repair_normalizes_water(repair_module, scorer_module) -> None:
    update = repair_module.UPDATE_BY_PATH[repair_module.MARINE_BROTH]
    repaired = repair_module.repair_record(_doc(update), update)

    assert repaired["ingredients"] == update.recipe["ingredients"]
    assert repaired["ingredients"][0]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert repaired["references"] == [
        {"reference": repair_module.TOGO_M1546},
        {"reference": repair_module.NBRC_339},
    ]
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )


def test_pplo_repair_adds_nad_and_5_percent_co2(
    repair_module, scorer_module
) -> None:
    update = repair_module.UPDATE_BY_PATH[repair_module.PPLO]
    repaired = repair_module.repair_record(_doc(update), update)

    assert repaired["temperature_value"] == 37.0
    assert repaired["ingredients"] == update.recipe["ingredients"]
    assert {
        row["preferred_term"]: row["concentration"] for row in repaired["ingredients"]
    } == {
        "PPLO (pleuropneumonia-like organism) medium": {
            "value": "1000",
            "unit": "ML_PER_L",
        },
        "NAD": {"value": "10", "unit": "MG_PER_L"},
        "CO2": {"value": "5", "unit": "PERCENT_V_V"},
    }
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_adds_history_once(repair_module) -> None:
    update = repair_module.UPDATE_BY_PATH[repair_module.MARINE_BROTH]
    once = repair_module.repair_record(_doc(update), update)
    twice = repair_module.repair_record(once, update)

    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == "; ".join(update.reference_urls)


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    for update in repair_module.UPDATES:
        path = root / update.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(update), sort_keys=False))

    first = repair_module.plan_repairs(root)
    for repaired_path, doc in first.items():
        repaired_path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(root)

    assert {
        path.relative_to(root): repair_module.dump_record(doc)
        for path, doc in second.items()
    } == {
        path.relative_to(root): repair_module.dump_record(doc)
        for path, doc in first.items()
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    update = repair_module.UPDATE_BY_PATH[repair_module.PPLO]
    doc = _doc(update)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=update.expected_id):
        repair_module.repair_record(doc, update)


def test_repair_rejects_wrong_source(repair_module) -> None:
    update = repair_module.UPDATE_BY_PATH[repair_module.PPLO]
    doc = _doc(update)
    doc["media_term"]["term"]["id"] = "TOGO:wrong"

    with pytest.raises(ValueError, match=update.expected_source_term):
        repair_module.repair_record(doc, update)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    update = repair_module.UPDATE_BY_PATH[repair_module.MARINE_BROTH]
    doc = _doc(update)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="ingredient list drifted"):
        repair_module.repair_record(doc, update)
