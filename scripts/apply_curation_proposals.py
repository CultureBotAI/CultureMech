#!/usr/bin/env python3
"""Normalize deep-research curation proposals into schema-valid YAML edits.

Edison phase-2 follow-ups emit organism + media-variant proposals, but
with field/enum names that do NOT match the CultureMech schema
(``supports: growth_on_medium`` vs the ``SUPPORT`` enum,
``media_variants`` vs ``variants``, structured ``modifications`` dicts
vs flat strings, ``genome_accession: CP002453`` vs the
``genome_assembly_id`` GCA_/GCF_/SAMN pattern, strain folded into
``preferred_term``, etc.).

This script reads a *curation proposal JSON* — a clean intermediate
vocabulary that a curator (or Claude) authors from the phase-1/phase-2
results — and normalizes it into exact schema YAML, merging into the
target ``MediaRecipe`` records:

  - ``add_target_organisms`` -> appended to ``target_organisms``
    (deduped by preferred_term + strain).
  - ``add_variants``        -> appended to ``variants``
    (deduped by name).
  - a ``curation_history`` event recording the enrichment.

After writing (skipped under ``--dry-run``, the default), each
modified file is validated with ``linkml-validate --target-class
MediaRecipe``. Nothing is committed — the caller reviews ``git diff``.

Proposal JSON shape::

    {
      "curator": "deep-research-edison-phase2",
      "proposals": [
        {
          "target": "bacterial/archaeoglobus_medium_dsm_399.yaml",
          "curation_note": "Phase-2 Edison deep research ...",
          "add_target_organisms": [
            {
              "name": "Archaeoglobus fulgidus",
              "strain": "DSM 4304",
              "ncbitaxon": "NCBITaxon:2234",      # optional
              "genome_assembly_ids": ["GCA_000008665.1"],  # optional; pattern-checked
              "other_identifiers": "INSDC CP002453; IMG 2503904003",  # optional -> folded into evidence
              "evidence": [
                {"reference": "doi:10.7888/juoeh.29.131",
                 "supports": "SUPPORT",            # loose synonyms normalized
                 "snippet": "...",
                 "explanation": "..."}
              ]
            }
          ],
          "add_variants": [
            {
              "name": "stl_medium_archaeoglobus_variant",
              "relationship": "DERIVED_FROM",      # validated vs enum
              "description": "...",
              "modifications": ["...", "..."],     # flat strings
              "purpose": "...",
              "evidence": [ ... ]
            }
          ]
        }
      ]
    }

Usage::

    # default dry-run: print planned edits, validate nothing is written
    python scripts/apply_curation_proposals.py \\
        --proposals research/media/top5-curation-proposals.json

    # apply + validate
    python scripts/apply_curation_proposals.py \\
        --proposals research/media/top5-curation-proposals.json --apply
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


def _rt_load(path: Path) -> Any:
    return yaml.safe_load(path.read_text())


def _rt_dump(doc: Any, path: Path) -> None:
    """Write with PyYAML default width.

    The normalized_yaml records were last written by PyYAML at its
    default wrap width, so a default-width safe_dump round-trips
    untouched content byte-for-byte. `git diff` then shows only the
    appended organism / variant / curation-history blocks. Do NOT add
    a width= override here — width=120 reflows every wrapped scalar and
    buries the real change in cosmetic noise.
    """
    path.write_text(yaml.safe_dump(doc, default_flow_style=False,
                                   sort_keys=False, allow_unicode=True))

REPO_ROOT = Path(__file__).resolve().parent.parent
NORMALIZED_DIR = REPO_ROOT / "data" / "normalized_yaml"
SCHEMA_PATH = REPO_ROOT / "src" / "culturemech" / "schema" / "culturemech.yaml"

DEFAULT_CURATOR = "deep-research-edison-phase2"

# Loose -> canonical EvidenceItemSupportEnum. Anything not mapped and not
# already a valid enum value falls back to SUPPORT with a warning.
_SUPPORTS_SYNONYMS = {
    "support": "SUPPORT",
    "supports": "SUPPORT",
    "growth_on_medium": "SUPPORT",
    "growth_on_media": "SUPPORT",
    "growth_condition": "SUPPORT",
    "growth": "SUPPORT",
    "media_variant": "SUPPORT",
    "preparation_method": "SUPPORT",
    "partial": "PARTIAL",
    "refute": "REFUTE",
    "no_evidence": "NO_EVIDENCE",
    "wrong_statement": "WRONG_STATEMENT",
}

# Loaded from schema at runtime; populated by _load_enums().
_SUPPORTS_ENUM: set[str] = set()
_RELATIONSHIP_ENUM: set[str] = set()

# genome_assembly_id pattern from the schema.
import re  # noqa: E402
_ASSEMBLY_RE = re.compile(r"^(GCF_|GCA_|SAMN)[0-9.]+$")


def _load_enums() -> None:
    """Read the two enums we validate against straight from the schema."""
    global _SUPPORTS_ENUM, _RELATIONSHIP_ENUM
    with SCHEMA_PATH.open() as f:
        schema = yaml.safe_load(f)
    enums = schema.get("enums", {})
    _SUPPORTS_ENUM = set((enums.get("EvidenceItemSupportEnum", {})
                          .get("permissible_values", {}) or {}).keys())
    _RELATIONSHIP_ENUM = set((enums.get("MediaVariantRelationshipEnum", {})
                              .get("permissible_values", {}) or {}).keys())


def _norm_supports(raw: str, warnings: list[str]) -> str:
    """Map a loose ``supports`` value to a valid EvidenceItemSupportEnum."""
    if raw in _SUPPORTS_ENUM:
        return raw
    mapped = _SUPPORTS_SYNONYMS.get(str(raw).strip().lower())
    if mapped and mapped in _SUPPORTS_ENUM:
        return mapped
    warnings.append(f"unknown supports={raw!r} -> defaulting to SUPPORT")
    return "SUPPORT"


def _norm_relationship(raw: str | None, warnings: list[str]) -> str | None:
    """Validate a variant relationship against MediaVariantRelationshipEnum."""
    if raw is None:
        return None
    if raw in _RELATIONSHIP_ENUM:
        return raw
    warnings.append(f"unknown relationship={raw!r} -> defaulting to DERIVED_FROM")
    return "DERIVED_FROM"


def _build_evidence(raw_list: list[dict[str, Any]], warnings: list[str]) -> list[dict[str, Any]]:
    """Normalize a list of loose evidence dicts to schema EvidenceItem dicts."""
    out: list[dict[str, Any]] = []
    for ev in raw_list or []:
        ref = ev.get("reference")
        if not ref:
            warnings.append("evidence item missing reference -> skipped")
            continue
        item: dict[str, Any] = {
            "reference": ref,
            "supports": _norm_supports(ev.get("supports", "SUPPORT"), warnings),
            "explanation": ev.get("explanation", ""),
        }
        # snippet is optional in the schema but strongly preferred
        if ev.get("snippet"):
            item["snippet"] = ev["snippet"]
        if not item["explanation"]:
            warnings.append(f"evidence {ref} missing explanation (required) -> empty string")
        out.append(item)
    return out


def _build_organism(raw: dict[str, Any], warnings: list[str]) -> dict[str, Any]:
    """Normalize a loose organism dict to a schema OrganismDescriptor."""
    name = raw.get("name") or raw.get("preferred_term")
    if not name:
        raise ValueError(f"organism proposal missing 'name': {raw}")
    org: dict[str, Any] = {"preferred_term": name}

    ncbitaxon = raw.get("ncbitaxon")
    if ncbitaxon:
        if not str(ncbitaxon).startswith("NCBITaxon:"):
            warnings.append(f"{name}: ncbitaxon {ncbitaxon!r} lacks NCBITaxon: prefix -> dropped")
        else:
            org["term"] = {"id": ncbitaxon, "label": raw.get("term_label", name)}

    if raw.get("strain"):
        org["strain"] = raw["strain"]

    # genome_assembly_id: keep only pattern-valid accessions; fold the rest
    # into an evidence note so we never emit a schema-invalid value.
    valid_assemblies: list[str] = []
    dropped_ids: list[str] = []
    for acc in raw.get("genome_assembly_ids", []) or []:
        if _ASSEMBLY_RE.match(str(acc)):
            valid_assemblies.append(str(acc))
        else:
            dropped_ids.append(str(acc))
    if valid_assemblies:
        org["genome_assembly_id"] = valid_assemblies

    evidence = _build_evidence(raw.get("evidence", []), warnings)

    # Fold non-assembly identifiers + dropped accessions into the first
    # evidence explanation so provenance survives without breaking the
    # genome_assembly_id pattern.
    extra_bits = []
    if raw.get("other_identifiers"):
        extra_bits.append(str(raw["other_identifiers"]))
    if dropped_ids:
        extra_bits.append("non-assembly accessions: " + ", ".join(dropped_ids))
    if extra_bits and evidence:
        note = " | Identifiers: " + "; ".join(extra_bits)
        evidence[0]["explanation"] = (evidence[0].get("explanation", "") + note).strip()
    elif extra_bits:
        warnings.append(f"{name}: identifiers {extra_bits} have no evidence item to attach to")

    if evidence:
        org["evidence"] = evidence
    return org


def _build_variant(raw: dict[str, Any], warnings: list[str]) -> dict[str, Any]:
    """Normalize a loose variant dict to a schema MediaVariant."""
    name = raw.get("name")
    if not name:
        raise ValueError(f"variant proposal missing 'name': {raw}")
    var: dict[str, Any] = {"name": name}
    rel = _norm_relationship(raw.get("relationship"), warnings)
    if rel:
        var["relationship"] = rel
    if raw.get("description"):
        var["description"] = raw["description"]
    mods = raw.get("modifications")
    if mods:
        # Schema: modifications is multivalued range:string. Coerce any
        # structured dicts the caller left in into readable strings.
        flat: list[str] = []
        for m in mods:
            if isinstance(m, str):
                flat.append(m)
            elif isinstance(m, dict):
                flat.append("; ".join(f"{k}={v}" for k, v in m.items()))
            else:
                flat.append(str(m))
        var["modifications"] = flat
    if raw.get("purpose"):
        var["purpose"] = raw["purpose"]
    evidence = _build_evidence(raw.get("evidence", []), warnings)
    if evidence:
        var["evidence"] = evidence
    return var


def _resolve_target(target: str) -> Path:
    """Resolve a proposal target to a YAML path under normalized_yaml/."""
    p = NORMALIZED_DIR / target
    if p.is_file():
        return p.resolve()
    # fall back to the shared resolver (slug/id/name)
    sys.path.insert(0, str(REPO_ROOT / "scripts"))
    import research_media as rm  # noqa: E402
    return rm.resolve_media_file(target)


def _dedup_key_org(o: dict[str, Any]) -> tuple[str, str]:
    return (str(o.get("preferred_term", "")).strip().lower(),
            str(o.get("strain", "")).strip().lower())


def apply_proposal(proposal: dict[str, Any], curator: str, *,
                   apply: bool) -> dict[str, Any]:
    """Merge one proposal into its target record. Returns a stats dict."""
    warnings: list[str] = []
    target_path = _resolve_target(proposal["target"])
    doc = _rt_load(target_path)
    if not isinstance(doc, dict):
        raise ValueError(f"target is not a mapping: {target_path}")

    # --- organisms ---
    new_orgs = [_build_organism(o, warnings)
                for o in proposal.get("add_target_organisms", [])]
    existing_orgs = doc.get("target_organisms") or []
    existing_keys = {_dedup_key_org(o) for o in existing_orgs if isinstance(o, dict)}
    added_orgs: list[str] = []
    for o in new_orgs:
        k = _dedup_key_org(o)
        if k in existing_keys:
            warnings.append(f"organism already present, skipped: {o['preferred_term']} "
                            f"({o.get('strain', '-')})")
            continue
        existing_orgs.append(o)
        existing_keys.add(k)
        added_orgs.append(f"{o['preferred_term']} ({o.get('strain', '-')})")
    if added_orgs:
        doc["target_organisms"] = existing_orgs

    # --- variants ---
    new_vars = [_build_variant(v, warnings)
                for v in proposal.get("add_variants", [])]
    existing_vars = doc.get("variants") or []
    existing_var_names = {str(v.get("name", "")).strip().lower()
                          for v in existing_vars if isinstance(v, dict)}
    added_vars: list[str] = []
    for v in new_vars:
        if v["name"].strip().lower() in existing_var_names:
            warnings.append(f"variant already present, skipped: {v['name']}")
            continue
        existing_vars.append(v)
        existing_var_names.add(v["name"].strip().lower())
        added_vars.append(v["name"])
    if added_vars:
        doc["variants"] = existing_vars

    # --- curation history ---
    changed = bool(added_orgs or added_vars)
    if changed:
        history = doc.get("curation_history") or []
        fields = []
        if added_orgs:
            fields.append("target_organisms")
        if added_vars:
            fields.append("variants")
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "curator": curator,
            "action": "ENRICHED",
            "notes": (proposal.get("curation_note")
                      or "Enriched from Edison deep-research phase-2 follow-up")
            + f" [added {len(added_orgs)} organism(s), {len(added_vars)} variant(s)]",
        }
        history.append(event)
        doc["curation_history"] = history

    if changed and apply:
        _rt_dump(doc, target_path)

    return {
        "target": str(target_path.relative_to(REPO_ROOT)),
        "added_organisms": added_orgs,
        "added_variants": added_vars,
        "warnings": warnings,
        "changed": changed,
    }


def validate_file(target_path: Path) -> tuple[bool, str]:
    """Run linkml-validate --target-class MediaRecipe on one file."""
    cmd = ["uv", "run", "linkml-validate", "--schema", str(SCHEMA_PATH),
           "--target-class", "MediaRecipe", str(target_path)]
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO_ROOT))
    ok = proc.returncode == 0
    return ok, (proc.stdout + proc.stderr).strip()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--proposals", type=Path, required=True,
                    help="Curation proposal JSON.")
    ap.add_argument("--apply", action="store_true",
                    help="Write changes to disk (default: dry-run, no writes).")
    ap.add_argument("--no-validate", action="store_true",
                    help="Skip linkml-validate after applying.")
    args = ap.parse_args(argv)

    _load_enums()
    import json
    data = json.loads(args.proposals.read_text())
    curator = data.get("curator", DEFAULT_CURATOR)
    proposals = data.get("proposals", [])
    if not proposals:
        print("No proposals found.", file=sys.stderr)
        return 2

    mode = "APPLY" if args.apply else "DRY RUN"
    print(f"Mode: {mode}   Proposals: {len(proposals)}   Curator: {curator}")
    print()

    results = []
    for p in proposals:
        r = apply_proposal(p, curator, apply=args.apply)
        results.append(r)
        print(f"== {r['target']} ==")
        for o in r["added_organisms"]:
            print(f"   + organism: {o}")
        for v in r["added_variants"]:
            print(f"   + variant:  {v}")
        if not r["changed"]:
            print("   (no changes)")
        for w in r["warnings"]:
            print(f"   ! {w}")
        print()

    # Validation pass (only meaningful after --apply, since dry-run didn't write)
    if args.apply and not args.no_validate:
        print("Validating modified records against MediaRecipe...")
        all_ok = True
        for r in results:
            if not r["changed"]:
                continue
            ok, out = validate_file(REPO_ROOT / r["target"])
            status = "OK" if ok else "FAIL"
            print(f"  [{status}] {r['target']}")
            if not ok:
                all_ok = False
                print("   " + out.replace("\n", "\n   "))
        print()
        print("All valid." if all_ok else "VALIDATION FAILURES — review above.")
        if not all_ok:
            return 1

    total_orgs = sum(len(r["added_organisms"]) for r in results)
    total_vars = sum(len(r["added_variants"]) for r in results)
    print(f"Summary: +{total_orgs} organisms, +{total_vars} variants across "
          f"{sum(1 for r in results if r['changed'])} records.")
    if not args.apply:
        print("Dry-run only — re-run with --apply to write changes, then review `git diff`.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
