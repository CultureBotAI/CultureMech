#!/usr/bin/env python3
"""Name the stock a flattened cocktail came from, without guessing its volume (#150).

The nesting repair needs two facts per record: WHICH stock solution the
stock-strength ingredients belong to, and the VOLUME it is added at. For records
MediaDive serves, both come from that medium's own recipe. For the 315 it does not
serve, neither does — and the Edison literature lane recovers the volume for only
~12% of them.

This recovers the FIRST fact for most of them, cheaply and without inference.

## How the identification is safe

Every stock MediaDive has ever returned is collected into a library of
`name -> composition`. A blocked record is matched against that library the same
way `apply_cocktail_nesting` matches: an ingredient counts only if it agrees with a
stock component on NAME **and** VALUE, and only if the plausibility audit already
flagged it. Three or more such agreements identify the stock — a coincidence would
require three independent compounds to carry the same stock-strength values.

## Why it does NOT fill in the volume

The obvious next step is to reuse the stock's usual addition volume. The data does
not support it, and the reason is worth recording so it is not re-proposed:

    Trace element solution SL-10   n=36  1 distinct volume  <- invariant, but matches
                                                               0 blocked records
    Seven vitamins solution        n=48  4 distinct volumes <- matches 97 records
    Trace salt solution            n=3   1 distinct volume  <- "invariant" at n=3

The well-sampled stocks vary; the ones that look invariant are under-sampled. SL-10
is the one stock whose volume is genuinely constant across a large sample, and it
matches no blocked record at all — because SL-10 is a DSMZ stock, DSMZ media are
exactly what MediaDive serves, so every SL-10 user was already repaired. The blocked
population is blocked *because* it is non-DSMZ, and it uses other stocks.

So this reports the observed volume distribution as EVIDENCE and stops there. A
curator confirming "Seven vitamins solution, 44 of 48 observed at 1 ml/L" against the
record's own source is doing something this script cannot: checking.

Read-only.

Usage::

    just identify-cocktail-stocks
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import apply_cocktail_nesting as acn  # noqa: E402
import audit_concentration_plausibility as acp  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
REPORTS = REPO / "data" / "import_tracking" / "reports"
PROPOSALS = REPORTS / "cocktail_nesting_proposals.tsv"
VOLUMES = REPORTS / "mediadive_solution_volumes.json"
DEFAULT_OUT = REPORTS / "cocktail_stock_identification.tsv"

MIN_COMPONENTS = 3   # a cocktail is >=3 flagged rows by the audit's own definition


def build_library(volumes: dict[str, Any]) -> tuple[dict[str, list], dict[str, Counter]]:
    """stock name -> (largest observed composition, distribution of addition volumes)."""
    comps: dict[str, list] = {}
    vols: dict[str, Counter] = defaultdict(Counter)
    for info in volumes.values():
        for add in info.get("additions") or []:
            name = str(add.get("solution_name"))
            components = add.get("stock_components") or []
            vols[name][str(add.get("addition_volume_ml"))] += 1
            if name not in comps or len(components) > len(comps[name]):
                comps[name] = components
    return comps, vols


def blocked_records(volumes: dict[str, Any]) -> list[tuple[str, list]]:
    """Flattened cocktails still unrepaired that MediaDive gave no stock for."""
    out = []
    with PROPOSALS.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            rel = row["file_path"]
            try:
                doc = yaml.safe_load((NORMALIZED / rel).read_text(errors="replace"))
            except (yaml.YAMLError, OSError):
                continue
            if not isinstance(doc, dict) or doc.get("solutions"):
                continue
            if (volumes.get(rel) or {}).get("additions"):
                continue
            out.append((rel, [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args(argv)

    if not (PROPOSALS.is_file() and VOLUMES.is_file()):
        print("Run `just propose-cocktail-nesting` and `just fetch-mediadive-volumes` first.",
              file=sys.stderr)
        return 1
    volumes = json.loads(VOLUMES.read_text())
    comps, vols = build_library(volumes)

    flagged: dict[str, set[str]] = {}
    for r in acp.audit(NORMALIZED):
        if r["finding"] in ("TRACE_SALT_AS_STOCK", "INDICATOR_UNIT_SLIP"):
            flagged.setdefault(r["file_path"], set()).add(acn._key(r["ingredient"]))

    rows = []
    for rel, ingredients in blocked_records(volumes):
        marks = flagged.get(rel, set())
        best: tuple[int, str] = (0, "")
        for name, components in comps.items():
            idx, _ = acn.match_components(ingredients, components, marks)
            if len(idx) > best[0]:
                best = (len(idx), name)
        matched, name = best
        if matched < MIN_COMPONENTS:
            continue
        dist = vols[name]
        total = sum(dist.values())
        top_vol, top_n = dist.most_common(1)[0]
        rows.append({
            "file_path": rel,
            "identified_stock": name,
            "matched_components": str(matched),
            "flagged_components": str(len(marks)),
            # Evidence, deliberately not a decision: how often this stock was seen,
            # and how consistent its volume was when it was.
            "observed_n": str(total),
            "volume_distribution": "; ".join(f"{v}ml x{c}" for v, c in dist.most_common()),
            "modal_volume_ml": top_vol,
            "modal_share": f"{top_n / total * 100:.0f}%",
            "volume_is_invariant": "yes" if len(dist) == 1 else "no",
        })

    rows.sort(key=lambda r: (-int(r["matched_components"]), r["file_path"]))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=list(rows[0]) if rows else
                           ["file_path", "identified_stock"])
        w.writeheader()
        w.writerows(rows)

    blocked = blocked_records(volumes)
    print(f"Blocked flattened cocktails: {len(blocked)}")
    print(f"Stock identified by exact name+value match (>={MIN_COMPONENTS} components): "
          f"{len(rows)}\n")
    by_stock = Counter(r["identified_stock"] for r in rows)
    print(f"  {'stock':42s} {'records':>7s} {'obs n':>6s} {'modal':>8s} {'invariant':>10s}")
    for name, n in by_stock.most_common(10):
        ex = next(r for r in rows if r["identified_stock"] == name)
        print(f"  {name[:40]:42s} {n:7d} {ex['observed_n']:>6s} "
              f"{ex['modal_volume_ml'] + 'ml ' + ex['modal_share']:>8s} "
              f"{ex['volume_is_invariant']:>10s}")

    print("\nThe volume is NOT filled in. The one stock with a genuinely invariant")
    print("volume across a large sample (SL-10, n=36) matches none of these records —")
    print("see this script's docstring for why. Confirm the volume against each")
    print("record's own source before nesting.")
    print(f"\nWrote {args.out.relative_to(REPO)} — read-only.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
