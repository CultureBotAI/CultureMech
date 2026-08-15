#!/usr/bin/env python3
"""Report ingredient names the corpus grounds more than one way (#258).

#258 was filed about glucose — `Dextrose` was split across CHEBI:17234, CHEBI:4167 and
CHEBI:17634 — but asked, correctly, whether the split was general before anyone patched
one compound. It is: 63 of 1,583 grounded names carry more than one `term.id`, across
13,657 ingredient rows. Dextrose was tenth by row count.

The useful signal is not "these disagree" but WHY, and the report separates the kinds
because they need different handling:

  HYDRATE      the competing ids are the same substance at different waters of
               crystallisation — `CoSO4 x 7 H2O` sitting on the ANHYDROUS cobalt
               sulfate. The NAME settles these: if it spells out a hydrate, the id
               must have it. Mechanically fixable.
  ION          one id is a bare ion or zwitterion where the name states a salt or the
               neutral compound (`KNO3` on CHEBI:17632, the nitrate ion). Also settled
               by the name.
  OTHER        everything else — genuinely different compounds, anomers, vitamer
               classes. `Vitamin B12` (cyanocobalamin vs the vitamer class) lives here
               and is a curation decision, not a sweep.

A minority reading is not automatically the wrong one. `CoSO4 x 7 H2O` had 1,161 rows on
the anhydrous id and 5 on the heptahydrate; the 5 were right. So the report shows the
full distribution and never picks a winner.

Read-only. Fixes live in `fix_wrong_compound_groundings.py`, which keys on the exact
name AND the id so that `Na2MoO4` can stay anhydrous while `Na2MoO4 x 2 H2O` moves.

Usage::

    just audit-grounding-consistency
    just audit-grounding-consistency --min-rows 50
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
NORMALIZED = REPO / "data" / "normalized_yaml"
DEFAULT_OUT = REPO / "data" / "import_tracking" / "reports" / "grounding_consistency.tsv"

# Strips the whole hydration clause, prefix included: "heptahydrate" must reduce to
# nothing, not to "hepta", or the two labels never share a stem and the class never
# fires. That bug made the report show zero HYDRATE splits.
HYDRATE = re.compile(
    r"(\d\s*H2O|\bx\s*H2O|\b(mono|di|tri|tetra|penta|hexa|hepta|octa|nona|deca|semi|"
    r"sesqui)?hydrate\b|\banhydrous\b|[\u00b7\u30fb]\s*\d?\s*H2O)", re.I)
ION_HINT = re.compile(r"(zwitterion|\(\d[+-]\)|\(\d?[+-]\)|ion\b|ate\(\d)", re.I)


def groundings(root: Path) -> dict[str, Counter]:
    out: dict[str, Counter] = defaultdict(Counter)
    for path in root.rglob("*.yaml"):
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        if not isinstance(doc, dict):
            continue
        groups = [doc.get("ingredients")] + [
            s.get("composition") for s in (doc.get("solutions") or [])
            if isinstance(s, dict)]
        for items in groups:
            for ing in items or []:
                if not isinstance(ing, dict):
                    continue
                name = str(ing.get("preferred_term") or "").strip()
                term = (ing.get("term") or {}).get("id")
                if name and term:
                    out[name][str(term)] += 1
    return out


def classify(name: str, labels: dict[str, str]) -> str:
    """Why do these ids compete? HYDRATE / ION / OTHER."""
    vals = list(labels.values())
    if HYDRATE.search(name) or any(HYDRATE.search(v) for v in vals):
        # ...but only if the ids differ by hydration rather than by substance.
        stems = {HYDRATE.sub("", v).strip().lower() for v in vals}
        if len(stems) == 1:
            return "HYDRATE"
    if any(ION_HINT.search(v) for v in vals):
        return "ION"
    return "OTHER"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--yaml-dir", type=Path, default=NORMALIZED)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--min-rows", type=int, default=0,
                    help="Only report names with at least this many rows.")
    args = ap.parse_args(argv)

    all_names = groundings(args.yaml_dir.resolve())
    split = {n: c for n, c in all_names.items() if len(c) > 1}

    labels: dict[str, str] = {}
    try:
        from oaklib import get_adapter
        adapter = get_adapter("sqlite:obo:chebi")
    except Exception:                                   # noqa: BLE001 - offline is fine
        adapter = None

    def label_of(term_id: str) -> str:
        if term_id not in labels:
            try:
                labels[term_id] = (adapter.label(term_id) or "") if adapter else ""
            except Exception:                           # noqa: BLE001
                labels[term_id] = ""
        return labels[term_id]

    rows = []
    for name, dist in split.items():
        total = sum(dist.values())
        if total < args.min_rows:
            continue
        lab = {t: label_of(t) for t in dist}
        rows.append({
            "ingredient": name,
            "rows": total,
            "distinct_ids": len(dist),
            "kind": classify(name, lab),
            "distribution": "; ".join(f"{t} ({lab[t] or '?'}) x{n}"
                                      for t, n in dist.most_common()),
        })
    rows.sort(key=lambda r: (-r["rows"], r["ingredient"]))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, delimiter="\t",
                           fieldnames=["ingredient", "rows", "distinct_ids", "kind",
                                       "distribution"])
        w.writeheader()
        w.writerows(rows)

    by_kind = Counter(r["kind"] for r in rows)
    print(f"Grounded ingredient names: {len(all_names)}")
    print(f"Names grounded MORE THAN ONE way: {len(split)} "
          f"({sum(sum(c.values()) for c in split.values())} rows)\n")
    print(f"  {'kind':10s} {'names':>6s} {'rows':>8s}")
    for kind in ("HYDRATE", "ION", "OTHER"):
        n = [r for r in rows if r["kind"] == kind]
        print(f"  {kind:10s} {len(n):6d} {sum(r['rows'] for r in n):8d}")
    print(f"\n  {'rows':>6s}  {'kind':8s} ingredient")
    for r in rows[:20]:
        print(f"  {r['rows']:6d}  {r['kind']:8s} {r['ingredient'][:56]}")
    if by_kind.get("HYDRATE") or by_kind.get("ION"):
        print("\nHYDRATE and ION splits are settled by the ingredient NAME and are "
              "mechanically fixable; see fix_wrong_compound_groundings.py.")
    try:
        shown = args.out.relative_to(REPO)
    except ValueError:
        shown = args.out
    print(f"\nWrote {shown} — read-only.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
