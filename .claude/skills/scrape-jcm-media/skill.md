---
name: scrape-jcm-media
description: Scrape growth-medium recipes directly from the RIKEN JCM GRMD database and emit CultureMech-normalized YAML records. Use to close the gap between CultureMech's JCM coverage (originally ingested second-hand via MediaDive/TOGO) and the live JCM catalogue — e.g. when newly added high-GRMD media are missing, or to audit JCM completeness.
category: ingestion
requires_database: false
requires_internet: true
version: 1.0.0
---

# Scrape JCM Media (GRMD database)

## Overview

**Purpose**: Ingest growth-medium recipes straight from the Japan Collection
of Microorganisms (JCM) Growth Medium Database (GRMD) into CultureMech.

**Why this exists.** CultureMech's ~1,300 existing JCM media were *never*
scraped from JCM directly. They arrived as derivative copies through two
aggregators:

- **MediaDive** (DSMZ) — `curator: mediadive-import`, term id
  `mediadive.medium:J<GRMD>` (~1,311 records).
- **TOGO** medium database — `curator: togo-import`, as `TOGO M####`
  records citing JCM as the original source.

Both aggregator snapshots lag the live JCM catalogue, so JCM media added
after those imports (high GRMD numbers, currently the **1333–1481** band) are
absent. This skill talks to JCM directly so the gap can be closed and kept
current.

**When to use**: a JCM completeness audit shows real media missing; JCM has
published new media; or you want to refresh a specific GRMD record from the
authoritative source rather than an aggregator mirror.

**When NOT to use**: for media already well-covered by MediaDive/TOGO (no
need to re-scrape); for non-JCM sources (use the relevant importer).

## Source & quirks

Each medium lives at:

    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=<N>

- The CGI returns **HTTP 200 for every number**. A number with no medium
  yields a tiny (~843-byte) page with no `<TABLE>`; real media render a
  `<FONT SIZE=3>` name heading + one or more bordered `component | amount |
  unit` tables, with free-text preparation notes between/after tables.
- A page is a **real medium iff it has a `<FONT SIZE=3>` name heading** — NOT
  merely if it has a `<TABLE>`. Unassigned numbers return a ~843-byte page
  with no name heading; those are natural gaps in JCM's numbering, not missing
  ingestions.
- **Derivative media**: some named media have no composition table, only a
  one-line modification of a base recipe (e.g. "Use Medium No. 1462 with
  21.0 g/L NaCl"). Because the schema requires >=1 ingredient, the importer
  inherits the base medium's table (one level), records the derivation in
  `notes`, and preserves the modification text in `preparation_steps` for a
  curator to apply. If the base is itself table-less, the record is skipped
  with a warning.
- Chemical formulae use `<sub>` tags (`Na<sub>2</sub>CO<sub>3</sub>`); the
  parser flattens these to `Na2CO3`.
- The unit is sometimes fused into the amount cell (`20g`, `980mL`) with an
  empty unit column — the parser recovers the suffix.
- Supplementary solutions ("add per liter…") appear as extra tables, often
  cross-referencing other media (`see Medium No. 1079`); these are captured
  as `ML_PER_L` ingredients with the cross-reference preserved in the name.

## Tool

`scripts/import_jcm_grmd.py`

```bash
# Auto-detect every real JCM medium absent from the corpus (authoritative)
uv run --extra dev python scripts/import_jcm_grmd.py --detect-missing --scan-max 1500 --dry-run

# Explicit GRMD numbers, preview only
uv run --extra dev python scripts/import_jcm_grmd.py --grmd 1333 1341 1462 --dry-run

# Write records under bacterial/ and validate each against MediaRecipe
uv run --extra dev python scripts/import_jcm_grmd.py --grmd 1333 1341 \
    --out-dir data/normalized_yaml/bacterial --validate
```

Flags: `--grmd N [N ...]` | `--detect-missing` (+`--scan-max`) | `--out-dir` |
`--dry-run` | `--validate` | `--delay` (politeness between requests).

## Workflow

1. **Find the gap.** Either run `--detect-missing` (re-probes JCM 1..scan-max
   and reports real media absent from `data/normalized_yaml/`), or feed an
   explicit `--grmd` list from a prior audit. Gap detection compares against
   every `GRMD=<N>` link already present in the corpus.
2. **Dry-run first.** Inspect parsed name, ingredient count, `physical_state`,
   `medium_type`, and pH for sanity. Watch for thin parses (a medium that
   legitimately uses a commercial pre-mix will have few rows + a prep note).
3. **Mint + write.** IDs are minted sequentially from `max(CultureMech:NNNNNN)
   + 1` across the corpus. Files are named `JCM_J<GRMD>_<NAME>.yaml`.
4. **Validate.** `--validate` runs `linkml-validate -C MediaRecipe` per record.
5. **Review the diff** (`git diff --stat`) before committing.

## What it captures vs. what is downstream

Captured (faithful first-pass):
- `original_name`, snake_case `name`, `ingredients` (preferred_term +
  concentration value/unit), `physical_state`, `medium_type`, `ph_value`
  (when stated), `preparation_steps`, `media_term` (`jcm.grmd:<N>`),
  provenance `notes` link, a `jcm-grmd-import` curation_history entry.

Deliberately left to existing downstream curators (do NOT duplicate here):
- **CHEBI** ingredient term mapping (`chebi-enrichment`).
- **MediaIngredientMech** links (`mediaingredientmech-enrichment`).
- **Category review**: every record is written as `bacterial` by default;
  many high-GRMD JCM media are archaea/extremophiles. Recategorization is a
  manual/curated step — the import note flags this.
- Target-organism association (the GRMD page does not list strains).

## Caveats / review checklist

- `medium_type` is a heuristic (COMPLEX if a chemically-undefined component
  like yeast extract/peptone/blood is present, else DEFINED) — verify.
- `physical_state` is SOLID_AGAR iff an `agar` component is present.
- Supplementary-solution rows are real ingredients but reference external
  recipes by JCM number; resolving those into composition is a follow-up.
- Be polite: keep `--delay` > 0 for large runs.
