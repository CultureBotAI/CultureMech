#!/usr/bin/env python3
"""Run the CultureMech KGX export through koza and write a node/edge TSV pair.

Why a driver script rather than a bare `koza transform` call (#294):

1. koza's CLI takes a **configuration YAML**, not a Python file. The old recipe
   passed `kgx_export.py`, so it had never run against koza 2.x.
2. koza does **no glob expansion**, and the corpus is 15,878 separate YAML
   records. The expanded list overflows ARG_MAX — `ls data/normalized_yaml/*/*.yaml`
   already fails — so the file list cannot go through `-i` on the command line.
   Passing it through koza's Python API sidesteps the shell entirely.
3. The node-dedup set is run-scoped and has to be cleared before each run.

Reports node and edge counts, and fails loudly if either file is missing or
holds only its header — a silent empty export is the failure mode #294 was
about.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RECORDS = REPO_ROOT / "data" / "normalized_yaml"
DEFAULT_OUTPUT = REPO_ROOT / "output" / "kgx"
CONFIG = REPO_ROOT / "src" / "culturemech" / "export" / "kgx.yaml"


def find_records(records_dir: Path) -> list[str]:
    """Every record YAML under `records_dir`, one directory deep.

    Matches the corpus layout `data/normalized_yaml/<category>/<slug>.yaml`. The
    sibling `*_index.json` files live at the top level and are not YAML, so the
    `*/*.yaml` shape excludes them without needing a filter.
    """
    return [str(p) for p in sorted(records_dir.glob("*/*.yaml"))]


def run(records_dir: Path, output_dir: Path, limit: int = 0) -> tuple[int, int]:
    """Run the transform. Returns (node_count, edge_count) excluding headers."""
    from koza.model.formats import OutputFormat
    from koza.runner import KozaRunner

    sys.path.insert(0, str(REPO_ROOT / "src"))

    files = find_records(records_dir)
    if not files:
        raise SystemExit(f"No record YAMLs found under {records_dir}")

    # No dedup reset here, and deliberately so. Koza loads the transform with
    # `importlib.util.spec_from_file_location` and, in its own words, "without
    # touching sys.modules" — so every run gets a brand-new module object with a
    # brand-new (empty) `_EMITTED_NODE_IDS`. Clearing the set through
    # `culturemech.export.kgx_export` would touch a different object entirely and
    # protect nothing.
    #
    # What matters is the invariant, not the mechanism: two runs in one process
    # must produce identical output. That is pinned by
    # `test_a_second_run_in_the_same_process_repeats_the_output`, which keeps
    # holding if koza ever starts caching modules — at which point
    # `reset_node_dedup()` becomes the fix, called from inside the transform
    # module rather than from here.

    print(f"Reading {len(files)} records from {records_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)

    _config, runner = KozaRunner.from_config_file(
        str(CONFIG),
        input_files=files,
        output_dir=str(output_dir),
        output_format=OutputFormat.tsv,
        row_limit=limit,
    )
    runner.run()

    return _verify(output_dir)


def _verify(output_dir: Path) -> tuple[int, int]:
    """Confirm both files exist and carry rows. Raises SystemExit otherwise."""
    counts = []
    for kind in ("nodes", "edges"):
        path = output_dir / f"culturemech_{kind}.tsv"
        if not path.exists():
            raise SystemExit(
                f"{path} was not written. TSVWriter only creates a file when the "
                f"matching property list is set in {CONFIG.name}."
            )
        rows = sum(1 for _ in path.open()) - 1  # discount the header
        if rows <= 0:
            raise SystemExit(f"{path} has a header but no rows.")
        counts.append(rows)
        print(f"  {_display(path)}: {rows:,} rows")
    return counts[0], counts[1]


def _display(path: Path) -> str:
    """Repo-relative when possible; absolute otherwise (canary runs write to /tmp)."""
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--records-dir", type=Path, default=DEFAULT_RECORDS)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Stop after N records (0 = all). Use for a canary run.",
    )
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])

    node_count, edge_count = run(args.records_dir, args.output_dir, args.limit)
    print(f"\n✓ KGX export complete: {node_count:,} nodes, {edge_count:,} edges")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
