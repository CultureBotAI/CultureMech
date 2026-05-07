#!/usr/bin/env python3
"""Render the media growth review manifest as a GitHub Pages report."""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
from collections import Counter
from html import escape
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = REPO_ROOT / "reports" / "media_growth_review_manifest.tsv"
DEFAULT_OUTPUT = REPO_ROOT / "pages" / "media_growth_review.html"


STATUS_LABELS = {
    "applied_growth_evidence": "Applied evidence",
    "has_supported_growth_candidate": "Supported candidate",
    "has_review_candidates": "Review candidates",
    "reviewed_no_candidates": "Reviewed, no candidates",
    "not_reviewed": "Not reviewed",
}


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def to_int(row: dict[str, str], key: str) -> int:
    try:
        return int(row.get(key) or 0)
    except ValueError:
        return 0


def status_class(status: str) -> str:
    return status.replace("_", "-")


def build_report(rows: list[dict[str, str]], source_path: Path) -> str:
    total = len(rows)
    by_status = Counter(row["review_status"] for row in rows)
    by_dir = Counter(row["category_dir"] for row in rows)
    applied = sum(1 for row in rows if to_int(row, "growth_metric_count"))
    supported = sum(1 for row in rows if to_int(row, "supported_growth_evidence_count"))
    genome_ids = sum(1 for row in rows if to_int(row, "genome_id_count"))
    variants = sum(1 for row in rows if to_int(row, "variant_count"))
    reviewed = total - by_status.get("not_reviewed", 0)
    coverage = (reviewed / total * 100) if total else 0
    generated_at = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")

    status_rows = "\n".join(
        f"<tr><th>{escape(STATUS_LABELS.get(status, status))}</th>"
        f"<td>{by_status.get(status, 0):,}</td></tr>"
        for status in STATUS_LABELS
    )
    category_rows = "\n".join(
        f"<tr><th>{escape(category or 'uncategorized')}</th><td>{count:,}</td></tr>"
        for category, count in sorted(by_dir.items())
    )

    table_rows = []
    for row in rows:
        if row["review_status"] == "not_reviewed":
            continue
        display_name = row.get("original_name") or row.get("name") or row.get("id")
        table_rows.append({
            "yaml_path": row.get("yaml_path", ""),
            "category": row.get("category_dir", ""),
            "id": row.get("id", ""),
            "name": display_name,
            "status": row.get("review_status", ""),
            "growth_metrics": to_int(row, "growth_metric_count"),
            "support_evidence": to_int(row, "supported_growth_evidence_count"),
            "genome_ids": to_int(row, "genome_id_count"),
            "variants": to_int(row, "variant_count"),
            "candidates": to_int(row, "proposal_candidate_count"),
            "proposal": row.get("proposal_path", ""),
        })

    rows_json = json.dumps(table_rows, ensure_ascii=False)
    status_options = "\n".join(
        f'<option value="{escape(status)}">{escape(label)}</option>'
        for status, label in STATUS_LABELS.items()
    )
    category_options = "\n".join(
        f'<option value="{escape(category)}">{escape(category)}</option>'
        for category in sorted(by_dir)
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CultureMech Media Growth Evidence Review</title>
<style>
:root {{
  color-scheme: light;
  --ink: #182026;
  --muted: #5d6972;
  --line: #d9e0e5;
  --panel: #ffffff;
  --page: #f6f8f9;
  --accent: #276f86;
  --accent-2: #7a5a12;
  --good: #256b44;
  --warn: #9a5b00;
  --quiet: #53616b;
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  background: var(--page);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.45;
}}
a {{ color: var(--accent); }}
header {{
  background: var(--panel);
  border-bottom: 1px solid var(--line);
  padding: 28px clamp(16px, 4vw, 44px);
}}
nav {{
  display: flex;
  gap: 18px;
  flex-wrap: wrap;
  margin-bottom: 16px;
  font-size: 14px;
}}
h1 {{
  font-size: clamp(28px, 4vw, 42px);
  line-height: 1.1;
  margin: 0 0 8px;
  letter-spacing: 0;
}}
h2 {{ margin: 0 0 14px; font-size: 20px; }}
p {{ margin: 0; }}
.muted {{ color: var(--muted); }}
.wrap {{ max-width: 1260px; margin: 0 auto; padding: 24px clamp(16px, 4vw, 44px) 44px; }}
.metrics {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
  gap: 12px;
  margin-bottom: 24px;
}}
.metric {{
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 16px;
}}
.metric strong {{ display: block; font-size: 28px; line-height: 1.15; }}
.metric span {{ color: var(--muted); font-size: 13px; }}
.grid {{
  display: grid;
  grid-template-columns: minmax(260px, 1fr) minmax(260px, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}}
section {{
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 18px;
}}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{
  border-bottom: 1px solid var(--line);
  padding: 9px 8px;
  text-align: left;
  vertical-align: top;
  font-size: 14px;
}}
td.num, th.num {{ text-align: right; }}
tbody tr:last-child th, tbody tr:last-child td {{ border-bottom: 0; }}
.controls {{
  display: grid;
  grid-template-columns: minmax(240px, 1fr) 210px 180px;
  gap: 10px;
  margin-bottom: 14px;
}}
input, select {{
  width: 100%;
  border: 1px solid var(--line);
  border-radius: 6px;
  padding: 10px 11px;
  font: inherit;
  background: #fff;
  color: var(--ink);
}}
.scroll {{ overflow-x: auto; }}
.badge {{
  display: inline-block;
  border-radius: 999px;
  padding: 2px 8px;
  font-size: 12px;
  line-height: 1.45;
  border: 1px solid var(--line);
  white-space: nowrap;
}}
.applied-growth-evidence {{ color: var(--good); border-color: #8bc3a2; background: #edf8f0; }}
.has-supported-growth-candidate {{ color: var(--good); border-color: #8bc3a2; background: #edf8f0; }}
.has-review-candidates {{ color: var(--warn); border-color: #d8b46c; background: #fff7e5; }}
.reviewed-no-candidates {{ color: var(--quiet); border-color: #c4ccd2; background: #f4f6f7; }}
.not-reviewed {{ color: var(--quiet); }}
.path {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12px; overflow-wrap: anywhere; }}
.footnote {{ margin-top: 12px; font-size: 13px; color: var(--muted); }}
@media (max-width: 760px) {{
  .grid, .controls {{ grid-template-columns: 1fr; }}
}}
</style>
</head>
<body>
<header>
  <nav>
    <a href="index.html">Media index</a>
  </nav>
  <h1>CultureMech Media Growth Evidence Review</h1>
  <p class="muted">Coverage report for medium-centered growth-evidence review. Generated {escape(generated_at)} from <code>{escape(str(source_path.relative_to(REPO_ROOT)))}</code>.</p>
</header>
<main class="wrap">
  <div class="metrics">
    <div class="metric"><strong>{total:,}</strong><span>Total normalized YAML records</span></div>
    <div class="metric"><strong>{reviewed:,}</strong><span>Records covered by proposals or applied evidence ({coverage:.1f}%)</span></div>
    <div class="metric"><strong>{applied:,}</strong><span>Records with applied growth metrics</span></div>
    <div class="metric"><strong>{supported:,}</strong><span>Records with supported applied evidence</span></div>
    <div class="metric"><strong>{genome_ids:,}</strong><span>Records with genome assembly identifiers</span></div>
    <div class="metric"><strong>{variants:,}</strong><span>Records with modeled variants</span></div>
  </div>

  <div class="grid">
    <section>
      <h2>Review Status</h2>
      <table><tbody>{status_rows}</tbody></table>
    </section>
    <section>
      <h2>Records By Directory</h2>
      <table><tbody>{category_rows}</tbody></table>
    </section>
  </div>

  <section>
    <h2>Reviewed Records</h2>
    <div class="controls">
      <input id="query" type="search" placeholder="Search name, id, YAML path, or proposal path">
      <select id="status"><option value="">All statuses</option>{status_options}</select>
      <select id="category"><option value="">All directories</option>{category_options}</select>
    </div>
    <div class="scroll">
      <table>
        <thead>
          <tr>
            <th>Medium</th>
            <th>Status</th>
            <th class="num">Metrics</th>
            <th class="num">Evidence</th>
            <th class="num">Genome IDs</th>
            <th class="num">Variants</th>
            <th class="num">Candidates</th>
            <th>YAML / Proposal</th>
          </tr>
        </thead>
        <tbody id="records"></tbody>
      </table>
    </div>
    <p class="footnote"><span id="visibleCount">0</span> reviewed rows shown. This report is a coverage artifact; candidate rows still require curator judgment before YAML application.</p>
  </section>
</main>
<script>
const rows = {rows_json};
const labels = {json.dumps(STATUS_LABELS)};
const tbody = document.getElementById("records");
const visibleCount = document.getElementById("visibleCount");
const query = document.getElementById("query");
const statusFilter = document.getElementById("status");
const categoryFilter = document.getElementById("category");

function esc(value) {{
  return String(value ?? "").replace(/[&<>"']/g, ch => ({{
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }}[ch]));
}}

function statusClass(status) {{
  return status.replaceAll("_", "-");
}}

function render() {{
  const q = query.value.trim().toLowerCase();
  const selectedStatus = statusFilter.value;
  const selectedCategory = categoryFilter.value;
  const filtered = rows.filter(row => {{
    if (selectedStatus && row.status !== selectedStatus) return false;
    if (selectedCategory && row.category !== selectedCategory) return false;
    if (!q) return true;
    return [row.name, row.id, row.yaml_path, row.proposal, row.category]
      .join(" ").toLowerCase().includes(q);
  }});
  visibleCount.textContent = filtered.length.toLocaleString();
  tbody.innerHTML = filtered.map(row => `
    <tr>
      <td><strong>${{esc(row.name || row.id)}}</strong><br><span class="muted">${{esc(row.id)}} · ${{esc(row.category)}}</span></td>
      <td><span class="badge ${{statusClass(row.status)}}">${{esc(labels[row.status] || row.status)}}</span></td>
      <td class="num">${{row.growth_metrics}}</td>
      <td class="num">${{row.support_evidence}}</td>
      <td class="num">${{row.genome_ids}}</td>
      <td class="num">${{row.variants}}</td>
      <td class="num">${{row.candidates}}</td>
      <td class="path">${{esc(row.yaml_path)}}${{row.proposal ? "<br>" + esc(row.proposal) : ""}}</td>
    </tr>
  `).join("");
}}

query.addEventListener("input", render);
statusFilter.addEventListener("change", render);
categoryFilter.addEventListener("change", render);
render();
</script>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    rows = load_rows(args.manifest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build_report(rows, args.manifest))
    print(f"Wrote {args.output.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
