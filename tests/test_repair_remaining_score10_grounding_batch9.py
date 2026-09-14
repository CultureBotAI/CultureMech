from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_remaining_score10_grounding_batch9.py"
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
    return _load_script(SCRIPT, "repair_remaining_score10_grounding_batch9")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_grounding_batch9")


def _ingredient(name: str, grounded: bool = False) -> dict:
    row = {"preferred_term": name, "concentration": {"value": "1", "unit": "G_PER_L"}}
    if grounded:
        row["term"] = {"id": "CHEBI:2509", "label": "agar"}
    return row


def _doc(repair_module, target) -> dict:
    return {
        "id": target.record_id,
        "name": target.path.stem,
        "category": target.path.parts[0],
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "DSMZ Medium",
            "term": {"id": "mediadive.medium:test", "label": target.path.stem},
        },
        "notes": "Source: DSMZ",
        "ph_value": 7.0,
        "ingredients": [
            _ingredient(name, grounded=name not in target.exact_terms) for name in target.signature
        ],
        "curation_history": [],
    }


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("target", tuple(_load_script(SCRIPT, "batch9").TARGETS))
def test_grounding_records_exit_review_ranking(
    repair_module,
    scorer_module,
    target,
) -> None:
    repaired = repair_module.repair_record(
        target.path,
        _load_yaml(repair_module.NORMALIZED / target.path),
    )

    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(target.path), repaired)]) == []


@pytest.mark.parametrize("target", tuple(_load_script(SCRIPT, "batch9_unmapped").TARGETS))
def test_intentionally_unmapped_names_stay_unmapped(repair_module, target) -> None:
    if not target.reviewed_unmapped_terms:
        return

    repaired = repair_module.repair_record(
        target.path,
        _load_yaml(repair_module.NORMALIZED / target.path),
    )
    by_name = {row["preferred_term"]: row for row in repaired["ingredients"]}

    assert set(repair_module.CURATED_UNMAPPED_FLAGS) <= set(repaired["data_quality_flags"])
    for preferred_term in target.reviewed_unmapped_terms:
        assert "term" not in by_name[preferred_term]


def test_widdel_hydrate_terms_are_grounded(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH[
        Path("bacterial/widdel_freshwater_medium_with_pyruvate.yaml")
    ]
    repaired = repair_module.repair_record(
        target.path,
        _load_yaml(repair_module.NORMALIZED / target.path),
    )
    by_name = {row["preferred_term"]: row for row in repaired["ingredients"]}

    for preferred_term in target.exact_terms:
        assert by_name[preferred_term]["term"] == repair_module.TERMS[preferred_term]


def test_repair_is_idempotent(repair_module) -> None:
    target = repair_module.TARGETS[0]
    once = repair_module.repair_record(
        target.path,
        _load_yaml(repair_module.NORMALIZED / target.path),
    )
    twice = repair_module.repair_record(target.path, once)

    assert twice == once
    assert repair_module.dump_record(twice) == repair_module.dump_record(once)


def test_plan_repairs_targets_current_records(repair_module) -> None:
    expected = {}
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.path
        expected[path] = repair_module.repair_record(target.path, _load_yaml(path))

    assert repair_module.plan_repairs() == expected


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(target.path, doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["ingredients"][0]["preferred_term"] = "Peptone"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(target.path, doc)
