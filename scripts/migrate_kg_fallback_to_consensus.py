#!/usr/bin/env python3
"""G25 Phase 1 — replace low-confidence kg_fallback chebi_terms with the
corpus's own reliable consensus grounding (zero external calls).

The `chebi_term` field carries a large low-confidence layer (`match_type:
kg_fallback` / `synonym_match_ambiguous`, ~61% of all chebi_terms) that is
frequently wrong (e.g. "Distilled water" -> CHEBI:6636 magnesium dichloride).
~82% of those occurrences have a label that ALSO appears with a *reliable*
grounding elsewhere in the corpus, so they can be fixed by borrowing that
consensus — no OAK/OLS lookup required.

Reliable grounding for a label = its primary `term` (when CHEBI) or an
`exact_match` `chebi_term`, seen on any ingredient. A label is *eligible* only
when its reliable groundings are UNANIMOUS (a single distinct CHEBI id) — labels
with conflicting reliable ids (the G23 same-name-multiple-CHEBI cases, e.g.
hydrate variants) are deferred to Phase 2 (OAK + OLS).

For each ingredient whose grounding is the low-confidence layer (a chebi_term
with a non-exact match_type, and no CHEBI primary `term`), if its label has a
unanimous reliable consensus, the chebi_term is rewritten to that id+label with
`match_type: corpus_consensus`. Idempotent, --dry-run, CurationEvent, PyYAML
round-trip (surgical diffs).

Usage
-----
    python scripts/migrate_kg_fallback_to_consensus.py --dry-run
    python scripts/migrate_kg_fallback_to_consensus.py --report data/import_tracking/reports/kg_fallback_consensus_changes.tsv
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
CURATOR = "kg-fallback-consensus-v1.0"
LOW_CONF_MATCH = {"kg_fallback", "synonym_match_ambiguous", "(none)", None}


def name_key(s) -> str:
    return " ".join(str(s or "").lower().split())


def iter_ingredients(data: dict):
    if not isinstance(data, dict):
        return
    for grp in ("ingredients", "composition"):
        for ing in data.get(grp) or []:
            if isinstance(ing, dict):
                yield ing
    for sol in data.get("solutions") or []:
        if isinstance(sol, dict):
            for ing in sol.get("composition") or []:
                if isinstance(ing, dict):
                    yield ing


def primary_chebi(ing: dict) -> str | None:
    t = ing.get("term")
    if isinstance(t, dict) and str(t.get("id", "")).startswith("CHEBI:"):
        return str(t["id"])
    return None


def reliable_grounding(ing: dict):
    """Return (id, label) from a reliable grounding on this ingredient, else None."""
    t = ing.get("term")
    if isinstance(t, dict) and str(t.get("id", "")).startswith("CHEBI:"):
        return str(t["id"]), t.get("label")
    ct = ing.get("chebi_term")
    if isinstance(ct, dict) and ct.get("match_type") == "exact_match" \
            and str(ct.get("id", "")).startswith("CHEBI:"):
        return str(ct["id"]), ct.get("label")
    return None


def build_consensus(files):
    """label_key -> (chebi_id, label) when reliable groundings are unanimous."""
    by_label: dict[str, dict] = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    for p in files:
        try:
            data = yaml.safe_load(p.read_text())
        except Exception:
            continue
        for ing in iter_ingredients(data):
            rg = reliable_grounding(ing)
            if rg:
                key = name_key(ing.get("preferred_term", ""))
                if not key:
                    continue  # don't pool label-less ingredients in a shared "" bucket
                cid, lbl = rg
                by_label[key][cid][lbl or cid] += 1
    consensus = {}
    for label, ids in by_label.items():
        if len(ids) == 1:                       # unanimous single id
            cid = next(iter(ids))
            best_label = ids[cid].most_common(1)[0][0]
            consensus[label] = (cid, best_label)
    return consensus


def migrate_file(path: Path, consensus: dict, dry_run: bool, changelog: list) -> int:
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict):
        return 0
    local = 0
    for ing in iter_ingredients(data):
        if primary_chebi(ing):
            continue                            # already reliably grounded
        ct = ing.get("chebi_term")
        if not isinstance(ct, dict) or ct.get("match_type") not in LOW_CONF_MATCH:
            continue
        key = name_key(ing.get("preferred_term", ""))
        if not key:
            continue  # never borrow grounding for a label-less ingredient
        target = consensus.get(key)
        if not target:
            continue
        cid, lbl = target
        was = str(ct.get("id"))
        # Merge over the existing chebi_term so prior metadata (e.g.
        # `confidence`) survives the consensus rewrite instead of being dropped.
        ing["chebi_term"] = {**ct, "id": cid, "label": lbl, "match_type": "corpus_consensus"}
        changelog.append((str(path.relative_to(REPO_ROOT)) if str(path).startswith(str(REPO_ROOT)) else str(path),
                          ing.get("preferred_term", ""), was, cid))
        local += 1
    if local and not dry_run:
        data.setdefault("curation_history", []).append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "curator": CURATOR,
            "action": "Replaced low-confidence kg_fallback chebi_term with corpus consensus",
            "notes": (f"Re-grounded {local} chebi_term(s) to the unanimous reliable CHEBI "
                      "for the ingredient label seen elsewhere in the corpus (G25 Phase 1, "
                      "zero external lookups)."),
        })
        path.write_text(yaml.safe_dump(data, default_flow_style=False,
                                       allow_unicode=True, sort_keys=False))
    return local


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--yaml-dir", type=Path, default=NORMALIZED_DIR)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", type=Path, default=None)
    args = ap.parse_args(argv)

    files = sorted(args.yaml_dir.rglob("*.yaml"))
    print(f"Building consensus map from {len(files)} files...")
    consensus = build_consensus(files)
    print(f"  unanimous-consensus labels available: {len(consensus)}")

    changelog: list = []
    total_files = total = 0
    for p in files:
        n = migrate_file(p, consensus, args.dry_run, changelog)
        if n:
            total_files += 1
            total += n

    print(f"{'[DRY RUN] ' if args.dry_run else ''}files changed: {total_files} | "
          f"kg_fallback chebi_terms re-grounded to consensus: {total}")

    if args.report and changelog:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        with args.report.open("w") as fh:
            fh.write("file\tpreferred_term\tfrom_chebi\tto_chebi\n")
            for row in changelog:
                fh.write("\t".join(map(str, row)) + "\n")
        print(f"wrote change report: {args.report} ({len(changelog)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
