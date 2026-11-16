#!/usr/bin/env python3
"""Inventory variant prose for human review, issue #683 (2026-11-13).

Inputs: normalized YAML records, this script, schema and dependency lock.
Outputs: a deterministic, lossless TSV review queue and a provenance manifest.
Review fixes #690 and #691 protect source boundaries and final publication.
This does not extract chemical identities, approve mappings or change recipes.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import platform
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = REPO_ROOT / "data" / "normalized_yaml"
CONTRACT = "culturemech-variant-prose-review-v1"
PRODUCT = "review_queue.tsv"
FIELDS = (
    "review_status",
    "row_kind",
    "recipe_id",
    "source_path",
    "source_sha256",
    "variant_index",
    "variant_name",
    "variant_relationship",
    "variant_description",
    "variant_purpose",
    "modification_index",
    "modification_text",
    "variant_json",
    "record_references_json",
)
SCOPE = {
    "included": "Every variants[].modifications[] entry, including nonchemical text",
    "context_only": "One row for each variant with absent or empty modifications",
    "review_status": "UNREVIEWED",
    "chemical_identities_inferred": False,
    "mapping_decisions": False,
    "scientific_validation": False,
}


class InventoryError(ValueError):
    """An incomplete or inconsistent review inventory cannot be accepted."""


YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


class InventoryLoader(YAML_LOADER):
    """Keep timestamp-looking text as strings and reject duplicate mapping keys."""

    yaml_implicit_resolvers = {
        key: [(tag, regex) for tag, regex in values if tag != "tag:yaml.org,2002:timestamp"]
        for key, values in YAML_LOADER.yaml_implicit_resolvers.items()
    }

    def construct_mapping(self, node, deep=False):
        self.flatten_mapping(node)
        keys = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str):
                raise InventoryError("YAML mapping keys must be strings")
            if key in keys:
                raise InventoryError(f"Duplicate YAML mapping key: {key}")
            keys.add(key)
        return super().construct_mapping(node, deep=deep)


def fingerprint_bytes(content: bytes) -> dict[str, Any]:
    return {"sha256": hashlib.sha256(content).hexdigest(), "bytes": len(content)}


def fingerprint(path: Path) -> dict[str, Any]:
    return fingerprint_bytes(path.read_bytes())


def corpus_inventory(input_dir: Path) -> dict[str, Any]:
    if not input_dir.is_dir():
        raise InventoryError(f"Input directory does not exist: {input_dir}")
    files = {}
    # Path.rglob includes gitignored and hidden paths. Reject symlinks rather
    # than silently skipping linked directories or accepting mutable outsiders.
    for path in sorted(input_dir.rglob("*")):
        if path.is_symlink():
            raise InventoryError(f"Symlink inside source directory: {path}")
        if path.suffix.lower() in {".yaml", ".yml"}:
            if not path.is_file():
                raise InventoryError(f"YAML source is not a regular file: {path}")
            files[path.relative_to(input_dir).as_posix()] = fingerprint(path)
    if not files:
        raise InventoryError("No YAML input files")
    return files


def dependency_inventory() -> dict[str, Any]:
    return {
        name: fingerprint(REPO_ROOT / name)
        for name in (
            "scripts/inventory_variant_prose.py",
            "src/culturemech/schema/culturemech.yaml",
            "pyproject.toml",
            "uv.lock",
            ".python-version",
        )
    }


def environment() -> dict[str, str]:
    return {
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
        "PyYAML": yaml.__version__,
        "yaml_loader": YAML_LOADER.__name__,
    }


def checkout_revision() -> str:
    return subprocess.check_output(
        ["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"], text=True
    ).strip()


def canonical_json(value: Any) -> str:
    # The loader rejects non-string mapping keys. Non-JSON tags, NaN and cycles
    # fail here instead of being silently coerced or dropping original context.
    return json.dumps(
        value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False
    )


def _optional_text(variant: dict[str, Any], field: str) -> str:
    value = variant.get(field)
    if value is not None and not isinstance(value, str):
        raise InventoryError(f"Variant {field} must be a string or null")
    return value or ""


def extract(input_dir: Path, sources: dict[str, Any]) -> tuple[list[dict], dict[str, int]]:
    rows = []
    counts = {
        "scanned_records": len(sources),
        "records_with_variants": 0,
        "records_without_variants": 0,
        "variants": 0,
        "modification_entries": 0,
        "context_only_variants": 0,
        "queue_rows": 0,
    }
    for relative, expected in sources.items():
        content = (input_dir / relative).read_bytes()
        if fingerprint_bytes(content) != expected:
            raise InventoryError(f"Source changed while reading: {relative}")
        try:
            record = yaml.load(content, Loader=InventoryLoader)
            if not isinstance(record, dict):
                raise InventoryError("Source must be a nonempty record mapping")
            recipe_id = record.get("id")
            if not isinstance(recipe_id, str) or not recipe_id.strip():
                raise InventoryError("Source requires a nonempty string id")
            variants = record.get("variants", [])
            if not isinstance(variants, list):
                raise InventoryError("variants must be a list when present")
            counts["records_with_variants" if variants else "records_without_variants"] += 1
            references_json = canonical_json(record.get("references"))
            for variant_index, variant in enumerate(variants):
                if not isinstance(variant, dict):
                    raise InventoryError(f"variants[{variant_index}] must be a mapping")
                name = variant.get("name")
                if not isinstance(name, str) or not name.strip():
                    raise InventoryError(f"variants[{variant_index}] requires a name")
                modifications = variant.get("modifications", [])
                if not isinstance(modifications, list):
                    raise InventoryError(f"variants[{variant_index}].modifications must be a list")
                if any(not isinstance(text, str) for text in modifications):
                    raise InventoryError(
                        f"variants[{variant_index}].modifications entries must be strings"
                    )
                common = {
                    "review_status": "UNREVIEWED",
                    "recipe_id": recipe_id,
                    "source_path": relative,
                    "source_sha256": expected["sha256"],
                    "variant_index": variant_index,
                    "variant_name": name,
                    "variant_relationship": _optional_text(variant, "relationship"),
                    "variant_description": _optional_text(variant, "description"),
                    "variant_purpose": _optional_text(variant, "purpose"),
                    "variant_json": canonical_json(variant),
                    "record_references_json": references_json,
                }
                counts["variants"] += 1
                counts["modification_entries"] += len(modifications)
                if not modifications:
                    counts["context_only_variants"] += 1
                    rows.append(
                        dict(
                            common,
                            row_kind="context_only",
                            modification_index="",
                            modification_text="",
                        )
                    )
                for index, text in enumerate(modifications):
                    rows.append(
                        dict(
                            common,
                            row_kind="modification",
                            modification_index=index,
                            modification_text=text,
                        )
                    )
        except (yaml.YAMLError, ValueError, TypeError, RecursionError) as error:
            raise InventoryError(f"{relative}: {error}") from error
    counts["queue_rows"] = len(rows)
    return rows, counts


def render_queue(rows: list[dict]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def _check_stable(input_dir: Path, sources: dict, dependencies: dict, runtime: dict) -> None:
    if corpus_inventory(input_dir) != sources:
        raise InventoryError("Source membership/content changed during inventory")
    if dependency_inventory() != dependencies:
        raise InventoryError("Script/schema/lock dependencies changed during inventory")
    if environment() != runtime:
        raise InventoryError("Runtime changed during inventory")


def collect(input_dir: Path) -> tuple[dict, bytes]:
    input_dir = input_dir.resolve()
    sources = corpus_inventory(input_dir)
    dependencies = dependency_inventory()
    runtime = environment()
    rows, counts = extract(input_dir, sources)
    product = render_queue(rows)
    _check_stable(input_dir, sources, dependencies, runtime)
    manifest = {
        "contract": CONTRACT,
        "scope": SCOPE,
        "input_root": str(input_dir),
        "source_scope": "whole_catalog" if input_dir == DEFAULT_INPUT.resolve() else "subset",
        "checkout_revision": checkout_revision(),
        "revision_note": "Source and dependency hashes bind working-tree bytes; checkout revision is informational.",
        "sources": sources,
        "dependencies": dependencies,
        "runtime": runtime,
        "counts": counts,
        "products": {PRODUCT: fingerprint_bytes(product)},
    }
    return manifest, product


def build(input_dir: Path, output_dir: Path) -> dict:
    input_dir = input_dir.resolve()
    output_dir = output_dir.resolve()
    if output_dir == input_dir or input_dir in output_dir.parents:
        raise InventoryError("Output directory must be outside the input directory")
    if output_dir.exists():
        raise InventoryError("Output directory must be new")
    manifest, product = collect(input_dir)
    manifest_bytes = (canonical_json(manifest) + "\n").encode("utf-8")
    receipt = {
        "output_dir": str(output_dir),
        "manifest_sha256": fingerprint_bytes(manifest_bytes)["sha256"],
        "source_scope": manifest["source_scope"],
        "counts": manifest["counts"],
        "scope": SCOPE,
    }
    output_dir.mkdir(parents=True, exist_ok=False)
    (output_dir / PRODUCT).write_bytes(product)
    if fingerprint(output_dir / PRODUCT) != manifest["products"][PRODUCT]:
        raise InventoryError("Written queue does not match extracted content")
    _check_stable(
        input_dir.resolve(), manifest["sources"], manifest["dependencies"], manifest["runtime"]
    )
    if fingerprint(output_dir / PRODUCT) != manifest["products"][PRODUCT]:
        raise InventoryError("Written queue changed during publication")
    # No accepted manifest exists until every source/dependency/product check
    # passes. Leave failed work in place for inspection, never clean up a
    # successfully published artifact as part of temporary-directory teardown.
    pending = output_dir / "manifest.json.pending"
    pending.write_bytes(manifest_bytes)
    os.replace(pending, output_dir / "manifest.json")
    return receipt


def verify(
    directory: Path, input_dir: Path | None = None, expected_manifest_sha256: str | None = None
) -> dict:
    manifest_path = directory / "manifest.json"
    original_manifest = manifest_path.read_bytes()
    digest = fingerprint_bytes(original_manifest)["sha256"]
    if expected_manifest_sha256 is not None:
        if not re.fullmatch(r"[0-9a-f]{64}", expected_manifest_sha256):
            raise InventoryError("Expected manifest SHA-256 must be 64 lowercase hex characters")
        if digest != expected_manifest_sha256:
            raise InventoryError("Manifest does not match externally supplied SHA-256")
    manifest = json.loads(original_manifest)
    if manifest["contract"] != CONTRACT or manifest["scope"] != SCOPE:
        raise InventoryError("Unknown or modified review-inventory contract")
    if manifest["source_scope"] not in {"whole_catalog", "subset"}:
        raise InventoryError("Unknown source scope")
    recorded_input = Path(manifest["input_root"]).resolve()
    source = input_dir.resolve() if input_dir is not None else recorded_input
    if source != recorded_input and expected_manifest_sha256 is None:
        raise InventoryError(
            "Relocated input verification requires an externally pinned manifest SHA-256"
        )
    if expected_manifest_sha256 is None:
        actual_scope = "whole_catalog" if source == DEFAULT_INPUT.resolve() else "subset"
        if manifest["source_scope"] != actual_scope:
            raise InventoryError("Source scope differs from the local input location")
    sources = corpus_inventory(source)
    dependencies = dependency_inventory()
    runtime = environment()
    if sources != manifest["sources"]:
        raise InventoryError("Source membership/content differs from manifest")
    if dependencies != manifest["dependencies"]:
        raise InventoryError("Script/schema/lock dependencies differ from manifest")
    if runtime != manifest["runtime"]:
        raise InventoryError("Runtime differs from manifest")
    rows, counts = extract(source, sources)
    expected_product = fingerprint_bytes(render_queue(rows))
    if counts != manifest["counts"]:
        raise InventoryError("Accounting differs from source-derived counts")
    if manifest["products"] != {PRODUCT: expected_product}:
        raise InventoryError("Manifest product differs from source-derived queue")
    if fingerprint(directory / PRODUCT) != expected_product:
        raise InventoryError("Written queue differs from source-derived queue")
    _check_stable(source, sources, dependencies, runtime)
    if fingerprint(directory / PRODUCT) != expected_product:
        raise InventoryError("Written queue changed during verification")
    if manifest_path.read_bytes() != original_manifest:
        raise InventoryError("Manifest changed during verification")
    return {
        "verified": True,
        "manifest_sha256": digest,
        "verification_level": (
            "externally_pinned_manifest" if expected_manifest_sha256 else "local_consistency_only"
        ),
        "checkout_revision_independently_verified": False,
        "source_scope": manifest["source_scope"],
        "counts": counts,
        "scope": SCOPE,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input-dir", type=Path, help="YAML directory (default: normalized catalog)"
    )
    parser.add_argument(
        "--output-dir", type=Path, help="New directory for review queue and manifest"
    )
    parser.add_argument(
        "--plan", action="store_true", help="Parse and report metadata only; write nothing"
    )
    parser.add_argument(
        "--verify", type=Path, metavar="DIRECTORY", help="Verify an existing review inventory"
    )
    parser.add_argument(
        "--expected-manifest-sha256", help="Externally recorded SHA-256 for --verify"
    )
    args = parser.parse_args(argv)
    if args.verify is not None and (args.plan or args.output_dir is not None):
        parser.error("--verify cannot be combined with --plan or --output-dir")
    if args.expected_manifest_sha256 and args.verify is None:
        parser.error("--expected-manifest-sha256 requires --verify")
    if args.plan and args.output_dir is not None:
        parser.error("--plan cannot be combined with --output-dir")
    if not args.plan and args.verify is None and args.output_dir is None:
        parser.error("Specify --plan, --output-dir or --verify")
    try:
        if args.verify is not None:
            result = verify(args.verify, args.input_dir, args.expected_manifest_sha256)
        elif args.plan:
            manifest, _ = collect(args.input_dir or DEFAULT_INPUT)
            result = {
                "plan_only": True,
                "source_scope": manifest["source_scope"],
                "counts": manifest["counts"],
                "scope": SCOPE,
                "products": manifest["products"],
                "runtime": manifest["runtime"],
            }
        else:
            result = build(args.input_dir or DEFAULT_INPUT, args.output_dir)
        print(json.dumps(result, sort_keys=True, indent=2))
        return 0
    except (
        InventoryError,
        OSError,
        KeyError,
        TypeError,
        ValueError,
        subprocess.CalledProcessError,
    ) as error:
        print(f"Variant prose inventory failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
