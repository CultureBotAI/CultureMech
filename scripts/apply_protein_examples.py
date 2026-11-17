#!/usr/bin/env python3
"""Apply curated UniProtKB ProteinExample entries to CultureMech normalized recipes.

Operates exclusively on authoritative normalized recipe records under
`data/normalized_yaml/`. Defaults to `--dry-run` mode unless `--apply` is
explicitly passed, validates each modified recipe with closed-schema LinkML +
`ProteinExample` semantic checks before writing (`write_validated_recipe`), and
appends a `curation_history` event for every modified record.

Input batch YAML format:

  proposals:
    - recipe_id: CultureMech:001234
      target_scope: recipe            # recipe | organism | cofactor_requirement | transporter
      organism_taxon_id: NCBITaxon:83333
      target_name: ompF               # used when target_scope is cofactor_requirement or transporter
      source_note: PMID:12345678 curation
      protein_example:
        uniprot_term:
          id: UniProtKB:P02931
          label: Outer membrane porin F
        organism_term:
          id: NCBITaxon:83333
          label: Escherichia coli K-12
        gene_symbol: ompF
        locus_tag: b0929
        functional_role: Outer membrane diffusion porin for hydrophilic solutes
        evidence:
          - reference: PMID:12345678
            supports: SUPPORT
            snippet: "OmpF forms general diffusion pores in Escherichia coli K-12."
            explanation: Supports OmpF porin function in E. coli K-12.

Usage:
    just apply-protein-examples batch.yaml --dry-run
    just apply-protein-examples batch.yaml --apply
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

from culturemech.validation.protein_examples import validate_protein_example_entry  # noqa: E402
from culturemech.validation.write_validated import (  # noqa: E402
    LayerBoundaryError,
    ValidationFailedError,
    validate_recipe,
    write_validated_recipe,
)

DEFAULT_YAML_DIR = REPO_ROOT / "data" / "normalized_yaml"
DEFAULT_CURATOR = "apply_protein_examples.py"


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


def _dedup_append(target_list: list[dict[str, Any]], pe: dict[str, Any]) -> bool:
    """Append `pe` to `target_list` if `(uniprot_term.id, organism_term.id)` is not present."""
    ut = pe.get("uniprot_term") or {}
    ot = pe.get("organism_term") or {}
    new_pair = (ut.get("id"), ot.get("id"))
    for existing in target_list:
        if not isinstance(existing, dict):
            continue
        e_ut = existing.get("uniprot_term") or {}
        e_ot = existing.get("organism_term") or {}
        if (e_ut.get("id"), e_ot.get("id")) == new_pair:
            return False
    target_list.append(copy.deepcopy(pe))
    return True


def _apply_proposal_to_recipe(recipe: dict[str, Any], proposal: dict[str, Any]) -> str | None:
    """Apply one proposal to `recipe` in-place. Returns change summary or None if no-op."""
    pe = proposal.get("protein_example")
    if not isinstance(pe, dict):
        raise ValueError("Proposal missing 'protein_example' mapping.")

    scope = proposal.get("target_scope", "recipe")
    org_taxon = proposal.get("organism_taxon_id")
    target_name = proposal.get("target_name")

    enclosing_org = org_taxon if scope != "recipe" else None
    issues = validate_protein_example_entry(
        pe, "proposal.protein_example", enclosing_organism_id=enclosing_org
    )
    if issues:
        joined = "; ".join(i.message for i in issues)
        raise ValueError(f"Invalid ProteinExample in proposal: {joined}")

    uid = pe["uniprot_term"]["id"]
    oid = pe["organism_term"]["id"]

    if scope == "recipe":
        bucket = recipe.setdefault("protein_examples", [])
        if _dedup_append(bucket, pe):
            return f"Added recipe protein_examples entry {uid} ({oid})"
        return None

    organisms = recipe.get("target_organisms") or []
    for org in organisms:
        if not isinstance(org, dict):
            continue
        term = org.get("term") or {}
        if org_taxon and term.get("id") != org_taxon:
            continue

        if scope == "organism":
            bucket = org.setdefault("protein_examples", [])
            if _dedup_append(bucket, pe):
                return f"Added target_organisms ({org_taxon}) protein_examples entry {uid}"
            return None

        if scope == "cofactor_requirement":
            for cr in org.get("cofactor_requirements") or []:
                if not isinstance(cr, dict):
                    continue
                cof = cr.get("cofactor") or {}
                cof_name = cof.get("preferred_term") or (cof.get("term") or {}).get("id")
                if target_name and cof_name != target_name:
                    continue
                bucket = cr.setdefault("protein_examples", [])
                if _dedup_append(bucket, pe):
                    return (
                        f"Added cofactor_requirements ({cof_name}) protein_examples entry "
                        f"{uid} ({oid})"
                    )
                return None

        if scope == "transporter":
            for tr in org.get("transporters") or []:
                if not isinstance(tr, dict):
                    continue
                if target_name and tr.get("name") != target_name:
                    continue
                bucket = tr.setdefault("protein_examples", [])
                if _dedup_append(bucket, pe):
                    return (
                        f"Added transporters ({tr.get('name')}) protein_examples entry "
                        f"{uid} ({oid})"
                    )
                return None

    raise ValueError(
        f"Could not resolve target_scope={scope!r} (organism_taxon_id={org_taxon!r}, "
        f"target_name={target_name!r}) in recipe {recipe.get('id')!r}"
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
            else "Applied curated UniProtKB protein_examples"
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
