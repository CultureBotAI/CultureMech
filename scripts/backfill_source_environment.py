#!/usr/bin/env python3
"""Backfill `source_environment` on CultureMech recipes from CommunityMech.

Closes issue #2: every CommunityMech community/isolate YAML that carries
both an `environment_term` (ENVO-grounded) AND a `culturemech_id`
reference is a curator-vetted assertion that the linked CultureMech
recipe targets that environment. Walk those, dedupe by ENVO id per
recipe, and append `SourceEnvironmentDescriptor` entries to the recipe's
`source_environment` list (the schema slot landed in commit dbe26e8ce
but no records populated it).

CommunityMech is assumed to live at a sibling path:
    ../CommunityMech/CommunityMech

Tests + examples are excluded (they contain synthetic CultureMech IDs
that don't exist in this corpus).

Each touched recipe gets a CurationEvent via the G10 helper. Re-runs
are idempotent — existing source_environment entries with matching ENVO
ids are skipped.

Usage:
    python scripts/backfill_source_environment.py [--dry-run]
                                                  [--communitymech-root PATH]
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))
from culturemech.curate.curation_event import record_curation_event  # noqa: E402

CURATOR = "backfill_source_environment.py"
ACTION = "BACKFILLED_SOURCE_ENVIRONMENT"
DEFAULT_COMMUNITYMECH = REPO_ROOT.parent / "CommunityMech" / "CommunityMech"
DEFAULT_DATA_ROOT = REPO_ROOT / "data" / "normalized_yaml"
SKIP_PREFIXES = ("tests/", "examples/")


def collect_env_links(cm_root: Path) -> dict[str, list[dict[str, Any]]]:
    """Walk CommunityMech YAMLs and return {culturemech_id: [env, ...]}.

    Deduped by (culturemech_id, envo_term_id); first observation wins
    for preferred_term / notes when multiple communities point to the
    same recipe with the same ENVO id.
    """
    by_recipe: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    for path in sorted(cm_root.rglob("*.yaml")):
        rel = str(path.relative_to(cm_root))
        if any(rel.startswith(p) for p in SKIP_PREFIXES):
            continue
        try:
            # path.read_text() can raise OSError on permission/disk errors
            # and UnicodeDecodeError on non-UTF-8 content — both should
            # skip the file rather than crash a multi-thousand-file scan
            # (Copilot caught this on PR #28).
            text = path.read_text(encoding="utf-8")
            doc = yaml.safe_load(text)
        except (OSError, UnicodeDecodeError, yaml.YAMLError):
            continue
        if not isinstance(doc, dict):
            continue
        env = doc.get("environment_term")
        if not isinstance(env, dict):
            continue
        cm_ids: set[str] = set()
        _collect_culturemech_ids(doc, cm_ids)
        if not cm_ids:
            continue
        term_section = env.get("term")
        envo_id = ""
        envo_label = ""
        if isinstance(term_section, dict):
            envo_id = (term_section.get("id") or "").strip()
            envo_label = (term_section.get("label") or "").strip()
        # Build a SourceEnvironmentDescriptor-shaped dict. Fall back to
        # the ENVO label or id when CommunityMech omitted preferred_term
        # — empty strings make for hard-to-use entries and break dedup
        # (Copilot caught this on PR #28).
        preferred_term = env.get("preferred_term") or envo_label or envo_id
        if not preferred_term:
            # No identifying info at all; skip rather than emit an empty
            # descriptor.
            continue
        descriptor: dict[str, Any] = {"preferred_term": preferred_term}
        # Only emit term.id (not term.label): the same ENVO CURIE has
        # been observed with different labels across CommunityMech
        # curators (e.g., ENVO:01001405 → "laboratory bioreactor" vs
        # "laboratory culture" vs "laboratory environment"), and Term.label
        # is intended to be the *canonical* ontology label. Downstream
        # consumers should resolve the label from ENVO directly.
        if envo_id:
            descriptor["term"] = {"id": envo_id}
        if env.get("notes"):
            descriptor["notes"] = env["notes"]
        dedup_key = envo_id or preferred_term
        for cmid in cm_ids:
            if dedup_key not in by_recipe[cmid]:
                by_recipe[cmid][dedup_key] = descriptor
    return {k: list(v.values()) for k, v in by_recipe.items()}


def _collect_culturemech_ids(node: Any, sink: set[str]) -> None:
    if isinstance(node, dict):
        cmid = node.get("culturemech_id")
        if isinstance(cmid, str) and cmid.startswith("CultureMech:"):
            sink.add(cmid)
        for v in node.values():
            _collect_culturemech_ids(v, sink)
    elif isinstance(node, list):
        for v in node:
            _collect_culturemech_ids(v, sink)


def index_recipes_by_id(data_root: Path) -> dict[str, Path]:
    """Index CultureMech recipes by id field."""
    out: dict[str, Path] = {}
    for path in data_root.rglob("*.yaml"):
        try:
            with path.open() as f:
                # Cheap scan: id is always on the first ~10 lines.
                for _ in range(20):
                    line = f.readline()
                    if not line:
                        break
                    if line.startswith("id: CultureMech:"):
                        rid = line.split(":", 1)[1].strip()
                        out[f"CultureMech:{rid.split(':', 1)[1] if ':' in rid else rid}"] = path
                        break
        except OSError:
            continue
    return out


def merge_into_recipe(
    recipe: dict[str, Any],
    new_envs: list[dict[str, Any]],
) -> tuple[int, int]:
    """Append new SourceEnvironmentDescriptor entries; skip if same ENVO
    id (or same preferred_term when no ENVO) already present.

    Also strips stale `term.label` values from any existing entry that
    appears to have come from a previous backfill — this script no
    longer propagates labels from CommunityMech (see collect_env_links)
    and re-running should normalize earlier writes.

    Source slot may be missing, a single dict (LinkML dataclasses accept
    one-or-many for multivalued slots), or a list. Normalize to a list
    in place before processing — Copilot caught the dict-shape edge on
    PR #28.

    Returns ``(added, normalized)`` — count of newly-appended entries
    and count of existing entries whose stale label was stripped.
    """
    raw = recipe.get("source_environment")
    if raw is None:
        existing: list[dict[str, Any]] = []
        recipe["source_environment"] = existing
    elif isinstance(raw, list):
        existing = raw
    elif isinstance(raw, dict):
        existing = [raw]
        recipe["source_environment"] = existing
    else:
        # Unrecognized shape — overwrite to a clean list rather than
        # silently corrupting the recipe.
        existing = []
        recipe["source_environment"] = existing

    normalized = 0
    for entry in existing:
        if not isinstance(entry, dict):
            continue
        term = entry.get("term")
        if isinstance(term, dict) and "label" in term:
            del term["label"]
            normalized += 1

    existing_keys: set[str] = set()
    for entry in existing:
        if not isinstance(entry, dict):
            continue
        envo_id = ((entry.get("term") or {}).get("id") or "").strip()
        existing_keys.add(envo_id or entry.get("preferred_term") or "")
    added = 0
    for env in new_envs:
        envo_id = ((env.get("term") or {}).get("id") or "").strip()
        key = envo_id or env.get("preferred_term") or ""
        if key in existing_keys:
            continue
        existing.append(env)
        existing_keys.add(key)
        added += 1
    return added, normalized


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--communitymech-root", type=Path, default=DEFAULT_COMMUNITYMECH)
    ap.add_argument("--data-root", type=Path, default=DEFAULT_DATA_ROOT)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.communitymech_root.is_dir():
        print(f"CommunityMech root not found: {args.communitymech_root}",
              file=sys.stderr)
        return 2

    print(f"Scanning {args.communitymech_root} for environment_term + culturemech_id links...",
          file=sys.stderr)
    links = collect_env_links(args.communitymech_root)
    print(f"  -> {sum(len(v) for v in links.values())} env entries "
          f"across {len(links)} CultureMech recipes", file=sys.stderr)

    print(f"Indexing recipes under {args.data_root}...", file=sys.stderr)
    recipe_index = index_recipes_by_id(args.data_root)
    print(f"  -> indexed {len(recipe_index)} recipes", file=sys.stderr)

    missing: list[str] = []
    touched = 0
    total_added = 0
    for cmid, envs in sorted(links.items()):
        path = recipe_index.get(cmid)
        if path is None:
            missing.append(cmid)
            continue
        with path.open() as f:
            recipe = yaml.safe_load(f)
        if not isinstance(recipe, dict):
            continue
        added, normalized = merge_into_recipe(recipe, envs)
        if added == 0 and normalized == 0:
            continue
        if added > 0:
            record_curation_event(
                recipe,
                curator=CURATOR,
                action=ACTION,
                notes=f"added={added} env(s) from CommunityMech",
                source="CommunityMech (environment_term + culturemech_id linkage)",
                skip_if_recent=True,
            )
        touched += 1
        total_added += added
        rel = path.relative_to(REPO_ROOT)
        marks = []
        if added:
            marks.append(f"added {added} env(s)")
        if normalized:
            marks.append(f"stripped {normalized} stale label(s)")
        print(f"  + {cmid}: {', '.join(marks)} -> {rel}", file=sys.stderr)
        if not args.dry_run:
            with path.open("w") as f:
                yaml.safe_dump(recipe, f, sort_keys=False, allow_unicode=True,
                               width=80)

    mode = "[DRY RUN] " if args.dry_run else ""
    print(file=sys.stderr)
    print(f"{mode}Recipes touched: {touched}", file=sys.stderr)
    print(f"{mode}Env entries added: {total_added}", file=sys.stderr)
    if missing:
        print(f"{mode}Skipped {len(missing)} CultureMech IDs not in corpus: "
              f"{', '.join(missing[:5])}{'...' if len(missing) > 5 else ''}",
              file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
