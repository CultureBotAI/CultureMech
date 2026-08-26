"""Regression tests for the source-grounded CCAP instruction migration."""

from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def migration():
    name = "repair_ccap_instruction_rows"
    spec = importlib.util.spec_from_file_location(name, REPO / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def test_target_paths_are_unique_and_cover_the_reviewed_batch(migration):
    targets = (*migration.SIMPLE_TARGETS, *migration.REBUILD_TARGETS)
    paths = [target.path for target in targets]

    assert len(paths) == 45
    assert len(paths) == len(set(paths))


def test_simple_repair_is_guarded_and_idempotent(migration):
    target = migration.SimpleTarget(
        path="algae/example.yaml",
        record_id="CultureMech:000001",
        source="MR_example.pdf",
        rows=(migration.row("For agar, add", "15", "G_PER_L"),),
        replacements=(migration.IngredientSpec(
            "Water", "1", "L", "Source component.", "CHEBI:15377", "water", True
        ),),
        steps=(migration.add_agar(),),
    )
    doc = {
        "id": "CultureMech:000001",
        "ingredients": [{
            "preferred_term": "For agar, add",
            "concentration": {"value": "15", "unit": "G_PER_L"},
        }],
        "curation_history": [],
    }

    repaired, changed = migration.repair_simple(doc, target)

    assert changed is True
    assert repaired["ingredients"][0]["preferred_term"] == "Water"
    assert repaired["preparation_steps"][0]["action"] == "ADD_AGAR"
    assert repaired["curation_history"][-1]["action"] == migration.ACTION
    assert migration.repair_simple(repaired, target)[1] is False

    wrong = copy.deepcopy(doc)
    wrong["ingredients"][0]["concentration"]["value"] = "12"
    with pytest.raises(ValueError, match="expected one"):
        migration.repair_simple(wrong, target)


def test_composite_repair_restores_constituent_media(migration):
    target = migration.RebuildTarget(
        path="algae/mix.yaml",
        record_id="CultureMech:000002",
        source="MR_mix.pdf",
        current_rows=(migration.row("Soil is prepared as above.", "105", "G_PER_L"),),
        ingredients=(),
        solutions=(migration.SolutionSpec(
            "Base medium", "500", "ML_PER_L", "CultureMech:000003", "Base",
            "One half of the mixture.",
        ),),
        steps=(migration.step("MIX", "Mix constituent media."),),
    )
    doc = {
        "id": "CultureMech:000002",
        "ingredients": [{
            "preferred_term": "Soil is prepared as above.",
            "concentration": {"value": "105", "unit": "G_PER_L"},
        }],
        "curation_history": [],
    }

    repaired, changed = migration.repair_rebuild(doc, target)

    assert changed is True
    assert repaired["ingredients"] == []
    assert repaired["solutions"][0]["culturemech_term"]["id"] == "CultureMech:000003"
    assert repaired["solutions"][0]["concentration"]["unit"] == "ML_PER_L"
    assert migration.repair_rebuild(repaired, target)[1] is False
