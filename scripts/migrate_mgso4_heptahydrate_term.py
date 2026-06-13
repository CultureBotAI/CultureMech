#!/usr/bin/env python3
"""Correct MgSO4·7H2O primary-`term` grounding (heptahydrate vs generic).

The G23 reliable-layer audit surfaced that explicitly-heptahydrate magnesium
sulfate ingredients ("MgSO4·7H2O" in many spellings) carry the PRIMARY
`term.id` = CHEBI:32599 ("magnesium sulfate", the generic/anhydrous class)
instead of CHEBI:31795 ("magnesium sulfate heptahydrate"). This is the
reliable-layer (primary `term`) analogue of the chebi_term fixes in G22/G24 —
those scripts only touched chebi_term / mediaingredientmech fields.

Label-conditional and conservative: only entries whose label denotes the
HEPTAHYDRATE (a "7 H2O" pattern) are remapped 32599 -> 31795. Generic
"Magnesium sulfate" / "MgSO4" stay on 32599, and "MgSO4 x 6 H2O" (a 6, not 7)
is untouched. The term label is set to the canonical CHEBI label.

Idempotent, --dry-run, CurationEvent, PyYAML round-trip.

Usage
-----
    python scripts/migrate_mgso4_heptahydrate_term.py --dry-run
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
NORMALIZED_DIR = REPO_ROOT / "data" / "normalized_yaml"
CURATOR = "mgso4-heptahydrate-term-fix-v1.0"
FROM_ID = "CHEBI:32599"          # magnesium sulfate (generic)
TO_ID = "CHEBI:31795"            # magnesium sulfate heptahydrate
TO_LABEL = "magnesium sulfate heptahydrate"
# Heptahydrate notation: a 7 immediately tied to water-of-crystallisation.
HEPTA = re.compile(r"7\s*h\s*2?\s*o", re.I)


def iter_ingredients(data: dict):
    for g in ("ingredients", "composition"):
        for i in data.get(g) or []:
            if isinstance(i, dict):
                yield i
    for s in data.get("solutions") or []:
        if isinstance(s, dict):
            for i in s.get("composition") or []:
                if isinstance(i, dict):
                    yield i


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--yaml-dir", type=Path, default=NORMALIZED_DIR)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    files = sorted(args.yaml_dir.rglob("*.yaml"))
    total_files = total = 0
    for p in files:
        try:
            data = yaml.safe_load(p.read_text())
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        local = 0
        for ing in iter_ingredients(data):
            t = ing.get("term")
            if not isinstance(t, dict) or str(t.get("id")) != FROM_ID:
                continue
            if HEPTA.search(str(ing.get("preferred_term", ""))):
                ing["term"] = {"id": TO_ID, "label": TO_LABEL}
                local += 1
        if local and not args.dry_run:
            data.setdefault("curation_history", []).append({
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "curator": CURATOR,
                "action": "Corrected MgSO4·7H2O primary term grounding to heptahydrate",
                "notes": f"Re-grounded {local} heptahydrate-labelled ingredient(s) from "
                         f"{FROM_ID} (generic magnesium sulfate) to {TO_ID} "
                         "(magnesium sulfate heptahydrate). Generic/hexahydrate labels untouched.",
            })
            p.write_text(yaml.safe_dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False))
        if local:
            total_files += 1
            total += local
    print(f"{'[DRY RUN] ' if args.dry_run else ''}files changed: {total_files} | "
          f"MgSO4·7H2O primary terms re-grounded {FROM_ID} -> {TO_ID}: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
