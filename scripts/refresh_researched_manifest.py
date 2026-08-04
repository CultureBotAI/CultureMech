#!/usr/bin/env python3
"""Refresh the tracked researched-media manifest from local Edison runs.

This is the one step that crosses from untracked (`research/media/`, gitignored)
to tracked (`data/import_tracking/researched_media.json`). Run it after a batch
of deep research, review the diff, commit it. Everything downstream —
`prioritize_deep_research_candidates.py` in particular — reads only the manifest,
which is what makes the committed priority reports reproducible (#121).

Entries are MERGED, never replaced: each machine sees only its own
`research/media/`, so overwriting would silently drop another contributor's
records. Nothing is ever removed by this script.

Usage::

    just refresh-researched-manifest              # merge local runs in
    just refresh-researched-manifest --dry-run    # show what would be added
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import researched_manifest as rmf  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--manifest", type=Path, default=rmf.DEFAULT_MANIFEST,
                    help="Tracked manifest to update.")
    ap.add_argument("--research-dir", type=Path, default=rmf.DEFAULT_RESEARCH_DIR,
                    help="Local (gitignored) Edison output directory to scan.")
    ap.add_argument("--axis-research-dir", type=Path, default=rmf.AXIS_RESEARCH_DIR,
                    help="Axis-classification output dir, also scanned. Its entries are\n"
                         "tagged kind=axis and excluded from the medium-level filter.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Report what would be added without writing.")
    args = ap.parse_args(argv)

    existing = rmf.load_manifest(args.manifest)
    discovered = (rmf.scan_research_dir(args.research_dir)
                  + rmf.scan_research_dir(args.axis_research_dir))
    merged, added = rmf.merge_entries(existing, discovered)

    print(f"Manifest:     {args.manifest}")
    print(f"Research dir: {args.research_dir}"
          f"{'' if args.research_dir.is_dir() else '  (missing — nothing to scan)'}")
    print(f"Existing entries: {len(existing)}")
    print(f"Completed runs found locally: {len(discovered)}")
    print(f"New entries: {len(added)}")

    if added:
        print()
        for e in added[:20]:
            print(f"  + {e['slug']}  ({e['job']})")
        if len(added) > 20:
            print(f"  + ... {len(added) - 20} more")

    if args.dry_run:
        print("\nDRY RUN — nothing written.")
        return 0

    if not added and existing:
        print("\nManifest already up to date; not rewriting.")
        return 0

    rmf.write_manifest(merged, args.manifest)
    print(f"\nWrote {len(merged)} entries -> {args.manifest}")
    print("Review the diff and commit it — this is what makes the priority "
          "reports reproducible for everyone else.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
