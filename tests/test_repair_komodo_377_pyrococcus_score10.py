from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_377_pyrococcus_score10.py"
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
    return _load_script(SCRIPT, "repair_komodo_377_pyrococcus")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_377")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _child_by_path(repair_module):
    return {f"data/normalized_yaml/{child.path}": child for child in repair_module.CHILDREN}


def test_ph_variant_exits_review_ranking(repair_module, scorer_module) -> None:
    child = _child_by_path(repair_module)["data/normalized_yaml/bacterial/for_dsm_19918.yaml"]
    repaired = repair_module.repair_child(
        _load_yaml(repair_module.NORMALIZED / child.path),
        child,
    )

    assert repaired["parent_media"]["relationship"] == "PH_VARIANT"
    assert repaired["variant_relationship"] == "PH_VARIANT"
    assert "ingredients_curated" in repaired["data_quality_flags"]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(child.path), repaired)]) == []


def test_parent_promotes_medium_377_root(repair_module) -> None:
    before = _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    repaired = repair_module.repair_parent(before)
    by_path = {entry["path"]: entry for entry in repaired["variant_children"]}

    assert "parent_media" not in repaired
    assert "variant_relationship" not in repaired
    assert "variant_modifications" not in repaired
    assert set(by_path) == set(_child_by_path(repair_module))
    for path, child in _child_by_path(repair_module).items():
        assert by_path[path] == repair_module._child_entry(child)


def test_old_hub_becomes_child(repair_module) -> None:
    child = _child_by_path(repair_module)["data/normalized_yaml/bacterial/for_dsm_19918.yaml"]
    repaired = repair_module.repair_child(
        _load_yaml(repair_module.NORMALIZED / child.path),
        child,
    )

    assert "variant_children" not in repaired
    assert repaired["parent_media"] == repair_module._parent_ref(child)
    assert repaired["variant_relationship"] == "PH_VARIANT"


def test_archaea_child_path_is_preserved(repair_module) -> None:
    child = _child_by_path(repair_module)["data/normalized_yaml/archaea/pyrococcus_st04_medium.yaml"]
    repaired = repair_module.repair_child(
        _load_yaml(repair_module.NORMALIZED / child.path),
        child,
    )

    assert repaired["parent_media"]["path"] == (
        "data/normalized_yaml/archaea/pyrococcus_staphylothermus_medium.yaml"
    )


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.plan_repairs()
    twice = {
        path: repair_module.repair_parent(doc)
        if path == repair_module.NORMALIZED / repair_module.PARENT
        else repair_module.repair_child(
            doc,
            _child_by_path(repair_module)[
                f"data/normalized_yaml/{path.relative_to(repair_module.NORMALIZED)}"
            ],
        )
        for path, doc in once.items()
    }

    assert twice == once
    for path in once:
        assert repair_module.dump_record(twice[path]) == repair_module.dump_record(
            once[path]
        )


def test_plan_repairs_targets_current_records(repair_module) -> None:
    expected = {
        repair_module.NORMALIZED / repair_module.PARENT: repair_module.repair_parent(
            _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
        )
    }
    for child in repair_module.CHILDREN:
        expected[repair_module.NORMALIZED / child.path] = repair_module.repair_child(
            _load_yaml(repair_module.NORMALIZED / child.path),
            child,
        )

    assert repair_module.plan_repairs() == expected


def test_repair_rejects_wrong_child_source(repair_module) -> None:
    child = repair_module.CHILDREN[-1]
    doc = _load_yaml(repair_module.NORMALIZED / child.path)
    doc["media_term"]["term"]["id"] = "komodo.medium:wrong"

    with pytest.raises(ValueError, match=child.source_term):
        repair_module.repair_child(doc, child)


def test_repair_rejects_child_ingredient_drift(repair_module) -> None:
    child = repair_module.CHILDREN[-1]
    doc = _load_yaml(repair_module.NORMALIZED / child.path)
    doc["ingredients"][0]["preferred_term"] = "MgSO4 x 7 H2O"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_child(doc, child)
