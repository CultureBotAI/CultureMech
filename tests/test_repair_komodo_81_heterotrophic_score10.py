from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_81_heterotrophic_score10.py"
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
    return _load_script(SCRIPT, "repair_komodo_81_heterotrophic")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_81")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_dsm_variant_exits_review_ranking(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_child(
        _load_yaml(repair_module.NORMALIZED / repair_module.CHILD)
    )

    assert repaired["parent_media"] == repair_module._parent_ref()
    assert repaired["variant_relationship"] == repair_module.RELATIONSHIP
    assert "ingredients_curated" in repaired["data_quality_flags"]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.CHILD), repaired)]) == []


def test_parent_updates_only_dsm_21436_edge(repair_module) -> None:
    before = _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    repaired = repair_module.repair_parent(before)

    before_by_path = {entry["path"]: entry for entry in before["variant_children"]}
    after_by_path = {entry["path"]: entry for entry in repaired["variant_children"]}
    child_path = f"data/normalized_yaml/{repair_module.CHILD}"

    assert after_by_path[child_path] == repair_module._child_entry()
    assert set(after_by_path) == set(before_by_path)
    for path, entry in after_by_path.items():
        if path != child_path:
            assert entry == before_by_path[path]


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.plan_repairs()
    twice = {
        path: repair_module.repair_parent(doc)
        if path == repair_module.NORMALIZED / repair_module.PARENT
        else repair_module.repair_child(doc)
        for path, doc in once.items()
    }

    assert twice == once
    for path in once:
        assert repair_module.dump_record(twice[path]) == repair_module.dump_record(
            once[path]
        )


def test_plan_repairs_targets_current_records(repair_module) -> None:
    assert repair_module.plan_repairs() == {
        repair_module.NORMALIZED / repair_module.PARENT: repair_module.repair_parent(
            _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
        ),
        repair_module.NORMALIZED / repair_module.CHILD: repair_module.repair_child(
            _load_yaml(repair_module.NORMALIZED / repair_module.CHILD)
        ),
    }


def test_repair_rejects_wrong_child_source(repair_module) -> None:
    doc = _load_yaml(repair_module.NORMALIZED / repair_module.CHILD)
    doc["media_term"]["term"]["id"] = "komodo.medium:wrong"

    with pytest.raises(ValueError, match=repair_module.CHILD_SOURCE_TERM):
        repair_module.repair_child(doc)


def test_repair_rejects_child_solution_drift(repair_module) -> None:
    doc = _load_yaml(repair_module.NORMALIZED / repair_module.CHILD)
    doc["solutions"][0]["composition"][0]["preferred_term"] = "Nicotinic acid"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_child(doc)
