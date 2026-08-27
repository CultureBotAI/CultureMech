---
name: generate-ingredient-umap
description: Generate an interactive UMAP scatter plot of CultureMech CHEBI ingredients in KG-Microbe embedding space — each point is one unique ingredient, sized by frequency and colored by occurrence tier
category: visualization
requires_database: false
requires_internet: false
version: 1.0.0
tags: [umap, visualization, ingredients, chebi, embeddings, kg-microbe, d3js, html]
---

# Generate Ingredient UMAP Skill

## Overview

Produces an interactive HTML visualization (`app/ingredient_umap.html`) where each point
is a unique CHEBI ingredient observed across CultureMech media, positioned in 2D using
UMAP reduction of 512-dim KG-Microbe DeepWalk embeddings.

- **Point size** — log-scale occurrence frequency across CultureMech media
- **Point color** — occurrence tier (top 100 = red, top 500 = orange, other = blue)
- **Tooltip** — ingredient name, CHEBI ID, CAS-RN, occurrence count, example media
- **Search** — filter by ingredient name or CHEBI ID
- **Zoom/pan** — mouse wheel + drag

**Run from `CultureMech/` directory.**

---

## Quick Start

```bash
# Dry-run: count CHEBI ingredients, skip embedding/UMAP (fast)
just gen-ingredient-umap-dry

# Generate full visualization (takes ~2-5 min for embedding load + UMAP)
just gen-ingredient-umap

# Force cache reload (if embeddings changed)
just gen-ingredient-umap-force-reload

# Open in browser
open app/ingredient_umap.html
```

---

## Manual / Custom Run

```bash
# Default (uses local embeddings, auto-detects unified mapping)
python scripts/generate_ingredient_umap.py

# Custom output path
python scripts/generate_ingredient_umap.py --output docs/ingredient_umap.html

# Filter to ingredients seen ≥5 times
python scripts/generate_ingredient_umap.py --min-count 5

# Custom UMAP parameters
python scripts/generate_ingredient_umap.py --n-neighbors 30 --min-dist 0.05

# Explicit embeddings path
python scripts/generate_ingredient_umap.py \
    --embeddings-path /path/to/DeepWalk...tsv.gz
```

---

## Files

| File | Description |
|------|-------------|
| `scripts/generate_ingredient_umap.py` | CLI entry point |
| `src/culturemech/visualization/ingredient_umap_generator.py` | `IngredientUMAPGenerator` class |
| `src/culturemech/templates/ingredient_umap.html` | Jinja2 + D3.js template |
| `app/ingredient_umap.html` | Generated output |
| `.umap_cache/CHEBI_embeddings.pkl` | Pickle cache (auto-created, ~800MB) |

---

## Embeddings

Auto-detected in this order:
1. `data/embeddings/DeepWalkSkipGramEnsmallen_degreenorm_embedding_512_v2_2026-05-26_00_56_15.tsv.gz` (local, preferred)
2. `../CommunityMech/CommunityMech/data/embeddings/...tsv.gz` (sibling repo fallback)

First load parses the full 1.4M-node TSV and caches CHEBI-only nodes as pickle.
Subsequent runs use the cache (fast).

---

## MIM Annotation

CAS-RN and KG-Microbe node IDs shown in tooltips come from:
```
../culturebotai-claw/workspace/unified_ingredient_mapping.tsv
```
Auto-resolved from sibling repo. If the file is absent, tooltips omit CAS-RN.

---

## Coverage Baseline (as of 2026-04-15)

| Metric | Count |
|--------|-------|
| CHEBI ingredients found in YAML files | 660 |
| Embedded (found in KG graph) | 650 (98.5%) |
| Missing embeddings | 10 (rare/new CHEBI IDs) |
| Top 100 tier | 100 |
| Top 500 tier | 400 |
| Other tier | 150 |

---

## CHEBI Extraction Priority

The generator extracts CHEBI IDs from each ingredient using this priority:

1. `term.id` starting with `CHEBI:` (native CultureMech field)
2. `chebi_term.id` starting with `CHEBI:` (enriched by MIM sync)
3. Name lookup in `data/chemical_name_to_chebi_mapping_enhanced.json` (fallback)

---

## When to Rerun

| Event | Action |
|-------|--------|
| MIM sync added new CHEBI IDs to CultureMech | `just gen-ingredient-umap` |
| New media records imported | `just gen-ingredient-umap` |
| KG-Microbe embeddings updated (new release) | `just gen-ingredient-umap-force-reload` |

---

## Related Skills

- `match-kg-microbe` — matches CultureMech media (not ingredients) to KG-Microbe nodes
- `cross-repo-sync` (culturebotai-claw) — sync MIM CHEBIs before regenerating (increases coverage)
