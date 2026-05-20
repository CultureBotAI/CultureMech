#!/usr/bin/env python3
"""Strict LinkML validation harness for CultureMech instance records.

Wraps the in-process linkml.validator with JsonschemaValidationPlugin(closed=True)
so unknown fields are flagged (the default `just validate` target uses an open
schema and silently lets unknown fields pass). Emits a structured TSV of every
ERROR result and exits non-zero if any are found.

Usage:
    python scripts/validate_strict.py [PATH ...]
    python scripts/validate_strict.py --sample 5
    python scripts/validate_strict.py --out reports/instance_validation_failures.tsv

Paths may be files or directories; directories are walked for *.yaml.

Default scope when no paths given:
    data/normalized_yaml/{algae,bacterial,fungal,archaea,specialized}
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Iterable

import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml.validator.report import Severity

SCHEMA_PATH = Path("src/culturemech/schema/culturemech.yaml")
OAK_CONFIG_PATH = Path("conf/oak_config.yaml")
DEFAULT_ROOTS = [Path(f"data/normalized_yaml/{sub}") for sub in
                 ("algae", "bacterial", "fungal", "archaea", "specialized")]


_SOLUTION_TERM_PREFIXES = ("mediadive.solution:", "MediaIngredientMech:")


def infer_target_class(instance: dict) -> str:
    """Pick the right root class for this record.

    A standalone stock-solution record (e.g. mediadive_*_Main_sol_*.yaml)
    is identified by its `term.id` prefix — `mediadive.solution:*` or
    `MediaIngredientMech:*`. Both correspond to ~4,784 records that
    look like SolutionDescriptors with their own id and curation
    history, not full MediaRecipes. Everything else is MediaRecipe.
    """
    if not isinstance(instance, dict):
        return "MediaRecipe"
    term = instance.get("term")
    if isinstance(term, dict):
        tid = term.get("id")
        if isinstance(tid, str) and tid.startswith(_SOLUTION_TERM_PREFIXES):
            return "SolutionRecipe"
    return "MediaRecipe"

# Per-worker singleton — built lazily after fork so the schema parses once per
# worker process, not once per file.
_VALIDATOR: Validator | None = None


def _get_validator() -> Validator:
    global _VALIDATOR
    if _VALIDATOR is None:
        _VALIDATOR = Validator(
            schema=str(SCHEMA_PATH),
            validation_plugins=[JsonschemaValidationPlugin(closed=True)],
        )
    return _VALIDATOR


# Classifier regexes — keep narrow so each category is meaningful and the rest
# fall into "other" for manual review rather than getting silently bucketed.
_CATEGORY_RULES: list[tuple[str, re.Pattern[str]]] = [
    ("unexpected_field",
     re.compile(r"Additional properties are not allowed \('(?P<key>[^']+)' was unexpected\) in (?P<path>\S+)")),
    ("missing_required",
     re.compile(r"'(?P<key>[^']+)' is a required property in (?P<path>\S+)")),
    ("enum_mismatch",
     re.compile(r"'(?P<value>[^']+)' is not one of \[(?P<choices>[^\]]+)\]")),
    ("type_mismatch",
     re.compile(r"(?P<value>'[^']+'|\S+) is not of type '(?P<type>[^']+)'")),
    ("pattern_mismatch",
     re.compile(r"(?P<value>'[^']+'|\S+) does not match (?P<pattern>'[^']+')")),
    ("format_mismatch",
     re.compile(r"(?P<value>'[^']+'|\S+) is not a '(?P<format>[^']+)'")),
    ("range_violation",
     re.compile(r"(?P<value>\S+) is (less than|greater than) (?P<bound>\S+)")),
]


def classify(message: str) -> tuple[str, str]:
    """Return (category, detail) for a validator message."""
    for name, rule in _CATEGORY_RULES:
        m = rule.search(message)
        if m:
            parts = m.groupdict()
            detail = "|".join(f"{k}={v}" for k, v in parts.items())
            return name, detail
    return "other", ""


def validate_one(path: Path) -> list[dict]:
    """Validate a single YAML file. Returns one dict per ERROR result."""
    validator = _get_validator()
    try:
        with path.open() as f:
            instance = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return [{
            "file": str(path),
            "layer": "schema",
            "category": "yaml_parse_error",
            "detail": "",
            "path": "",
            "message": str(e).splitlines()[0][:300],
        }]
    if instance is None:
        return [{
            "file": str(path),
            "layer": "schema",
            "category": "empty_file",
            "detail": "",
            "path": "",
            "message": "file parsed as None",
        }]

    target_class = infer_target_class(instance)
    try:
        report = validator.validate(instance, target_class=target_class)
    except Exception as e:  # noqa: BLE001 — surface anything weird as a row
        return [{
            "file": str(path),
            "layer": "schema",
            "category": "validator_crash",
            "detail": type(e).__name__,
            "path": "",
            "message": str(e)[:300],
        }]

    rows = []
    for result in report.results:
        if result.severity != Severity.ERROR:
            continue
        category, detail = classify(result.message)
        rows.append({
            "file": str(path),
            "layer": "schema",
            "category": category,
            "detail": detail,
            "path": result.instance_index or "",
            "message": result.message[:300],
        })
    return rows


def _run_external_validator(cmd: list[str], path: Path, layer: str) -> list[dict]:
    """Run a CLI validator on a single file and capture ERROR lines into rows.

    Both `linkml-term-validator` and `linkml-reference-validator` emit lines
    that start with the LinkML severity marker (`[ERROR] ...` or `ERROR:...`).
    We capture anything matching that and turn it into a row.
    """
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, timeout=120, check=False
        )
    except subprocess.TimeoutExpired:
        return [{
            "file": str(path), "layer": layer, "category": "validator_timeout",
            "detail": "", "path": "", "message": f"{layer} validator timed out",
        }]
    out = (proc.stdout or "") + "\n" + (proc.stderr or "")
    rows: list[dict] = []
    for line in out.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("[ERROR]") or stripped.startswith("ERROR:") or "ERROR" in stripped.split()[:2]:
            msg = stripped[:300]
            rows.append({
                "file": str(path), "layer": layer, "category": "external_error",
                "detail": "", "path": "", "message": msg,
            })
    if proc.returncode != 0 and not rows:
        # Validator exited nonzero but emitted no parseable ERROR line; surface anyway.
        rows.append({
            "file": str(path), "layer": layer, "category": "external_error",
            "detail": f"rc={proc.returncode}", "path": "",
            "message": (out.strip()[:300] or f"{layer} validator returned {proc.returncode}"),
        })
    return rows


def _peek_target_class(path: Path) -> str:
    """Lightweight target-class inference for external validators
    (which take the class as a CLI flag, not as data).
    Same routing rule as the in-process validator's `infer_target_class`.
    """
    try:
        with path.open() as f:
            instance = yaml.safe_load(f)
    except (yaml.YAMLError, OSError):
        return "MediaRecipe"
    return infer_target_class(instance)


def validate_terms(path: Path, target_class: str) -> list[dict]:
    return _run_external_validator(
        [
            "uv", "run", "linkml-term-validator", "validate-data", str(path),
            "-s", str(SCHEMA_PATH), "-t", target_class,
            "--labels", "-c", str(OAK_CONFIG_PATH),
        ],
        path, "terms",
    )


def validate_references(path: Path, target_class: str) -> list[dict]:
    return _run_external_validator(
        [
            "uv", "run", "linkml-reference-validator", "validate", "data", str(path),
            "--schema", str(SCHEMA_PATH), "--target-class", target_class,
        ],
        path, "references",
    )


def validate_one_layered(path: Path, layers: tuple[str, ...]) -> list[dict]:
    """Run the configured set of validation layers on a single file.

    External validators (terms / references) need the target class as a CLI
    flag — peek the file once to route MediaRecipe vs SolutionRecipe so
    standalone solution records aren't false-failed against MediaRecipe.
    """
    rows: list[dict] = []
    target_class = _peek_target_class(path) if {"terms", "references"} & set(layers) else "MediaRecipe"
    if "schema" in layers:
        rows.extend(validate_one(path))
    if "terms" in layers:
        rows.extend(validate_terms(path, target_class))
    if "references" in layers:
        rows.extend(validate_references(path, target_class))
    return rows


def iter_yaml_files(paths: Iterable[Path]) -> list[Path]:
    out: list[Path] = []
    for p in paths:
        if p.is_file():
            out.append(p)
        elif p.is_dir():
            out.extend(sorted(p.rglob("*.yaml")))
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path,
                        help="Files or directories. Defaults to standard normalized_yaml subdirs.")
    parser.add_argument("--out", type=Path, default=Path("reports/instance_validation_failures.tsv"),
                        help="TSV output path.")
    parser.add_argument("--sample", type=int, metavar="N",
                        help="Validate only the first N files (after sorting). Useful for smoke tests.")
    parser.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 4) - 1),
                        help="Process pool size. Default: ncpu - 1.")
    parser.add_argument("--fail-on", choices=("error", "never"), default="error",
                        help="Exit non-zero policy. 'error' (default) exits 1 if any ERROR row was emitted.")
    parser.add_argument("--quiet", action="store_true",
                        help="Suppress per-file progress dots.")
    parser.add_argument("--layer", default="schema",
                        choices=("schema", "terms", "references", "all"),
                        help="Validation layer(s) to run. 'schema' (default) is the in-process "
                             "closed-schema check (fast). 'terms' and 'references' shell out to "
                             "linkml-term-validator / linkml-reference-validator per file and are "
                             "much slower at corpus scale. 'all' runs all three.")
    args = parser.parse_args()

    layers = (
        ("schema", "terms", "references")
        if args.layer == "all"
        else (args.layer,)
    )

    roots = args.paths or DEFAULT_ROOTS
    files = iter_yaml_files(roots)
    if args.sample:
        files = files[: args.sample]
    if not files:
        print("No YAML files found.", file=sys.stderr)
        return 2

    args.out.parent.mkdir(parents=True, exist_ok=True)

    print(f"Validating {len(files)} files with {args.workers} workers; "
          f"layers={','.join(layers)}; schema={SCHEMA_PATH}",
          file=sys.stderr)

    all_rows: list[dict] = []
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(validate_one_layered, p, layers): p for p in files}
        done = 0
        for fut in as_completed(futures):
            done += 1
            rows = fut.result()
            all_rows.extend(rows)
            if not args.quiet and done % 250 == 0:
                print(f"  {done}/{len(files)} files processed, {len(all_rows)} ERROR rows so far",
                      file=sys.stderr)

    # Sort for deterministic TSV output (avoids noisy diffs from worker scheduling).
    all_rows.sort(key=lambda r: (r["file"], r["layer"], r["path"], r["category"], r["message"]))
    with args.out.open("w", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["file", "layer", "category", "detail", "path", "message"],
            delimiter="\t",
            quoting=csv.QUOTE_MINIMAL,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(all_rows)

    by_cat: dict[tuple[str, str], int] = {}
    files_with_errors: set[str] = set()
    for row in all_rows:
        key = (row["layer"], row["category"])
        by_cat[key] = by_cat.get(key, 0) + 1
        files_with_errors.add(row["file"])

    print("", file=sys.stderr)
    print(f"=== validate-strict summary ===", file=sys.stderr)
    print(f"  files scanned:      {len(files)}", file=sys.stderr)
    print(f"  layers:             {','.join(layers)}", file=sys.stderr)
    print(f"  files with ERROR:   {len(files_with_errors)}", file=sys.stderr)
    print(f"  total ERROR rows:   {len(all_rows)}", file=sys.stderr)
    print(f"  TSV:                {args.out}", file=sys.stderr)
    if by_cat:
        print(f"  by layer/category:", file=sys.stderr)
        for (layer, cat), count in sorted(by_cat.items(), key=lambda kv: -kv[1]):
            print(f"    {layer:>10s} {cat:24s} {count:>8d}", file=sys.stderr)

    if args.fail_on == "error" and all_rows:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
