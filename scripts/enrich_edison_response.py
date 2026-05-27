#!/usr/bin/env python3
"""Retroactively enrich Edison research outputs with full provenance.

For each ``research/media/*-edison-*-meta.yaml`` carrying a real
``task_id`` (i.e. status != "dry-run"), pull the verbose response via
``client.get_task(task_id, verbose=True)`` and any artifact-file
listing via ``client.list_files(trajectory_id)`` and write the
missing sidecar files:

    {stem}-response.json   full response.model_dump
    {stem}-citations.md    parsed reference list
    {stem}-agent-state.json   tool-call trace + env frame + metadata
    {stem}-files.json      artifact-file inventory

These secondary calls are **metadata-only** — no Edison compute is
re-billed; Edison stores task results and serves them back.

Use cases:
  - You ran phase-1 with the old script that only saved the answer
    md + a sparse meta; this backfills everything you originally
    missed.
  - A live run partially completed and you want to confirm exactly
    what came back without re-running.
  - You want the full agent-state trace for debugging a surprising
    answer.

Usage::

    # Enrich every meta yaml that's missing sidecars
    python scripts/enrich_edison_response.py

    # Limit to a specific medium / pattern
    python scripts/enrich_edison_response.py --pattern 'archaeoglobus_*'

    # Force re-write of sidecars even if they already exist
    python scripts/enrich_edison_response.py --force

    # See what would happen without making any API calls
    python scripts/enrich_edison_response.py --dry-run
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import _edison_capture as ec  # noqa: E402
import research_media_edison as rme  # noqa: E402  -- reuse load_api_key

DEFAULT_RESEARCH_DIR = REPO_ROOT / "research" / "media"


def _strip_meta_suffix(name: str) -> str:
    """Drop the ``-meta.yaml`` tail to get the stem the capture helper used."""
    if name.endswith("-meta.yaml"):
        return name[: -len("-meta.yaml")]
    if name.endswith(".yaml"):
        return name[: -len(".yaml")]
    return name


def needs_enrichment(out_dir: Path, stem: str, *, force: bool) -> dict[str, bool]:
    """Return a dict of which sidecars are missing for this stem."""
    return {
        "response_json": force or not (out_dir / f"{stem}-response.json").exists(),
        "citations_md": force or not (out_dir / f"{stem}-citations.md").exists(),
        "agent_state_json": force or not (out_dir / f"{stem}-agent-state.json").exists(),
        "files_json": force or not (out_dir / f"{stem}-files.json").exists(),
        "answer_md": force or not (out_dir / f"{stem}.md").exists(),
    }


def enrich_one(client: Any, meta_path: Path, *, force: bool, dry_run: bool) -> dict[str, Any]:
    """Pull verbose + files for one meta. Returns a stats dict."""
    meta = yaml.safe_load(meta_path.read_text())
    if not isinstance(meta, dict):
        return {"path": str(meta_path), "status": "invalid-meta", "wrote": []}

    status = str(meta.get("status") or "").lower()
    task_id = str(meta.get("task_id") or "")
    if status == "dry-run" or not task_id:
        return {"path": str(meta_path), "status": "skipped-no-task-id", "wrote": []}

    stem = _strip_meta_suffix(meta_path.name)
    out_dir = meta_path.parent
    missing = needs_enrichment(out_dir, stem, force=force)
    if not any(missing.values()):
        return {"path": str(meta_path), "status": "already-complete", "wrote": []}

    print(f"  + enriching {stem}  (missing: "
          f"{[k for k, v in missing.items() if v]})", flush=True)

    if dry_run:
        return {"path": str(meta_path), "status": "dry-run",
                "would_write": [k for k, v in missing.items() if v]}

    wrote: list[str] = []

    # Verbose fetch covers: response.json (using verbose payload as
    # canonical), agent-state.json, and lets us refresh meta fields
    # we may have skipped originally (answer_reasoning, etc.).
    try:
        verbose = client.get_task(task_id=task_id, verbose=True)
    except Exception as exc:  # pylint: disable=broad-except
        print(f"    ! verbose fetch failed: {exc}", file=sys.stderr)
        verbose = None

    # Always try the non-verbose response too for answer/formatted_answer/cost
    # (some response classes carry these only in the non-verbose form).
    try:
        normal = client.get_task(task_id=task_id, verbose=False)
    except Exception as exc:  # pylint: disable=broad-except
        print(f"    ! normal fetch failed: {exc}", file=sys.stderr)
        normal = None

    primary = normal or verbose
    if primary is None:
        return {"path": str(meta_path), "status": "fetch-failed", "wrote": []}

    # Re-derive answer body and write the .md if missing
    answer = getattr(primary, "answer", None)
    formatted_answer = getattr(primary, "formatted_answer", None)
    if missing["answer_md"]:
        body = formatted_answer or answer or "(no answer field on this job's response type)"
        (out_dir / f"{stem}.md").write_text(body)
        wrote.append("answer_md")

    if missing["response_json"]:
        merged: dict[str, Any] = {}
        if normal is not None:
            merged["response"] = ec._safe_model_dump(normal)  # pylint: disable=protected-access
        if verbose is not None:
            merged["verbose"] = ec._safe_model_dump(verbose)  # pylint: disable=protected-access
        (out_dir / f"{stem}-response.json").write_text(
            json.dumps(merged, indent=2, default=str))
        wrote.append("response_json")

    if missing["citations_md"]:
        citations = ec.parse_citations(formatted_answer or answer)
        query = str(meta.get("query") or "")
        (out_dir / f"{stem}-citations.md").write_text(
            ec.render_citations_md(citations, query=query))
        wrote.append("citations_md")

    if missing["agent_state_json"] and verbose is not None:
        agent_state = ec._safe_model_dump(getattr(verbose, "agent_state", None))  # pylint: disable=protected-access
        environment_frame = ec._safe_model_dump(getattr(verbose, "environment_frame", None))  # pylint: disable=protected-access
        verbose_metadata = ec._safe_model_dump(getattr(verbose, "metadata", None))  # pylint: disable=protected-access
        if any(x is not None for x in (agent_state, environment_frame, verbose_metadata)):
            (out_dir / f"{stem}-agent-state.json").write_text(json.dumps({
                "task_id": task_id,
                "agent_state": agent_state,
                "environment_frame": environment_frame,
                "metadata": verbose_metadata,
            }, indent=2, default=str))
            wrote.append("agent_state_json")

    if missing["files_json"]:
        try:
            files_listing = client.list_files(trajectory_id=task_id)
        except Exception as exc:  # pylint: disable=broad-except
            print(f"    ! list_files failed: {exc}", file=sys.stderr)
            files_listing = None
        if files_listing is not None:
            (out_dir / f"{stem}-files.json").write_text(
                json.dumps(ec._safe_model_dump(files_listing),  # pylint: disable=protected-access
                           indent=2, default=str))
            wrote.append("files_json")

    # Refresh the meta yaml with the now-richer field set
    updates: dict[str, Any] = {
        "answer_chars": len(answer or ""),
        "formatted_answer_chars": len(formatted_answer or ""),
        "has_answer_reasoning": bool(getattr(primary, "answer_reasoning", None)),
        "answer_reasoning_chars": len(getattr(primary, "answer_reasoning", "") or ""),
        "citations_parsed": len(ec.parse_citations(formatted_answer or answer)),
        "sidecar_files": ec._existing_sidecars(out_dir, stem),  # pylint: disable=protected-access
        "enriched_at": ec._to_iso(__import__("datetime").datetime.now(  # pylint: disable=protected-access
            __import__("datetime").timezone.utc)),
    }
    # Preserve existing query_sha256, but stamp it in if missing.
    if not meta.get("query_sha256") and meta.get("query"):
        updates["query_sha256"] = ec.query_sha256(str(meta["query"]))
    # Pull through fields we may not have captured originally.
    for field in ("job_name", "user", "agent_name", "build_owner",
                  "environment_name", "share_status"):
        val = getattr(primary, field, None)
        if val is not None and meta.get(field) is None:
            updates[field] = val
    created_at = getattr(primary, "created_at", None)
    if created_at is not None and not meta.get("created_at"):
        updates["created_at"] = ec._to_iso(created_at)  # pylint: disable=protected-access

    meta.update(updates)
    meta_path.write_text(yaml.safe_dump(meta, sort_keys=False,
                                        allow_unicode=True, width=100))

    return {"path": str(meta_path), "status": "enriched", "wrote": wrote}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--research-dir", type=Path, default=DEFAULT_RESEARCH_DIR,
                    help="Directory containing *-edison-*-meta.yaml files.")
    ap.add_argument("--pattern", default="*-edison-*-meta.yaml",
                    help="Glob pattern for meta yamls to consider.")
    ap.add_argument("--force", action="store_true",
                    help="Re-write sidecars even if they already exist.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Show what would be enriched without making API calls.")
    args = ap.parse_args(argv)

    if not args.research_dir.is_dir():
        print(f"Research dir not found: {args.research_dir}", file=sys.stderr)
        return 2

    meta_paths = sorted(args.research_dir.glob(args.pattern))
    if not meta_paths:
        print(f"No metas matched {args.pattern} under {args.research_dir}")
        return 0

    print(f"Considering {len(meta_paths)} meta yamls in "
          f"{args.research_dir.relative_to(REPO_ROOT)}/")

    client = None
    if not args.dry_run:
        api_key = rme.load_api_key()
        from edison_client import EdisonClient
        client = EdisonClient(api_key=api_key)

    results: list[dict[str, Any]] = []
    try:
        for meta_path in meta_paths:
            results.append(enrich_one(client, meta_path,
                                      force=args.force, dry_run=args.dry_run))
    finally:
        if client is not None:
            client.close()

    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    print()
    print("Summary:")
    for k, v in sorted(by_status.items()):
        print(f"  {k:>22}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
