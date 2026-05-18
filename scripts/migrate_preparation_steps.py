#!/usr/bin/env python3
"""Migrate `preparation_steps[*].instruction` -> `action` + `description`.

Schema (PreparationStep) requires:
    action: PreparationActionEnum    (required)
    description: string              (required)

Legacy records carry a single free-text `instruction` field instead.
This script splits each `instruction` into:
    action      = best-guess PreparationActionEnum value from keyword matching
    description = the original instruction text (verbatim)

Heuristics scan the text for keywords (autoclave -> AUTOCLAVE, dissolve ->
DISSOLVE, pH -> ADJUST_PH, etc.). Anything that doesn't match a keyword
defaults to MIX (the most generic action). The `description` field
preserves the full original text either way, so no information is lost
even when the action is a guess.

Each migrated file gets a CurationEvent. Re-runs are no-ops.

Usage:
    python scripts/migrate_preparation_steps.py [--dry-run]
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
from pathlib import Path
from typing import Any

import yaml

CURATOR = "migrate_preparation_steps.py"
ACTION = "MIGRATED_PREPARATION_STEPS"
DEFAULT_ROOT = "data/normalized_yaml"
DEFAULT_ACTION = "MIX"

# Order matters — earlier patterns win. Most-specific terms first.
ACTION_PATTERNS: list[tuple[str, list[str]]] = [
    ("FILTER_STERILIZE", [r"filter\s*steril", r"0\.22\s*[μu]m", r"membrane\s*filter"]),
    ("AUTOCLAVE",        [r"autoclav", r"121\s*°?c", r"steam\s*steril"]),
    ("ADJUST_PH",        [r"adjust\s*ph", r"\bph\s*adjust", r"ph\s*to\s*\d", r"\bph\b.{0,40}\b(naoh|hcl|koh)\b"]),
    ("ADD_AGAR",         [r"\badd.{0,20}agar\b", r"solidif.*agar"]),
    ("POUR_PLATES",      [r"pour\s*plat", r"petri\s*dish"]),
    ("ALIQUOT",          [r"\baliquot", r"divid.{0,20}portion"]),
    ("STORE",            [r"\bstor[ae]\b", r"storage"]),
    ("DISSOLVE",         [r"\bdissolv", r"complete.{0,20}dissolution"]),
    ("HEAT",             [r"\bheat\b", r"\bwarm\b", r"\bboil"]),
    ("COOL",             [r"\bcool\b", r"chill"]),
    ("MIX",              [r"\bmix\b", r"\bstir\b", r"\bshak", r"agitate"]),
]


def now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def guess_action(text: str) -> str:
    lower = text.lower()
    for action, patterns in ACTION_PATTERNS:
        for pat in patterns:
            if re.search(pat, lower):
                return action
    return DEFAULT_ACTION


def migrate_one(path: Path, dry_run: bool) -> int:
    """Return number of instruction entries migrated."""
    try:
        with path.open() as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError:
        return 0
    if not isinstance(data, dict):
        return 0
    steps = data.get("preparation_steps") or []
    migrated = 0
    for step in steps:
        if not isinstance(step, dict):
            continue
        if "instruction" in step and "action" not in step:
            text = step.pop("instruction")
            if not isinstance(text, str):
                text = str(text)
            step["action"] = guess_action(text)
            step["description"] = text
            migrated += 1
    if migrated == 0:
        return 0
    history = data.setdefault("curation_history", [])
    history.append({
        "timestamp": now_iso(),
        "curator": CURATOR,
        "action": ACTION,
        "notes": f"instruction->action+description for {migrated} step(s)",
    })
    if not dry_run:
        with path.open("w") as f:
            yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, width=80)
    return migrated


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=DEFAULT_ROOT)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()

    paths = sorted(Path(args.root).rglob("*.yaml"))
    total_steps = 0
    files_changed = 0
    action_dist: dict[str, int] = {}
    for p in paths:
        n = migrate_one(p, args.dry_run)
        if n:
            files_changed += 1
            total_steps += n
            if args.limit and files_changed >= args.limit:
                break

    # Re-read action distribution in updated files for diagnostics.
    if not args.dry_run and files_changed:
        for p in paths:
            try:
                d = yaml.safe_load(p.read_text())
            except yaml.YAMLError:
                continue
            if not isinstance(d, dict):
                continue
            for s in d.get("preparation_steps") or []:
                if isinstance(s, dict) and (a := s.get("action")):
                    action_dist[a] = action_dist.get(a, 0) + 1

    mode = "[DRY RUN] " if args.dry_run else ""
    print(f"{mode}scanned: {len(paths)}, files migrated: {files_changed}, "
          f"step rewrites: {total_steps}", file=sys.stderr)
    if action_dist:
        print("  resulting action distribution (all PreparationSteps):", file=sys.stderr)
        for a, c in sorted(action_dist.items(), key=lambda kv: -kv[1]):
            print(f"    {a:20s} {c:>6d}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
