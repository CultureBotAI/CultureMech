"""Independent delta comparison falsification with synthetic CSV artifacts."""

import copy
import csv
import importlib.util
import json
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location(
    "compare_variant_inventory_683",
    Path(__file__).resolve().parents[1] / "scripts/adhoc/compare_variant_inventory_683.py",
)
comparison = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(comparison)


@pytest.fixture
def tables(tmp_path):
    base = {
        "recipe_id": "CultureMech:000001",
        "component_field": "ingredients",
        "component_index": "0",
        "preferred_term": "base",
        "resolved_identifier": "CHEBI:15377",
        "resolution_source": "mim_exact",
        "mim_mapping_status": "MAPPED",
        "mim_ambiguity": "",
        "ingredient_json": json.dumps({"notes": 'Synthetic "quoted"\tnote\n' + "x" * 140000}),
    }
    current_base = {**base, **dict.fromkeys(comparison.VARIANT_FIELDS, "")}
    positive = {
        **current_base,
        "component_field": "variants/0/ingredient_changes",
        "preferred_term": "new synthetic label",
        "resolved_identifier": "",
        "resolution_source": "not_found",
        "mim_mapping_status": "",
        "change_action": "ADD",
        "descriptor_role": "ingredient",
        "descriptor_path": "/variants/0/ingredient_changes/0/ingredient",
    }
    old_path = tmp_path / "baseline.tsv"
    new_path = tmp_path / "candidate.tsv"
    comparison.write_tsv(old_path, list(base), [base])
    comparison.write_tsv(new_path, list(current_base), [current_base, positive])
    return old_path, new_path, base, current_base, positive


def rewrite(path, records):
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(records)


def test_all_base_columns_and_large_quoted_fields_survive_new_events(tables):
    old, new, _base, _current, positive = tables
    limit = csv.field_size_limit()
    state = comparison.compare_occurrences(old, new)
    assert state["base_rows"] == 1
    assert state["variant_rows"] == [positive]
    assert sum(state["candidate_groups"].values()) == 2
    assert len(state["candidate_groups"]) - len(state["baseline_groups"]) == 1
    assert csv.field_size_limit() == limit


@pytest.mark.parametrize("fault", ["descriptor", "missing", "context"])
def test_equal_counts_or_identities_cannot_hide_original_row_drift(tables, fault):
    old, new, _base, current, positive = tables
    current = copy.deepcopy(current)
    if fault == "descriptor":
        current["ingredient_json"] = json.dumps({"concentration": {"value": "999"}})
    elif fault == "context":
        current["change_stage"] = "Unexpected base scope"
    rewrite(new, [positive] if fault == "missing" else [current, positive])
    with pytest.raises(ValueError, match="base"):
        comparison.compare_occurrences(old, new)


def test_unresolved_removed_labels_are_visible_without_positive_promotion(tables, tmp_path):
    old, new, _base, _current, positive = tables
    state = comparison.compare_occurrences(old, new)
    removed = {
        **positive,
        "component_index": "1",
        "preferred_term": "removed-only synthetic label",
        "change_action": "REMOVE",
        "descriptor_path": "/variants/0/ingredient_changes/1/ingredient",
        "counts_as_presence": "false",
    }
    ledger = tmp_path / "ledger.tsv"
    comparison.write_tsv(
        ledger, list(removed), [{**positive, "counts_as_presence": "true"}, removed]
    )
    unresolved, counts = comparison.context_rows(ledger, state)
    assert counts["variant_change_events"] == 2
    assert counts["variant_positive_occurrences"] == 1
    assert counts["variant_context_only_mentions"] == 1
    assert unresolved[0]["preferred_term"] == "removed-only synthetic label"
    assert unresolved[0]["label_in_positive_inventory"] == "false"
    assert unresolved[0]["label_in_baseline_inventory"] == "false"
    assert "removed-only synthetic label" not in state["candidate_labels"]
    rewrite(ledger, [removed])
    with pytest.raises(ValueError, match="occurrence/ledger"):
        comparison.context_rows(ledger, state)


def test_product_mutation_does_not_pass_original_manifest_pin(tmp_path):
    product = tmp_path / "occurrences.tsv"
    product.write_text("synthetic original\n")
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps({"products": {product.name: comparison.fingerprint(product)}}))
    pin = comparison.fingerprint(manifest)["sha256"]
    comparison.pinned_bundle(tmp_path, pin)
    product.write_text("changed product; manifest untouched\n")
    with pytest.raises(ValueError, match="product differs"):
        comparison.pinned_bundle(tmp_path, pin)
