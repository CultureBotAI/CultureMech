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


SEMI_DEFINED_MAX_G_PER_L = 0.5


def _chebi_id(ing: dict[str, Any]) -> str | None:
    for key in ("mediaingredientmech_chebi_term", "term"):
        term = ing.get(key)
        if isinstance(term, dict) and isinstance(term.get("id"), str) \
                and term["id"].startswith("CHEBI:"):
            return term["id"]
    return None


def semi_defined_candidate(doc: dict[str, Any]) -> tuple[bool, str]:
    """Is this UNDEFINED record actually SEMI_DEFINED, on evidence rather than assumption?

    SEMI_DEFINED is "predominantly defined ... supplemented with a small amount of
    one or more undefined components". Both halves must be shown, and the second
    is the hard one.

    Presence of an undefined component is provable; ABSENCE is not, because the
    name list is finite. So "predominantly defined" is not inferred from "no other
    undefined component matched" — that would be the #158 asymmetry run backwards,
    and an unrecognised extract at 10 g/L would be silently promoted. Instead every
    other ingredient must carry a CHEBI id, which is positive evidence that it is a
    known chemical.
    """
    hits = undefined_components(doc)
    if len(hits) != 1:
        return False, "not exactly one undefined component"
    mass = undefined_mass(hits)
    if mass is None:
        return False, "undefined component is unquantified"
    if mass >= SEMI_DEFINED_MAX_G_PER_L:
        return False, f"{mass:g} g/L is not 'a small amount'"
    others = [i for i in doc.get("ingredients") or []
              if isinstance(i, dict) and i not in hits]
    if not others:
        return False, "no other ingredients to be predominantly defined"
    ungrounded = [str(i.get("preferred_term")) for i in others if not _chebi_id(i)]
    if ungrounded:
        return False, f"{len(ungrounded)} other ingredient(s) not CHEBI-grounded"
    return True, f"{mass:g} g/L {hits[0].get('preferred_term')}; {len(others)} others all CHEBI-grounded"


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
    ap.add_argument("--promote-semi-defined", action="store_true",
                    help="Promote UNDEFINED records to SEMI_DEFINED where the evidence "
                         "supports it: exactly one undefined component below "
                         "0.5 g/L, and every other ingredient CHEBI-grounded.")
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

    if args.promote_semi_defined:
        promoted = 0
        skipped: dict[str, int] = {}
        # Near-misses are the actionable subset: exactly one small undefined
        # component, held back only because a sibling ingredient is ungrounded.
        # Either that sibling needs grounding (record becomes promotable) or it is
        # an unrecognised extract (word list needs the name) — both decidable per
        # record, and neither findable if only aggregate counts are printed (#172).
        report_rows: list[dict[str, str]] = []
        for path in sorted(args.normalized_dir.rglob("*.yaml")):
            try:
                doc = yaml.safe_load(path.read_text(errors="replace"))
            except (yaml.YAMLError, OSError):
                continue
            if not isinstance(doc, dict) or is_solution_record(doc):
                continue
            current = str(doc.get("composition_type"))
            # Include records already promoted, so the report is IDEMPOTENT. Scanning
            # only UNDEFINED means a re-run drops every promoted row and the artifact
            # silently changes shape between the promoting run and the next one.
            if current not in ("UNDEFINED", "SEMI_DEFINED"):
                continue
            ok, why = semi_defined_candidate(doc)
            hits = undefined_components(doc)
            if ok:
                if current == "UNDEFINED":
                    promoted += restamp(path, "SEMI_DEFINED")
                report_rows.append({
                    "file_path": str(path.relative_to(args.normalized_dir)),
                    "record_id": str(doc.get("id") or ""),
                    "verdict": "PROMOTED",
                    "detail": why,
                    "ungrounded_siblings": "",
                })
                continue
            skipped[why.split(";")[0]] = skipped.get(why.split(";")[0], 0) + 1
            if "not CHEBI-grounded" not in why:
                continue  # only near-misses are worth a row
            others = [i for i in doc.get("ingredients") or []
                      if isinstance(i, dict) and i not in hits]
            report_rows.append({
                "file_path": str(path.relative_to(args.normalized_dir)),
                "record_id": str(doc.get("id") or ""),
                "verdict": "CURATOR: ground the sibling, or add it to the undefined list",
                "detail": why,
                "ungrounded_siblings": "; ".join(
                    str(i.get("preferred_term")) for i in others if not _chebi_id(i)),
            })

        semi_out = args.out.with_name(args.out.stem.replace("_conflicts", "") + "_semi_defined.tsv")
        semi_out.parent.mkdir(parents=True, exist_ok=True)
        with semi_out.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, delimiter="\t", fieldnames=[
                "file_path", "record_id", "verdict", "detail", "ungrounded_siblings"])
            w.writeheader()
            w.writerows(report_rows)

        near = sum(1 for r in report_rows if r["verdict"].startswith("CURATOR"))
        print(f"\nPromoted {promoted} UNDEFINED record(s) -> SEMI_DEFINED.")
        print(f"Near-misses held back only by an ungrounded sibling: {near}")
        print("Not promoted, by reason:")
        for why, n in sorted(skipped.items(), key=lambda kv: -kv[1])[:6]:
            print(f"  {n:5d}  {why}")
        print(f"\nWrote {_display(semi_out)}")
        return 0

    if not args.apply:
        print("\nReport only. Re-run with --apply to restamp the unambiguous ones.")
        return 0

    changed = sum(restamp(r["_path"], "UNDEFINED") for r in clear)
    print(f"\nRestamped {changed} record(s) DEFINED -> UNDEFINED.")
    print(f"Left {len(borderline) + len(unmeasured)} for curation — see the report.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
