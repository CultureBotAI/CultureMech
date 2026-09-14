from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_591_halobacteroides_ph_score10.py"
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
    return _load_script(SCRIPT, "repair_komodo_591_halobacteroides_ph_score10")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_591")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_ph_variant_exits_review_ranking(repair_module, scorer_module) -> None:
    child = repair_module.CHILDREN[0]
    repaired = repair_module.repair_child(
        _load_yaml(repair_module.NORMALIZED / child.path),
        child,
    )

    assert repaired["parent_media"]["relationship"] == "PH_VARIANT"
    assert repaired["variant_relationship"] == "PH_VARIANT"
    assert "ingredients_curated" in repaired["data_quality_flags"]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(child.path), repaired)]) == []


def test_parent_preserves_same_ph_duplicate_child(repair_module) -> None:
    before = _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    repaired = repair_module.repair_parent(before)
    by_path = {entry["path"]: entry for entry in repaired["variant_children"]}
    child = repair_module.CHILDREN[0]
    expected_path = f"data/normalized_yaml/{child.path}"

    assert by_path[expected_path] == repair_module._child_entry(child)
    for entry in before["variant_children"]:
        if entry["path"] != expected_path:
            assert by_path[entry["path"]] == entry


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.plan_repairs()
    twice = {
        path: (
            repair_module.repair_parent(doc)
            if path == repair_module.NORMALIZED / repair_module.PARENT
            else repair_module.repair_child(doc, repair_module.CHILDREN[0])
        )
        for path, doc in once.items()
    }

    assert twice == once
    for path in once:
        assert repair_module.dump_record(twice[path]) == repair_module.dump_record(once[path])


def test_plan_repairs_targets_current_records(repair_module) -> None:
    child = repair_module.CHILDREN[0]
    assert repair_module.plan_repairs() == {
        repair_module.NORMALIZED
        / repair_module.PARENT: repair_module.repair_parent(
            _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
        ),
        repair_module.NORMALIZED
        / child.path: repair_module.repair_child(
            _load_yaml(repair_module.NORMALIZED / child.path),
            child,
        ),
    }


def test_repair_rejects_wrong_parent_id(repair_module) -> None:
    doc = _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.PARENT_ID):
        repair_module.repair_parent(doc)


def test_repair_rejects_wrong_child_source(repair_module) -> None:
    child = repair_module.CHILDREN[0]
    doc = _load_yaml(repair_module.NORMALIZED / child.path)
    doc["media_term"]["term"]["id"] = "komodo.medium:wrong"

    with pytest.raises(ValueError, match=child.source_term):
        repair_module.repair_child(doc, child)


def test_repair_rejects_child_ingredient_drift(repair_module) -> None:
    child = repair_module.CHILDREN[0]
    doc = _load_yaml(repair_module.NORMALIZED / child.path)
    doc["ingredients"][0]["preferred_term"] = "NH4Br"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_child(doc, child)


def test_repair_rejects_child_ph_drift(repair_module) -> None:
    child = repair_module.CHILDREN[0]
    doc = _load_yaml(repair_module.NORMALIZED / child.path)
    doc["ph_value"] = 7.5

    with pytest.raises(ValueError, match="expected pH"):
        repair_module.repair_child(doc, child)
