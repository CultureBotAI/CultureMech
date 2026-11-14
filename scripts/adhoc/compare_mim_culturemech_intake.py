#!/usr/bin/env python3
"""Compare CultureMech ingredient-bundle and frozen MIM intake manifests (#687).

Inputs: local bundle manifest (inputs) and MIM manifest (culturemech_files).
Output: JSON receipt of exact recipe paths/SHA256 values; source files are read only.
This checks source-byte coverage, not ingredient identity, mapping coverage, or
release readiness. No network access or campaign mutations. Added 2026-11-13.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

PREFIX = "data/normalized_yaml/"
SHA256 = re.compile(r"[0-9a-fA-F]{64}\Z")


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    """Reject duplicate JSON keys rather than silently discard source entries."""
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def read_manifest(path: Path) -> tuple[dict[str, Any], str]:
    raw = path.read_bytes()
    manifest = json.loads(raw, object_pairs_hook=unique_object)
    if not isinstance(manifest, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return manifest, hashlib.sha256(raw).hexdigest()


def source_hashes(manifest: dict[str, Any], key: str) -> dict[str, str]:
    entries = manifest.get(key)
    if not isinstance(entries, dict) or not entries:
        raise ValueError(f"{key}: expected a nonempty object")
    result: dict[str, str] = {}
    for raw_path, entry in entries.items():
        path = raw_path.removeprefix(PREFIX)
        if (
            not path
            or "\\" in path
            or any(part in {"", ".", ".."} for part in path.split("/"))
        ):
            raise ValueError(f"{key}: unsafe or noncanonical relative path {raw_path!r}")
        if path in result:
            raise ValueError(f"{key}: duplicate normalized path {path!r}")
        if key == "inputs" and not isinstance(entry, dict):
            raise ValueError(f"{key}: expected SHA256 metadata object for {raw_path!r}")
        digest = entry.get("sha256") if key == "inputs" else entry
        if not isinstance(digest, str) or not SHA256.fullmatch(digest):
            raise ValueError(f"{key}: invalid SHA256 for {raw_path!r}")
        result[path] = digest.lower()
    return result


def compare_manifests(bundle_path: Path, mim_path: Path) -> dict[str, Any]:
    bundle, bundle_digest = read_manifest(bundle_path)
    mim, mim_digest = read_manifest(mim_path)
    bundle_files = source_hashes(bundle, "inputs")
    mim_files = source_hashes(mim, "culturemech_files")
    common = bundle_files.keys() & mim_files.keys()
    missing_from_mim = sorted(bundle_files.keys() - mim_files.keys())
    missing_from_bundle = sorted(mim_files.keys() - bundle_files.keys())
    changed = [
        {"path": path, "bundle_sha256": bundle_files[path], "mim_sha256": mim_files[path]}
        for path in sorted(common)
        if bundle_files[path] != mim_files[path]
    ]
    match = not (missing_from_mim or missing_from_bundle or changed)
    return {
        "schema_version": 1,
        "status": "MATCH" if match else "MISMATCH",
        "scope": "CultureMech recipe paths and SHA256 bytes declared by two manifests",
        "limitations": [
            "Does not rehash the recipe files or verify either manifest's producer.",
            "Does not establish ingredient-group, occurrence, or mapping coverage.",
            "Does not establish scientific approval or MIM/KGM release readiness.",
        ],
        "path_normalization": f"Remove one leading {PREFIX!r}; preserve remaining characters.",
        "sources": {
            "bundle": {"path": str(bundle_path), "sha256": bundle_digest, "key": "inputs"},
            "mim": {"path": str(mim_path), "sha256": mim_digest, "key": "culturemech_files"},
        },
        "counts": {
            "bundle_files": len(bundle_files),
            "mim_files": len(mim_files),
            "common_paths": len(common),
            "matching_sha256": len(common) - len(changed),
            "missing_from_mim": len(missing_from_mim),
            "missing_from_bundle": len(missing_from_bundle),
            "sha256_mismatches": len(changed),
        },
        "missing_from_mim": missing_from_mim,
        "missing_from_bundle": missing_from_bundle,
        "sha256_mismatches": changed,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-manifest", required=True, type=Path)
    parser.add_argument("--mim-manifest", required=True, type=Path)
    parser.add_argument("--output", type=Path, help="New JSON receipt; defaults to stdout. Never overwrite.")
    args = parser.parse_args(argv)
    try:
        receipt = compare_manifests(args.bundle_manifest, args.mim_manifest)
        encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
        if args.output is None:
            sys.stdout.write(encoded)
        else:
            with args.output.open("x", encoding="utf-8") as stream:
                stream.write(encoded)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    return 0 if receipt["status"] == "MATCH" else 1


if __name__ == "__main__":
    raise SystemExit(main())
