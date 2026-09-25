# YAML Record Review: thiobacillus_cuprinus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thiobacillus_cuprinus_medium.yaml
- Started UTC: 2026-09-25T12:57:16Z
- Finished UTC: 2026-09-25T12:57:40Z
- Verdict: needs curation

## Target

- Generated YAML for the KOMODO 493 THIOBACILLUS CUPRINUS MEDIUM record enriched from DSMZ 493.
- The record was merged from `thiobacillus_cuprinus_medium`.
- The checked sources were the local KOMODO 493 enrichment metadata, MediaDive 493, and DSMZ Medium 493.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to KOMODO 493, THIOBACILLUS CUPRINUS MEDIUM.
- The notes map KOMODO 493 to DSMZ 493.
- DSMZ/MediaDive 493 identifies the exact DSMZ formulation as a Thiomonas H5 medium, and a separate exact DSMZ 493 normalized record exists as `thiomonas_h_5_medium`.

## Evidence

- DSMZ 493 lists a 1012 ml final volume with basal salts, 2 ml 0.1% NiCl2 x 6 H2O, 10 ml Modified Wolin's mineral solution, 0.5 g yeast extract, and 1000 ml distilled water.
- DSMZ 493 says to dissolve ingredients except yeast extract, adjust to pH 3.5 with sulfuric acid, autoclave, and add yeast extract from a sterile stock solution.
- The Modified Wolin's mineral solution is a separate 1 L stock.

## Completeness

- The pH 3.5 value and many DSMZ 493 ingredient names are present.
- Ingredients shared by the final recipe and the Modified Wolin's mineral stock have been summed, including `MgSO4 x 7 H2O`, `CaCl2 x 2 H2O`, `NaCl`, and `NiCl2 x 6 H2O`.
- The Modified Wolin's mineral stock is flattened at stock strength even though only 10 ml is added.
- The source water row and DSMZ preparation instruction are missing.

## Findings

- The record identity is inconsistent: the YAML keeps the KOMODO Thiobacillus cuprinus name while the copied DSMZ 493 source is a Thiomonas H5 medium.
- Merged duplicate rows combine basal-medium ingredients with stock-solution ingredients and overstate final `MgSO4 x 7 H2O`, `CaCl2 x 2 H2O`, `NaCl`, and `NiCl2 x 6 H2O`.
- Most Modified Wolin's mineral solution components are represented as final g/L values instead of a 10 ml/L stock addition.
- DSMZ 493's source preparation text and 1000 ml distilled-water row are omitted.

## Recommended Edits

- Reconcile KOMODO 493 with the direct DSMZ 493 `thiomonas_h_5_medium` record before treating this as a distinct Thiobacillus cuprinus medium.
- Preserve the DSMZ 493 main solution, 2 ml 0.1% nickel chloride addition, 10 ml Modified Wolin's stock addition, and sterile yeast-extract addition separately.
- Remove duplicate sums created across the parent medium and the stock solution.
- Restore the DSMZ water row and preparation instruction.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify exact KOMODO 493 and DSMZ 493 normalized records before deciding whether to merge, alias, or split them.
- Check that Modified Wolin's mineral solution is either explicitly referenced or diluted before final concentrations are stored.

## Additional Notes

- None found.
