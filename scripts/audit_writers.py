#!/usr/bin/env python3
"""Audit YAML-writing scripts in CultureMech.

For every Python module under `scripts/` and `src/culturemech/{import,enrich,merge}`
that writes a YAML (looks for `yaml.dump`, `yaml.safe_dump`, or `.write_text(`
on a `.yaml` path), record:

  - appends to `curation_history`?
  - has a `--dry-run` flag?
  - calls `linkml-validate` (in any form) before writing?
  - is mentioned in `project.justfile` (i.e. wired into a target)?

Output: TSV to stdout (and via --out to a file).
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(".").resolve()
SEARCH_DIRS = [
    Path("scripts"),
    Path("src/culturemech/import"),
    Path("src/culturemech/enrich"),
    Path("src/culturemech/merge"),
]

# Patterns
_WRITE_PATTERNS = [
    re.compile(r"yaml\.safe_dump\("),
    re.compile(r"yaml\.dump\("),
    # write_text on something that looks like a yaml path
    re.compile(r"\.write_text\("),  # broader; refined per-file below
]
_WRITE_YAML_HINT = re.compile(r"\.ya?ml['\"]|\.yaml\b")
_CURATION_APPEND = re.compile(
    r"curation_history.*?(append|\+=|\.insert)"
    r"|['\"]curator['\"]\s*:"
    r"|append_curation_event"
    r"|record_curation"
)
_DRY_RUN = re.compile(r"--dry[-_]run|dry_run\s*[:=]")
_VALIDATE_BEFORE_WRITE = re.compile(
    r"linkml[._-]?validate"
    r"|RecipeValidator"
    r"|validate_recipe\("
    r"|validator\.validate\("
)


def script_paths() -> list[Path]:
    out: list[Path] = []
    for d in SEARCH_DIRS:
        if not d.exists():
            continue
        out.extend(sorted(p for p in d.rglob("*.py") if "__pycache__" not in str(p)))
    return out


def looks_like_yaml_writer(text: str) -> bool:
    if "yaml.safe_dump(" in text or "yaml.dump(" in text:
        return True
    # `.write_text(` only counts if combined with a yaml hint nearby.
    if ".write_text(" in text and _WRITE_YAML_HINT.search(text):
        return True
    return False


def audit(path: Path, justfile_text: str) -> dict | None:
    try:
        text = path.read_text()
    except (UnicodeDecodeError, OSError):
        return None
    if not looks_like_yaml_writer(text):
        return None
    return {
        "path": str(path),
        "writes_yaml": "yes",
        "appends_curation_history": "yes" if _CURATION_APPEND.search(text) else "no",
        "has_dry_run": "yes" if _DRY_RUN.search(text) else "no",
        "validates_before_write": "yes" if _VALIDATE_BEFORE_WRITE.search(text) else "no",
        "wired_into_just": "yes" if path.stem in justfile_text or path.name in justfile_text else "no",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=None, help="TSV output path (default stdout)")
    args = ap.parse_args()

    justfile_text = (Path("project.justfile").read_text() + "\n"
                     + Path("justfile").read_text() if Path("justfile").exists()
                     else Path("project.justfile").read_text())

    rows: list[dict] = []
    for p in script_paths():
        row = audit(p, justfile_text)
        if row is not None:
            rows.append(row)

    fields = ["path", "writes_yaml", "appends_curation_history",
              "has_dry_run", "validates_before_write", "wired_into_just"]

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", lineterminator="\n")
            w.writeheader()
            for row in rows:
                w.writerow(row)
        print(f"Wrote {len(rows)} rows to {args.out}", file=sys.stderr)
    else:
        w = csv.DictWriter(sys.stdout, fieldnames=fields, delimiter="\t")
        w.writeheader()
        for row in rows:
            w.writerow(row)

    # Print summary
    def count(field: str, val: str) -> int:
        return sum(1 for r in rows if r[field] == val)

    print("", file=sys.stderr)
    print(f"=== writers audit summary ({len(rows)} writers) ===", file=sys.stderr)
    print(f"  appends curation_history:   {count('appends_curation_history', 'yes')} / {len(rows)}",
          file=sys.stderr)
    print(f"  has --dry-run:              {count('has_dry_run', 'yes')} / {len(rows)}",
          file=sys.stderr)
    print(f"  validates before write:     {count('validates_before_write', 'yes')} / {len(rows)}",
          file=sys.stderr)
    print(f"  wired into justfile:        {count('wired_into_just', 'yes')} / {len(rows)}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
