"""Render CultureMech medium YAMLs to per-record HTML pages.

Walks `data/merge_yaml/merged_2026/*.yaml` (configurable), applies the
Jinja2 template at `src/culturemech/templates/media.html.j2`, writes
output to `pages/media/{slug}.html`.

Idempotent: skips records whose YAML mtime is older than the existing
HTML's mtime. Pass --force to regenerate everything.

Phase 2 of the dismech-pattern port; see
../culturebotai-claw/docs/proposals/phase2_culturemech_html_pages_and_qc_dashboard.md
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_YAML_DIR = REPO_ROOT / "data" / "merge_yaml" / "merged_2026"
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


def make_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "j2"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals["curie_to_url"] = curie_to_url
    return env


def render_one(env: Environment, source_path: Path, out_dir: Path,
               force: bool = False) -> tuple[str, dict | None, str]:
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
        if out_path.stat().st_mtime >= source_path.stat().st_mtime:
            return "skipped", medium, slug
    template = env.get_template("media.html.j2")
    html = template.render(
        medium=medium,
        source_path=str(source_path.relative_to(REPO_ROOT)),
        generated_at=_dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
    )
    out_path.write_text(html)
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
<p class="muted">{count:,} media records, generated {generated_at}.</p>
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
        generated_at=_dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
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
    files = sorted(args.yaml_dir.glob("*.yaml"))
    if args.limit:
        files = files[: args.limit]
    print(f"Rendering up to {len(files)} medium pages → {args.out_dir}")

    rendered = skipped = errors = 0
    successful: list[dict] = []
    for path in files:
        status, medium, slug = render_one(env, path, args.out_dir,
                                          force=args.force)
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
