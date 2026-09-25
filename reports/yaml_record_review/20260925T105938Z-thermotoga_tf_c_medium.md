# YAML Record Review: thermotoga_tf_c_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermotoga_tf_c_medium.yaml
- Started UTC: 2026-09-25T10:57:36Z
- Finished UTC: 2026-09-25T10:59:38Z
- Verdict: needs curation

## Target

- Generated YAML for DSMZ Medium 613, THERMOTOGA TF(C) MEDIUM.
- The record was merged from `thermotoga_tf_c_medium`.
- The checked sources were MediaDive REST entry 613 and the DSMZ Medium 613 PDF.

## Validation

- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The direct source record is correctly identified as DSMZ Medium 613.
- The source pH range, 6.5 to 6.8, and the DSMZ anoxic preparation text are retained.
- Data-quality cleanup already merged the duplicate NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O rows created by flattening the Modified Wolin stock into the main recipe.

## Evidence

- DSMZ/MediaDive 613 lists 1000 ml water plus NH4Cl, K2HPO4, Na2HPO4 x H2O, NaCl, MgCl2 x 6 H2O, MgSO4 x 7 H2O, 10 ml/l Modified Wolin's mineral solution, yeast extract, Trypticase peptone, 0.5 ml/l 0.1% sodium resazurin, D-glucose, CaCl2 x 2 H2O, 1 ml/l Wolin's vitamin solution, L-Cysteine HCl x H2O, and Na2S x 9 H2O.
- DSMZ 613 adjusts the medium to pH 6.5 to 6.8, sparges with 100% N2, autoclaves under anoxic conditions, and adds glucose, calcium chloride, vitamins, sulfide, and cysteine from sterile anoxic stocks.
- The source uses the same 1000 ml Modified Wolin's mineral solution stock as DSMZ Medium 664 and adds a separate 1000 ml Wolin's vitamin solution stock at 1 ml/l.

## Completeness

- The direct record keeps the pH range and main DSMZ preparation text.
- The generated record omits the 1000 ml distilled-water row.
- Modified Wolin's mineral solution and Wolin's vitamin solution were both expanded as full-strength top-level stock recipes.

## Findings

- The formula has blocking stock-solution flattening. The 10 ml/l Modified Wolin's mineral solution addition was expanded at whole-stock strength, adding full 1 g/L NaCl, 3 g/L MgSO4 x 7 H2O, and 0.1 g/L CaCl2 x 2 H2O rows to the main formulation.
- The 1 ml/l Wolin's vitamin solution addition was expanded into full-strength 10x vitamin stock rows rather than diluted into the final medium.
- The exact ignored/hidden source-ID search found a KOMODO DSMZ 613 duplicate, `tf_c_medium`, with the same stock expansion and a conflicting pH range of 6.8 to 7.0.

## Recommended Edits

- Regenerate DSMZ 613 with Modified Wolin's mineral solution represented as a 10 ml/l addition and Wolin's vitamin solution represented as a 1 ml/l addition, or with both stocks expanded only after applying those dilutions.
- Keep the direct DSMZ pH range and anoxic preparation text.
- Stop summing main-medium NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O with Modified Wolin stock salts at undiluted concentrations.
- Merge or retire the KOMODO `tf_c_medium` duplicate after the direct DSMZ 613 record is repaired.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Compare the regenerated formula against DSMZ 613 and verify that vitamin rows are absent from the top-level recipe unless they have been diluted from a 1 ml/l 10x stock.

## Additional Notes

- None found.
