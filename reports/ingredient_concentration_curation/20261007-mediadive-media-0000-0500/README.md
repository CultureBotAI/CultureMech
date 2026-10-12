# Receiving-Medium Concentration Source Pass: Records 0-499

Applied locally on 2026-10-07, against baseline
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`. This is a partial source pass within
the all-record objective, not completion of these media or the corpus.

The subsequent [DSMZ 2 follow-up](../20261007-dsmz2-stock-boundary/README.md)
repairs one of the 340 originally unchanged records. Original batch counts and
rows below remain historical; current read-back uses its explicit hash-linked
successor, preserving the one-report-per-exact-path inventory.

## Scope And Result

The first 500 entries of the frozen [3,329-medium inventory](../20261007-medium-source-inventory.json)
have one per-record result each under `records/`, including 340 unchanged records.
The inventory uses exact tracked paths and source IDs, not case-insensitive
filesystem lookup or name-based recipe matching. The subsequent
[500-999 batch](../20261007-mediadive-media-0500-1000/README.md) advances the
inventory boundary; unresolved work within this batch remains open.

Later preparation-context inspection identified an [over-scoped DSMZ 12
extraction-input claim](../20261007-mediadive-media-0500-1000/extraction-scope-finding.md).
Its literal snippet and numeric read-back are intact, but the current evidence
does not distinguish extraction input from finished-medium concentration.
Authoritative correction remains required; the historical acceptance counts
below are not a claim that every interpretation is scientifically verified.

- 160 additional authoritative normalized records changed.
- 907 new ingredient-level evidence entries, 160 bibliography entries, and
  160 append-only curation events.
- No numeric concentration changes or newly filled concentration slots.
- No chemical identifier, ingredient inventory, stock, variant, or growth-association changes.
- Zero failed records and zero baseline/proposed schema failures.

The [plan](plan.json) records exact before/after/source hashes, field paths,
old/new values, source locators, quotations, calculations, and decisions. The
official source endpoint is `https://mediadive.dsmz.de/rest/medium/{id}`.
Serial retrieval completed all 500 sources without failures. The retained
snippets are literal JSON excerpts from those responses, not reconstructed quotes.
Titles, institutional source, discovery mode, access dates, and original recipe
links are captured. Individual authors and publication year are not supplied by
these API records and were not invented.

## Evidence Boundaries

Accepted claims match the exact medium accession/name and original collection
link, main-solution identity, direct ingredient inventory, source chemical form,
and existing quantity. Explicit provider `g_l` values are checked against the
source amount/unit/volume arithmetic. Existing amounts are preserved. Evidence
is scoped to the provider-declared main-recipe concentration, not an independently
measured final volume, stock composition, or downstream dilution. Secondary
ontology mappings are not validated by this amount evidence.

Optional/conditional rows and stock-strength attributes are not silently
discarded. The sole automatically accepted condition is `for solid medium` when
the local physical state is `SOLID_AGAR`. Omitted solvent, source-only ingredients,
stock doses (including missing doses and unasserted candidates), preparation
instructions, and variant relationships appear as explicit follow-up rows.

Manual cross-checks included the [original nutrient-agar recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1.pdf)
and the [original Azotobacter recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium3.pdf).
The latter's full single page was also visually inspected, confirming hydrated
salt forms, milligram units, and the separate sugar-preparation water instruction.
Downloaded PDF SHA256:
`5886d55d76e69c43de307ecaaa5dee4577336f93851b0d0d755fdbd292cf5193`.
These are representative manual checks, not a claim to have manually read all
500 source documents. MediaDive's [solution catalogue](https://mediadive.dsmz.de/solutions)
also explicitly labels solution volumes in ml and its [manual](https://mediadive.dsmz.de/docs/website)
distinguishes recipes from molecular compositions.

## Unresolved Findings

The 11,289 unsupported report rows comprise 9,287 unmatched source recipe rows,
1,381 preparation-context rows, 395 variant/candidate rows, and 226 local
concentrations. Another 7,162 local concentration rows are marked conflict.
These are report-row counts, not counts of independent scientific findings.

- Stock topology blocks support in 293 records. Source-specific reconstruction
  is still needed; stock concentrations were not endorsed as main-medium amounts.
- Source arithmetic disagrees for 36 rows in nine records. Values remain
  unchanged; rounding tolerances were not widened to force acceptance.
- Nineteen records lack source ingredient/preparation inventory required by the
  reviewer. Source name/link drift and duplicate ingredient labels also remain
  explicit conflicts, not guessed mappings.
- Source-only solvent/ingredients, preparation-dependent quantities, and variant
  formulations require further curation. A result file does not mean completion.

### Merge Evidence Loss: Unresolved

The [actual-group audit](merge-retention.json) invoked the maintained matcher and
merger across the corpus, then inspected the 151 groups containing these 160
edited records. Only **230 of 907** accepted amount/evidence pairs survive.
**119 records lose evidence; 112 lose the new bibliography entry.** The audit
exits 1. Authoritative YAML remains intact.

`RecipeMerger._merge_ingredients` selects one ingredient list by chemical
annotation completeness and discards the others; root metadata is likewise
taken from the canonical recipe. For example, the DSMZ 265/KOMODO 265 group
selects `CultureMech:004668` and loses all twelve newly supported amount claims
from `CultureMech:001364`. This behavior needs formulation-aware evidence
preservation. A concentration-independent ingredient fingerprint is not enough
to transfer support between media or variants.

No generated recipes were copied into the worktree. The loss is not treated as
a passing merge gate or as a reason to erase correct normalized evidence.

## Verification

See [validation.json](validation.json) for exact outcomes and commands.

- All 500 result hashes and 907 new snippets matched the source captures.
- Reapplying the plan changed zero records; all 160 edits were already applied.
- 257 selected regression tests passed, including source identity, repeated JSON
  rows, hydrate/stock boundaries, arithmetic, report coverage, stale-plan guards,
  record I/O, and maintained merge/freshness behavior.
- Baseline and post-edit strict validation: 15,910 files, zero errors. ID gate
  passed. Representative baseline/post-edit open-schema checks passed.
- Independent whole-worktree diff audit confirms append-only provenance and no
  unrelated data changes. Current totals are [4,295 edited records and 24,906 new evidence entries](../20261007-diff-audit-after-media-0500.json).
- Full merge verification remains failing: 1,247 name conflicts and 3,286
  fingerprint issues. Freshness and retention failures are separate from schema validity.
  Freshness also exits 1: 3,723 only-tracked, 3,864 only-generated, 1,487 changed,
  and 1,110 unchanged records. The generated corpus was built only in a temporary directory.
- Ruff, Black, and `git diff --check` passed.
- Product validation cannot load `oaklib`; the reference-validator executable
  is unavailable. Neither is counted as a passing check.

Checks used the isolated Python 3.11 runtime; no maintained Python 3.13/CI pass
is asserted. All curation changes remain local and uncommitted.
