# Unmapped ingredient occurrence guide

## Purpose

CultureMech classifies ingredient occurrences through the pinned
MediaIngredientMech (MIM) label resolver. An occurrence is unmapped when the
resolver returns no `resolved_identifier`; it is not classified from the mere
presence or absence of a colon in a local field.

The canonical artifact is a complete direct-occurrence TSV. The mapped and
unmapped YAML files are deterministic summaries of that same row population,
not independent scans.

## Direct-root traversal

The extractor selects exactly one component field from each normalized root
record according to its schema shape:

- MediaRecipe-shaped roots contribute `ingredients`.
- SolutionRecipe-shaped roots contribute `composition`.

These fields are alternatives. They are never concatenated. Consequently,
`See source for composition` entries retained in a SolutionRecipe's legacy
`ingredients` field are not ingredients, and nested
`solutions[].composition` entries are not expanded once per referencing
medium. The artifact represents direct root containment only.

Each occurrence is identified by the stable tuple:

```text
(recipe_id, component_field, component_index)
```

`recipe_id` is the root `CultureMech:NNNNNN` identifier. `component_field` is
`ingredients` or `composition`, and `component_index` is zero-based. Recipe
labels are display metadata; duplicate labels never merge distinct recipes.
`source_path` is a POSIX path relative to `--input-dir`, keeping custom corpus
scans portable and byte-identical across worktrees.

For display, the extractor uses a root `preferred_term` when present and falls
back to `name` only for MediaRecipe-shaped legacy records. It never falls back
to a filename stem. The canonical TSV records that choice in `label_source` as
`preferred_term` or `legacy_name`.

## Resolver partition

The occurrence pipeline imports the same `GroundingDecision` resolver used by
KGX:

- Resolved: `mim_exact`, `mim_normalized`, `local_fallback`, and
  `ambiguous_local_fallback` have a non-empty `resolved_identifier` and enter
  the mapped summary.
- Unresolved: `authoritative_unmapped`, `ambiguous`, and `not_found` have no
  selected identifier and enter the unmapped summary.

An explicit MIM `UNMAPPED` decision suppresses a conflicting local grounding.
An unsafe ambiguity may retain a local identity only through the visibly named
`ambiguous_local_fallback` result.

MediaDive compound IDs are provenance, not ontology mappings. They remain in
`source_compound_id` even when the same component has a CHEBI `chebi_term` or a
MIM-selected identity. The TSV also retains `local_identifier`, MIM match type,
mapping status, ambiguity, diagnostic ontology ID, and `grounding_reason`.

See [MediaIngredientMech ingredient identity resolution](mediaingredientmech_enrichment.md)
for the pinned artifact and matching rules.

## Generated artifacts

Run:

```bash
just aggregate-all-ingredients
```

The command invokes `scripts/aggregate_ingredients.py` once and writes:

- `output/ingredient_occurrences.tsv` — complete mapped and unmapped direct
  occurrences, with no row cap.
- `output/mapped_ingredients.yaml` — identity-first mapped summary.
- `output/unmapped_ingredients.yaml` — unresolved label summary.
- `output/ingredient_aggregation_errors.tsv` — machine-readable input failures.

The standalone mapped and unmapped commands use the same shared scanner; they
do not maintain separate traversal or grounding rules.

`--min-occurrences` filters only summary groups in the compatibility YAML
views. It never removes rows from `ingredient_occurrences.tsv`.

`output/` is a generated-data directory. Do not hand-edit or commit these
artifacts.

## Count definitions

For each summary row:

- `occurrence_count` is the number of complete TSV rows in the group.
- `distinct_recipe_count` is the number of unique `recipe_id` values in those
  rows.
- `recipe_occurrences` is complete and uncapped.

Collection `recipe_count` and category `recipes_with_mapped` /
`recipes_with_unmapped` values likewise use stable recipe IDs. Counts are never
derived from display labels or a retained sample. Repeated positions for the
same ingredient in one recipe increase `occurrence_count` but increase
`distinct_recipe_count` only once.

## Unmapped summary shape

The standalone schema is
`src/culturemech/schema/unmapped_ingredients_schema.yaml`. A summary entry keeps
the source query label and the full resolver provenance:

```yaml
total_unmapped_count: 1
total_instances: 2
recipe_count: 2
unmapped_ingredients:
- preferred_term: Calf brains
  occurrence_count: 2
  distinct_recipe_count: 2
  mapping_status: UNMAPPED
  recipe_occurrences:
  - recipe_id: CultureMech:000021
    recipe_label: Example medium A
    recipe_category: BACTERIAL
    source_path: bacterial/example_a.yaml
    component_field: ingredients
    component_index: 4
    preferred_term: Calf brains
    local_identifier: UBERON:0000955
    resolution_source: authoritative_unmapped
    mim_mapping_status: UNMAPPED
    grounding_reason: MIM explicitly leaves this label unmapped; local grounding suppressed
  - recipe_id: CultureMech:000022
    recipe_label: Example medium B
    recipe_category: BACTERIAL
    source_path: bacterial/example_b.yaml
    component_field: ingredients
    component_index: 2
    preferred_term: Calf brains
    local_identifier: UBERON:0000955
    resolution_source: authoritative_unmapped
    mim_mapping_status: UNMAPPED
    grounding_reason: MIM explicitly leaves this label unmapped; local grounding suppressed
```

There is deliberately no wall-clock `generation_date`. Input paths and stable
coordinates are sorted, TSV files use LF line endings, and reruns over identical
recipes plus the same pinned MIM index are byte-identical.

## Failure and publication semantics

YAML parse failures and extraction-blocking schema/shape failures are written
to `output/ingredient_aggregation_errors.tsv` whether or not `--verbose` is
enabled. `--verbose` controls progress messages only.

If a fatal error occurs, the command exits nonzero. The error report is updated,
but the occurrence and summary files are not partially replaced. Successful
outputs are staged as one publication set only after the complete scan and all
consistency checks pass. Each destination is atomically replaced; an in-process
failure on a later replacement rolls earlier members back to their prior files.

## Curation workflow

Use the unmapped summary to prioritize labels, but fix identity authority in the
appropriate layer:

1. If the recipe label itself is missing or demonstrably wrong, correct the
   source recipe through the normal CultureMech curation workflow.
2. If the label is source-faithful but lacks an identity, curate or mint the
   record in MIM and refresh CultureMech's pinned label index explicitly.
3. Do not insert a guessed CURIE into recipe YAML merely to make the mapped count
   increase.
4. Rerun `just aggregate-all-ingredients` and review the semantic diff.

The generated summaries never rewrite curated recipe data.
