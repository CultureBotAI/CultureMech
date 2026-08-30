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

Requires an authenticated `codex` CLI whose help advertises native web search and
schema-constrained output; the fleet canary checks both without starting a research run.

Usage::

    just research-media-codex lb_broth
    just research-media-codex lb_broth --dry-run
    just research-media-codex lb_broth --min-sources 5
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from deep_research_contract import (  # noqa: E402
    ContractError,
    codex_canary,
    render_prompt_template,
    run_codex_research,
)
from research_media import (  # noqa: E402
    DEFAULT_RESEARCH_DIR,
    DEFAULT_TEMPLATE,
    load_media,
    resolve_media_file,
    template_vars,
)

URL = re.compile(r"https?://[^\s)\]>,]+")

PREAMBLE = (
    "Research the growth medium described below. Use web search — do not answer from "
    "memory alone. Reply in markdown: a short direct answer first, then supporting "
    "detail, then a numbered list of every URL you consulted. Where a claim rests on a "
    "specific source, cite it inline. If the sources disagree, say so rather than "
    "picking one.\n\n"
)


def preflight() -> list[str]:
    """Reasons the canonical Codex canary cannot be used right now."""
    result = codex_canary()
    return [] if result.ok else [result.detail]


def build_prompt(doc: dict, media_file: Path, template: Path) -> str:
    """The research prompt: the shared media template, filled, behind a Codex preamble."""
    variables = template_vars(doc, media_file)
    # Single-brace placeholders, matching the shared template that `research_media.py`
    # hands to deep-research-client via --var. Substituting `{{key}}` filled nothing and
    # shipped the raw template as the prompt — caught by --dry-run.
    try:
        body = render_prompt_template(template, variables)
    except ContractError as exc:
        raise ValueError(
            f"{exc}. research_media.template_vars no longer covers this template — "
            "fix rather than send a prompt with holes."
        ) from exc
    return PREAMBLE + body


def source_count(text: str) -> int:
    return len({u.rstrip(".,);") for u in URL.findall(text or "")})


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--target", required=True, help="Media YAML path, slug, ID, or name")
    ap.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    ap.add_argument("--research-dir", type=Path, default=DEFAULT_RESEARCH_DIR)
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument(
        "--min-chars",
        type=int,
        default=1000,
        help="Fail without replacing any prior report if the answer is shorter.",
    )
    ap.add_argument(
        "--min-sources",
        type=int,
        default=3,
        help="Fail if the report cites fewer distinct URLs than this. A run "
        "that found nothing should not look like a result.",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the prompt and destination without calling Codex.",
    )
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

    try:
        summary = run_codex_research(
            prompt,
            out_file,
            repo_root=REPO_ROOT,
            timeout=args.timeout,
            min_chars=args.min_chars,
            min_sources=args.min_sources,
        )
    except ContractError as exc:
        print(f"Codex research rejected: {exc}", file=sys.stderr)
        return 1
    print(
        f"Wrote {out_file.relative_to(REPO_ROOT)} — {summary.characters} chars, "
        f"{summary.sources} distinct source(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
