"""Render a CultureMech deep-research template for one medium and print it.

Render-only: this does NOT call Edison or any external API. It resolves a
medium target, fills the template vars (including the cross-record variant
set via ``{variant_records}``), and writes the filled prompt to stdout (or
``--out``). Use it to run media recipe validation *natively in Claude Code*
— render the prompt, then research it with the harness's own web tools
instead of spending Edison credits.

Examples:
    # validate one medium + its variants, print prompt to stdout
    python scripts/render_media_prompt.py --target 1_10_r2a_medium

    # use a different template, write to a file
    python scripts/render_media_prompt.py --target lb_broth \
        --template templates/media_growth_research.md --out prompt.md
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import research_media as rm  # noqa: E402 -- reuse resolver + template_vars

DEFAULT_TEMPLATE = Path("templates/media_recipe_validation.md")


class _DefaultEmpty(dict):
    """``str.format_map`` helper: leave unknown placeholders blank instead of KeyError."""

    def __missing__(self, key):  # noqa: ANN001
        return ""


def render_query(media_path: Path, template_path: Path) -> str:
    """Fill ``template_path`` with the media record's template vars. No external calls."""
    doc = rm.load_media(media_path)
    variables = rm.template_vars(doc, media_path)
    return template_path.read_text().format_map(_DefaultEmpty(variables))


def parse_args(argv: list[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--target", required=True, help="Media YAML path, slug, ID, name, or original name.")
    ap.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE,
                    help=f"Template to render (default: {DEFAULT_TEMPLATE}).")
    ap.add_argument("--out", type=Path, help="Write prompt here instead of stdout.")
    return ap.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    media_file = rm.resolve_media_file(args.target)
    prompt = render_query(media_file, args.template)
    if args.out:
        args.out.write_text(prompt)
        print(f"Wrote rendered prompt for {media_file} -> {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(prompt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
