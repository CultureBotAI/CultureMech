from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_293_propionigenium_score10.py"
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
    return _load_script(SCRIPT, "repair_komodo_293_propionigenium")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_293")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_strain_pointer_exits_review_ranking(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_child(
        _load_yaml(repair_module.NORMALIZED / repair_module.CHILD.path)
    )

    assert repaired["parent_media"]["relationship"] == "STRAIN_SPECIFIC_VARIANT"
    assert repaired["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"
    assert repaired["variant_modifications"] == [repair_module._child_notes()]
    assert "ingredients_curated" in repaired["data_quality_flags"]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.CHILD.path), repaired)]) == []


def test_parent_lists_strain_child_and_duplicate_children(repair_module) -> None:
    repaired = repair_module.repair_parent(
        _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    )

    assert repaired["variant_children"] == [
        repair_module._child_entry(),
        *[repair_module._duplicate_entry(duplicate) for duplicate in repair_module.DUPLICATES],
    ]


@pytest.mark.parametrize(
    "duplicate",
    tuple(_load_script(SCRIPT, "komodo_293_duplicates").DUPLICATES),
)
def test_duplicate_children_link_to_parent(repair_module, duplicate) -> None:
    before = _load_yaml(repair_module.NORMALIZED / duplicate.path)
    repaired = repair_module.repair_duplicate(duplicate.path, before)

    assert repaired["parent_media"]["relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module._duplicate_notes(duplicate)]
    assert "ingredients_curated" in repaired["data_quality_flags"]


def test_dsmz_duplicate_preserves_strain_specific_child(repair_module) -> None:
    duplicate = repair_module.DUPLICATES[1]
    before = _load_yaml(repair_module.NORMALIZED / duplicate.path)
    repaired = repair_module.repair_duplicate(duplicate.path, before)

    assert repaired["variant_children"] == before["variant_children"]


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.plan_repairs()
    twice = {}
    for path, doc in once.items():
        relative = path.relative_to(repair_module.NORMALIZED)
        if relative == repair_module.PARENT:
            twice[path] = repair_module.repair_parent(doc)
        elif relative == repair_module.CHILD.path:
            twice[path] = repair_module.repair_child(doc)
        else:
            twice[path] = repair_module.repair_duplicate(relative, doc)

    assert twice == once
    for path in once:
        assert repair_module.dump_record(twice[path]) == repair_module.dump_record(once[path])


def test_plan_repairs_targets_current_records(repair_module) -> None:
    expected = {
        repair_module.NORMALIZED
        / repair_module.PARENT: repair_module.repair_parent(
            _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
        ),
        repair_module.NORMALIZED
        / repair_module.CHILD.path: repair_module.repair_child(
            _load_yaml(repair_module.NORMALIZED / repair_module.CHILD.path)
        ),
    }
    for duplicate in repair_module.DUPLICATES:
        path = repair_module.NORMALIZED / duplicate.path
        expected[path] = repair_module.repair_duplicate(
            duplicate.path,
            _load_yaml(path),
        )

    assert repair_module.plan_repairs() == expected


def test_repair_rejects_wrong_strain_child_source(repair_module) -> None:
    doc = _load_yaml(repair_module.NORMALIZED / repair_module.CHILD.path)
    doc["media_term"]["term"]["id"] = "komodo.medium:wrong"

    with pytest.raises(ValueError, match=repair_module.CHILD.source_term):
        repair_module.repair_child(doc)


def test_repair_rejects_duplicate_ingredient_drift(repair_module) -> None:
    duplicate = repair_module.DUPLICATES[0]
    doc = _load_yaml(repair_module.NORMALIZED / duplicate.path)
    doc["ingredients"][0]["preferred_term"] = "Glucose"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_duplicate(duplicate.path, doc)
