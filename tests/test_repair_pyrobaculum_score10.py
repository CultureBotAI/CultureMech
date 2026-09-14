from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_pyrobaculum_score10.py"
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
    return _load_script(SCRIPT, "repair_pyrobaculum_score10")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_pyrobaculum_score10")


def _doc(repair_module, target: Path) -> dict:
    return {
        "id": repair_module.EXPECTED_IDS[target],
        "name": "pyrobaculum_calidifontis_medium",
        "category": "archaea",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "DSMZ Medium 1090",
            "term": {
                "id": "mediadive.medium:1090",
                "label": "PYROBACULUM CALIDIFONTIS MEDIUM",
            },
        },
        "notes": "Source: DSMZ",
        "ph_value": 7.0,
        "ingredients": [
            {
                "preferred_term": "Tryptone",
                "concentration": {"value": "10", "unit": "G_PER_L"},
            },
            {
                "preferred_term": "Yeast extract",
                "concentration": {"value": "1", "unit": "G_PER_L"},
            },
            {
                "preferred_term": "Na2S2O3 x 5 H2O",
                "concentration": {"value": "3", "unit": "G_PER_L"},
                "term": {
                    "id": "CHEBI:32150",
                    "label": "sodium thiosulfate pentahydrate",
                },
            },
        ],
        "curation_history": [],
    }


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("target", tuple(_load_script(SCRIPT, "pyro_targets").TARGETS))
def test_pyrobaculum_score10_records_exit_review_ranking(
    repair_module,
    scorer_module,
    target: Path,
) -> None:
    repaired = repair_module.repair_record(target, _doc(repair_module, target))

    assert repaired["ingredients"][0]["term"] == repair_module.TRYPTONE_TERM
    assert repaired["ingredients"][1]["term"] == repair_module.YEAST_EXTRACT_TERM
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(target), repaired)]) == []


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.repair_record(
        repair_module.TARGETS[0],
        _doc(repair_module, repair_module.TARGETS[0]),
    )
    twice = repair_module.repair_record(repair_module.TARGETS[0], once)

    assert twice == once
    assert repair_module.dump_record(twice) == repair_module.dump_record(once)


def test_plan_repairs_targets_current_records(repair_module) -> None:
    expected = {}
    for relative in repair_module.TARGETS:
        path = repair_module.NORMALIZED / relative
        expected[path] = repair_module.repair_record(relative, _load_yaml(path))

    assert repair_module.plan_repairs() == expected


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module, repair_module.TARGETS[0])
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_IDS[repair_module.TARGETS[0]]):
        repair_module.repair_record(repair_module.TARGETS[0], doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module, repair_module.TARGETS[0])
    doc["ingredients"][0]["preferred_term"] = "Tryptone (BD Bacto)"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(repair_module.TARGETS[0], doc)
