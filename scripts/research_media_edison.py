#!/usr/bin/env python3
"""Run Edison Scientific deep research against CultureMech media records.

Uses the `edison-client` SDK directly. The companion `research_media.py`
wraps `deep-research-client`.

The original reason for this second path is GONE: DRC 0.2.4 did not
register Edison at all, so the SDK was the only way to reach it. As of
DRC 0.2.10 it does — `deep-research-client providers` lists `falcon`
once `EDISON_API_KEY` is set (#284).

The path survives for a different and still-current reason: DRC's
`falcon` provider exposes only `system_prompt`, `allowed_domains`,
`temperature`, `max_tokens` and `max_embedded_images`. It does NOT
expose Edison's JOB selection, and job choice is the whole point of
this script — LITERATURE vs LITERATURE_HIGH vs precedent vs phoenix are
different agents at different costs. Routing through DRC today would
silently pin us to one job.

So: use `research_media.py --provider falcon` when the default job is
what you want and you would like the shared cache and output handling;
use this script when the job matters.

The default job is LITERATURE (== `job-futurehouse-paperqa3`), the
PaperQA agent — the best fit for "what organisms grow on this medium,
what is its pH, what are its CHEBI mappings"-type questions. Use
``--job literature-high`` for the deeper variant (more reads, higher
cost), ``--job precedent`` for first-mention search, ``--job phoenix``
for synthesis.

Auth: reads ``EDISON_PLATFORM_API_KEY`` (SDK-native) or ``EDISON_API_KEY``
(legacy alias from research_media.py) from environment. A repo-root
``.env`` is auto-loaded via python-dotenv.

Outputs land under ``research/media/{slug}-edison-{job}.md``
(``slug`` = YAML file stem to match research_media.py's DRC naming,
``job`` = lowercase-hyphenated job name, e.g. ``literature-high``). A
sibling ``{slug}-edison-{job}-meta.yaml`` captures the rendered query
text, task_id, total_cost, status, template_path, and template_vars —
sufficient for audit and re-runs.

Usage::

    # single record
    python scripts/research_media_edison.py --target dehalospirillum_medium

    # batch from the existing priority list
    python scripts/research_media_edison.py \\
        --batch data/import_tracking/reports/edison_batch.json --limit 5

    # different job
    python scripts/research_media_edison.py --target lb_broth --job literature-high

    # dry-run skips the API call but still writes the meta yaml
    # (including the full rendered query) so you can inspect the
    # prompt that would have been sent without spending credits.
    python scripts/research_media_edison.py --target lb_broth --dry-run

Records that already have a completed (non-dry-run) run for the SAME job are
skipped by default, so re-running a batch does not re-spend credits; pass
``--force`` to re-submit anyway. The skip is applied BEFORE ``--start`` /
``--limit``, which makes those windows count work still to do: repeating
``--limit 5`` walks forward 5 fresh records at a time instead of resubmitting
the same first five.
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
import _edison_capture as ec  # noqa: E402  -- response/citation/agent capture

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
    """Stable filename slug for output naming.

    Uses the YAML file stem (e.g. ``luria_bertani_lb_medium``) — human-
    readable and consistent with research_media.py's DRC outputs.
    The CultureMech CURIE ID is captured separately in the meta file.
    """
    return media_path.stem


def _short_job(job) -> str:
    """CLI-friendly filename suffix for a JobNames enum member.

    ``JobNames.LITERATURE_HIGH`` -> ``literature-high`` (hyphens, not
    underscores, to match the ``--job literature-high`` CLI alias).
    """
    return job.name.lower().replace("_", "-")


def _display_path(path: Path) -> str:
    """Show ``path`` relative to the repo when possible; else absolute.

    ``Path.relative_to`` raises ValueError when the target is outside
    REPO_ROOT (e.g. user passes ``--out-dir /tmp/research``); fall
    back to absolute string for display rather than crashing.
    """
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def has_existing_research(out_dir: Path, slug: str, job_short: str) -> bool:
    """True iff a completed (non-dry-run) Edison run already exists for this slug+job.

    Mirrors ``prioritize_deep_research_candidates.has_existing_research`` — a
    dry-run meta does NOT count, since it cost nothing and produced no answer.

    Scoped to the SAME job rather than any job (the prioritizer's
    ``{slug}-edison-*`` glob), because ``--job literature-high`` after
    ``--job literature`` is a deliberately different, more expensive question.
    Blocking that would be wrong; blocking an identical re-submission is the
    point.
    """
    meta_path = out_dir / f"{slug}-edison-{job_short}-meta.yaml"
    if not meta_path.is_file():
        return False
    try:
        meta = yaml.safe_load(meta_path.read_text()) or {}
    except (yaml.YAMLError, OSError):
        return False
    if not isinstance(meta, dict):
        return False
    status = str(meta.get("status") or "").lower()
    task_id = str(meta.get("task_id") or "")
    return bool(status and status != "dry-run" and task_id)


def partition_already_researched(
    targets: list[Path],
    out_dir: Path,
    job_short: str,
) -> tuple[list[Path], list[Path]]:
    """Split resolved targets into (to_submit, already_done), preserving order."""
    to_submit: list[Path] = []
    already: list[Path] = []
    for path in targets:
        if has_existing_research(out_dir, slug_for(path), job_short):
            already.append(path)
        else:
            to_submit.append(path)
    return to_submit, already


def run_one(
    client,
    media_path: Path,
    job,
    template_path: Path,
    out_dir: Path,
    dry_run: bool,
) -> dict[str, Any]:
    """Submit one task; write results to out_dir; return a stats dict.

    On a successful API call, ``_edison_capture.capture_full_response``
    writes a primary answer .md plus four sibling files
    (-response.json, -citations.md, -agent-state.json, -files.json)
    for full provenance. See scripts/_edison_capture.py for details.
    """
    from edison_client import TaskRequest

    query, variables = render_query(media_path, template_path)
    slug = slug_for(media_path)
    job_short = _short_job(job)
    stem = f"{slug}-edison-{job_short}"
    meta_path = out_dir / f"{stem}-meta.yaml"

    def _safe_rel(p: Path) -> str:
        return str(p.relative_to(REPO_ROOT)) if str(p).startswith(str(REPO_ROOT)) else str(p)

    base_meta: dict[str, Any] = {
        "slug": slug,
        "media_path": _safe_rel(media_path),
        "media_id": str(rm.load_media(media_path).get("id") or ""),
        "job": job.name,
        "job_id": job.value,
        "template_path": _safe_rel(template_path),
        "template_vars": variables,
        "query_chars": len(query),
        "query": query,
        "submitted_at": datetime.now(timezone.utc).isoformat(),
    }

    if dry_run:
        # Render the meta yaml even in dry-run so callers can audit
        # exactly what would be sent (and compare query_sha256 to
        # detect identical re-runs). No .md is written; only meta.
        meta = ec.capture_dry_run(out_dir=out_dir, stem=stem, query=query, base_meta=base_meta)
        meta_path.write_text(yaml.safe_dump(meta, sort_keys=False,
                                            allow_unicode=True, width=100))
        md_path = out_dir / f"{stem}.md"
        print(f"[DRY RUN] {_display_path(media_path)} -> {_display_path(md_path)}")
        print(f"          job={job.name} query_chars={len(query)} meta={_display_path(meta_path)}")
        return {"slug": slug, "status": "dry-run", "cost": 0.0}

    out_dir.mkdir(parents=True, exist_ok=True)
    task = TaskRequest(name=job, query=query)
    print(f"  + submitting {slug} ({job.name})...", flush=True)
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
    print(f"    -> {_display_path(md_path)}  cost={total_cost}  "
          f"citations={meta.get('citations_parsed')}  "
          f"agent_state={meta.get('sidecar_files', {}).get('agent_state_json', False)}")
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
    ap.add_argument("--force", action="store_true",
                    help="Re-submit records that already have a completed run for this "
                         "job, re-spending credits. Default: skip them.")
    args = ap.parse_args(argv)

    job = resolve_job(args.job)

    targets: list[Path]
    if args.target:
        targets = [rm.resolve_media_file(args.target)]
    else:
        candidate_lists = load_batch_targets(args.batch)
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

    # Drop already-researched records BEFORE applying --start/--limit, so the
    # window counts work still to do. Windowing first would make `--limit 5` mean
    # "the first 5 batch entries" — re-billing any of them already done, and
    # advancing by fewer than 5 new records per run.
    job_short = _short_job(job)
    skipped: list[Path] = []
    if not args.force:
        targets, skipped = partition_already_researched(targets, args.out_dir, job_short)

    if args.batch:
        targets = targets[args.start:]
        if args.limit is not None:
            targets = targets[: args.limit]

    if not targets:
        if skipped:
            print(f"All {len(skipped)} resolved record(s) already have a completed "
                  f"{job.name} run; nothing to submit. Use --force to re-run them.")
            return 0
        print("No targets to research.", file=sys.stderr)
        return 2

    print(f"Edison job:    {job.name} ({job.value})")
    print(f"Template:      {_display_path(args.template.resolve())}")
    print(f"Output dir:    {_display_path(args.out_dir.resolve())}")
    print(f"Recipes:       {len(targets)} to submit"
          + (f", {len(skipped)} skipped (already researched)" if skipped else ""))
    if args.force:
        print("Mode:          --force (re-submitting regardless of existing runs)")
    if args.dry_run:
        print("Mode:          DRY RUN (no API calls, no credits spent)")
    print()
    if skipped:
        for p in skipped[:5]:
            print(f"  skip {slug_for(p)} — completed {job_short} run exists")
        if len(skipped) > 5:
            print(f"  skip ... {len(skipped) - 5} more")
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

    print()
    print(f"Done. {len(results)} submitted / {len(skipped)} skipped (already researched).")
    if not args.dry_run:
        total_cost = sum(r["cost"] or 0.0 for r in results)
        print(f"Total reported cost: {total_cost:.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
