#!/usr/bin/env python3
"""Flag composition tables that were never parsed, and prose sitting in name slots.

Two related ingestion failures, kept in one audit because they are found by the
same scan and a curator triaging one wants to see the other.

  NAME_IN_CONCENTRATION   `preferred_term` is empty and `concentration.value`
                          holds a chemical name — the two fields were swapped on
                          import. `NBRC_1003` carries
                          `preferred_term: ''` with
                          `concentration: {value: MgSO4·7H2O, unit: G_PER_L}`.
                          Unambiguous: a concentration value is never a formula.

  EMPTY_INGREDIENT_NAME   `preferred_term` is empty but the concentration looks
                          numeric. The name is simply lost. Superset of the
                          above; reported separately so the swap can be repaired
                          first, since it still carries the name to restore.

  UNPARSED_SOLUTION_TABLE `solutions[]` with `composition: []` and a name that is
                          a concatenated composition table
                          (`MgSO4·7H2O0.5g(NH4)2SO40.4gK2HPO40.2g...`). The whole
                          recipe was dropped into one string. Unlike the
                          ingredient cases this DOES reach the KGX export, because
                          solution ids are minted from `preferred_term` and need
                          no grounding (#294): all 31 become a node, each carrying
                          one `has_part` edge — 31 garbage nodes and 31 edges,
                          verified against the export output.

  PROSE_AS_INGREDIENT     An ingredient row whose name is a preparation
                          instruction — `Make up to 1 litre with deionised water.
                          For agar, add` carrying the 15 G_PER_L that belongs to
                          the agar which followed it (#273). These are ungrounded,
                          so they produce no KGX edge; the harm is to ingredient
                          counts and composition analysis.

Scope and honesty about it:

  - Read-only. Nothing is rewritten. Recovery for the first three means going
    back to the pre-normalization payload — the concatenated string has lost its
    delimiters (`MgSO4·7H2O0.5g` has no separator between name and amount), so
    re-splitting it here would be guesswork on hydrate dots and multi-digit
    numbers.
  - PROSE_AS_INGREDIENT uses an instruction-verb list AND a length-or-sentence
    test. Either alone is far noisier: on the current corpus the loose filters
    flag 1,192 ingredient values, the conjunction flags 44, and spot-checking
    says the 44 are all real.
  - Solution RECORDS are not excluded, and their reagents are genuinely scanned:
    the 4,784 standalone stock-solution records keep their rows in a top-level
    `composition:` rather than `ingredients:`, so an ingredients-only scan would
    silently skip 35,009 rows while appearing to cover the corpus. A name in a
    concentration field is wrong wherever it appears. The `location` column says
    which of the three places each finding came from.

Usage::

    just audit-unparsed-composition
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
NORMALIZED = REPO_ROOT / "data" / "normalized_yaml"
DEFAULT_OUT = (REPO_ROOT / "data" / "import_tracking" / "reports"
               / "unparsed_composition.tsv")

# A concentration value we accept as a number: plain, ranged, or bounded, plus
# the explicit VARIABLE placeholder the schema allows.
_NUMERIC_VALUE = re.compile(r"^\s*[<>~]?\s*[\d.]+\s*(?:-\s*[\d.]+)?\s*$")

# Verbs and phrases that only appear in preparation prose, never in a reagent
# name. Deliberately not a general English-verb test: `Add` is the signal, and a
# reagent called "Sodium acetate" must not trip anything here.
_INSTRUCTION = re.compile(
    r"\b(add|adjust|make up|dissolve|autoclav|steriliz|mix|store|prepare"
    r"|bring to|filter|boil|incubat|dispense|supplement|final concentration"
    r"|per litre|per liter|after|before|if needed|as needed)\b",
    re.IGNORECASE,
)

# A concatenated composition table, identified by its actual signature: an amount
# and unit welded directly onto the next reagent's name — the `0.5g(` in
# `MgSO4·7H2O0.5g(NH4)2SO40.4g`. That is what a table looks like once the
# delimiters are gone.
#
# The obvious cheaper test — a letter followed by a digit — does not work. It
# matches hydrate forms (`MgSO4·7H2O`) and, at this length, catalogue
# cross-references: `MINERAL MEDIUM FOR HYDROGENOPHILUS ISLANDICUM (see Medium
# [M803])` trips it on `M803`. Those are legitimate solution entries that simply
# point at another record, and flagging 14 of them as corrupt would be a false
# accusation. The amount+unit rule separates the two cleanly — 31 tables kept,
# all 14 cross-references dropped — and is stable: every real table has at least
# four such runs, so thresholds of 1 through 4 select exactly the same set.
_GLUED_AMOUNT = re.compile(r"\d(?:\.\d+)?\s*(?:mg|ml|kg|g|L|l)(?=[A-Za-z(])")
_MIN_GLUED_RUNS = 2
_MIN_TABLE_LEN = 60

# Long enough that a reagent name is implausible. Kept generous: the longest
# genuine names in the corpus are around 70 characters.
_PROSE_MIN_LEN = 80


def _holds_a_name(value: Any) -> bool:
    """True when a concentration value is text that cannot be a concentration.

    Absence is NOT evidence of a swap. An ingredient with an empty name and no
    concentration block at all has simply lost its name; reporting
    NAME_IN_CONCENTRATION for it would point a curator at a field that does not
    exist. Nothing in the corpus is shaped that way today, which is exactly why
    the distinction has to be pinned rather than left to chance.

    A non-string is already a number, or malformed in a way this audit does not
    claim to diagnose; either way it is not a reagent name.
    """
    if value is None or not isinstance(value, str):
        return False
    text = value.strip()
    if not text or text.casefold() == "variable":
        return False
    return not _NUMERIC_VALUE.match(text)


def _looks_like_prose(name: str) -> bool:
    """Instruction verb AND (long or sentence-shaped). See module docstring."""
    if not _INSTRUCTION.search(name):
        return False
    return len(name) > _PROSE_MIN_LEN or ". " in name or name.rstrip().endswith(".")


def _looks_like_table(name: str) -> bool:
    if len(name) < _MIN_TABLE_LEN:
        return False
    return len(_GLUED_AMOUNT.findall(name)) >= _MIN_GLUED_RUNS


def _reagent_rows(doc: dict[str, Any]) -> Iterator[tuple[str, dict[str, Any]]]:
    """Every reagent-shaped row in a record, wherever it lives.

    Three locations, and missing any of them leaves the gate porous:

      ``ingredients[]``            media records.
      ``composition[]``            top level, on the 4,784 standalone stock-
                                   solution records — 35,009 rows that an
                                   ingredients-only scan never sees.
      ``solutions[].composition[]``  reagents nested inside an inline solution.

    The rows are the same shape in all three, so they get the same detectors.
    """
    for row in doc.get("ingredients") or []:
        if isinstance(row, dict):
            yield "ingredients", row
    for row in doc.get("composition") or []:
        if isinstance(row, dict):
            yield "composition", row
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        for row in solution.get("composition") or []:
            if isinstance(row, dict):
                yield "solutions[].composition", row


def audit_record(doc: dict[str, Any], path: Path) -> Iterator[dict[str, str]]:
    """Every finding in one record."""
    record_id = str(doc.get("id") or "")
    rel = str(path.relative_to(REPO_ROOT)) if path.is_relative_to(REPO_ROOT) else str(path)

    for location, ingredient in _reagent_rows(doc):
        name = ingredient.get("preferred_term")
        concentration = ingredient.get("concentration") or {}
        value = concentration.get("value")
        unit = concentration.get("unit")
        base = {
            "file_path": rel,
            "record_id": record_id,
            "location": location,
            "value": "" if value is None else str(value),
            "unit": "" if unit is None else str(unit),
        }

        if isinstance(name, str) and not name.strip():
            if _holds_a_name(value):
                yield {
                    **base, "finding": "NAME_IN_CONCENTRATION", "name": "",
                    "detail": "preferred_term is empty and the concentration "
                              "value holds what looks like a reagent name",
                }
            else:
                yield {
                    **base, "finding": "EMPTY_INGREDIENT_NAME", "name": "",
                    "detail": "preferred_term is empty; the name is not "
                              "recoverable from this record",
                }
            continue

        if isinstance(name, str) and _looks_like_prose(name):
            yield {
                **base, "finding": "PROSE_AS_INGREDIENT", "name": name,
                "detail": "preparation instruction parsed as an ingredient; its "
                          "concentration belongs to the reagent that followed it",
            }

    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        name = solution.get("preferred_term")
        if not isinstance(name, str) or not name:
            continue
        if (solution.get("composition") or []):
            continue
        if _looks_like_table(name):
            yield {
                "file_path": rel, "record_id": record_id,
                "location": "solutions[].preferred_term",
                "finding": "UNPARSED_SOLUTION_TABLE", "name": name,
                "value": "", "unit": "",
                "detail": "composition is empty and the name is a concatenated "
                          "composition table; reaches the KGX export as a node",
            }


def audit(normalized_dir: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(normalized_dir.glob("*/*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError):
            continue
        if isinstance(doc, dict):
            rows.extend(audit_record(doc, path))
    return rows


FINDINGS = (
    "NAME_IN_CONCENTRATION",
    "EMPTY_INGREDIENT_NAME",
    "UNPARSED_SOLUTION_TABLE",
    "PROSE_AS_INGREDIENT",
)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument(
        "--max-allowed", type=int, default=None,
        help="Exit non-zero when total findings exceed this baseline. Gates NEW "
             "defects without blocking on the existing backlog, the same "
             "convention as audit-concentration-plausibility. Lower it as the "
             "backlog is repaired; never raise it to make a run pass.",
    )
    ap.add_argument(
        "--max-exported", type=int, default=None,
        help="Exit non-zero when more than N UNPARSED_SOLUTION_TABLE findings "
             "exist. The sharper gate: these are the only ones that reach the "
             "KGX export, so a rise means new garbage nodes in the graph.",
    )
    args = ap.parse_args(argv if argv is not None else sys.argv[1:])

    rows = audit(args.normalized_dir)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh, delimiter="\t",
            fieldnames=["finding", "location", "file_path", "record_id", "name",
                        "value", "unit", "detail"],
        )
        writer.writeheader()
        writer.writerows(rows)

    tally = Counter(row["finding"] for row in rows)
    records = len({row["file_path"] for row in rows})
    print(f"Scanned {args.normalized_dir}")
    print(f"Findings: {len(rows)} across {records} records\n")
    for finding in FINDINGS:
        print(f"  {finding:24s} {tally.get(finding, 0)}")

    exported = tally.get("UNPARSED_SOLUTION_TABLE", 0)
    print(f"\nReaching the KGX export: {exported} "
          "(UNPARSED_SOLUTION_TABLE only — the ingredient findings are "
          "ungrounded, so they emit no edge)")

    rel = (args.out.relative_to(REPO_ROOT)
           if args.out.is_relative_to(REPO_ROOT) else args.out)
    print(f"\nWrote {rel}")
    print("\nRead-only. Recovery means returning to the pre-normalization "
          "payload: the concatenated string has lost the delimiters between "
          "reagent and amount, so re-splitting it here would be guesswork.")

    failed = False
    if args.max_allowed is not None and len(rows) > args.max_allowed:
        print(f"\nFAIL: {len(rows)} findings > baseline {args.max_allowed}. An "
              f"import or edit has introduced unparsed composition beyond the "
              f"known backlog; see the report for which records.", file=sys.stderr)
        failed = True
    if args.max_exported is not None and exported > args.max_exported:
        print(f"\nFAIL: {exported} unparsed solution tables > baseline "
              f"{args.max_exported}. These become garbage nodes in the KGX "
              f"export.", file=sys.stderr)
        failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
