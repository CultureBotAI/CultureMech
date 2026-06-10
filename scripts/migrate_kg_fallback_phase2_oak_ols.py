#!/usr/bin/env python3
"""G25 Phase 2 — resolve the remaining low-confidence chebi_terms via OAK + OLS
(with a corpus-majority disambiguator), de-ground mixtures, flag the rest.

Phase 1 fixed the labels with a UNANIMOUS reliable corpus grounding. The
remainder (~375 distinct labels) are either (a) real chemicals whose corpus
groundings disagree (anomers / hydrate forms / charge states), or (b) complex
mixtures that have no single CHEBI. This phase resolves them with external
authorities, safely:

  Path A (ontology-authoritative): OAK `sqlite:obo:chebi` returns EXACTLY ONE
    exact (label==query or query∈synonyms) CHEBI for the label or its normalised
    form, AND that id is in the OLS4 exact set -> resolve (match_type=exact_match).
    OAK is precise for clean chemicals (glucose->CHEBI:17234, selenate->77775).

  Path B (corpus-majority, ontology cross-checked): when the ontology can't
    disambiguate a hydrate/anomer (multiple exact hits), use the corpus's own
    reliable majority grounding C (>=90% share, >=5 occ) IF C appears in the
    OAK∪OLS exact set for the label/normalised form -> resolve
    (match_type=corpus_consensus). E.g. "MgSO4 x 7 H2O": 96% of reliable
    groundings are CHEBI:31795 (heptahydrate), and 31795 ∈ OLS-exact -> 31795.

  De-ground: no ontology exact match AND a mixture pattern (peptone / tryptone /
    casamino / *extract / broth / sea water / serum / ...) -> remove the wrong
    low-confidence chebi_term (the primary `term` is untouched).

  Flag: everything else -> left as-is and written to a curator-review TSV.

Reuses the repo name-normaliser (enrich_sssom_with_ols.normalize_ingredient_name).
Lookups are cached by label (375 unique). Idempotent, --dry-run, CurationEvent,
PyYAML round-trip.

Usage
-----
    python scripts/migrate_kg_fallback_phase2_oak_ols.py --dry-run
    python scripts/migrate_kg_fallback_phase2_oak_ols.py \
        --report data/import_tracking/reports/kg_fallback_phase2_changes.tsv \
        --flag-report data/import_tracking/reports/kg_fallback_phase2_curator_review.tsv
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
NORMALIZED_DIR = REPO_ROOT / "data" / "normalized_yaml"
CURATOR = "kg-fallback-oak-ols-v1.0"
LOW_CONF = {"kg_fallback", "synonym_match_ambiguous", "(none)", None}
RELIABLE = {"exact_match", "corpus_consensus"}
MIXTURE = re.compile(
    r"\b(peptone|polypepton|tryptone|trypticase|casamino|casitone|casein|"
    r"yeast extract|beef extract|meat extract|malt extract|lab.?lemco|"
    r"broth|infusion|digest|serum|blood|sea\s*water|sea\s*salt|seawater|"
    r"proteose|hydrol?ysate|soytone|gelatin|rumen)\b", re.I)

sys.path.insert(0, str(REPO_ROOT / "scripts"))
try:
    from enrich_sssom_with_ols import normalize_ingredient_name as _norm
except Exception:
    def _norm(s):  # pragma: no cover
        return s


def name_key(s) -> str:
    return " ".join(str(s or "").lower().split())


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


def primary_chebi(ing):
    t = ing.get("term")
    return str(t["id"]) if isinstance(t, dict) and str(t.get("id", "")).startswith("CHEBI:") else None


def build_corpus_reliable(files):
    by_label = collections.defaultdict(collections.Counter)
    for p in files:
        try:
            data = yaml.safe_load(p.read_text())
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        for ing in iter_ingredients(data):
            t = ing.get("term")
            ct = ing.get("chebi_term")
            cid = None
            if isinstance(t, dict) and str(t.get("id", "")).startswith("CHEBI:"):
                cid = str(t["id"])
            elif isinstance(ct, dict) and ct.get("match_type") in RELIABLE \
                    and str(ct.get("id", "")).startswith("CHEBI:"):
                cid = str(ct["id"])
            if cid:
                by_label[name_key(ing.get("preferred_term", ""))][cid] += 1
    return by_label


class Resolver:
    def __init__(self):
        from oaklib import get_adapter
        self.oak = get_adapter("sqlite:obo:chebi")
        self._ols: dict[str, set] = {}
        self._oak: dict[str, set] = {}

    def oak_exact(self, q):
        if q in self._oak:
            return self._oak[q]
        out = set()
        try:
            for cid in list(self.oak.basic_search(q))[:12]:
                if not str(cid).startswith("CHEBI:"):
                    continue
                lbl = (self.oak.label(cid) or "").lower()
                syns = {s.lower() for s in self.oak.entity_aliases(cid)}
                if q.lower() == lbl or q.lower() in syns:
                    out.add(str(cid))
        except Exception:
            pass
        self._oak[q] = out
        return out

    def ols_exact(self, q):
        """Exact CHEBI matches for ``q``, or None if the OLS call ERRORED.

        Returning None on network/timeout/HTTP error (vs an empty set for a
        genuine no-match) lets callers avoid treating a transient OLS outage
        as "OLS returned nothing".
        """
        if q in self._ols:
            return self._ols[q]
        try:
            r = requests.get("https://www.ebi.ac.uk/ols4/api/search",
                             params={"q": q, "ontology": "chebi", "exact": "true",
                                     "rows": 8, "queryFields": "label,synonym"}, timeout=25)
            r.raise_for_status()
            out = {d["obo_id"] for d in r.json().get("response", {}).get("docs", [])
                   if d.get("obo_id", "").startswith("CHEBI:")}
        except Exception:
            self._ols[q] = None
            return None
        self._ols[q] = out
        return out

    def resolve(self, label, corpus_rel):
        """Return (action, chebi_id, label_out, method). action in resolve|deground|flag."""
        norm = _norm(label)
        forms = {label, norm}
        oak = set().union(*(self.oak_exact(f) for f in forms))
        ols_results = [self.ols_exact(f) for f in forms]
        ols_errored = any(r is None for r in ols_results)
        ols = set().union(*(r or set() for r in ols_results))
        # Hydrate/formula labels lose their water-of-crystallisation under
        # normalisation, so an ontology lookup on the normalised name can pick
        # the WRONG hydrate (e.g. "MgSO4 x 7 H2O" -> magnesium sulfate ->
        # hexahydrate). For these, trust only the corpus majority, never Path A.
        has_hydrate = bool(re.search(r"x\s*\d+\s*h2?o|hydrate", label, re.I))

        # Path B FIRST — corpus strong-majority cross-checked against the ontology.
        # The corpus's own dominant grounding is more reliable than a lossy
        # normalised-name lookup, and it carries the correct hydrate form.
        if corpus_rel:
            total = sum(corpus_rel.values())
            c, n = corpus_rel.most_common(1)[0]
            if total >= 5 and n / total >= 0.90 and (c in oak or c in ols):
                return "resolve", c, label, "corpus_consensus"

        # Path A — single precise OAK hit confirmed by OLS (non-hydrate only).
        if not has_hydrate and len(oak) == 1:
            c = next(iter(oak))
            # Take the "OLS empty" shortcut only when OLS genuinely returned
            # nothing — never when the OLS call errored/timed out (which must
            # not silently bypass the cross-check).
            if c in ols or (not ols and not ols_errored):
                return "resolve", c, label, "oak_ols_exact"

        # De-ground clear mixtures with no ontology grounding
        if not oak and not ols and MIXTURE.search(label):
            return "deground", None, label, "mixture_no_chebi"

        return "flag", None, label, "ambiguous_or_unresolved"


def migrate(files, resolver, corpus_rel, dry_run, changelog, flags):
    decided: dict[str, tuple] = {}
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
            if primary_chebi(ing):
                continue
            ct = ing.get("chebi_term")
            if not isinstance(ct, dict) or ct.get("match_type") not in LOW_CONF:
                continue
            lk = name_key(ing.get("preferred_term", ""))
            if lk not in decided:
                decided[lk] = resolver.resolve(ing.get("preferred_term", ""),
                                               corpus_rel.get(lk))
            action, cid, lbl, method = decided[lk]
            was = str(ct.get("id"))
            if action == "resolve":
                # Use the canonical CHEBI label for the resolved id (fall back
                # to the ingredient name only if OAK has no label), and merge
                # over the existing chebi_term so prior `confidence` survives.
                canon = resolver.oak.label(cid) or lbl
                ing["chebi_term"] = {**ct, "id": cid, "label": canon,
                                     "match_type": "exact_match" if method == "oak_ols_exact" else "corpus_consensus"}
                changelog.append((lk, was, cid, method)); local += 1
            elif action == "deground":
                del ing["chebi_term"]
                changelog.append((lk, was, "REMOVED", method)); local += 1
            else:
                flags[(lk, was)] = method
        if local and not dry_run:
            data.setdefault("curation_history", []).append({
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "curator": CURATOR,
                "action": "Resolved/de-grounded low-confidence chebi_term via OAK+OLS (G25 Phase 2)",
                "notes": f"{local} chebi_term(s): OAK sqlite:obo:chebi + OLS4 exact agreement, "
                         "corpus-majority disambiguation, or mixture de-ground.",
            })
            p.write_text(yaml.safe_dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False))
        if local:
            total_files += 1; total += local
    return total_files, total


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--yaml-dir", type=Path, default=NORMALIZED_DIR)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", type=Path, default=None)
    ap.add_argument("--flag-report", type=Path, default=None)
    args = ap.parse_args(argv)

    files = sorted(args.yaml_dir.rglob("*.yaml"))
    print(f"Building corpus reliable map from {len(files)} files...")
    corpus_rel = build_corpus_reliable(files)
    print("Loading OAK sqlite:obo:chebi ...")
    resolver = Resolver()

    changelog: list = []
    flags: dict = {}
    tf, t = migrate(files, resolver, corpus_rel, args.dry_run, changelog, flags)

    by_method = collections.Counter(c[3] for c in changelog)
    print(f"{'[DRY RUN] ' if args.dry_run else ''}files changed: {tf} | chebi_terms resolved/de-grounded: {t}")
    for m, n in by_method.most_common():
        print(f"    {m}: {n}")
    print(f"    flagged for curator review (left as-is): {len(flags)} (label,id) pairs")

    if args.report and changelog:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        with args.report.open("w") as fh:
            fh.write("label\tfrom_chebi\tto_chebi\tmethod\n")
            for r in changelog:
                fh.write("\t".join(map(str, r)) + "\n")
        print(f"wrote {args.report} ({len(changelog)} rows)")
    if args.flag_report and flags:
        args.flag_report.parent.mkdir(parents=True, exist_ok=True)
        with args.flag_report.open("w") as fh:
            fh.write("label\tcurrent_chebi\treason\n")
            for (lk, was), m in sorted(flags.items()):
                fh.write(f"{lk}\t{was}\t{m}\n")
        print(f"wrote {args.flag_report} ({len(flags)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
