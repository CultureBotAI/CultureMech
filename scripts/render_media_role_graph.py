"""Render a MediaRecipe (or corpus roll-up) as a mermaid role-relationship graph.

Walks a `MediaRecipe` YAML and emits a mermaid flowchart of the ingredient
↔ role relationships that landed via PRs #93 / #94 / #95 / #98 / #99, plus
the pre-existing medium ↔ solution / medium ↔ organism / organism ↔
community-role edges. Complementary to `src/culturemech/export/kgx_export.py`
(which flattens roles into a single biolink qualifier): this script keeps
each of the three facets on its own colored edge and dedupes role-value
nodes across ingredients so a curator can see recurring facet coverage.

Three modes:
  - **single**: one recipe → one .mmd (default when `--target` is given).
  - **batch**: many recipes → one .mmd per recipe (`--yaml-dir` + `--limit`).
  - **roll-up**: aggregate (ingredient, facet, role) frequencies across the
    corpus → one summary .mmd showing which faceted roles co-occur.

Node budget: capped at `--max-ingredients` (default 30, matching the
`build_ingredient_composition_graph` sentinel in the sibling
`culturebotai-claw/src/kg_microbe_browser/graph.py`). Beyond the cap the
graph emits a `...N more` sentinel node.

Output convention (invented — no prior `.mmd` files in this repo):
  reports/media_role_graphs/<slug>.mmd     (single or batch)
  reports/media_role_graphs/_rollup.mmd    (corpus roll-up)

Reference walk mirrors `src/culturemech/export/kgx_export.transform()`:
ingredients → solutions[.composition] → target_organisms → variants.
Extends beyond kgx_export.py by:
  1. Preserving each of the three facet slots as distinct edges.
  2. Emitting `role_curie` escape-hatch values.
  3. Following `target_organisms[].community_role` (renamed in #92).
  4. Following `target_organisms[].growth_metrics[].nutrient_overrides[]`
     (post-#94 range: NutritionalRoleEnum).
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable, Iterator, Optional

import yaml

logger = logging.getLogger(__name__)

FACET_SLOTS = ("nutritional_roles", "physicochemical_roles", "cellular_metabolic_roles")

# Facet display metadata — labels shown on edges + hex colors for edge styling.
FACET_STYLE = {
    "nutritional_roles":       {"label": "nut",  "color": "#2ca02c"},  # green
    "physicochemical_roles":   {"label": "phys", "color": "#1f77b4"},  # blue
    "cellular_metabolic_roles":{"label": "cell", "color": "#d62728"},  # red
}

# CHEBI id lives at any of these paths on an ingredient dict, matching the
# audit_missing_roles.py / backfill_ingredient_roles.py preference order.
CHEBI_ID_PATHS = (
    ("term", "id"),
    ("chebi_term", "id"),
    ("mediaingredientmech_chebi_term", "id"),
)


def _sanitize_id(s: str) -> str:
    """Mermaid node ids must be [A-Za-z0-9_].

    Sanitizer matches `culturebotai-claw/src/kg_microbe_browser/graph.py::_id`.
    """
    return re.sub(r"[^A-Za-z0-9_]", "_", s)


def _label(s: str, max_len: int = 70) -> str:
    """Sanitize a label for a mermaid node.

    Matches `culturebotai-claw/src/kg_microbe_browser/graph.py::_label`:
    collapse newlines, replace `"` with `'`, trim to max_len.
    """
    if s is None:
        return ""
    s = str(s).replace("\n", " ").replace('"', "'").strip()
    if len(s) > max_len:
        s = s[: max_len - 3] + "..."
    return s


def _get_nested(record: dict, path: tuple[str, ...]) -> Optional[str]:
    current: object = record
    for key in path:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current if isinstance(current, str) else None


def ingredient_chebi_id(ing: dict) -> Optional[str]:
    for path in CHEBI_ID_PATHS:
        value = _get_nested(ing, path)
        if value and value.startswith("CHEBI:"):
            return value
    return None


def ingredient_display_id(ing: dict) -> str:
    """Return a graph-node id for an ingredient. Prefers CHEBI, then any term id, then preferred_term."""
    chebi = ingredient_chebi_id(ing)
    if chebi:
        return chebi
    for path in [("term", "id"), ("chebi_term", "id"), ("mediaingredientmech_chebi_term", "id")]:
        v = _get_nested(ing, path)
        if v:
            return v
    pt = (ing.get("preferred_term") or "").strip()
    return f"ing:{pt}" if pt else "ing:unnamed"


def _emit_style(lines: list[str]) -> None:
    """Emit mermaid classDef color rules for each facet."""
    lines.append("")
    for slot, style in FACET_STYLE.items():
        lines.append(f"classDef {slot} stroke:{style['color']},stroke-width:2px,color:{style['color']}")


def _iter_recipe_ingredients(recipe: dict) -> Iterator[tuple[str, dict, str]]:
    """Yield (source, ingredient_dict, parent_id) for each ingredient in the recipe.

    `source` is one of:
      - "direct"  — ingredient sits in MediaRecipe.ingredients[]
      - "solution:<solution_id>" — ingredient sits under a SolutionDescriptor.composition[]

    `parent_id` is the graph-node id of the medium (for direct) or the
    solution (for composition).
    """
    for ing in (recipe.get("ingredients") or []):
        if isinstance(ing, dict):
            yield "direct", ing, "MEDIUM"
    for sol in (recipe.get("solutions") or []):
        if not isinstance(sol, dict):
            continue
        sol_id = _get_nested(sol, ("term", "id")) or f"sol:{(sol.get('preferred_term') or '').strip()}"
        for ing in (sol.get("composition") or []):
            if isinstance(ing, dict):
                yield f"solution:{sol_id}", ing, sol_id


def render_single_recipe(
    recipe_path: Path,
    max_ingredients: int = 30,
    include_notes: bool = False,
) -> str:
    """Render one MediaRecipe as a mermaid flowchart source string.

    Returns the .mmd source (no ```mermaid fence). Empty recipe → empty string.
    """
    try:
        doc = yaml.safe_load(recipe_path.read_text())
    except Exception as exc:
        logger.warning("failed to parse %s: %s", recipe_path, exc)
        return ""
    if not isinstance(doc, dict):
        return ""

    medium_label = (doc.get("preferred_term") or recipe_path.stem).strip()
    medium_id = _get_nested(doc, ("media_term", "term", "id")) or f"media:{recipe_path.stem}"

    lines: list[str] = ["flowchart LR"]
    lines.append(f'MEDIUM["`**{_label(medium_label)}**`"]:::medium')

    ingredients_seen = 0
    dropped_ingredient_count = 0
    ingredient_nodes: set[str] = set()
    role_value_nodes: dict[tuple[str, str], str] = {}  # (facet, value) → node_id
    solution_nodes: set[str] = set()

    # --- ingredients (direct + solution.composition) ---
    for source, ing, parent_id in _iter_recipe_ingredients(doc):
        if ingredients_seen >= max_ingredients:
            dropped_ingredient_count += 1
            continue
        ingredients_seen += 1

        ing_id = ingredient_display_id(ing)
        node_id = _sanitize_id(ing_id)
        term = (ing.get("preferred_term") or "").strip()
        label = _label(f"{term}\\n({ing_id})" if term else ing_id)

        if node_id not in ingredient_nodes:
            ingredient_nodes.add(node_id)
            lines.append(f'{node_id}["`{label}`"]:::ingredient')

        if source == "direct":
            lines.append(f"MEDIUM --> {node_id}")
        else:
            sol_id = source.split(":", 1)[1]
            sol_node = _sanitize_id(sol_id)
            if sol_node not in solution_nodes:
                solution_nodes.add(sol_node)
                lines.append(f'{sol_node}(["`{_label(sol_id)}`"]):::solution')
                lines.append(f"MEDIUM -.-> {sol_node}")
            lines.append(f"{sol_node} --> {node_id}")

        # facet role edges — one per (facet, value)
        for slot in FACET_SLOTS:
            for value in (ing.get(slot) or []):
                key = (slot, value)
                if key not in role_value_nodes:
                    role_value_nodes[key] = _sanitize_id(f"role_{slot}_{value}")
                    role_id = role_value_nodes[key]
                    facet_short = FACET_STYLE[slot]["label"]
                    lines.append(f'{role_id}(("`{value}\\n[{facet_short}]`")):::{slot}')
                role_id = role_value_nodes[key]
                lines.append(f"{node_id} --|{FACET_STYLE[slot]['label']}|--> {role_id}")

        # role_curie escape-hatch — separate node style
        for curie in (ing.get("role_curie") or []):
            key = ("role_curie", curie)
            if key not in role_value_nodes:
                role_value_nodes[key] = _sanitize_id(f"role_curie_{curie}")
                lines.append(f'{role_value_nodes[key]}(("`{curie}\\n[curie]`")):::role_curie')
            lines.append(f"{node_id} --|curie|--> {role_value_nodes[key]}")

        if include_notes and ing.get("notes"):
            note_id = f"note_{node_id}"
            lines.append(f'{note_id}["`_{_label(ing["notes"], 90)}_`"]:::note')
            lines.append(f"{node_id} -.-> {note_id}")

    if dropped_ingredient_count:
        lines.append(
            f'MORE["`...{dropped_ingredient_count} more ingredients (cap: {max_ingredients})`"]:::truncated'
        )
        lines.append(f"MEDIUM --> MORE")

    # --- target organisms ---
    for org in (doc.get("target_organisms") or []):
        if not isinstance(org, dict):
            continue
        org_id = _get_nested(org, ("term", "id")) or f"org:{(org.get('preferred_term') or '').strip()}"
        org_node = _sanitize_id(org_id)
        org_label = _label(f"{(org.get('preferred_term') or '').strip()}\\n({org_id})")
        lines.append(f'{org_node}["`{org_label}`"]:::organism')
        lines.append(f"MEDIUM ==> {org_node}")

        for value in (org.get("community_role") or []):
            key = ("community_organism_role", value)
            if key not in role_value_nodes:
                role_value_nodes[key] = _sanitize_id(f"cor_{value}")
                lines.append(f'{role_value_nodes[key]}(("`{value}\\n[org-role]`")):::community_role')
            lines.append(f"{org_node} --|community-role|--> {role_value_nodes[key]}")

        # nutrient_overrides live on growth_metrics
        for gm in (org.get("growth_metrics") or []):
            if not isinstance(gm, dict):
                continue
            for override in (gm.get("nutrient_overrides") or []):
                if not isinstance(override, dict):
                    continue
                src = (override.get("source") or "").strip()
                role = (override.get("role") or "").strip()
                sole = " (sole)" if override.get("is_sole_source") else ""
                node_id = _sanitize_id(f"override_{org_id}_{role}_{src}")
                lines.append(f'{node_id}["`{_label(src)}{sole}\\n[NutOverride: {role}]`"]:::nutrient_override')
                lines.append(f"{org_node} --|nut-override|--> {node_id}")

    _emit_style(lines)
    lines.append("classDef medium fill:#f5f5f5,stroke:#333,stroke-width:2px,font-weight:bold")
    lines.append("classDef ingredient fill:#fff,stroke:#666,color:#333")
    lines.append("classDef solution fill:#e6f2ff,stroke:#3366aa,color:#000")
    lines.append("classDef organism fill:#fff2e6,stroke:#cc6600,color:#000,font-weight:bold")
    lines.append("classDef community_role fill:#e6ffe6,stroke:#009900,color:#005500")
    lines.append("classDef nutrient_override fill:#f0e6ff,stroke:#7733aa,color:#330066")
    lines.append("classDef role_curie stroke-dasharray:5 5")
    lines.append("classDef truncated fill:#fee,stroke:#c33,color:#833")
    lines.append("classDef note fill:#fefee0,stroke:#cca,color:#663,font-style:italic")

    return "\n".join(lines) + "\n"


def render_rollup(yaml_root: Path, limit: Optional[int] = None) -> str:
    """Render a cross-corpus roll-up: which (facet, role) pairs co-occur on which CHEBI ids.

    Each edge weight = number of recipes / ingredients where that pairing appears.
    Currently near-empty because the corpus has no populated facet slots yet
    (see audit_missing_roles.py output). Included so once #128 / Step 7b
    populates the slots, this graph immediately becomes useful.
    """
    counts: Counter[tuple[str, str, str]] = Counter()  # (chebi_id, facet, value)
    ingredient_labels: dict[str, str] = {}
    files_scanned = 0
    for path in sorted(yaml_root.rglob("*.yaml")):
        if limit is not None and files_scanned >= limit:
            break
        files_scanned += 1
        try:
            doc = yaml.safe_load(path.read_text())
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue
        for _src, ing, _parent in _iter_recipe_ingredients(doc):
            chebi = ingredient_chebi_id(ing) or ""
            if not chebi:
                continue
            ingredient_labels.setdefault(chebi, (ing.get("preferred_term") or "").strip() or chebi)
            for slot in FACET_SLOTS:
                for value in (ing.get(slot) or []):
                    counts[(chebi, slot, value)] += 1

    lines = ["flowchart LR", f'HEADER["`**Corpus role roll-up**\\n{files_scanned} recipes scanned`"]:::header']

    if not counts:
        lines.append('EMPTY["`_(No faceted role assignments found yet. Run #95 backfill or Step 7b literature lane to populate.)_`"]:::empty')
        lines.append("HEADER --> EMPTY")
        lines.append("")
        lines.append("classDef header fill:#f5f5f5,stroke:#333,font-weight:bold")
        lines.append("classDef empty fill:#fee,stroke:#c33,color:#833,font-style:italic")
        return "\n".join(lines) + "\n"

    role_value_nodes: dict[tuple[str, str], str] = {}
    ing_nodes: set[str] = set()
    for (chebi, slot, value), n in counts.most_common(60):
        ing_node = _sanitize_id(chebi)
        if ing_node not in ing_nodes:
            ing_nodes.add(ing_node)
            lines.append(f'{ing_node}["`{_label(ingredient_labels[chebi])}\\n({chebi})`"]:::ingredient')
        key = (slot, value)
        if key not in role_value_nodes:
            role_value_nodes[key] = _sanitize_id(f"role_{slot}_{value}")
            facet_short = FACET_STYLE[slot]["label"]
            lines.append(f'{role_value_nodes[key]}(("`{value}\\n[{facet_short}]`")):::{slot}')
        lines.append(f"{ing_node} --|{FACET_STYLE[slot]['label']}: {n}|--> {role_value_nodes[key]}")

    _emit_style(lines)
    lines.append("classDef header fill:#f5f5f5,stroke:#333,font-weight:bold")
    lines.append("classDef ingredient fill:#fff,stroke:#666,color:#333")
    return "\n".join(lines) + "\n"


def _slug_for(path: Path) -> str:
    return path.stem


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--target", type=Path, help="Path to a single MediaRecipe YAML.")
    group.add_argument("--yaml-dir", type=Path, help="Root of the normalized-YAML corpus (for batch or roll-up).")
    parser.add_argument(
        "--mode",
        choices=("single", "batch", "rollup"),
        default=None,
        help="Explicit mode. Defaults: single if --target, batch if --yaml-dir.",
    )
    parser.add_argument("--out-dir", type=Path, default=Path("reports/media_role_graphs"),
                        help="Where to write .mmd files.")
    parser.add_argument("--max-ingredients", type=int, default=30,
                        help="Cap on ingredients per single/batch graph (default 30).")
    parser.add_argument("--limit", type=int, default=None,
                        help="Batch/rollup only: cap total recipes processed.")
    parser.add_argument("--include-notes", action="store_true",
                        help="Attach curator `notes:` free-text as dashed side-nodes on each ingredient.")
    parser.add_argument("--stdout", action="store_true",
                        help="Emit to stdout instead of writing .mmd files.")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format="%(message)s")

    if args.target is None and args.yaml_dir is None:
        parser.error("one of --target or --yaml-dir is required")

    mode = args.mode
    if mode is None:
        mode = "single" if args.target is not None else "batch"

    if mode == "single":
        if args.target is None:
            parser.error("--mode single requires --target")
        mmd = render_single_recipe(args.target, args.max_ingredients, args.include_notes)
        if args.stdout:
            print(mmd)
        else:
            args.out_dir.mkdir(parents=True, exist_ok=True)
            out = args.out_dir / f"{_slug_for(args.target)}.mmd"
            out.write_text(mmd)
            print(f"wrote {out}", file=sys.stderr)
        return 0

    if mode == "batch":
        if args.yaml_dir is None:
            parser.error("--mode batch requires --yaml-dir")
        args.out_dir.mkdir(parents=True, exist_ok=True)
        n = 0
        for path in sorted(args.yaml_dir.rglob("*.yaml")):
            if args.limit is not None and n >= args.limit:
                break
            mmd = render_single_recipe(path, args.max_ingredients, args.include_notes)
            if not mmd.strip():
                continue
            out = args.out_dir / f"{_slug_for(path)}.mmd"
            out.write_text(mmd)
            n += 1
        print(f"wrote {n} .mmd files to {args.out_dir}", file=sys.stderr)
        return 0

    if mode == "rollup":
        if args.yaml_dir is None:
            parser.error("--mode rollup requires --yaml-dir")
        mmd = render_rollup(args.yaml_dir, args.limit)
        if args.stdout:
            print(mmd)
        else:
            args.out_dir.mkdir(parents=True, exist_ok=True)
            out = args.out_dir / "_rollup.mmd"
            out.write_text(mmd)
            print(f"wrote {out}", file=sys.stderr)
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
