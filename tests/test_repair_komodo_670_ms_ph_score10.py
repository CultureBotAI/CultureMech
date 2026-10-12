"""Historical migration behavior, not scientific approval of strain formulations."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_670_ms_ph_score10.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module(tmp_path_factory):
    module = _load_script(SCRIPT, "repair_komodo_670_ms_ph_score10")
    fixture = json.loads((REPO / "tests/fixtures/komodo670_legacy_migration.json").read_text())
    root = tmp_path_factory.mktemp("legacy-komodo670")
    # A historical flat-recipe migration must not constrain later source-backed curation.
    for relative, item in fixture["records"].items():
        raw = item["text"].encode()
        assert hashlib.sha256(raw).hexdigest() == item["sha256"]
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
    module.NORMALIZED = root
    return module


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_670")


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("child", tuple(_load_script(SCRIPT, "komodo_670").CHILDREN))
def test_ms_ph_variants_exit_review_ranking(
    repair_module,
    scorer_module,
    child,
) -> None:
    repaired = repair_module.repair_child(
        child.path,
        _load_yaml(repair_module.NORMALIZED / child.path),
    )

    assert repaired["parent_media"]["relationship"] == "PH_VARIANT"
    assert repaired["variant_relationship"] == "PH_VARIANT"
    assert "ingredients_curated" in repaired["data_quality_flags"]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(child.path), repaired)]) == []


def test_parent_lists_all_ph_variant_children(repair_module) -> None:
    repaired = repair_module.repair_parent(
        _load_yaml(repair_module.NORMALIZED / repair_module.PARENT),
    )

    assert repaired["variant_children"] == [
        *repair_module.SOURCE_DUPLICATE_CHILDREN,
        *[repair_module._child_entry(child) for child in repair_module.CHILDREN],
    ]


def test_repair_is_idempotent(repair_module) -> None:
    once = repair_module.plan_repairs(repair_module.NORMALIZED)
    twice = {
        path: (
            repair_module.repair_parent(doc)
            if path == repair_module.NORMALIZED / repair_module.PARENT
            else repair_module.repair_child(path.relative_to(repair_module.NORMALIZED), doc)
        )
        for path, doc in once.items()
    }

    assert twice == once


def test_plan_repairs_targets_historical_records(repair_module) -> None:
    expected = {
        repair_module.NORMALIZED
        / repair_module.PARENT: repair_module.repair_parent(
            _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
        )
    }
    for child in repair_module.CHILDREN:
        path = repair_module.NORMALIZED / child.path
        expected[path] = repair_module.repair_child(child.path, _load_yaml(path))

    assert repair_module.plan_repairs(repair_module.NORMALIZED) == expected


def test_repair_rejects_wrong_parent_id(repair_module) -> None:
    doc = _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.PARENT_ID):
        repair_module.repair_parent(doc)


def test_repair_rejects_wrong_child_id(repair_module) -> None:
    child = repair_module.CHILDREN[0]
    doc = _load_yaml(repair_module.NORMALIZED / child.path)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=child.record_id):
        repair_module.repair_child(child.path, doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    child = repair_module.CHILDREN[0]
    doc = _load_yaml(repair_module.NORMALIZED / child.path)
    doc["ingredients"][0]["preferred_term"] = "Peptone"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_child(child.path, doc)


def test_legacy_parent_migration_rejects_new_stock_topology(repair_module) -> None:
    doc = _load_yaml(repair_module.NORMALIZED / repair_module.PARENT)
    iron = doc["ingredients"].pop()
    doc["solutions"] = [{"preferred_term": "Iron stock", "composition": [iron]}]
    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_parent(doc)
