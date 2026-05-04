#!/usr/bin/env python3
"""One-off migration: stamp `is_max_attainment: true` on existing GrowthMetrics.

Background
----------
The schema bump that introduced the v2 GrowthMetrics shape (commits
adding PerturbationContext / StrainModification / NutrientOverride)
adds an optional `is_max_attainment: bool` flag. Existing
`target_organisms[].growth_metrics[]` entries — populated by curator
passes m9 / nutrient_broth / bg11 ×3 / geobacter_sulfurreducens_medium
— were all reviewed at apply-time as max-attainment / standard-medium
claims (the curator rejected conditional-growth / perturbed-condition
candidates outright). Backfilling `is_max_attainment: true` on those
existing entries is the safe migration default.

Behaviour
---------
* Walks `data/normalized_yaml/**/*.yaml`.
* For every populated growth_metrics entry (≥1 of `max_od600`,
  `doubling_time_minutes`, `growth_rate_per_hour` is set) that lacks
  the `is_max_attainment` field, sets it to `True`.
* Idempotent — second run touches 0 entries.
* Default is dry-run; pass `--apply` to write YAMLs.

Usage
-----
    python3 scripts/migrate_growth_metrics_v2.py
    python3 scripts/migrate_growth_metrics_v2.py --apply
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data" / "normalized_yaml"

_METRIC_KEYS = ("max_od600", "doubling_time_minutes", "growth_rate_per_hour")


def has_metric(gm: dict) -> bool:
    return any(gm.get(k) is not None for k in _METRIC_KEYS)


def migrate_recipe(path: Path) -> tuple[int, dict]:
    """Return (n_stamped, updated_doc). updated_doc is None when no
    change was needed."""
    try:
        doc = yaml.safe_load(path.read_text())
    except Exception as e:
        print(f"  load error {path.name}: {e}", file=sys.stderr)
        return 0, None
    if not isinstance(doc, dict):
        return 0, None

    stamped = 0
    for org in (doc.get("target_organisms") or []):
        for gm in (org.get("growth_metrics") or []):
            if not isinstance(gm, dict):
                continue
            if "is_max_attainment" in gm:
                continue
            if not has_metric(gm):
                continue
            gm["is_max_attainment"] = True
            stamped += 1
    return stamped, doc if stamped else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true",
                    help="write YAMLs (default: dry-run)")
    ap.add_argument("--data-dir", type=Path, default=DATA_DIR)
    args = ap.parse_args()

    if not args.data_dir.is_dir():
        print(f"data dir not found: {args.data_dir}", file=sys.stderr)
        return 2

    total_files = 0
    files_changed = 0
    metrics_stamped = 0
    for p in sorted(args.data_dir.rglob("*.yaml")):
        total_files += 1
        n, doc = migrate_recipe(p)
        if n == 0 or doc is None:
            continue
        files_changed += 1
        metrics_stamped += n
        rel = p.relative_to(REPO_ROOT)
        print(f"  {rel}: stamped {n} growth_metrics entries")
        if args.apply:
            p.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True))

    print()
    print(f"Total YAMLs:               {total_files}")
    print(f"Files needing migration:   {files_changed}")
    print(f"GrowthMetrics stamped:     {metrics_stamped}")
    print(f"Mode:                      {'APPLY' if args.apply else 'DRY-RUN'}")
    if not args.apply and metrics_stamped:
        print(f"\nRe-run with --apply to write changes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
