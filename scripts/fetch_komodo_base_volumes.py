#!/usr/bin/env python3
"""Recover addition volumes for KOMODO-sourced flattened cocktails (#150).

The remaining #150 long tail is not a research problem, it is an addressing problem.
111 of the 119 blocked records whose stock we can already name carry a
``komodo.medium:`` id, and `apply_cocktail_nesting.source_medium` refuses those on
purpose: KOMODO_294 stamps "DSMZ Medium: 294" on a record whose DSMZ 294 is a different
medium entirely (#244). So the stock is known, the volume exists upstream, and nothing
connects them.

What makes it tractable is that the KOMODO key itself carries the medium number, and it
can be derived TWICE, independently:

  * structurally, from the key -- ``142_12346`` -> ``142``, ``87a_13941`` -> ``87a``;
  * from the tracked KOMODO->DSMZ export, ``komodo_to_dsmz()``.

This script requires both to agree before it will fetch anything. That is a real check:
it is the disagreement between a stamped number and a derived one that produced #244.

Evidence classes, and why only one of them is an assertion
---------------------------------------------------------
A stock's addition volume is a property of the CITING MEDIUM, not of the stock. This
run demonstrates it flatly: MediaDive medium 142 adds "Trace element solution (Vishniac
& Santer)" at **0.2 ml**, medium 69 adds the same stock at **5 ml** -- 25x apart. So a
volume may only be asserted for the medium whose own recipe was read.

  READ_FROM_THIS_MEDIUM  the KOMODO key is a bare medium number (no variant suffix) AND
                         the fetched medium's name agrees with the record's. The recipe
                         read IS this record's recipe, so the volume is stated.

  CROSS_MEDIUM_INFERENCE everything else -- a modified variant (``142_12346``, whose own
                         recipe was never published separately), or a bare id whose name
                         disagrees (``69`` is THIOBACILLUS NOVELLUS here and STARKEYA
                         NOVELLA upstream: a genuine rename, but this script will not
                         adjudicate taxonomy). The volume is written to
                         ``concentration_candidates`` with its support and its
                         counterevidence, never to ``concentration``.

Output is shaped exactly like ``mediadive_solution_volumes.json`` so
`apply_cocktail_nesting` consumes it through the same code path -- and therefore behind
the same name+value match, which remains the thing that stops a wrong stock being
applied.

Read-only: writes a JSON cache, never touches the corpus.

Usage::

    just fetch-komodo-volumes --limit 5     # canary
    just fetch-komodo-volumes               # all resolvable KOMODO cocktails
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from fetch_mediadive_solution_volumes import (  # noqa: E402
    COCKTAIL_NAME, extract_additions, fetch_medium, komodo_to_dsmz, names_agree,
)

REPO = Path(__file__).resolve().parent.parent
NORMALIZED = REPO / "data" / "normalized_yaml"
PROPOSALS = REPO / "data" / "import_tracking" / "reports" / "cocktail_nesting_proposals.tsv"
DEFAULT_OUT = REPO / "data" / "import_tracking" / "reports" / "komodo_base_volumes.json"

# The concrete spread this corpus shows for one stock across two media. Quoted into
# every inferred candidate so a reviewer sees the risk without going to look for it.
SPREAD_NOTE = ("A stock's addition volume varies by citing medium: MediaDive medium 142 "
               "adds 'Trace element solution (Vishniac & Santer)' at 0.2 ml and medium "
               "69 adds the same stock at 5 ml.")

BARE_ID = re.compile(r"^\d+[a-z]?$")
BASE_OF = re.compile(r"^(\d+[a-z]?)")



MIN_SHARED_COMPOUNDS = 8
# ...of which at least this many must come from the medium's MAIN solution (#269).
# A medium's identity lives in its main solution: two unrelated media that both add
# SL-10 and Seven vitamins share ~14 stock compounds at identical values for free,
# because a stock's composition is the same wherever it is used. Counting only the
# total would let a record be identified on stocks alone.
MIN_MAIN_SOLUTION_COMPOUNDS = 5


def _norm_compound(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(s or "").lower())


def _num(v):
    try:
        return float(str(v).strip())
    except (TypeError, ValueError):
        return None


def medium_composition(medium: dict[str, Any],
                       main_only: bool = False) -> dict[str, float]:
    """Every compound MediaDive lists for this medium, at its g/l.

    `main_only` drops the referenced trace/vitamin stocks, leaving the salts that
    actually distinguish one medium from another.
    """
    out: dict[str, float] = {}
    for sol in medium.get("solutions") or []:
        if main_only and COCKTAIL_NAME.search(str(sol.get("name") or "")):
            continue
        for r in sol.get("recipe") or []:
            v = _num(r.get("g_l"))
            if r.get("compound") and v is not None:
                out.setdefault(_norm_compound(r["compound"]), v)
    return out


def record_composition(doc: dict[str, Any]) -> dict[str, float]:
    """Every compound this record lists, at its value, wherever it sits."""
    out: dict[str, float] = {}
    groups = [doc.get("ingredients")] + [
        s.get("composition") for s in (doc.get("solutions") or []) if isinstance(s, dict)]
    for items in groups:
        for i in items or []:
            if not isinstance(i, dict) or not i.get("preferred_term"):
                continue
            v = _num((i.get("concentration") or {}).get("value"))
            if v is not None:
                out.setdefault(_norm_compound(i["preferred_term"]), v)
    return out


def composition_agreement(doc: dict[str, Any],
                          medium: dict[str, Any]) -> tuple[float, int, int]:
    """(fraction of shared compounds whose VALUES agree, number shared, number of
    those that come from the medium's MAIN solution).

    This is the evidence that settles what a name comparison cannot. Most anaerobic
    DSMZ media share a backbone -- salts, trace elements, vitamins, bicarbonate,
    sulfide -- so comparing compound NAMES scores ~0.97 even between unrelated media
    and discriminates nothing. Comparing VALUES separates them cleanly: measured
    against its own resolved medium a record scores 1.00 over 15-47 shared compounds,
    and against three unrelated media it scores 0.00.

    Perfect agreement over MIN_SHARED_COMPOUNDS or more means the fetched medium is
    where this record's numbers came from, whatever either side calls it -- which is a
    stronger identification than the name match this used to require.
    """
    a, b = record_composition(doc), medium_composition(medium)
    shared = set(a) & set(b)
    if not shared:
        return 0.0, 0, 0
    agree = sum(1 for k in shared
                if abs(a[k] - b[k]) <= max(1e-9, 0.001 * abs(b[k])))
    main = len(shared & set(medium_composition(medium, main_only=True)))
    return agree / len(shared), len(shared), main


def composition_confirms(ratio: float, shared: int, main: int) -> bool:
    """Does the composition identify this medium well enough to assert its volume?"""
    return (ratio == 1.0 and shared >= MIN_SHARED_COMPOUNDS
            and main >= MIN_MAIN_SOLUTION_COMPOUNDS)


def komodo_key(doc: dict[str, Any]) -> str | None:
    mid = str(((doc.get("media_term") or {}).get("term") or {}).get("id") or "")
    return mid.split(":", 1)[1] if mid.startswith("komodo.medium:") else None


def resolve_base(key: str, kmap: dict[str, str]) -> tuple[str | None, str]:
    """The DSMZ/MediaDive medium number for a KOMODO key, or (None, reason).

    Both derivations must agree. A KOMODO key that the tracked export maps somewhere
    other than its own leading number is exactly the case this refuses to guess at.
    """
    m = BASE_OF.match(key)
    if not m:
        return None, "no medium number in the KOMODO key"
    structural = m.group(1)
    mapped = kmap.get(key) or kmap.get(structural)
    if not mapped:
        return None, f"KOMODO {key} is absent from the KOMODO->DSMZ export"
    if mapped.lower() != structural.lower():
        return None, (f"KOMODO {key} derives to {structural} structurally but the export "
                      f"maps it to {mapped} — refusing to choose")
    return structural, ""


def classify(key: str, doc: dict[str, Any], medium: dict[str, Any],
             base: str) -> tuple[str, str, str]:
    """(volume_basis, support, counterevidence) for this record/medium pair."""
    md_name = str((medium.get("medium") or {}).get("name") or "")
    rec_name = str(doc.get("original_name") or doc.get("name") or "")
    bare = bool(BARE_ID.fullmatch(key))
    agree = names_agree(doc, medium)

    ratio, shared, main = composition_agreement(doc, medium)
    confirmed = composition_confirms(ratio, shared, main)

    if bare and (agree or confirmed):
        how = (f"whose name ({md_name!r}) agrees with this record's" if agree else
               f"whose composition this record reproduces EXACTLY -- all {shared} "
               f"shared compounds at identical values ({main} of them from the main "
               f"solution), while unrelated media score 0")
        return ("READ_FROM_THIS_MEDIUM",
                f"KOMODO {key} resolves to DSMZ/MediaDive medium {base}, {how}; the "
                f"volume is printed in that medium's own recipe.", "")

    if bare:
        return ("CROSS_MEDIUM_INFERENCE",
                f"KOMODO {key} resolves to DSMZ/MediaDive medium {base} both "
                f"structurally and via the KOMODO->DSMZ export; volume read from that "
                f"medium's recipe.",
                f"The fetched medium is named {md_name!r} but this record is "
                f"{rec_name!r}, AND the compositions differ: only {ratio:.0%} of the "
                f"{shared} shared compounds carry the same value, so this record is not "
                f"simply medium {base} under another name. " + SPREAD_NOTE)

    return ("CROSS_MEDIUM_INFERENCE",
            f"This record is a variant of medium {base} (KOMODO key {key!r}); volume "
            f"read from base medium {base} ({md_name!r}).",
            f"The variant's own recipe was never read — only base medium {base}'s — so "
            f"the modification may change this volume. " + SPREAD_NOTE)


def komodo_records() -> list[tuple[str, str, dict[str, Any]]]:
    """(rel_path, komodo_key, doc) for flattened cocktails carrying a KOMODO medium id."""
    if not PROPOSALS.is_file():
        print(f"Run `just propose-cocktail-nesting` first — {PROPOSALS.name} is missing.",
              file=sys.stderr)
        return []
    out = []
    with PROPOSALS.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            path = NORMALIZED / row["file_path"]
            try:
                doc = yaml.safe_load(path.read_text(errors="replace"))
            except (yaml.YAMLError, OSError):
                continue
            if not isinstance(doc, dict):
                continue
            key = komodo_key(doc)
            if key:
                out.append((row["file_path"], key, doc))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--limit", type=int, default=0, help="Only the first N records.")
    ap.add_argument("--delay", type=float, default=0.34)
    args = ap.parse_args(argv)

    kmap = komodo_to_dsmz()
    records = komodo_records()
    if args.limit:
        records = records[:args.limit]
    print(f"Flattened cocktails carrying a KOMODO medium id: {len(records)}")

    cache: dict[str, dict[str, Any] | None] = {}     # medium number -> payload
    results: dict[str, Any] = {}
    stats = {"asserted": 0, "inferred": 0, "unresolved": 0, "not_found": 0, "no_stock": 0}

    for i, (rel, key, doc) in enumerate(records, 1):
        base, why = resolve_base(key, kmap)
        if not base:
            stats["unresolved"] += 1
            results[rel] = {"komodo_key": key, "resolved": False, "reason": why,
                            "additions": []}
            print(f"  [{i}/{len(records)}] {rel[:44]:46s} REFUSED — {why}")
            continue

        if base not in cache:
            cache[base] = fetch_medium(base)
            time.sleep(args.delay)
        medium = cache[base]
        if not medium:
            stats["not_found"] += 1
            results[rel] = {"komodo_key": key, "mediadive_id": base, "resolved": False,
                            "reason": f"MediaDive has no medium {base}", "additions": []}
            print(f"  [{i}/{len(records)}] {rel[:44]:46s} medium {base:>6s} -> NOT FOUND")
            continue

        basis, support, counter = classify(key, doc, medium, base)
        additions = []
        for add in extract_additions(medium):
            if add.get("addition_volume_ml") is None:
                continue
            entry = dict(add)
            entry["volume_basis"] = basis
            entry["volume_support"] = support
            if counter:
                entry["volume_counterevidence"] = counter
            additions.append(entry)
        if not additions:
            stats["no_stock"] += 1
        elif basis == "READ_FROM_THIS_MEDIUM":
            stats["asserted"] += 1
        else:
            stats["inferred"] += 1
        results[rel] = {"komodo_key": key, "mediadive_id": base, "resolved": True,
                        "volume_basis": basis, "additions": additions}
        flag = "ASSERT" if basis == "READ_FROM_THIS_MEDIUM" else "infer "
        print(f"  [{i}/{len(records)}] {rel[:44]:46s} medium {base:>6s} {flag} "
              f"{len(additions)} stock addition(s)"
              + (f"  e.g. {additions[0]['solution_name'][:28]} @ "
                 f"{additions[0]['addition_volume_ml']} ml" if additions else ""))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(results, indent=2) + "\n")
    print(f"\nRecords with an addition volume: "
          f"{stats['asserted']} assertable (medium read directly), "
          f"{stats['inferred']} inferred (candidate only).")
    print(f"  no stock addition in the fetched medium: {stats['no_stock']}")
    print(f"  medium number refused as ambiguous:      {stats['unresolved']}")
    print(f"  MediaDive has no such medium:            {stats['not_found']}")
    try:
        shown = args.out.relative_to(REPO)
    except ValueError:
        shown = args.out          # --out may point outside the repo (canary runs do)
    print(f"Wrote {shown} — read-only; the corpus is untouched.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
