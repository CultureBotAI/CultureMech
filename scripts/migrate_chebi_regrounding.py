#!/usr/bin/env python3
"""Re-ground CHEBI mis-mappings found by the grounding audit (backlog G21/G22).

reports/chebi_grounding_audit.md identified CHEBI ids applied to a chemically
DIFFERENT compound than the ingredient. This script fixes the confirmed,
label-conditional cases. Each remap rule fires only when BOTH the current
(wrong) `term.id` and the ingredient's `preferred_term` match — so e.g. only the
"Pyridoxine" entries on CHEBI:131531 are touched, while correctly-labelled
"Pyridoxamine" entries are left alone.

The one exception is the CHEBI:78020 (heptacosanoate) DE-GROUND rule, which is
id-only (its label regex is empty and matches everything): heptacosanoate is
never a real media ingredient, so every field carrying that id is de-grounded
regardless of label. A few of those entries are single compounds with a
recoverable correct CHEBI (CuCl2·6H2O, K2SO4·7H2O, NaHSeO3) — they are left
ungrounded here ("better ungrounded than wrong") and queued for targeted
re-grounding in G24.

Verified correct targets (MIM curated CHEBI keying, except where MIM is itself
wrong — glycerol and casamino acids — which were verified against CHEBI directly):

  CHEBI:131531 (pyridoxamine)         + label ~pyridoxine  -> CHEBI:30961 (pyridoxine hydrochloride)
  CHEBI:15978  (glycerol 3-phosphate) + label ~glycerol*   -> CHEBI:17754 (glycerol)   [*excl. phosphate]
  CHEBI:75211  (tannic acid)          + label ~mnso4/mangan -> CHEBI:86364 (manganese sulfate monohydrate)
  CHEBI:77732  (cadmium nitrate)      + label ~ca(no3)2     -> CHEBI:64205 (calcium nitrate)
  CHEBI:32149  (sodium sulfate)       + label ~selenate/seo4 -> CHEBI:77775 (sodium selenate)
  CHEBI:78020  (heptacosanoate)       + label ~casamino     -> DE-GROUND (mixture; no single CHEBI)

Applies to every id-bearing term field on an ingredient/solution-composition
entry: `term`, `chebi_term`, `mediaingredientmech_chebi_term`. Remapped term
keeps the ingredient's own `preferred_term` as the label (id-safe). De-ground
removes the offending term field(s) entirely (better ungrounded than wrong).

Idempotent (once remapped, the wrong id is gone so re-runs are no-ops),
--dry-run, appends a CurationEvent, PyYAML safe_dump round-trip (surgical diffs).

Usage
-----
    python scripts/migrate_chebi_regrounding.py --dry-run
    python scripts/migrate_chebi_regrounding.py --report data/import_tracking/reports/chebi_regrounding_changes.tsv
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
NORMALIZED_DIR = REPO_ROOT / "data" / "normalized_yaml"
CURATOR = "chebi-regrounding-v1.0"
TERM_FIELDS = ("term", "chebi_term", "mediaingredientmech_chebi_term")

# (from_id, label_must_match, label_must_NOT_match, to_id) ; to_id None => de-ground
REMAP_RULES = [
    ("CHEBI:131531", re.compile(r"pyridoxine", re.I), None,                     "CHEBI:30961"),
    ("CHEBI:15978",  re.compile(r"glycer(ol|in)", re.I), re.compile(r"phosphate|glycerophosphate", re.I), "CHEBI:17754"),
    ("CHEBI:75211",  re.compile(r"mnso4|manganese\s*sul", re.I), None,           "CHEBI:86364"),  # sulfate-specific: don't remap other Mn salts to MnSO4
    ("CHEBI:77732",  re.compile(r"ca\(no3\)2|calcium\s*nitrate", re.I), None,    "CHEBI:64205"),
    ("CHEBI:77732",  re.compile(r"ferric\s*citrate|iron.{0,4}citrate", re.I), None, "CHEBI:144434"),  # ferric citrate monohydrate (also wrong on cadmium-nitrate id)
    ("CHEBI:32149",  re.compile(r"na2seo4|sodium\s*selen", re.I), None,          "CHEBI:77775"),  # sodium-specific: don't remap other selenates to Na2SeO4
    ("CHEBI:78020",  re.compile(r""), None,                                      None),  # heptacosanoate is never a real media ingredient: de-ground ALL (casamino, meat extract, nutrient broth, salts, ...)
    # G22 — split CHEBI:37583 (trisodium phosphate) by speciation. It holds only
    # sodium monobasic + dibasic labels (no genuine trisodium), each to its own id.
    ("CHEBI:37583",  re.compile(r"dihydrogen|monobasic", re.I), None,            "CHEBI:37585"),  # NaH2PO4 (sodium dihydrogen phosphate)
    ("CHEBI:37583",  re.compile(r"dibasic|disodium", re.I), None,                "CHEBI:34683"),  # Na2HPO4 (disodium hydrogen phosphate)
    # G24 — targeted shared-id garbage (verified individually). NOT a blanket
    # exact-name remap: MIM itself mis-grounds glycerol/casamino, so trusting it
    # wholesale would undo G21 and propagate MIM's own errors (6,519 such candidates).
    # Only the audited, chemically-confident minority entries on shared ids:
    ("CHEBI:32149",  re.compile(r"\blactate\b", re.I), None,                     "CHEBI:75228"),   # sodium lactate (was sodium sulfate)
    ("CHEBI:32149",  re.compile(r"propionate", re.I), None,                      "CHEBI:132106"),  # sodium propionate
    ("CHEBI:32149",  re.compile(r"nicl2|nickel", re.I), None,                    "CHEBI:34887"),   # nickel(II) chloride
    # Racemic DL-malate -> stereo-neutral disodium malate (NOT the (S)-specific
    # CHEBI:91261). Must precede the generic malate rule so the DL match fires
    # first (after it remaps the id off CHEBI:32149, the generic rule no longer
    # matches). Consistent with the stereo-neutral sodium-lactate rule above.
    ("CHEBI:32149",  re.compile(r"(?=.*\bdl\b)(?=.*malate)", re.I), None,        "CHEBI:91260"),   # disodium malate (racemic DL)
    ("CHEBI:32149",  re.compile(r"malate", re.I), None,                          "CHEBI:91261"),   # sodium malate
    # Stereo-UNSPECIFIED sodium malate -> stereo-neutral disodium malate (NOT the
    # (S)-specific CHEBI:91261). "Sodium malate" / "Na malate" / "Na-malate" name no
    # stereochemistry, so the neutral parent is correct, consistent with the DL-malate
    # rule above and the stereo-neutral sodium-lactate rule. The mustnot pattern keeps
    # L-/D-/DL-malate off this rule (L = (S), correct on 91261; DL already routed to
    # 91260). Fires from the current 91261 grounding, and is also reachable in a
    # from-scratch run after the generic 32149->91261 rule rewrites the id within the
    # same pass.
    ("CHEBI:91261",  re.compile(r"malate", re.I), re.compile(r"(?:dl|[dl])-?\s*malate", re.I), "CHEBI:91260"),  # disodium malate (stereo-unspecified)
    ("CHEBI:15978",  re.compile(r"agar|middlebrook|mueller|hinton|\bisp\b|whole\s*egg|broth", re.I), None, None),  # complex media de-grounded (not glycerol-3-phosphate)
]


def _entry_label(ing: dict) -> str:
    return str(ing.get("preferred_term") or "")


def rewrite_entry(ing: dict, changelog: list) -> bool:
    if not isinstance(ing, dict):
        return False
    label = _entry_label(ing)
    changed = False
    for from_id, must, mustnot, to_id in REMAP_RULES:
        if not must.search(label):
            continue
        if mustnot and mustnot.search(label):
            continue
        for fld in TERM_FIELDS:
            t = ing.get(fld)
            if isinstance(t, dict) and str(t.get("id")) == from_id:
                if to_id is None:
                    del ing[fld]
                    changelog.append((label, fld, from_id, "REMOVED"))
                else:
                    # Merge over the existing term dict so pre-existing
                    # metadata (confidence, match_type, ...) survives the
                    # regrounding rather than being dropped.
                    ing[fld] = {**t, "id": to_id, "label": label}
                    changelog.append((label, fld, from_id, to_id))
                changed = True
    return changed


def migrate_file(path: Path, text: str, dry_run: bool, changelog: list) -> int:
    data = yaml.safe_load(text)
    if not isinstance(data, dict):
        return 0
    local: list = []
    # ingredient lists live in three places: `ingredients`, the standalone
    # solution-record `composition` (top level), and nested `solutions[].composition`.
    for ing in data.get("ingredients") or []:
        rewrite_entry(ing, local)
    for ing in data.get("composition") or []:
        rewrite_entry(ing, local)
    for sol in data.get("solutions") or []:
        if isinstance(sol, dict):
            for comp in sol.get("composition") or []:
                rewrite_entry(comp, local)
    if local and not dry_run:
        data.setdefault("curation_history", []).append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "curator": CURATOR,
            "action": "Corrected CHEBI ingredient grounding (audit G21/G22)",
            "notes": (f"Re-grounded {len(local)} term reference(s) to the correct CHEBI "
                      "(see reports/chebi_grounding_audit.md). Label-conditional fixes for "
                      "pyridoxine/pyridoxamine, glycerol, MnSO4, Ca(NO3)2, ferric citrate, "
                      "selenate; CHEBI:78020 (heptacosanoate) de-grounded from all entries it "
                      "mis-tagged (casamino acids + assorted salts/extracts: meat extract, "
                      "nutrient broth, Czapek Dox agar, CuCl2·6H2O, K2SO4·7H2O, NaHSeO3, "
                      "Vitamin B12 solution)."),
        })
        path.write_text(yaml.safe_dump(data, default_flow_style=False,
                                       allow_unicode=True, sort_keys=False))
    try:
        rel = str(path.relative_to(REPO_ROOT))
    except ValueError:
        rel = str(path)
    changelog.extend((rel, *c) for c in local)
    return len(local)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--yaml-dir", type=Path, default=NORMALIZED_DIR)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", type=Path, default=None)
    args = ap.parse_args(argv)

    wrong_ids = {r[0] for r in REMAP_RULES}
    # Read each candidate once and thread the text through to migrate_file
    # (avoids reading every file a second time).
    files = []
    for p in sorted(args.yaml_dir.rglob("*.yaml")):
        text = p.read_text()
        if any(wid in text for wid in wrong_ids):
            files.append((p, text))

    changelog: list = []
    total_files = total = 0
    for p, text in files:
        n = migrate_file(p, text, args.dry_run, changelog)
        if n:
            total_files += 1
            total += n

    print(f"{'[DRY RUN] ' if args.dry_run else ''}files changed: {total_files} | "
          f"term references re-grounded: {total}")
    # per-rule summary
    from collections import Counter
    by_rule = Counter((c[3], c[4]) for c in changelog)
    for (frm, to), n in sorted(by_rule.items()):
        print(f"    {frm} -> {to}: {n}")

    if args.report and changelog:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        with args.report.open("w") as fh:
            fh.write("file\tpreferred_term\tfield\tfrom_chebi\tto_chebi\n")
            for row in changelog:
                fh.write("\t".join(map(str, row)) + "\n")
        print(f"wrote change report: {args.report} ({len(changelog)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
