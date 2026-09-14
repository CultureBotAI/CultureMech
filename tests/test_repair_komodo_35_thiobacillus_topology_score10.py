from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_35_thiobacillus_topology_score10.py"
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
    return _load_script(SCRIPT, "repair_komodo_35_thiobacillus_topology_score10")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_35")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_ranked_strain_records_exit_review_ranking(repair_module, scorer_module) -> None:
    for child in repair_module.CHILDREN:
        repaired = repair_module.repair_child(
            _load_yaml(repair_module.NORMALIZED / child.path),
            child,
        )

        assert repaired["parent_media"]["relationship"] == child.relationship
        assert repaired["variant_relationship"] == child.relationship
        assert "ingredients_curated" in repaired["data_quality_flags"]
        assert scorer_module.score_record(repaired) == (0, [])
        assert scorer_module.score_parsed([(str(child.path), repaired)]) == []


def test_base_medium_replaces_strain_specific_parent(repair_module) -> None:
    repaired = repair_module.repair_parent(
        _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    )

    assert "parent_media" not in repaired
    assert "variant_relationship" not in repaired
    assert "variant_modifications" not in repaired
    assert repaired["variant_children"] == [
        repair_module._child_entry(child) for child in repair_module.CHILDREN
    ]


def test_old_parent_loses_variant_children(repair_module) -> None:
    child = repair_module.CHILDREN[0]
    repaired = repair_module.repair_child(
        _load_yaml(repair_module.NORMALIZED / child.path),
        child,
    )

    assert "variant_children" not in repaired
    assert repaired["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.plan_repairs()
    twice = {
        path: repair_module.repair_parent(doc)
        if path == repair_module.NORMALIZED / repair_module.PARENT
        else repair_module.repair_child(
            doc,
            next(
                child
                for child in repair_module.CHILDREN
                if path == repair_module.NORMALIZED / child.path
            ),
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
    doc["ingredients"][0]["preferred_term"] = "NaCl"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_child(doc, child)


def test_repair_rejects_child_ph_drift(repair_module) -> None:
    child = repair_module.CHILDREN[1]
    doc = _load_yaml(repair_module.NORMALIZED / child.path)
    doc["ph_value"] = 4.2

    with pytest.raises(ValueError, match="expected pH"):
        repair_module.repair_child(doc, child)
