# YAML Record Review: halodesulfovibrio_postgate_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halodesulfovibrio_postgate_medium.yaml`
- Started UTC: 2026-09-23T10:16:17Z
- Finished UTC: 2026-09-23T10:18:29Z
- Verdict: needs curation

## Target

Generated merged YAML for DSMZ medium 163, `HALODESULFOVIBRIO (POSTGATE) MEDIUM`, after duplicate merging with DSMZ/KOMODO medium 410 records.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The top-level record claims `mediadive.medium:163` / DSMZ 163 identity, but its NaCl concentration comes from the lower-salt DSMZ 410 brackish recipe.
- An ignored-file-inclusive exact search for `mediadive.medium:163`, `mediadive.medium:410`, `komodo.medium:163`, `komodo.medium:410`, and the two DSMZ PDF names found the four merged source records plus one separate `medium_163_modified_for_dsm_10520` DSMZ 163 derivative.
- The hydrate-sensitive sulfate and chloride salt groundings are appropriate.
- The merge history also preserves a `SALINITY_VARIANT` relationship in the normalized sources, which conflicts with the generated merged record's treatment of the brackish and marine recipes as source duplicates.

## Evidence

- DSMZ 163 uses Solution A at 980 ml, Solution B at 10 ml, and Solution C at 10 ml; its Solution A contains 25.00 g NaCl and the final medium pH is 6.8-7.0.
- DSMZ 410 uses the same A/B/C stock layout but contains 10.00 g NaCl in Solution A and adjusts to pH 7.8.
- MediaDive reports Solution B as 0.5 g FeSO4 x 7 H2O in 10 ml and Solution C as 0.1 g Na-thioglycolate plus 0.1 g Ascorbic acid in 10 ml; those stocks are dosed into the 1 L main solution at 10 ml each.

## Completeness

- Missing stock structure: the generated flat recipe does not represent Solutions A, B, and C or their 980 ml/10 ml/10 ml assembly volumes.
- Missing water: all three solution water rows were dropped.
- Missing DSMZ 163 conditional instructions for DSM 10520 and DSM 15630.
- Missing anaerobic equipment and atmosphere structure: gassing under N2 and distribution into anoxic Hungate tubes are present only as prose inside a single `AUTOCLAVE` step.

## Findings

1. Marine DSMZ 163 and brackish DSMZ 410 were merged despite different NaCl and pH. The generated record is labelled as DSMZ 163 and keeps the DSMZ 163 pH range of 6.8-7.0, but it carries the DSMZ 410 NaCl concentration of 10.2041 g/L rather than the DSMZ 163 marine value derived from 25 g in Solution A.
2. Solution B and C stock concentrations were flattened as final medium concentrations. FeSO4 x 7 H2O appears as 50 g/L instead of a 10 ml/L addition from a 0.5 g/10 ml stock, and Na-thioglycolate plus Ascorbic acid appear as 10 g/L instead of 10 ml/L additions from 0.1 g/10 ml stocks.
3. Solution A components were converted from stock-solution g/L values instead of direct final-medium gram amounts. K2HPO4, NH4Cl, Na2SO4, CaCl2 x 2 H2O, MgSO4 x 7 H2O, Na-DL-lactate, and Yeast extract are inflated by 1/0.98 relative to the 1 L final medium.
4. DSMZ 163 source notes for DSM 10520 and DSM 15630 are absent, so strain-specific pH/carbonate/gas and post-sterilization Bacto peptone supplements were lost.

## Recommended Edits

- Split DSMZ 163 and DSMZ 410 back into distinct salinity/pH variants linked by `SALINITY_VARIANT`, not `SOURCE_DUPLICATE`.
- Represent Solutions A, B, and C as named stocks or scale every solute to its true final-medium amount before flattening.
- Restore each solution's distilled water row and the 980 ml/10 ml/10 ml assembly proportions.
- Preserve anaerobic N2 sparging, Hungate distribution, and autoclaving as separate structured preparation semantics.
- Add DSMZ 163 strain-specific follow-on variants or notes for DSM 10520 and DSM 15630.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Verify DSMZ 163 keeps 25 g NaCl in Solution A and final pH 6.8-7.0 while DSMZ 410 keeps 10 g NaCl in Solution A and pH 7.8.
- Confirm the generated merge no longer collapses `mediadive.medium:163` and `mediadive.medium:410` into one fingerprint.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
