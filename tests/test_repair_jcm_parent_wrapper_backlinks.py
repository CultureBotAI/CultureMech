from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_parent_wrapper_backlinks.py"
VALIDATOR = REPO / "scripts" / "validate_media_variant_links.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_jcm_parent_wrapper_backlinks")


@pytest.fixture(scope="module")
def validator_module():
    return _load_script(VALIDATOR, "validate_media_variant_links_for_jcm_backlinks")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_parents_gain_missing_reciprocal_child_links(repair_module) -> None:
    repaired = repair_module.plan_repairs()

    rhodobium = repaired[repair_module.NORMALIZED / repair_module.RHODOBIUM.path]
    thiorhodococcus = repaired[repair_module.NORMALIZED / repair_module.THIORHODOCOCCUS.path]

    assert repair_module._child_entry(repair_module.CHILDREN[0]) in rhodobium["variant_children"]
    assert thiorhodococcus["variant_children"] == [
        repair_module._child_entry(child) for child in repair_module.CHILDREN[1:]
    ]


def test_existing_rhodobium_children_are_preserved(repair_module) -> None:
    before = _load_yaml(repair_module.NORMALIZED / repair_module.RHODOBIUM.path)
    repaired = repair_module.repair_parent(repair_module.RHODOBIUM, before)

    before_by_id = {child["id"]: child for child in before["variant_children"]}
    after_by_id = {child["id"]: child for child in repaired["variant_children"]}

    assert set(after_by_id) == set(before_by_id) | {repair_module.CHILDREN[0].record_id}
    for record_id, child in before_by_id.items():
        assert after_by_id[record_id] == child


def test_repaired_links_validate(repair_module, validator_module) -> None:
    plans = repair_module.plan_repairs()

    path_to_recipe = {
        f"data/normalized_yaml/{parent.path}": plans[repair_module.NORMALIZED / parent.path]
        for parent in repair_module.PARENTS
    }
    path_to_recipe.update(
        {
            f"data/normalized_yaml/{child.path}": _load_yaml(repair_module.NORMALIZED / child.path)
            for child in repair_module.CHILDREN
        }
    )
    for parent in repair_module.PARENTS:
        for child in plans[repair_module.NORMALIZED / parent.path]["variant_children"]:
            if child["path"] not in path_to_recipe:
                path_to_recipe[child["path"]] = _load_yaml(REPO / child["path"])
    index = validator_module.RecipeIndex(
        path_to_recipe=path_to_recipe,
        id_to_path={doc["id"]: path for path, doc in path_to_recipe.items()},
    )

    assert validator_module.validate_links(index) == []


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.plan_repairs()
    twice = {
        path: repair_module.repair_parent(
            (
                repair_module.RHODOBIUM
                if path == repair_module.NORMALIZED / repair_module.RHODOBIUM.path
                else repair_module.THIORHODOCOCCUS
            ),
            doc,
        )
        for path, doc in once.items()
    }

    assert twice == once
    for path in once:
        assert repair_module.dump_record(twice[path]) == repair_module.dump_record(once[path])


def test_plan_repairs_targets_current_records(repair_module) -> None:
    assert repair_module.plan_repairs() == {
        repair_module.NORMALIZED
        / parent.path: repair_module.repair_parent(
            parent,
            _load_yaml(repair_module.NORMALIZED / parent.path),
        )
        for parent in repair_module.PARENTS
    }


def test_child_parent_drift_is_rejected(repair_module) -> None:
    child = repair_module.CHILDREN[0]
    doc = _load_yaml(repair_module.NORMALIZED / child.path)
    doc["parent_media"]["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="parent_media no longer matches"):
        repair_module._require_child(child, doc)
