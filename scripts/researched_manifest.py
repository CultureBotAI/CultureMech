#!/usr/bin/env python3
"""Tracked manifest of media records that have completed Edison deep research.

Why this exists (#121): `research/` is gitignored, so any report that excluded
"already-researched" records by scanning `research/media/` was a function of
whoever last ran it. Regenerating on a different machine reordered the top-10
completely — a diff indistinguishable from "the author had researched more
locally".

The split:

  - `research/media/*-meta.yaml`  — untracked, machine-local, authoritative for
    what THIS machine actually ran.
  - `data/import_tracking/researched_media.json` — tracked, the shared view.
    The only input the prioritizer is allowed to read.

`refresh_researched_manifest.py` is the one step that crosses from untracked to
tracked, and it produces a reviewable diff. Everything downstream is then a pure
function of tracked data.

Manifest shape (sorted by slug, then job, for stable diffs)::

    {
      "description": "...",
      "entries": [
        {"slug": "lb_broth", "job": "literature", "task_id": "abc123"},
        ...
      ]
    }
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = REPO_ROOT / "data" / "import_tracking" / "researched_media.json"
DEFAULT_RESEARCH_DIR = REPO_ROOT / "research" / "media"
# Axis classification writes to its own directory so its reports cannot claim the
# `<slug>-edison-literature.md` filenames growth research keys its skip on.
AXIS_RESEARCH_DIR = REPO_ROOT / "research" / "media_axis"

_DESCRIPTION = (
    "Media records with a completed (non-dry-run) Edison deep-research run. "
    "Tracked so that deep_research_priority*.json are reproducible from git alone "
    "(see issue #121). Refresh with `just refresh-researched-manifest`; entries are "
    "merged, never dropped, so multiple machines can contribute."
)


def _entry_key(entry: dict[str, Any]) -> tuple[str, str, str]:
    """Identity of a run, for dedup and stable sort.

    `kind` is part of the key because growth research and axis classification run
    under the SAME job ("literature") on the same slug. Keyed on (slug, job) alone
    they collide, and since `merge_entries` unions by key, whichever ran first
    would permanently mask the other — a real growth run silently dropped as a
    duplicate of an axis run.

    Entries written before `kind` existed default to "medium", matching
    `researched_slugs()`, so legacy rows keep their identity and do not re-add.
    """
    return (str(entry.get("slug") or ""), str(entry.get("job") or ""),
            str(entry.get("kind") or "medium"))


def load_manifest(path: Path = DEFAULT_MANIFEST) -> list[dict[str, Any]]:
    """Return the manifest's entries, or [] when it does not exist.

    A missing manifest means "exclude nothing" rather than an error: the report
    stays a pure function of tracked data either way, and a fresh checkout with
    no manifest should still produce a usable ranking.
    """
    if not path.is_file():
        return []
    try:
        doc = json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        return []
    if isinstance(doc, dict):
        entries = doc.get("entries")
    elif isinstance(doc, list):
        entries = doc  # tolerate a bare list
    else:
        entries = None
    if not isinstance(entries, list):
        return []
    return [e for e in entries if isinstance(e, dict) and e.get("slug")]


def researched_slugs(path: Path = DEFAULT_MANIFEST) -> set[str]:
    """Media slugs with at least one completed MEDIUM-level run.

    Phase-2 per-organism follow-ups (`kind == "organism"`) are excluded: they
    research one organism against a medium, which does not mean the medium
    itself has been researched. Entries written before `kind` existed are
    treated as medium-level, matching the old behavior.
    """
    return {
        str(e["slug"]) for e in load_manifest(path)
        if str(e.get("kind") or "medium") == "medium"
    }


AXIS_TEMPLATE_STEM = "media_axis_classification"


def _is_axis_run(meta: dict[str, Any]) -> bool:
    """True iff this meta came from the axis-classification template.

    Keyed on the template rather than the output directory: the directory is a
    caller-supplied argument, so a run written elsewhere would be misclassified,
    while `template_path` is stamped into the meta by the runner itself.
    """
    return AXIS_TEMPLATE_STEM in str(meta.get("template_path") or "")


def scan_research_dir(research_dir: Path = DEFAULT_RESEARCH_DIR) -> list[dict[str, Any]]:
    """Read local `*-edison-*-meta.yaml` files into manifest entries.

    This is the ONLY function that reads untracked state. A dry-run meta costs
    nothing and produced no answer, so it is not a completed run.
    """
    if not research_dir.is_dir():
        return []
    found: list[dict[str, Any]] = []
    for meta_path in sorted(research_dir.glob("*-edison-*-meta.yaml")):
        try:
            meta = yaml.safe_load(meta_path.read_text()) or {}
        except (yaml.YAMLError, OSError):
            continue
        if not isinstance(meta, dict):
            continue
        status = str(meta.get("status") or "").lower()
        task_id = str(meta.get("task_id") or "")
        if not status or status == "dry-run" or not task_id:
            continue
        # `<slug>-edison-<job>-meta.yaml` -> slug, job
        stem = meta_path.name[: -len("-meta.yaml")]
        slug_from_name, _, job = stem.rpartition("-edison-")
        slug = str(meta.get("slug") or slug_from_name)
        entry: dict[str, Any] = {
            "slug": slug,
            "job": job or "unknown",
            "task_id": task_id,
        }
        # Phase-2 per-organism follow-ups are named
        # `<medium_slug>-organism-<organism>` and carry no `slug:` of their own.
        # They research ONE organism against a medium, which is not the same as
        # having researched the medium — so they are tagged and excluded from the
        # medium-level filter. Recording them anyway keeps the manifest a full
        # account of what was actually billed.
        if "-organism-" in slug:
            entry["kind"] = "organism"
            entry["media_slug"] = slug.split("-organism-", 1)[0]
        elif _is_axis_run(meta):
            # Axis classification (#152) asks which nutritional_class / functional_role
            # a medium has. It runs under the SAME job ("literature") as growth
            # research and produces the same `<slug>-edison-literature-meta.yaml`
            # filename, so job and filename cannot tell them apart — only the
            # template can.
            #
            # This distinction is load-bearing, not cosmetic. `researched_slugs()`
            # feeds the deep-research prioritizer's already-researched filter, so
            # tagging these "medium" would drop every axis-classified record out of
            # the growth-research queue — silently, since a smaller candidate list
            # looks like progress. Same failure the separate out-dir prevents one
            # layer down.
            entry["kind"] = "axis"
        else:
            entry["kind"] = "medium"
        found.append(entry)
    return found


def merge_entries(
    existing: list[dict[str, Any]],
    discovered: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Union `discovered` into `existing`, keyed by (slug, job).

    Returns (merged_sorted, newly_added). Union rather than replace: each machine
    sees only its own `research/media/`, so overwriting would silently delete
    another contributor's records. Entries are never dropped here — pruning is a
    deliberate, separate action.
    """
    by_key = {_entry_key(e): e for e in existing}
    added: list[dict[str, Any]] = []
    for entry in discovered:
        key = _entry_key(entry)
        if key not in by_key:
            by_key[key] = entry
            added.append(entry)
    merged = sorted(by_key.values(), key=_entry_key)
    return merged, added


def write_manifest(entries: list[dict[str, Any]], path: Path = DEFAULT_MANIFEST) -> None:
    """Write the manifest with sorted entries and a trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = {
        "description": _DESCRIPTION,
        "entries": sorted(entries, key=_entry_key),
    }
    path.write_text(json.dumps(doc, indent=2) + "\n")
