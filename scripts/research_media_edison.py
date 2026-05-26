#!/usr/bin/env python3
"""Run Edison Scientific deep research against CultureMech media records.

Uses the `edison-client` SDK directly. The companion `research_media.py`
wraps `deep-research-client`, but as of DRC 0.2.4 only `cyberian` and
`openai` are registered providers — Edison/PaperQA is not exposed
there, so we drive the SDK directly.

The default job is LITERATURE (== `job-futurehouse-paperqa3`), the
PaperQA agent — the best fit for "what organisms grow on this medium,
what is its pH, what are its CHEBI mappings"-type questions. Use
``--job literature-high`` for the deeper variant (more reads, higher
cost), ``--job precedent`` for first-mention search, ``--job phoenix``
for synthesis.

Auth: reads ``EDISON_PLATFORM_API_KEY`` (SDK-native) or ``EDISON_API_KEY``
(legacy alias from research_media.py) from environment. A repo-root
``.env`` is auto-loaded via python-dotenv.

Outputs land under ``research/media/{slug}-edison-{job}.md`` (matching
the existing DRC naming convention used by research_media.py). A
sibling ``{slug}-edison-{job}-meta.yaml`` captures task_id, cost,
status, and the prompt that was sent — useful for audit and re-runs.

Usage::

    # single record
    python scripts/research_media_edison.py --target dehalospirillum_medium

    # batch from the existing priority list
    python scripts/research_media_edison.py \\
        --batch data/import_tracking/reports/edison_batch.json --limit 5

    # different job
    python scripts/research_media_edison.py --target lb_broth --job literature-high

    # dry-run prints the rendered query without spending credits
    python scripts/research_media_edison.py --target lb_broth --dry-run
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import research_media as rm  # noqa: E402  -- reuse template_vars + resolve

DEFAULT_TEMPLATE = REPO_ROOT / "templates" / "media_growth_research.md"
DEFAULT_OUT_DIR = REPO_ROOT / "research" / "media"


_JOB_ALIASES: dict[str, str] = {
    "literature": "LITERATURE",
    "paperqa": "LITERATURE",
    "literature-high": "LITERATURE_HIGH",
    "literature_high": "LITERATURE_HIGH",
    "paperqa-high": "LITERATURE_HIGH",
    "precedent": "PRECEDENT",
    "phoenix": "PHOENIX",
}


def resolve_job(name: str):
    """Map a user-friendly --job alias to the edison_client JobNames enum."""
    from edison_client import JobNames

    key = _JOB_ALIASES.get(name.lower())
    if key is None:
        raise SystemExit(
            f"Unknown --job '{name}'. Choose one of: "
            + ", ".join(sorted(_JOB_ALIASES))
        )
    return getattr(JobNames, key)


def load_api_key() -> str:
    """Pick up the Edison key from env (with the legacy alias).

    The SDK natively reads ``EDISON_PLATFORM_API_KEY``; older code in
    this repo set ``EDISON_API_KEY``. Honor both.
    """
    load_dotenv(REPO_ROOT / ".env")
    key = os.environ.get("EDISON_PLATFORM_API_KEY") or os.environ.get("EDISON_API_KEY")
    if not key:
        raise SystemExit(
            "EDISON_PLATFORM_API_KEY (or EDISON_API_KEY) is not set. "
            "Add it to .env at the repo root, or `export EDISON_PLATFORM_API_KEY=...` "
            "in your shell."
        )
    return key


def render_query(media_path: Path, template_path: Path) -> tuple[str, dict[str, str]]:
    """Render the deep-research template for a single recipe.

    Returns ``(query_text, template_vars)`` so callers can stamp the
    variables into the meta file alongside the rendered query.
    """
    doc = rm.load_media(media_path)
    variables = rm.template_vars(doc, media_path)
    template = template_path.read_text()
    return template.format_map(_DefaultEmpty(variables)), variables


class _DefaultEmpty(dict):
    """``str.format_map`` helper: leave unknown placeholders blank instead of KeyError."""

    def __missing__(self, key):  # noqa: ANN001
        return ""


def slug_for(media_path: Path) -> str:
    """Stable filename slug for output naming."""
    doc = rm.load_media(media_path)
    cid = str(doc.get("id") or "")
    if ":" in cid:
        return cid.split(":", 1)[1]
    return media_path.stem


def run_one(
    client,
    media_path: Path,
    job,
    template_path: Path,
    out_dir: Path,
    dry_run: bool,
) -> dict[str, Any]:
    """Submit one task; write results to out_dir; return a stats dict."""
    from edison_client import TaskRequest

    query, variables = render_query(media_path, template_path)
    slug = slug_for(media_path)
    job_short = job.name.lower()
    md_path = out_dir / f"{slug}-edison-{job_short}.md"
    meta_path = out_dir / f"{slug}-edison-{job_short}-meta.yaml"

    if dry_run:
        print(f"[DRY RUN] {media_path.relative_to(REPO_ROOT)} -> {md_path.relative_to(REPO_ROOT)}")
        print(f"          job={job.name} query_chars={len(query)}")
        return {"slug": slug, "status": "dry-run", "cost": 0.0}

    out_dir.mkdir(parents=True, exist_ok=True)
    task = TaskRequest(name=job, query=query)
    print(f"  + submitting {slug} ({job.name})...", flush=True)
    [response] = client.run_tasks_until_done(task, progress_bar=False)

    # PaperQA-family responses carry the answer + cost; other jobs may not.
    formatted_answer = getattr(response, "formatted_answer", None)
    answer = getattr(response, "answer", None)
    total_cost = getattr(response, "total_cost", None)
    body = formatted_answer or answer or "(no answer field on this job's response type)"
    md_path.write_text(body)

    meta = {
        "slug": slug,
        "media_path": str(media_path.relative_to(REPO_ROOT)),
        "job": job.name,
        "job_id": job.value,
        "task_id": str(getattr(response, "task_id", None) or ""),
        "status": getattr(response, "status", None),
        "submitted_at": datetime.now(timezone.utc).isoformat(),
        "total_cost": total_cost,
        "total_queries": getattr(response, "total_queries", None),
        "has_successful_answer": getattr(response, "has_successful_answer", None),
        "template_vars": variables,
        "query_chars": len(query),
    }
    meta_path.write_text(yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100))
    print(f"    -> {md_path.relative_to(REPO_ROOT)}  cost={total_cost}")
    return {"slug": slug, "status": meta["status"], "cost": total_cost or 0.0}


def load_batch_targets(batch_path: Path) -> list[list[str]]:
    """Return candidate identifiers per entry from a edison_batch.json file.

    Each entry carries both ``recipe_name`` (slug) and ``file_path``
    (relative to ``data/normalized_yaml/``). The batch file dates from
    before the snake_case rename, so ``file_path`` often points at a
    legacy filename; ``recipe_name`` (slug) is what survives. Return
    ALL candidates per entry so callers can fall through on first miss.
    """
    data = json.loads(batch_path.read_text())
    if not isinstance(data, list):
        raise SystemExit(f"--batch expects a JSON list of records: {batch_path}")
    out: list[list[str]] = []
    for entry in data:
        if not isinstance(entry, dict):
            continue
        candidates = [
            entry.get("recipe_name"),
            entry.get("file_path"),
        ]
        candidates = [c for c in candidates if c]
        if candidates:
            out.append(candidates)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--target", help="Media YAML path, slug, ID, name, or original name.")
    src.add_argument("--batch", type=Path, help="Path to edison_batch.json (or similar list).")
    ap.add_argument("--job", default="literature",
                    help="literature (paperqa3, default) | literature-high | precedent | phoenix")
    ap.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    ap.add_argument("--limit", type=int, default=None,
                    help="When using --batch, cap the number of recipes to research.")
    ap.add_argument("--start", type=int, default=0,
                    help="When using --batch, skip this many entries before submitting.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Render queries + print plan; do NOT call the API.")
    args = ap.parse_args(argv)

    job = resolve_job(args.job)

    targets: list[Path]
    if args.target:
        targets = [rm.resolve_media_file(args.target)]
    else:
        candidate_lists = load_batch_targets(args.batch)
        candidate_lists = candidate_lists[args.start:]
        if args.limit is not None:
            candidate_lists = candidate_lists[: args.limit]
        targets = []
        unresolved: list[str] = []
        media_dir = REPO_ROOT / "data" / "normalized_yaml"
        for candidates in candidate_lists:
            resolved: Path | None = None
            # Prefer a verbatim `data/normalized_yaml/<candidate>` lookup
            # for candidates that look like relative paths (have a "/"
            # or end with ".yaml"). resolve_media_file doesn't apply
            # this prefix and slug-only fallback hits multi-match
            # ValueErrors when the slug is shared across several files
            # (e.g., "dehalospirillum_medium" appears in TOGO/KOMODO/
            # JCM variants of the same canonical recipe).
            for name in candidates:
                if "/" in name or name.endswith(".yaml"):
                    p = media_dir / name
                    if p.is_file():
                        resolved = p.resolve()
                        break
            if resolved is None:
                for name in candidates:
                    try:
                        resolved = rm.resolve_media_file(name)
                        break
                    except (FileNotFoundError, ValueError):
                        continue
            if resolved is None:
                unresolved.append(" / ".join(candidates))
            else:
                targets.append(resolved)
        if unresolved:
            print(f"Note: skipped {len(unresolved)} unresolvable batch entries:",
                  file=sys.stderr)
            for u in unresolved[:5]:
                print(f"  - {u}", file=sys.stderr)
            if len(unresolved) > 5:
                print(f"  - ... {len(unresolved) - 5} more", file=sys.stderr)

    if not targets:
        print("No targets to research.", file=sys.stderr)
        return 2

    print(f"Edison job:    {job.name} ({job.value})")
    print(f"Template:      {args.template.relative_to(REPO_ROOT)}")
    print(f"Output dir:    {args.out_dir.relative_to(REPO_ROOT)}")
    print(f"Recipes:       {len(targets)}")
    if args.dry_run:
        print("Mode:          DRY RUN (no API calls, no credits spent)")
    print()

    client = None
    if not args.dry_run:
        api_key = load_api_key()
        from edison_client import EdisonClient
        client = EdisonClient(api_key=api_key)

    results: list[dict[str, Any]] = []
    try:
        for media_path in targets:
            results.append(
                run_one(client, media_path, job, args.template, args.out_dir, args.dry_run)
            )
    finally:
        if client is not None:
            client.close()

    if not args.dry_run:
        total_cost = sum(r["cost"] or 0.0 for r in results)
        print()
        print(f"Done. {len(results)} recipes researched. Total reported cost: {total_cost:.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
