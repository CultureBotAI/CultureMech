from __future__ import annotations

import copy
import importlib
import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
MediaDiveImporter = importlib.import_module(
    "culturemech.import.mediadive_importer"
).MediaDiveImporter


def load_migration():
    path = REPO / "scripts" / "repair_mediadive_jcm_structure.py"
    spec = importlib.util.spec_from_file_location("repair_mediadive_jcm_structure", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def importer_for(payload: dict) -> MediaDiveImporter:
    importer = MediaDiveImporter.__new__(MediaDiveImporter)
    importer.mediadive_dir = REPO / "tests" / "fixtures" / "missing" / "mediadive"
    importer.ingredients_by_name = {}
    importer._api_data_cache = {"data": [payload]}
    return importer


def small_payload() -> dict:
    return {
        "medium": {"id": "J1", "name": "TEST"},
        "solutions": [
            {
                "id": 1,
                "name": "Main sol. J1",
                "recipe": [
                    {
                        "compound": "Salt",
                        "compound_id": 1,
                        "amount": 2,
                        "unit": "g",
                        "g_l": 2.0,
                    },
                    {
                        "solution": "Trace stock",
                        "solution_id": 99,
                        "amount": 3,
                        "unit": "ml",
                    },
                ],
            },
            {
                "id": 99,
                "name": "Trace stock",
                "recipe": [
                    {
                        "compound": "Trace metal",
                        "compound_id": 2,
                        "amount": 4,
                        "unit": "g",
                        "g_l": 4.0,
                    }
                ],
            },
        ],
    }


def test_importer_keeps_stock_contents_out_of_final_ingredients():
    importer = importer_for(small_payload())

    ingredients = importer._parse_api_composition("J1")
    solutions = importer._parse_api_solutions("J1")

    assert [row["preferred_term"] for row in ingredients] == ["Salt"]
    assert [row["preferred_term"] for row in solutions] == ["Trace stock"]
    assert solutions[0]["term"]["id"] == "mediadive.solution:99"
    assert solutions[0]["concentration"] == {"value": "3", "unit": "ML_PER_L"}


@pytest.mark.parametrize(
    ("attribute", "expected"),
    [
        (
            "w/v) Yeast extract (BD-Difco, 10%",
            "10% (w/v) Yeast extract (BD-Difco) solution",
        ),
        (
            "w/v) Trypticase peptone (BD-BBL, 10%",
            "10% (w/v) Trypticase peptone (BD-BBL) solution",
        ),
        ("w/v) MES (pH 6.0, 20%", "20% (w/v) MES (pH 6.0) solution"),
    ],
)
def test_recovers_the_three_empty_mediadive_stock_labels(attribute: str, expected: str):
    item = {"compound": "", "compound_id": 1944, "attribute": attribute}
    assert MediaDiveImporter._api_stock_name(item) == expected


def test_migration_is_guarded_and_idempotent(monkeypatch):
    migration = load_migration()
    target = migration.Target(
        path="bacterial/test.yaml",
        direct_ingredients=("Salt",),
        solutions=(("Trace stock", "3", "mediadive.solution:99"),),
        merged_blank_value="7",
    )
    monkeypatch.setitem(migration.TARGETS, "J1", target)
    doc = {
        "media_term": {"term": {"id": "mediadive.medium:J1"}},
        "ingredients": [
            {"preferred_term": "Salt", "concentration": {"value": "2", "unit": "G_PER_L"}},
            {"preferred_term": "", "concentration": {"value": "7", "unit": "G_PER_L"}},
            {
                "preferred_term": "Trace metal",
                "concentration": {"value": "4", "unit": "G_PER_L"},
            },
        ],
        "curation_history": [],
    }

    repaired, changed = migration.repair_document(doc, small_payload(), "J1")

    assert changed is True
    assert [row["preferred_term"] for row in repaired["ingredients"]] == ["Salt"]
    assert [row["preferred_term"] for row in repaired["solutions"]] == ["Trace stock"]
    assert repaired["curation_history"][-1]["action"] == "RESTORED_STOCK_SOLUTION_BOUNDARIES"
    assert migration.repair_document(repaired, small_payload(), "J1")[1] is False

    wrong = copy.deepcopy(doc)
    wrong["ingredients"][1]["concentration"]["value"] = "8"
    with pytest.raises(ValueError, match="expected merged blank value 7"):
        migration.repair_document(wrong, small_payload(), "J1")
