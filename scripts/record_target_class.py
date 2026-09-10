#!/usr/bin/env python3
"""Print the LinkML class a record file validates against (#450).

A stock-solution record has the `SolutionRecipe` shape (`preferred_term`,
`composition`, an upstream `term`); everything else is a `MediaRecipe`. The
`just validate*` recipes hardcoded `MediaRecipe`, so a solution record was
checked against the wrong class and, with no `set -e`, the failure was
swallowed. The decision is `record_kinds.has_solution_shape`, the same one
`validate_strict` routes on, so the recipes cannot disagree with the gate.

Usage: record_target_class.py <record.yaml>   ->   SolutionRecipe | MediaRecipe
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from record_kinds import has_solution_shape  # noqa: E402


def target_class(record: object) -> str:
    return "SolutionRecipe" if has_solution_shape(record) else "MediaRecipe"


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    path = Path(argv[1])
    try:
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        print(f"error: cannot read {path}: {exc}", file=sys.stderr)
        return 1
    print(target_class(record))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
