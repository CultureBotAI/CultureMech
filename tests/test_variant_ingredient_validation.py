"""Source, stage and writer-boundary guards for variant changes (#683, 2026-11-16)."""

from __future__ import annotations

import copy

import pytest
import yaml

from culturemech.validation.variant_ingredients import (
    validate_recipe_variant_ingredients,
    variant_ingredient_validation_results,
)
from culturemech.validation.write_validated import validate_recipe
from scripts.validate_strict import validate_one
from tests.test_variant_ingredient_schema import change


def recipe(action="ADD"):
    entry = change(action)
    return {
        "id": "CultureMech:999683",
        "name": "test variant source binding",
        "medium_type": "DEFINED",
        "physical_state": "LIQUID",
        "ingredients": [{"preferred_term": "water"}],
        "variants": [
            {
                "name": "assay variant",
                "modifications": [entry["source_text"]],
                "ingredient_changes": [entry],
            }
        ],
    }


def entry(record):
    return record["variants"][0]["ingredient_changes"][0]


def categories(record):
    return {issue.category for issue in validate_recipe_variant_ingredients(record)}


@pytest.mark.parametrize("action", ["ADD", "REMOVE", "REPLACE", "SET_CONCENTRATION"])
def test_valid_changes_and_zero_dose_are_not_mutated(action):
    record = recipe(action)
    before = copy.deepcopy(record)
    assert not validate_recipe_variant_ingredients(record)
    assert not validate_recipe(record)
    assert record == before


def test_legacy_prose_and_unspecified_parent_relationship_remain_valid():
    record = recipe()
    del record["variants"][0]["ingredient_changes"]
    assert not validate_recipe_variant_ingredients(record)
    assert not validate_recipe(record)


@pytest.mark.parametrize("index", [-1, True, "0", 1, None])
def test_bad_source_coordinates_are_rejected(index):
    record = recipe()
    entry(record)["source_modification_index"] = index
    assert "variant_source_index" in categories(record)


def test_source_text_binding_rejects_even_whitespace_drift():
    record = recipe()
    record["variants"][0]["modifications"][0] += " "
    assert "variant_source_text" in categories(record)


def test_reordered_modifications_need_updated_binding():
    record = recipe()
    record["variants"][0]["modifications"].insert(0, "A different preparation stage.")
    assert "variant_source_text" in categories(record)
    entry(record)["source_modification_index"] = 1
    assert not categories(record)


@pytest.mark.parametrize("action", ["ADD", "REMOVE", "REPLACE", "SET_CONCENTRATION"])
@pytest.mark.parametrize(
    "relationship",
    ["SUPPLEMENTED_VARIANT", "OMITTED_COMPONENT_VARIANT", "CONCENTRATION_VARIANT"],
)
def test_recipe_relationship_does_not_infer_stage_event_action(relationship, action):
    record = recipe(action)
    record["variants"][0]["relationship"] = relationship
    before = copy.deepcopy(record)
    assert not categories(record)
    assert not validate_recipe(record)
    assert record == before


@pytest.mark.parametrize("action", ["ADD", "REMOVE", "REPLACE", "SET_CONCENTRATION"])
def test_source_duplicate_cannot_carry_ingredient_changes(action):
    record = recipe(action)
    record["variants"][0]["relationship"] = "SOURCE_DUPLICATE"
    assert "variant_relationship" in categories(record)


def test_added_dose_under_concentration_relationship_does_not_become_a_total():
    """An explicit addition must not be relabelled SET_CONCENTRATION (#768)."""
    record = recipe()
    variant = record["variants"][0]
    variant["relationship"] = "CONCENTRATION_VARIANT"
    source = "Supplement the base medium with sodium selenite at 1 nM."
    variant["modifications"] = [source]
    item = entry(record)
    item["source_text"] = source
    item["stage"] = "supplemental dose to the source-defined base medium"
    item["ingredient"] = {
        "preferred_term": "Sodium selenite",
        "concentration": {"value": "1", "unit": "NANOMOLAR"},
    }
    item["evidence"][0]["snippet"] = source
    before = copy.deepcopy(record)
    assert not validate_recipe(record)
    assert record == before
    assert item["action"] == "ADD"
    item["ingredient"]["modifier"] = "ABSENT"
    assert "variant_presence" in categories(record)


@pytest.mark.parametrize("relationship", ["SUPPLEMENTED_VARIANT", "OMITTED_COMPONENT_VARIANT"])
def test_mixed_stage_events_retain_individual_invariants(relationship):
    record = recipe()
    variant = record["variants"][0]
    variant["relationship"] = relationship
    changes = [change(action) for action in ("ADD", "REMOVE", "REPLACE", "SET_CONCENTRATION")]
    variant["modifications"] = [item["source_text"] for item in changes]
    for index, item in enumerate(changes):
        item["source_modification_index"] = index
        item["stage"] = f"source-defined preparation stage {index}"
    variant["ingredient_changes"] = changes
    assert not validate_recipe(record)
    del changes[2]["replaced_ingredient"]
    assert "variant_replacement" in categories(record)
    changes[2]["replaced_ingredient"] = {"preferred_term": "old source ingredient"}
    del changes[3]["ingredient"]["concentration"]
    assert "variant_concentration" in categories(record)


def test_substituted_formulation_allows_alternative_inputs_and_individual_changes():
    """A recipe substitution need not be fifteen invented 1:1 replacements (#761)."""
    record = recipe()
    variant = record["variants"][0]
    variant["relationship"] = "SUBSTITUTED_COMPONENT_VARIANT"
    names = [
        "Ammonium sulfate",
        "Potassium dihydrogen phosphate",
        "Disodium phosphate",
        "Sodium citrate",
        "Magnesium sulfate",
        "Calcium chloride",
        "Zinc sulfate",
        "Copper sulfate",
        "Ferric ammonium citrate",
        "L-Glutamate",
        "Pyridoxine",
        "Biotin",
        "Glycerol",
        "Bovine serum albumin",
        "Water",
    ]
    changes = []
    for name in names:
        item = change("ADD")
        item["ingredient"] = {"preferred_term": name}
        item["stage"] = "alternative from-scratch preparation"
        changes.append(item)
    isotope = change("REPLACE")
    isotope["ingredient"] = {"preferred_term": "[3-13C] sodium L-lactate"}
    isotope["replaced_ingredient"] = {"preferred_term": "Sodium L-lactate"}
    changes.append(isotope)
    glucose = change("SET_CONCENTRATION")
    glucose["ingredient"] = {
        "preferred_term": "Glucose",
        "concentration": {"value": "5", "unit": "G_PER_L"},
    }
    changes.append(glucose)
    variant["ingredient_changes"] = changes
    assert not categories(record)
    assert not validate_recipe(record)
    del isotope["replaced_ingredient"]
    assert "variant_replacement" in categories(record)
    isotope["replaced_ingredient"] = {"preferred_term": "Sodium L-lactate"}
    changes[0]["ingredient"]["modifier"] = "ABSENT"
    assert "variant_presence" in categories(record)


@pytest.mark.parametrize("field", ["reference", "snippet", "explanation"])
def test_evidence_requires_source_quote_and_claim_context(field):
    record = recipe()
    entry(record)["evidence"][0][field] = "  "
    assert "variant_evidence" in categories(record)


def test_partial_evidence_alone_does_not_approve_a_change():
    record = recipe()
    entry(record)["evidence"][0]["supports"] = "PARTIAL"
    assert "variant_evidence" in categories(record)


def test_duplicate_evidence_references_are_rejected():
    record = recipe()
    entry(record)["evidence"] *= 2
    assert "variant_evidence" in categories(record)


def test_absent_modifier_cannot_be_a_positive_occurrence():
    record = recipe()
    entry(record)["ingredient"]["modifier"] = "ABSENT"
    assert "variant_presence" in categories(record)
    entry(record)["action"] = "REMOVE"
    assert not categories(record)


def test_duplicate_changes_fail_but_distinct_doses_remain_separate():
    record = recipe("SET_CONCENTRATION")
    changes = record["variants"][0]["ingredient_changes"]
    changes.append(copy.deepcopy(changes[0]))
    assert "duplicate_variant_change" in categories(record)
    changes[1]["ingredient"]["concentration"]["value"] = "0.25"
    assert not categories(record)


@pytest.mark.parametrize("bad", [None, "text", [], 3])
def test_malformed_entries_report_without_crashing(bad):
    record = recipe()
    record["variants"][0]["ingredient_changes"] = [bad]
    assert "variant_change_type" in categories(record)


def test_both_write_and_strict_validation_enforce_source_binding(tmp_path):
    record = recipe()
    entry(record)["source_text"] += " changed"
    results = variant_ingredient_validation_results(record)
    assert results and results[0].type == "variant_ingredients"
    assert results[0].context == ["variants[0].ingredient_changes[0].source_text"]
    assert any(result.type == "variant_ingredients" for result in validate_recipe(record))
    path = tmp_path / "recipe.yaml"
    path.write_text(yaml.safe_dump(record), encoding="utf-8")
    rows = validate_one(path)
    assert any(
        row["layer"] == "variant_ingredients" and row["category"] == "variant_source_text"
        for row in rows
    )
