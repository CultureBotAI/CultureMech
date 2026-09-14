from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_communitymech_sources_score10_batch10.py"
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
    return _load_script(SCRIPT, "repair_communitymech_sources_score10_batch10")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_communitymech_sources_batch10")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("target", tuple(_load_script(SCRIPT, "batch10").TARGETS))
def test_communitymech_imports_exit_review_ranking(
    repair_module,
    scorer_module,
    target,
) -> None:
    repaired = repair_module.repair_record(
        target.path,
        _load_yaml(repair_module.NORMALIZED / target.path),
    )

    assert repaired["sources"] == repair_module._sources(target)
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(target.path), repaired)]) == []


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
    doc = {
        "id": "CultureMech:wrong",
        "source_data": {
            "origin": "CommunityMech",
            "community_ids": list(target.community_ids),
        },
    }

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(target.path, doc)


def test_repair_rejects_wrong_origin(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = {
        "id": target.record_id,
        "source_data": {
            "origin": "MediaDive",
            "community_ids": list(target.community_ids),
        },
    }

    with pytest.raises(ValueError, match="CommunityMech source_data.origin"):
        repair_module.repair_record(target.path, doc)


def test_repair_rejects_wrong_community_ids(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = {
        "id": target.record_id,
        "source_data": {
            "origin": "CommunityMech",
            "community_ids": ["CommunityMech:wrong"],
        },
    }

    with pytest.raises(ValueError, match="expected community_ids"):
        repair_module.repair_record(target.path, doc)
