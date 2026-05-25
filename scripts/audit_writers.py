#!/usr/bin/env python3
"""Audit YAML-writing scripts in CultureMech.

For every Python module under `scripts/` and `src/culturemech/{import,enrich,merge}`
that writes a YAML (looks for `yaml.dump`, `yaml.safe_dump`, or `.write_text(`
on a `.yaml` path), record:

  - target_kind: `recipe` (writes back to per-recipe YAML in
    data/normalized_yaml/), `report` (writes a manifest / report /
    log / analysis output), `mixed` (does both — typically importers
    that write recipes plus a sibling index), or `unknown` (couldn't
    classify from the script source).
  - appends to `curation_history`?
  - has a `--dry-run` flag?
  - calls `linkml-validate` (in any form) before writing?
  - is mentioned in `project.justfile` (i.e. wired into a target)?

TSV columns: path, writes_yaml, target_kind, appends_curation_history,
has_dry_run, validates_before_write, wired_into_just.

Use `target_kind` to scope follow-up work — `record_curation_event()`
adoption (G10) is meaningful only for `recipe` and `mixed` writers;
reports/manifests/logs aren't recipes and don't have a curation history.

Output: TSV to stdout (and via --out to a file).
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

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
    r"|write_validated_recipe\("  # G09 helper from culturemech.validation
)
# Heuristic for "writes back to a per-recipe YAML in data/normalized_yaml/"
# (i.e. would benefit from a CurationEvent) vs writes a report/manifest/index
# (where curation_history is meaningless because the target isn't a recipe).
_RECIPE_WRITER = re.compile(
    r"recipe_path\s*,\s*['\"]w['\"]"
    r"|yaml_file\s*,\s*['\"]w['\"]"
    r"|\(\s*p\s*,\s*['\"]w['\"]\)"
    r"|\(\s*path\s*,\s*['\"]w['\"]\)"
    r"|p\.write_text\("
    r"|output_path\s*=\s*self\.output_dir"  # mediadive solution importer
)
_REPORT_WRITER = re.compile(
    # Narrowly target report/manifest/log sinks. We deliberately do NOT
    # match a bare `output_path = ...` assignment because importers like
    # scripts/import_mediadive_solutions.py legitimately use that name
    # for the per-recipe YAML they emit — Copilot caught that on PR #26.
    r"args\.output\b"
    r"|args\.report\b"
    r"|out\.write_text\b"
    r"|report_file\b"
    r"|report_path\b"
    r"|log_file\b"
    r"|manifest\b"
    r"|\.tsv\b"
    r"|\.json\b"
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
    # write_validated_recipe is the G09 helper that wraps yaml.safe_dump.
    if "write_validated_recipe(" in text:
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
    # Categorize: a writer that *only* writes reports/manifests does not
    # benefit from CurationEvent — flag separately so G10 follow-ups stay
    # focused on actual recipe modifiers.
    recipe = bool(_RECIPE_WRITER.search(text))
    report = bool(_REPORT_WRITER.search(text))
    if recipe and not report:
        target = "recipe"
    elif report and not recipe:
        target = "report"
    elif recipe and report:
        target = "mixed"
    else:
        target = "unknown"
    return {
        "path": str(path),
        "writes_yaml": "yes",
        "target_kind": target,
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

    fields = ["path", "writes_yaml", "target_kind", "appends_curation_history",
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

    recipe_writers = [r for r in rows if r["target_kind"] in ("recipe", "mixed")]

    print("", file=sys.stderr)
    print(f"=== writers audit summary ({len(rows)} writers) ===", file=sys.stderr)
    print(f"  target kind:                recipe={count('target_kind', 'recipe')} "
          f"mixed={count('target_kind', 'mixed')} report={count('target_kind', 'report')} "
          f"unknown={count('target_kind', 'unknown')}", file=sys.stderr)
    print(f"  appends curation_history:   {count('appends_curation_history', 'yes')} / {len(rows)}",
          file=sys.stderr)
    print(f"  (recipe writers only) appends curation_history: "
          f"{sum(1 for r in recipe_writers if r['appends_curation_history']=='yes')} / {len(recipe_writers)}",
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
