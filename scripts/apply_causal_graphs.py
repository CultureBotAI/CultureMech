#!/usr/bin/env python3
"""Apply curated CausalEdge entries to CultureMech normalized recipes.

Operates exclusively on authoritative normalized recipe records under
`data/normalized_yaml/`. Defaults to `--dry-run` mode unless `--apply` is
explicitly passed, validates each modified recipe with closed-schema LinkML +
`CausalEdge` semantic checks before writing (`write_validated_recipe`), and
appends a `curation_history` event for every modified record.

Input batch YAML format:

  proposals:
    - recipe_id: CultureMech:001234
      target_scope: recipe            # recipe | organism
      organism_taxon_id: NCBITaxon:83333
      source_note: PMID:12345678 causal mechanism curation
      causal_edge:
        id: edge_glucose_enables_growth
        subject_term:
          id: CHEBI:17234
          label: D-glucose
        predicate: ENABLES_GROWTH
        object_term:
          id: NCBITaxon:83333
          label: Escherichia coli K-12
        organism_term:
          id: NCBITaxon:83333
          label: Escherichia coli K-12
        protein_terms:
          - id: UniProtKB:P69786
            label: PTS system glucose-specific EIICB component
        condition_context: Aerobic minimal medium M9 at 37 C
        evidence:
          - reference: PMID:12345678
            supports: SUPPORT
            snippet: "D-glucose serves as the sole carbon and energy source supporting aerobic growth of E. coli K-12 in M9 minimal medium."
            explanation: Demonstrates causal growth support by D-glucose in M9 minimal medium.

Usage:
    just apply-causal-graphs batch.yaml --dry-run
    just apply-causal-graphs batch.yaml --apply
"""

from __future__ import annotations

import argparse
import copy
import datetime
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from culturemech.validation.causal_graphs import validate_causal_edge_entry  # noqa: E402
from culturemech.validation.write_validated import (  # noqa: E402
    LayerBoundaryError,
    ValidationFailedError,
    validate_recipe,
    write_validated_recipe,
)

DEFAULT_YAML_DIR = REPO_ROOT / "data" / "normalized_yaml"
DEFAULT_CURATOR = "apply_causal_graphs.py"


def _load_proposals(batch_path: Path) -> list[dict[str, Any]]:
    data = yaml.safe_load(batch_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("proposals"), list):
        raise ValueError(f"Batch file {batch_path} must be a YAML mapping with a 'proposals' list.")
    return data["proposals"]


def _assert_normalized_yaml_scope(yaml_dir: Path) -> None:
    resolved = yaml_dir.resolve()
    parts = resolved.parts
    if "merge_yaml" in parts or "normalized_yaml" not in parts:
        raise LayerBoundaryError(
            f"Refusing to write to {yaml_dir}; "
            "authoritative edits must target data/normalized_yaml/."
        )


def _edge_signature(
    ce: dict[str, Any], enclosing_org: str | None = None
) -> tuple[str | None, str | None, str | None, str | None]:
    st = ce.get("subject_term") or {}
    ot = ce.get("object_term") or {}
    org = ce.get("organism_term") or {}
    return (
        st.get("id") if isinstance(st, dict) else None,
        ce.get("predicate"),
        ot.get("id") if isinstance(ot, dict) else None,
        (org.get("id") if isinstance(org, dict) else None) or enclosing_org,
    )


def _dedup_append(
    target_list: list[dict[str, Any]],
    ce: dict[str, Any],
    enclosing_org: str | None = None,
) -> bool:
    """Append `ce` to `target_list` if neither `id` nor `(subject, predicate, object, organism)` is present."""
    new_id = ce.get("id")
    new_sig = _edge_signature(ce, enclosing_org=enclosing_org)
    for existing in target_list:
        if not isinstance(existing, dict):
            continue
        if (
            existing.get("id") == new_id
            or _edge_signature(existing, enclosing_org=enclosing_org) == new_sig
        ):
            return False
    target_list.append(copy.deepcopy(ce))
    return True


def _apply_proposal_to_recipe(recipe: dict[str, Any], proposal: dict[str, Any]) -> str | None:
    """Apply one proposal to `recipe` in-place. Returns change summary or None if no-op."""
    ce = proposal.get("causal_edge")
    if not isinstance(ce, dict):
        raise ValueError("Proposal missing 'causal_edge' mapping.")

    scope = proposal.get("target_scope", "recipe")
    org_taxon = proposal.get("organism_taxon_id")

    if scope not in ("recipe", "organism"):
        raise ValueError(f"Unsupported target_scope={scope!r}; expected 'recipe' or 'organism'.")

    if scope == "organism" and not org_taxon:
        org_term = ce.get("organism_term")
        if isinstance(org_term, dict):
            org_taxon = org_term.get("id")
        if not org_taxon:
            raise ValueError(
                "Organism-scoped proposal requires 'organism_taxon_id' or 'causal_edge.organism_term.id'."
            )

    enclosing_org = org_taxon if scope == "organism" else None
    issues = validate_causal_edge_entry(
        ce, "proposal.causal_edge", enclosing_organism_id=enclosing_org
    )
    if issues:
        joined = "; ".join(i.message for i in issues)
        raise ValueError(f"Invalid CausalEdge in proposal: {joined}")

    edge_id = ce["id"]
    subj_id = ce["subject_term"]["id"]
    pred = ce["predicate"]
    obj_id = ce["object_term"]["id"]

    if scope == "recipe":
        bucket = recipe.setdefault("causal_graphs", [])
        if _dedup_append(bucket, ce):
            return f"Added recipe causal_graphs entry {edge_id} ({subj_id} {pred} {obj_id})"
        return None

    organisms = recipe.get("target_organisms") or []
    for org in organisms:
        if not isinstance(org, dict):
            continue
        term = org.get("term") or {}
        if term.get("id") != org_taxon:
            continue

        bucket = org.setdefault("causal_graphs", [])
        if _dedup_append(bucket, ce, enclosing_org=org_taxon):
            return (
                f"Added target_organisms ({term.get('id')}) causal_graphs entry "
                f"{edge_id} ({subj_id} {pred} {obj_id})"
            )
        return None

    raise ValueError(
        f"Could not resolve target_scope={scope!r} (organism_taxon_id={org_taxon!r}) "
        f"in recipe {recipe.get('id')!r}"
    )


def append_curation_history(
    recipe: dict[str, Any],
    curator: str,
    changes: list[str],
    notes: str,
) -> None:
    """Append a schema-compliant CurationEvent to `recipe['curation_history']`."""
    curation_history = recipe.setdefault("curation_history", [])
    curation_history.append(
        {
            "timestamp": datetime.datetime.now(datetime.timezone.utc)
            .isoformat()
            .replace("+00:00", "Z"),
            "curator": curator,
            "action": "ANNOTATED",
            "changes": "; ".join(changes),
            "notes": notes,
        }
    )


def apply_proposals_to_directory(
    proposals: list[dict[str, Any]],
    yaml_dir: Path,
    *,
    curator: str = DEFAULT_CURATOR,
    dry_run: bool = True,
) -> tuple[int, int]:
    """Apply `proposals` across `yaml_dir`. Returns `(recipes_touched, recipes_written)`."""
    _assert_normalized_yaml_scope(yaml_dir)

    by_recipe_id: dict[str, list[dict[str, Any]]] = {}
    for prop in proposals:
        rid = prop.get("recipe_id")
        if not isinstance(rid, str) or not rid.strip():
            raise ValueError("Each proposal must specify a non-empty 'recipe_id'.")
        by_recipe_id.setdefault(rid.strip(), []).append(prop)

    recipes_touched = 0
    recipes_written = 0

    for yaml_path in sorted(yaml_dir.rglob("*.yaml")):
        if yaml_path.name.endswith("_index.yaml"):
            continue
        recipe = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
        if not isinstance(recipe, dict):
            continue
        rid = recipe.get("id")
        if rid not in by_recipe_id:
            continue

        changes: list[str] = []
        notes_parts: list[str] = []
        for prop in by_recipe_id[rid]:
            summary = _apply_proposal_to_recipe(recipe, prop)
            if summary:
                changes.append(summary)
                if prop.get("source_note"):
                    notes_parts.append(str(prop["source_note"]))

        if not changes:
            continue

        recipes_touched += 1
        note_str = (
            "; ".join(sorted(set(notes_parts)))
            if notes_parts
            else "Applied curated growth-media causal_graphs"
        )
        append_curation_history(recipe, curator, changes, note_str)

        errors = validate_recipe(recipe)
        if errors:
            raise ValidationFailedError(yaml_path, errors)

        if not dry_run:
            write_validated_recipe(recipe, yaml_path)
            recipes_written += 1

    return recipes_touched, recipes_written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("batch", nargs="?", type=Path, help="YAML batch file containing proposals.")
    parser.add_argument(
        "--input",
        dest="input_batch",
        type=Path,
        help="YAML batch file containing proposals (alias for positional batch).",
    )
    parser.add_argument(
        "--yaml-dir",
        "--normalized-dir",
        dest="yaml_dir",
        type=Path,
        default=DEFAULT_YAML_DIR,
        help="Root directory of normalized YAML recipes (default: data/normalized_yaml).",
    )
    parser.add_argument(
        "--curator",
        default=DEFAULT_CURATOR,
        help="Curator name recorded in curation_history.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="Validate and preview changes without writing files (default).",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write validated changes and curation_history events to disk.",
    )
    args = parser.parse_args(argv)
    batch_path = args.input_batch or args.batch
    if batch_path is None:
        parser.error("either positional 'batch' or '--input' must be provided")

    dry_run = not args.apply
    proposals = _load_proposals(batch_path)
    touched, written = apply_proposals_to_directory(
        proposals,
        args.yaml_dir,
        curator=args.curator,
        dry_run=dry_run,
    )
    mode = "DRY-RUN" if dry_run else "APPLIED"
    print(f"[{mode}] Recipes touched: {touched}; recipes written: {written}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
