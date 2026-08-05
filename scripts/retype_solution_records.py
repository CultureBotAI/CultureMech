#!/usr/bin/env python3
"""Mark stock solutions that were imported as media records (#175).

202 records under `data/normalized_yaml/` are stock solutions, not media: "Trace
element solution (medium 929)", "Solution C, medium 1275", "10 x M9 salts",
"Vitamin mixture (medium 1001)". They came in through the KOMODO ModelSEED import,
which **flattened** each solution's contents into its parent medium's ingredient
list and left the solution itself as an empty stub — `KOMODO_1072_PSEUDO...` has no
`solutions:` at all but lists `MnCl2 x 4 H2O`, `FeSO4 x 7 H2O` and `Biotin`
directly, which is what upstream cites as "Trace element solution (see below)".

So their composition is not missing from the corpus. It has been absorbed into the
parent, and these are leftover stubs. They are not media with an absent recipe,
and counting them as such overstated #175 by nearly half.

## Why `record_kind` and not an id

`is_solution_record()` normally keys on a `term.id` prefix, an upstream provenance
assertion. These records have none, and the id they DO carry cannot be borrowed:
their `mediadive.medium:N` values collide coincidentally with unrelated entries in
the solutions namespace. `100x Vitamin solution` carries `mediadive.medium:3145`,
and solution 3145 is "SODIUM CHLORIDE". Measured across all 202: **3** have a
name-agreeing solution id, **170** would assert a false identity, 29 do not resolve
at all.

Writing `mediadive.solution:3145` onto a vitamin solution would be false chemistry
of the #166 kind — plausible, well-formed, and wrong. So the kind is asserted
directly in a slot a reviewer can see, rather than smuggled into a provenance
field.

## Why this is a script and not a read-time rule

Matching "*solution*" while reading would silently reclassify any genuine medium
named "Ringer's solution" or "Hank's balanced salt solution", and nobody would see
it happen. Written once, by this script, the decision appears in a diff.

Deleting these records was the alternative. It was rejected: their CultureMech ids
appear in 16 tracked artifacts, and CultureMech ids are meant to be stable, so
retirement creates dangling references while re-typing does not.

Report-only by default.

Usage::

    just retype-solution-records
    just retype-solution-records --apply
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_kinds import RECORD_KIND_SOLUTION, is_solution_record  # noqa: E402
from triage_missing_compositions import (  # noqa: E402
    SOLUTION_NAMED,
    has_no_usable_composition,
)

NORMALIZED = REPO / "data" / "normalized_yaml"


def candidates_from(records) -> list[tuple[Path, dict[str, Any]]]:
    """Candidates among already-parsed records.

    Split out so the corpus guard can use the session-scoped fixture instead of
    re-parsing all ~15,900 files, which cost 421s and made this the single
    slowest test in the suite (#191).

    BOTH conditions are required. A record named "...solution" that has a real
    ingredient list is a medium as far as this corpus is concerned — Ringer's and
    Hank's BSS are solutions by name but usable media by content, and re-typing
    them would remove them from media audits that should still see them.
    """
    out = []
    for path, doc in records:
        if not isinstance(doc, dict) or is_solution_record(doc):
            continue
        if not has_no_usable_composition(doc):
            continue
        name = str(doc.get("original_name") or doc.get("name") or "")
        if SOLUTION_NAMED.search(name):
            out.append((path, doc))
    return out


def candidates(normalized: Path = NORMALIZED) -> list[tuple[Path, dict[str, Any]]]:
    """Parse the corpus from disk, then select candidates."""
    records = []
    for path in sorted(normalized.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        records.append((path, doc))
    return candidates_from(records)


def stamp(path: Path, doc: dict[str, Any]) -> bool:
    """Insert `record_kind: SOLUTION`. Returns True if the file changed."""
    text = path.read_text()
    if re.search(r"^record_kind:", text, re.M):
        return False
    # After `category:` when present, else at the top — the id must stay first.
    new, n = re.subn(r"^(category:.*)$", rf"\1\nrecord_kind: {RECORD_KIND_SOLUTION}",
                     text, count=1, flags=re.M)
    if not n:
        new, n = re.subn(r"^(id:.*)$", rf"\1\nrecord_kind: {RECORD_KIND_SOLUTION}",
                         text, count=1, flags=re.M)
    if not n:
        return False
    path.write_text(new)
    return True


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    ap.add_argument("--apply", action="store_true",
                    help="Write record_kind: SOLUTION. Default is report-only.")
    args = ap.parse_args(argv)

    found = candidates(args.normalized_dir)
    print(f"Stock solutions imported as media records: {len(found)}\n")
    for path, doc in found[:25]:
        print(f"  {str(path.relative_to(args.normalized_dir))[:50]:52s} "
              f"{str(doc.get('original_name') or '')[:40]}")
    if len(found) > 25:
        print(f"  ... and {len(found) - 25} more")

    if not args.apply:
        print("\nReport only. Re-run with --apply to stamp record_kind: SOLUTION.")
        return 0

    written = sum(1 for path, doc in found if stamp(path, doc))
    print(f"\nStamped {written} record(s) with record_kind: {RECORD_KIND_SOLUTION}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
