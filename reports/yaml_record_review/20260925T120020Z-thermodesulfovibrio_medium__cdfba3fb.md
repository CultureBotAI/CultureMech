# YAML Record Review: thermodesulfovibrio_medium__cdfba3fb

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfovibrio_medium__cdfba3fb.yaml
- Started UTC: 2026-09-25T12:00:20Z
- Finished UTC: 2026-09-25T12:00:20Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:002828`, `thermodesulfovibrio_medium`, generated from JCM Medium J479 / MediaDive `mediadive.medium:J479`.

## Validation

- LinkML schema: Passed with `linkml-validate`; no issues found.
- Strict validation: Passed with 0 ERROR rows; `/private/tmp/thermodesulfovibrio_medium__cdfba3fb.strict.tsv` contained only the header.
- Reference validation: Passed; the validator ran 0 checks for this record.
- Term validation: Passed.
- Embedded curation history: Not checked; the available history validator covers standalone `history/` records, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The recipe identity is grounded correctly to JCM Medium J479, "THERMODESULFOVIBRIO MEDIUM". The direct JCM page and MediaDive payload both show that J479 is assembled from Solution A of JCM Medium J284, without yeast extract, plus separate J479 Solution B and Solution C stocks.

## Evidence

- JCM J479: Solution A delegates to Medium No. 284 without yeast extract and the final medium is completed by adding 0.05 volume each of Solutions B and C, then 0.01 volume of 3% L-cysteine x HCl x H2O and 0.01 volume of 3% Na2S x 9H2O solutions before inoculation.
- MediaDive J479: Solution B is a 50 ml stock with 2.2 g sodium lactate in 50 ml distilled water; Solution C is a 50 ml stock with 2.8 g Na2SO4 in 50 ml distilled water.
- JCM J284: Solution A contains KH2PO4, MgCl2 x 6 H2O, CaCl2 x 2 H2O, NH4Cl, trace vitamins solution, trace element solution, Se/W solution, NaHCO3, resazurin, and 900 ml distilled water, with yeast extract to be omitted for J479.

## Completeness

The generated record only carries the two high-concentration J479 stock rows. It omits the delegated J284 Solution A base, the water rows, the nested trace-vitamin, trace-element, and Se/W stocks, NaHCO3, resazurin, the anaerobic reduced additions, and explicit stock-volume additions for J479 Solutions B and C.

## Findings

- The `Sodium lactate` and `Na2SO4` ingredients are the full 50 ml stock strengths from J479 Solution B and Solution C, 44 G_PER_L and 56 G_PER_L, not final medium concentrations.
- The record drops Solution A from Medium No. 284 instead of copying J284 Solution A while omitting yeast extract.
- The 3% L-cysteine x HCl x H2O and 3% Na2S x 9H2O reducing solutions are only present in free text and are absent from structured ingredients or stock-addition structure.
- The preparation steps preserve the broad completion text but do not model the stock boundaries, stock volumes, N2-CO2 handling inherited from J284, or the overnight post-autoclave stand for Solution A.

## Recommended Edits

- Rebuild J479 as a stock-aware recipe with a J284-derived Solution A that excludes yeast extract.
- Represent J479 Solutions B and C as 50 ml stocks and their 0.05 volume additions instead of flattening 44 G_PER_L sodium lactate and 56 G_PER_L Na2SO4 into the top-level medium.
- Add structured anaerobic 3% L-cysteine x HCl x H2O and Na2S x 9H2O additions, preserving their 0.01 volume addition instructions.
- Add the distilled-water rows and keep the J284 trace vitamin, trace element, and Se/W recipes scoped to their stock solutions.

## Follow-up Checks

- Revalidate the curated stock structure against the schema after deciding whether Solution A should be embedded directly or represented as a cross-medium stock dependency.
- Confirm the intended final volume denominator for the two 0.01 volume reducing additions before deriving any final G_PER_L values.

## Additional Notes

No target-organism evidence was reviewed. The exact local source search included ignored and hidden files and found only the expected J479 normalized recipe for this record; nested source pages J284 and J479 were fetched directly from JCM.
