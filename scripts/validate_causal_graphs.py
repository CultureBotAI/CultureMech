#!/usr/bin/env python3
"""Validate CultureMech ``causal_graphs`` slots across YAML recipe files (Issue #658).

Checks:
1. LinkML closed-schema validation (ensuring ``CausalEdge``, ``CausalTerm``,
   and ``CausalPredicateEnum`` fields conform to ``culturemech.yaml``).
2. Semantic causal-graph rules in ``culturemech.validation.causal_graphs``:
   - valid ``CausalEdge.id`` syntax (``edge_...`` or ``CausalEdge:...``) and uniqueness
   - ontology-grounded ``subject_term`` and ``object_term`` CURIEs and non-empty labels
   - rejection of bare ingredient role tokens and self-loop edges
   - constrained ``predicate`` in ``CausalPredicateEnum``
   - ``organism_term`` NCBITaxon CURIE + non-empty label + enclosing taxon consistency
   - optional ``protein_terms`` canonical UniProtKB accessions + non-empty labels
   - mandatory claim-scoped ``evidence`` with valid reference, supporting enum,
     verbatim ``snippet``, and ``explanation``

Exits 0 when all inspected records pass, 1 when any ERROR finding is emitted.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Iterable
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from culturemech.validation.causal_graphs import (  # noqa: E402
    iter_causal_graph_lists,
    validate_recipe_causal_graphs,
)
from culturemech.validation.write_validated import validate_recipe  # noqa: E402


def _iter_yaml_files(paths: Iterable[Path]) -> list[Path]:
    files: list[Path] = []
    for p in paths:
        if p.is_dir():
            files.extend(
                child
                for child in sorted(p.rglob("*.yaml"))
                if not child.name.endswith("_index.yaml")
            )
        elif p.is_file():
            files.append(p)
    return files


def validate_files(
    paths: Iterable[Path],
    check_linkml: bool = True,
) -> tuple[int, int, list[tuple[Path, str, str, str]]]:
    """Validate YAML files and return (files_checked, edges_checked, failures)."""
    files = _iter_yaml_files(paths)
    failures: list[tuple[Path, str, str, str]] = []
    total_edges = 0

    for yaml_path in files:
        try:
            data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
        except Exception as exc:
            failures.append((yaml_path, "<root>", "YAML_PARSE_ERROR", str(exc)))
            continue

        if not isinstance(data, dict):
            continue

        lists = iter_causal_graph_lists(data)
        edge_count = sum(len(entries) for _, entries, _ in lists)

        has_non_list = (
            "causal_graphs" in data
            and not isinstance(data.get("causal_graphs"), (list, type(None)))
        ) or any(
            isinstance(org, dict)
            and "causal_graphs" in org
            and not isinstance(org.get("causal_graphs"), (list, type(None)))
            for org in (data.get("target_organisms") or [])
        )
        if edge_count == 0 and not has_non_list:
            continue

        total_edges += edge_count

        if check_linkml:
            for res in validate_recipe(data):
                if res.type != "causal_graphs":
                    failures.append((yaml_path, "<linkml>", "SCHEMA_VIOLATION", res.message))

        for issue in validate_recipe_causal_graphs(data):
            failures.append((yaml_path, issue.path, issue.rule, issue.message))

    return len(files), total_edges, failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[Path("data/normalized_yaml")],
        help="YAML files or directories to validate (default: data/normalized_yaml)",
    )
    parser.add_argument(
        "--skip-linkml",
        action="store_true",
        help="Run semantic causal-graph checks only without LinkML validator",
    )
    args = parser.parse_args(argv)

    files_checked, edges_checked, failures = validate_files(
        args.paths,
        check_linkml=not args.skip_linkml,
    )

    print(
        f"Checked {files_checked} YAML file(s), "
        f"{edges_checked} causal_graphs entry/entries; "
        f"errors={len(failures)}"
    )
    for yaml_path, field_path, rule, message in failures:
        print(f"ERROR\t{yaml_path}\t{field_path}\t{rule}\t{message}")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
