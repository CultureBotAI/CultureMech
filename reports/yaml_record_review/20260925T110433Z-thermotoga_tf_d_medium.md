# YAML Record Review: thermotoga_tf_d_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermotoga_tf_d_medium.yaml
- Started UTC: 2026-09-25T11:00:12Z
- Finished UTC: 2026-09-25T11:04:33Z
- Verdict: needs curation

## Target

- Generated YAML for DSMZ Medium 1232, THERMOTOGA TF(D) MEDIUM.
- The record was merged from `tf_d_medium` and `thermotoga_tf_d_medium`.
- The checked sources were MediaDive REST entry 1232 and the DSMZ Medium 1232 PDF.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; exited 0 after the cache line only.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The record is correctly identified as DSMZ Medium 1232, and the source-duplicate merge folded the KOMODO `komodo.medium:1232` copy into the direct DSMZ record.
- pH 6.8 and the main DSMZ anoxic preparation text are retained.
- The generated ingredient list still includes full-strength Modified Wolin and Wolin vitamin stock rows.

## Evidence

- DSMZ/MediaDive 1232 lists 1000 ml water plus NH4Cl, MgSO4 x 7 H2O, MgCl2 x 6 H2O, K2HPO4, Na2HPO4 x 2 H2O, NaCl, 10 ml/l Modified Wolin's mineral solution, yeast extract, Trypticase peptone, 0.5 ml/l 0.1% sodium resazurin, starch, CaCl2 x 2 H2O, 1 ml/l Wolin's vitamin solution, L-Cysteine HCl x H2O, and Na2S x 9 H2O.
- Modified Wolin's mineral solution is a 1000 ml DSMZ stock used at 10 ml/l in the main medium.
- Wolin's vitamin solution is a separate 1000 ml stock used at 1 ml/l in the main medium.

## Completeness

- The pH, main preparation text, and source duplicate relationship are present.
- The generated record omits the 1000 ml distilled-water row.
- The 10 ml/l Modified Wolin and 1 ml/l Wolin vitamin additions are expanded as undiluted top-level stock recipes.

## Findings

- The final formula is not quantitatively faithful to DSMZ 1232. Data-quality cleanup summed main MgSO4 x 7 H2O, NaCl, and CaCl2 x 2 H2O with undiluted Modified Wolin stock rows, producing 4.87933 g/L MgSO4 x 7 H2O, 26.7171 g/L NaCl, and 0.653907 g/L CaCl2 x 2 H2O.
- The Wolin 10x vitamin stock was expanded at full stock strength even though the source adds only 1 ml/l.
- The exact ignored/hidden source-ID search confirmed this generated record already folds the KOMODO DSMZ 1232 duplicate into the direct DSMZ 1232 record, so the remaining issue is stock modeling rather than an unmerged direct/KOMODO pair.

## Recommended Edits

- Regenerate DSMZ 1232 with Modified Wolin's mineral solution represented as a 10 ml/l addition and Wolin's vitamin solution represented as a 1 ml/l addition, or with both stocks expanded only after applying those dilutions.
- Stop summing main-medium MgSO4 x 7 H2O, NaCl, and CaCl2 x 2 H2O with undiluted Modified Wolin stock salts.
- Restore the explicit 1000 ml distilled-water row if water is expected in regenerated DSMZ records.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Compare the regenerated formula against DSMZ 1232 and verify that no vitamin stock row remains at full 10x strength in the final medium.

## Additional Notes

- None found.
