# YAML Record Review: halophilic_sob_medium__78b818a0

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halophilic_sob_medium__78b818a0.yaml`
- Started UTC: 2026-09-23T11:02:25Z
- Finished UTC: 2026-09-23T11:03:28Z
- Verdict: needs curation

## Target

Generated merged YAML for Togo Medium M1063, `Halophilic SOB Medium`, imported from JCM medium 1006.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches Togo `TOGO:M1063`, which points to JCM medium 1006.
- An ignored-file-inclusive exact search for `TOGO:M1063`, `medium/M1063`, `JCM_M1006`, `jcm_grmd?GRMD=1006`, and `halophilic_sob_medium` found this Togo M1063 import, the direct MediaDive/JCM J1006 import, and their two merged outputs.
- The core salt and trace-metal groundings are mostly appropriate.
- CoCl2 x 6 H2O and NiCl2 x 6 H2O are grounded too broadly to generic cobalt and nickel chlorides and need hydrate-specific terms.

## Evidence

- Togo M1063 preserves the source pH target as `7.5`.
- Togo M1063 has a 1 L main solution with MgSO4 x 7 H2O, NaCl, CaCl2 x 2 H2O, KCl, ammonium sulfate, and distilled water.
- The source calls for autoclaving the main solution, then aseptically adding 10 ml 1 M NaHCO3, 5 ml 1 M NH4Cl, 3 ml 1 M K2HPO4, 20 ml 1 M Na2S2O3, 1 ml 0.5 M EDTA, 0.06 ml trace metal solution, 0.06 ml trace vitamins, and 6 ul vitamin B12 solution.
- The trace-metal solution is a separate 1 L stock that starts with 1 ml 32% HCl, contains FeCl2 x 4 H2O and eight trace salts, and is transferred into the main solution at only 0.06 ml.
- The generated record flattened trace-metal stock components into the top-level ingredient list and converted the eight post-autoclave additions to empty `solutions` with `G_PER_L` concentrations.

## Completeness

- Missing pH: the generated record has no `ph_value: 7.5`.
- Mis-scaled water: the two scoped 1 L water rows collapsed to a single `2.0 G_PER_L` artifact.
- Missing topology: post-autoclave molar solutions, trace vitamins, vitamin B12, and trace metal solution transfer volumes are not represented.
- Missing preparation: autoclaving, aseptic addition, filter sterilization, and pH adjustment are all absent.
- Misplaced trace stock: trace-metal stock components are top-level ingredients at stock concentration.

## Findings

1. The generated Togo M1063 record omits the source pH target of 7.5.
2. Main-solution and trace-metal-stock water were collapsed to `2.0 G_PER_L`.
3. The 10 ml, 5 ml, 3 ml, 20 ml, 1 ml, 0.06 ml, 0.06 ml, and 6 ul additions became empty gram-per-liter solution placeholders.
4. Trace-metal-stock components were flattened into top-level ingredients instead of being scoped under the 0.06 ml trace metal solution.
5. Autoclaving, aseptic addition, filter sterilization, and pH-adjustment instructions are missing.
6. CoCl2 x 6 H2O and NiCl2 x 6 H2O need hydrate-specific groundings.

## Recommended Edits

- Add `ph_value: 7.5`.
- Preserve the main and trace-metal-stock recipes as scoped 1 L solutions with their own water rows.
- Model the eight post-autoclave additions with their milliliter or microliter transfer volumes.
- Restore preparation steps for autoclaving, aseptic solution addition, filter sterilization of starred solutions, and pH adjustment.
- Re-ground CoCl2 x 6 H2O and NiCl2 x 6 H2O to hydrate-specific terms.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Re-run an ignored-file-inclusive exact search for `TOGO:M1063`, `mediadive.medium:J1006`, and `JCM_M1006` after regeneration.
- Verify that regenerated Togo M1063 reconciles with the direct JCM J1006 import without flattening trace stocks into the main recipe.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
- A live fetch of the current JCM GRMD 1006 page returned `Nothing found`; the Togo payload and existing direct JCM J1006 import retained the older source structure used for this review.
