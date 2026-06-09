#!/usr/bin/env python3
"""Grounding-consistency QC probe (backlog G23).

Self-consistency check for ingredient CHEBI grounding — no external truth
needed (MIM is unreliable; it mis-grounds glycerol, casamino acids, ...).
Two complementary signals:

  A. SAME NAME, MULTIPLE CHEBI — one ingredient name grounded to >1 CHEBI id
     across the corpus (e.g. "Glucose" -> CHEBI:17234 and CHEBI:42758).
     The clearest inconsistency: the same substance can't have two ids.
  B. SAME CHEBI, MULTIPLE NAMES — one CHEBI id carrying chemically-distinct
     ingredient names (e.g. CHEBI:32149 tagging both "Na2SO4" and
     "Na-DL-lactate"). Names are normalised to collapse benign formatting
     (salt/hydrate/formula/case) so only genuinely different compounds remain.

Walks `ingredients`, top-level `composition`, and nested
`solutions[].composition` across all records. Writes a TSV report and prints a
summary. With `--max-allowed N`, exits non-zero when signal-A names exceed the
baseline — wire that into CI to block *new* inconsistencies while the existing
backlog (G24) is worked down.

Usage
-----
    uv run python scripts/audit_chebi_consistency.py
    uv run python scripts/audit_chebi_consistency.py --out reports/chebi_consistency.tsv --max-allowed 0
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
NORMALIZED_DIR = REPO_ROOT / "data" / "normalized_yaml"
# Consistency is checked on the RELIABLE CHEBI grounding only: the primary
# `term` (when CHEBI) or an `exact_match` `chebi_term`. The `kg_fallback`
# chebi_term layer (~61% of chebi_terms) is a known low-confidence KG-embedding
# guess (e.g. "Distilled water" -> CHEBI:6636 magnesium dichloride) and is
# counted/reported separately rather than treated as a grounding.
RELIABLE_CHEBI_MATCH = {"exact_match"}


def reliable_chebi(ing: dict) -> str | None:
    term = ing.get("term")
    if isinstance(term, dict) and str(term.get("id", "")).startswith("CHEBI:"):
        return str(term["id"])
    ct = ing.get("chebi_term")
    if isinstance(ct, dict) and str(ct.get("id", "")).startswith("CHEBI:") \
            and ct.get("match_type") in RELIABLE_CHEBI_MATCH:
        return str(ct["id"])
    return None


def fallback_match_type(ing: dict) -> str | None:
    ct = ing.get("chebi_term")
    if isinstance(ct, dict) and str(ct.get("id", "")).startswith("CHEBI:") \
            and ct.get("match_type") not in RELIABLE_CHEBI_MATCH:
        return str(ct.get("match_type") or "(none)")
    return None


def name_key(s: str) -> str:
    """Light normalisation: case + whitespace only (keeps distinct names distinct)."""
    return " ".join(str(s or "").lower().split())


def core_key(s: str) -> str:
    """Aggressive normalisation: strip salt/hydrate/formula/case so benign
    formatting variants of the *same* compound collapse together."""
    s = str(s or "").lower()
    s = re.sub(r"\([^)]*\)", "", s)
    s = re.sub(r"[·•・]|\bx\b", " ", s)
    s = re.sub(r"\d+\s*h2?o|hydrate|anhydrous|solution|difco|\bbd\b", " ", s)
    s = re.sub(r"\b(na2?|sodium|potassium|k2?|di|tri|mono|disodium|dipotassium|"
               r"calcium|magnesium|ammonium|ferric|ferrous|iron|hydrochloride|hcl|salt)\b", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(sorted(set(w for w in s.split() if w)))


def iter_ingredients(data: dict):
    if not isinstance(data, dict):
        return
    for grp_key in ("ingredients", "composition"):
        for ing in data.get(grp_key) or []:
            if isinstance(ing, dict):
                yield ing
    for sol in data.get("solutions") or []:
        if isinstance(sol, dict):
            for ing in sol.get("composition") or []:
                if isinstance(ing, dict):
                    yield ing


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--yaml-dir", type=Path, default=NORMALIZED_DIR)
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument("--max-allowed", type=int, default=None,
                    help="Exit 1 if the count of same-name-multiple-CHEBI names exceeds this baseline.")
    args = ap.parse_args(argv)

    name_to_chebi: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    chebi_to_core: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    fallback = collections.Counter()

    for p in args.yaml_dir.rglob("*.yaml"):
        try:
            data = yaml.safe_load(p.read_text())
        except Exception:
            continue
        for ing in iter_ingredients(data):
            label = ing.get("preferred_term", "")
            cid = reliable_chebi(ing)
            if cid:
                name_to_chebi[name_key(label)][cid] += 1
                chebi_to_core[cid][core_key(label)] += 1
            ft = fallback_match_type(ing)
            if ft:
                fallback[ft] += 1

    # Signal A: same name -> multiple CHEBI
    a = {n: dict(c) for n, c in name_to_chebi.items() if len([k for k in c]) > 1 and n}
    # Signal B: same CHEBI -> multiple distinct core names
    b = {cid: dict(c) for cid, c in chebi_to_core.items()
         if len([k for k in c if k]) > 1}

    print(f"Signal A — same name, multiple CHEBI ids (reliable groundings): {len(a)} names")
    print(f"Signal B — same CHEBI id, multiple distinct compounds: {len(b)} ids")
    print(f"Low-confidence chebi_term layer (reported, not gated): "
          f"{sum(fallback.values())} fields {dict(fallback)}")

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w") as fh:
            fh.write("signal\tkey\tvariants\n")
            for n, c in sorted(a.items(), key=lambda kv: -sum(kv[1].values())):
                fh.write(f"A_name_multi_chebi\t{n}\t{c}\n")
            for cid, c in sorted(b.items(), key=lambda kv: -sum(kv[1].values())):
                fh.write(f"B_chebi_multi_compound\t{cid}\t{c}\n")
        print(f"wrote {args.out} ({len(a)+len(b)} rows)")

    if args.max_allowed is not None and len(a) > args.max_allowed:
        print(f"FAIL: {len(a)} same-name-multiple-CHEBI names > baseline {args.max_allowed}",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
