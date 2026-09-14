from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_870_syntrophothermus_score10.py"
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
    return _load_script(SCRIPT, "repair_komodo_870_syntrophothermus")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_870")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("child", tuple(_load_script(SCRIPT, "komodo_870").CHILDREN))
def test_strain_pointers_exit_review_ranking(
    repair_module,
    scorer_module,
    child,
) -> None:
    repaired = repair_module.repair_child(
        child.path,
        _load_yaml(repair_module.NORMALIZED / child.path),
    )

    assert repaired["parent_media"] == repair_module._parent_ref(child)
    assert repaired["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"
    assert repaired["variant_modifications"] == [repair_module._notes(child)]
    assert "ingredients_curated" in repaired["data_quality_flags"]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(child.path), repaired)]) == []


def test_parent_preserves_dsmz_parent_and_lists_strain_children(repair_module) -> None:
    repaired = repair_module.repair_parent(
        _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    )

    assert repaired["parent_media"]["id"] == "CultureMech:002028"
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_children"] == [
        repair_module._child_entry(child) for child in repair_module.CHILDREN
    ]
    assert "ingredients_curated" in repaired["data_quality_flags"]


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


def test_repair_rejects_parent_ingredient_drift(repair_module) -> None:
    doc = _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    doc["ingredients"][0]["concentration"]["value"] = "0.14"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_parent(doc)
