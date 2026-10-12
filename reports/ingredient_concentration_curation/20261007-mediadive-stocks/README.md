# MediaDive Stock Concentration Curation

Status: **applied locally; partial progress, not corpus-wide completion**.

Reviewed baseline: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`.
`origin/main` was fetched and matched that commit before this batch. The earlier
three-record JCM curation batch was preserved. Only authoritative normalized
records changed; no derived merges, pages, taxa-media associations, or IDs changed.

## Applied Results

| Exact record | Claims inspected | Corrections | Evidence-only claims | Unresolved |
| --- | ---: | ---: | ---: | ---: |
| [3980 trace elements](mediadive_3980_Trace_element_solution.md) | 12 | 1 | 10 | 1 |
| [3981 Se/W](mediadive_3981_Se_W_solution.md) | 4 | 1 | 2 | 1 |
| [3861 trace vitamins](mediadive_3861_Trace_vitamins.md) | 12 | 1 | 10 | 1 |
| [595 SL-10](mediadive_595_Trace_element_solution_SL-10.md) | 11 | 1 | 8 | 2 |
| [5980 Wolin vitamins](mediadive_5980_Wolin_s_vitamin_solution_10x.md) | 12 | 1 | 10 | 1 |
| Total | 51 | 5 | 40 | 6 |

Five records changed, zero failed or skipped. Forty-five new ingredient-level
evidence entries support 45 record-local claims. Every entry includes the exact
upstream JSON excerpt, stable official source URL, claim path, locator,
calculation or interpretation, access date, and response SHA256. Each record has
a bibliography entry and an append-only `codex` curation event. Source titles,
type, discovery mode, and organization are recorded; individual authors and
publication year were not supplied by the responses and were not invented.

The five corrected water claims were imported as `990` or `1000 PERCENT_V_V`:

- Stocks 3981, 3861, and 5980 now retain the source's 1000 ml water addition as
  `1 L` per prepared batch, not a volume percentage.
- Stocks 3980 and 595 now use `VARIABLE`, with value `to 1 L final volume`,
  following the explicit make-up instruction. The original table amounts and
  instruction remain quoted separately; no exact delivered water volume is assumed.

The 40 mass concentrations were not changed. Their evidence supports the
provider-declared stock `g_l` values, cross-checked against source amount, unit,
and declared stock volume. It does not establish concentrations in a receiving
medium, or infer a measured final volume from the water addition alone.

The six unresolved claims are five legacy `See source for composition`
placeholders and the SL-10 HCl mass concentration. The placeholders and existing
quality flags remain unchanged; composition evidence is not evidence for a
placeholder. Ingredient source IDs and exact source labels/forms were checked;
existing secondary ontology groundings were not re-curated in this batch.

## Sources And Open Questions

Official REST responses were retrieved over HTTPS on 2026-10-07:

- [Solution 3980](https://mediadive.dsmz.de/rest/solution/3980)
- [Solution 3981](https://mediadive.dsmz.de/rest/solution/3981)
- [Solution 3861](https://mediadive.dsmz.de/rest/solution/3861)
- [Solution 595](https://mediadive.dsmz.de/rest/solution/595)
- [Solution 5980](https://mediadive.dsmz.de/rest/solution/5980)

Exact response hashes are pinned in the mutator and each per-record report.
Raw responses are local research captures, not checked-in curation artifacts.
These institutional URLs identify the actual recipes; no DOI was invented.

SL-10's API lists a 10 ml dose with attribute `25%`, without specifying its
percentage basis. The source PDF cross-checks also say only `HCl (25%) 10.00 ml`:
[DSMZ 1255, page 1, SL-10 table](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1255.pdf)
and [its cited DSMZ 320 stock recipe, page 1](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf).
Both give a final stock make-up instruction, but neither inspected table supplies
the missing HCl percentage basis/density. No new SUPPORT evidence was attached
to the existing `2.5 G_PER_L`. Do not treat the API's derived value as independent
confirmation, or encode the stock dose as a volume of pure HCl.

## Reproducibility

The scoped mutator is
[`scripts/repair_mediadive_stock_concentration_evidence.py`](../../../scripts/repair_mediadive_stock_concentration_evidence.py).
It does not reimport the corpus or automatically extend this reviewed cohort.
It pins baseline record hashes, exact tracked paths, stable IDs, source hashes,
solution IDs, compound IDs, names, hydrate forms, and original values. It rejects
conditional/optional rows, unreviewed stock attributes, missing or nonfinite
numbers, ambiguous source excerpts, new nested content, and concurrent edits.
The whole cohort is prepared and closed-schema validated before any recipe write.

Place the five verified responses in a local source directory with filenames
`ingredient-mediadive-solution-<ID>-20261007.json`, then run:

```bash
PYTHONPATH=src uv run python scripts/repair_mediadive_stock_concentration_evidence.py \
  --source-dir <source-directory> --dry-run
PYTHONPATH=src uv run python scripts/repair_mediadive_stock_concentration_evidence.py \
  --source-dir <source-directory> --apply \
  --report-dir reports/ingredient_concentration_curation/20261007-mediadive-stocks
```

Changed upstream response bytes require new review, not bypassing the hash check.
After apply, a second apply changed zero recipes and added no evidence or events.
Do not regenerate the per-record reports against a different cohort or baseline.

## Verification

- `just validate-schema`: passed for all five records before and after edits.
- `just validate-strict`: all five records, zero errors before and after edits.
- Write-time `validate_recipe(..., target_class="SolutionRecipe")`: passed.
- Focused curation, earlier audit, plausibility, record-IO, merge and freshness
  regression selection: **128 passed**, including 27 new stock curation tests.
  After adding three CLI/preflight safety tests, the expanded stock suite passed
  **30 tests** (overlaps the earlier 27; do not add these suite totals).
- Read-back verification: all 45 persisted snippets are exact substrings of the
  hash-verified responses, and all original history entries remain unchanged.
- Ruff, Black, and `git diff --check`: passed.
- `just validate-references`: unavailable in the isolated Python 3.11 runtime;
  `linkml-reference-validator` could not spawn. Source retrieval, manual source
  inspection, exact-substring checks, and arithmetic checks above are distinct
  from an automated reference-validation pass.
- Five before/after merge fingerprints remain `None`: these standalone solution
  compositions were already excluded from the current recipe merge pipeline.
  This is a pipeline coverage limitation, not proof that their data are absent.
- Full `just verify-merges`: exit 1, with 1,247 duplicate canonical-name conflicts
  and 3,286 fingerprint issues in the untouched merged corpus, matching the
  previous batch's completed check.
- Full `just audit-merge-freshness --json`: completed with exit 1 (drift), also
  matching the previous batch: 6,320 tracked files versus 6,461 generated files;
  3,723 filenames only in tracked output, 3,864 only in fresh output, 1,469 shared
  files with changed content, and 1,128 unchanged. These are filename/content
  comparisons, not counts of missing independent scientific recipes. Temporary
  generation covered all 15,910 inputs; no generated files were copied into the
  worktree.
- Runtime: isolated Python 3.11 with current repository source/schema. Native
  PyYAML `CSafeLoader` accelerated the full merge gates without changing scope or
  rules; YAML output still uses the maintained emitter.

## Remaining Scope

This batch does not resolve the earlier 18 M1308 concentration gaps or its two
inline variants, flattening in DSMZ 962a/1255, the other MediaDive solution unit
errors, or the remainder of the all-record review. No correction was propagated
to a similarly named medium or variant.

A new git-tracked inventory of the current worktree found 15,910 normalized YAML
records, including 4,775 records whose root term starts with
`mediadive.solution:`. Those solution compositions contain 34,967 concentration
objects; 34,922 lack an ingredient-level entry containing both a nonempty snippet
and an HTTP(S)/DOI reference. This is a presence check, not scientific verification
or a count of all possible evidence containers. There are 4,414 numeric
`PERCENT_V_V` values greater than 100 in 4,279 of these records after this batch.
Each needs source-specific review; the flag alone does not authorize division by
ten or any other numerical correction. Other solution types, embedded stocks,
variants, and ordinary medium ingredients remain in the full goal's scope too.

The importer still maps volume amounts to percent without the correct factor;
do not rerun it as a repair. A future source-verified batch should address that
conversion and preserve stock-strength attributes, units, and preparation stage
before broadening apply scope.
