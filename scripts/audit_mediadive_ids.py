#!/usr/bin/env python3
"""Check every corpus medium id against the MediaDive catalogue by NAME (#244).

A record's `media_term.term.id` is how any tool reaches upstream data — composition,
stock volumes, cross-references. If it points at a different medium, that tool
silently imports the wrong recipe. The #150 cocktail repair hit this: 165 of 312
resolved records fetched a medium whose name disagreed with the record's.

## What this audit established, which is NOT what #244 first claimed

Run over the whole corpus (6,962 records, from the single `/rest/media` listing
rather than per-record fetches), the disagreements are not spread across the corpus.
They are entirely an artifact of one translation step:

    mediadive.medium:*   3,322 AGREE + 3 renamed upstream = 3,325 of 3,325  (100%)
    komodo.medium:*      1,032 AGREE, 2,213 DISAGREE, 392 not in MediaDive

So **the corpus's own MediaDive ids are correct**. What is unreliable is
`data/raw/komodo_web/komodo_dsmz_mappings.json`: 43.5% of it is a bare identity
default (`komodo_id == dsmz_medium_number`), and MediaDive has renumbered since that
export, so translating a KOMODO id through it lands on an unrelated medium about 72%
of the time — KOMODO 294 "Pelobacter acidigallici" resolves to MediaDive 294
"Syntrophus HQGo1".

A KOMODO id is not wrong AS a KOMODO id. It simply must not be treated as a MediaDive
id, and any tool that does needs the name check `fetch_mediadive_solution_volumes`
applies before using fetched data.

## Verdicts

AGREE                the id exists in MediaDive and the names match
RENAMED_UPSTREAM     MediaDive renamed the medium but kept the number; the corpus id
                     is right (verified per case — see KNOWN_UPSTREAM_RENAMES)
DISAGREE             the id resolves to a DIFFERENT medium — for komodo ids this is
                     the mapping's fault, not the record's
NOT_IN_MEDIADIVE     the resolved id is absent from the catalogue
UNRESOLVED           a komodo id with no DSMZ mapping

For DISAGREE and NOT_IN_MEDIADIVE a `suggested_id` is reported when the record's name
matches exactly one MediaDive medium — a candidate for a curator, NOT an automatic
correction: names collide (JCM "GS MEDIUM" vs DSMZ "GS MEDIUM", #239), so a unique
match is evidence, not proof. Only 39 of 2,605 get one, which is why this cannot be
mass-corrected.

Read-only.

Usage::

    just audit-mediadive-ids                 # summary + TSV
    just audit-mediadive-ids --show 20       # also print examples
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from fetch_mediadive_solution_volumes import komodo_to_dsmz  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
DEFAULT_OUT = REPO / "data" / "import_tracking" / "reports" / "mediadive_id_audit.tsv"
CATALOGUE_URL = "https://mediadive.dsmz.de/rest/media"


def fetch_catalogue(cache: Path | None = None) -> dict[str, str]:
    """MediaDive medium id -> name, from the single catalogue listing."""
    if cache and cache.is_file():
        payload = json.loads(cache.read_text())
    else:
        with urllib.request.urlopen(CATALOGUE_URL, timeout=60) as r:
            payload = json.load(r)
        if cache:
            cache.write_text(json.dumps(payload))
    media = payload.get("data") or payload
    return {str(m["id"]): str(m.get("name") or "") for m in media if m.get("id") is not None}


def norm(s: Any) -> str:
    return re.sub(r"[^a-z0-9]", "", str(s or "").lower())


# MediaDive renamed these media upstream (taxonomic reclassification) while keeping
# the number. Each was verified by hand: the record's pH matches the MediaDive
# medium's exactly AND the record's own DSMZ PDF link cites the same medium number.
# So the corpus id is CORRECT and only the name moved — recording them here keeps the
# audit at zero real defects instead of carrying three permanent false alarms.
KNOWN_UPSTREAM_RENAMES = {
    "1236": "SPOROLITUUS -> THERMOSINUS MEDIUM (pH 7.0 both; record cites DSMZ_Medium1236.pdf)",
    "1298": "S. ALKALITOLERANS -> S. TAMANENSIS (pH 9.0 both; record cites DSMZ_Medium1298.pdf)",
    "1796": "PAS -> PAS-Ah for Acanthamoeba hatchetti (pH 6.5 both; same medium, abbreviated)",
}


def names_match(record_names: list[str], catalogue_name: str) -> bool:
    """Same medium? Containment either way, since MediaDive names are often longer
    ("BACTO MARINE BROTH (DIFCO 2216)" vs "Bacto Marine Broth")."""
    cat = norm(catalogue_name)
    if not cat:
        return False
    for n in record_names:
        c = norm(n)
        if c and (c == cat or c in cat or cat in c):
            return True
    return False


def record_names(doc: dict[str, Any]) -> list[str]:
    term = (doc.get("media_term") or {}).get("term") or {}
    return [doc.get("original_name"), doc.get("name"), term.get("label"),
            (doc.get("media_term") or {}).get("preferred_term")]


def audit(catalogue: dict[str, str], komodo_map: dict[str, str]) -> list[dict[str, str]]:
    by_name: dict[str, list[str]] = defaultdict(list)
    for mid, name in catalogue.items():
        by_name[norm(name)].append(mid)

    rows = []
    for path in sorted(NORMALIZED.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        if not isinstance(doc, dict):
            continue
        raw = str(((doc.get("media_term") or {}).get("term") or {}).get("id") or "")
        m = re.fullmatch(r"mediadive\.medium:(.+)", raw)
        k = re.fullmatch(r"komodo\.medium:(.+)", raw)
        if m:
            resolved, scheme = m.group(1), "mediadive"
        elif k:
            resolved, scheme = komodo_map.get(k.group(1)), "komodo"
        else:
            continue

        names = [n for n in record_names(doc) if n]
        if not resolved:
            verdict, cat_name = "UNRESOLVED", ""
        elif resolved not in catalogue:
            verdict, cat_name = "NOT_IN_MEDIADIVE", ""
        elif names_match(names, catalogue[resolved]):
            verdict, cat_name = "AGREE", catalogue[resolved]
        elif scheme == "mediadive" and resolved in KNOWN_UPSTREAM_RENAMES:
            verdict, cat_name = "RENAMED_UPSTREAM", catalogue[resolved]
        else:
            verdict, cat_name = "DISAGREE", catalogue[resolved]

        suggested = ""
        if verdict in ("DISAGREE", "NOT_IN_MEDIADIVE"):
            hits: set[str] = set()
            for n in names:
                hits.update(by_name.get(norm(n), []))
            if len(hits) == 1:
                suggested = hits.pop()

        rows.append({
            "file_path": str(path.relative_to(NORMALIZED)),
            "record_id": str(doc.get("id") or ""),
            "raw_id": raw,
            "scheme": scheme,
            "resolved_id": resolved or "",
            "verdict": verdict,
            "record_name": str(doc.get("original_name") or doc.get("name") or ""),
            "mediadive_name": cat_name,
            "suggested_id": suggested,
        })
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--cache", type=Path, default=Path("/tmp/mediadive_catalogue.json"),
                    help="Cache the catalogue listing here to avoid refetching.")
    ap.add_argument("--show", type=int, default=0, help="Print N examples per verdict.")
    args = ap.parse_args(argv)

    catalogue = fetch_catalogue(args.cache)
    rows = audit(catalogue, komodo_to_dsmz())
    counts = Counter(r["verdict"] for r in rows)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=[
            "file_path", "record_id", "raw_id", "scheme", "resolved_id", "verdict",
            "record_name", "mediadive_name", "suggested_id"])
        w.writeheader()
        w.writerows(rows)

    print(f"MediaDive catalogue: {len(catalogue)} media")
    print(f"Corpus records with a MediaDive-resolvable id: {len(rows)}\n")
    for verdict in ("AGREE", "RENAMED_UPSTREAM", "DISAGREE", "NOT_IN_MEDIADIVE", "UNRESOLVED"):
        n = counts.get(verdict, 0)
        print(f"  {verdict:18s} {n:6d}  ({n / max(len(rows), 1) * 100:.1f}%)")
    print("\n  by id scheme (this is the finding — see the module docstring):")
    per = Counter((r["scheme"], r["verdict"]) for r in rows)
    for (scheme, verdict), n in sorted(per.items()):
        print(f"    {scheme:10s} {verdict:18s} {n:6d}")

    fixable = [r for r in rows if r["verdict"] not in ("AGREE", "RENAMED_UPSTREAM")
               and r["suggested_id"]]
    print(f"\n  of the non-AGREE rows, {len(fixable)} have a UNIQUE name match in "
          f"MediaDive (a candidate id, not a proof)")

    for verdict in ("DISAGREE", "NOT_IN_MEDIADIVE"):
        for r in [x for x in rows if x["verdict"] == verdict][:args.show]:
            print(f"\n  {verdict}: {r['file_path']}")
            print(f"    id {r['raw_id']} -> {r['mediadive_name'] or '(absent)'!r}")
            print(f"    record name: {r['record_name']!r}"
                  + (f"  suggested id: {r['suggested_id']}" if r["suggested_id"] else ""))
    print(f"\nWrote {args.out.relative_to(REPO)} — read-only.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
