# YAML Record Review: tissierella_amo_1_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/tissierella_amo_1_medium.yaml`
- Started UTC: 2026-09-25T13:17:52Z
- Finished UTC: 2026-09-25T13:17:52Z
- Verdict: needs curation

## Target

Reviewed generated merged YAML for DSMZ medium 683, `TISSIERELLA (AMO.1) MEDIUM`.

The generated record merges three sources: the DSMZ normalized record and two KOMODO records, `amo_1_medium` and `amo_1_medium_replace_n_methylhydantoin_with_creatinine`.

## Validation

- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 errors; the TSV contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed; the only diagnostic was the known eutils/pkg_resources startup warning.
- Embedded curation history: Not checked; the available history validator targets standalone `history/` records, not `MediaRecipe.curation_history`.

## Identity and Grounding

The medium identity is grounded to DSMZ medium 683 by `media_term.term.id: mediadive.medium:683`, the DSMZ link in `notes`, and KOMODO synonyms that also point to medium 683.

DSMZ medium 683 lists its parent ingredients in 1000 ml water plus 1 ml each of Trace element solution SL-10, selenite-tungstate solution, and 10x Wolin's vitamin solution.

## Evidence

The generated record captures the parent salts, amino acids, N-methylhydantoin, bicarbonate, resazurin, and L-cysteine from the DSMZ recipe after volume normalization.

The trace, selenite-tungstate, and vitamin rows are stock-solution recipes, not independently supplied final liter concentrations.

## Completeness

No target organisms are present; that empty optional field is not a defect in this formulation review.

The record keeps the KOMODO `amo_1_medium_replace_n_methylhydantoin_with_creatinine` source as a source duplicate, but the DSMZ source describes creatinine as an alternate substrate replacing N-methylhydantoin. That variant semantics are not represented as a distinct creatinine-containing variant.

## Findings

- Major issue: Trace element solution SL-10 is flattened at stock concentrations. For example, `HCl` is recorded as 2.5 g/L and `FeCl2 x 4 H2O` as 1.5 g/L even though the parent medium adds only 1 ml of SL-10 per liter.
- Major issue: Selenite-tungstate solution is flattened at stock concentrations. The generated NaOH, Na2SeO3 x 5 H2O, and Na2WO4 x 2 H2O rows are stock recipe amounts, not final parent-medium concentrations.
- Major issue: Wolin's vitamin solution is a 10x stock added at 1 ml per liter, but the vitamin rows are recorded as stock g/L amounts.
- Minor issue: the creatinine replacement should be curated as an explicit variant if retained. The current merge treats the replacement record as a same-signature source duplicate and does not add creatinine or a substitution statement in `variants`.

## Recommended Edits

- Restore Trace element solution SL-10, selenite-tungstate solution, and Wolin's vitamin solution as nested component additions or dilute their stock ingredients into the parent medium with the source 1 ml/L factors.
- Keep the source preparation text for stock recipes with the stock component that it belongs to.
- Model the creatinine-for-N-methylhydantoin substitution as a `MediaVariant`, or remove the KOMODO replacement synonym from this parent if it cannot be grounded to a distinct source recipe.

## Follow-up Checks

- Confirm whether KOMODO medium 683 with creatinine maps to the DSMZ note or to an independent recipe before adding a creatinine variant.
- Re-run schema, strict, reference, and term validation after editing the normalized source YAML records and regenerating the merge.

## Additional Notes

Exact local source search found only the expected normalized DSMZ and KOMODO siblings for this merge. Ignored files were included for duplicate-report checks with `find`, and no pre-existing ignored report for this generated record was found.
