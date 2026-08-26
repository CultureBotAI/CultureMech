from __future__ import annotations

import importlib.util
import sys
from collections import Counter
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]


def load_migration():
    path = REPO / "scripts" / "resolve_composition_type_conflicts.py"
    spec = importlib.util.spec_from_file_location("resolve_composition_type_conflicts", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_reviewed_target_inventory_is_complete_and_unique() -> None:
    migration = load_migration()
    assert len(migration.TARGETS) == 46
    assert len({target.path for target in migration.TARGETS}) == 46
    assert Counter(target.composition_type for target in migration.TARGETS) == {
        "UNDEFINED": 40,
        "SEMI_DEFINED": 6,
    }


def test_repair_is_surgical_and_idempotent() -> None:
    migration = load_migration()
    target = next(row for row in migration.TARGETS if row.path == "bacterial/petrotoga_medium.yaml")
    text = (
        f"id: {target.record_id}\n"
        "name: petrotoga\n"
        "medium_type: DEFINED\n"
        "composition_type: DEFINED\n"
        "ingredients:\n"
        "- preferred_term: Yeast extract\n"
        "  concentration:\n"
        "    value: '0.197433'\n"
        "    unit: G_PER_L\n"
        "notes: 'composition_type: DEFINED remains prose'\n"
    )
    doc = yaml.safe_load(text)

    updated, changed = migration.plan_repair(doc, target, text)

    assert changed is True
    assert "medium_type: COMPLEX\n" in updated
    assert "composition_type: SEMI_DEFINED\n" in updated
    assert "notes: 'composition_type: DEFINED remains prose'" in updated
    assert migration.plan_repair(yaml.safe_load(updated), target, updated) == (updated, False)


def test_repair_refuses_identity_component_or_axis_drift() -> None:
    migration = load_migration()
    target = next(row for row in migration.TARGETS if row.path == "bacterial/petrotoga_medium.yaml")
    base = {
        "id": target.record_id,
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "ingredients": [
            {
                "preferred_term": "Yeast extract",
                "concentration": {"value": "0.197433", "unit": "G_PER_L"},
            }
        ],
    }
    text = yaml.safe_dump(base, sort_keys=False)

    wrong_id = dict(base, id="CultureMech:999999")
    with pytest.raises(ValueError, match="expected CultureMech"):
        migration.plan_repair(wrong_id, target, text)

    wrong_mass = yaml.safe_load(text)
    wrong_mass["ingredients"][0]["concentration"]["value"] = "0.2"
    with pytest.raises(ValueError, match="component signature drifted"):
        migration.plan_repair(wrong_mass, target, text)

    wrong_axis = dict(base, medium_type="COMPLEX")
    with pytest.raises(ValueError, match="unexpected type axes"):
        migration.plan_repair(wrong_axis, target, text)
