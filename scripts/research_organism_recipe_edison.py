#!/usr/bin/env python3
"""Phase-2 Edison deep research: extract a recipe for one organism on a parent medium.

This is the per-organism follow-up to scripts/research_media_edison.py.
The phase-1 medium-level search returns candidate organisms reported
to grow on a medium; this script drills into ONE organism at a time
and asks the API to extract the formulation + culture conditions +
identifiers from the primary publication(s).

Renders templates/medium_organism_recipe_extraction.md against the
parent medium YAML (for context) plus organism-specific variables
passed on the command line, submits an Edison literature task, and
writes the answer + a sibling meta yaml capturing the task_id, cost,
status, full rendered query, and per-organism variables.

Usage::

    # single organism on a single medium
    python scripts/research_organism_recipe_edison.py \\
        --target dehalospirillum_medium \\
        --organism "Dehalospirillum multivorans" \\
        --strain "DSM 12446"

    # supply a citation hint and a snippet from phase 1
    python scripts/research_organism_recipe_edison.py \\
        --target lb_broth \\
        --organism "Escherichia coli" \\
        --citation-hint "PMID:6347985" \\
        --phase1-snippet "grown in LB broth at 37C overnight"

    # drive a batch of organisms (one JSON file: list of dicts with
    # at least {target, organism, [strain, citation_hint,
    # phase1_snippet, identifiers]})
    python scripts/research_organism_recipe_edison.py \\
        --organisms-batch research/media/dehalospirillum_medium-organisms.json

    # dry-run renders the query + writes meta yaml; no API call
    python scripts/research_organism_recipe_edison.py \\
        --target lb_broth --organism "Escherichia coli" --dry-run
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import research_media as rm  # noqa: E402  -- reuse template_vars + resolve
import research_media_edison as rme  # noqa: E402  -- reuse auth/job/dry-run helpers
import _edison_capture as ec  # noqa: E402  -- response/citation/agent capture

DEFAULT_TEMPLATE = REPO_ROOT / "templates" / "medium_organism_recipe_extraction.md"
DEFAULT_OUT_DIR = REPO_ROOT / "research" / "media"


def _slug_organism(name: str, strain: str | None) -> str:
    """Filesystem-safe slug for an organism (+ optional strain).

    Used to disambiguate per-organism output files within the same
    parent medium's research directory. Lowercase, ascii word
    characters and hyphens only.
    """
    parts = [name]
    if strain:
        parts.append(strain)
    s = " ".join(parts).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "organism"


def render_organism_query(
    media_path: Path,
    template_path: Path,
    *,
    organism: str,
    strain: str | None,
    identifiers: str | None,
    citation_hint: str | None,
    phase1_snippet: str | None,
) -> tuple[str, dict[str, Any]]:
    """Render the per-organism template against parent medium + organism vars."""
    doc = rm.load_media(media_path)
    variables: dict[str, Any] = dict(rm.template_vars(doc, media_path))
    variables.update(
        {
            "organism_name": organism,
            "organism_strain": strain or "",
            "organism_identifiers": identifiers or "",
            "citation_hint": citation_hint or "",
            "phase1_snippet": phase1_snippet or "",
        }
    )
    template = template_path.read_text()
    query = template.format_map(rme._DefaultEmpty(variables))
    return query, variables


def run_one(
    client,
    media_path: Path,
    *,
    organism: str,
    strain: str | None,
    identifiers: str | None,
    citation_hint: str | None,
    phase1_snippet: str | None,
    job,
    template_path: Path,
    out_dir: Path,
    dry_run: bool,
) -> dict[str, Any]:
    """Submit one per-organism task; capture md + sidecars + meta yaml.

    See scripts/_edison_capture.py — the full provenance bundle
    (-response.json, -citations.md, -agent-state.json, -files.json)
    lands alongside the primary .md.
    """
    media_slug = rme.slug_for(media_path)
    organism_slug = _slug_organism(organism, strain)
    job_short = rme._short_job(job)
    stem = f"{media_slug}-organism-{organism_slug}-edison-{job_short}"
    meta_path = out_dir / f"{stem}-meta.yaml"

    query, variables = render_organism_query(
        media_path,
        template_path,
        organism=organism,
        strain=strain,
        identifiers=identifiers,
        citation_hint=citation_hint,
        phase1_snippet=phase1_snippet,
    )

    def _safe_rel(p: Path) -> str:
        return str(p.relative_to(REPO_ROOT)) if str(p).startswith(str(REPO_ROOT)) else str(p)

    base_meta: dict[str, Any] = {
        "media_slug": media_slug,
        "media_path": _safe_rel(media_path),
        "media_id": str(rm.load_media(media_path).get("id") or ""),
        "organism": organism,
        "organism_strain": strain or "",
        "organism_slug": organism_slug,
        "job": job.name,
        "job_id": job.value,
        "template_path": _safe_rel(template_path),
        "template_vars": variables,
        "query_chars": len(query),
        "query": query,
        "submitted_at": datetime.now(timezone.utc).isoformat(),
    }

    if dry_run:
        meta = ec.capture_dry_run(out_dir=out_dir, stem=stem, query=query, base_meta=base_meta)
        meta_path.write_text(yaml.safe_dump(meta, sort_keys=False,
                                            allow_unicode=True, width=100))
        md_path = out_dir / f"{stem}.md"
        print(f"[DRY RUN] {rme._display_path(media_path)} :: {organism!r}"
              f" -> {rme._display_path(md_path)}")
        print(f"          job={job.name} query_chars={len(query)} meta={rme._display_path(meta_path)}")
        return {"organism": organism, "status": "dry-run", "cost": 0.0}

    from edison_client import TaskRequest

    out_dir.mkdir(parents=True, exist_ok=True)
    task = TaskRequest(name=job, query=query)
    print(f"  + submitting {organism!r} on {media_slug} ({job.name})...", flush=True)
    [response] = client.run_tasks_until_done(task, progress_bar=False)

    meta = ec.capture_full_response(
        response=response,
        client=client,
        out_dir=out_dir,
        stem=stem,
        query=query,
        base_meta=base_meta,
    )
    meta_path.write_text(yaml.safe_dump(meta, sort_keys=False,
                                        allow_unicode=True, width=100))
    md_path = out_dir / f"{stem}.md"
    total_cost = meta.get("total_cost")
    print(f"    -> {rme._display_path(md_path)}  cost={total_cost}  "
          f"citations={meta.get('citations_parsed')}  "
          f"agent_state={meta.get('sidecar_files', {}).get('agent_state_json', False)}")
    return {"organism": organism, "status": meta["status"], "cost": total_cost or 0.0}


def load_organisms_batch(path: Path) -> list[dict[str, Any]]:
    """Load a JSON list of per-organism request dicts.

    Each entry must have at least ``target`` and ``organism``. Optional
    fields: ``strain``, ``identifiers``, ``citation_hint``,
    ``phase1_snippet``.
    """
    data = json.loads(path.read_text())
    if not isinstance(data, list):
        raise SystemExit(f"--organisms-batch expects a JSON list: {path}")
    out: list[dict[str, Any]] = []
    for entry in data:
        if not isinstance(entry, dict):
            continue
        if not entry.get("target") or not entry.get("organism"):
            print(f"Note: skipping entry without target+organism: {entry}", file=sys.stderr)
            continue
        out.append(entry)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--target",
                     help="Parent media YAML path, slug, ID, name, or original name.")
    src.add_argument("--organisms-batch", type=Path,
                     help="JSON list of {target, organism, ...} dicts.")
    ap.add_argument("--organism",
                    help="Organism name (required unless --organisms-batch).")
    ap.add_argument("--strain", default=None, help="Strain designation (optional).")
    ap.add_argument("--identifiers", default=None,
                    help="Comma-separated identifier hints (NCBITaxon, GTDB, GCF_, DSM, etc.).")
    ap.add_argument("--citation-hint", default=None,
                    help="PMID/DOI/URL from phase-1 results to focus extraction on.")
    ap.add_argument("--phase1-snippet", default=None,
                    help="Evidence snippet from phase-1 results (helps the API anchor on the right paper).")
    ap.add_argument("--job", default="literature",
                    help="literature (paperqa3, default) | literature-high | precedent | phoenix")
    ap.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    ap.add_argument("--limit", type=int, default=None,
                    help="When using --organisms-batch, cap the number of organisms processed.")
    ap.add_argument("--start", type=int, default=0,
                    help="When using --organisms-batch, skip this many entries before submitting.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Render queries + print plan; do NOT call the API.")
    args = ap.parse_args(argv)

    if args.target and not args.organism:
        raise SystemExit("--organism is required when --target is used.")

    job = rme.resolve_job(args.job)

    # Build the unified work list: (media_path, organism, strain, ids, cite, snippet)
    work: list[tuple[Path, str, str | None, str | None, str | None, str | None]] = []
    if args.target:
        media_path = rm.resolve_media_file(args.target)
        work.append((
            media_path, args.organism, args.strain, args.identifiers,
            args.citation_hint, args.phase1_snippet,
        ))
    else:
        entries = load_organisms_batch(args.organisms_batch)
        entries = entries[args.start:]
        if args.limit is not None:
            entries = entries[: args.limit]
        for entry in entries:
            try:
                media_path = rm.resolve_media_file(entry["target"])
            except (FileNotFoundError, ValueError) as exc:
                print(f"Note: skipping {entry['target']!r}: {exc}", file=sys.stderr)
                continue
            work.append((
                media_path,
                entry["organism"],
                entry.get("strain"),
                entry.get("identifiers"),
                entry.get("citation_hint"),
                entry.get("phase1_snippet"),
            ))

    if not work:
        print("No per-organism tasks to run.", file=sys.stderr)
        return 2

    print(f"Edison job:    {job.name} ({job.value})")
    print(f"Template:      {rme._display_path(args.template.resolve())}")
    print(f"Output dir:    {rme._display_path(args.out_dir.resolve())}")
    print(f"Tasks:         {len(work)}")
    if args.dry_run:
        print("Mode:          DRY RUN (no API calls, no credits spent)")
    print()

    client = None
    if not args.dry_run:
        api_key = rme.load_api_key()
        from edison_client import EdisonClient
        client = EdisonClient(api_key=api_key)

    results: list[dict[str, Any]] = []
    try:
        for media_path, organism, strain, ids, cite, snippet in work:
            results.append(run_one(
                client,
                media_path,
                organism=organism,
                strain=strain,
                identifiers=ids,
                citation_hint=cite,
                phase1_snippet=snippet,
                job=job,
                template_path=args.template,
                out_dir=args.out_dir,
                dry_run=args.dry_run,
            ))
    finally:
        if client is not None:
            client.close()

    if not args.dry_run:
        total_cost = sum(r["cost"] or 0.0 for r in results)
        print()
        print(f"Done. {len(results)} organism tasks completed. Total reported cost: {total_cost:.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
