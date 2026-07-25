#!/usr/bin/env python3
"""Apply Step 7b Edison-derived ingredient role tokens across CultureMech recipes.

Consumes the scalar-projection batch JSON produced by
`extract_roles_from_edison.py --out-cm`:

  {"proposals": [
    {"ingredient_identifier": "CHEBI:17561",
     "ingredient_slug": "L-cysteine",
     "source_run": "L-cysteine-edison-literature",
     "roles": {
       "nutritional_roles": ["AMINO_ACID_SOURCE", "SULFUR_SOURCE"],
       "physicochemical_roles": ["REDUCING_AGENT"],
       "cellular_metabolic_roles": ["SUBSTRATE"]}},
    ...]}

Walks every recipe under `data/normalized_yaml/**/*.yaml`, and for every
ingredient descriptor whose CHEBI identity matches a batch proposal, fills
in the three facet slots on the descriptor. Never overwrites — a slot
already populated on the descriptor is left alone (curator wins).

Complements MIM's `apply_role_research_results.py` (rich shape, evidence
carried through). Evidence and citations are the source-of-truth on the
MIM record; CultureMech carries only the scalar tokens per descriptor.

The two appliers should be run against the SAME extractor output (which
is why `extract_roles_from_edison.py` emits both `--out-mim` and `--out-cm`
in a single pass).

Usage:

    just apply-ingredient-roles data/import_tracking/reports/edison_role_batch_cm.json --dry-run
    just apply-ingredient-roles data/import_tracking/reports/edison_role_batch_cm.json

    # Direct CLI:
    uv run python scripts/apply_ingredient_roles.py \\
      data/import_tracking/reports/edison_role_batch_cm.json \\
      --yaml-dir data/normalized_yaml/ \\
      --curator edison-deep-research

Curation history: one event per changed recipe, with `curator=<--curator>`,
`action=ANNOTATED`, `changes=` listing facet slot names, and a `notes`
field naming the source Edison run and the ingredient identifiers touched.

Role tokens are NOT re-validated against the facet enums here — that check
lives in `extract_roles_from_edison.py`. A batch produced with its
`--no-validate` flag, or hand-edited afterwards, can carry invalid tokens
into the corpus, where they surface only at `just validate-strict`.
"""

from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_YAML_DIR = REPO_ROOT / "data" / "normalized_yaml"

FACET_SLOTS = ("nutritional_roles", "physicochemical_roles", "cellular_metabolic_roles")

DEFAULT_CURATOR = "edison-deep-research"


def _load_batch(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text())
    if not isinstance(data, dict) or "proposals" not in data:
        raise SystemExit(
            f"Batch file {path} must be a JSON object with a top-level 'proposals' list."
        )
    proposals = data["proposals"]
    if not isinstance(proposals, list):
        raise SystemExit(f"'proposals' in {path} must be a list, got {type(proposals).__name__}.")
    return proposals


def _index_by_identifier(
    proposals: list[dict[str, Any]],
    skipped: list[dict[str, Any]] | None = None,
) -> dict[str, dict[str, Any]]:
    """Index proposals by ingredient_identifier for O(1) lookup during the walk.

    A proposal with no `ingredient_identifier` cannot be matched to a descriptor
    and is dropped; dropped proposals are appended to `skipped` so the caller can
    report them rather than losing them silently.
    """
    idx: dict[str, dict[str, Any]] = {}
    for p in proposals:
        ident = p.get("ingredient_identifier")
        if not ident:
            if skipped is not None:
                skipped.append(p)
            continue
        if ident in idx:
            # Merge: first proposal wins per facet; later ones only fill facets
            # the earlier proposal left empty.
            existing = idx[ident].get("roles") or {}
            new = p.get("roles") or {}
            merged = dict(existing)
            for slot, tokens in new.items():
                merged.setdefault(slot, tokens)
            p = dict(p, roles=merged)
        idx[ident] = p
    return idx


def _descriptor_identifier(ing: dict[str, Any]) -> str | None:
    """Best-effort ontology id for an ingredient descriptor in a normalized recipe.

    Prefers `mediaingredientmech_chebi_term.id` (MIM-mapped anchor); falls back to
    `term.id`, then `ingredient_term.id`. The id is returned as-is whatever its
    namespace — no CHEBI filter — since matching is by equality against the batch's
    `ingredient_identifier`, which is itself CHEBI in practice. Returns None only
    when no descriptor term carries an id at all.
    """
    for key in ("mediaingredientmech_chebi_term", "term", "ingredient_term"):
        term = ing.get(key)
        if isinstance(term, dict):
            tid = term.get("id")
            if isinstance(tid, str) and tid:
                return tid
    return None


def _apply_to_descriptor(
    ing: dict[str, Any],
    proposal: dict[str, Any],
) -> list[str]:
    """Set empty facet slots on one descriptor. Returns list of slots changed."""
    roles = proposal.get("roles") or {}
    changed: list[str] = []
    for slot in FACET_SLOTS:
        tokens = roles.get(slot) or []
        if not tokens:
            continue
        if ing.get(slot):  # never-overwrite guard
            continue
        # Dedup tokens preserving order; enum validation is the schema/apply-linter's job.
        seen: set[str] = set()
        clean: list[str] = []
        for t in tokens:
            if isinstance(t, str) and t and t not in seen:
                seen.add(t)
                clean.append(t)
        if clean:
            ing[slot] = clean
            changed.append(slot)
    return changed


def _add_curation_event(
    recipe: dict[str, Any],
    curator_name: str,
    fields_changed: list[str],
    notes: str,
) -> None:
    """Append a curation_history event to the recipe.

    `CurationEvent` has no `fields_changed` slot — the slot is `changes`, and its
    range is a plain string, so the facet list is rendered comma-joined. The class
    is validated closed (`validate-strict` runs linkml-validate with closed=True),
    so any extra key here fails CI on every recipe this script writes.
    """
    history = recipe.setdefault("curation_history", [])
    history.append({
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
        "curator": curator_name,
        "action": "ANNOTATED",
        "changes": ", ".join(fields_changed),
        "notes": notes,
    })


def _walk_descriptors(recipe: dict[str, Any]):
    """Yield every ingredient-descriptor dict inside a recipe (top-level + solutions)."""
    for ing in recipe.get("ingredients") or []:
        if isinstance(ing, dict):
            yield ing
    for sol in recipe.get("solutions") or []:
        if not isinstance(sol, dict):
            continue
        for ing in sol.get("ingredients") or []:
            if isinstance(ing, dict):
                yield ing


def apply_to_recipe(
    recipe: dict[str, Any],
    proposals_by_id: dict[str, dict[str, Any]],
    curator_name: str,
) -> tuple[list[str], list[str]]:
    """Apply proposals to one recipe. Returns (fields_changed, touched_identifiers)."""
    fields_changed: set[str] = set()
    touched: list[str] = []
    for ing in _walk_descriptors(recipe):
        ident = _descriptor_identifier(ing)
        if not ident or ident not in proposals_by_id:
            continue
        proposal = proposals_by_id[ident]
        changed = _apply_to_descriptor(ing, proposal)
        if changed:
            fields_changed.update(changed)
            touched.append(ident)
    if fields_changed:
        source_runs = sorted(
            {proposals_by_id[i].get("source_run") for i in touched
             if proposals_by_id[i].get("source_run")}
        )
        notes = f"Populated {sorted(fields_changed)} for {sorted(set(touched))}; source_run={source_runs}"
        _add_curation_event(recipe, curator_name, sorted(fields_changed), notes)
    return sorted(fields_changed), touched


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("batch", type=Path,
                        help="JSON batch from extract_roles_from_edison.py --out-cm.")
    parser.add_argument("--yaml-dir", type=Path, default=DEFAULT_YAML_DIR,
                        help="Root of the normalized recipe YAMLs.")
    parser.add_argument("--curator", default=DEFAULT_CURATOR,
                        help="Curator identity written to curation_history events.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Report changes without writing files.")
    parser.add_argument("--limit", type=int, default=None,
                        help="Cap the number of recipes actually written (dry-run counts them all).")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args(argv)

    if not args.batch.is_file():
        print(f"Batch file not found: {args.batch}", file=sys.stderr)
        return 2
    if not args.yaml_dir.is_dir():
        print(f"YAML dir not found: {args.yaml_dir}", file=sys.stderr)
        return 2

    proposals = _load_batch(args.batch)
    unidentified: list[dict[str, Any]] = []
    proposals_by_id = _index_by_identifier(proposals, skipped=unidentified)
    if unidentified:
        print(f"WARNING: {len(unidentified)} proposal(s) have no `ingredient_identifier` "
              f"and cannot be matched to a descriptor — they will NOT be applied:")
        for p in unidentified:
            print(f"  - slug={p.get('ingredient_slug') or '(none)'} "
                  f"source_run={p.get('source_run') or '(none)'}")
    if not proposals_by_id:
        print("No proposals with an ingredient_identifier; nothing to apply.")
        return 0

    print(f"Loaded {len(proposals)} proposals ({len(proposals_by_id)} unique identifiers) from {args.batch}")
    print(f"Walking recipes under {args.yaml_dir}")

    recipes_touched = 0
    recipes_written = 0
    identifiers_touched: set[str] = set()

    for yaml_path in sorted(args.yaml_dir.rglob("*.yaml")):
        try:
            recipe = yaml.safe_load(yaml_path.read_text())
        except Exception as exc:
            if args.verbose:
                print(f"skip {yaml_path.relative_to(args.yaml_dir)}: parse error: {exc}")
            continue
        if not isinstance(recipe, dict):
            continue

        fields_changed, touched = apply_to_recipe(recipe, proposals_by_id, args.curator)
        if not fields_changed:
            continue

        recipes_touched += 1
        identifiers_touched.update(touched)

        if args.dry_run:
            if args.verbose:
                print(f"[DRY] {yaml_path.relative_to(args.yaml_dir)}: {fields_changed} ({len(touched)} ingredients)")
            continue

        if args.limit is not None and recipes_written >= args.limit:
            continue

        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(recipe, f, default_flow_style=False, sort_keys=False,
                      allow_unicode=True, width=120)
        recipes_written += 1
        if args.verbose:
            print(f"WROTE {yaml_path.relative_to(args.yaml_dir)}: {fields_changed}")

    print()
    print(f"Recipes touched: {recipes_touched}")
    print(f"Recipes written: {recipes_written}{' (DRY RUN)' if args.dry_run else ''}")
    print(f"Distinct ingredient identifiers applied: {len(identifiers_touched)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
