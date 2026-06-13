#!/usr/bin/env python3
"""Fix primary-`term` grounding: wrong-id re-grounding + label canonicalization.

report-label-drift surfaced that the PRIMARY `term` field (which all of G25 left
untouched — G25 only fixed `chebi_term`) has two problems:
  * wrong-id: term.id names a completely different compound than the ingredient
    (e.g. K2HPO4 -> CHEBI:32030 potassium bromide; Tricine -> CHEBI:35920 berbaman).
  * wrong-label: id correct but term.label is a formula/source string, not the
    OBO canonical label (NaCl vs "sodium chloride").

This driver classifies every distinct (term.id, preferred_term) primary-term
pair with OAK `sqlite:obo:chebi`, then applies one of two modes:

  --mode reground      : where the ingredient's name resolves (OAK exact) to a
                         DIFFERENT CHEBI than term.id, re-ground id+label to it.
  --mode canonicalize  : where the name resolves to the SAME id (id confirmed
                         correct), set term.label to the OBO canonical label.

SAFETY: an action fires only when the ingredient NAME (preferred_term, or its
normalised form) resolves to a single exact CHEBI in OAK. Names that don't
resolve (formula/recipe strings, mangled labels) are FLAGGED, never guessed.
Re-grounding is the higher-stakes change, so it additionally requires the
resolved id to differ from the current id. Idempotent, --dry-run, CurationEvent.

Usage
-----
    python scripts/fix_primary_term_grounding.py --mode reground --dry-run
    python scripts/fix_primary_term_grounding.py --mode canonicalize \
        --report data/import_tracking/reports/primary_term_canonicalize.tsv
"""
from __future__ import annotations

import argparse
import collections
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
NORMALIZED_DIR = REPO_ROOT / "data" / "normalized_yaml"
CURATORS = {"reground": "primary-term-regrounding-v1.0",
            "canonicalize": "primary-term-label-canonicalization-v1.0"}

# LLM-curated allowlist of approved wrong-id re-groundings (from_id -> to_id),
# each verified as a genuine cross-compound error (current id names an unrelated
# substance). Lateral synonym swaps and salt/acid downgrades (e.g. MES sodium
# salt CHEBI:62955 -> MES acid 39005; Bicine 39065; cobalamin 28911) are
# deliberately EXCLUDED — the current id there is already correct/more specific.
APPROVED_REGROUND = {
    ("CHEBI:3374", "CHEBI:31345"),    # Calcium pantothenate (was capsaicin)
    ("CHEBI:58242", "CHEBI:63043"),   # KNO3 (was Renilla luciferyl sulfate)
    ("CHEBI:59168", "CHEBI:132112"),  # Na2S2O3 (was nonaethylene glycol)
    ("CHEBI:59160", "CHEBI:77775"),   # Na2SeO4 (was triisocyanate)
    ("CHEBI:86477", "CHEBI:60720"),   # Na2SiO3 x 5 H2O (was sodium sulfite)
    ("CHEBI:65994", "CHEBI:39061"),   # ACES (was gypsosaponin C)
    ("CHEBI:62476", "CHEBI:63051"),   # (NH4)2HPO4 (was a glycoside)
    ("CHEBI:47622", "CHEBI:32029"),   # K-acetate (was generic acetate ester)
    ("CHEBI:53258", "CHEBI:30769"),   # citric acid (was sodium citrate)
    ("CHEBI:32586", "CHEBI:77775"),   # Na2SeO4 x 10 H2O (was sodium sulfate decahydrate)
    ("CHEBI:131532", "CHEBI:189426"), # Pyridoxine dihydrochloride (was pyridoxamine diHCl)
    ("CHEBI:18123", "CHEBI:229203"),  # Trigonelline HCl (was N-methylnicotinate)
    ("CHEBI:143268", "CHEBI:46756"),  # HEPES (was an imine intermediate)
}

sys.path.insert(0, str(REPO_ROOT / "scripts"))
try:
    from enrich_sssom_with_ols import normalize_ingredient_name as _norm
except Exception:
    def _norm(s):
        return s


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


class Oak:
    def __init__(self):
        from oaklib import get_adapter
        self.ad = get_adapter("sqlite:obo:chebi")
        self._lab, self._exact = {}, {}

    def label(self, cid):
        if cid not in self._lab:
            try:
                self._lab[cid] = self.ad.label(cid) or ""
            except Exception:
                self._lab[cid] = ""
        return self._lab[cid]

    def exact(self, name):
        if name in self._exact:
            return self._exact[name]
        out = set()
        try:
            for cid in list(self.ad.basic_search(name))[:12]:
                if not str(cid).startswith("CHEBI:"):
                    continue
                lbl = (self.label(cid) or "").lower()
                syns = {s.lower() for s in self.ad.entity_aliases(cid)}
                if name.lower() == lbl or name.lower() in syns:
                    out.add(str(cid))
        except Exception:
            pass
        self._exact[name] = out
        return out

    def resolve(self, name):
        """Single exact CHEBI for an ingredient name (raw or normalised), else None."""
        for q in (name, _norm(name)):
            if not q:
                continue
            hits = self.exact(q)
            if len(hits) == 1:
                return next(iter(hits))
        return None


def _tok(s):
    import re
    return set(w for w in re.sub(r"[^a-z0-9]+", " ", str(s).lower()).split() if len(w) > 2)


def _same_compound(a, b):
    """True if two CHEBI labels denote the same base compound (hydrate/charge/
    anomer variant) — i.e. they share their significant tokens. Used to AVOID
    re-grounding a correct hydrate-specific id down to its generic (e.g.
    'magnesium sulfate heptahydrate' vs 'magnesium sulfate')."""
    ta, tb = _tok(a), _tok(b)
    if not ta or not tb:
        return False
    return len(ta & tb) / min(len(ta), len(tb)) >= 0.6


def classify(pairs, oak):
    """pair (id, name) -> ('reground', new_id) | ('canonicalize', canon_label) | ('flag', reason)."""
    decisions = {}
    for (cid, name) in pairs:
        true_chebi = oak.resolve(name)
        canon = oak.label(cid)
        if true_chebi and true_chebi != cid:
            # Only re-ground when the current id is a chemically UNRELATED
            # compound. If current & resolved share their base compound (a
            # hydrate / charge / anomer variant), the current more-specific id
            # is usually right — never downgrade it; flag instead.
            if _same_compound(canon, oak.label(true_chebi)):
                decisions[(cid, name)] = ("flag", None, None)
            else:
                decisions[(cid, name)] = ("reground", true_chebi, oak.label(true_chebi))
        elif true_chebi == cid:
            if canon and canon != name:
                decisions[(cid, name)] = ("canonicalize", canon, None)
            else:
                decisions[(cid, name)] = ("ok", None, None)
        else:
            decisions[(cid, name)] = ("flag", None, None)
    return decisions


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mode", choices=["reground", "canonicalize"], required=True)
    ap.add_argument("--yaml-dir", type=Path, default=NORMALIZED_DIR)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", type=Path, default=None)
    args = ap.parse_args(argv)

    files = sorted(args.yaml_dir.rglob("*.yaml"))
    # collect distinct primary-term pairs
    pairs = set()
    parsed = {}
    for p in files:
        try:
            d = yaml.safe_load(p.read_text())
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        parsed[p] = d
        for ing in iter_ingredients(d):
            t = ing.get("term")
            if isinstance(t, dict) and str(t.get("id", "")).startswith("CHEBI:"):
                pairs.add((str(t["id"]), str(ing.get("preferred_term", "")).strip()))

    print(f"classifying {len(pairs)} distinct primary-term pairs via OAK ...")
    oak = Oak()
    decisions = classify(pairs, oak)
    tally = collections.Counter(v[0] for v in decisions.values())
    print("classification:", dict(tally))

    curator = CURATORS[args.mode]
    changelog, total_files, total = [], 0, 0
    for p, d in parsed.items():
        local = 0
        for ing in iter_ingredients(d):
            t = ing.get("term")
            if not isinstance(t, dict) or not str(t.get("id", "")).startswith("CHEBI:"):
                continue
            key = (str(t["id"]), str(ing.get("preferred_term", "")).strip())
            dec = decisions.get(key)
            if not dec:
                continue
            action, a, b = dec
            if args.mode == "reground" and action == "reground" and (key[0], a) in APPROVED_REGROUND:
                changelog.append((key[1], key[0], a)); t["id"], t["label"] = a, b; local += 1
            elif args.mode == "canonicalize" and action == "canonicalize":
                changelog.append((key[1], key[0], a)); t["label"] = a; local += 1
        if local and not args.dry_run:
            d.setdefault("curation_history", []).append({
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "curator": curator,
                "action": ("Re-grounded wrong primary term id (OAK-verified)"
                           if args.mode == "reground" else
                           "Canonicalized primary term label to OBO canonical (OAK)"),
                "notes": f"{local} primary term(s); ingredient name resolved by OAK sqlite:obo:chebi.",
            })
            p.write_text(yaml.safe_dump(d, default_flow_style=False, allow_unicode=True, sort_keys=False))
        if local:
            total_files += 1; total += local

    print(f"{'[DRY RUN] ' if args.dry_run else ''}mode={args.mode} files changed: {total_files} | "
          f"primary terms {args.mode}d: {total}")
    if args.report and changelog:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        with args.report.open("w") as fh:
            fh.write("preferred_term\tfrom_id\tto_id_or_label\n")
            for r in changelog:
                fh.write("\t".join(map(str, r)) + "\n")
        print(f"wrote {args.report} ({len(changelog)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
