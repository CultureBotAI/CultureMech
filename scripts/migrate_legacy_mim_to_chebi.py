#!/usr/bin/env python3
"""Refresh stale legacy MediaIngredientMech links to MIM's current CHEBI keying.

Background
----------
MediaIngredientMech migrated from minting `MediaIngredientMech:NNNNNN`
identifiers to keying its curated ingredients by ontology id (predominantly
CHEBI). Its current canonical `data/curated/mapped_ingredients.yaml` carries
zero `MediaIngredientMech:` ids. CultureMech records enriched before that
migration still carry legacy `mediaingredientmech_term` links pointing at the
deprecated id scheme.

This migration (refresh-replace, id-safe) rewrites those links to the new
`mediaingredientmech_chebi_term` field:

  - **CHEBI present** — the ingredient already carries its own CHEBI `term`
    (~99.8% do). If that CHEBI is in current MIM, replace the legacy field
    with `mediaingredientmech_chebi_term` using the ingredient's OWN CHEBI id
    and label. We deliberately do NOT import MIM's `preferred_term` (it
    diverges ~21% of the time, occasionally semantically), so no labels change.
  - **CHEBI gap (the ~203)** — legacy link but no CHEBI `term`. Try a
    name/synonym match against current MIM; on a CHEBI hit, set the
    ingredient's `term` (closes the grounding gap) and add the chebi_term.
  - **Unmappable** — CHEBI absent from current MIM and no name match: the
    legacy `mediaingredientmech_term` is left untouched.

Also emits a grounding-divergence report (CHEBI ids where the CultureMech
ingredient label and MIM's preferred_term differ) for downstream audit.

Files are re-emitted with PyYAML `safe_dump` (default_flow_style=False,
sort_keys=False) — the exact settings the corpus was written with — so every
unchanged field round-trips byte-identically and diffs stay surgical.

Usage
-----
    python scripts/migrate_legacy_mim_to_chebi.py --mim-repo ../MediaIngredientMech --dry-run
    python scripts/migrate_legacy_mim_to_chebi.py --mim-repo ../MediaIngredientMech \
        --report data/import_tracking/reports/mim_grounding_divergences.tsv
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
CURATOR = "mim-legacy-to-chebi-migration-v1.0"


def _norm(s) -> str:
    return " ".join(str(s or "").lower().split())


# Leading stereochemical descriptors. Two names with different descriptors
# (e.g. "DL-alanine" vs "L-alanine") are distinct compounds and must not be
# coalesced into a single authoritative CHEBI grounding.
_STEREO_RE = re.compile(
    r"^\s*(dl|d|l|rac|\(±\)|\(\+/-\)|\(\+\)|\(-\)|\(rs\)|\(r\)|\(s\))[-\s]",
    re.IGNORECASE,
)


def _stereo_prefix(s) -> str:
    """Return the normalized leading stereo descriptor of a name, or ''."""
    m = _STEREO_RE.match(str(s or ""))
    return m.group(1).lower() if m else ""


def _resolve_chebi(ing: dict, loader, divergences):
    """Return (chebi_id, label, set_term_value, mode) or (None, ...) if unmappable."""
    term = ing.get("term") if isinstance(ing.get("term"), dict) else None
    cid = str(term.get("id")) if term else ""

    if cid.startswith("CHEBI:") and cid in loader.by_chebi:
        mim = loader.by_chebi[cid]
        cm_lbl, mim_lbl = ing.get("preferred_term") or "", mim.get("preferred_term") or ""
        if _norm(cm_lbl) != _norm(mim_lbl):
            divergences.add((cid, str(cm_lbl), str(mim_lbl),
                             str((mim.get("ontology_mapping") or {}).get("ontology_label") or "")))
        # id-safe label: keep the ingredient's existing CHEBI label, else its name
        label = (term.get("label") or ing.get("preferred_term") or "")
        return cid, str(label), None, "chebi"

    if not cid.startswith("CHEBI:"):
        # CHEBI-grounding gap: resolve by name/synonym against current MIM.
        # Only EXACT name or synonym hits are allowed to mint an authoritative
        # `term`. Sub-exact fuzzy hits are too unreliable -- they coalesce
        # distinct compounds (sulfite/silicate, pyridoxine/pyridoxamine,
        # sulfate/selenate) into wrong groundings -- so disable fuzzy here
        # (fuzzy_threshold > 1.0) and reject anything that is not exact/synonym.
        match = loader.find_match(
            ing.get("preferred_term", ""), None, fuzzy_threshold=1.01
        )
        if match and match.get("match_method") in ("exact_name", "synonym"):
            # Never coalesce DL/D/L stereoisomers: if the ingredient and the
            # matched MIM entry carry different stereo descriptors, leave it
            # ungrounded rather than mint a wrong authoritative grounding.
            if _stereo_prefix(ing.get("preferred_term")) == _stereo_prefix(
                match.get("preferred_term")
            ):
                om = match.get("ontology_mapping") or {}
                mc = om.get("ontology_id")
                if not (mc and str(mc).startswith("CHEBI:")):
                    ident = str(match.get("identifier", ""))
                    mc = ident if ident.startswith("CHEBI:") else None
                if mc:
                    term_label = match.get("preferred_term") or ing.get("preferred_term")
                    # Only fill `term` when the ingredient has NO existing
                    # grounding (cid is "" -> term absent or its id is empty).
                    # An existing non-CHEBI grounding (FOODON/ENVO/NCIT) must
                    # be preserved, not clobbered by the name match.
                    set_term = {"id": str(mc), "label": str(term_label)} if not cid else None
                    return str(mc), str(ing.get("preferred_term") or term_label), set_term, \
                        f"namematch_{match.get('match_method', '?')}"
    return None, None, None, None


def _rewrite_entry(ing: dict, loader, divergences) -> bool:
    """Replace legacy mediaingredientmech_term in place; preserve key order."""
    if not isinstance(ing, dict) or "mediaingredientmech_term" not in ing:
        return False
    chebi, label, set_term, _mode = _resolve_chebi(ing, loader, divergences)
    if not chebi:
        return False  # unmappable -> leave legacy field intact

    rebuilt = {}
    for k, v in ing.items():
        if k == "term" and set_term is not None:
            # set_term is only non-None when the ingredient had no existing
            # grounding (see _resolve_chebi), so this fills a true gap rather
            # than overwriting an existing non-CHEBI term.
            rebuilt[k] = set_term
        elif k == "mediaingredientmech_term":
            rebuilt["mediaingredientmech_chebi_term"] = {"id": chebi, "label": label}
        else:
            rebuilt[k] = v
    if set_term is not None and "term" not in ing:
        # ingredient had no term at all: insert it just before the chebi link
        ordered = {}
        for k, v in rebuilt.items():
            if k == "mediaingredientmech_chebi_term":
                ordered["term"] = set_term
            ordered[k] = v
        rebuilt = ordered
    ing.clear()
    ing.update(rebuilt)
    return True


def migrate_file(path: Path, loader, divergences, dry_run: bool) -> int:
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict):
        return 0
    changed = 0
    # ingredient lists live in three places: `ingredients`, the standalone
    # solution-record `composition` (top level), and nested `solutions[].composition`.
    for ing in data.get("ingredients") or []:
        if _rewrite_entry(ing, loader, divergences):
            changed += 1
    for ing in data.get("composition") or []:
        if _rewrite_entry(ing, loader, divergences):
            changed += 1
    for sol in data.get("solutions") or []:
        if isinstance(sol, dict):
            for comp in sol.get("composition") or []:
                if _rewrite_entry(comp, loader, divergences):
                    changed += 1

    if changed and not dry_run:
        data.setdefault("curation_history", []).append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "curator": CURATOR,
            "action": "Refreshed legacy MediaIngredientMech links to CHEBI keying",
            "notes": (f"Replaced {changed} legacy mediaingredientmech_term link(s) with "
                      "mediaingredientmech_chebi_term (id-safe: ingredient's own CHEBI + "
                      "label). MIM deprecated the MediaIngredientMech:NNNNNN id scheme."),
        })
        path.write_text(yaml.safe_dump(data, default_flow_style=False,
                                       allow_unicode=True, sort_keys=False))
    return changed


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mim-repo", type=Path, required=True)
    ap.add_argument("--yaml-dir", type=Path, default=NORMALIZED_DIR)
    ap.add_argument("--limit", type=int, default=None, help="Process at most N files (testing).")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", type=Path, default=None, help="Write grounding-divergence TSV here.")
    args = ap.parse_args(argv)

    sys.path.insert(0, str(REPO_ROOT / "src"))
    from culturemech.enrich.mediaingredientmech_loader import MediaIngredientMechLoader
    loader = MediaIngredientMechLoader(args.mim_repo)

    files = [p for p in sorted(args.yaml_dir.rglob("*.yaml"))
             if "mediaingredientmech_term:" in p.read_text()]
    if args.limit:
        files = files[: args.limit]

    divergences: set = set()
    total_files = total_links = 0
    for p in files:
        n = migrate_file(p, loader, divergences, args.dry_run)
        if n:
            total_files += 1
            total_links += n

    print(f"{'[DRY RUN] ' if args.dry_run else ''}files changed: {total_files} | "
          f"links refreshed: {total_links} | grounding divergences: {len(divergences)}")

    if args.report and divergences:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        with args.report.open("w") as fh:
            fh.write("chebi_id\tculturemech_label\tmim_preferred_term\tmim_ontology_label\n")
            for row in sorted(divergences):
                fh.write("\t".join(row) + "\n")
        print(f"wrote divergence report: {args.report} ({len(divergences)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
