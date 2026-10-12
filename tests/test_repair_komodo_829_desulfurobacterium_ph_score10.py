from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_829_desulfurobacterium_ph_score10.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def repair_module(tmp_path, monkeypatch):
    module = _load_script(SCRIPT, "repair_komodo_829_desulfurobacterium_ph_score10")
    folder = REPO / "reports/ingredient_concentration_curation/20261009-desulfurobacterium-family"
    raw = (folder / "plan-v2.json").read_bytes()
    receipt = json.loads((folder / "apply.json").read_text())
    assert receipt["terminal"] and receipt["plan_sha256"] == hashlib.sha256(raw).hexdigest()
    wanted = {module.PARENT_ID, *(child.record_id for child in module.CHILDREN)}
    records = [r for r in json.loads(raw)["records"] if r["id"] in wanted]
    assert len(records) == len(wanted) == 3
    # Exercise the historical mutator on its reviewed baseline, never undo the
    # later source-specific curation to satisfy this older composition guard.
    for item in records:
        before = item["before_text"].encode()
        assert hashlib.sha256(before).hexdigest() == item["before_sha256"]
        relative = Path(item["path"]).relative_to("data/normalized_yaml")
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(before)
    monkeypatch.setattr(module, "NORMALIZED", tmp_path)
    return module


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_829")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_variants_exit_review_ranking(repair_module, scorer_module) -> None:
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


def test_parent_preserves_other_children(repair_module) -> None:
    before = _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    repaired = repair_module.repair_parent(before)
    by_path = {entry["path"]: entry for entry in repaired["variant_children"]}
    expected_paths = {f"data/normalized_yaml/{child.path}" for child in repair_module.CHILDREN}

    for child in repair_module.CHILDREN:
        assert by_path[f"data/normalized_yaml/{child.path}"] == repair_module._child_entry(child)
    for entry in before["variant_children"]:
        if entry["path"] not in expected_paths:
            assert by_path[entry["path"]] == entry


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.plan_repairs(repair_module.NORMALIZED)
    twice = {
        path: (
            repair_module.repair_parent(doc)
            if path == repair_module.NORMALIZED / repair_module.PARENT
            else repair_module.repair_child(
                doc,
                next(
                    child
                    for child in repair_module.CHILDREN
                    if path == repair_module.NORMALIZED / child.path
                ),
            )
        )
        for path, doc in once.items()
    }

    assert twice == once
    for path in once:
        assert repair_module.dump_record(twice[path]) == repair_module.dump_record(once[path])


def test_plan_repairs_targets_reviewed_baseline(repair_module) -> None:
    expected = {
        repair_module.NORMALIZED
        / repair_module.PARENT: repair_module.repair_parent(
            _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
        )
    }
    for child in repair_module.CHILDREN:
        expected[repair_module.NORMALIZED / child.path] = repair_module.repair_child(
            _load_yaml(repair_module.NORMALIZED / child.path),
            child,
        )

    assert repair_module.plan_repairs(repair_module.NORMALIZED) == expected


def test_legacy_plan_refuses_source_curated_current_corpus(repair_module) -> None:
    with pytest.raises(ValueError, match="composition signature drifted"):
        repair_module.plan_repairs(REPO / "data/normalized_yaml")


@pytest.mark.parametrize("key", ["parent", "child0", "child1"])
def test_legacy_repair_refuses_source_curated_current_records(repair_module, key) -> None:
    if key == "parent":
        path = repair_module.PARENT
        repair = repair_module.repair_parent
    else:
        child = repair_module.CHILDREN[int(key[-1])]
        path = child.path

        def repair(doc):
            return repair_module.repair_child(doc, child)

    current = REPO / "data/normalized_yaml" / path
    before = current.read_bytes()
    with pytest.raises(ValueError, match="composition signature drifted"):
        repair(yaml.safe_load(before))
    assert current.read_bytes() == before


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


def test_repair_rejects_child_composition_drift(repair_module) -> None:
    child = repair_module.CHILDREN[0]
    doc = _load_yaml(repair_module.NORMALIZED / child.path)
    doc["solutions"][0]["composition"][0]["preferred_term"] = "FeCl3"

    with pytest.raises(ValueError, match="composition signature drifted"):
        repair_module.repair_child(doc, child)


def test_repair_rejects_child_ph_drift(repair_module) -> None:
    child = next(child for child in repair_module.CHILDREN if child.relationship == "PH_VARIANT")
    doc = _load_yaml(repair_module.NORMALIZED / child.path)
    doc["ph_value"] = 6.0

    with pytest.raises(ValueError, match="expected pH"):
        repair_module.repair_child(doc, child)
