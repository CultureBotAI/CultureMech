#!/usr/bin/env python3
"""Validate typed UniProtKB ProteinExample entries in CultureMech YAML records.

Checks both closed-schema LinkML conformance (`UniProtTerm`, `ProteinExample`)
and semantic `ProteinExample` constraints (canonical UniProtKB primary
accession, explicit `NCBITaxon` `organism_term` with non-empty label, taxon
consistency with enclosing `target_organisms`, and claim-scoped `EvidenceItem`
with non-empty `reference`, `supports`, `snippet`, and `explanation`).

Usage:
    uv run python scripts/validate_protein_examples.py data/normalized_yaml/bacterial/r2a_medium.yaml
    uv run python scripts/validate_protein_examples.py data/normalized_yaml/
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Iterable

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from culturemech.validation.protein_examples import (  # noqa: E402
    iter_protein_example_lists,
    validate_recipe_protein_examples,
)
from culturemech.validation.write_validated import validate_recipe  # noqa: E402


def _iter_yaml_files(paths: Iterable[Path]) -> Iterable[Path]:
    for p in paths:
        if p.is_dir():
            for child in sorted(p.rglob("*.yaml")):
                if not child.name.endswith("_index.yaml"):
                    yield child
        elif p.is_file():
            yield p


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=None,
        help="YAML files or directories to validate (default: data/normalized_yaml).",
    )
    parser.add_argument(
        "--paths",
        dest="opt_paths",
        nargs="+",
        type=Path,
        default=None,
        help="Optional flag form for YAML files or directories to validate.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Optional TSV path to write any protein_examples validation findings.",
    )
    parser.add_argument(
        "--require-examples",
        action="store_true",
        help="Fail if none of the inspected files contain any protein_examples entries.",
    )
    args = parser.parse_args(argv)

    target_paths = args.opt_paths or args.paths or [REPO_ROOT / "data" / "normalized_yaml"]

    files_checked = 0
    examples_checked = 0
    error_count = 0
    rows: list[tuple[str, str, str]] = []

    for yaml_path in _iter_yaml_files(target_paths):
        files_checked += 1
        try:
            instance = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"[ERROR] {yaml_path}: YAML parse error: {exc}", file=sys.stderr)
            rows.append((str(yaml_path), "", f"YAML parse error: {exc}"))
            error_count += 1
            continue
        if not isinstance(instance, dict):
            continue

        lists = iter_protein_example_lists(instance)
        if not lists:
            continue

        for _, entries, _ in lists:
            examples_checked += len(entries)

        if "cofactors" in instance and "id" not in instance:
            issues = validate_recipe_protein_examples(instance)
            for issue in issues:
                print(f"[ERROR] {yaml_path} ({issue.path}): {issue.message}", file=sys.stderr)
                rows.append((str(yaml_path), issue.path, issue.message))
                error_count += 1
        else:
            results = validate_recipe(instance)
            for res in results:
                ctx = ",".join(res.context) if res.context else (str(res.instance_index) if res.instance_index else "")
                loc = f" ({ctx})" if ctx else ""
                print(f"[ERROR] {yaml_path}{loc}: {res.message}", file=sys.stderr)
                rows.append((str(yaml_path), ctx, res.message))
                error_count += 1

    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh, delimiter="\t")
            writer.writerow(["file", "path", "message"])
            writer.writerows(rows)

    print(
        f"Checked {files_checked} file(s), {examples_checked} protein_examples entry/entries; "
        f"errors: {error_count}"
    )
    if args.require_examples and examples_checked == 0:
        print("[ERROR] No protein_examples entries found in inspected scope.", file=sys.stderr)
        return 1
    return 1 if error_count > 0 else 0


if __name__ == "__main__":
    raise SystemExit(main())
