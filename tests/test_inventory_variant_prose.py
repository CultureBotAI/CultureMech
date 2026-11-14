"""Lossless prose inventory and provenance boundaries for issue #683."""

from __future__ import annotations

import csv
import json
import shutil
import sys
from pathlib import Path

import inventory_variant_prose as inventory
import pytest
import yaml


def write_record(root: Path, relative: str, record: dict | str) -> Path:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    content = record if isinstance(record, str) else yaml.safe_dump(record, allow_unicode=True)
    path.write_text(content, encoding="utf-8")
    return path


@pytest.fixture
def inputs(tmp_path):
    root = tmp_path / "inputs"
    write_record(
        root,
        "algae/medium.yaml",
        {
            "id": "CultureMech:000001",
            "references": [{"reference": "fixture:reference", "notes": "Unreviewed fixture"}],
            "variants": [
                {
                    "name": "assay",
                    "relationship": "modified_formulation",
                    "description": "Stock culture and assay are distinct.",
                    "purpose": "Test preservation, not scientific validity.",
                    "modifications": [
                        'Keep a "quoted" value\tand newline\nβ exactly.',
                        "",
                        "Keep an arbitrary nonchemical change.",
                    ],
                    "evidence": [{"reference": "fixture:reference", "snippet": "exact text"}],
                },
                {"name": "context without modifications", "description": "Do not drop me."},
                {"name": "context with empty modifications", "modifications": []},
            ],
        },
    )
    write_record(root, ".hidden/zero.yml", {"id": "CultureMech:000002", "variants": []})
    write_record(root, "ignored/zero.yaml", {"id": "CultureMech:000003"})
    (root / ".gitignore").write_text("ignored/\n", encoding="utf-8")
    return root


@pytest.fixture
def output(inputs, tmp_path):
    directory = tmp_path / "review"
    inventory.build(inputs, directory)
    return directory


def read_queue(output: Path) -> list[dict]:
    previous = csv.field_size_limit()
    try:
        csv.field_size_limit(sys.maxsize)
        with (output / inventory.PRODUCT).open(encoding="utf-8", newline="") as stream:
            return list(csv.DictReader(stream, delimiter="\t"))
    finally:
        csv.field_size_limit(previous)


def manifest(output: Path) -> dict:
    return json.loads((output / "manifest.json").read_text(encoding="utf-8"))


def rewrite_manifest(output: Path, value: dict) -> None:
    (output / "manifest.json").write_text(inventory.canonical_json(value) + "\n", encoding="utf-8")


def test_lossless_rows_context_and_accounting(inputs, output):
    rows = read_queue(output)
    original = yaml.safe_load((inputs / "algae/medium.yaml").read_text())
    assert len(rows) == 5
    assert [row["row_kind"] for row in rows] == ["modification"] * 3 + ["context_only"] * 2
    assert [row["modification_index"] for row in rows] == ["0", "1", "2", "", ""]
    assert [row["variant_index"] for row in rows] == ["0", "0", "0", "1", "2"]
    assert [row["modification_text"] for row in rows[:3]] == original["variants"][0][
        "modifications"
    ]
    assert all(row["review_status"] == "UNREVIEWED" for row in rows)
    assert rows[0]["variant_relationship"] == "modified_formulation"
    assert rows[0]["variant_purpose"] == original["variants"][0]["purpose"]
    for row in rows:
        assert json.loads(row["variant_json"]) == original["variants"][int(row["variant_index"])]
        assert json.loads(row["record_references_json"]) == original["references"]
        assert row["source_sha256"] == inventory.fingerprint(inputs / row["source_path"])["sha256"]
    document = manifest(output)
    assert document["counts"] == {
        "scanned_records": 3,
        "records_with_variants": 1,
        "records_without_variants": 2,
        "variants": 3,
        "modification_entries": 3,
        "context_only_variants": 2,
        "queue_rows": 5,
    }
    assert sorted(document["sources"]) == [
        ".hidden/zero.yml",
        "algae/medium.yaml",
        "ignored/zero.yaml",
    ]
    assert document["scope"]["mapping_decisions"] is False
    assert inventory.verify(output)["verification_level"] == "local_consistency_only"


def test_repeated_builds_are_byte_identical(inputs, output, tmp_path):
    second = tmp_path / "second"
    inventory.build(inputs, second)
    assert (output / inventory.PRODUCT).read_bytes() == (second / inventory.PRODUCT).read_bytes()
    assert (output / "manifest.json").read_bytes() == (second / "manifest.json").read_bytes()


def test_plan_writes_no_artifact(inputs, tmp_path, capsys):
    before = sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))
    assert inventory.main(["--plan", "--input-dir", str(inputs)]) == 0
    result = json.loads(capsys.readouterr().out)
    assert result["plan_only"] is True
    assert result["counts"]["queue_rows"] == 5
    assert "sources" not in result
    assert "modification_text" not in result
    assert before == sorted(path.relative_to(tmp_path) for path in tmp_path.rglob("*"))


@pytest.mark.parametrize(
    "record",
    [
        "",
        "[]",
        "id: CultureMech:000001\nvariants: invalid\n",
        {"variants": []},
        {"id": "CultureMech:000001", "variants": None},
        {"id": "CultureMech:000001", "variants": ["invalid"]},
        {"id": "CultureMech:000001", "variants": [{}]},
        {"id": "CultureMech:000001", "variants": [{"name": "x", "modifications": "text"}]},
        {"id": "CultureMech:000001", "variants": [{"name": "x", "modifications": [42]}]},
        {"id": "CultureMech:000001", "variants": [{"name": "x", "modifications": None}]},
        {"id": "CultureMech:000001", "variants": [{"name": "x", "purpose": ["bad"]}]},
        "id: CultureMech:000001\nvariants: []\nvariants: []\n",
    ],
    ids=[
        "empty",
        "root_list",
        "variants_scalar",
        "missing_id",
        "null_variants",
        "scalar_variant",
        "missing_name",
        "scalar_modifications",
        "nontext_modification",
        "null_modifications",
        "nontext_context",
        "duplicate_key",
    ],
)
def test_invalid_source_cannot_publish_manifest(tmp_path, record):
    root = tmp_path / "inputs"
    write_record(root, "invalid.yaml", record)
    output = tmp_path / "output"
    with pytest.raises(inventory.InventoryError):
        inventory.build(root, output)
    assert not (output / "manifest.json").exists()


def test_empty_source_directory_fails(tmp_path):
    empty = tmp_path / "empty"
    empty.mkdir()
    with pytest.raises(inventory.InventoryError, match="No YAML"):
        inventory.build(empty, tmp_path / "output")


def test_existing_output_is_never_overwritten(inputs, output):
    before = (output / "manifest.json").read_bytes()
    with pytest.raises(inventory.InventoryError, match="must be new"):
        inventory.build(inputs, output)
    assert (output / "manifest.json").read_bytes() == before


@pytest.mark.parametrize("location", ["same", "nested", "symlink_parent"])
def test_output_under_source_is_rejected_before_collect(inputs, tmp_path, monkeypatch, location):
    if location == "same":
        output = inputs
    elif location == "nested":
        output = inputs / "new-output"
    else:
        alias = tmp_path / "alias"
        alias.symlink_to(inputs, target_is_directory=True)
        output = alias / "new-output"

    def unexpected_collect(*args):
        pytest.fail("Output location must be checked before source collection")

    monkeypatch.setattr(inventory, "collect", unexpected_collect)
    with pytest.raises(inventory.InventoryError, match="outside the input"):
        inventory.build(inputs, output)
    assert not (output / "manifest.json").exists()
    if location != "same":
        assert not output.exists()


@pytest.mark.parametrize("change", ["add", "remove", "modify"])
def test_source_membership_and_content_drift(inputs, output, change):
    if change == "add":
        write_record(inputs, ".hidden/new.yaml", {"id": "CultureMech:000004"})
    elif change == "remove":
        (inputs / "ignored/zero.yaml").unlink()
    else:
        with (inputs / "ignored/zero.yaml").open("a") as stream:
            stream.write("# Changed raw source bytes\n")
    with pytest.raises(inventory.InventoryError, match="Source membership/content"):
        inventory.verify(output)


def test_output_tamper_detected_even_with_rehashed_manifest(output):
    queue = output / inventory.PRODUCT
    queue.write_bytes(queue.read_bytes().replace(b"UNREVIEWED", b"ACCEPTED"))
    value = manifest(output)
    value["products"][inventory.PRODUCT] = inventory.fingerprint(queue)
    rewrite_manifest(output, value)
    with pytest.raises(inventory.InventoryError, match="source-derived queue"):
        inventory.verify(output)


def test_counts_recomputed_from_sources(output):
    value = manifest(output)
    value["counts"]["variants"] += 1
    rewrite_manifest(output, value)
    with pytest.raises(inventory.InventoryError, match="Accounting"):
        inventory.verify(output)


def test_subset_cannot_claim_whole_catalog_in_local_verification(output):
    value = manifest(output)
    value["source_scope"] = "whole_catalog"
    rewrite_manifest(output, value)
    with pytest.raises(inventory.InventoryError, match="Source scope"):
        inventory.verify(output)


@pytest.mark.parametrize(
    "dependency",
    ["scripts/inventory_variant_prose.py", "src/culturemech/schema/culturemech.yaml", "uv.lock"],
)
def test_dependency_drift(inputs, tmp_path, monkeypatch, dependency):
    root = tmp_path / "tool"
    for relative in inventory.dependency_inventory():
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(inventory.REPO_ROOT / relative, target)
    monkeypatch.setattr(inventory, "REPO_ROOT", root)
    monkeypatch.setattr(inventory, "checkout_revision", lambda: "0" * 40)
    output = tmp_path / "output"
    inventory.build(inputs, output)
    with (root / dependency).open("a") as stream:
        stream.write("\n# dependency drift\n")
    with pytest.raises(inventory.InventoryError, match="dependencies"):
        inventory.verify(output)


def test_runtime_drift(output, monkeypatch):
    runtime = inventory.environment()
    monkeypatch.setattr(inventory, "environment", lambda: dict(runtime, PyYAML="changed"))
    with pytest.raises(inventory.InventoryError, match="Runtime"):
        inventory.verify(output)


def test_external_pin_and_relocation(inputs, output, tmp_path):
    pin = inventory.fingerprint(output / "manifest.json")["sha256"]
    relocated = tmp_path / "relocated"
    shutil.copytree(inputs, relocated)
    with pytest.raises(inventory.InventoryError, match="externally pinned"):
        inventory.verify(output, relocated)
    result = inventory.verify(output, relocated, pin)
    assert result["verification_level"] == "externally_pinned_manifest"
    assert result["source_scope"] == "subset"
    assert result["checkout_revision_independently_verified"] is False
    with pytest.raises(inventory.InventoryError, match="externally supplied"):
        inventory.verify(output, expected_manifest_sha256="0" * 64)
    value = manifest(output)
    value["checkout_revision"] = "0" * 40
    rewrite_manifest(output, value)
    with pytest.raises(inventory.InventoryError, match="externally supplied"):
        inventory.verify(output, expected_manifest_sha256=pin)


def test_large_and_timestamp_looking_text_remains_lossless(tmp_path):
    inputs = tmp_path / "inputs"
    text = 'Long "quoted" text\n' + "x" * 150_000
    write_record(
        inputs,
        "large.yaml",
        {
            "id": "CultureMech:000001",
            "variants": [{"name": "large", "modifications": [text]}],
        },
    )
    write_record(
        inputs,
        "date.yaml",
        "id: CultureMech:000002\nvariants:\n- name: dates\n  modifications:\n  - 2026-11-13\n",
    )
    output = tmp_path / "output"
    inventory.build(inputs, output)
    assert [row["modification_text"] for row in read_queue(output)] == ["2026-11-13", text]
    assert inventory.verify(output)["counts"]["modification_entries"] == 2


def test_source_change_after_queue_write_never_publishes_manifest(inputs, tmp_path, monkeypatch):
    output = tmp_path / "output"
    original = Path.write_bytes

    def change_source(path, content):
        result = original(path, content)
        if path.name == inventory.PRODUCT:
            with (inputs / "ignored/zero.yaml").open("a") as stream:
                stream.write("# source changed during publication\n")
        return result

    monkeypatch.setattr(Path, "write_bytes", change_source)
    with pytest.raises(inventory.InventoryError, match="changed during inventory"):
        inventory.build(inputs, output)
    assert (output / inventory.PRODUCT).is_file()
    assert not (output / "manifest.json").exists()


def test_partial_publication_has_no_accepted_manifest(inputs, tmp_path, monkeypatch):
    output = tmp_path / "output"

    def fail_publication(*args):
        raise OSError("Injected publication failure")

    monkeypatch.setattr(inventory.os, "replace", fail_publication)
    assert inventory.main(["--input-dir", str(inputs), "--output-dir", str(output)]) == 1
    assert (output / inventory.PRODUCT).is_file()
    assert (output / "manifest.json.pending").is_file()
    assert not (output / "manifest.json").exists()
    assert inventory.main(["--verify", str(output)]) == 1


def test_no_fallible_fingerprint_after_manifest_publication(inputs, tmp_path, monkeypatch):
    output = tmp_path / "output"
    published = False
    original_replace = inventory.os.replace
    original_fingerprint = inventory.fingerprint

    def replace_then_lock_reads(source, target):
        nonlocal published
        original_replace(source, target)
        published = True

    def fingerprint_before_publication_only(path):
        if published:
            raise OSError("Injected post-publication read failure")
        return original_fingerprint(path)

    monkeypatch.setattr(inventory.os, "replace", replace_then_lock_reads)
    monkeypatch.setattr(inventory, "fingerprint", fingerprint_before_publication_only)
    receipt = inventory.build(inputs, output)
    assert published
    assert (
        receipt["manifest_sha256"]
        == inventory.fingerprint_bytes((output / "manifest.json").read_bytes())["sha256"]
    )
    assert receipt["counts"]["queue_rows"] == 5


def test_symlinked_source_is_not_silently_skipped(inputs, tmp_path):
    (inputs / "linked").symlink_to(tmp_path, target_is_directory=True)
    with pytest.raises(inventory.InventoryError, match="Symlink"):
        inventory.corpus_inventory(inputs)
