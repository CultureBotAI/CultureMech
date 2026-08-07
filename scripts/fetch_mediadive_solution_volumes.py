#!/usr/bin/env python3
"""Fetch authoritative stock-solution addition volumes from MediaDive (#150).

The cocktail repair needs, per record, the volume at which a trace/vitamin stock is
added to the medium. `propose_cocktail_nesting.py` could only scrape a candidate out
of the record's own prose (15 of 579, several of them false positives), because that
is all the corpus holds.

MediaDive's `/rest/medium/{id}` has it exactly, and this is the endpoint that makes
#150 tractable. Each medium returns `solutions[]`, and a solution's `recipe[]` may
reference ANOTHER solution with the volume it contributes::

    {"solution": "Wolfe's mineral elixir", "solution_id": 1605,
     "amount": 1, "unit": "ml"}

That "1 ml" is the addition volume — authoritative, not inferred. The referenced
solution's own `recipe[]` is the cocktail's stock composition, and its `volume` is
the volume the stock is PREPARED in (1000 ml), which is a different number and must
not be mistaken for the addition volume. Conflating the two is the obvious way to
get this wrong, so both are reported separately.

Read-only: writes a JSON cache, never touches the corpus. Applying remains a
reviewed step (see `propose_cocktail_nesting.py`).

Usage::

    just fetch-mediadive-volumes --limit 5      # canary a few
    just fetch-mediadive-volumes                # all resolvable cocktails
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
NORMALIZED = REPO / "data" / "normalized_yaml"
PROPOSALS = REPO / "data" / "import_tracking" / "reports" / "cocktail_nesting_proposals.tsv"
DEFAULT_OUT = REPO / "data" / "import_tracking" / "reports" / "mediadive_solution_volumes.json"
API = "https://mediadive.dsmz.de/rest/medium/{}"

# A cocktail stock: trace elements, vitamins, mineral elixirs. Matching the
# REFERENCED solution's name keeps a main-solution self-reference or a buffer out.
COCKTAIL_NAME = re.compile(
    r"trace|vitamin|elixir|mineral|selenite|tungstate|SL-?\d+|metal", re.I)


KOMODO_DSMZ_MAP = REPO / "data" / "raw" / "komodo_web" / "komodo_dsmz_mappings.json"


def komodo_to_dsmz() -> dict[str, str]:
    """KOMODO medium id -> DSMZ medium number, from the tracked KOMODO web export.

    DSMZ medium numbers ARE MediaDive medium ids (MediaDive is DSMZ's database), so
    this is what lets a KOMODO-sourced record reach its MediaDive composition. The
    mapping is mostly identity with variant suffixes stripped (`1004.1` -> `1004`).

    It is NOT authoritative on its own: KOMODO 3136 maps to DSMZ 3136, which does not
    exist in MediaDive (that medium is really MediaDive 1203, see #239). So a
    resolved id is always confirmed by fetching and name-checking before use.
    """
    if not KOMODO_DSMZ_MAP.is_file():
        return {}
    try:
        data = json.loads(KOMODO_DSMZ_MAP.read_text())
    except (json.JSONDecodeError, OSError):
        return {}
    return {str(m["komodo_id"]): str(m["dsmz_medium_number"])
            for m in data.get("mappings", []) if m.get("dsmz_medium_number")}


def mediadive_id(doc: dict[str, Any], komodo_map: dict[str, str] | None = None) -> str | None:
    """The MediaDive medium id this record resolves to, if any.

    `mediadive.medium:<digits>[letter]` is direct. A `komodo.medium:` id is NOT a
    MediaDive id and must be translated through the KOMODO->DSMZ mapping first; using
    it directly is the #239 error. The J*/C*-prefixed ids are JCM/other catalogues
    whose composition MediaDive does not serve.
    """
    mid = str(((doc.get("media_term") or {}).get("term") or {}).get("id") or "")
    m = re.fullmatch(r"mediadive\.medium:(\d+[a-z]?)", mid)
    if m:
        return m.group(1)
    k = re.fullmatch(r"komodo\.medium:(.+)", mid)
    if k and komodo_map:
        dsmz = komodo_map.get(k.group(1))
        if dsmz and re.fullmatch(r"\d+[a-z]?", dsmz):
            return dsmz
    return None


def _norm_name(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(s or "").lower())


def names_agree(record: dict[str, Any], medium: dict[str, Any]) -> bool:
    """Does the fetched MediaDive medium look like the same medium as the record?

    Guards a mis-resolved id: a KOMODO number that happens to exist in MediaDive as a
    DIFFERENT medium would otherwise import the wrong composition wholesale. Compares
    the record's name/original_name against the MediaDive name, ignoring case and
    punctuation, and accepts a containment either way (MediaDive names are often
    longer, e.g. "BACTO MARINE BROTH (DIFCO 2216)").
    """
    md = _norm_name((medium.get("medium") or {}).get("name"))
    if not md:
        return False
    for candidate in (record.get("original_name"), record.get("name"),
                      ((record.get("media_term") or {}).get("term") or {}).get("label")):
        c = _norm_name(candidate)
        if c and (c == md or c in md or md in c):
            return True
    return False


def fetch_medium(mid: str, timeout: int = 20) -> dict[str, Any] | None:
    try:
        with urllib.request.urlopen(API.format(mid), timeout=timeout) as r:
            payload = json.load(r)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError):
        return None
    return payload.get("data") if payload.get("status") == 200 else None


def extract_additions(medium: dict[str, Any]) -> list[dict[str, Any]]:
    """Every "solution X is added at N ml" reference in this medium.

    Returns one entry per referenced cocktail solution, carrying BOTH volumes:
    `addition_volume_ml` (what the medium takes) and `stock_prepared_in_ml` (what the
    stock itself is made up to). The ratio of the two is what converts a stock
    concentration to its real final concentration.
    """
    by_id = {s.get("id"): s for s in medium.get("solutions") or []}
    out = []
    for sol in medium.get("solutions") or []:
        for item in sol.get("recipe") or []:
            ref_id = item.get("solution_id")
            ref_name = item.get("solution")
            if not ref_id or not ref_name:
                continue
            if not COCKTAIL_NAME.search(str(ref_name)):
                continue
            if str(item.get("unit") or "").lower() != "ml":
                continue          # a non-volume reference cannot give an addition volume
            referenced = by_id.get(ref_id) or {}
            out.append({
                "parent_solution": sol.get("name"),
                "solution_id": ref_id,
                "solution_name": ref_name,
                "addition_volume_ml": item.get("amount"),
                "stock_prepared_in_ml": referenced.get("volume"),
                "stock_components": [
                    {"compound": r.get("compound"), "amount": r.get("amount"),
                     "unit": r.get("unit"), "g_l": r.get("g_l")}
                    for r in (referenced.get("recipe") or [])
                    if r.get("compound")
                ],
            })
    return out


def cocktail_records() -> list[tuple[str, str, dict[str, Any]]]:
    """(file_path, mediadive_id) for flattened cocktails that resolve to MediaDive."""
    if not PROPOSALS.is_file():
        print(f"Run `just propose-cocktail-nesting` first — {PROPOSALS.name} is missing.",
              file=sys.stderr)
        return []
    import csv
    kmap = komodo_to_dsmz()
    out = []
    with PROPOSALS.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            path = NORMALIZED / row["file_path"]
            try:
                doc = yaml.safe_load(path.read_text(errors="replace"))
            except (yaml.YAMLError, OSError):
                continue
            mid = mediadive_id(doc, kmap) if isinstance(doc, dict) else None
            if mid:
                out.append((row["file_path"], mid, doc))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--limit", type=int, default=0, help="Fetch only the first N (canary).")
    ap.add_argument("--delay", type=float, default=0.34, help="Seconds between API calls.")
    args = ap.parse_args(argv)

    records = cocktail_records()
    if args.limit:
        records = records[:args.limit]
    print(f"Flattened cocktails resolving to a MediaDive medium: {len(records)}")

    results: dict[str, Any] = {}
    with_volume = 0
    mismatched = 0
    for i, (path, mid, doc) in enumerate(records, 1):
        medium = fetch_medium(mid)
        # A resolved id is only trusted when the fetched medium's NAME agrees with the
        # record's. Without this a mis-resolved KOMODO number silently imports another
        # medium's stock composition (#239).
        if medium and not names_agree(doc, medium):
            mismatched += 1
            print(f"  [{i}/{len(records)}] {path[:46]:48s} mediadive:{mid:>6s} "
                  f"-> NAME MISMATCH ({(medium.get('medium') or {}).get('name')!r}), skipped")
            results[path] = {"mediadive_id": mid, "fetched": True,
                             "name_mismatch": True, "additions": []}
            time.sleep(args.delay)
            continue
        additions = extract_additions(medium) if medium else []
        if additions:
            with_volume += 1
        results[path] = {"mediadive_id": mid, "fetched": medium is not None,
                         "additions": additions}
        print(f"  [{i}/{len(records)}] {path[:46]:48s} mediadive:{mid:>6s} "
              f"-> {len(additions)} stock addition(s)"
              + (f"  e.g. {additions[0]['solution_name']} @ "
                 f"{additions[0]['addition_volume_ml']} ml" if additions else ""))
        time.sleep(args.delay)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(results, indent=2) + "\n")
    print(f"\n{with_volume}/{len(records)} records have at least one authoritative "
          f"stock addition volume.")
    if mismatched:
        print(f"{mismatched} resolved id(s) fetched a medium whose name disagrees with "
              f"the record — skipped rather than importing the wrong composition.")
    print(f"Wrote {args.out.relative_to(REPO)} — read-only; the corpus is untouched.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
