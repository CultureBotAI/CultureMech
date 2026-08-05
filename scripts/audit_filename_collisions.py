#!/usr/bin/env python3
"""Triage recipes that share a filename across category directories (#116).

`data/normalized_yaml/<category>/<name>.yaml` is not unique across categories:
290 filenames appear in two or more category directories. #115 and #120 both hit
this and deliberately left the collisions alone rather than clobber a copy.

Deciding what to do with each pair is curation, not automation — this script does
not move, rename, or delete anything. It classifies each collision so the manual
pass is tractable, because the pairs are not all the same kind of problem:

  IDENTICAL      verbatim identical composition: same labels, same CHEBI
                 groundings, same concentrations, same units. Safe dedupe
                 candidates — there is nothing to choose between the copies.

  EQUIVALENT     the same medium imported twice, differing only in artefacts of
                 the ingestion chain — ingredient label variants
                 ("MgSO4・7H2O" vs "MgSO4 x 7 H2O", "Soluble starch" vs
                 "Starch"), a spurious water row, or the SAME ingredient grounded
                 to different CHEBI ids in the two copies. These need a curator to
                 pick the better-grounded copy; they are not distinct media.

  DIFFERENT      compositions genuinely diverge beyond those artefacts. These need
                 disambiguated filenames, not deduplication.

The EQUIVALENT class is why a naive comparison is misleading: by exact ingredient
tuples almost every collision looks DIFFERENT, but most of those differences are
ingestion noise. `1_10_sabourauds_agar.yaml` is the canonical example — identical
concentrations throughout, yet bacterial/ grounds Glucose to CHEBI:42758 while
fungal/ grounds it to CHEBI:17234, and bacterial/ carries an extra
"Distilled water 1 G_PER_L" row that is itself implausible (#118).

Usage::

    just audit-filename-collisions
    # -> data/import_tracking/reports/filename_collisions.tsv
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
NORMALIZED = REPO_ROOT / "data" / "normalized_yaml"
DEFAULT_OUT = REPO_ROOT / "data" / "import_tracking" / "reports" / "filename_collisions.tsv"

CATEGORIES = ("bacterial", "archaea", "algae", "fungal", "specialized")

# Water is dropped when testing equivalence: several ingestion paths add a
# "Distilled water" row (often at an implausible g/L, see #118) and several do
# not. Its presence says nothing about whether two records are the same medium.
WATER_IDS = {"CHEBI:15377"}
WATER_NAMES = {"distilled water", "water", "deionized water", "distilled h2o"}


def normalize_name(name: str) -> str:
    """Fold the label variants the ingestion chain produces.

    "MgSO4・7H2O" / "MgSO4 x 7 H2O" / "MgSO4·7H2O" all collapse; so do
    "Soluble starch" / "starch" via the qualifier strip.
    """
    s = (name or "").lower().strip()
    s = re.sub(r"\b(soluble|anhydrous|dried|powdered|technical)\b", "", s)
    s = re.sub(r"[·・x×*]\s*(\d+)\s*h2o", r"\1h2o", s)   # hydrate separators
    s = re.sub(r"[^a-z0-9]", "", s)
    return s


def _is_water(ident: str | None, name: str | None) -> bool:
    return (ident in WATER_IDS) or (normalize_name(name or "") in
                                    {normalize_name(w) for w in WATER_NAMES})


def _term_id(ing: dict[str, Any]) -> str | None:
    for key in ("mediaingredientmech_chebi_term", "term"):
        t = ing.get(key)
        if isinstance(t, dict) and isinstance(t.get("id"), str) and t["id"]:
            return t["id"]
    return None


def composition(doc: dict[str, Any], *, by: str, drop_water: bool) -> set[tuple]:
    """Ingredient composition as a comparable set.

    `by="id"` keys on the CHEBI id, `by="name"` on the normalized label. Both are
    needed: a pair can agree on ids while differing in labels, or vice versa, and
    either agreement is enough to call it the same medium.
    """
    out: set[tuple] = set()
    for ing in doc.get("ingredients") or []:
        if not isinstance(ing, dict):
            continue
        ident, name = _term_id(ing), ing.get("preferred_term")
        if drop_water and _is_water(ident, name):
            continue
        key = ident if by == "id" else normalize_name(str(name or ""))
        if not key:
            key = normalize_name(str(name or "")) or (ident or "?")
        conc = ing.get("concentration") or {}
        out.add((key, str(conc.get("value")), str(conc.get("unit"))))
    return out


def raw_composition(doc: dict[str, Any]) -> set[tuple]:
    """Verbatim composition: original label, CHEBI id, value and unit.

    Nothing is normalized or dropped. Two copies matching here are the same
    record; anything weaker belongs in EQUIVALENT, where a curator still has to
    choose between them — a label variant or a divergent grounding is a real
    difference between the files even when the medium is the same.
    """
    out: set[tuple] = set()
    for ing in doc.get("ingredients") or []:
        if not isinstance(ing, dict):
            continue
        conc = ing.get("concentration") or {}
        out.add((str(ing.get("preferred_term")), str(_term_id(ing)),
                 str(conc.get("value")), str(conc.get("unit"))))
    return out


def classify(docs: list[dict[str, Any]]) -> tuple[str, str]:
    """Return (classification, evidence) for the copies of one filename."""
    if len({frozenset(raw_composition(d)) for d in docs}) == 1:
        return "IDENTICAL", "verbatim same ingredients, groundings, concentrations and units"

    by_name = {frozenset(composition(d, by="name", drop_water=True)) for d in docs}
    if len(by_name) == 1:
        return "EQUIVALENT", "same after normalizing ingredient labels and ignoring water"

    by_id = {frozenset(composition(d, by="id", drop_water=True)) for d in docs}
    if len(by_id) == 1:
        return "EQUIVALENT", "same by CHEBI id; labels differ"

    sizes = sorted(len(composition(d, by="name", drop_water=True)) for d in docs)
    only = [composition(d, by="name", drop_water=True) for d in docs]
    shared = set.intersection(*only) if only else set()
    union = set.union(*only) if only else set()
    overlap = f"{len(shared)}/{len(union)} ingredient rows shared"
    return "DIFFERENT", f"{overlap}; sizes {sizes}"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args(argv)

    seen: dict[str, list[str]] = {}
    for cat in CATEGORIES:
        d = args.normalized_dir / cat
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.yaml")):
            seen.setdefault(f.name, []).append(cat)

    collisions = {n: cs for n, cs in seen.items() if len(cs) > 1}

    rows: list[dict[str, str]] = []
    for name, cats in sorted(collisions.items()):
        docs, ids, counts = [], [], []
        broken = False
        for c in cats:
            try:
                doc = yaml.safe_load((args.normalized_dir / c / name).read_text())
            except (yaml.YAMLError, OSError):
                broken = True
                break
            if not isinstance(doc, dict):
                broken = True
                break
            docs.append(doc)
            ids.append(str(doc.get("id") or "?"))
            counts.append(str(len(doc.get("ingredients") or [])))
        if broken:
            rows.append({"filename": name, "categories": ",".join(cats),
                         "classification": "UNREADABLE", "evidence": "YAML parse failure",
                         "ids": "", "ingredient_counts": ""})
            continue
        cls, evidence = classify(docs)
        rows.append({"filename": name, "categories": ",".join(cats),
                     "classification": cls, "evidence": evidence,
                     "ids": ",".join(ids), "ingredient_counts": ",".join(counts)})

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, delimiter="\t",
                           fieldnames=["filename", "categories", "classification",
                                       "evidence", "ids", "ingredient_counts"])
        w.writeheader()
        w.writerows(rows)

    tally: dict[str, int] = {}
    for r in rows:
        tally[r["classification"]] = tally.get(r["classification"], 0) + 1

    print(f"Filenames colliding across category dirs: {len(collisions)}")
    for k in ("IDENTICAL", "EQUIVALENT", "DIFFERENT", "UNREADABLE"):
        if k in tally:
            print(f"  {k:11s} {tally[k]}")
    rel = args.out.relative_to(REPO_ROOT) if args.out.is_relative_to(REPO_ROOT) else args.out
    print(f"\nWrote {rel}")
    print("\nNothing was moved, renamed or deleted — classification only (#116 is curation).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
