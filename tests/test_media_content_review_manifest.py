"""Focused tests for the corpus-wide media content manifest."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def manifest():
    return _load("build_media_content_review_manifest")


INGREDIENT_KEYS = {
    "preferred_term",
    "term",
    "chebi_term",
    "mediaingredientmech_chebi_term",
    "concentration",
}
SOLUTION_KEYS = {
    "preferred_term",
    "term",
    "culturemech_term",
    "composition",
    "concentration",
    "concentration_candidates",
}
UNITS = {"G_PER_L", "VARIABLE"}


def _summarize(manifest, tmp_path: Path, doc: object):
    path = tmp_path / "data" / "normalized_yaml" / "bacterial" / "record.yaml"
    path.parent.mkdir(parents=True)
    path.write_text(yaml.safe_dump(doc, sort_keys=False))
    return manifest.summarize_record(
        path,
        UNITS,
        INGREDIENT_KEYS,
        tmp_path,
        expected_solution_keys=SOLUTION_KEYS,
    )


def _healthy_media() -> dict:
    return {
        "id": "CultureMech:000001",
        "name": "lb_medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "physical_state": "LIQUID",
        "ingredients": [
            {
                "preferred_term": "Glucose",
                "term": {"id": "CHEBI:17234"},
                "concentration": {"value": "1", "unit": "G_PER_L"},
            }
        ],
    }


def test_healthy_media_passes(manifest, tmp_path):
    row = _summarize(manifest, tmp_path, _healthy_media())

    assert row["record_kind"] == "MEDIA"
    assert row["missing_name"] == 0
    assert row["missing_composition"] == 0
    assert row["total_component_count"] == 1
    assert row["review_status"] == "PASS"
    assert row["issue_codes"] == ""


def test_missing_media_name_and_composition_are_blocking(manifest, tmp_path):
    doc = _healthy_media() | {"name": "", "ingredients": [], "solutions": []}
    row = _summarize(manifest, tmp_path, doc)

    assert row["missing_name"] == 1
    assert row["missing_composition"] == 1
    assert row["review_status"] == "BLOCKING"
    assert set(row["issue_codes"].split(";")) >= {
        "MISSING_MEDIA_NAME",
        "MISSING_MEDIA_COMPOSITION",
    }


def test_absent_and_variable_concentrations_are_separate_review_signals(manifest, tmp_path):
    doc = _healthy_media()
    doc["ingredients"] = [
        {"preferred_term": "HCl"},
        {
            "preferred_term": "Agar",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
        },
    ]
    row = _summarize(manifest, tmp_path, doc)

    assert row["missing_concentration_count"] == 1
    assert row["variable_concentration_count"] == 1
    assert row["unresolved_concentration_count"] == 2
    assert row["review_status"] == "NEEDS_REVIEW"
    assert set(row["issue_codes"].split(";")) == {
        "MISSING_CONCENTRATION",
        "VARIABLE_CONCENTRATION",
    }
    assert set(row["issue_locations"].split(";")) == {
        "MISSING_CONCENTRATION@ingredients[0].concentration",
        "VARIABLE_CONCENTRATION@ingredients[1].concentration",
    }


def test_component_without_required_name_is_blocking(manifest, tmp_path):
    doc = _healthy_media()
    doc["ingredients"] = [
        {
            "term": {"id": "CHEBI:17234"},
            "concentration": {"value": "1", "unit": "G_PER_L"},
        }
    ]
    row = _summarize(manifest, tmp_path, doc)

    assert row["missing_component_name_count"] == 1
    assert row["review_status"] == "BLOCKING"
    assert "MISSING_COMPONENT_NAME" in row["issue_codes"]
    assert row["issue_locations"] == ("MISSING_COMPONENT_NAME@ingredients[0].preferred_term")


def test_media_solution_is_a_component_with_its_own_working_concentration(manifest, tmp_path):
    doc = _healthy_media()
    doc["solutions"] = [
        {
            "preferred_term": "Trace-element stock",
            "composition": [
                {
                    "preferred_term": "ZnSO4",
                    "concentration": {"value": "1", "unit": "G_PER_L"},
                }
            ],
        }
    ]
    row = _summarize(manifest, tmp_path, doc)

    assert row["solution_count"] == 1
    assert row["solution_component_count"] == 1
    assert row["total_component_count"] == 3
    assert row["missing_concentration_count"] == 1
    assert row["missing_solution_concentration_count"] == 1
    assert row["missing_solution_concentration_with_candidates_count"] == 0
    assert row["missing_solution_concentration_without_candidates_count"] == 1
    assert row["issue_codes"] == "MISSING_SOLUTION_CONCENTRATION"
    assert row["issue_locations"] == ("MISSING_SOLUTION_CONCENTRATION@solutions[0].concentration")
    assert row["review_status"] == "NEEDS_REVIEW"


def test_missing_solution_concentration_tracks_non_asserted_candidates(manifest, tmp_path):
    doc = _healthy_media()
    doc["solutions"] = [
        {
            "preferred_term": "Vitamin stock",
            "concentration_candidates": [{"value": "1", "unit": "ML_PER_L"}],
        }
    ]
    row = _summarize(manifest, tmp_path, doc)

    assert row["solution_concentration_candidate_count"] == 1
    assert row["missing_solution_concentration_with_candidates_count"] == 1
    assert row["missing_solution_concentration_without_candidates_count"] == 0


def test_native_solution_uses_composition_and_ignores_placeholder_ingredients(manifest, tmp_path):
    doc = {
        "id": "CultureMech:000002",
        "preferred_term": "Trace element stock",
        "term": {"id": "mediadive.solution:2"},
        "composition": [
            {
                "preferred_term": "ZnSO4",
                "concentration": {"value": "1", "unit": "G_PER_L"},
            },
            {
                "preferred_term": "MnCl2",
                "concentration": {"value": "1", "unit": "G_PER_L"},
            },
        ],
        "ingredients": [
            {
                "preferred_term": "See source for composition",
                "concentration": {"value": "variable", "unit": "VARIABLE"},
            }
        ],
    }
    row = _summarize(manifest, tmp_path, doc)

    assert row["record_kind"] == "SOLUTION"
    assert row["record_shape"] == "SOLUTION_RECIPE"
    assert row["top_level_solution_component_count"] == 2
    assert row["total_component_count"] == 2
    assert row["variable_concentration_count"] == 0
    assert row["review_status"] == "PASS"


def test_empty_native_solution_composition_is_blocking(manifest, tmp_path):
    row = _summarize(
        manifest,
        tmp_path,
        {
            "id": "CultureMech:000004",
            "preferred_term": "Empty stock",
            "term": {"id": "mediadive.solution:4"},
            "composition": [],
        },
    )

    assert row["record_kind"] == "SOLUTION"
    assert row["missing_composition"] == 1
    assert row["issue_codes"] == "MISSING_SOLUTION_COMPOSITION"
    assert row["issue_locations"] == "MISSING_SOLUTION_COMPOSITION@composition"
    assert row["review_status"] == "BLOCKING"


def test_malformed_component_is_counted_and_located(manifest, tmp_path):
    doc = _healthy_media()
    doc["ingredients"] = ["not a mapping"]
    row = _summarize(manifest, tmp_path, doc)

    assert row["total_component_count"] == 1
    assert row["malformed_component_count"] == 1
    assert set(row["issue_codes"].split(";")) == {
        "MALFORMED_COMPONENT",
        "MISSING_MEDIA_COMPOSITION",
    }
    assert set(row["issue_locations"].split(";")) == {
        "MALFORMED_COMPONENT@ingredients[0]",
        "MISSING_MEDIA_COMPOSITION@ingredients|solutions",
    }


def test_curated_solution_stub_is_not_called_a_medium_without_ingredients(manifest, tmp_path):
    row = _summarize(
        manifest,
        tmp_path,
        {
            "id": "CultureMech:000003",
            "name": "trace_element_solution",
            "record_kind": "SOLUTION",
            "ingredients": [],
        },
    )

    assert row["record_kind"] == "SOLUTION"
    assert row["missing_composition"] == 0
    assert row["issue_codes"] == "SOLUTION_STUB"
    assert row["review_status"] == "NEEDS_REVIEW"


def test_schema_drives_the_expected_ingredient_keys(manifest):
    units, ingredient_keys, solution_keys = manifest.schema_review_config(
        REPO_ROOT / "src" / "culturemech" / "schema" / "culturemech.yaml"
    )

    assert "VARIABLE" in units
    assert {
        "chebi_term",
        "mediaingredientmech_chebi_term",
        "source",
        "synonyms",
    } <= ingredient_keys
    assert {"preferred_term", "composition", "concentration_candidates"} <= solution_keys


def test_variation_groups_exclude_solution_records(manifest):
    base = {
        "ingredient_identity_signature": "same",
        "ingredient_concentration_signature": "same-concentration",
        "total_component_count": 1,
        "embedded_variant_count": 0,
        "yaml_path": "data/normalized_yaml/bacterial/media.yaml",
        "record_kind": "MEDIA",
    }
    solution = base | {
        "yaml_path": "data/normalized_yaml/bacterial/solution.yaml",
        "record_kind": "SOLUTION",
    }

    assert manifest.build_groups([base, solution]) == []
