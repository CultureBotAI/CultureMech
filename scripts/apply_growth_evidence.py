#!/usr/bin/env python3
"""Apply growth-evidence proposals to MediaRecipe YAMLs.

Phase C of the CultureMech literature-review pipeline (per
`/Users/marcin/.claude/plans/now-focus-on-culturemech-piped-shell.md`).

Reads workspace/reports/growth_evidence_proposals/*.yaml — emitted by
`propose_growth_evidence.py` — and applies high-confidence entries
(those with `supports: SUPPORT`) to the matching MediaRecipe YAML
under data/normalized_yaml/**/.

Per applied candidate:
  - Insert/update the target_organisms[] entry that matches its
    NCBITaxon CURIE (or append a new entry; the proposer surfaces
    binomial names, the curator must add NCBITaxon:N before SUPPORT).
  - Append new growth_metrics[] entries with PMID + verbatim snippet
    EvidenceItem.
  - Add new genome_assembly_id values without dedup-collision.
  - Append a curation_history entry:
      curator: literature_review_apply
      action: ADDED_GROWTH_EVIDENCE

Default is dry-run (prints a diff summary). `--apply` writes.

Usage:
    python3 scripts/apply_growth_evidence.py
    python3 scripts/apply_growth_evidence.py --apply
    python3 scripts/apply_growth_evidence.py --proposal-dir custom/dir --apply
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data" / "normalized_yaml"
DEFAULT_PROPOSAL_DIR = REPO_ROOT / "workspace" / "reports" / "growth_evidence_proposals"


# ---------- recipe lookup ----------

def find_recipe(stem: str) -> Path | None:
    """Locate a MediaRecipe YAML by its stem."""
    if not DATA_DIR.is_dir():
        return None
    for p in DATA_DIR.rglob(f"{stem}.yaml"):
        return p
    return None


# ---------- per-candidate application ----------

def find_organism_idx(target_organisms: list[dict], ncbitaxon: str | None,
                      preferred_term: str | None) -> int | None:
    if not target_organisms:
        return None
    for i, o in enumerate(target_organisms):
        term = o.get("term") or {}
        tid = (term.get("id") if isinstance(term, dict) else "") or ""
        if ncbitaxon and tid == ncbitaxon:
            return i
        if (not ncbitaxon and preferred_term
                and (o.get("preferred_term") or "").strip().lower()
                == preferred_term.strip().lower()):
            return i
    return None


def make_evidence_item(pmid: str, snippet: str, query: str | None) -> dict:
    ev: dict = {
        "reference": f"PMID:{pmid}",
        "supports": "SUPPORT",
    }
    if snippet:
        ev["snippet"] = snippet
    if query:
        ev["explanation"] = f"Auto-applied from literature query: {query}"
    return ev


def _merge_strain_modifications(organism: dict, new_mods: list[dict]) -> int:
    """Merge new StrainModification entries onto the OrganismDescriptor.

    Dedup is by (modification_type, target_lower) — same gene knockout
    cited from two PMIDs is one logical modification, not two.
    Returns count of newly added entries.
    """
    if not new_mods:
        return 0
    existing = organism.setdefault("strain_modifications", [])
    seen: set[tuple[str, str]] = set()
    for em in existing:
        key = ((em.get("modification_type") or ""),
               (em.get("target") or "").strip().lower())
        seen.add(key)
    added = 0
    for m in new_mods:
        if not isinstance(m, dict):
            continue
        key = ((m.get("modification_type") or ""),
               (m.get("target") or "").strip().lower())
        if key in seen:
            continue
        seen.add(key)
        existing.append(dict(m))
        added += 1
    return added


def apply_candidate(recipe: dict, candidate: dict) -> dict:
    """Mutate recipe in place; return a count dict describing changes."""
    counts = {
        "organisms_added": 0,
        "metrics_added": 0,
        "genomes_added": 0,
        "strain_mods_added": 0,
    }
    extracted = candidate.get("extracted") or {}
    pmid = candidate.get("pmid") or ""
    snippet = candidate.get("snippet") or ""
    query = candidate.get("query")

    ncbitaxon = candidate.get("ncbitaxon")
    organism_label = (
        candidate.get("organism")
        or (extracted.get("organisms") or [None])[0]
    )
    if not organism_label and not ncbitaxon:
        return counts

    target_organisms = recipe.setdefault("target_organisms", [])
    idx = find_organism_idx(target_organisms, ncbitaxon, organism_label)

    if idx is None:
        new_org: dict = {"preferred_term": organism_label or "UNSPECIFIED"}
        if ncbitaxon:
            new_org["term"] = {"id": ncbitaxon, "label": organism_label or ""}
        target_organisms.append(new_org)
        idx = len(target_organisms) - 1
        counts["organisms_added"] += 1

    organism = target_organisms[idx]

    # v2 schema: strain_modifications live on the OrganismDescriptor
    # (carry across observations). Apply before growth-metrics so the
    # mods are in place when downstream tooling joins them up.
    counts["strain_mods_added"] = _merge_strain_modifications(
        organism, extracted.get("strain_modifications") or [],
    )

    metrics = extracted.get("growth_metrics") or {}
    if metrics:
        gm_entry: dict = dict(metrics)
        if pmid:
            gm_entry["evidence"] = [make_evidence_item(pmid, snippet, query)]
        # v2 schema: per-observation perturbation context fields.
        if "is_max_attainment" in extracted:
            gm_entry["is_max_attainment"] = extracted["is_max_attainment"]
        if extracted.get("growth_mode"):
            gm_entry["growth_mode"] = extracted["growth_mode"]
        if extracted.get("perturbations"):
            gm_entry["perturbations"] = list(extracted["perturbations"])
        if extracted.get("nutrient_overrides"):
            gm_entry["nutrient_overrides"] = list(extracted["nutrient_overrides"])
        # Dedup: skip when an existing growth_metrics entry already
        # cites the same PMID. Keeps `apply-growth --apply` idempotent
        # across re-runs of the same proposal.
        existing_metrics = organism.get("growth_metrics") or []
        already_present = False
        if pmid:
            ref_match = f"PMID:{pmid}"
            for existing in existing_metrics:
                for ev in (existing.get("evidence") or []):
                    if (ev.get("reference") or "").strip() == ref_match:
                        already_present = True
                        break
                if already_present:
                    break
        if not already_present:
            organism.setdefault("growth_metrics", []).append(gm_entry)
            counts["metrics_added"] += 1

    new_genomes = extracted.get("genome_assembly_ids") or []
    if new_genomes:
        existing = list(organism.get("genome_assembly_id") or [])
        for g in new_genomes:
            if g not in existing:
                existing.append(g)
                counts["genomes_added"] += 1
        if existing:
            organism["genome_assembly_id"] = existing

    return counts


def append_curation_history(recipe: dict, summary: dict) -> None:
    history = recipe.setdefault("curation_history", [])
    history.append({
        "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(),
        "curator": "literature_review_apply",
        "action": "ADDED_GROWTH_EVIDENCE",
        "notes": (
            f"organisms_added={summary['organisms_added']} "
            f"metrics_added={summary['metrics_added']} "
            f"genomes_added={summary['genomes_added']} "
            f"strain_mods_added={summary.get('strain_mods_added', 0)}"
        ),
    })


# ---------- driver ----------

def process_proposal(proposal_path: Path, apply: bool) -> dict:
    """Returns a per-recipe summary dict."""
    summary = {
        "proposal": proposal_path.name,
        "recipe_path": None,
        "applied": 0,
        "skipped_no_support": 0,
        "skipped_missing_recipe": 0,
        "organisms_added": 0,
        "metrics_added": 0,
        "genomes_added": 0,
        "strain_mods_added": 0,
        "wrote": False,
    }
    try:
        with open(proposal_path) as f:
            proposal = yaml.safe_load(f) or {}
    except Exception as e:
        print(f"  load error: {e}", file=sys.stderr)
        return summary

    candidates = proposal.get("candidates") or []
    proposal_recipe_path = proposal.get("recipe_path")
    recipe_path = (REPO_ROOT / proposal_recipe_path) if proposal_recipe_path else None
    if not recipe_path or not recipe_path.is_file():
        recipe_path = find_recipe(proposal_path.stem)

    if not recipe_path or not recipe_path.is_file():
        summary["skipped_missing_recipe"] = len(candidates)
        return summary
    summary["recipe_path"] = str(recipe_path.relative_to(REPO_ROOT))

    high_conf = [c for c in candidates if c.get("supports") == "SUPPORT"]
    summary["skipped_no_support"] = len(candidates) - len(high_conf)
    if not high_conf:
        return summary

    with open(recipe_path) as f:
        recipe = yaml.safe_load(f) or {}

    cum = {"organisms_added": 0, "metrics_added": 0, "genomes_added": 0,
           "strain_mods_added": 0}
    for c in high_conf:
        deltas = apply_candidate(recipe, c)
        for k in cum:
            cum[k] += deltas.get(k, 0)
        summary["applied"] += 1

    summary.update(cum)

    if any(cum.values()):
        append_curation_history(recipe, cum)

    if apply and any(cum.values()):
        with open(recipe_path, "w") as f:
            yaml.safe_dump(recipe, f, sort_keys=False, allow_unicode=True)
        summary["wrote"] = True

    return summary


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("--apply", action="store_true",
                    help="write changes to MediaRecipe YAMLs (default: dry-run)")
    ap.add_argument("--proposal-dir", type=Path, default=DEFAULT_PROPOSAL_DIR,
                    help="directory containing proposal YAMLs (default: workspace/reports/growth_evidence_proposals)")
    args = ap.parse_args()

    if not args.proposal_dir.is_dir():
        print(f"Proposal directory not found: {args.proposal_dir}")
        print("(Run scripts/propose_growth_evidence.py --apply first.)")
        return 1

    proposals = sorted(args.proposal_dir.glob("*.yaml"))
    if not proposals:
        print(f"No proposal YAMLs in {args.proposal_dir}")
        return 1
    print(f"Proposals to process: {len(proposals)}")
    print(f"Mode: {'APPLY (modifying recipe YAMLs)' if args.apply else 'DRY-RUN (no writes)'}")

    totals = {"applied": 0, "skipped_no_support": 0,
              "skipped_missing_recipe": 0, "organisms_added": 0,
              "metrics_added": 0, "genomes_added": 0,
              "strain_mods_added": 0, "wrote": 0}

    for p in proposals:
        s = process_proposal(p, apply=args.apply)
        print(
            f"  {p.name}: applied={s['applied']} "
            f"orgs+={s['organisms_added']} metrics+={s['metrics_added']} "
            f"genomes+={s['genomes_added']} "
            f"strain_mods+={s.get('strain_mods_added', 0)} "
            f"skipped_no_support={s['skipped_no_support']} "
            f"missing_recipe={s['skipped_missing_recipe']} "
            f"{'(wrote)' if s['wrote'] else ''}"
        )
        for k in ("applied", "skipped_no_support", "skipped_missing_recipe",
                  "organisms_added", "metrics_added", "genomes_added",
                  "strain_mods_added"):
            totals[k] += s.get(k, 0)
        if s["wrote"]:
            totals["wrote"] += 1

    print()
    print("Totals:")
    for k, v in totals.items():
        print(f"  {k}: {v}")
    if not args.apply:
        print("(dry-run — pass --apply to persist changes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
