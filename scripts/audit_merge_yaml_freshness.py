#!/usr/bin/env python3
"""Verify that data/merge_yaml/ is a current derivation of normalized_yaml (#215).

Every corpus quality gate in this repo — the plausibility detectors, the CHEBI
consistency check, id<->label correspondence — scans ``data/normalized_yaml/**``
only. ``data/merge_yaml/**`` holds 10,433 tracked media records that no gate
looks at. That is defended by a single load-bearing assumption, stated in
``chebi-consistency.yaml``:

    merge_yaml is always regenerated from normalized_yaml, so a defect there is a
    defect in normalized_yaml, which IS gated.

If that assumption holds, gating merge_yaml separately is redundant: every gate on
normalized_yaml transitively covers it. If it does NOT hold, merge_yaml is a
second, ungated corpus. The assumption had never been tested — this tool tests it.

## What it does

Regenerates merge_yaml from normalized_yaml into a temp directory with the same
merger the ``merge-recipes`` recipe uses, then diffs that fresh output against the
tracked corpus. Reports records present only in the tracked copy, only in a fresh
run, and those whose content differs.

## Why it is not a CI gate or a unit test

The merge fingerprints ~15.9k records and takes ~2.7 min, writing ~6.3k files.
That is too slow for the unit suite and for a per-PR gate. It is also, as of this
writing, DRIFTED — the tracked corpus was last regenerated in #98 (2026-07-20)
while normalized_yaml has changed through #202 (2026-08-04) — so wiring it green
into CI would require a maintainer to first regenerate the corpus and decide what
merge_yaml is for (see #215). This tool exists to make that drift measurable and
to give one command to re-check it, not to block CI on a decision that is not
ours to make. Only ``compare_corpora`` — the pure diff — is unit-tested.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
NORMALIZED_DIR = REPO / "data" / "normalized_yaml"
# The merge-recipes recipe writes here by default; this is the tracked corpus a
# fresh run must reproduce. merged_2026/ is a separate, older generation (#215).
TRACKED_MERGED_DIR = REPO / "data" / "merge_yaml" / "merged"

# Placeholder that replaces every curation-event timestamp before comparison.
_TS_SENTINEL = "<normalized-for-freshness-compare>"


def normalize_record(raw: bytes) -> bytes:
    """Blank curation-event timestamps so run time is not mistaken for drift.

    merge_recipes stamps ``datetime.now()`` into a MERGED_RECIPES curation event
    on every run (merge_recipes.py -> record_curation_event), so a raw byte
    compare would report every record as changed even immediately after a clean
    regenerate — the tool would be a false-positive machine and useless as an
    ongoing check. Normalizing only the timestamps leaves every substantive field
    (ingredients, concentrations, category, name, merged_from, the event's own
    curator/action/source) to drive the comparison. Records without a
    ``curation_history`` are returned untouched, so the common case pays no YAML
    round-trip.
    """
    try:
        doc = yaml.safe_load(raw)
    except yaml.YAMLError:
        return raw
    if not isinstance(doc, dict) or "curation_history" not in doc:
        return raw
    history = doc.get("curation_history")
    if isinstance(history, list):
        for event in history:
            if isinstance(event, dict) and "timestamp" in event:
                event["timestamp"] = _TS_SENTINEL
    return yaml.dump(doc, default_flow_style=False, allow_unicode=True,
                     sort_keys=False).encode("utf-8")


@dataclass
class DriftReport:
    """The difference between a fresh merge and the tracked corpus."""

    only_in_tracked: list[str] = field(default_factory=list)
    only_in_fresh: list[str] = field(default_factory=list)
    changed: list[str] = field(default_factory=list)
    unchanged: list[str] = field(default_factory=list)

    @property
    def is_current(self) -> bool:
        return not (self.only_in_tracked or self.only_in_fresh or self.changed)

    @property
    def drift_count(self) -> int:
        return len(self.only_in_tracked) + len(self.only_in_fresh) + len(self.changed)

    def summary(self) -> dict[str, int]:
        return {
            "tracked_total": len(self.only_in_tracked) + len(self.changed) + len(self.unchanged),
            "fresh_total": len(self.only_in_fresh) + len(self.changed) + len(self.unchanged),
            "only_in_tracked": len(self.only_in_tracked),
            "only_in_fresh": len(self.only_in_fresh),
            "changed": len(self.changed),
            "unchanged": len(self.unchanged),
        }


def compare_corpora(tracked_dir: Path, fresh_dir: Path) -> DriftReport:
    """Diff two directories of ``*.yaml`` records by filename and bytes.

    Pure and side-effect-free so it can be unit-tested without running the merge.
    A record is ``changed`` when the same filename exists in both but its content
    differs after :func:`normalize_record` (which blanks the volatile merge
    timestamp); ``only_in_*`` captures records the merge added or dropped.
    """
    tracked = {p.name: p for p in tracked_dir.glob("*.yaml")}
    fresh = {p.name: p for p in fresh_dir.glob("*.yaml")}
    report = DriftReport()
    for name in sorted(set(tracked) | set(fresh)):
        in_t, in_f = name in tracked, name in fresh
        if in_t and not in_f:
            report.only_in_tracked.append(name)
        elif in_f and not in_t:
            report.only_in_fresh.append(name)
        elif normalize_record(tracked[name].read_bytes()) != normalize_record(fresh[name].read_bytes()):
            report.changed.append(name)
        else:
            report.unchanged.append(name)
    return report


def regenerate(dest: Path) -> None:
    """Run the merger into ``dest`` exactly as ``just merge-recipes`` does."""
    dest.mkdir(parents=True, exist_ok=True)
    res = subprocess.run(
        ["uv", "run", "python", "-m", "culturemech.merge.merge_recipes",
         "--normalized-dir", str(NORMALIZED_DIR),
         "--output-dir", str(dest),
         "--stats-file", str(dest.parent / "merge_stats.json")],
        cwd=REPO,
    )
    if res.returncode != 0:
        raise SystemExit(f"merge_recipes failed with exit code {res.returncode}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tracked-dir", type=Path, default=TRACKED_MERGED_DIR,
                    help="The tracked merged corpus a fresh run must reproduce.")
    ap.add_argument("--json", action="store_true",
                    help="Emit the drift summary as JSON and nothing else.")
    ap.add_argument("--list", action="store_true",
                    help="Also print every drifted record name, not just counts.")
    args = ap.parse_args(argv)

    if not args.tracked_dir.is_dir():
        print(f"Tracked corpus not found: {args.tracked_dir}", file=sys.stderr)
        return 2

    with tempfile.TemporaryDirectory() as td:
        fresh_dir = Path(td) / "merged"
        if not args.json:
            print(f"Regenerating merge_yaml from {NORMALIZED_DIR.relative_to(REPO)} "
                  f"(this takes ~3 min)...", file=sys.stderr)
        regenerate(fresh_dir)
        report = compare_corpora(args.tracked_dir, fresh_dir)

    summary = report.summary()
    if args.json:
        print(json.dumps(summary, indent=2))
        return 0 if report.is_current else 1

    print("\n" + "=" * 60)
    print("merge_yaml derivation freshness (#215)")
    print("=" * 60)
    print(f"  tracked corpus : {summary['tracked_total']:>6} records  "
          f"({args.tracked_dir.relative_to(REPO)})")
    print(f"  fresh run      : {summary['fresh_total']:>6} records")
    print(f"  unchanged      : {summary['unchanged']:>6}")
    print(f"  changed        : {summary['changed']:>6}")
    print(f"  only in tracked: {summary['only_in_tracked']:>6}  (a fresh run would drop these)")
    print(f"  only in fresh  : {summary['only_in_fresh']:>6}  (a fresh run would add these)")
    if args.list:
        for label, names in (("only in tracked", report.only_in_tracked),
                             ("only in fresh", report.only_in_fresh),
                             ("changed", report.changed)):
            for n in names:
                print(f"    {label}: {n}")
    print()
    if report.is_current:
        print("CURRENT — merge_yaml matches a fresh derivation. Every gate on "
              "normalized_yaml transitively covers it.")
        return 0
    print(f"DRIFTED — {report.drift_count} records differ from a fresh derivation. "
          "merge_yaml is NOT a current view of normalized_yaml, so the corpus gates "
          "that scan normalized_yaml only do not cover it (#215).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
