#!/usr/bin/env python3
"""Restore the real ingredient names and amounts to the UTEX records.

## What went wrong

UTEX composition tables are headed
`# | Component | Amount | Stock Solution Concentration | Final Concentration`.
The fetcher read `cols[0]` and `cols[1]` — fixed positions, never the header —
so the row ordinal became the ingredient and the component name became the
"amount". The real Amount column was never read at all.

Downstream that became, in every one of the 99 UTEX records:

    - preferred_term: '1'
      concentration: {value: variable, unit: G_PER_L}
      notes: 'Original amount: DYIII Medium'

Three separate defects in four lines. The name is an ordinal; the real name is
stranded in a note that claims to be an amount; and the concentration is
invented — `G_PER_L` was supplied by `fix_schema_inconsistencies.py` for every
ingredient that had no amount, asserting grams per litre for four drops of
vitamin cocktail.

## What this repairs

Against a fresh capture (`just fetch-utex` with the header-aware fetcher):

1. `preferred_term` <- the real component name, with any trailing vendor or CAS
   parenthetical split off, so the name can actually ground against ChEBI/MIM.
   `NaNO3(Fisher BP360-500)` never matched anything; `NaNO3` does.
2. `supplier_catalog` <- the vendor parenthetical, which is what that field is
   for. A `(CAS: ...)` parenthetical is not a supplier and goes to `notes`.
3. `concentration` <- parsed from the source, preferring the page's own Final
   Concentration column over the Amount column, converted to the corpus's
   per-litre convention with exact decimal arithmetic. Where the amount has no
   volume basis to convert against ("4 drops", "1 cc", "1 per 200 mL"), the
   value is `{value: variable, unit: VARIABLE}` — the corpus's existing honest
   placeholder — never a guessed unit.
4. `notes` <- the verbatim source cells, so every derived value can be checked
   against what UTEX actually printed, and the fabricated "Original amount:"
   note is gone.

Matching is by ordinal position cross-checked against the name recovered from
the note, comparing base names with vendor/CAS parentheticals stripped (UTEX
switched from catalogue numbers to CAS numbers after the January 2026 capture).
All 497 corrupted ingredients match unambiguously; an ingredient that does not
match is left untouched and reported.

Preview by default. `--apply` writes.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter

# `timezone.utc`, not `datetime.UTC`: the latter is 3.11+ and this project
# supports >=3.10. The rest of scripts/ already uses timezone.utc.
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from record_io import write_record  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RECORDS = REPO_ROOT / "data" / "normalized_yaml"
DEFAULT_CAPTURE = REPO_ROOT / "data" / "raw" / "utex" / "utex_media.json"

CURATOR = "repair_utex_ingredients.py"
ACTION = "REPAIRED_UTEX_COMPOSITION"

# The note the corruption left behind. Its payload is the real ingredient name.
ORIGINAL_AMOUNT = re.compile(r"^Original amount:\s*(.*)$")

# A trailing parenthetical naming a vendor or a CAS number, e.g.
# "NaNO3(Fisher BP360-500)" or "MgSO4•7H2O(CAS: 10034-99-8)". Anchored at the
# end so a parenthetical that is part of the chemistry — "PABA(p-aminobenzoic
# acid)" — is only stripped when a vendor/CAS one follows it.
VENDORS = (
    "Sigma",
    "Fisher",
    "Baker",
    "MCIB",
    "Bacto",
    "Difco",
    "ICN",
    "Aldrich",
    "Mallinckrodt",
    "ACROS",
    "VWR",
    "EM Science",
    "J.T. Baker",
    "Alfa",
)
_VENDOR_ALT = "|".join(re.escape(v) for v in VENDORS)
TRAILING_PAREN = re.compile(
    rf"\((?P<body>(?:CAS:\s*|(?:{_VENDOR_ALT})\b)[^()]*)\)\s*$", re.IGNORECASE
)

UNIT_BY_NUMERATOR = {
    "g": "G_PER_L",
    "mg": "MG_PER_L",
    "µg": "MICROG_PER_L",
    "ug": "MICROG_PER_L",
    "mcg": "MICROG_PER_L",
    "ml": "ML_PER_L",
    "l": "L",
}
MOLARITY = {"m": "MOLAR", "mm": "MILLIMOLAR", "µm": "MICROMOLAR", "um": "MICROMOLAR"}
# Litres per one unit of the denominator, for converting an amount onto the
# corpus's per-litre convention.
LITRES = {"l": Decimal(1), "ml": Decimal(1) / Decimal(1000), "cc": Decimal(1) / Decimal(1000)}

NUMBER = r"(?P<n>\d+(?:\.\d+)?)"
RATIO = re.compile(
    rf"^{NUMBER}\s*(?P<num>µg|ug|mcg|mg|mL|ml|g|L)\s*/\s*"
    rf"(?P<d>\d+(?:\.\d+)?)?\s*(?P<den>mL|ml|L|l|cc)\b",
    re.IGNORECASE,
)
MOLAR = re.compile(rf"^{NUMBER}\s*(?P<u>mM|µM|uM|M)\b")


def strip_vendor(name: str) -> tuple[str, str | None, str | None]:
    """`name` -> (base name, supplier text, CAS number).

    Only one of supplier/CAS is ever returned; UTEX prints one or the other.
    """
    match = TRAILING_PAREN.search(name)
    if not match:
        return name.strip(), None, None
    body = match.group("body").strip()
    base = name[: match.start()].strip()
    if body.lower().startswith("cas:"):
        return base, None, body.split(":", 1)[1].strip()
    return base, body, None


def split_supplier(text: str) -> dict[str, str]:
    """ "Sigma P 3786" -> {supplier_name: Sigma, catalog_number: P 3786}."""
    for vendor in sorted(VENDORS, key=len, reverse=True):
        if text.lower().startswith(vendor.lower()):
            catalog = text[len(vendor) :].strip()
            entry = {"supplier_name": vendor}
            if catalog:
                entry["catalog_number"] = catalog
            return entry
    return {"supplier_name": text}


def _decimal(text: str) -> Decimal | None:
    try:
        return Decimal(text)
    except InvalidOperation:
        return None


def _render(value: Decimal) -> str:
    """Shortest exact decimal string; no float noise, no trailing zeros."""
    normalized = value.normalize()
    text = format(normalized, "f")
    return text


def parse_concentration(text: str) -> dict[str, str] | None:
    """A UTEX Amount or Final Concentration cell -> a ConcentrationValue.

    Returns None when the cell states no convertible quantity — "4 drops",
    "1 cc", "1 per 200 mL", "40 mL of supernatant". Those get the corpus's
    VARIABLE placeholder rather than a guessed unit.
    """
    cell = (text or "").strip()
    if not cell:
        return None

    molar = MOLAR.match(cell)
    if molar and not RATIO.match(cell):
        number = _decimal(molar.group("n"))
        if number is not None:
            return {"value": _render(number), "unit": MOLARITY[molar.group("u").lower()]}

    ratio = RATIO.match(cell)
    if ratio:
        number = _decimal(ratio.group("n"))
        unit = UNIT_BY_NUMERATOR.get(ratio.group("num").lower())
        per = LITRES.get(ratio.group("den").lower())
        if number is None or unit is None or per is None:
            return None
        denominator = _decimal(ratio.group("d") or "1")
        if denominator is None or denominator == 0:
            return None
        litres = denominator * per
        if litres == 0:
            return None
        return {"value": _render(number / litres), "unit": unit}

    return None


VARIABLE = {"value": "variable", "unit": "VARIABLE"}


def build_ingredient(existing: dict[str, Any], source: dict[str, str]) -> dict[str, Any]:
    """The repaired ingredient, preserving every field the repair does not own."""
    repaired = dict(existing)

    base, supplier, cas = strip_vendor(source["ingredient"])
    repaired["preferred_term"] = base

    amount = (source.get("amount") or "").strip()
    final = (source.get("final_concentration") or "").strip()
    stock = (source.get("stock_concentration") or "").strip()

    # The page's own Final Concentration is a stronger claim than an amount we
    # would have to convert, so it wins where UTEX printed one.
    concentration = parse_concentration(final) or parse_concentration(amount)
    repaired["concentration"] = concentration or dict(VARIABLE)

    if supplier:
        repaired.setdefault("supplier_catalog", split_supplier(supplier))

    # Verbatim provenance, so every converted value stays checkable and nothing
    # the page printed is discarded.
    printed = [f"amount {amount}" if amount else ""]
    if stock:
        printed.append(f"stock {stock}")
    if final:
        printed.append(f"final {final}")
    if cas:
        printed.append(f"CAS {cas}")
    parts = [p for p in printed if p]
    note = "UTEX lists: " + "; ".join(parts) if parts else None

    previous = (existing.get("notes") or "").strip()
    if previous and not ORIGINAL_AMOUNT.match(previous):
        # Someone curated a real note onto this ingredient; keep it.
        note = f"{previous} | {note}" if note else previous
    if note:
        repaired["notes"] = note
    else:
        repaired.pop("notes", None)

    return repaired


def utex_id(record: dict[str, Any]) -> str | None:
    for reference in record.get("references") or []:
        value = reference.get("reference") if isinstance(reference, dict) else None
        if isinstance(value, str) and value.startswith("UTEX:"):
            return value.split(":", 1)[1]
    return None


def recovered_name(ingredient: dict[str, Any]) -> str | None:
    match = ORIGINAL_AMOUNT.match((ingredient.get("notes") or "").strip())
    return match.group(1).strip() if match else None


def base_name(name: str) -> str:
    return strip_vendor(name)[0].lower()


def repair_record(
    record: dict[str, Any], composition: list[dict[str, str]], stats: Counter
) -> tuple[dict[str, Any], int, list[str]]:
    """Returns (record, repaired_count, per-ingredient failures)."""
    ingredients = record.get("ingredients") or []
    failures: list[str] = []
    repaired_count = 0

    for index, ingredient in enumerate(ingredients):
        term = str(ingredient.get("preferred_term", "")).strip()
        if not term.isdigit():
            stats["skipped_not_corrupted"] += 1
            continue
        name = recovered_name(ingredient)
        if not name:
            failures.append(f"[{index}] preferred_term={term!r} has no recoverable name")
            continue
        if index >= len(composition):
            failures.append(f"[{index}] {name!r} has no row at that ordinal in the capture")
            continue
        source = composition[index]
        if base_name(source["ingredient"]) != base_name(name):
            failures.append(
                f"[{index}] {name!r} does not match capture row {source['ingredient']!r}"
            )
            continue
        ingredients[index] = build_ingredient(ingredient, source)
        repaired_count += 1

    return record, repaired_count, failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--records-dir", type=Path, default=DEFAULT_RECORDS)
    parser.add_argument("--capture", type=Path, default=DEFAULT_CAPTURE)
    parser.add_argument("--apply", action="store_true", help="Write. Default is preview.")
    parser.add_argument("--limit", type=int, default=0, help="Repair at most N records.")
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])

    capture = json.loads(args.capture.read_text())
    by_id = {r["id"]: r for r in capture["recipes"]}

    stats: Counter = Counter()
    failed: list[tuple[str, list[str]]] = []
    changed: list[Path] = []

    for path in sorted(args.records_dir.glob("*/*.yaml")):
        record = yaml.safe_load(path.read_text())
        if not isinstance(record, dict):
            continue
        source_id = utex_id(record)
        if not source_id:
            continue
        stats["utex_records"] += 1

        corrupted = sum(
            1
            for i in record.get("ingredients") or []
            if str(i.get("preferred_term", "")).strip().isdigit()
        )
        if not corrupted:
            stats["records_already_clean"] += 1
            continue
        if source_id not in by_id:
            stats["records_missing_from_capture"] += 1
            failed.append((path.name, [f"UTEX:{source_id} is not in the capture"]))
            continue

        record, repaired, failures = repair_record(record, by_id[source_id]["composition"], stats)
        stats["ingredients_repaired"] += repaired
        if failures:
            failed.append((path.name, failures))
            stats["records_with_failures"] += 1
            continue
        if not repaired:
            continue

        record.setdefault("curation_history", []).append(
            {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "curator": CURATOR,
                "action": ACTION,
                "notes": (
                    f"Restored {repaired} ingredient name(s) and amount(s) from a "
                    f"re-fetched UTEX capture. The original fetcher read fixed column "
                    f"positions, so the row ordinal was stored as the ingredient name, "
                    f"the component name as the amount, and the Amount column was never "
                    f"read; concentration was then filled in as G_PER_L regardless. "
                    f"Source: {capture.get('source_url', 'UTEX')}, "
                    f"captured {capture.get('fetched_date', 'unknown')}."
                ),
            }
        )
        stats["records_repaired"] += 1
        changed.append(path)
        if args.apply:
            write_record(path, record)
        if args.limit and stats["records_repaired"] >= args.limit:
            break

    verb = "Repaired" if args.apply else "Would repair"
    print(
        f"\n{verb} {stats['records_repaired']} records / "
        f"{stats['ingredients_repaired']} ingredients"
    )
    for key in sorted(stats):
        print(f"  {key}: {stats[key]}")
    if failed:
        print(f"\n{len(failed)} record(s) left untouched:")
        for name, reasons in failed:
            print(f"  {name}")
            for reason in reasons:
                print(f"      {reason}")
    if not args.apply:
        print("\nPreview only. Re-run with --apply to write.")

    # A partial apply is a failure: it leaves the corpus half-repaired.
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
