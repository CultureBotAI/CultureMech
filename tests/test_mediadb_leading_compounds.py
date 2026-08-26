"""Regression tests for the corrupted leading MediaDB compound rows."""

from __future__ import annotations

import importlib
import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))


@pytest.fixture(scope="module")
def importer_module():
    return importlib.import_module("culturemech.import.mediadb_importer")


@pytest.fixture(scope="module")
def migration_module():
    name = "fix_mediadb_leading_compounds"
    spec = importlib.util.spec_from_file_location(name, REPO / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def test_importer_restores_corrupt_atp_and_nad_rows(importer_module, tmp_path):
    data = tmp_path / "raw"
    data.mkdir()
    (data / "mediadb_media.json").write_text('{"data": []}')
    (data / "mediadb_compounds.json").write_text(
        '{"data": ['
        '{"id": "2", "name": "4-di-O-methyl-alpha-L-fucoside", "chebi_id": ""},'
        '{"id": "3", "name": "4-dimethoxyphenyl", "chebi_id": ""}'
        "]}"
    )
    (data / "mediadb_organisms.json").write_text('{"data": []}')
    importer = importer_module.MediaDBImporter(data, tmp_path / "out")

    ingredients = importer._map_ingredients(
        {
            "composition": [
                {"compound_id": "2", "concentration": 1.25, "unit": "mM"},
                {"compound_id": "3", "concentration": 0.00603, "unit": "mM"},
            ]
        }
    )

    assert ingredients[0]["preferred_term"] == "ATP"
    assert ingredients[0]["term"] == {"id": "CHEBI:15422", "label": "ATP"}
    assert "KEGG.COMPOUND:C00002" in ingredients[0]["notes"]
    assert ingredients[1]["preferred_term"] == "NAD+"
    assert ingredients[1]["term"] == {"id": "CHEBI:15846", "label": "NAD(+)"}


def test_migration_is_guarded_and_idempotent(migration_module):
    doc = {
        "media_term": {"term": {"id": "MEDIADB:46"}},
        "ingredients": [
            {
                "preferred_term": "",
                "concentration": {"value": "1.25", "unit": "MILLIMOLAR"},
            }
        ],
        "curation_history": [],
    }

    changed, _ = migration_module.apply_correction(doc)
    assert changed
    assert doc["ingredients"][0]["preferred_term"] == "ATP"
    assert doc["ingredients"][0]["term"]["id"] == "CHEBI:15422"
    assert len(doc["curation_history"]) == 1

    changed, reason = migration_module.apply_correction(doc)
    assert not changed
    assert reason == "already named"
    assert len(doc["curation_history"]) == 1


def test_migration_rejects_unexpected_concentration(migration_module):
    doc = {
        "media_term": {"term": {"id": "MEDIADB:279"}},
        "ingredients": [
            {
                "preferred_term": "",
                "concentration": {"value": "1", "unit": "MILLIMOLAR"},
            }
        ],
    }

    with pytest.raises(ValueError, match="expected 0.00603 MILLIMOLAR"):
        migration_module.apply_correction(doc)
