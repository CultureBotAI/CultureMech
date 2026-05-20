#!/usr/bin/env python3
"""Migrate `MediaRecipe.ph_range` from a free-text string to the
structured `PhRange` class introduced for G33 (audit follow-on).

Parsing rules (best-effort; preserves the original whenever a clean
parse isn't possible):

  "6.8-7.2"             -> {min: 6.8, max: 7.2}
  "7"                   -> {min: 7.0, max: 7.0}
  "6.5 - 7.0"           -> {min: 6.5, max: 7.0}
  "approximately 7.4"   -> {min: 7.4, max: 7.4, notes: "approximately 7.4"}
  "alkaline 9-10"       -> {min: 9.0, max: 10.0, notes: "alkaline 9-10"}
  "varies by species"   -> {notes: "varies by species"}

Each migrated file gets a CurationEvent via the G10 helper.
Re-runs are no-ops (ph_range value is a dict after the first migration).

Usage:
    python scripts/migrate_ph_range.py [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from culturemech.curate import record_curation_event  # noqa: E402

CURATOR = "migrate_ph_range.py"
ACTION = "MIGRATED_PH_RANGE"
DEFAULT_ROOT = "data/normalized_yaml"

# Match optional leading text + "<num>" or "<num> - <num>" + optional trailing text.
_RANGE_PATTERN = re.compile(
    r"(?P<low>\d+(?:\.\d+)?)\s*(?:[-–to]+\s*(?P<high>\d+(?:\.\d+)?))?"
)


def parse_ph_range(text: str) -> dict[str, Any]:
    """Parse a free-text pH-range string into a PhRange-shaped dict."""
    m = _RANGE_PATTERN.search(text)
    if not m:
        return {"notes": text}
    low = float(m.group("low"))
    high = float(m.group("high")) if m.group("high") else low
    # If the captured substring is not the whole string (e.g. has prefix /
    # suffix like "alkaline 9-10" or "approximately 7.4"), keep the original
    # text in notes so the qualifier isn't lost.
    captured = m.group(0)
    out: dict[str, Any] = {"min": low, "max": high}
    if captured.strip() != text.strip():
        out["notes"] = text
    return out


def migrate_one(path: Path, dry_run: bool) -> bool:
    try:
        with path.open() as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError:
        return False
    if not isinstance(data, dict):
        return False
    ph = data.get("ph_range")
    if not isinstance(ph, str):
        return False
    parsed = parse_ph_range(ph)
    data["ph_range"] = parsed
    record_curation_event(
        data,
        curator=CURATOR,
        action=ACTION,
        notes=f"ph_range {ph!r} -> {parsed!r}",
    )
    if not dry_run:
        with path.open("w") as f:
            yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, width=80)
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=DEFAULT_ROOT)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    paths = sorted(Path(args.root).rglob("*.yaml"))
    n = 0
    for p in paths:
        if migrate_one(p, args.dry_run):
            n += 1
    mode = "[DRY RUN] " if args.dry_run else ""
    print(f"{mode}scanned: {len(paths)}, migrated: {n}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
