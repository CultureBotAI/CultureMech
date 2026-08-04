#!/usr/bin/env python3
"""Draw a stratified sample of media for Edison axis classification (#152).

`nutritional_class` and `functional_role` sit on 1 record each. Filling them needs
signal the corpus does not carry, so it needs literature research — and there are
11,094 media at minutes per record, which is a campaign rather than a batch.

This draws a bounded sample instead, across four strata chosen because they answer
different questions:

  SEMI_DEFINED      composition already characterised (#152/#171), so the axes are
                    the only missing piece — highest signal per record.
  DEEP_RESEARCH     the existing priority ranking's top-N. Note that ranking
                    optimises for ORGANISM yield, not axis-classification value, so
                    it is included to test whether the two agree rather than
                    assumed to be the right frame.
  WELL_KNOWN        LB, TSB, M9, MacConkey and similar, where the correct answer is
                    independently checkable. This stratum is the ACCURACY CONTROL:
                    without it the run produces classifications nobody can grade.
  OTHER             a uniform draw from everything else, so the sample says
                    something about the corpus rather than only about its
                    interesting corners.

Strata are disjoint and assigned in the order above, so a record already taken as
SEMI_DEFINED is not redrawn as WELL_KNOWN. The `stratum` field is carried into the
batch so results can be scored per stratum afterwards — the point of sampling is
to learn the hit rate before committing to the remaining ~10,900.

Sampling is seeded and deterministic: the same corpus and seed reproduce the same
batch, so a rerun after a partial failure does not silently research a different
set.

Usage::

    just sample-axis-research-batch --size 200
    just research-media-edison-axis data/import_tracking/reports/axis_research_batch.json \\
        --limit 25 --dry-run
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_kinds import is_solution_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
RANKING = REPO / "data" / "import_tracking" / "reports" / "deep_research_priority_top100.json"
DEFAULT_OUT = REPO / "data" / "import_tracking" / "reports" / "axis_research_batch.json"

# Media whose nutritional class and functional role are documented in any
# microbiology text, so a wrong answer is immediately visible.
WELL_KNOWN = re.compile(
    r"\b(lb|luria|tryptic soy|tsb|tsa|brain heart|bhi|m9|nutrient (agar|broth)|"
    r"macconkey|sabouraud|potato dextrose|pda|mueller|blood agar|chocolate agar|"
    r"r2a|marine broth|czapek|malt extract agar|ym|yp[dg])\b", re.I)


def load_media(normalized: Path) -> list[tuple[Path, dict[str, Any]]]:
    out = []
    for path in sorted(normalized.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        if isinstance(doc, dict) and not is_solution_record(doc):
            out.append((path, doc))
    return out


def assign_strata(records, ranking_paths: set[str], normalized: Path
                  ) -> dict[str, list[tuple[Path, dict[str, Any]]]]:
    """Disjoint strata, assigned in priority order so no record appears twice."""
    strata: dict[str, list] = {"SEMI_DEFINED": [], "DEEP_RESEARCH": [],
                               "WELL_KNOWN": [], "OTHER": []}
    for path, doc in records:
        rel = str(path.relative_to(normalized))
        name = f"{doc.get('name', '')} {doc.get('original_name', '')}"
        if str(doc.get("composition_type")) == "SEMI_DEFINED":
            strata["SEMI_DEFINED"].append((path, doc))
        elif rel in ranking_paths:
            strata["DEEP_RESEARCH"].append((path, doc))
        elif WELL_KNOWN.search(name):
            strata["WELL_KNOWN"].append((path, doc))
        else:
            strata["OTHER"].append((path, doc))
    return strata


def allocate(size: int, capacity: dict[str, int]) -> dict[str, int]:
    """Split `size` across strata as evenly as their capacity allows.

    Flooring `size // n_strata` is not enough, and neither is handing the
    remainder to the biggest pools. Strata are genuinely uneven — DEEP_RESEARCH
    holds only 99 records against OTHER's 9,730 — so once a small stratum is
    exhausted its unused quota has to go somewhere, or the batch comes back short
    while reporting success (#185).

    Fills in rounds: each round shares what is still needed among the strata that
    still have room, so a stratum that runs out donates its remainder to the ones
    that can absorb it. Returns exactly `size` unless the whole corpus is smaller.
    """
    quota = dict.fromkeys(capacity, 0)
    remaining = min(size, sum(capacity.values()))
    while remaining > 0:
        open_strata = [n for n in capacity if quota[n] < capacity[n]]
        if not open_strata:
            break
        # Largest-capacity first, so the leftover single records land in the pools
        # deep enough to absorb them without skewing their character.
        share, extra = divmod(remaining, len(open_strata))
        order = sorted(open_strata, key=lambda n: -capacity[n])
        if share == 0:  # fewer records left than open strata
            share, extra = 0, remaining
        for i, name in enumerate(order):
            want = share + (1 if i < extra else 0)
            take = min(want, capacity[name] - quota[name])
            quota[name] += take
            remaining -= take
    return quota


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    ap.add_argument("--ranking", type=Path, default=RANKING)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--size", type=int, default=200)
    ap.add_argument("--seed", type=int, default=20260803,
                    help="fixed so a rerun researches the same records, not a new set")
    args = ap.parse_args(argv)

    ranking_paths: set[str] = set()
    if args.ranking.is_file():
        ranking_paths = {e["file_path"] for e in json.loads(args.ranking.read_text())
                         if isinstance(e, dict) and e.get("file_path")}

    records = load_media(args.normalized_dir)
    strata = assign_strata(records, ranking_paths, args.normalized_dir)

    rng = random.Random(args.seed)
    quota = allocate(args.size, {k: len(v) for k, v in strata.items()})
    drawn: dict[str, list[dict[str, Any]]] = {}
    print(f"{'stratum':16s} {'available':>10s} {'drawn':>7s}")
    for name, pool in strata.items():
        take = min(quota[name], len(pool))
        drawn[name] = [{
            "recipe_name": path.stem,
            "file_path": str(path.relative_to(args.normalized_dir)),
            "culturemech_id": str(doc.get("id") or ""),
            "stratum": name,
        } for path, doc in rng.sample(pool, take)]
        print(f"{name:16s} {len(pool):10d} {take:7d}")

    # Round-robin the strata rather than concatenating them, so EVERY PREFIX of the
    # batch is itself stratified. This matters because the runner researches in file
    # order and `--limit N` takes the first N: with the strata concatenated, a
    # 25-record probe would have drawn all 25 from SEMI_DEFINED and measured nothing
    # about the other three. Interleaved, `--limit 25` samples all four ~evenly, and
    # the probe is a strict subset of the full run — so the remaining records can be
    # finished later without re-researching any.
    batch: list[dict[str, Any]] = []
    for i in range(max((len(v) for v in drawn.values()), default=0)):
        for name in strata:
            if i < len(drawn[name]):
                batch.append(drawn[name][i])

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(batch, indent=2) + "\n")
    rel = args.out.relative_to(REPO) if args.out.is_relative_to(REPO) else args.out
    # `allocate` already caps each stratum at its capacity, so a shortfall can
    # only mean the corpus itself is smaller than --size. Say so rather than
    # returning a short batch that reads as full coverage.
    if len(batch) < args.size:
        print(f"  NOTE: corpus holds only {len(batch)} eligible records; "
              f"--size {args.size} was capped", file=sys.stderr)
    print(f"\nDrew {len(batch)} records (seed {args.seed}) -> {rel}")
    print("\nCanary the BATCH path before running it — --target and --batch are\n"
          "different code paths, and only the batch one resolves by slug:\n"
          f"  just research-media-edison-axis {rel} --limit 25 --dry-run")
    return 0


if __name__ == "__main__":
    sys.exit(main())
