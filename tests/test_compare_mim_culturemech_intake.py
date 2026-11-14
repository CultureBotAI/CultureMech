"""Fail-closed checks for the source-byte reconciliation used by release tracker #687."""

import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/adhoc/compare_mim_culturemech_intake.py"
SPEC = importlib.util.spec_from_file_location("compare_mim_culturemech_intake", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
compare = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(compare)
pytestmark = pytest.mark.fast

A = "a" * 64
B = "b" * 64


def manifests(tmp_path, bundle_files, mim_files):
    bundle = tmp_path / "bundle.json"
    mim = tmp_path / "mim.json"
    bundle.write_text(json.dumps({"inputs": bundle_files}))
    mim.write_text(json.dumps({"culturemech_files": mim_files}))
    return bundle, mim


def test_match_normalizes_only_prefix_and_records_exact_source_digests(tmp_path):
    bundle, mim = manifests(
        tmp_path,
        {"algae/β Medium.yaml": {"sha256": A, "bytes": 123}},
        {"data/normalized_yaml/algae/β Medium.yaml": A.upper()},
    )
    before = (bundle.read_bytes(), mim.read_bytes())
    receipt = compare.compare_manifests(bundle, mim)
    assert receipt["status"] == "MATCH"
    assert receipt["counts"]["matching_sha256"] == 1
    assert receipt["sources"]["bundle"]["sha256"] == hashlib.sha256(before[0]).hexdigest()
    assert receipt["sources"]["mim"]["sha256"] == hashlib.sha256(before[1]).hexdigest()
    assert (bundle.read_bytes(), mim.read_bytes()) == before


def test_reports_drift_in_both_directions_and_exits_nonzero(tmp_path, capsys):
    bundle, mim = manifests(
        tmp_path,
        {"algae/changed.yaml": {"sha256": A}, "algae/new.yaml": {"sha256": A}},
        {"data/normalized_yaml/algae/changed.yaml": B, "algae/old.yaml": A},
    )
    assert compare.main(["--bundle-manifest", str(bundle), "--mim-manifest", str(mim)]) == 1
    receipt = json.loads(capsys.readouterr().out)
    assert receipt["status"] == "MISMATCH"
    assert receipt["missing_from_mim"] == ["algae/new.yaml"]
    assert receipt["missing_from_bundle"] == ["algae/old.yaml"]
    assert receipt["sha256_mismatches"] == [
        {"path": "algae/changed.yaml", "bundle_sha256": A, "mim_sha256": B}
    ]


@pytest.mark.parametrize(
    "entries, message",
    [
        ({}, "nonempty object"),
        ({"algae/a.yaml": "invalid"}, "invalid SHA256"),
        ({"../algae/a.yaml": A}, "relative path"),
        ({"/algae/a.yaml": A}, "relative path"),
        ({"algae//a.yaml": A}, "relative path"),
        ({"algae/a.yaml": A, "data/normalized_yaml/algae/a.yaml": A}, "duplicate normalized"),
    ],
)
def test_rejects_invalid_or_ambiguous_inventory(entries, message):
    with pytest.raises(ValueError, match=message):
        compare.source_hashes({"culturemech_files": entries}, "culturemech_files")


def test_duplicate_json_keys_are_rejected(tmp_path):
    source = tmp_path / "duplicate.json"
    source.write_text('{"culturemech_files": {}, "culturemech_files": {}}')
    with pytest.raises(ValueError, match="duplicate JSON key"):
        compare.read_manifest(source)


def test_bundle_entries_require_sha256_metadata_objects():
    with pytest.raises(ValueError, match="metadata object"):
        compare.source_hashes({"inputs": {"algae/a.yaml": A}}, "inputs")
    with pytest.raises(ValueError, match="invalid SHA256"):
        compare.source_hashes({"inputs": {"algae/a.yaml": {"bytes": 123}}}, "inputs")


def test_receipt_cannot_overwrite_input_or_existing_output(tmp_path):
    bundle, mim = manifests(tmp_path, {"algae/a.yaml": {"sha256": A}}, {"algae/a.yaml": A})
    args = ["--bundle-manifest", str(bundle), "--mim-manifest", str(mim)]
    before = bundle.read_bytes()
    with pytest.raises(SystemExit) as error:
        compare.main([*args, "--output", str(bundle)])
    assert error.value.code == 2
    assert bundle.read_bytes() == before
    output = tmp_path / "receipt.json"
    assert compare.main([*args, "--output", str(output)]) == 0
    assert json.loads(output.read_text())["status"] == "MATCH"
    with pytest.raises(SystemExit) as error:
        compare.main([*args, "--output", str(output)])
    assert error.value.code == 2
