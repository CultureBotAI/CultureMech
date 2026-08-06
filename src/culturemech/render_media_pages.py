"""Render CultureMech medium YAMLs to per-record HTML pages.

Walks `data/merge_yaml/merged/*.yaml` (configurable), applies the
Jinja2 template at `src/culturemech/templates/media.html.j2`, writes
output to `pages/media/{slug}.html`.

Idempotent: skips a record when its HTML is fresher than the source YAML AND
was built with the current template+renderer signature (a short hash embedded in
each page). Editing the Jinja template or this renderer changes the signature, so
stale pages are regenerated automatically — no --force needed. Pass --force to
regenerate everything unconditionally.

Phase 2 of the dismech-pattern port; see
../culturebotai-claw/docs/proposals/phase2_culturemech_html_pages_and_qc_dashboard.md
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup

# Make the shared kg_microbe_browser package importable. PYTHONPATH may
# already provide it; sibling-dir fallback covers default `python -m` runs.
# parents[2] is CultureMech repo root; sibling is culturebotai-claw.
CLAW_SRC = (Path(__file__).resolve().parents[2].parent
            / "culturebotai-claw" / "src")
if CLAW_SRC.is_dir():
    sys.path.insert(0, str(CLAW_SRC))

try:
    from kg_microbe_browser import build_ingredient_composition_graph
except ImportError:
    def build_ingredient_composition_graph(medium: dict,  # type: ignore
                                           max_ingredients: int = 30) -> str:
        return ""


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_YAML_DIR = REPO_ROOT / "data" / "merge_yaml" / "merged"
DEFAULT_OUT_DIR = REPO_ROOT / "pages" / "media"
DEFAULT_INDEX_DIR = REPO_ROOT / "pages"
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"

# CURIE → resolver URL templates. Anything not listed → no link.
_CURIE_RESOLVERS = {
    "CHEBI": "https://www.ebi.ac.uk/ols4/ontologies/chebi/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_{}",
    "FOODON": "https://www.ebi.ac.uk/ols4/ontologies/foodon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FFOODON_{}",
    "ENVO": "https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_{}",
    "UBERON": "https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_{}",
    "NCBITaxon": "https://www.ebi.ac.uk/ols4/ontologies/ncbitaxon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FNCBITaxon_{}",
    "NCIT": "https://www.ebi.ac.uk/ols4/ontologies/ncit/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FNCIT_{}",
    "GO": "https://www.ebi.ac.uk/ols4/ontologies/go/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_{}",
    "TOGO": "https://togomedium.org/medium/{}",
    "DSMZ": "https://mediadive.dsmz.de/medium/{}",
    "MEDIADIVE": "https://mediadive.dsmz.de/medium/{}",
}


def curie_to_url(curie: str | None) -> str:
    if not curie or ":" not in curie:
        return "#"
    prefix, local = curie.split(":", 1)
    template = _CURIE_RESOLVERS.get(prefix)
    if not template:
        return "#"
    return template.format(local)


_SLUG_RE = re.compile(r"[^A-Za-z0-9._-]+")


def slug_for(medium: dict, source_path: Path) -> str:
    """Use CURIE local part if present (CultureMech:008339 → 008339);
    otherwise the YAML stem."""
    cid = medium.get("id") or ""
    if ":" in cid:
        return cid.split(":", 1)[1]
    return _SLUG_RE.sub("_", source_path.stem)


def safe_mermaid(value: str) -> Markup:
    """Strip the ```mermaid fence from the graph builder's output and
    wrap in <pre class="mermaid"> for the Mermaid JS init."""
    if not value:
        return Markup("")
    s = value.strip()
    if s.startswith("```mermaid"):
        s = s[len("```mermaid"):].lstrip()
    if s.endswith("```"):
        s = s[:-3].rstrip()
    return Markup(f'<pre class="mermaid">\n{s}\n</pre>')


def make_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "j2"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals["curie_to_url"] = curie_to_url
    env.filters["safe_mermaid"] = safe_mermaid
    return env


# Embedded in every rendered page so a template/renderer change forces a
# re-render even when the source YAML is unchanged. The mtime-only skip below
# would otherwise silently no-op a template edit (you'd need --force).
_SIG_MARKER = "<!-- culturemech-build-sig: {} -->"


def build_signature() -> str:
    """sha256 of the page template + this renderer's source (12 hex chars).

    Folded into the skip decision: if either the Jinja template or the renderer
    changes, the signature changes and stale pages are regenerated.
    """
    h = hashlib.sha256()
    h.update((TEMPLATES_DIR / "media.html.j2").read_bytes())
    h.update(Path(__file__).resolve().read_bytes())
    return h.hexdigest()[:12]


def render_one(env: Environment, source_path: Path, out_dir: Path,
               build_sig: str, force: bool = False) -> tuple[str, dict | None, str]:
    """Returns (status, parsed_medium, slug). status is rendered/skipped/error:reason."""
    try:
        with open(source_path) as f:
            medium = yaml.safe_load(f) or {}
    except Exception as e:
        return f"error:{type(e).__name__}", None, ""
    if not isinstance(medium, dict) or not medium.get("id"):
        return "error:no-id", None, ""
    slug = slug_for(medium, source_path)
    out_path = out_dir / f"{slug}.html"
    if not force and out_path.exists():
        # Skip only when the page is fresher than its YAML AND was built with the
        # current template+renderer signature; a template/renderer edit changes
        # the signature and forces a re-render (mtime alone would miss it).
        if out_path.stat().st_mtime >= source_path.stat().st_mtime:
            try:
                fresh_build = _SIG_MARKER.format(build_sig) in out_path.read_text()
            except OSError:
                fresh_build = False
            if fresh_build:
                return "skipped", medium, slug
    template = env.get_template("media.html.j2")
    # source_path is shown in the footer; render it relative to the repo
    # root when reachable (matches index-link convention) and fall back to a
    # plain absolute string for paths the renderer was invoked on from
    # outside the repo (or via a relative path that doesn't anchor at REPO_ROOT).
    abs_source = source_path.resolve()
    try:
        src_display = str(abs_source.relative_to(REPO_ROOT))
    except ValueError:
        src_display = str(abs_source)
    html = template.render(
        medium=medium,
        composition_graph=build_ingredient_composition_graph(medium),
        source_path=src_display,
    )
    out_path.write_text(html + f"\n{_SIG_MARKER.format(build_sig)}\n")
    return "rendered", medium, slug


# ---------- index page ----------

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>CultureMech — Media index</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header>
<h1>CultureMech — Media index</h1>
<p class="muted">{count:,} media records.</p>
<p><a href="media_growth_review.html">Media growth evidence review</a></p>
</header>
{by_category}
</body>
</html>
"""


def _category_section(category: str, items: list[tuple[str, str, str]]) -> str:
    rows = "".join(
        f'<li><a href="media/{slug}.html"><code>{cid}</code></a> '
        f'<span class="muted">—</span> {name}</li>'
        for (cid, slug, name) in sorted(items, key=lambda x: x[2].lower())
    )
    return (f'<section><h2>{category} '
            f'<small class="muted">({len(items)})</small></h2>'
            f'<ul class="medium-index">{rows}</ul></section>')


def write_index(out_dir: Path, all_records: list[dict]) -> None:
    by_cat: dict[str, list[tuple[str, str, str]]] = {}
    for r in all_records:
        cat = (r["medium"].get("category") or "uncategorized")
        by_cat.setdefault(cat, []).append(
            (r["medium"].get("id") or "", r["slug"],
             r["medium"].get("name") or r["slug"]))
    sections = "\n".join(
        _category_section(cat, items)
        for cat, items in sorted(by_cat.items())
    )
    rows_total = sum(len(v) for v in by_cat.values())
    html = INDEX_TEMPLATE.format(
        count=rows_total,
        by_category=sections,
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(html)


# ---------- CLI ----------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--yaml-dir", type=Path, default=DEFAULT_YAML_DIR)
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    ap.add_argument("--index-dir", type=Path, default=DEFAULT_INDEX_DIR)
    ap.add_argument("--limit", type=int, default=None,
                    help="render at most N records (smoke testing)")
    ap.add_argument("--force", action="store_true",
                    help="regenerate even when HTML is fresher than YAML")
    args = ap.parse_args()

    if not args.yaml_dir.is_dir():
        print(f"yaml-dir not found: {args.yaml_dir}", file=sys.stderr)
        return 2
    args.out_dir.mkdir(parents=True, exist_ok=True)

    env = make_env()
    build_sig = build_signature()
    # ``rglob`` so the renderer works against both layouts: flat
    # (``data/merge_yaml/merged/*.yaml``) and category-nested
    # (``data/normalized_yaml/<category>/*.yaml``). The latter is the
    # unified raw-pages mode introduced by retiring the legacy
    # ``culturemech.render`` script.
    files = sorted(args.yaml_dir.rglob("*.yaml"))
    if args.limit:
        files = files[: args.limit]
    print(f"Rendering up to {len(files)} medium pages → {args.out_dir}")

    rendered = skipped = errors = 0
    successful: list[dict] = []
    for path in files:
        status, medium, slug = render_one(env, path, args.out_dir,
                                          build_sig, force=args.force)
        if status == "rendered":
            rendered += 1
        elif status == "skipped":
            skipped += 1
        else:
            errors += 1
            if errors <= 5:
                print(f"  {path.name}: {status}", file=sys.stderr)
        if medium and slug:
            successful.append({"medium": medium, "slug": slug})

    print(f"  rendered: {rendered}")
    print(f"  skipped:  {skipped}")
    print(f"  errors:   {errors}")

    print("Writing index...")
    write_index(args.index_dir, successful)
    print(f"  → {args.index_dir / 'index.html'}")

    # Copy stylesheet so the pages have something to look at.
    style_src = TEMPLATES_DIR / "style.css"
    if style_src.exists():
        (args.index_dir / "style.css").write_bytes(style_src.read_bytes())

    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
