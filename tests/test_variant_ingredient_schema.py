"""Validate the public variant-change schema contract (#683, 2026-11-16).

Exercises both native LinkML and the tracked generated JSON schema, including
negative action/evidence cases and the generated dataclass consumer API.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

import jsonschema
import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml.validator.report import Severity

from culturemech.schema.culturemech_dataclasses import (
    IngredientDescriptor,
    MediaVariant,
    VariantIngredientChange,
)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "src/culturemech/schema/culturemech.yaml"


def change(action="ADD"):
    entry = {
        "action": action,
        "ingredient": {"preferred_term": "source ingredient"},
        "stage": "assay treatment",
        "source_modification_index": 0,
        "source_text": "Add source ingredient for the assay treatment.",
        "evidence": [
            {
                "reference": "https://example.org/recipe",
                "supports": "SUPPORT",
                "snippet": "Add source ingredient for the assay treatment.",
                "explanation": "The source specifies the ingredient and treatment stage.",
            }
        ],
    }
    if action == "REPLACE":
        entry["replaced_ingredient"] = {"preferred_term": "old ingredient"}
    if action == "SET_CONCENTRATION":
        entry["ingredient"]["concentration"] = {"value": "0", "unit": "NG_PER_L"}
    return entry


@pytest.fixture(scope="module", params=["native", "generated"])
def schema_errors(request):
    if request.param == "native":
        validator = Validator(
            schema=str(SCHEMA), validation_plugins=[JsonschemaValidationPlugin(closed=True)]
        )

        def errors(instance):
            return [
                r
                for r in validator.validate(
                    instance, target_class="VariantIngredientChange"
                ).results
                if r.severity == Severity.ERROR
            ]

    else:
        schema = json.loads(SCHEMA.with_name("culturemech.schema.json").read_text())
        schema["$ref"] = "#/$defs/VariantIngredientChange"
        # The generator also places the default root's properties at the top level.
        validator = jsonschema.validators.validator_for(schema)(
            {
                "$schema": schema["$schema"],
                "$defs": schema["$defs"],
                "$ref": schema["$ref"],
            }
        )

        def errors(instance):
            return list(validator.iter_errors(instance))

    return errors


@pytest.mark.parametrize("action", ["ADD", "REMOVE", "REPLACE", "SET_CONCENTRATION"])
def test_valid_action_with_unresolved_identity(schema_errors, action):
    assert not schema_errors(change(action))


@pytest.mark.parametrize(
    "field",
    [
        "action",
        "ingredient",
        "stage",
        "source_modification_index",
        "source_text",
        "evidence",
    ],
)
def test_provenance_and_claim_fields_are_required(schema_errors, field):
    entry = change()
    del entry[field]
    assert schema_errors(entry)


@pytest.mark.parametrize(
    "field,value",
    [
        ("stage", " \t"),
        ("source_text", ""),
        ("source_modification_index", -1),
        ("source_modification_index", True),
        ("action", "INFER"),
        ("evidence", []),
        ("ingredient", {"preferred_term": "  "}),
    ],
)
def test_invalid_values_fail_closed(schema_errors, field, value):
    entry = change()
    entry[field] = value
    assert schema_errors(entry)


def test_replacement_requires_old_descriptor_and_forbids_it_for_other_actions(schema_errors):
    entry = change("REPLACE")
    del entry["replaced_ingredient"]
    assert schema_errors(entry)
    for action in ("ADD", "REMOVE", "SET_CONCENTRATION"):
        entry = change(action)
        entry["replaced_ingredient"] = {"preferred_term": "old ingredient"}
        assert schema_errors(entry)


def test_set_concentration_requires_amount(schema_errors):
    entry = change("SET_CONCENTRATION")
    del entry["ingredient"]["concentration"]
    assert schema_errors(entry)


def test_evidence_must_include_support(schema_errors):
    entry = change()
    entry["evidence"][0]["supports"] = "PARTIAL"
    assert schema_errors(entry)
    entry["evidence"].append(change()["evidence"][0])
    assert not schema_errors(entry)


@pytest.mark.parametrize("unit", ["NG_PER_L", "MICROG_PER_ML", "NANOMOLAR", "PICOMOLAR", "PPM"])
def test_source_units_are_preserved_without_conversion(schema_errors, unit):
    entry = change("SET_CONCENTRATION")
    entry["ingredient"]["concentration"] = {"value": "4.5", "unit": unit}
    entry["ingredient"]["notes"] = "Source basis unspecified; no conversion asserted."
    before = copy.deepcopy(entry)
    assert not schema_errors(entry)
    assert entry == before


def test_generated_dataclasses_preserve_nested_change_fields():
    entry = change("REPLACE")
    variant = MediaVariant(
        name="assay variant", modifications=[entry["source_text"]], ingredient_changes=[entry]
    )
    assert isinstance(variant.ingredient_changes[0], VariantIngredientChange)
    assert isinstance(variant.ingredient_changes[0].ingredient, IngredientDescriptor)
    assert variant.ingredient_changes[0].source_modification_index == 0
    assert variant.ingredient_changes[0].source_text == entry["source_text"]
    assert variant.ingredient_changes[0].replaced_ingredient.preferred_term == "old ingredient"


@pytest.fixture(scope="module", params=["mapped", "unmapped"])
def summary_validator(request):
    kind = request.param
    validator = Validator(
        schema=str(SCHEMA.with_name(f"{kind}_ingredients_schema.yaml")),
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )
    target = "MappedRecipeOccurrence" if kind == "mapped" else "UnmappedRecipeOccurrence"

    def errors(instance):
        return [
            r
            for r in validator.validate(instance, target_class=target).results
            if r.severity == Severity.ERROR
        ]

    return errors, kind


def summary_row(kind):
    row = {
        "recipe_id": "CultureMech:999683",
        "recipe_label": "test variant source binding",
        "source_path": "test.yaml",
        "component_field": "ingredients",
        "component_index": 0,
        "preferred_term": "source ingredient",
        "resolution_source": "mim_exact" if kind == "mapped" else "not_found",
    }
    if kind == "mapped":
        row["resolved_identifier"] = "CHEBI:15377"
    return row


def test_summary_schema_accepts_base_and_scoped_positive_events(summary_validator):
    errors, kind = summary_validator
    row = summary_row(kind)
    assert not errors(row)
    row.update(
        {
            "component_field": "variants/0/ingredient_changes",
            "variant_index": 0,
            "variant_name": "assay variant",
            "change_index": 0,
            "change_action": "ADD",
            "change_stage": "assay treatment",
            "descriptor_role": "ingredient",
            "descriptor_path": "/variants/0/ingredient_changes/0/ingredient",
            "source_modification_index": 0,
            "source_text": change()["source_text"],
            "evidence_json": json.dumps(change()["evidence"]),
            "change_json": json.dumps(change()),
        }
    )
    assert not errors(row)
    row["change_action"] = "REMOVE"
    assert errors(row), "negative targets must not enter positive summary occurrences"
    row["change_action"] = "ADD"
    row["descriptor_role"] = "replaced_ingredient"
    assert errors(row)


def test_summary_schema_refuses_unqualified_variant_coordinates(summary_validator):
    errors, kind = summary_validator
    row = summary_row(kind)
    row["component_field"] = "variants/0/ingredient_changes"
    assert errors(row), "variant occurrence metadata cannot be silently dropped"
