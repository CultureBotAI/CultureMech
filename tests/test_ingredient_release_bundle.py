"""Candidate-bundle provenance and failure boundaries, using tiny native corpora."""

from __future__ import annotations

import json
import shutil

import ingredient_release_bundle as bundle
import pytest
import yaml


@pytest.fixture
def inputs(tmp_path):
    root = tmp_path / "inputs"
    (root / "bacterial").mkdir(parents=True)
    (root / ".hidden").mkdir()
    medium = {
        "id": "CultureMech:000001",
        "name": "Bundle fixture",
        "physical_state": "LIQUID",
        "category": "bacterial",
        "ingredients": [
            {"preferred_term": "water", "term": {"id": "CHEBI:15377"}},
            {"preferred_term": "fixture unknown\nmaterial\twith quoted cells"},
        ],
        "solutions": [
            {
                "preferred_term": "inline stock",
                "composition": [{"preferred_term": "water", "term": {"id": "CHEBI:15377"}}],
            }
        ],
    }
    (root / "bacterial" / "medium.yaml").write_text(yaml.safe_dump(medium), encoding="utf-8")
    empty = {
        "id": "CultureMech:000002",
        "name": "Zero direct ingredients",
        "physical_state": "LIQUID",
        "ingredients": [],
    }
    (root / ".hidden" / "zero.yaml").write_text(yaml.safe_dump(empty), encoding="utf-8")
    return root


@pytest.fixture
def candidate(inputs, tmp_path):
    output = tmp_path / "candidate"
    manifest = bundle.build(inputs, output)
    return output, manifest


def test_native_bundle_counts_quoted_cells_hidden_and_zero_records(inputs, candidate):
    output, manifest = candidate
    counts = manifest["counts"]
    assert counts["scanned_records"] == 2
    assert counts["records_with_occurrences"] == 1
    assert counts["records_without_direct_occurrences"] == 1
    assert counts["occurrences"] == 3
    assert counts["mapped_occurrences"] == 2
    assert counts["unresolved_occurrences"] == 1
    assert counts["ingredient_groups"] == 2
    assert counts["groups_by_status"] == {"MAPPED": 1, "UNMAPPED": 1}
    assert ".hidden/zero.yaml" in manifest["inputs"]
    assert manifest["scope"] == "subset"
    assert manifest["integrated_release"] is False
    assert len(manifest["mim_label_index"]["source_commit"]) == 40
    assert bundle.verify(output, inputs)["status"] == "VERIFIED_CANDIDATE"


def test_repeated_native_generation_has_identical_products(inputs, candidate, tmp_path):
    _, first = candidate
    second = bundle.build(inputs, tmp_path / "second")
    assert second["products"] == first["products"]
    assert second["inputs"] == first["inputs"]
    assert second["counts"] == first["counts"]


@pytest.mark.parametrize("change", ["added", "removed", "changed"])
def test_input_membership_and_content_drift_fail(inputs, candidate, change):
    output, _ = candidate
    if change == "added":
        (inputs / "new.yaml").write_text("id: another\n", encoding="utf-8")
    elif change == "removed":
        (inputs / ".hidden" / "zero.yaml").unlink()
    else:
        path = inputs / ".hidden" / "zero.yaml"
        path.write_text(path.read_text() + "# changed input\n", encoding="utf-8")
    with pytest.raises(bundle.BundleError, match="Input membership or content"):
        bundle.verify(output, inputs)


@pytest.mark.parametrize("product", ["mapped_ingredients.yaml", "ingredients_list.tsv"])
def test_artifact_edits_are_rejected(inputs, candidate, product):
    output, _ = candidate
    path = output / product
    path.write_text(path.read_text() + "\n", encoding="utf-8")
    with pytest.raises(bundle.BundleError, match="artifacts or accounting"):
        bundle.verify(output, inputs)


def test_native_invalid_input_leaves_error_evidence_without_candidate(inputs, tmp_path):
    (inputs / "invalid.yaml").write_text("not: [valid\n", encoding="utf-8")
    output = tmp_path / "invalid-output"
    with pytest.raises(bundle.BundleError, match="Native ingredient aggregation failed"):
        bundle.build(inputs, output)
    assert not output.exists()
    stages = list(tmp_path.glob(".invalid-output.incomplete-*"))
    assert len(stages) == 1
    assert not (stages[0] / "manifest.json").exists()
    assert list(bundle._rows(stages[0] / "ingredient_aggregation_errors.tsv"))


def test_input_change_during_generation_never_publishes(inputs, tmp_path, monkeypatch):
    native = bundle._aggregate

    def changing_source(input_dir, stage):
        result = native(input_dir, stage)
        (input_dir / "new.yaml").write_text("new: record\n", encoding="utf-8")
        return result

    monkeypatch.setattr(bundle, "_aggregate", changing_source)
    output = tmp_path / "drifting-output"
    with pytest.raises(bundle.BundleError, match="changed during aggregation"):
        bundle.build(inputs, output)
    assert not output.exists()


def test_plan_does_not_aggregate_or_create_output(inputs, tmp_path, monkeypatch):
    def forbidden(*args):
        pytest.fail("plan must not run aggregation")

    monkeypatch.setattr(bundle, "_aggregate", forbidden)
    output = tmp_path / "plan-output"
    plan = bundle.build(inputs, output, plan=True)
    assert plan["scanned_records"] == 2
    assert plan["status"] == "PLAN_ONLY"
    assert not output.exists()
    assert bundle.main(["build", "--input-dir", str(inputs), "--plan"]) == 0


def test_late_input_change_during_accounting_never_publishes(inputs, tmp_path, monkeypatch):
    accounting = bundle.artifact_accounting

    def changing_source(directory, corpus):
        result = accounting(directory, corpus)
        (inputs / "late.yaml").write_text("new: record\n", encoding="utf-8")
        return result

    monkeypatch.setattr(bundle, "artifact_accounting", changing_source)
    output = tmp_path / "late-drift"
    with pytest.raises(bundle.BundleError, match="changed during artifact accounting"):
        bundle.build(inputs, output)
    assert not output.exists()


def test_source_change_during_verification_is_detected(inputs, candidate, monkeypatch):
    output, _ = candidate
    inventory = bundle.product_inventory

    def changing_source(directory, counts):
        result = inventory(directory, counts)
        (inputs / "late.yaml").write_text("new: record\n", encoding="utf-8")
        return result

    monkeypatch.setattr(bundle, "product_inventory", changing_source)
    with pytest.raises(bundle.BundleError, match="changed during verification"):
        bundle.verify(output, inputs)


def test_subset_cannot_claim_full_catalog(inputs, candidate):
    output, manifest = candidate
    manifest["scope"] = "full_catalog_direct_ingredients"
    (output / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(bundle.BundleError, match="scope does not match"):
        bundle.verify(output, inputs)


def test_existing_destination_is_preserved(inputs, candidate):
    output, _ = candidate
    previous = (output / "manifest.json").read_bytes()
    with pytest.raises(bundle.BundleError, match="Output already exists"):
        bundle.build(inputs, output)
    assert (output / "manifest.json").read_bytes() == previous


def test_changed_implementation_fails_currentness(inputs, candidate, monkeypatch):
    output, _ = candidate
    actual = bundle.dependency_inventory()
    actual["scripts/ingredient_occurrences.py"] = {"sha256": "0" * 64, "bytes": 0}
    monkeypatch.setattr(bundle, "dependency_inventory", lambda: actual)
    with pytest.raises(bundle.BundleError, match="Implementation/schema/resolver"):
        bundle.verify(output, inputs)


def test_outputs_inside_input_tree_are_refused(inputs):
    with pytest.raises(bundle.BundleError, match="outside the scanned input"):
        bundle.build(inputs, inputs / "output")


def test_unpinned_verification_reports_local_consistency_only(inputs, candidate):
    output, manifest = candidate
    result = bundle.verify(output, inputs)
    assert result["assurance"] == "local_consistency_only"
    assert result["recorded_source_commit"] == manifest["git"]["commit"]
    assert "not independently verified" in result["qualification"]


def test_pinned_verification_rejects_changed_origin_before_parsing(inputs, candidate):
    output, manifest = candidate
    pin = bundle.fingerprint(output / "manifest.json")["sha256"]
    assert bundle.verify(output, inputs, expected_manifest_sha256=pin)["assurance"] == (
        "externally_pinned_manifest"
    )
    manifest["git"]["commit"] = "0" * 40
    (output / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(bundle.BundleError, match="expected handoff pin"):
        bundle.verify(output, inputs, expected_manifest_sha256=pin)
    # A changed manifest must fail its pin even before JSON parsing is attempted.
    (output / "manifest.json").write_text("not-json", encoding="utf-8")
    with pytest.raises(bundle.BundleError, match="expected handoff pin"):
        bundle.verify(output, inputs, expected_manifest_sha256=pin)


def test_duplicate_mim_metadata_must_match_actual_pin_even_without_manifest_pin(inputs, candidate):
    output, manifest = candidate
    manifest["mim_label_index"]["source_commit"] = "0" * 40
    (output / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(bundle.BundleError, match="MIM label-index metadata"):
        bundle.verify(output, inputs)


def test_manifest_change_during_verification_fails(inputs, candidate, monkeypatch):
    output, manifest = candidate
    inventory = bundle.product_inventory
    pin = bundle.fingerprint(output / "manifest.json")["sha256"]

    def changing_manifest(directory, counts):
        result = inventory(directory, counts)
        manifest["git"]["commit"] = "0" * 40
        (directory / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        return result

    monkeypatch.setattr(bundle, "product_inventory", changing_manifest)
    with pytest.raises(bundle.BundleError, match="Manifest changed during verification"):
        bundle.verify(output, inputs, expected_manifest_sha256=pin)


def test_full_catalog_relocation_requires_pin_and_exact_input_membership(
    inputs, tmp_path, monkeypatch
):
    # Use a tiny authoritative corpus to exercise the full-catalog path without
    # scanning production records. The native parser and artifact writers run.
    monkeypatch.setattr(bundle, "DEFAULT_INPUT", inputs)
    output = tmp_path / "full-candidate"
    manifest = bundle.build(inputs, output)
    assert manifest["scope"] == "full_catalog_direct_ingredients"
    pin = bundle.fingerprint(output / "manifest.json")["sha256"]
    relocated = tmp_path / "relocated"
    shutil.copytree(inputs, relocated)
    with pytest.raises(bundle.BundleError, match="relocation requires"):
        bundle.verify(output, relocated)
    result = bundle.verify(output, relocated, expected_manifest_sha256=pin)
    assert result["scope"] == "full_catalog_direct_ingredients"
    assert result["relocated_catalog"] is True
    assert result["assurance"] == "externally_pinned_manifest"
    (relocated / "added.yaml").write_text("new: record\n", encoding="utf-8")
    with pytest.raises(bundle.BundleError, match="Input membership or content"):
        bundle.verify(output, relocated, expected_manifest_sha256=pin)


def test_recorded_subset_is_never_promoted_by_destination(inputs, candidate, monkeypatch):
    output, _ = candidate
    monkeypatch.setattr(bundle, "DEFAULT_INPUT", inputs)
    pin = bundle.fingerprint(output / "manifest.json")["sha256"]
    assert bundle.verify(output, inputs, expected_manifest_sha256=pin)["scope"] == "subset"
