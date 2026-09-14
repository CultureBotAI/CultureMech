from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_298b1_luphet1_score10.py"
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
    return _load_script(SCRIPT, "repair_komodo_298b1_luphet1")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_298b1")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_strain_pointer_exits_review_ranking(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_child(
        _load_yaml(repair_module.NORMALIZED / repair_module.CHILD)
    )

    assert repaired["parent_media"] == repair_module._parent_ref()
    assert repaired["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"
    assert repaired["variant_modifications"] == [repair_module.NOTE]
    assert "ingredients_curated" in repaired["data_quality_flags"]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.CHILD), repaired)]) == []


def test_parent_reclassifies_only_dsm_8271_child(repair_module) -> None:
    before = _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    repaired = repair_module.repair_parent(before)

    before_by_id = {child["id"]: child for child in before["variant_children"]}
    after_by_id = {child["id"]: child for child in repaired["variant_children"]}

    assert after_by_id[repair_module.CHILD_ID] == repair_module._child_entry()
    assert set(after_by_id) == set(before_by_id)
    for record_id in set(after_by_id) - {repair_module.CHILD_ID}:
        assert after_by_id[record_id] == before_by_id[record_id]


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


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    doc["ingredients"][0]["preferred_term"] = "Glucose"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_parent(doc)
