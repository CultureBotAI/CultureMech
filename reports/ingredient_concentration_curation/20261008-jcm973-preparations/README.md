# JCM973 Preparation-Stage Follow-Up

Four existing normalized records are updated locally: TOGO M1023 (liquid),
TOGO M1024 (agar), MediaDive medium J973, and standalone solution 4996. This
supplements their existing exact-path reports; it does not add four new unique
reviews or establish completion of the all-record objective.

## Evidence And Decisions

The [frozen context](inspected-context.json) contains the complete inspected
baseline records and five hash-pinned HTTP responses captured on 2026-10-08.
The original JCM973 URL returned HTTP 200 with `Nothing found.` The TOGO and
MediaDive APIs preserve the recipe and its preparation instructions; they are
transcriptions of the same JCM source, not independent experimental evidence.
Authors and publication year are unavailable and are not invented.

- Magnesium chloride hexahydrate: 203 g made **up to** 500.0 ml gives **406 g/L
  in the separate stock before autoclaving**. Four flattened 203 g/L values are
  corrected to this stock-scoped value, not to a final-medium concentration.
- Other components: dissolved **in** 500 ml water, without a final-volume
  instruction. Twenty-five unsupported g/L encodings are removed. Every source
  gram amount remains in ingredient notes with an exact snippet and source URL.
- Base-stock water: four 0.5 L batch inputs are represented, correcting two
  existing TOGO units and adding two missing MediaDive quantities. Magnesium
  makeup water remains unquantified; neither stock receives a numeric working
  dose after autoclaving.
- Agar remains specific to M1024. Its source says 20 g per preparation batch,
  not 20 g/L. The other three records do not acquire agar.

The repair moves 31 original ingredient nodes into eight preparation descriptors
and adds **45 evidence entries, eight references and four append-only codex
events**. Existing chemical groundings, physical states, IDs, root pH,
preparation text and historical metadata are preserved. The standalone record's
legacy placeholder and quality flags are unchanged. No growth associations,
taxonomic corrections or DSMZ1468 equivalence are asserted.

Final-medium concentrations, final mixed volume, magnesium makeup-water amount,
and actual stock-addition volumes remain unresolved. Source batch masses do not
become final concentrations merely because the schema accepts a number.

## Adversarial Review

1. **Resolved before apply:** the first preview put the prepared magnesium-stock
   volume into the working-dose slot. The final plan keeps it in preparation
   notes only. [The rejected preview](preview-v1-not-applied.json) is archived
   and was never applied.
2. **Resolved:** the previous TOGO verifier would reject legitimate later repairs
   to unchanged unsupported records. Explicit, verify-only hash-linked follow-up
   support now validates those records without rewriting historical reports or
   allowing the old apply operation to overwrite newer work.
3. **Covered by adversarial tests:** no treating water input as final volume,
   making up a stock dose, inferring final-medium salt/agar concentrations,
   changing hydrate identity, manufacturing quotes/year, rewriting history, or
   accepting concurrent record edits.

## Artifacts And Validation

- [Applied plan](plan.json): complete before/after text, hashes and 48 claim rows.
- [Per-record supplements](records): use `- Follow-up target:`, retaining the
  original reports' unique `- Record:` entries.
- [Independent audit](audit.py): checks literal source excerpts, arithmetic,
  stage boundaries, claim coverage and inversion of every allowed semantic edit.
- [Baseline checks](baseline.json): open schemas, full-corpus strict validation
  and 97 focused tests passed before application.
- [Post-application checks](validation.json): readback, no-op, independent audit,
  open schemas, strict validation of all 15,910 normalized records, permanent
  IDs, variant links, historical report continuity and 116 focused tests pass.
  The fast suite passes 7,773 tests (16 skipped, 1,889 deselected). Product
  validation exits 0 with 91 warnings and 96,061 no-adapter skips.
- [Citation checks](reference-validation.json): all 45 snippets pass the
  installed matcher; the independent audit also verifies exact captured text.
  Full reference validation fails on eight API-title mismatches: the installed
  fetcher returns URLs as titles instead of dataset name fields. Actual dataset
  titles remain in the records; neither metadata nor caches were falsified to
  force a pass.
- [Actual merge retention](merge-retention.json): all three media retain their
  complete stocks and provenance in current singleton groups; the solution is
  excluded. This does not demonstrate multi-source merge correctness.
- Global merge verification fails with 1,247 name conflicts and 3,287 fingerprint
  issues. [Freshness](merge-freshness.json) fails: 6,320 tracked versus 6,498 fresh
  outputs, with 3,723 tracked-only, 3,901 fresh-only, 1,709 changed and 888 unchanged
  shared paths. Generated repository merges were not hand-edited.
- [Final checks](final-checks.json) verify all four live record hashes, all five
  source captures, 48 report rows, semantic inversion, terminal journals, lint
  and formatting. They also check the next pair's unchanged baseline and four
  separate source captures; that triage is not applied curation.

These checks use the partial locked Python 3.13 environment, not full CI.
The records and reports remain local, uncommitted and unpublished.
