#!/usr/bin/env python3
"""Regenerate or verify corpus statistics in README and the landing page."""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BEGIN = "<!-- BEGIN GENERATED CORPUS STATS -->"
END = "<!-- END GENERATED CORPUS STATS -->"


def yaml_count(path: Path) -> int:
    """Count YAML records recursively beneath path."""
    return sum(1 for candidate in path.rglob("*.yaml") if candidate.is_file())


def corpus_counts(normalized_dir: Path, merged_dir: Path) -> tuple[dict[str, int], int]:
    """Read one count snapshot shared by the README and landing page."""
    for directory in (normalized_dir, merged_dir):
        if not directory.is_dir():
            raise ValueError(f"Corpus directory does not exist: {directory}")
    categories = {
        directory.name: yaml_count(directory)
        for directory in normalized_dir.iterdir()
        if directory.is_dir() and not directory.name.startswith(".")
    }
    return categories, yaml_count(merged_dir)


def _render_readme_stats(categories: dict[str, int], merged_total: int) -> str:
    normalized_total = sum(categories.values())
    rows = "\n".join(f"| {name} | {count:,} |" for name, count in sorted(categories.items()))
    return f"""{BEGIN}
The tracked corpus currently contains **{normalized_total:,} normalized records** and **{merged_total:,} merged records**.

| Normalized category | Records |
| --- | ---: |
{rows}
| **Total normalized** | **{normalized_total:,}** |
| **Total merged** | **{merged_total:,}** |
{END}"""


def render_stats(normalized_dir: Path, merged_dir: Path) -> str:
    """Render the canonical, deterministic README statistics block."""
    return _render_readme_stats(*corpus_counts(normalized_dir, merged_dir))


def render_landing_stats(categories: dict[str, int], merged_total: int) -> str:
    """Render landing cards from the same corpus counts as README."""
    normalized_total = sum(categories.values())
    populated_categories = sum(count > 0 for count in categories.values())
    return f"""{BEGIN}
      <div class="stat"><b>{normalized_total:,}</b><span>normalized records</span></div>
      <div class="stat"><b>{merged_total:,}</b><span>merged records</span></div>
      <div class="stat"><b>{populated_categories}</b><span>populated categories</span></div>
      {END}"""


def _replace_stats(text: str, block: str, document: str) -> str:
    if text.count(BEGIN) != 1 or text.count(END) != 1:
        raise ValueError(f"{document} must contain exactly one generated corpus-stats block")
    start, end = text.index(BEGIN), text.index(END)
    if start >= end:
        raise ValueError(f"{document} corpus-stats markers must be in BEGIN/END order")
    return text[:start] + block + text[end + len(END) :]


def replace_stats(readme_text: str, block: str) -> str:
    """Replace exactly one generated block, preserving the rest of README."""
    return _replace_stats(readme_text, block, "README")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path, default=ROOT / "README.md")
    parser.add_argument(
        "--landing",
        type=Path,
        help="landing HTML (defaults to app/index.html for the repository README)",
    )
    parser.add_argument("--normalized-dir", type=Path, default=ROOT / "data" / "normalized_yaml")
    parser.add_argument("--merged-dir", type=Path, default=ROOT / "data" / "merge_yaml" / "merged")
    parser.add_argument("--check", action="store_true", help="fail instead of updating stale text")
    args = parser.parse_args()

    # Preserve custom --readme-only callers: they must explicitly select a
    # landing file instead of accidentally rewriting this checkout's app.
    landing = args.landing
    if landing is None and args.readme.resolve() == (ROOT / "README.md").resolve():
        landing = ROOT / "app" / "index.html"

    try:
        categories, merged_total = corpus_counts(args.normalized_dir, args.merged_dir)
        outputs = [(args.readme, _render_readme_stats(categories, merged_total))]
        if landing is not None:
            if landing.resolve() == args.readme.resolve():
                raise ValueError("README and landing page must be different files")
            outputs.append((landing, render_landing_stats(categories, merged_total)))
        updates = []
        # Validate every input and marker block before writing either output.
        for path, block in outputs:
            current = path.read_text()
            expected = _replace_stats(current, block, str(path))
            if current != expected:
                updates.append((path, expected))
    except (OSError, ValueError) as error:
        parser.error(str(error))

    if not updates:
        print("Corpus statistics are current.")
        return 0
    if args.check:
        stale = ", ".join(str(path) for path, _ in updates)
        print(f"Corpus statistics are stale in {stale}; run `just update-readme-stats`.")
        return 1
    for path, expected in updates:
        path.write_text(expected)
        print(f"Updated {path}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
