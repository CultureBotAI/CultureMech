"""Amount basis and quarantined-name boundaries for #683/#760 (2026-11-16)."""

import copy
import csv
import json
from dataclasses import replace
from pathlib import Path

import ingredient_occurrences as occurrence
import ingredient_release_bundle as bundle
import jsonschema
import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml.validator.report import Severity

from culturemech.validation.write_validated import validate_recipe


def recipe():
    source = "Set the water input to 950 mL per batch; final volume unspecified."
    uncertain = "A calcium chloride hydrate is reported for an unspecified assay."
    return {
        "id": "CultureMech:000001",
        "name": "Synthetic quantity/hold fixture",
        "physical_state": "LIQUID",
        "ingredients": [{"preferred_term": "water"}],
        "variants": [
            {
                "name": "Synthetic assay",
                "modifications": [source, uncertain],
                "ingredient_changes": [
                    {
                        "action": "SET_AMOUNT",
                        "ingredient": {"preferred_term": "water"},
                        "stage": "synthetic batch preparation",
                        "source_modification_index": 0,
                        "source_text": source,
                        "amount": {
                            "value": "950",
                            "unit": "ML",
                            "basis": "PER_BATCH",
                            "basis_statement": "Absolute input; final volume is unspecified.",
                        },
                        "evidence": [
                            {
                                "reference": "https://example.org/synthetic",
                                "supports": "SUPPORT",
                                "snippet": source,
                                "explanation": "Synthetic exact batch statement.",
                            }
                        ],
                    }
                ],
                "ingredient_mentions": [
                    {
                        "source_label": "calcium chloride hydrate",
                        "reported_action": "UNSPECIFIED",
                        "stage": "unspecified in source",
                        "source_modification_index": 1,
                        "source_text": uncertain,
                        "reason": "The chemical form and assay are not established.",
                        "held_fields": ["IDENTITY_FORM", "STAGE"],
                    }
                ],
            }
        ],
    }


@pytest.fixture(scope="module")
def schema_validator():
    source = Path(__file__).resolve().parents[1] / "src/culturemech/schema/culturemech.schema.json"
    schema = json.loads(source.read_text())
    return jsonschema.validators.validator_for(schema)(
        {
            "$schema": schema["$schema"],
            "$defs": schema["$defs"],
            "$ref": "#/$defs/VariantIngredientChange",
        }
    )


@pytest.mark.parametrize(
    "unit,basis,value",
    [
        ("ML", "PER_BATCH", "950"),
        ("G", "PER_BATCH", "1.5"),
        ("PERCENT", "UNSPECIFIED_PERCENT", "0.3"),
    ],
)
def test_literal_amount_is_valid_without_inventing_concentration(
    schema_validator, unit, basis, value
):
    record = recipe()
    change = record["variants"][0]["ingredient_changes"][0]
    change["amount"].update(unit=unit, basis=basis, value=value)
    before = copy.deepcopy(record)
    assert not list(schema_validator.iter_errors(change))
    assert not validate_recipe(record)
    assert record == before
    assert "concentration" not in change["ingredient"]


@pytest.mark.parametrize(
    "mutation",
    [
        "missing",
        "wrong_percent_basis",
        "wrong_mass_basis",
        "concentration",
        "remove",
        "unknown_unit",
        "blank_context",
    ],
)
def test_false_or_ambiguous_amount_basis_refuses(schema_validator, mutation):
    record = recipe()
    change = record["variants"][0]["ingredient_changes"][0]
    if mutation == "missing":
        del change["amount"]
    elif mutation == "wrong_percent_basis":
        change["amount"]["unit"] = "PERCENT"
    elif mutation == "wrong_mass_basis":
        change["amount"]["basis"] = "UNSPECIFIED_PERCENT"
    elif mutation == "concentration":
        change["ingredient"]["concentration"] = {"value": "950", "unit": "ML_PER_L"}
    elif mutation == "remove":
        change["action"] = "REMOVE"
    elif mutation == "unknown_unit":
        change["amount"]["unit"] = "ML_PER_L"
    else:
        change["amount"]["basis_statement"] = " "
    assert list(schema_validator.iter_errors(change))
    assert validate_recipe(record)


@pytest.mark.parametrize(
    "mutation",
    ["invented_label", "changed_source", "identity", "presence", "negative_index", "duplicate"],
)
def test_held_names_cannot_invent_or_promote_assertions(mutation):
    record = recipe()
    mentions = record["variants"][0]["ingredient_mentions"]
    mention = mentions[0]
    if mutation == "invented_label":
        mention["source_label"] = "calcium chloride dihydrate"
    elif mutation == "changed_source":
        mention["source_text"] += " changed"
    elif mutation == "identity":
        mention["term"] = {"id": "CHEBI:3312"}
    elif mutation == "presence":
        mention["counts_as_presence"] = True
    elif mutation == "negative_index":
        mention["source_modification_index"] = -1
    else:
        mentions.append(copy.deepcopy(mention))
    assert validate_recipe(record)


def test_native_bundle_keeps_literal_amount_and_unresolved_name_separate(tmp_path):
    inputs = tmp_path / "input"
    inputs.mkdir()
    (inputs / "recipe.yaml").write_text(yaml.safe_dump(recipe(), sort_keys=False))
    scanned = occurrence.scan_ingredient_occurrences(inputs)
    assert not scanned.errors
    assert len(scanned.occurrences) == 2
    assert len(scanned.variant_mentions) == 1
    row = scanned.occurrences[1]
    assert row.change_action == "SET_AMOUNT"
    assert row.concentration_value == row.concentration_unit == ""
    assert json.loads(row.change_json)["amount"]["value"] == "950"
    assert all(row.preferred_term == "water" for row in scanned.occurrences)
    output = tmp_path / "bundle"
    manifest = bundle.build(inputs, output)
    assert manifest["contract"] == "culturemech-direct-ingredients-v3"
    assert manifest["counts"]["variant_held_mentions"] == 1
    assert manifest["counts"]["variant_changes_by_action"] == {"SET_AMOUNT": 1}
    assert bundle.verify(output, inputs)["status"] == "VERIFIED_CANDIDATE"
    path = output / "variant_ingredient_holds.tsv"
    with path.open(newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        fields, rows = reader.fieldnames, list(reader)
    rows[0]["counts_as_presence"] = "true"
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(bundle.BundleError, match="withheld"):
        bundle.verify(output, inputs)


@pytest.mark.parametrize("mapped", [True, False])
def test_amount_event_validates_in_native_summary_schema(tmp_path, mapped):
    inputs = tmp_path / "inputs"
    inputs.mkdir()
    (inputs / "recipe.yaml").write_text(yaml.safe_dump(recipe(), sort_keys=False))
    row = occurrence.scan_ingredient_occurrences(inputs).occurrences[1]
    if mapped:
        row = replace(row, resolved_identifier="CHEBI:15377")
        builder, schema_name, target = (
            occurrence.build_mapped_output,
            "mapped",
            "MappedIngredientsCollection",
        )
    else:
        row = replace(row, resolved_identifier="", resolution_source="not_found")
        builder, schema_name, target = (
            occurrence.build_unmapped_output,
            "unmapped",
            "UnmappedIngredientsCollection",
        )
    output = builder([row])
    schema = (
        Path(__file__).resolve().parents[1]
        / f"src/culturemech/schema/{schema_name}_ingredients_schema.yaml"
    )
    report = Validator(
        schema=str(schema), validation_plugins=[JsonschemaValidationPlugin(closed=True)]
    ).validate(output, target_class=target)
    assert not [item for item in report.results if item.severity == Severity.ERROR]
    entries = output[f"{schema_name}_ingredients"]
    assert len(entries) == 1
    assert entries[0]["recipe_occurrences"][0]["change_action"] == "SET_AMOUNT"
