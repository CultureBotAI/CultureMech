# YAML Record Review: thermotoga_medium__5c966fff

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermotoga_medium__5c966fff.yaml
- Started UTC: 2026-09-25T10:57:34Z
- Finished UTC: 2026-09-25T10:59:36Z
- Verdict: needs curation

## Target

- Generated YAML for JCM Medium J237, THERMOTOGA MEDIUM.
- The record was merged from `thermotoga_medium`.
- The checked sources were the MediaDive REST entry for JCM J237 and the JCM 237 medium page.

## Validation

- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; exited 0 after the startup line only and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; exited 0 with only the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The direct source record is correctly identified as MediaDive/JCM Medium J237.
- pH 6.5 and the JCM autoclaving step are retained.
- The generated record has already merged duplicate salts from the main recipe, 250 ml/l Artificial sea water stock, and 15 ml/l Trace minerals stock into single top-level rows.

## Evidence

- MediaDive/JCM J237 defines a 1015 ml main solution consisting of 750 ml water, 250 ml artificial sea water, 15 ml trace minerals, 5 g starch, 0.5 g KH2PO4, 2 mg NiCl2 x 6 H2O, 20 g NaCl, 0.5 g yeast extract, 1 mg resazurin, and 0.5 g Na2S x 9 H2O.
- MediaDive/JCM J237 lists Artificial sea water as a 1000 ml stock that is added at 250 ml/l, not as direct full-strength final-medium seawater salts.
- MediaDive/JCM J237 lists Trace minerals as a 1000 ml stock that is added at 15 ml/l and includes its own nitrilotriacetic acid, MgSO4 x 7 H2O, NaCl, CaCl2 x 2 H2O, H3BO3, and other trace salts.
- The source preparation mixes all components except Na2S x 9 H2O, adjusts to pH 6.5, and autoclaves under N2.

## Completeness

- The pH and the MediaDive/JCM preparation steps are present.
- The generated record omits the explicit 750 ml main-water row.
- Artificial sea water and Trace minerals were expanded as undiluted top-level stock rows rather than preserved as stock additions or diluted into the final 1015 ml volume.

## Findings

- The final formula is not quantitatively faithful to JCM 237. NaCl is 48.4044 g/L because data-quality cleanup summed 19.7044 g/L normalized main NaCl with undiluted 27.7 g/L Artificial sea water NaCl and undiluted 1 g/L Trace minerals NaCl.
- CaCl2 x 2 H2O, MgSO4 x 7 H2O, and H3BO3 are also inflated by direct stock expansion and duplicate summing; the stock contributions were never scaled by 250 ml/l for Artificial sea water or 15 ml/l for Trace minerals.
- The exact ignored/hidden source-ID search found a stale TOGO M229 duplicate for the same JCM 237 source. That duplicate has the same stock-modeling problem plus separate TOGO unit and pH losses.

## Recommended Edits

- Regenerate JCM 237 with Artificial sea water and Trace minerals represented as 250 ml/l and 15 ml/l stock additions, or with each stock row expanded only after the correct dilution is applied.
- Stop summing main-medium salts with undiluted stock-recipe salts.
- Preserve the pH 6.5 and preparation steps that are already available in the direct MediaDive/JCM import.
- Merge or retire the TOGO M229 duplicate after the direct JCM record is repaired.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Compare NaCl, CaCl2 x 2 H2O, MgSO4 x 7 H2O, H3BO3, NiCl2 x 6 H2O, and resazurin against the MediaDive/JCM 237 values after the 1015 ml final-volume normalization.

## Additional Notes

- None found.
