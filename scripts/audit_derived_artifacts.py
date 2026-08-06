#!/usr/bin/env python3
"""Inventory, classify and freshness-check tracked derived artifacts (#145).

A category move leaves a record's old path embedded in tracked artifacts that
nothing refreshes. Only the recipe indexes fail loudly (#125). The registry
(#144), the chebi report (#157) and two review manifests (#168) each rotted
silently and were found by someone going looking — six instances so far, and this
session added several more tracked reports to the pile.

## Why this is a script and not a table

#145 suggests recording the classification as "a short table in
`docs/DATA_LAYERS.md`". A static table listing derived artifacts would itself be a
derived artifact nobody refreshes — the seventh instance of the same bug. So the
classification is computed from the repo, and the tracked manifest it writes is
checked against a fresh computation by a test.

## The three kinds (from #157, which established that the remedy differs)

CURRENT_VIEW   Must match what its writer produces from today's corpus. Guarded by
               regenerating to a temp path and comparing. These are the ones a
               record move invalidates.

SNAPSHOT       A record of what was true when something ran: `reports/archive/*`,
               dated filenames, and the output of one-time `migrate_*` scripts.
               Refreshing these would falsify history, so they are deliberately
               NOT checked.

UNKNOWN        No writer found, or a writer whose purity is unestablished. NOT a
               failure — it is the honest state for an artifact nobody has
               classified yet, and listing them is the point. Silence here would
               imply coverage that does not exist.

## What "checkable" means

An artifact is freshness-checkable only if its writer takes `--out` and does not
touch the corpus. `migrate_*` scripts rewrite records; `propose_media_variant_links`
proposes links; `build_media_growth_review_html` builds HTML. Running those to
check a report would have side effects far beyond the check, which is exactly why
#168 did not verify its two manifests. Checkable artifacts are declared explicitly
below rather than guessed.

Usage::

    just audit-derived-artifacts             # inventory + classification
    just audit-derived-artifacts --check     # also verify CURRENT_VIEW freshness
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from artifact_writers import classify_file  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
DEFAULT_OUT = REPO / "data" / "import_tracking" / "derived_artifacts.tsv"

ARTIFACT_SUFFIX = re.compile(r"\.(tsv|json|csv)$")
# Script-name prefixes that mean "regenerates a view of the corpus".
GENERATOR = re.compile(r"(audit_|score_|triage_|report_|prioritize_|sample_|refresh_|generate_)")
DATED = re.compile(r"\d{4}-\d{2}-\d{2}|_\d{8}")

# Artifacts whose writer takes `--out` and does not mutate the corpus, so a
# freshness check can regenerate them to a temp path safely. Explicit, because
# "has --out" is not the same as "is safe to run": audit_composition_type also
# has --promote-semi-defined, and is only pure without it.
CHECKABLE: dict[str, list[str]] = {
    "data/import_tracking/reports/composition_type_conflicts.tsv":
        ["scripts/audit_composition_type.py"],
    "data/import_tracking/reports/concentration_plausibility.tsv":
        ["scripts/audit_concentration_plausibility.py"],
    "data/import_tracking/reports/filename_collisions.tsv":
        ["scripts/audit_filename_collisions.py"],
    "data/import_tracking/reports/selective_agent_mismatch.tsv":
        ["scripts/audit_selective_agent_mismatch.py"],
    "data/import_tracking/reports/review_need_ranking.tsv":
        ["scripts/score_review_need.py"],
    "data/import_tracking/reports/missing_compositions.tsv":
        ["scripts/triage_missing_compositions.py"],
    "data/import_tracking/reports/unparsed_compositions.tsv":
        ["scripts/report_unparsed_compositions.py"],
    # The one CONSUMED output of the content-review writer (read by
    # propose_media_variant_links); its json/groups/summary siblings had no reader
    # and were untracked (#168). --out writes just this .tsv, so the check is pure.
    "reports/media_content_review_manifest.tsv":
        ["scripts/build_media_content_review_manifest.py"],
}


def tracked_artifacts() -> list[str]:
    out = subprocess.run(["git", "ls-files"], capture_output=True, text=True,
                         cwd=REPO).stdout.split()
    return sorted(f for f in out if ARTIFACT_SUFFIX.search(f)
                  and (f.startswith("reports/") or f.startswith("data/")))


SELF = "scripts/audit_derived_artifacts.py"


def find_writers(artifact: str) -> list[str]:
    """Every script mentioning this artifact's basename.

    Returns ALL candidates, not the first. Nine artifacts have more than one, and
    first-match-wins resolved them arbitrarily: `culturemech_id_registry.tsv` has
    three (`refresh_id_registry`, `assign_culturemech_ids`, `id_utils`) and got the
    right one by alphabetical luck, while `media_content_review_manifest.tsv` has
    two genuinely different tools. Ambiguity a curator can see beats a confident
    wrong answer.

    Excludes this script. It names every CHECKABLE artifact, so it matched all of
    them — and sorted first for `unparsed_compositions.tsv`, making the manifest
    report the auditor as that report's writer (#204). A tool must not attribute
    artifacts to itself.
    """
    base = os.path.basename(artifact)
    res = subprocess.run(["grep", "-rl", "--include=*.py", "--", base, "scripts", "src"],
                         capture_output=True, text=True, cwd=REPO)
    return sorted(f for f in res.stdout.split() if f and f != SELF)


def classify(artifact: str, writer: str | None) -> tuple[str, str]:
    if artifact.startswith("reports/archive/"):
        return "SNAPSHOT", "archived"
    if DATED.search(os.path.basename(artifact)):
        return "SNAPSHOT", "dated filename"
    if writer is None:
        return "UNKNOWN", "no writer found"
    base = os.path.basename(writer)
    if base.startswith("migrate_"):
        return "SNAPSHOT", f"one-time migration ({base})"
    if artifact in CHECKABLE:
        return "CURRENT_VIEW", base
    if GENERATOR.match(base):
        return "CURRENT_VIEW", base
    return "UNKNOWN", f"writer purity unestablished ({base})"


def inventory() -> list[dict[str, str]]:
    rows = []
    for art in tracked_artifacts():
        mentions = find_writers(art)
        base = os.path.basename(art)
        # Grep cannot tell a reader from a writer: research_media.py READS the id
        # registry to build an index and appeared among its "writers" (#209). This
        # traces the binding through the module instead.
        writers = [m for m in mentions
                   if classify_file(REPO / m, base) == "yes"] or mentions
        # A declared checkable artifact's writer is known exactly; re-deriving it
        # by grep would be guessing at something already stated.
        declared = CHECKABLE.get(art)
        if declared:
            writers = [declared[0]] + [w for w in writers if w != declared[0]]
        # Classify from the REGENERATING writer when several touch the artifact.
        # `culturemech_id_registry.tsv` is written by assign_culturemech_ids (which
        # MINTS ids), refresh_id_registry (which rebuilds it) and id_utils. Taking
        # the alphabetically first made it UNKNOWN and lost a correct answer; the
        # refresher is the one that determines whether the file is current.
        primary = next((w for w in writers if GENERATOR.match(os.path.basename(w))),
                       writers[0] if writers else None)
        kind, why = classify(art, primary)
        confirmed = [m for m in mentions if classify_file(REPO / m, base) == "yes"]
        rows.append({
            "artifact": art,
            "kind": kind,
            "reason": why,
            "writes": "; ".join(confirmed),
            "mentioned_by": "; ".join(mentions),
            "freshness_checked": "yes" if art in CHECKABLE else "",
        })
    return rows


def check_freshness(rows: list[dict[str, str]]) -> list[str]:
    """Regenerate each checkable artifact to a temp path and compare."""
    stale = []
    for art, cmd in CHECKABLE.items():
        src = REPO / art
        if not src.is_file():
            stale.append(f"{art}: declared checkable but missing")
            continue
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td) / os.path.basename(art)
            res = subprocess.run(
                ["uv", "run", "python", *cmd, "--out", str(tmp)],
                capture_output=True, text=True, cwd=REPO)
            if res.returncode != 0 or not tmp.is_file():
                stale.append(f"{art}: regeneration failed ({res.stderr.strip()[:120]})")
                continue
            if tmp.read_bytes() != src.read_bytes():
                stale.append(f"{art}: STALE — differs from a fresh run")
    return stale


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--check", action="store_true",
                    help="Also regenerate every CURRENT_VIEW artifact and compare.")
    ap.add_argument("--refresh", action="store_true",
                    help="Regenerate the freshness-checked artifacts in place. This is "
                         "the one follow-up step after a bulk record move (#145), "
                         "instead of a checklist held in someone's head.")
    args = ap.parse_args(argv)

    rows = inventory()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=[
            "artifact", "kind", "reason", "writes", "mentioned_by",
            "freshness_checked"])
        w.writeheader()
        w.writerows(rows)

    from collections import Counter
    counts = Counter(r["kind"] for r in rows)
    print(f"Tracked derived artifacts: {len(rows)}")
    for k in ("CURRENT_VIEW", "SNAPSHOT", "UNKNOWN"):
        print(f"  {counts.get(k, 0):4d}  {k}")
    checked = sum(1 for r in rows if r["freshness_checked"])
    print(f"\n  {checked} of {counts.get('CURRENT_VIEW', 0)} CURRENT_VIEW artifacts are "
          f"freshness-checked.")
    print("  The rest have a writer that is not safe to run for a check (it mutates")
    print("  records, proposes links, or builds HTML) — see CHECKABLE in this script.")
    print(f"\nWrote {args.out.relative_to(REPO) if args.out.is_relative_to(REPO) else args.out}")

    if args.refresh:
        print("\nRegenerating freshness-checked artifacts in place...")
        failed = []
        for art, cmd in CHECKABLE.items():
            res = subprocess.run(["uv", "run", "python", *cmd, "--out", str(REPO / art)],
                                 capture_output=True, text=True, cwd=REPO)
            status = "ok" if res.returncode == 0 else "FAILED"
            if res.returncode != 0:
                failed.append(art)
            print(f"  {status:7s} {art}")
        if failed:
            print(f"\n{len(failed)} regeneration(s) failed.", file=sys.stderr)
            return 1
        print("\nReview the diff and commit it.")
        return 0

    if not args.check:
        return 0

    print("\nRegenerating CURRENT_VIEW artifacts to compare...")
    stale = check_freshness(rows)
    if stale:
        print(f"\n{len(stale)} artifact(s) are stale:", file=sys.stderr)
        for s in stale:
            print(f"  {s}", file=sys.stderr)
        print("\nRefresh with `just refresh-derived`.", file=sys.stderr)
        return 1
    print("All freshness-checked artifacts match a fresh run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
