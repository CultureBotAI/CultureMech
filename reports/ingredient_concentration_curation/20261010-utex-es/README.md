# UTEX Enriched Seawater Ingredient Review

## Applied Locally, Validation Recorded

The six exact records in [the applied plan](plan-v3.json) are changed locally.
The [source ledger](source-review-v2.json) covers all 124 ingredient and stock
quantity claims using twelve official UTEX recipes and separately scoped
chemical identity sources. Six linked formulation PDF page images were
inspected. Report coverage does not certify a complete formulation.

- Twenty stock nodes relocated: ES Fe, P-II and three vitamin stocks now sit
  inside the enrichment stock in each of four expanded recipes.
- Eight amount-basis corrections: 1 L seawater and the respective 20, 2, 10 or
  5 mL enrichment are absolute inputs, not fractions of an assumed final volume.
- Twenty-four unsupported water quantities removed; the solvent ingredients
  and source-backed makeup/buffer notes remain.
- Eight vitamin identities corrected to cyanocobalamin or thiamine hydrochloride.
  Four unsupported glycerophosphate primary/MIM identifier pairs are removed;
  the supplied beta-glycerophosphate disodium pentahydrate is retained without
  inventing an exact replacement identifier.
- 134 evidence entries, 26 references, thirty bibliography enrichments and six
  append-only history events. Forty-eight ingredient/stock notes and nine
  parent/child dose descriptions are clarified.
- No taxa-media associations added. Permanent IDs, earlier history, growth
  claims and unrelated recipe fields remain unchanged.

Stock mass concentrations remain at their source-supported values. The two
dilution records retain the explicitly reported 500/500 and 665/335 mL per
1 L total; the latter is not rounded to mathematical thirds.

## Evidence Limits

The parent HTML total-volume heading conflicts with its per-liter-of-seawater
procedure and PDF. No measured final mixture volume is inferred. The enrichment
source lists vitamin doses but omits a later vitamin-addition instruction.
The ES Fe formula/catalog discrepancy and the unquantified P-II cobalt sulfate
alternative remain explicit. No catalog-based chemical replacement, alternative
mass, or molar conversion is invented.

The packaged MIM index retains an incorrect glycerophosphate alias. Its immutable
snapshot is not changed. Supplier and ChEBI pages inspected through the web tool
are distinguished from complete downloaded captures. Unknown named authors and
publication years are not invented; the 2/3 PDF copyright notice does not date
the current HTML. Generic lighting, temperature and growth claims are outside
this ingredient review.

## Validation

The initial unapplied preview had three adversarial failures because a missing
relationship note raised a raw KeyError. The rejection is now explicit. A second
preview passed 141 tests, but manual review found 2/3-specific wording carried
into the 1/2 dilution explanation; that was corrected before any recipe edits.
Historical plans, ledgers and logs are retained rather than overwritten.

The [final preview](preview-v3.json) passes all 24 baseline/proposed schema
commands, 142 adversarial/equivalence tests, Ruff, Black and diff checks.
[Application](apply.json) changes exactly six normalized records. Readback and
repeat no-op pass. The ignored-inclusive baseline report inventory confirms
all six records were outside the preceding follow-up coverage.

Six canonical per-record reports cover all 124 quantity claims. Cumulative
reconciliation verifies 5,377 edited records, 37,337 added evidence entries,
6,040 references, 5,616 history events and 1,751 quantity corrections. Follow-up
reports cover 11,905 of 15,910 exact normalized paths; 4,005 remain outside this
coverage. Report presence is not complete scientific verification.

Live reference validation passes for both dilution records (four snippet and
two title checks). The four expanded-recipe commands abort on supplier timeouts
without per-claim results; no automatic snippet passes are inferred for them.
Manual source inspection remains separate, and the production reference gate
does not pass.

Index regeneration changes only the four expanded recipes' root solution counts
from six to one in `algae_index.json`, `recipe_index.json` and
`by_source_unknown_index.json`. All other generated indexes are semantically
unchanged. Runtime merge-retention checks preserve all six distinct formulations,
their evidence and valid parent/child links; no merged YAML is written.

All twelve post-edit schema/strict commands and 351 focused tests pass. Corpus
strict, ID, product and MIM-index checks pass. Product checks retain 91 warnings
and 96,008 no-adapter skips. Global merge verification still fails with 1,247
name conflicts and 3,287 fingerprint issues. Freshness also fails: 15,056
differences (2,045 changed, 4,275 only tracked and 8,736 only fresh), with 6,320
tracked versus 10,781 freshly derived records.

The fast tier finishes with **15,056 passed, sixteen skipped, 3,498 deselected
and two dependency deprecation warnings**, in 1,892.24 seconds. This is not a
full-suite pass. The [terminal checkpoint](validation.json) verifies unchanged
tested code, schema, audit registry, source captures, report/index hashes and all
15,910 normalized record hashes, plus guarded readback. It records the failed
reference and merge gates separately from the passing local checks.

Nothing is committed, merged or publication-ready; the full all-record objective
remains active. F/2 inline-variant evidence, NH4 snippet/relationship corrections
and the remaining corpus source reviews are still pending.
