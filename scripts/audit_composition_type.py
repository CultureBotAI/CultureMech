#!/usr/bin/env python3
"""Find records whose composition_type contradicts their own ingredient list (#158).

`MediumCompositionTypeEnum.DEFINED` means "every component and its exact quantity
is known". 285 records assert it while listing yeast extract, peptone, tryptone
or similar — components that are chemically undefined by definition.

The error predates #148: the migration faithfully mapped `medium_type: DEFINED`
onto `composition_type: DEFINED` and invented nothing. What changed is that the
new slot's description states plainly what DEFINED means, which makes the
contradiction checkable.

## Only one direction is decidable

Detection rests on a finite list of undefined-component names, and that asymmetry
matters:

  * A record containing "yeast extract" **cannot** be DEFINED. Presence is proof.
  * A record containing none of these names is **not thereby** defined — the list
    is not exhaustive, and an unrecognised extract simply is not matched.

So this script only ever reports and repairs the DEFINED direction. The 1,894
UNDEFINED records with no recognised undefined component are NOT evidence of
mislabelling and are deliberately left alone; confirming those needs per-record
curation, not a word list.

## Choosing between UNDEFINED and SEMI_DEFINED

`SEMI_DEFINED` is "predominantly defined ... supplemented with a small amount of
one or more undefined components". That is a quantitative claim, so the total
undefined mass decides it, and the corpus splits cleanly:

    >= 5 g/L   239 records    unambiguously UNDEFINED
    1-5 g/L     31
    0.5-1 g/L    6
    < 0.5 g/L    8            plausibly SEMI_DEFINED
    unmeasured   1

`--apply` restamps only records at or above `--undefined-threshold` (default
5 g/L), where no reasonable reading calls 5 g/L of peptone "a small amount". The
remainder are reported for a curator: whether a 1-5 g/L supplement is SEMI_DEFINED
is a judgement about the medium, not something a threshold settles.

Usage::

    just audit-composition-type              # report
    just audit-composition-type --apply      # restamp the unambiguous ones
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_kinds import is_solution_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
DEFAULT_OUT = REPO / "data" / "import_tracking" / "reports" / "composition_type_conflicts.tsv"
DEFAULT_THRESHOLD = 5.0

# Chemically undefined components: biological extracts and enzymatic digests whose
# exact composition is not known. Matched on `preferred_term`, which is where the
# corpus carries the human-readable name.
UNDEFINED_COMPONENT = re.compile(
    r"\b(yeast extract|peptone|tryptone|trypticase|casamino|casein hydrolysate|"
    r"beef extract|meat extract|malt extract|liver extract|proteose|soytone|"
    r"brain[- ]heart|tryptic soy|rumen fluid|blood|serum)\b",
    re.I,
)


def _display(path: Path) -> str:
    """Show `path` relative to the repo when possible, else absolute.

    `Path.relative_to` raises when the target is outside REPO — which a caller
    passing --out to a scratch directory will hit. Crashing on the way to
    printing a filename would abort the run before --apply did anything.
    """
    try:
        return str(path.relative_to(REPO))
    except ValueError:
        return str(path)


def undefined_components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        ing for ing in doc.get("ingredients") or []
        if isinstance(ing, dict)
        and UNDEFINED_COMPONENT.search(str(ing.get("preferred_term") or ""))
    ]


def undefined_mass(ingredients: list[dict[str, Any]]) -> float | None:
    """Total g/L of the undefined components, or None if any is unquantified.

    None rather than a partial sum: a record with an unmeasured extract cannot be
    placed against a mass threshold, and guessing low would silently restamp it.
    """
    total = 0.0
    for ing in ingredients:
        conc = ing.get("concentration") or {}
        if str(conc.get("unit")) != "G_PER_L":
            return None
        try:
            total += float(conc.get("value"))
        except (TypeError, ValueError):
            return None
    return total


def audit(normalized: Path = NORMALIZED) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(normalized.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        if not isinstance(doc, dict) or is_solution_record(doc):
            continue
        if str(doc.get("composition_type")) != "DEFINED":
            continue
        hits = undefined_components(doc)
        if not hits:
            continue
        mass = undefined_mass(hits)
        rows.append({
            "file_path": str(path.relative_to(normalized)),
            "record_id": str(doc.get("id") or ""),
            "name": str(doc.get("name") or ""),
            "undefined_components": "; ".join(
                str(i.get("preferred_term")) for i in hits),
            "n_undefined": str(len(hits)),
            "undefined_g_per_l": "" if mass is None else f"{mass:g}",
            "_path": path,
            "_mass": mass,
        })
    return rows


def restamp(path: Path, new_value: str) -> bool:
    """Rewrite the composition_type line in place, leaving all other lines byte-identical."""
    text = path.read_text()
    updated, n = re.subn(r"^composition_type:.*$", f"composition_type: {new_value}",
                         text, count=1, flags=re.M)
    if n:
        path.write_text(updated)
    return bool(n)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--undefined-threshold", type=float, default=DEFAULT_THRESHOLD,
                    help="g/L of undefined components at or above which UNDEFINED is "
                         "unambiguous (default: 5.0)")
    ap.add_argument("--apply", action="store_true",
                    help="restamp records at or above the threshold to UNDEFINED")
    args = ap.parse_args(argv)

    rows = audit(args.normalized_dir)
    clear = [r for r in rows if r["_mass"] is not None and r["_mass"] >= args.undefined_threshold]
    borderline = [r for r in rows if r["_mass"] is not None and r["_mass"] < args.undefined_threshold]
    unmeasured = [r for r in rows if r["_mass"] is None]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=[
            "file_path", "record_id", "name", "undefined_components",
            "n_undefined", "undefined_g_per_l", "verdict"])
        w.writeheader()
        for r in rows:
            verdict = ("UNDEFINED" if r in clear
                       else "CURATOR: SEMI_DEFINED?" if r in borderline
                       else "CURATOR: unquantified")
            w.writerow({k: v for k, v in r.items() if not k.startswith("_")} | {"verdict": verdict})

    print(f"DEFINED records containing an undefined component: {len(rows)}")
    print(f"  >= {args.undefined_threshold:g} g/L — unambiguously UNDEFINED : {len(clear)}")
    print(f"  <  {args.undefined_threshold:g} g/L — curator call (SEMI_DEFINED?): {len(borderline)}")
    print(f"  unquantified undefined component            : {len(unmeasured)}")
    print(f"\nWrote {_display(args.out)}")

    if not args.apply:
        print("\nReport only. Re-run with --apply to restamp the unambiguous ones.")
        return 0

    changed = sum(restamp(r["_path"], "UNDEFINED") for r in clear)
    print(f"\nRestamped {changed} record(s) DEFINED -> UNDEFINED.")
    print(f"Left {len(borderline) + len(unmeasured)} for curation — see the report.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
