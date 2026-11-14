---
name: list-ingredients
description: "Compile CultureMech's catalog-wide structured ingredient inventory and reproducible source bundle for a MIM/KG-Microbe handoff. Use for ingredient lists, unmapped inventories, coverage/currentness checks, or preparing an integrated mapping release. Preserves recipe data and unresolved identities; does not publish mappings or infer ingredients from prose."
allowed-tools: Bash, Read
metadata:
  category: reporting
  requires_database: false
  requires_internet: false
  version: 1.2.0
---

# List ingredients across the corpus

## Command

```bash
just aggregate-all-ingredients
```

This runs `scripts/aggregate_ingredients.py`, which scans
`data/normalized_yaml/` once and resolves each direct ingredient through the
pinned MediaIngredientMech label index. A full run takes several minutes.

## Reproducible MIM / KG-Microbe handoff

For a release candidate or a claim that an existing list is current, use the
bundle wrapper rather than relying on output timestamps. Read
[the integrated release guide](../../../docs/ingredient_release.md) for the
producer/consumer boundaries and exact scope.

```bash
just plan-ingredient-release
just build-ingredient-release output/ingredient-release-candidate
just verify-ingredient-release output/ingredient-release-candidate
```

Use a new destination for each attempt. The wrapper reuses the native scanner,
preserves the ordinary `output/` files, records input membership/content and
code/schema/MIM-index hashes, and verifies output hashes and row accounting.
A missing or changed input invalidates the bundle. A manifest is reproducibility
evidence, not scientific review or permission to install a mapping release.
For downstream intake, run `just verify-ingredient-handoff BUNDLE SHA256` using
the manifest digest independently recorded in the reviewed producer handoff.
The ordinary verifier checks local consistency; it cannot authenticate a
manifest supplied alongside the same untrusted products.

Before a first full run with changed code, use one actual recipe in an isolated
input directory through the same `build`/`verify` CLI. Report it as a subset
canary; then run the default full-catalog input. Do not substitute a category
scan or previously generated YAML summary for the authoritative corpus.

Keep the current MIM campaign's frozen inputs intact. Hand off the new bundle's
manifest digest and source scope for explicit adoption. The bundled MIM label
index and the new MIM SSSOM are different versioned products; do not refresh the
index implicitly or call a candidate a released KGM input.

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
  among occurrences MIM resolved directly (`mim_exact`/`mim_normalized`),
  preferring terms MIM marks `MAPPED` over its `REJECTED` ones; ties break by
  code point (uppercase first). Without directly resolved occurrences it is the
  most frequent source label.
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
  entries, plus the `composition` of stocks written inline in a record's
  `solutions[]` (#604). Ingredients inside referenced stock solutions are not
  expanded; the referenced record counts them once.
- Separately modeled variant recipe records are included. Ingredient mentions
  only in `variants[].modifications`, notes, or other prose are not extracted.
  Say **all structured direct ingredients across the catalog**, not all chemical
  mentions or every medium's fully expanded formulation. Preserve prose-only
  additions as a curation gap; do not guess their identities.
- The list is never filtered by `--min-occurrences`. Its row count equals
  `total_mapped_count + total_unmapped_count` from the YAML views at the default
  `min_occurrences=1`.

## Verification

- `just aggregate-mapped-ingredients` and `just aggregate-unmapped-ingredients`
  also refresh the list together with `ingredient_occurrences.tsv`. Without
  `--list-output`, every command writes the list beside `--occurrences-output`;
  `aggregate-all-ingredients` is the one command that refreshes every output.
- Confirm `ingredient_aggregation_errors.tsv` has only a header row.
- Report counts from this run, with the commit, rather than from a prior run;
  the corpus changes continuously. See `docs/unmapped_ingredients_guide.md`.
