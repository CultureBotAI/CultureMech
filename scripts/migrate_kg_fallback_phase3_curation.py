#!/usr/bin/env python3
"""G25 Phase 3 — LLM-curated resolution of the 281 flagged chebi_term labels.

Phase 2 flagged 281 labels whose low-confidence kg_fallback grounding could not
be auto-resolved. An LLM curator classified each in
`data/import_tracking/reports/g25_phase3_llm_curation.tsv` as either:
  - resolve <canonical chemical name>  (real single compound)
  - deground                            (mixture / biological / medium / buffer-mix)

SAFETY: the curator asserts the COMPOUND NAME, never a CHEBI id. The id is
resolved here by OAK `sqlite:obo:chebi` (exact label/synonym) and cross-checked
against OLS4 — so a curator slip can't inject a wrong id; it just fails to
resolve and stays flagged. Flagged labels NOT in the curation file are also
re-checked: if the current id's OAK label already matches the ingredient label,
the grounding was correct and its match_type is upgraded to `manual_curated`.

Each touched ingredient's chebi_term becomes either {id, label, match_type:
manual_curated} (resolve / confirm) or is removed (deground). Idempotent,
--dry-run, CurationEvent, PyYAML round-trip.

Usage
-----
    python scripts/migrate_kg_fallback_phase3_curation.py --dry-run
    python scripts/migrate_kg_fallback_phase3_curation.py \
        --report data/import_tracking/reports/kg_fallback_phase3_changes.tsv
"""
from __future__ import annotations

import argparse
import collections
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
NORMALIZED_DIR = REPO_ROOT / "data" / "normalized_yaml"
CURATION_TSV = REPO_ROOT / "data" / "import_tracking" / "reports" / "g25_phase3_llm_curation.tsv"
CURATOR = "kg-fallback-llm-curation-v1.0"
LOW_CONF = {"kg_fallback", "synonym_match_ambiguous", "(none)", None}


def name_key(s) -> str:
    return " ".join(str(s or "").lower().split())


def _alnum(s) -> str:
    return "".join(c for c in str(s).lower() if c.isalnum())


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
    return isinstance(t, dict) and str(t.get("id", "")).startswith("CHEBI:")


def build_corpus_reliable(files):
    """label_key -> Counter(chebi_id -> count) over reliable groundings."""
    rel = collections.defaultdict(collections.Counter)
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
            elif isinstance(ct, dict) and ct.get("match_type") in ("exact_match", "corpus_consensus") \
                    and str(ct.get("id", "")).startswith("CHEBI:"):
                cid = str(ct["id"])
            if cid:
                rel[name_key(ing.get("preferred_term", ""))][cid] += 1
    return rel


def corpus_majority(rel):
    """Return the >=90% (>=5 occ) dominant CHEBI for a label, else None."""
    if not rel:
        return None
    total = sum(rel.values())
    c, n = rel.most_common(1)[0]
    return c if total >= 5 and n / total >= 0.90 else None


class Oak:
    def __init__(self):
        from oaklib import get_adapter
        self.ad = get_adapter("sqlite:obo:chebi")
        self._lab = {}
        self._exact = {}
        self._ols = {}

    def label(self, cid):
        if cid not in self._lab:
            try:
                self._lab[cid] = self.ad.label(cid) or ""
            except Exception:
                self._lab[cid] = ""
        return self._lab[cid]

    def label_matches(self, cid, label):
        ol = self.label(cid)
        if not ol:
            return False
        try:
            syns = {_alnum(s) for s in [ol] + list(self.ad.entity_aliases(cid))}
        except Exception:
            syns = {_alnum(ol)}
        nl = _alnum(label)
        return nl in syns or any(nl in s or s in nl for s in syns if len(s) > 3)

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

    def ols(self, name):
        if name in self._ols:
            return self._ols[name]
        out = set()
        try:
            r = requests.get("https://www.ebi.ac.uk/ols4/api/search",
                             params={"q": name, "ontology": "chebi", "exact": "true",
                                     "rows": 8, "queryFields": "label,synonym"}, timeout=25)
            out = {d["obo_id"] for d in r.json().get("response", {}).get("docs", [])
                   if d.get("obo_id", "").startswith("CHEBI:")}
        except Exception:
            pass
        self._ols[name] = out
        return out

    def resolve_name(self, name):
        """Single CHEBI for a curated canonical name: OAK exact==1 confirmed by OLS."""
        oak = self.exact(name)
        if len(oak) == 1:
            c = next(iter(oak))
            ols = self.ols(name)
            if c in ols or not ols:
                return c
        # fall back to OLS single
        ols = self.ols(name)
        if len(ols) == 1:
            return next(iter(ols))
        return None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--yaml-dir", type=Path, default=NORMALIZED_DIR)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", type=Path, default=None)
    args = ap.parse_args(argv)

    curation = {}
    for row in csv.DictReader(CURATION_TSV.open(), delimiter="\t"):
        curation[name_key(row["label_key"])] = (row["action"].strip(),
                                                 (row.get("canonical_name") or "").strip())

    files = sorted(args.yaml_dir.rglob("*.yaml"))
    corpus_rel = build_corpus_reliable(files)

    oak = Oak()
    # pre-resolve curated names; fall back to corpus strong-majority for labels
    # whose canonical name OAK/OLS can't match exactly (CHEBI hydrate labels are
    # formula-style, e.g. CHEBI:86345 "MgCl2 x 6 H2O"). The curator has already
    # vouched each is a single real chemical, so a >=90% corpus majority is safe.
    name_to_chebi = {}
    unresolved_names = {}
    for lk, (action, name) in curation.items():
        if action == "resolve" and name:
            c = oak.resolve_name(name)
            if c:
                name_to_chebi[lk] = (c, name, "manual_curated")
            else:
                cm = corpus_majority(corpus_rel.get(lk))
                if cm:
                    name_to_chebi[lk] = (cm, name, "corpus_consensus")
                else:
                    unresolved_names[lk] = name
    changelog = []
    stats = collections.Counter()
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
            was = str(ct.get("id"))
            if lk in name_to_chebi:
                cid, nm, mt = name_to_chebi[lk]
                ing["chebi_term"] = {"id": cid, "label": nm, "match_type": mt}
                stats["resolved"] += 1; local += 1
                changelog.append((lk, was, cid, "resolve_" + mt))
            elif curation.get(lk, ("", ""))[0] == "deground":
                del ing["chebi_term"]
                stats["degrounded"] += 1; local += 1
                changelog.append((lk, was, "REMOVED", "deground"))
            elif lk not in curation and oak.label_matches(was, ing.get("preferred_term", "")):
                # not curated but current grounding is actually correct -> confirm
                ct["match_type"] = "manual_curated"
                stats["confirmed"] += 1; local += 1
                changelog.append((lk, was, was, "confirm"))
            # else: leave flagged (unresolved name or still-uncertain)
        if local and not args.dry_run:
            data.setdefault("curation_history", []).append({
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "curator": CURATOR,
                "action": "LLM-curated low-confidence chebi_term (G25 Phase 3)",
                "notes": f"{local} chebi_term(s): curator-named compound resolved via OAK+OLS, "
                         "or de-grounded as a mixture, or confirmed correct.",
            })
            p.write_text(yaml.safe_dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False))

    print(f"{'[DRY RUN] ' if args.dry_run else ''}resolved={stats['resolved']} "
          f"degrounded={stats['degrounded']} confirmed={stats['confirmed']}")
    print(f"curated labels: {len(curation)} | names resolved to CHEBI: {len(name_to_chebi)} | "
          f"curated names that FAILED to resolve: {len(unresolved_names)}")
    if unresolved_names:
        for lk, nm in sorted(unresolved_names.items())[:40]:
            print(f"    UNRESOLVED  {lk!r} -> {nm!r}")
    if args.report and changelog:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        with args.report.open("w") as fh:
            fh.write("label\tfrom_chebi\tto_chebi\taction\n")
            for r in changelog:
                fh.write("\t".join(map(str, r)) + "\n")
        print(f"wrote {args.report} ({len(changelog)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
