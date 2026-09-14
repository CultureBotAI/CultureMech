from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_helicobacter_medium_1279_score10.py"
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
    return _load_script(SCRIPT, "repair_helicobacter_medium_1279_score10")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_helicobacter_1279")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_helicobacter_exits_review_ranking(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(
        _load_yaml(repair_module.NORMALIZED / repair_module.TARGET)
    )

    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_commercial_additions_get_exact_mediadive_terms(repair_module) -> None:
    repaired = repair_module.repair_record(
        _load_yaml(repair_module.NORMALIZED / repair_module.TARGET)
    )
    by_name = {row["preferred_term"]: row for row in repaired["ingredients"]}

    for preferred_term, term in repair_module.TERMS.items():
        assert by_name[preferred_term]["term"] == term
        assert by_name[preferred_term]["source"] == "MediaDive solution 2559"
        assert by_name[preferred_term]["notes"] == repair_module.NOTES[preferred_term]


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.repair_record(
        _load_yaml(repair_module.NORMALIZED / repair_module.TARGET)
    )
    twice = repair_module.repair_record(once)

    assert twice == once
    assert repair_module.dump_record(twice) == repair_module.dump_record(once)


def test_plan_repairs_targets_current_record(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    assert repair_module.plan_repairs() == {
        path: repair_module.repair_record(_load_yaml(path))
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _load_yaml(repair_module.NORMALIZED / repair_module.TARGET)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.TARGET_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _load_yaml(repair_module.NORMALIZED / repair_module.TARGET)
    doc["ingredients"][0]["preferred_term"] = "Peptone"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)
