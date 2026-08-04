#!/usr/bin/env python3
"""Triage media that carry no usable composition (#175).

Classifies every record with nothing to work from, so the backlog can be attacked
by cause rather than one record at a time. REPORT ONLY — see "the trap" below for
why the obvious repair is not attempted.

## The count is 428, not 463

The original issue measured `ingredients` alone. A stock-supplied component is
recorded under `solutions`, so 35 records that look empty are not: they carry
their whole composition there. The same oversight made 15 of 17 findings in #181
false positives, so it is worth stating plainly — a record's composition lives in
`ingredients` AND `solutions`, and any audit that reads one slot will invent a
defect.

## What the 428 are

  327  KOMODO ModelSEED, no ingredients and no solutions
  101  a single placeholder ingredient ("See source for composition")

**202 of the 428 are named like a stock solution rather than a medium** —
"Trace element solution (medium 929)", "Solution C, medium 1275",
"10 x M9 salts". These are not media missing a composition; they are solutions
imported as media records. `record_kinds.is_solution_record()` does not catch them
because it keys on a `term.id` prefix these records lack, deliberately: an id
prefix is an explicit provenance assertion, whereas guessing from a name would
also swallow genuine media.

## The trap — why 217 records are NOT auto-repairable

Those names cite a medium number, and 217 of them resolve to a composition file in
`data/raw/mediadive/compositions/`. Applying it would be wrong.

"Trace element solution (medium 1072)" means *the trace element solution defined
inside medium 1072* — not medium 1072 itself. And `dsmz_1072`'s composition is the
whole medium: KH2PO4, MgSO4, NH4Cl, KCl, CaCl2, Na-acetate, yeast extract,
casamino acids, NaCl at 15 g/L — plus a line reading "Trace element solution (see
below) 2.0ml", which is the thing actually wanted.

So the mapping that looks like a 217-record fix would write an entire medium's
recipe into each solution record. That is #166 at scale: plausible, round-trips,
validates, and wrong.

The local dump is independently unreliable. `dsmz_929` records its `medium_name`
as "NaCl" (its first component), and `dsmz_1275` lists "Solution A:" as a 0.65 g
component — a section header parsed as a chemical. It is
`extraction_method: pdf_tabular_parsing` output, not a curated source.

Recovering these needs the sub-solution block within each medium's DSMZ record,
which the local extraction does not preserve.

Usage::

    just triage-missing-compositions
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_kinds import is_solution_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
MEDIADIVE_COMPOSITIONS = REPO / "data" / "raw" / "mediadive" / "compositions"
DEFAULT_OUT = REPO / "data" / "import_tracking" / "reports" / "missing_compositions.tsv"

PLACEHOLDER = re.compile(
    r"see\s+source|refer\s+to|not\s+specified|composition\s+not\s+available|"
    r"contact\s+source|proprietary", re.I)

# "Trace element solution (medium 929)", "Solution C, medium 1275", "10 x M9 salts",
# "Phosphate buffer (10x) (medium 1341)".
#
# Matches the word "solution" directly rather than enumerating the reagents that
# may precede it. An earlier version listed trace element / vitamin / mineral /
# salts and missed 34 records — "Amino acid solution", "Haemin solution",
# "Chelated iron solution", "Na-sesquicarbonate solution" (#194). The reagent list
# was never going to be completable; the word "solution" is the signal.
# `mixture` and the SL-nn / SL8 series are the same thing under another word:
# "Vitamin mixture (medium 1001)", "Trace elements SL-12".
SOLUTION_NAMED = re.compile(
    r"\bsolutions?\b|\bbuffer\b|\bstock\b|\bmixture\b|\bSL-?\d+\b|"
    r"^\s*\d+\s*x\b|\(\s*\d+\s*x\s*\)", re.I)
NAME_CITES_MEDIUM = re.compile(r"\bmedium\s+(\d+)\b", re.I)


def composition_terms(doc: dict[str, Any]) -> tuple[list[dict], list[dict]]:
    ings = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    sols = [s for s in doc.get("solutions") or [] if isinstance(s, dict)]
    return ings, sols


def has_no_usable_composition(doc: dict[str, Any]) -> str | None:
    """Return the kind of emptiness, or None when the record is fine."""
    ings, sols = composition_terms(doc)
    if not ings and not sols:
        return "no ingredients and no solutions"
    if sols:
        return None
    names = [str(i.get("preferred_term") or "") for i in ings]
    if len(ings) <= 1 and any(PLACEHOLDER.search(n) for n in names):
        return "placeholder ingredient only"
    return None


def _mediadive_ids() -> set[str]:
    if not MEDIADIVE_COMPOSITIONS.is_dir():
        return set()
    out = set()
    for f in os.listdir(MEDIADIVE_COMPOSITIONS):
        m = re.match(r"dsmz_(\d+)_composition\.json$", f)
        if m:
            out.add(m.group(1))
    return out


def triage_parsed(records: list[tuple[str, dict[str, Any]]],
                  mediadive_ids: set[str] | None = None) -> list[dict[str, str]]:
    """Pure function over parsed records, so tests need no fixture files."""
    if mediadive_ids is None:
        mediadive_ids = _mediadive_ids()
    rows: list[dict[str, str]] = []
    for rel, doc in records:
        if not isinstance(doc, dict) or is_solution_record(doc):
            continue
        kind = has_no_usable_composition(doc)
        if not kind:
            continue
        name = str(doc.get("original_name") or doc.get("name") or "")
        notes = str(doc.get("notes") or "")
        source = (m.group(1).strip() if (m := re.search(r"Source:\s*([^|\n]+)", notes))
                  else "")
        looks_like_solution = bool(SOLUTION_NAMED.search(name))
        cited = NAME_CITES_MEDIUM.search(name)
        # Recorded, NOT proposed as a fix: the cited medium is the one the solution
        # is defined INSIDE, so its composition is the whole medium (see docstring).
        cites = cited.group(1) if cited else ""
        rows.append({
            "file_path": rel,
            "record_id": str(doc.get("id") or ""),
            "name": name,
            "kind": kind,
            "source": source[:40],
            "looks_like_a_solution": "yes" if looks_like_solution else "",
            "name_cites_medium": cites,
            "cited_medium_in_local_dump": "yes" if cites in mediadive_ids and cites else "",
        })
    rows.sort(key=lambda r: (r["kind"], r["source"], r["file_path"]))
    return rows


def collect(normalized: Path = NORMALIZED) -> list[dict[str, str]]:
    records = []
    for path in sorted(normalized.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        records.append((str(path.relative_to(normalized)), doc))
    return triage_parsed(records)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--max-allowed", type=int, default=None,
                    help="Exit 1 if more than N records lack a composition.")
    args = ap.parse_args(argv)

    rows = collect(args.normalized_dir)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=[
            "file_path", "record_id", "name", "kind", "source",
            "looks_like_a_solution", "name_cites_medium",
            "cited_medium_in_local_dump"])
        w.writeheader()
        w.writerows(rows)

    from collections import Counter
    print(f"Records with no usable composition: {len(rows)}\n")
    for k, v in Counter(r["kind"] for r in rows).most_common():
        print(f"  {v:5d}  {k}")
    print("\nby source:")
    for k, v in Counter(r["source"] or "(none)" for r in rows).most_common(6):
        print(f"  {v:5d}  {k}")
    sol = [r for r in rows if r["looks_like_a_solution"]]
    print(f"\n  {len(sol)} are named like a stock SOLUTION, not a medium — these are "
          f"mis-typed\n      records rather than media with a missing recipe.")
    cited = [r for r in rows if r["cited_medium_in_local_dump"]]
    print(f"  {len(cited)} cite a medium number present in the local mediadive dump.")
    print("      NOT auto-repairable: the cited medium is the one the solution is")
    print("      defined INSIDE, so its composition is the whole medium. Applying it")
    print("      would write a full recipe into a solution record (#166 at scale).")
    print(f"\nWrote {args.out.relative_to(REPO) if args.out.is_relative_to(REPO) else args.out}")

    if args.max_allowed is not None and len(rows) > args.max_allowed:
        print(f"\nFAIL: {len(rows)} exceeds --max-allowed {args.max_allowed}",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
