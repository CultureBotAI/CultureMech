from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_962_thermincola_score10.py"
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
    return _load_script(SCRIPT, "repair_komodo_962_thermincola")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_962")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("child", tuple(_load_script(SCRIPT, "komodo_962").CHILDREN))
def test_children_link_to_dsmz_962_parent(repair_module, child) -> None:
    repaired = repair_module.repair_child(
        child.path,
        _load_yaml(repair_module.NORMALIZED / child.path),
    )

    assert repaired["parent_media"] == repair_module._parent_ref(child)
    assert repaired["variant_relationship"] == child.relationship
    assert repaired["variant_modifications"] == [child.notes]
    assert "ingredients_curated" in repaired["data_quality_flags"]


def test_strain_pointer_exits_review_ranking(repair_module, scorer_module) -> None:
    child = repair_module.CHILD_BY_PATH[Path("bacterial/for_dsm_14005.yaml")]
    repaired = repair_module.repair_child(
        child.path,
        _load_yaml(repair_module.NORMALIZED / child.path),
    )

    assert repaired["parent_media"]["relationship"] == "STRAIN_SPECIFIC_VARIANT"
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(child.path), repaired)]) == []


def test_parent_is_promoted_and_lists_962_children(repair_module) -> None:
    repaired = repair_module.repair_parent(
        _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    )

    assert "parent_media" not in repaired
    assert "variant_relationship" not in repaired
    assert "variant_modifications" not in repaired
    assert "ingredients_curated" in repaired["data_quality_flags"]
    assert repaired["variant_children"] == [
        repair_module._child_entry(child) for child in repair_module.CHILDREN
    ]


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.plan_repairs()
    twice = {
        path: repair_module.repair_parent(doc)
        if path == repair_module.NORMALIZED / repair_module.PARENT
        else repair_module.repair_child(
            path.relative_to(repair_module.NORMALIZED),
            doc,
        )
        for path, doc in once.items()
    }

    assert twice == once
    for path in once:
        assert repair_module.dump_record(twice[path]) == repair_module.dump_record(
            once[path]
        )


def test_plan_repairs_targets_current_records(repair_module) -> None:
    parent_path = repair_module.NORMALIZED / repair_module.PARENT
    expected = {
        parent_path: repair_module.repair_parent(_load_yaml(parent_path)),
    }
    for child in repair_module.CHILDREN:
        path = repair_module.NORMALIZED / child.path
        expected[path] = repair_module.repair_child(child.path, _load_yaml(path))

    assert repair_module.plan_repairs() == expected


def test_repair_rejects_wrong_child_source(repair_module) -> None:
    child = repair_module.CHILDREN[0]
    doc = _load_yaml(repair_module.NORMALIZED / child.path)
    doc["media_term"]["term"]["id"] = "komodo.medium:wrong"

    with pytest.raises(ValueError, match=child.source_term):
        repair_module.repair_child(child.path, doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    doc["ingredients"][0]["concentration"]["value"] = "1.0"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_parent(doc)
