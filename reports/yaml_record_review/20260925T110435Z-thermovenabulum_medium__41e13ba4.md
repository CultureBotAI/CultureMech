# YAML Record Review: thermovenabulum_medium__41e13ba4

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermovenabulum_medium__41e13ba4.yaml
- Started UTC: 2026-09-25T11:00:14Z
- Finished UTC: 2026-09-25T11:04:35Z
- Verdict: needs curation

## Target

- Generated YAML for KOMODO Medium 1255, THERMOVENABULUM medium, linked to DSMZ Medium 1255.
- The record was merged from `KOMODO_1255_THERMOVENABULUM_medium` and `thermovenabulum_medium`.
- The checked sources were MediaDive REST entry 1255 and the DSMZ Medium 1255 PDF.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; exited 0 after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The generated record correctly links KOMODO Medium 1255 to DSMZ Medium 1255 and explicitly marks the KOMODO and direct DSMZ records as source duplicates.
- pH 7.0 is retained.
- The direct DSMZ preparation text did not survive into the generated KOMODO-led merge.

## Evidence

- DSMZ/MediaDive 1255 lists 1000 ml water plus NaCl, NH4Cl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, KH2PO4, K2HPO4, 10 ml/l Trace element solution SL-10, yeast extract, tryptone, 0.5 ml/l FeSO4 in acid, PIPES, 0.5 ml/l 0.1% sodium resazurin, D-glucose, 1 ml/l Wolin's vitamin solution, and Na2S x 9 H2O.
- Trace element solution SL-10 is a 1000 ml DSMZ stock used at 10 ml/l in the main medium.
- Wolin's vitamin solution is a separate 1000 ml stock used at 1 ml/l in the main medium.
- DSMZ 1255 has an anoxic N2 preparation step that adds glucose, vitamins, and sulfide after autoclaving.

## Completeness

- The pH and duplicate relationship are present.
- The generated record lacks the DSMZ preparation step and omits the 1000 ml distilled-water row.
- SL-10 and Wolin's vitamin solution were expanded as undiluted top-level stock recipes.

## Findings

- The formula has blocking stock-solution flattening. The 10 ml/l SL-10 addition was expanded as full-strength HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O rows.
- The 1 ml/l Wolin's vitamin solution addition was expanded into full-strength 10x vitamin stock rows.
- The record should carry the DSMZ preparation step from the direct source when merging the KOMODO and DSMZ duplicates.

## Recommended Edits

- Regenerate DSMZ/KOMODO 1255 with Trace element solution SL-10 represented as a 10 ml/l addition and Wolin's vitamin solution represented as a 1 ml/l addition, or with both stocks expanded only after dilution.
- Preserve the DSMZ 1255 anoxic preparation text during source-duplicate merging.
- Restore the explicit 1000 ml water row if water is expected in regenerated DSMZ records.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Compare the regenerated formula against DSMZ 1255 and verify that SL-10 and Wolin vitamin rows are either nested or correctly diluted in the top-level medium.

## Additional Notes

- None found.
