from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_901_acidolobus_score10.py"
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
    return _load_script(SCRIPT, "repair_komodo_901_acidolobus")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_901")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_dsmz_parent_lists_komodo_source_duplicate(repair_module) -> None:
    repaired = repair_module.repair_dsmz_parent(
        _load_yaml(repair_module.NORMALIZED / repair_module.DSMZ_PARENT)
    )

    assert "ingredients_curated" in repaired["data_quality_flags"]
    assert repaired["variant_children"] == [repair_module._komodo_child_entry()]


def test_komodo_parent_links_to_dsmz_and_lists_strain_child(repair_module) -> None:
    repaired = repair_module.repair_komodo_parent(
        _load_yaml(repair_module.NORMALIZED / repair_module.KOMODO_PARENT)
    )

    assert repaired["parent_media"] == repair_module._dsmz_parent_ref()
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.SOURCE_DUPLICATE_NOTES]
    assert repaired["variant_children"] == [repair_module._strain_child_entry()]
    assert "ingredients_curated" in repaired["data_quality_flags"]


def test_child_links_to_komodo_parent(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_child(
        _load_yaml(repair_module.NORMALIZED / repair_module.CHILD)
    )

    assert repaired["parent_media"] == repair_module._komodo_parent_ref()
    assert repaired["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"
    assert repaired["variant_modifications"] == [repair_module.STRAIN_NOTES]
    assert "ingredients_curated" in repaired["data_quality_flags"]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.CHILD), repaired)]) == []


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.plan_repairs()
    twice = {
        path: repair_module.repair_dsmz_parent(doc)
        if path == repair_module.NORMALIZED / repair_module.DSMZ_PARENT
        else repair_module.repair_komodo_parent(doc)
        if path == repair_module.NORMALIZED / repair_module.KOMODO_PARENT
        else repair_module.repair_child(doc)
        for path, doc in once.items()
    }

    assert twice == once
    for path in once:
        assert repair_module.dump_record(twice[path]) == repair_module.dump_record(
            once[path]
        )


def test_plan_repairs_targets_current_records(repair_module) -> None:
    dsmz_path = repair_module.NORMALIZED / repair_module.DSMZ_PARENT
    parent_path = repair_module.NORMALIZED / repair_module.KOMODO_PARENT
    child_path = repair_module.NORMALIZED / repair_module.CHILD

    assert repair_module.plan_repairs() == {
        dsmz_path: repair_module.repair_dsmz_parent(_load_yaml(dsmz_path)),
        parent_path: repair_module.repair_komodo_parent(_load_yaml(parent_path)),
        child_path: repair_module.repair_child(_load_yaml(child_path)),
    }


def test_repair_rejects_wrong_child_source(repair_module) -> None:
    doc = _load_yaml(repair_module.NORMALIZED / repair_module.CHILD)
    doc["media_term"]["term"]["id"] = "komodo.medium:wrong"

    with pytest.raises(ValueError, match=repair_module.CHILD_SOURCE_TERM):
        repair_module.repair_child(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _load_yaml(repair_module.NORMALIZED / repair_module.KOMODO_PARENT)
    doc["ingredients"][0]["concentration"]["value"] = "1.0"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_komodo_parent(doc)
