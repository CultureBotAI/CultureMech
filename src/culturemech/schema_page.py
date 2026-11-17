"""Generate app/schema.html from the CultureMech LinkML schema."""

from __future__ import annotations

import html
import shutil
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = Path(__file__).resolve().parent / "schema" / "culturemech.yaml"
DEFAULT_OUT = REPO_ROOT / "app" / "schema.html"


def _esc(val: Any) -> str:
    return html.escape(str(val or ""))


def render_schema_html(schema_path: Path = SCHEMA_PATH, out_path: Path = DEFAULT_OUT) -> Path:
    data = yaml.safe_load(schema_path.read_text(encoding="utf-8")) or {}
    schema_id = data.get("id", "https://w3id.org/culturemech")
    title = data.get("title", "CultureMech — LinkML Schema")
    description = (data.get("description") or "").strip()
    license_name = data.get("license", "BSD-3-Clause")

    classes: dict[str, dict[str, Any]] = data.get("classes") or {}
    enums: dict[str, dict[str, Any]] = data.get("enums") or {}

    class_cards: list[str] = []
    for cls_name, cls_def in classes.items():
        if not isinstance(cls_def, dict):
            continue
        cls_desc = _esc((cls_def.get("description") or "").strip())
        attrs = cls_def.get("attributes") or {}
        rows: list[str] = []
        for slot_name, slot_def in attrs.items():
            if not isinstance(slot_def, dict):
                continue
            rng = _esc(slot_def.get("range") or "string")
            mult = "list" if slot_def.get("multivalued") else "single"
            req = (
                "required"
                if slot_def.get("required")
                else ("recommended" if slot_def.get("recommended") else "optional")
            )
            sdesc = _esc((slot_def.get("description") or "").strip())
            rows.append(
                f"<tr>"
                f"<td><code>{_esc(slot_name)}</code></td>"
                f"<td><code>{rng}</code></td>"
                f"<td>{mult}</td>"
                f"<td>{req}</td>"
                f"<td>{sdesc}</td>"
                f"</tr>"
            )
        table_html = (
            '<table class="schema-table">'
            "<thead><tr><th>Attribute</th><th>Range</th><th>Cardinality</th><th>Status</th><th>Description</th></tr></thead>"
            f"<tbody>{''.join(rows)}</tbody></table>"
            if rows
            else '<p class="muted">No inline attributes.</p>'
        )
        class_cards.append(
            f'<section class="schema-card" data-kind="class" data-name="{_esc(cls_name.lower())}">'
            f"<h3><code>{_esc(cls_name)}</code></h3>"
            f"<p>{cls_desc}</p>"
            f"{table_html}"
            f"</section>"
        )

    enum_cards: list[str] = []
    for enum_name, enum_def in enums.items():
        if not isinstance(enum_def, dict):
            continue
        edesc = _esc((enum_def.get("description") or "").strip())
        pvs = enum_def.get("permissible_values") or {}
        rows = []
        for pv_name, pv_def in pvs.items():
            pv_def = pv_def if isinstance(pv_def, dict) else {}
            meaning = _esc(pv_def.get("meaning") or "")
            pdesc = _esc((pv_def.get("description") or "").strip())
            rows.append(
                f"<tr><td><code>{_esc(pv_name)}</code></td><td><code>{meaning}</code></td><td>{pdesc}</td></tr>"
            )
        table_html = (
            '<table class="schema-table">'
            "<thead><tr><th>Permissible Value</th><th>Meaning / Term</th><th>Description</th></tr></thead>"
            f"<tbody>{''.join(rows)}</tbody></table>"
            if rows
            else '<p class="muted">No permissible values listed.</p>'
        )
        enum_cards.append(
            f'<section class="schema-card" data-kind="enum" data-name="{_esc(enum_name.lower())}">'
            f"<h3><code>{_esc(enum_name)}</code></h3>"
            f"<p>{edesc}</p>"
            f"{table_html}"
            f"</section>"
        )

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{_esc(title)} — CultureMech</title>
  <style>
    :root {{
      --pastel-a: #FFE0B5;
      --pastel-b: #CDEBC5;
      --accent: #4B9E5F;
      --ink: #1a1a1a;
      --muted: #555;
      --card: #ffffff;
      --line: rgba(0,0,0,.12);
    }}
    :root[data-theme="dark"] {{
      --pastel-a: #24331d;
      --pastel-b: #12160f;
      --accent: #6cc47f;
      --ink: #eaf0e6;
      --muted: #9db09a;
      --card: #1c2118;
      --line: #2e3a2c;
    }}
    @media (prefers-color-scheme: dark) {{
      :root:not([data-theme="light"]) {{
        --pastel-a: #24331d;
        --pastel-b: #12160f;
        --accent: #6cc47f;
        --ink: #eaf0e6;
        --muted: #9db09a;
        --card: #1c2118;
        --line: #2e3a2c;
      }}
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--pastel-b);
      color: var(--ink);
      line-height: 1.55;
    }}
    a {{ color: var(--accent); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .header {{
      background: linear-gradient(135deg, var(--pastel-a), var(--pastel-b));
      padding: 2.25rem 1.5rem;
      border-bottom: 1px solid var(--line);
      text-align: center;
    }}
    .header h1 {{ margin: 0 0 0.35rem; font-size: 2rem; }}
    .header p {{ margin: 0 auto; max-width: 760px; color: var(--muted); }}
    .header-nav {{
      margin-top: 1rem;
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.5rem;
    }}
    .header-nav a {{
      color: var(--ink);
      font-size: 0.85rem;
      font-weight: 600;
      padding: 0.35rem 0.8rem;
      border-radius: 999px;
      background: rgba(255,255,255,.55);
      border: 1px solid var(--line);
    }}
    :root[data-theme="dark"] .header-nav a {{ background: rgba(255,255,255,.08); }}
    .wrap {{ max-width: 1200px; margin: 0 auto; padding: 2rem 1.5rem; }}
    .toolbar {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 1rem 1.25rem;
      margin-bottom: 1.5rem;
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      align-items: center;
      justify-content: space-between;
    }}
    .toolbar input {{
      flex: 1 1 280px;
      padding: 0.55rem 0.85rem;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--card);
      color: var(--ink);
      font-size: 0.95rem;
    }}
    .schema-card {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 1.25rem 1.5rem;
      margin-bottom: 1.25rem;
      overflow-x: auto;
    }}
    .schema-card h3 {{ margin: 0 0 0.35rem; font-size: 1.2rem; color: var(--accent); }}
    .schema-table {{ width: 100%; border-collapse: collapse; font-size: 0.88rem; margin-top: 0.75rem; }}
    .schema-table th, .schema-table td {{
      border: 1px solid var(--line);
      padding: 0.45rem 0.65rem;
      text-align: left;
      vertical-align: top;
    }}
    .schema-table th {{ background: rgba(0,0,0,.04); font-weight: 600; }}
    footer {{
      border-top: 1px solid var(--line);
      padding: 1.5rem;
      text-align: center;
      font-size: 0.88rem;
      color: var(--muted);
    }}
  </style>
</head>
<body>
  <header class="header">
    <h1>{_esc(title)}</h1>
    <p>{_esc(description)}</p>
    <p style="margin-top:0.35rem;font-size:0.85rem;">Schema URI: <code>{_esc(schema_id)}</code> &middot; License: {_esc(license_name)} &middot; <a href="culturemech.yaml" download="culturemech.yaml">Download LinkML YAML &darr;</a></p>
    <nav class="header-nav" aria-label="Primary navigation">
      <a href="index.html">Home</a>
      <a href="browser.html">Browse Recipes</a>
      <a href="text_map.html">Text Map</a>
      <a href="umap.html">Media PaCMAP</a>
      <a href="umap_graph.html">Media Graph</a>
      <a href="ingredient_umap.html">Ingredient PaCMAP</a>
      <a href="schema.html" aria-current="page">Schema</a>
      <a href="https://culturebotai.github.io/mechs/">All Mech projects &nearr;</a>
    </nav>
  </header>
  <main class="wrap">
    <div class="toolbar">
      <input type="search" id="schemaFilter" placeholder="Filter classes, slots, or enums..." aria-label="Filter schema elements">
      <div>
        <strong>{len(class_cards)}</strong> classes &middot; <strong>{len(enum_cards)}</strong> enums &middot;
        <a href="recipes.json" download="culturemech_recipes.json">Download JSON</a> &middot;
        <a href="recipes.tsv" download="culturemech_recipes.tsv">Download TSV</a>
      </div>
    </div>
    <h2>Classes ({len(class_cards)})</h2>
    <div id="classContainer">
      {''.join(class_cards)}
    </div>
    <h2>Enumerations ({len(enum_cards)})</h2>
    <div id="enumContainer">
      {''.join(enum_cards)}
    </div>
  </main>
  <footer>
    <p><strong>CultureMech</strong> &middot; <a href="index.html">Home</a> &middot; <a href="browser.html">Browse Recipes</a> &middot; <a href="culturemech.yaml" download="culturemech.yaml">LinkML YAML</a> &middot; <a href="https://github.com/CultureBotAI/CultureMech">GitHub (CultureBotAI/CultureMech)</a> &middot; {_esc(license_name)}</p>
  </footer>
  <script>
    const filterInput = document.getElementById('schemaFilter');
    filterInput.addEventListener('input', () => {{
      const q = filterInput.value.trim().toLowerCase();
      document.querySelectorAll('.schema-card').forEach(card => {{
        const match = !q || card.textContent.toLowerCase().includes(q);
        card.style.display = match ? '' : 'none';
      }});
    }});
  </script>
  <script src="theme-toggle.js"></script>
</body>
</html>
"""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(page_html, encoding="utf-8")
    shutil.copyfile(schema_path, out_path.parent / "culturemech.yaml")
    return out_path


def main() -> None:
    out = render_schema_html()
    print(f"✓ Generated {out}")


if __name__ == "__main__":
    main()
