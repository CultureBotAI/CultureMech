---
name: list-ingredients
description: "Produce the corpus-wide list of distinct ingredients across all CultureMech normalized recipe records, with identifiers, mapping status, and occurrence/recipe counts. Use when asked for a list, inventory, or table of all ingredients, the most common ingredients, or which ingredients are unmapped. Read-only over recipe data; not for grounding fixes or record edits."
allowed-tools: Bash, Read
metadata:
  category: reporting
  requires_database: false
  requires_internet: false
  version: 1.1.0
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
are joined with ` | `; a label that itself contains ` | ` cannot be told apart
from two labels.

Read the TSVs with a CSV parser (`csv.DictReader`, pandas). Cells with quotes
are CSV-quoted, so `wc -l`, `grep`, `cut`, and `awk` can misread rows.

## Interpreting the list

- Mapped rows group by resolved identifier. Unmapped rows group by exact source
  label plus resolution source, MIM mapping status, and MIM ambiguity, so
  spelling variants of one unmapped material are separate rows.
- For mapped rows, `preferred_term` is the most frequent MIM preferred term
  among occurrences MIM resolved directly (`mim_exact`/`mim_normalized`), ties
  broken alphabetically; without such rows it is the most frequent source label.
  It can differ from every entry in `label_variants`. Identity is
  `resolved_identifier`, not the name.
- `UNMAPPED` and `MAPPED` describe occurrences, not labels. Local fallback
  depends on each descriptor, so the same label can be a variant of a MAPPED row
  and also appear as an UNMAPPED row. A MAPPED row whose `resolution_sources`
  includes `ambiguous_local_fallback` was mapped only by local fallback in some
  records (#510). Before calling a label unmapped, search `label_variants` of
  MAPPED rows for it.
- Blank or whitespace-only labels are kept as
  `blank:<recipe_id>:<field>:<index>` rows.
- The list counts direct `ingredients` (media) or `composition` (solutions)
  entries only; ingredients inside referenced stock solutions are not expanded.
- The list is never filtered by `--min-occurrences`. Its row count equals
  `total_mapped_count + total_unmapped_count` from the YAML views at the default
  `min_occurrences=1`.

## Verification

- `just aggregate-mapped-ingredients` and `just aggregate-unmapped-ingredients`
  also refresh the list together with `ingredient_occurrences.tsv`, but
  `aggregate-all-ingredients` is the one command that refreshes every output.
- Confirm `ingredient_aggregation_errors.tsv` has only a header row.
- Report counts from this run, with the commit, rather than from a prior run;
  the corpus changes continuously. See `docs/unmapped_ingredients_guide.md`.
