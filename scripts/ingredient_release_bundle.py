#!/usr/bin/env python3
"""Build/verify a provenance-bound direct-ingredient candidate (2026-11-13).

Inputs: normalized YAML, native aggregator/schema and packaged MIM label index.
Outputs: existing five aggregation products plus a manifest in a new directory.
Serves issue #682; never publishes a MIM release.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.metadata
import json
import os
import platform
import subprocess
import sys
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = REPO_ROOT / "data" / "normalized_yaml"
PRODUCTS = (
    "ingredient_occurrences.tsv",
    "ingredients_list.tsv",
    "mapped_ingredients.yaml",
    "unmapped_ingredients.yaml",
    "ingredient_aggregation_errors.tsv",
)
CONTRACT = "culturemech-direct-ingredients-v1"
SCOPE = {
    "included": [
        "root ingredients or composition selected by native record shape",
        "recursively inline solutions[].composition",
    ],
    "excluded": [
        "expansion of references to other scanned solution records",
        "variant modification text and ingredients mentioned only in prose",
        "copies inside referenced stocks beyond the referenced record",
    ],
}


class BundleError(ValueError):
    """The candidate cannot be accepted or verified."""


def fingerprint(path: Path) -> dict[str, Any]:
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
            size += len(chunk)
    return {"sha256": digest.hexdigest(), "bytes": size}


def corpus_inventory(input_dir: Path) -> dict[str, Any]:
    if not input_dir.is_dir():
        raise BundleError(f"Input directory does not exist: {input_dir}")
    files = sorted(input_dir.rglob("*.yaml"))  # Includes ignored/hidden inputs, like native scan.
    if not files:
        raise BundleError("No YAML input files")
    return {path.relative_to(input_dir).as_posix(): fingerprint(path) for path in files}


def dependency_inventory() -> dict[str, Any]:
    # Pin the local Python/schema closure conservatively. This also notices new
    # imported modules without maintaining a second hand-written import graph.
    paths = set((REPO_ROOT / "src" / "culturemech").rglob("*.py"))
    paths.update((REPO_ROOT / "src" / "culturemech" / "schema").rglob("*.yaml"))
    for relative in (
        "scripts/ingredient_release_bundle.py",
        "scripts/ingredient_occurrences.py",
        "scripts/record_kinds.py",
        "scripts/validate_strict.py",
        "src/culturemech/data/mediaingredientmech/label_index.csv",
        "src/culturemech/data/mediaingredientmech/label_index.metadata.json",
        "pyproject.toml",
        "uv.lock",
    ):
        paths.add(REPO_ROOT / relative)
    return {path.relative_to(REPO_ROOT).as_posix(): fingerprint(path) for path in sorted(paths)}


def git_state() -> dict[str, Any]:
    def git(*args: str) -> str:
        return subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), *args], text=True, encoding="utf-8"
        ).strip()

    status = git("status", "--porcelain", "--untracked-files=normal")
    return {"commit": git("rev-parse", "HEAD"), "dirty": bool(status), "status": status}


def environment() -> dict[str, Any]:
    packages = {}
    for name in ("PyYAML", "linkml", "linkml-runtime", "jsonschema"):
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = None
    return {"python": platform.python_version(), "packages": packages}


def _rows(path: Path):
    with path.open(encoding="utf-8", newline="") as stream:
        yield from csv.DictReader(stream, delimiter="\t")


def artifact_accounting(directory: Path, corpus: dict[str, Any]) -> dict[str, Any]:
    """Reconcile native TSVs, including quoted/newline-containing cells."""
    occurrences = mapped = 0
    paths: set[str] = set()
    keys: set[tuple[str, str, str]] = set()
    categories: Counter[str] = Counter()
    for row in _rows(directory / "ingredient_occurrences.tsv"):
        key = (row["recipe_id"], row["component_field"], row["component_index"])
        if key in keys:
            raise BundleError(f"Duplicate occurrence coordinate: {key}")
        keys.add(key)
        source_path = row["source_path"]
        if source_path not in corpus:
            raise BundleError(f"Occurrence outside input inventory: {source_path}")
        paths.add(source_path)
        categories[row["recipe_category"] or "UNKNOWN"] += 1
        occurrences += 1
        mapped += bool(row["resolved_identifier"])

    groups: Counter[str] = Counter()
    grouped_occurrences: Counter[str] = Counter()
    for row in _rows(directory / "ingredients_list.tsv"):
        status = row["mapping_status"]
        if status not in {"MAPPED", "UNMAPPED", "AMBIGUOUS"}:
            raise BundleError(f"Unknown mapping status: {status}")
        if bool(row["resolved_identifier"]) != (status == "MAPPED"):
            raise BundleError("List status disagrees with resolved identity")
        count = int(row["occurrence_count"])
        if count < 1:
            raise BundleError("Ingredient group has no occurrences")
        groups[status] += 1
        grouped_occurrences[status] += count
    if sum(grouped_occurrences.values()) != occurrences:
        raise BundleError("Ingredient-list counts do not equal occurrence count")
    if grouped_occurrences["MAPPED"] != mapped:
        raise BundleError("Mapped ingredient-list counts do not equal mapped occurrences")
    errors = sum(1 for _ in _rows(directory / "ingredient_aggregation_errors.tsv"))
    if errors:
        raise BundleError(f"Aggregation has {errors} errors")
    return {
        "scanned_records": len(corpus),
        "records_with_occurrences": len(paths),
        "records_without_direct_occurrences": len(corpus) - len(paths),
        "scanned_files_by_directory": dict(
            sorted(Counter(path.split("/")[0] if "/" in path else "." for path in corpus).items())
        ),
        "occurrences_by_category": dict(sorted(categories.items())),
        "occurrences": occurrences,
        "mapped_occurrences": mapped,
        "unresolved_occurrences": occurrences - mapped,
        "ingredient_groups": sum(groups.values()),
        "groups_by_status": dict(sorted(groups.items())),
        "errors": errors,
    }


def product_inventory(directory: Path, counts: dict[str, Any]) -> dict[str, Any]:
    products = {name: fingerprint(directory / name) for name in PRODUCTS}
    for name, count in (
        ("ingredient_occurrences.tsv", counts["occurrences"]),
        ("ingredients_list.tsv", counts["ingredient_groups"]),
        ("ingredient_aggregation_errors.tsv", counts["errors"]),
    ):
        products[name]["data_rows"] = count
    return products


def _aggregate(input_dir: Path, stage: Path) -> int:
    # Plan/verification do not import the schema validator or run aggregation.
    sys.path.insert(0, str(REPO_ROOT / "src"))
    sys.path.insert(0, str(REPO_ROOT / "scripts"))
    import ingredient_occurrences

    from culturemech.ingredients import mim_label_index

    for module in (ingredient_occurrences, mim_label_index):
        if not Path(module.__file__).resolve().is_relative_to(REPO_ROOT):
            raise BundleError(f"Imported code outside pinned checkout: {module.__file__}")
    # Verify even an empty-direct-occurrence corpus binds a valid packaged pin.
    mim_label_index.get_default_mim_label_index.cache_clear()
    mim_label_index.get_default_mim_label_index()
    return ingredient_occurrences.run_aggregation(
        input_dir=input_dir,
        occurrences_output=stage / "ingredient_occurrences.tsv",
        mapped_output=stage / "mapped_ingredients.yaml",
        unmapped_output=stage / "unmapped_ingredients.yaml",
        errors_output=stage / "ingredient_aggregation_errors.tsv",
        list_output=stage / "ingredients_list.tsv",
        min_occurrences=1,
        verbose=True,
    )


def build(input_dir: Path, output_dir: Path | None, *, plan: bool = False) -> dict[str, Any]:
    input_dir = input_dir.resolve()
    if output_dir is None and not plan:
        raise BundleError("build requires --output-dir unless --plan is selected")
    if output_dir is not None:
        output_dir = output_dir.absolute()
        if output_dir.exists() or output_dir.is_symlink():
            raise BundleError(f"Output already exists; choose a new directory: {output_dir}")
        if output_dir.resolve().is_relative_to(input_dir):
            raise BundleError("Output must be outside the scanned input directory")
    before = corpus_inventory(input_dir)
    dependencies = dependency_inventory()
    git = git_state()
    scope = "full_catalog_direct_ingredients" if input_dir == DEFAULT_INPUT else "subset"
    if plan:
        return {
            "status": "PLAN_ONLY",
            "scope": scope,
            "scanned_records": len(before),
            "input_dir": str(input_dir),
            "output_dir": str(output_dir) if output_dir else None,
            "git": git,
        }
    assert output_dir is not None
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=f".{output_dir.name}.incomplete-", dir=output_dir.parent))
    try:
        if _aggregate(input_dir, stage):
            raise BundleError("Native ingredient aggregation failed")
        if before != corpus_inventory(input_dir) or dependencies != dependency_inventory():
            raise BundleError("Inputs or implementation changed during aggregation")
        if git["commit"] != git_state()["commit"]:
            raise BundleError("Repository HEAD changed during aggregation")
        counts = artifact_accounting(stage, before)
        manifest = {
            "contract": CONTRACT,
            "status": "CANDIDATE",
            "integrated_release": False,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "scope": scope,
            "coverage": SCOPE,
            "input_dir": os.path.relpath(input_dir, REPO_ROOT),
            "git": git,
            "environment": environment(),
            "inputs": before,
            "dependencies": dependencies,
            "mim_label_index": json.loads(
                (
                    REPO_ROOT
                    / ("src/culturemech/data/mediaingredientmech/label_index.metadata.json")
                ).read_text(encoding="utf-8")
            ),
            "counts": counts,
            "products": product_inventory(stage, counts),
        }
        # Recheck after accounting/hashing, which can take time for large outputs.
        if before != corpus_inventory(input_dir) or dependencies != dependency_inventory():
            raise BundleError("Inputs or implementation changed during artifact accounting")
        if git["commit"] != git_state()["commit"]:
            raise BundleError("Repository HEAD changed during artifact accounting")
        # mkdir is the exclusive no-overwrite reservation. A manifest is installed
        # last; interrupted/failed publication never has an acceptance manifest.
        output_dir.mkdir()
        for name in PRODUCTS:
            (stage / name).rename(output_dir / name)
        manifest_path = output_dir / "manifest.json"
        temporary = output_dir / ".manifest.incomplete"
        temporary.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        temporary.rename(manifest_path)
        stage.rmdir()  # Empty directory created by this invocation only.
        return manifest
    except Exception as exc:
        raise BundleError(f"{exc}; incomplete evidence retained at {stage}") from exc


def verify(bundle_dir: Path, input_dir: Path | None = None) -> dict[str, Any]:
    manifest = json.loads((bundle_dir / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("contract") != CONTRACT or manifest.get("status") != "CANDIDATE":
        raise BundleError("Unsupported candidate manifest")
    if manifest.get("integrated_release") is not False or manifest.get("coverage") != SCOPE:
        raise BundleError("Candidate has an unsupported release or coverage claim")
    if set(manifest["products"]) != set(PRODUCTS):
        raise BundleError("Candidate product membership differs from contract")
    source = input_dir.resolve() if input_dir else (REPO_ROOT / manifest["input_dir"]).resolve()
    expected_scope = "full_catalog_direct_ingredients" if source == DEFAULT_INPUT else "subset"
    if manifest["scope"] != expected_scope:
        raise BundleError("Candidate scope does not match the input directory")
    current = corpus_inventory(source)
    if current != manifest["inputs"]:
        raise BundleError("Input membership or content differs from candidate")
    if dependency_inventory() != manifest["dependencies"]:
        raise BundleError("Implementation/schema/resolver differs from candidate")
    counts = artifact_accounting(bundle_dir, current)
    if (
        counts != manifest["counts"]
        or product_inventory(bundle_dir, counts) != manifest["products"]
    ):
        raise BundleError("Candidate artifacts or accounting differ from manifest")
    if current != corpus_inventory(source) or manifest["dependencies"] != dependency_inventory():
        raise BundleError("Inputs or implementation changed during verification")
    return {
        "status": "VERIFIED_CANDIDATE",
        "scope": manifest["scope"],
        "counts": counts,
        "source_commit": manifest["git"]["commit"],
        "qualification": "Current input and artifact bytes match; not an integrated MIM/KGM release.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    builder = commands.add_parser("build", help="Generate one new candidate bundle")
    builder.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT)
    builder.add_argument("--output-dir", type=Path, help="Required unless --plan is selected")
    builder.add_argument("--plan", action="store_true", help="Inventory inputs without generation")
    verifier = commands.add_parser("verify", help="Check artifacts and current input bytes")
    verifier.add_argument("--bundle-dir", type=Path, required=True)
    verifier.add_argument("--input-dir", type=Path, help="Relocated identical input directory")
    args = parser.parse_args(argv)
    try:
        result = (
            build(args.input_dir, args.output_dir, plan=args.plan)
            if args.command == "build"
            else verify(args.bundle_dir, args.input_dir)
        )
        if args.command == "build" and not args.plan:
            result = {key: result[key] for key in ("status", "scope", "counts")}
        print(json.dumps(result, indent=2, sort_keys=True))
    except (
        BundleError,
        OSError,
        KeyError,
        TypeError,
        ValueError,
        subprocess.CalledProcessError,
    ) as exc:
        print(f"Ingredient candidate failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
