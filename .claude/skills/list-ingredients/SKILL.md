---
name: list-ingredients
description: "Produce the corpus-wide list of distinct ingredients across all CultureMech normalized recipe records, with identifiers, mapping status, and occurrence/recipe counts. Use when asked for a list, inventory, or table of all ingredients, the most common ingredients, or which ingredients are unmapped. Read-only over recipe data; not for grounding fixes or record edits."
allowed-tools: Bash, Read
metadata:
  category: reporting
  requires_database: false
  requires_internet: false
  version: 1.0.0
---

# List ingredients across the corpus

## Command

```bash
just aggregate-all-ingredients
```

This runs `scripts/aggregate_ingredients.py`, which scans
`data/normalized_yaml/` once and resolves each direct ingredient through the
pinned MediaIngredientMech label index. A full run takes several minutes.

## Outputs (`output/`, generated and gitignored — never commit or hand-edit)

| File | Content |
| --- | --- |
| `ingredients_list.tsv` | **The list.** One row per distinct ingredient, sorted by distinct recipe count. |
| `ingredient_occurrences.tsv` | Canonical table: one row per ingredient per record, uncapped. |
| `mapped_ingredients.yaml` / `unmapped_ingredients.yaml` | Summary views that embed every occurrence (large). |
| `ingredient_aggregation_errors.tsv` | Input failures. A non-empty report means nothing else was replaced. |

`ingredients_list.tsv` columns: `preferred_term`, `resolved_identifier`,
`identifier_prefix`, `mapping_status` (`MAPPED`, `UNMAPPED`, `AMBIGUOUS`),
`occurrence_count`, `distinct_recipe_count`, `label_variant_count`,
`label_variants`, `resolution_sources`, `recipe_categories`. Multi-valued cells
are joined with ` | `.

## Interpreting the list

- Mapped rows group by resolved identifier; unmapped rows group by exact source
  label (plus resolution source), so spelling variants of one unmapped material
  are separate rows.
- Blank labels are kept as `blank:<recipe_id>:<field>:<index>` rows.
- The list counts direct `ingredients` (media) or `composition` (solutions)
  entries only; ingredients inside referenced stock solutions are not expanded.
- The list is never filtered by `--min-occurrences`. Its row count equals
  `total_mapped_count + total_unmapped_count` from the YAML views at the default
  `min_occurrences=1`.

## Verification

- Confirm `ingredient_aggregation_errors.tsv` has only a header row.
- Report counts from this run, with the commit, rather than from a prior run;
  the corpus changes continuously. See `docs/unmapped_ingredients_guide.md`.
