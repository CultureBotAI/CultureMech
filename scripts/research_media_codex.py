#!/usr/bin/env python3
"""Run media research through the local Codex CLI (#284).

A third research path, and it exists because the other two are constrained:

  * `research_media.py` wraps `deep-research-client`. Its `falcon` (Edison) provider
    returns **HTTP 402 Payment Required** today, and `research_media_edison.py` hits the
    same API, so both Edison routes are billing-blocked. `claude_code` works and is the
    recommended default.
  * `deep-research-client` ships no Codex provider (ten provider modules, none of them
    codex) and has **no entry-point mechanism** for external ones — only an internal
    `register()`. Adding one means upstreaming to DRC or forking it; editing the installed
    package would be silently undone by the next `uv sync`.

So Codex is driven directly here, the same way `research_media_edison.py` drives the
Edison SDK directly rather than through DRC.

## What Codex is and is not good for

Depth is prompt-bound, not tool-bound, and it is worth recording how that was learned. A
bare one-line question gave:

    claude_code   295s   20,876 chars   22 sources
    codex exec     26s      901 chars    3 sources

which read like "Codex is fast but shallow". Run through the real research template, the
same tool gave **10,813 chars and 27 distinct sources in 7m19s** -- comparable depth. The
first comparison measured my prompt, not Codex.

On that first templated run it also found a defect nobody was looking for: `lb_broth.yaml`
claimed `kg_microbe_match: mediadive.medium:74`, and MediaDive 74 is THERMUS THERMOPHILUS
MEDIUM. Verified against the API, and 7 of 8 sampled records turned out to have the same
problem (#286).

The `--min-sources` gate exists because a thin run should announce itself: a report citing
one URL has not researched anything, and must not look like a result.

Requires `codex` on PATH and `web_search` enabled in `~/.codex/config.toml`; both are
checked before anything runs.

Usage::

    just research-media-codex lb_broth
    just research-media-codex lb_broth --dry-run
    just research-media-codex lb_broth --min-sources 5
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from research_media import (  # noqa: E402
    DEFAULT_RESEARCH_DIR, DEFAULT_TEMPLATE, load_media, resolve_media_file, template_vars,
)

CODEX_CONFIG = Path.home() / ".codex" / "config.toml"
URL = re.compile(r"https?://[^\s)\]>,]+")

PREAMBLE = (
    "Research the growth medium described below. Use web search — do not answer from "
    "memory alone. Reply in markdown: a short direct answer first, then supporting "
    "detail, then a numbered list of every URL you consulted. Where a claim rests on a "
    "specific source, cite it inline. If the sources disagree, say so rather than "
    "picking one.\n\n"
)


def preflight() -> list[str]:
    """Reasons Codex cannot be used right now. Empty means go.

    Checked up front because both failure modes are quiet otherwise: a missing binary
    surfaces as a confusing subprocess error, and web search being off produces a
    confident answer with no sources, which reads like a result.
    """
    problems: list[str] = []
    if shutil.which("codex") is None:
        problems.append("`codex` is not on PATH — install the Codex CLI")
    if CODEX_CONFIG.is_file():
        try:
            cfg = tomllib.loads(CODEX_CONFIG.read_text())
        except tomllib.TOMLDecodeError:
            cfg = {}
        if str(cfg.get("web_search", "")).lower() not in {"live", "true", "on"}:
            problems.append(
                f"`web_search` is not enabled in {CODEX_CONFIG} — Codex would answer "
                "from memory and cite nothing")
    else:
        problems.append(f"{CODEX_CONFIG} not found — cannot confirm web search is on")
    return problems


def build_prompt(doc: dict, media_file: Path, template: Path) -> str:
    """The research prompt: the shared media template, filled, behind a Codex preamble."""
    body = template.read_text()
    variables = template_vars(doc, media_file)
    # Single-brace placeholders, matching the shared template that `research_media.py`
    # hands to deep-research-client via --var. Substituting `{{key}}` filled nothing and
    # shipped the raw template as the prompt — caught by --dry-run.
    for key, value in variables.items():
        body = body.replace("{" + key + "}", value)
    missing = sorted(set(re.findall(r"\{([a-z_]+)\}", body)) - set(variables))
    if missing:
        raise ValueError(
            f"template placeholders not filled: {missing}. research_media.template_vars "
            "no longer covers this template — fix rather than send a prompt with holes.")
    return PREAMBLE + body


def run_codex(prompt: str, out_file: Path, timeout: int) -> tuple[int, str]:
    out_file.parent.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(
        ["codex", "exec", "--output-last-message", str(out_file), prompt],
        capture_output=True, text=True, timeout=timeout)
    return proc.returncode, (proc.stderr or "")[-800:]


def source_count(text: str) -> int:
    return len({u.rstrip(".,);") for u in URL.findall(text or "")})


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--target", required=True, help="Media YAML path, slug, ID, or name")
    ap.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    ap.add_argument("--research-dir", type=Path, default=DEFAULT_RESEARCH_DIR)
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--min-sources", type=int, default=3,
                    help="Fail if the report cites fewer distinct URLs than this. A run "
                         "that found nothing should not look like a result.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print the prompt and destination without calling Codex.")
    args = ap.parse_args(argv)

    problems = preflight()
    if problems and not args.dry_run:
        for p in problems:
            print(f"  BLOCKED: {p}", file=sys.stderr)
        return 2

    media_file = resolve_media_file(args.target)
    doc = load_media(media_file)
    prompt = build_prompt(doc, media_file, args.template)

    slug = media_file.stem
    out_dir = args.research_dir / "media" / media_file.parent.name
    out_file = out_dir / f"{slug}-deep-research-codex.md"

    if args.dry_run:
        print(f"target:  {media_file.relative_to(REPO_ROOT)}")
        print(f"output:  {out_file.relative_to(REPO_ROOT)}")
        for p in problems:
            print(f"WOULD BLOCK: {p}")
        print(f"--- prompt ({len(prompt)} chars) ---\n{prompt[:600]}...")
        return 0

    code, err = run_codex(prompt, out_file, args.timeout)
    if code != 0:
        print(f"codex exec failed (exit {code}):\n{err}", file=sys.stderr)
        return 1
    if not out_file.exists() or not out_file.stat().st_size:
        print(f"codex exec reported success but wrote nothing to {out_file}",
              file=sys.stderr)
        return 1

    text = out_file.read_text()
    n = source_count(text)
    print(f"Wrote {out_file.relative_to(REPO_ROOT)} — {len(text)} chars, {n} distinct source(s).")
    if n < args.min_sources:
        print(f"  WARNING: only {n} source(s), below --min-sources {args.min_sources}. "
              f"Treat this as a lead, not evidence; `claude_code` cites far more "
              f"(22 vs 3 on the same query).", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
