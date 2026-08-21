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
import os
import re
import sys
from collections.abc import Sequence
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup, escape

# Make the shared kg_microbe_browser package importable. PYTHONPATH may
# already provide it; sibling-dir fallback covers default `python -m` runs.
# parents[2] is CultureMech repo root; sibling is culturebotai-claw.
CLAW_SRC = Path(__file__).resolve().parents[2].parent / "culturebotai-claw" / "src"
if CLAW_SRC.is_dir():
    sys.path.insert(0, str(CLAW_SRC))

try:
    from kg_microbe_browser import build_ingredient_composition_graph
except ImportError:
    COMPOSITION_GRAPHS_AVAILABLE = False

    def build_ingredient_composition_graph(
        medium: dict, max_ingredients: int = 30  # type: ignore
    ) -> str:
        return ""

else:
    COMPOSITION_GRAPHS_AVAILABLE = True


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
    """Return a filesystem-safe CURIE local part or YAML stem."""
    cid = str(medium.get("id") or "")
    candidate = cid.split(":", 1)[1] if ":" in cid else source_path.stem
    slug = _SLUG_RE.sub("_", candidate).strip("._")
    return slug or "recipe"


def safe_mermaid(value: str) -> Markup:
    """Strip the ```mermaid fence from the graph builder's output and
    wrap escaped source in <pre class="mermaid"> for the Mermaid JS init.

    Graph text is derived from imported recipe data.  It must remain text: a
    closing ``</pre>`` in an ingredient label must not become page markup.
    """
    if not value:
        return Markup("")
    s = value.strip()
    if s.startswith("```mermaid"):
        s = s[len("```mermaid") :].lstrip()
    if s.endswith("```"):
        s = s[:-3].rstrip()
    return Markup('<pre class="mermaid">\n') + escape(s) + Markup("\n</pre>")


def make_env(templates_dir: Path = TEMPLATES_DIR) -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
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


def build_signature(templates_dir: Path = TEMPLATES_DIR) -> str:
    """sha256 of renderer templates/assets + this source (12 hex chars).

    Folded into the skip decision: if either the Jinja template or the renderer
    changes, the signature changes and stale pages are regenerated.
    """
    h = hashlib.sha256()
    for path in sorted(p for p in templates_dir.rglob("*") if p.is_file()):
        h.update(path.relative_to(templates_dir).as_posix().encode())
        h.update(path.read_bytes())
    h.update(Path(__file__).resolve().read_bytes())
    return h.hexdigest()[:12]


def relative_href(from_dir: Path, target: Path) -> str:
    """Return a browser-friendly relative path from a directory to a target."""
    return Path(os.path.relpath(target, start=from_dir)).as_posix()


def render_one(
    env: Environment,
    source_path: Path,
    out_dir: Path,
    index_dir: Path,
    build_sig: str,
    force: bool = False,
) -> tuple[str, dict | None, str]:
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
        index_href=relative_href(out_path.parent, index_dir / "index.html"),
        style_href=relative_href(out_path.parent, index_dir / "style.css"),
        mermaid_init_href=relative_href(out_path.parent, index_dir / "mermaid-init.js"),
    )
    out_path.write_text(html + f"\n{_SIG_MARKER.format(build_sig)}\n")
    return "rendered", medium, slug


# ---------- index page ----------


def write_index(
    env: Environment,
    index_dir: Path,
    page_dir: Path,
    all_records: list[dict],
) -> None:
    """Write an autoescaped index with links relative to its actual layout."""
    by_cat: dict[str, list[dict[str, str]]] = {}
    for r in all_records:
        cat = r["medium"].get("category") or "uncategorized"
        slug = r["slug"]
        by_cat.setdefault(cat, []).append(
            {
                "id": r["medium"].get("id") or "",
                "name": r["medium"].get("name") or slug,
                "href": relative_href(index_dir, page_dir / f"{slug}.html"),
            }
        )
    groups = [
        (category, sorted(items, key=lambda item: item["name"].lower()))
        for category, items in sorted(by_cat.items())
    ]
    html = env.get_template("index.html.j2").render(
        count=sum(len(items) for _, items in groups),
        groups=groups,
        composition_graphs_available=COMPOSITION_GRAPHS_AVAILABLE,
    )
    index_dir.mkdir(parents=True, exist_ok=True)
    (index_dir / "index.html").write_text(html)


def copy_assets(templates_dir: Path, index_dir: Path) -> None:
    """Copy renderer-owned static assets beside the generated index."""
    for name in ("style.css", "mermaid-init.js"):
        source = templates_dir / name
        if source.is_file():
            (index_dir / name).write_bytes(source.read_bytes())


def render_pages(
    *,
    yaml_dir: Path | None = None,
    source_files: Sequence[Path] | None = None,
    out_dir: Path = DEFAULT_OUT_DIR,
    index_dir: Path = DEFAULT_INDEX_DIR,
    templates_dir: Path = TEMPLATES_DIR,
    limit: int | None = None,
    force: bool = False,
) -> int:
    """Render a directory or an explicit set of recipe files.

    Returns a process-style exit code so Click, argparse, just, and tests share
    exactly the same implementation.
    """
    if source_files:
        files = [Path(path) for path in source_files]
        missing = [path for path in files if not path.is_file()]
        if missing:
            for path in missing[:5]:
                print(f"file not found: {path}", file=sys.stderr)
            return 2
    else:
        yaml_dir = Path(yaml_dir or DEFAULT_YAML_DIR)
        if not yaml_dir.is_dir():
            print(f"yaml-dir not found: {yaml_dir}", file=sys.stderr)
            return 2
        files = sorted(yaml_dir.rglob("*.yaml"))

    if limit is not None:
        files = files[:limit]

    out_dir = Path(out_dir)
    index_dir = Path(index_dir)
    templates_dir = Path(templates_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    index_dir.mkdir(parents=True, exist_ok=True)

    env = make_env(templates_dir)
    build_sig = build_signature(templates_dir)
    print(f"Rendering up to {len(files)} medium pages → {out_dir}")
    if not COMPOSITION_GRAPHS_AVAILABLE:
        print(
            "warning: culturebotai-claw is unavailable; publishing without composition graphs",
            file=sys.stderr,
        )

    rendered = skipped = errors = 0
    successful: list[dict] = []
    for path in files:
        status, medium, slug = render_one(env, path, out_dir, index_dir, build_sig, force=force)
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
    write_index(env, index_dir, out_dir, successful)
    copy_assets(templates_dir, index_dir)
    print(f"  → {index_dir / 'index.html'}")
    return 0 if errors == 0 else 1


# ---------- CLI ----------


def main(argv: Sequence[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    source = ap.add_mutually_exclusive_group()
    source.add_argument("--yaml-dir", type=Path)
    source.add_argument(
        "--file",
        dest="source_files",
        type=Path,
        action="append",
        help="render exactly this YAML file; repeat to render multiple files",
    )
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    ap.add_argument("--index-dir", type=Path, default=DEFAULT_INDEX_DIR)
    ap.add_argument("--template-dir", type=Path, default=TEMPLATES_DIR)
    ap.add_argument(
        "--limit", type=int, default=None, help="render at most N records (smoke testing)"
    )
    ap.add_argument(
        "--force", action="store_true", help="regenerate even when HTML is fresher than YAML"
    )
    args = ap.parse_args(argv)
    return render_pages(
        yaml_dir=args.yaml_dir or DEFAULT_YAML_DIR,
        source_files=args.source_files,
        out_dir=args.out_dir,
        index_dir=args.index_dir,
        templates_dir=args.template_dir,
        limit=args.limit,
        force=args.force,
    )


if __name__ == "__main__":
    sys.exit(main())
