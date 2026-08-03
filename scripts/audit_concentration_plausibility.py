#!/usr/bin/env python3
"""Flag implausible ingredient concentrations in the recipe corpus (#118).

Deep-research review surfaced a systematic ingestion defect: trace-element
**stock-solution** concentrations and unit slips stored as **final per-litre
medium** values. These are not research gaps, they are normalization bugs, and
any concentration-derived feature (ingredient UMAP, role inference, quantitative
KG edges) silently inherits them.

Three detectors, each keyed to a confirmed failure mode rather than a generic
outlier test:

  WATER_AS_VOLUME     Water at >= 1000 G_PER_L. A litre of medium cannot contain
                      2000 g of water as a solute — the value is a preparation
                      VOLUME (a 2-L prep) that was flattened into the ingredient
                      list. Confirmed on sulfolobus_medium_for_dsm_9790.

  TRACE_SALT_AS_STOCK Trace-element salts (Mn/Zn/Cu/Co/Ni/Mo/B/Se/W borates,
                      molybdates...) at >= 1 G_PER_L. Trace elements are used at
                      mg/L or below in final medium; g/L values are the
                      concentration of the STOCK SOLUTION the recipe draws from.
                      Confirmed on sulfolobus_medium_for_dsm_9790 (MnCl2 180,
                      Na2B4O7 450, ZnSO4 22 G_PER_L) and
                      TOGO_M1791_Pelobacter_acetylenicus_Medium.

  INDICATOR_UNIT_SLIP Redox indicators and vitamins in G_PER_L at >= 0.1. These
                      are used at mg/L; a G_PER_L value is a 1000x unit slip.
                      Confirmed on TOGO_M1796_Desulfovibrio_medium (Resazurin
                      1 G_PER_L, ~1000x too high).

Scope and honesty about it:

  - Read-only. Nothing is rewritten. The real repair for the trace-element case is
    to nest the cocktail under a stock `solution` object with an addition volume,
    which changes record structure and needs curation per record.
  - Only G_PER_L rows are examined (149,289 of 166,684 ingredient rows). The
    MILLIMOLAR / VARIABLE / MG_PER_L rows are not covered — a molar-basis
    plausibility check needs molecular weights and is a separate piece of work.
  - Stock-solution RECORDS are excluded via `record_kinds.is_solution_record`:
    high concentrations are correct there by definition. That exclusion is the
    single biggest false-positive guard.

Usage::

    just audit-concentration-plausibility
    # -> data/import_tracking/reports/concentration_plausibility.tsv
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Any, Iterator

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from record_kinds import is_solution_record  # noqa: E402

NORMALIZED = REPO_ROOT / "data" / "normalized_yaml"
DEFAULT_OUT = REPO_ROOT / "data" / "import_tracking" / "reports" / "concentration_plausibility.tsv"
CATEGORIES = ("bacterial", "archaea", "algae", "fungal", "specialized")

WATER_IDS = {"CHEBI:15377"}
WATER_RE = re.compile(r"\b(distilled\s+water|deionized\s+water|water|h2o|aqua)\b", re.I)
WATER_MIN_G_PER_L = 1000.0

# Trace-element cations/anions. Matched on the label because these rows are
# frequently ungrounded; the element token must appear as a chemical-formula
# prefix, not merely anywhere in the string.
TRACE_ELEMENT_RE = re.compile(
    r"^(na2b4o7|h3bo3|mncl2|mnso4|znso4|zncl2|cucl2|cuso4|cocl2|coso4|"
    r"nicl2|niso4|na2moo4|na2seo3|na2seo4|na2wo4|nh4_?vo3|alk\(so4\)2|"
    r"feso4|fecl3|fecl2|na2edta)\b",
    re.I,
)
TRACE_MIN_G_PER_L = 1.0

# Redox indicators and vitamins: used at mg/L or below in final medium.
INDICATOR_RE = re.compile(
    r"^(resazurin|resorufin|methylene\s*blue|phenol\s*red|bromocresol|"
    r"neutral\s*red|biotin|folic\s*acid|thiamine|riboflavin|pyridoxine|"
    r"cyanocobalamin|vitamin\s*b12|nicotinic\s*acid|pantothen|lipoic\s*acid|"
    r"p-?aminobenzoic)",
    re.I,
)
INDICATOR_MIN_G_PER_L = 0.1


def _term_id(ing: dict[str, Any]) -> str | None:
    for key in ("mediaingredientmech_chebi_term", "term"):
        t = ing.get(key)
        if isinstance(t, dict) and isinstance(t.get("id"), str) and t["id"]:
            return t["id"]
    return None


def _clean_label(name: str) -> str:
    """Strip hydrate suffixes so formula prefixes match: 'MnCl2 x 4 H2O' -> 'mncl2'."""
    s = (name or "").strip().lower()
    s = re.sub(r"\s*[·・x×*]\s*\d+\s*h2o\s*$", "", s)
    s = re.sub(r"\s*\.\s*\d+\s*h2o\s*$", "", s)
    return s.strip()


def check_ingredient(ing: dict[str, Any]) -> tuple[str, str] | None:
    """Return (finding, detail) when a row is implausible, else None."""
    conc = ing.get("concentration") or {}
    if str(conc.get("unit")) != "G_PER_L":
        return None
    try:
        value = float(conc.get("value"))
    except (TypeError, ValueError):
        return None
    if value <= 0:
        return None

    name = str(ing.get("preferred_term") or "")
    label = _clean_label(name)
    ident = _term_id(ing)

    if (ident in WATER_IDS or WATER_RE.search(label)) and value >= WATER_MIN_G_PER_L:
        return ("WATER_AS_VOLUME",
                f"{value:g} G_PER_L water — reads as a preparation volume, not a concentration")

    if TRACE_ELEMENT_RE.match(label) and value >= TRACE_MIN_G_PER_L:
        return ("TRACE_SALT_AS_STOCK",
                f"{value:g} G_PER_L trace-element salt — stock-solution magnitude, "
                f"final medium is normally mg/L or below")

    if INDICATOR_RE.match(label) and value >= INDICATOR_MIN_G_PER_L:
        return ("INDICATOR_UNIT_SLIP",
                f"{value:g} G_PER_L indicator/vitamin — normally mg/L; "
                f"likely a 1000x unit slip")

    return None


def iter_media(normalized_dir: Path) -> Iterator[tuple[Path, dict[str, Any]]]:
    for cat in CATEGORIES:
        d = normalized_dir / cat
        if not d.is_dir():
            continue
        for path in sorted(d.glob("*.yaml")):
            try:
                doc = yaml.safe_load(path.read_text())
            except (yaml.YAMLError, OSError):
                continue
            if not isinstance(doc, dict):
                continue
            # Stock-solution records legitimately carry stock magnitudes.
            if is_solution_record(doc):
                continue
            yield path, doc


def audit(normalized_dir: Path = NORMALIZED) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path, doc in iter_media(normalized_dir):
        for ing in doc.get("ingredients") or []:
            if not isinstance(ing, dict):
                continue
            hit = check_ingredient(ing)
            if not hit:
                continue
            finding, detail = hit
            conc = ing.get("concentration") or {}
            rows.append({
                "finding": finding,
                "file_path": str(path.relative_to(normalized_dir)),
                "record_id": str(doc.get("id") or ""),
                "ingredient": str(ing.get("preferred_term") or ""),
                "value": str(conc.get("value")),
                "unit": str(conc.get("unit")),
                "detail": detail,
            })
    return rows


COCKTAIL_MIN_ROWS = 3


def summarize_records(rows: list[dict[str, str]],
                      normalized_dir: Path) -> list[dict[str, str]]:
    """Roll findings up per record and mark flattened stock cocktails.

    A record carrying >=3 flagged vitamin/indicator rows, or >=3 flagged
    trace-salt rows, and NO `solutions:` block is a stock solution that was
    flattened into the ingredient list rather than nested with an addition
    volume. DSMZ_962a_THERMOVENABULUM_MEDIUM is the worked example: nine
    vitamins at exactly the DSMZ vitamin-solution stock concentrations
    (biotin 0.02, folic acid 0.02, pyridoxine-HCl 0.1, thiamine 0.05 G_PER_L ...)
    sitting directly in `ingredients:`.

    This is the actionable subset — it names the records where the repair is
    "nest this cocktail under a solution object", not "fix one typo".
    """
    by_record: dict[str, list[dict[str, str]]] = {}
    for r in rows:
        by_record.setdefault(r["file_path"], []).append(r)

    out: list[dict[str, str]] = []
    for file_path, found in sorted(by_record.items()):
        counts = {k: 0 for k in ("WATER_AS_VOLUME", "TRACE_SALT_AS_STOCK",
                                 "INDICATOR_UNIT_SLIP")}
        for r in found:
            counts[r["finding"]] += 1
        try:
            doc = yaml.safe_load((normalized_dir / file_path).read_text()) or {}
        except (yaml.YAMLError, OSError):
            doc = {}
        has_solutions = bool(doc.get("solutions"))
        cocktail = (
            not has_solutions
            and (counts["INDICATOR_UNIT_SLIP"] >= COCKTAIL_MIN_ROWS
                 or counts["TRACE_SALT_AS_STOCK"] >= COCKTAIL_MIN_ROWS)
        )
        out.append({
            "file_path": file_path,
            "record_id": found[0]["record_id"],
            "flagged_rows": str(len(found)),
            "water_as_volume": str(counts["WATER_AS_VOLUME"]),
            "trace_salt_as_stock": str(counts["TRACE_SALT_AS_STOCK"]),
            "indicator_unit_slip": str(counts["INDICATOR_UNIT_SLIP"]),
            "has_solutions_block": "yes" if has_solutions else "no",
            "flattened_cocktail": "yes" if cocktail else "no",
        })
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--max-allowed", type=int, default=None,
                    help="Exit non-zero when flagged rows exceed this baseline. Gates "
                         "NEW defects without blocking on the existing backlog — the "
                         "same convention as `check-chebi-grounding`. Lower it as the "
                         "backlog is repaired; never raise it to make a run pass.")
    args = ap.parse_args(argv)

    rows = audit(args.normalized_dir)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, delimiter="\t",
                           fieldnames=["finding", "file_path", "record_id",
                                       "ingredient", "value", "unit", "detail"])
        w.writeheader()
        w.writerows(rows)

    summary = summarize_records(rows, args.normalized_dir)
    summary_path = args.out.with_name(args.out.stem + "_by_record.tsv")
    with summary_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, delimiter="\t",
                           fieldnames=["file_path", "record_id", "flagged_rows",
                                       "water_as_volume", "trace_salt_as_stock",
                                       "indicator_unit_slip", "has_solutions_block",
                                       "flattened_cocktail"])
        w.writeheader()
        w.writerows(summary)

    tally: dict[str, int] = {}
    for r in rows:
        tally[r["finding"]] = tally.get(r["finding"], 0) + 1
    affected = len({r["file_path"] for r in rows})
    cocktails = sum(1 for s in summary if s["flattened_cocktail"] == "yes")

    print(f"Implausible concentration rows: {len(rows)} across {affected} records")
    for k in ("WATER_AS_VOLUME", "TRACE_SALT_AS_STOCK", "INDICATOR_UNIT_SLIP"):
        if k in tally:
            print(f"  {k:20s} {tally[k]}")
    print(f"\nRecords holding a FLATTENED STOCK COCKTAIL: {cocktails}")
    print("  (>=3 flagged vitamin or trace rows and no `solutions:` block — "
          "the actionable subset)")
    print(f"\nWrote {args.out.relative_to(REPO_ROOT)}")
    print(f"Wrote {summary_path.relative_to(REPO_ROOT)}")
    print("\nRead-only. Repairing the trace-element case means nesting the cocktail "
          "under a stock `solution` object with an addition volume — per-record curation.")

    if args.max_allowed is not None and len(rows) > args.max_allowed:
        print(f"\nFAIL: {len(rows)} implausible concentration rows > baseline "
              f"{args.max_allowed}. A new import or edit has introduced rows beyond the "
              f"known backlog; see the report for which records.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
