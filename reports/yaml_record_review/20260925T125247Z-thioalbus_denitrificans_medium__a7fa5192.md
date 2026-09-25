# YAML Record Review: thioalbus_denitrificans_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thioalbus_denitrificans_medium__a7fa5192.yaml
- Started UTC: 2026-09-25T12:53:11Z
- Finished UTC: 2026-09-25T12:53:35Z
- Verdict: needs curation

## Target

- Generated YAML for the direct JCM/MediaDive J721 THIOALBUS DENITRIFICANS MEDIUM import.
- The record was merged from `thioalbus_denitrificans_medium`.
- The checked sources were MediaDive J721 and the JCM 721 medium page.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to JCM/MediaDive J721, THIOALBUS DENITRIFICANS MEDIUM.
- The JCM page lists the same JCM 721 medium name and pH 7.5 preparation.
- No conflicting duplicate merge was observed.

## Evidence

- JCM 721 lists a basal medium containing 20 g NaCl, 0.4 g MgCl2 x 6 H2O, 0.1 g CaCl2 x 2 H2O, 0.2 g NH4Cl, 1 g KH2PO4, 0.5 g KCl, 0.1 g yeast extract, and 1000 ml distilled water.
- After autoclaving, JCM 721 adds 1 ml vitamin solution, 1 ml trace element solution, 5 ml 8% NaHCO3 solution, 5 ml 1 M NaNO3 solution, and 5 ml 1 M Na2S2O3 solution per liter.
- MediaDive represents the final main solution volume as 1017 ml and scales the basal salts to that final volume.

## Completeness

- The pH 7.5 preparation text, anaerobic handling, and post-autoclave additions are partially preserved.
- Vitamin-solution compounds and trace-element compounds are flattened into top-level ingredients at stock concentrations.
- The 8% bicarbonate, 1 M nitrate, and 1 M thiosulfate additions are represented as 5 g/L NaHCO3, 5 g/L NaNO3, and 5 g/L Na2S2O3 rather than as stock additions or calculated final molar concentrations.
- `Sodium phosphate buffer` is imported as 100 g/L, but the MediaDive row is the 100 ml volume of 10 mM pH 7.1 buffer used to prepare the vitamin stock.

## Findings

- The generated record overstates every vitamin- and trace-stock component by treating stock-solution concentrations as final medium concentrations.
- The `Sodium phosphate buffer` amount is unit-swapped from a buffer volume into 100 g/L.
- HCl is represented as 12.5 g/L final HCl even though JCM 439 uses 12.5 ml of 25% HCl inside a 1 L trace-element stock.
- The post-autoclave 8% and 1 M stock additions are flattened in a way that loses their source stock concentration and dilution context.

## Recommended Edits

- Model JCM 721 as a main solution plus vitamin, trace, bicarbonate, nitrate, and thiosulfate stock additions with their source volumes.
- Recompute final ingredient concentrations only after applying the 1017 ml final-volume dilution.
- Replace the imported `Sodium phosphate buffer` concentration with stock-solution structure or remove it from the final recipe.
- Keep the JCM pH and anaerobic autoclaving text attached to the parent medium.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Confirm JCM 403 and JCM 439 stock recipes if the stock contents are expanded rather than referenced.
- Verify no exact JCM 721 direct import is re-merged with stock-solution definitions during regeneration.

## Additional Notes

- None found.
