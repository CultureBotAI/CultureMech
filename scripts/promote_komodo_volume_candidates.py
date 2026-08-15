#!/usr/bin/env python3
"""Promote KOMODO volume candidates the composition confirms, sharpen the rest (#262).

#261 resolved KOMODO-sourced cocktails through their base medium number and, where the
fetched medium's NAME disagreed with the record's, wrote the addition volume as a
`concentration_candidate` rather than asserting it. 41 records landed there. The
counterevidence said the identification "rests on the medium number alone".

That was too pessimistic, and the corpus contains the evidence to settle it. Comparing a
record's composition against the fetched medium's:

  * comparing compound NAMES discriminates nothing -- anaerobic DSMZ media share a
    backbone (salts, trace elements, vitamins, bicarbonate, sulfide), so even unrelated
    media score ~0.97;
  * comparing VALUES separates them completely. Measured against its own resolved medium
    a record scores 1.00 over 15-47 shared compounds; against three unrelated media,
    0.00.

Run over the 41, that splits cleanly with a wide gap and nothing in between:

  28 records   1.00 agreement over 15-47 compounds  -> the fetched medium IS where these
                                                       numbers came from
  13 records   <=0.96                               -> compounds genuinely differ

So the name disagreements are overwhelmingly upstream RENAMES, not #244 collisions.
KOMODO 294 -- the record that motivated the whole guard, `PELOBACTER ACIDIGALLICI` here
and `SYNTROPHUS HQGo1` upstream -- reproduces medium 294 across 30 of 30 compounds at
identical values. Same medium, different name.

What this does:

  promote   perfect agreement over >= MIN_SHARED_COMPOUNDS: rewrite the candidate as an
            asserted `concentration`. Never touches a solution that already HAS a
            `concentration` -- promotion fills a gap, it does not overwrite.
  sharpen   otherwise: leave the candidate unasserted and replace the counterevidence
            with the measured disagreement, which tells a curator far more than a name
            mismatch does.

Read-only by default; `--apply` writes via record_io with a curation event.

Usage::

    just promote-komodo-candidates                    # report
    just promote-komodo-candidates --limit 1 --apply  # canary
    just promote-komodo-candidates --apply
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

from fetch_komodo_base_volumes import (  # noqa: E402
    SPREAD_NOTE, composition_agreement, composition_confirms,
)
from fetch_mediadive_solution_volumes import fetch_medium  # noqa: E402
from record_io import write_record  # noqa: E402

from culturemech.curate.curation_event import record_curation_event  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
KOMODO_VOLUMES = REPO / "data" / "import_tracking" / "reports" / "komodo_base_volumes.json"
BARE_ID = re.compile(r"^\d+[a-z]?$")


def promote_doc(doc: dict[str, Any], base: str, ratio: float, shared: int,
                md_name: str, main: int = 0) -> tuple[int, int]:
    """Update this record in place. Returns (promoted, sharpened) solution counts."""
    confirmed = composition_confirms(ratio, shared, main)
    promoted = sharpened = 0
    for sol in doc.get("solutions") or []:
        if not isinstance(sol, dict):
            continue
        cands = sol.get("concentration_candidates")
        if not cands:
            continue
        cand = next((c for c in cands
                     if c.get("basis") == "CROSS_MEDIUM_INFERENCE"), None)
        if not cand:
            continue
        if confirmed:
            # Promotion fills a gap; it must never overwrite a stated value.
            if "concentration" in sol:
                continue
            sol["concentration"] = {"value": cand["value"], "unit": cand["unit"]}
            sol.pop("concentration_candidates", None)
            sol["preparation_notes"] = re.sub(
                r"addition volume NOT asserted.*",
                f"volume from medium {base}'s own MediaDive recipe, identified by this "
                f"record reproducing that medium's composition exactly ({shared}/{shared} "
                f"shared compounds at identical values, {main} of them from the main "
                f"solution) despite the upstream rename to "
                f"{md_name!r} (#262).",
                str(sol.get("preparation_notes") or ""))
            promoted += 1
        else:
            cand["counterevidence"] = (
                f"Not confirmed as medium {base}: {ratio:.0%} of the {shared} shared "
                f"compounds carry the same value ({main} shared with that medium's main "
                f"solution). A record that IS the medium scores 100%, with at least 5 "
                f"main-solution compounds. " + SPREAD_NOTE)
            sharpened += 1
    return promoted, sharpened


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="Write. Default is report-only.")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--delay", type=float, default=0.25)
    args = ap.parse_args(argv)

    if not KOMODO_VOLUMES.is_file():
        print(f"Run `just fetch-komodo-volumes` first — {KOMODO_VOLUMES.name} is missing.",
              file=sys.stderr)
        return 1
    data = json.loads(KOMODO_VOLUMES.read_text())

    targets = [(rel, info) for rel, info in sorted(data.items())
               if info.get("volume_basis") == "CROSS_MEDIUM_INFERENCE"
               and info.get("additions")
               and BARE_ID.fullmatch(str(info.get("komodo_key") or ""))]
    print(f"KOMODO records whose volume is a candidate on a bare medium id: {len(targets)}")

    cache: dict[str, Any] = {}
    promoted_recs = sharpened_recs = 0
    changed = 0
    for rel, info in targets:
        path = NORMALIZED / rel
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        if not isinstance(doc, dict) or not doc.get("solutions"):
            continue
        base = info["mediadive_id"]
        if base not in cache:
            cache[base] = fetch_medium(base)
            time.sleep(args.delay)
        medium = cache[base]
        if not medium:
            continue
        ratio, shared, main = composition_agreement(doc, medium)
        md_name = str((medium.get("medium") or {}).get("name") or "")
        p, s = promote_doc(doc, base, ratio, shared, md_name, main)
        if not (p or s):
            continue
        changed += 1
        promoted_recs += bool(p)
        sharpened_recs += bool(s)
        verdict = "PROMOTE" if p else "sharpen"
        print(f"  {verdict} {rel[:44]:46s} medium {base:>5s} "
              f"{ratio:5.0%} of {shared:2d} shared ({main:2d} main-solution)")
        if args.apply:
            record_curation_event(
                doc, curator="promote_komodo_volume_candidates.py",
                action=("ASSERTED_VOLUME_FROM_COMPOSITION_MATCH" if p
                        else "SHARPENED_VOLUME_COUNTEREVIDENCE"),
                notes=(f"This record reproduces MediaDive medium {base} "
                       f"({md_name!r}) across {shared} shared compounds at "
                       f"{ratio:.0%} identical values, {main} of them from that "
                       f"medium's main solution."
                       + (f" That identifies the medium despite the name difference, so "
                          f"its stated addition volume is now asserted rather than "
                          f"proposed (#262)." if p else
                          f" That is short of the exact agreement required to assert the "
                          f"volume, so it stays a candidate (#262).")),
                changes=(f"{p} volume(s) promoted to concentration; "
                         f"{s} candidate(s) re-evidenced"))
            write_record(path, doc)
        if args.limit and changed >= args.limit:
            break

    print(f"\n{promoted_recs} record(s) had a volume PROMOTED to an assertion; "
          f"{sharpened_recs} kept a candidate with sharper counterevidence.")
    if not args.apply:
        print("Report only. Re-run with --apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
