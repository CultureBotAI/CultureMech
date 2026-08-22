#!/usr/bin/env python3
"""Regenerate or verify the README corpus-statistics block."""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BEGIN = "<!-- BEGIN GENERATED CORPUS STATS -->"
END = "<!-- END GENERATED CORPUS STATS -->"


def yaml_count(path: Path) -> int:
    """Count YAML records recursively beneath path."""
    return sum(1 for candidate in path.rglob("*.yaml") if candidate.is_file())


def render_stats(normalized_dir: Path, merged_dir: Path) -> str:
    """Render the canonical, deterministic README statistics block."""
    categories = {
        directory.name: yaml_count(directory)
        for directory in normalized_dir.iterdir()
        if directory.is_dir() and not directory.name.startswith(".")
    }
    normalized_total = sum(categories.values())
    merged_total = yaml_count(merged_dir)
    rows = "\n".join(f"| {name} | {count:,} |" for name, count in sorted(categories.items()))
    return f"""{BEGIN}
The tracked corpus currently contains **{normalized_total:,} normalized records** and **{merged_total:,} merged records**.

| Normalized category | Records |
| --- | ---: |
{rows}
| **Total normalized** | **{normalized_total:,}** |
| **Total merged** | **{merged_total:,}** |
{END}"""


def replace_stats(readme_text: str, block: str) -> str:
    """Replace exactly one generated block, preserving the rest of README."""
    if readme_text.count(BEGIN) != 1 or readme_text.count(END) != 1:
        raise ValueError("README must contain exactly one generated corpus-stats block")
    prefix, remainder = readme_text.split(BEGIN, 1)
    _, suffix = remainder.split(END, 1)
    return prefix + block + suffix


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path, default=ROOT / "README.md")
    parser.add_argument("--normalized-dir", type=Path, default=ROOT / "data" / "normalized_yaml")
    parser.add_argument("--merged-dir", type=Path, default=ROOT / "data" / "merge_yaml" / "merged")
    parser.add_argument("--check", action="store_true", help="fail instead of updating stale text")
    args = parser.parse_args()

    try:
        current = args.readme.read_text()
        expected = replace_stats(current, render_stats(args.normalized_dir, args.merged_dir))
    except (OSError, ValueError) as error:
        parser.error(str(error))

    if current == expected:
        print("README corpus statistics are current.")
        return 0
    if args.check:
        print("README corpus statistics are stale; run `just update-readme-stats`.")
        return 1
    args.readme.write_text(expected)
    print(f"Updated {args.readme}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
