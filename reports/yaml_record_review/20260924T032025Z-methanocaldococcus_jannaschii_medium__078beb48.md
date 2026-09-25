# YAML Record Review: methanocaldococcus_jannaschii_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/methanocaldococcus_jannaschii_medium__078beb48.yaml`
- Started UTC: 2026-09-24T03:20:25Z
- Finished UTC: 2026-09-24T03:20:25Z
- Verdict: needs curation

## Target

- Stable ID: `CultureMech:008846`
- Label: `methanocaldococcus_jannaschii_medium`
- Category: `archaea`
- Maintained owner: `data/normalized_yaml/archaea/TOGO_M225_Methanocaldococcus_Jannaschii_Medium.yaml`
- Source identity: TOGO medium M225, original source JCM medium 232

## Validation

- Open schema: Passed; `linkml-validate` reported no issues.
- Strict validator: Passed; 1 file scanned, 0 files with errors, and 0 error rows.
- Reference validator: Passed; 0 reference checks were applicable.
- Term validator: Passed.
- Embedded history: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

- `media_term` grounds the record to `TOGO:M225`, and the TOGO payload identifies that medium as JCM medium 232.
- Exact ignored-file search for `TOGO_M225_Methanocaldococcus_Jannaschii_Medium`, `TOGO:M225`, `JCM_M232`, `jcm_grmd?GRMD=232`, `methanocaldococcus_jannaschii_medium`, and `CultureMech:008846` confirms that this record is generated from one TOGO source YAML, with no merge-source ambiguity inside this fingerprint.
- The same exact search also found `data/merge_yaml/merged/methanocaldococcus_jannaschii_medium__682e654d.yaml`, a direct JCM 232 generated record for the same named source recipe. This TOGO import therefore appears to duplicate a formula already represented under the direct JCM/MediaDive identity.
- TOGO maps the JCM 232 cross-references to TOGO M142 and TOGO M190, which are the TOGO mirrors of original JCM media 151 and 197 respectively; those cross-reference IDs are plausible, but their solution contents are not encoded.

## Evidence

- The live JCM 232 formula and the TOGO M225 API agree on the core table: 980 ml distilled water, 3.4 g `MgSO4 x 7 H2O`, 30 g NaCl, 0.14 g `CaCl2 x 2 H2O`, 0.25 g NH4Cl, 0.14 g K2HPO4, 2.7 g `MgCl2 x 6 H2O`, 0.5 g `Na2S x 9 H2O`, 0.33 g KCl, 1 g NaHCO3, 0.01 g `Fe(NH4)2(SO4)2 x 6 H2O`, 0.5 g `L-Cysteine HCl x H2O`, 10 ml trace minerals, and 10 ml trace vitamins.
- JCM and TOGO list three milligram-scale entries in the main formula: 1 mg resazurin, 0.75 mg `NiCl2 x 6 H2O`, and 0.5 mg `Na2SeO3 x 5 H2O`.
- JCM points trace minerals to medium 151 and trace vitamins to medium 197; TOGO M142 is original JCM M151 and includes a nested `Trace minerals` solution, while TOGO M190 is original JCM M197 and includes a nested `Trace vitamins` solution.
- JCM 232 instructs the curator to adjust the medium to pH 6.0, boil briefly, cool and dispense under H2/CO2 at 80:20, separately autoclave cysteine and sulfide as 5% solutions under N2, add them before inoculation, and pressurize inoculated bottles to 200 kPa H2/CO2 at 80:20.

## Completeness

- The TOGO source and the live JCM page together provide enough source detail to encode the final medium, the two cross-referenced trace stocks, the pH, and the anaerobic preparation.
- Empty `target_organisms` and `growth_data` are optional-field omissions, not review findings for this record.

## Findings

- Blocker: both cross-referenced stocks are empty stubs. The record stores `Trace minerals (see Medium [M142])` and `Trace vitamins (see Medium [M190])` as `Unknown solution` entries with empty `composition` arrays, so the 10 ml stock additions cannot be reconstructed from the YAML.
- Blocker: the stock additions have volume units in the source but `G_PER_L` in YAML. Each `10 ml` JCM/TOGO cross-reference was migrated to a solution concentration of `10` `G_PER_L`, which changes a stock volume into a mass concentration.
- Blocker: three milligram entries were converted without scaling. Resazurin is recorded as `1` `G_PER_L` instead of approximately `0.001` g/L, `NiCl2 x 6 H2O` as `0.75` `G_PER_L` instead of approximately `0.00075` g/L, and `Na2SeO3 x 5 H2O` as `0.5` `G_PER_L` instead of approximately `0.0005` g/L.
- Major: source pH 6.0 is absent from the generated record.
- Major: all anaerobic preparation is missing, including the H2/CO2 80:20 handling gas, the separate cysteine and sulfide 5% solution sterilization under N2, the overnight standing step, and the final 200 kPa H2/CO2 pressurization.
- Major: `Carbon dioxide gas`, `N2`, and `Hydrogen gas` are top-level variable ingredients rather than preparation/headspace conditions, so the 80:20 H2/CO2 gas ratio and the restricted role of N2 for reductant autoclaving are lost.
- Major: the record is typed as `COMPLEX` and `UNDEFINED`, but JCM 232 is a defined chemical recipe once the M142 trace-minerals and M190 trace-vitamins stocks are resolved.
- Minor: generated output contains a second record for JCM 232 under `methanocaldococcus_jannaschii_medium__682e654d.yaml`; one of the TOGO/direct-JCM copies should be merged or retired after both copies are curated.

## Recommended Edits

- In `data/normalized_yaml/archaea/TOGO_M225_Methanocaldococcus_Jannaschii_Medium.yaml`, replace the two empty `Unknown solution` objects with structured `Trace minerals` and `Trace vitamins` stock additions that retain the 10 ml dosing from JCM 232.
- Populate the trace-minerals stock from the `Trace minerals` subcomponent in TOGO M142/JCM 151 and the trace-vitamins stock from the `Trace vitamins` subcomponent in TOGO M190/JCM 197.
- Convert resazurin, `NiCl2 x 6 H2O`, and `Na2SeO3 x 5 H2O` from source milligrams to final g/L values.
- Add source pH 6.0 and encode the JCM preparation sequence, including H2/CO2 80:20 handling, separate 5% reductant solutions under N2, overnight standing, and final 200 kPa H2/CO2 pressurization.
- Move CO2, H2, and N2 out of top-level ingredients into preparation or atmosphere fields that preserve ratios and use context.
- Change `medium_type` and `composition_type` to the defined-medium values used by the curated direct JCM record if the nested trace stocks contain only defined chemicals.
- Compare this TOGO M225 record against the direct JCM 232 generated record and keep only one canonical generated recipe for the same formula.

## Follow-up Checks

- Rerun open-schema, strict, reference, and term validation after replacing the empty stock stubs.
- Search the regenerated record for `Unknown solution` and confirm neither trace stock remains empty.
- Search the regenerated record for the three milligram-scale ingredients and confirm their numeric values are less than `0.01` g/L.
- Confirm regenerated output no longer contains two active JCM 232 records for `methanocaldococcus_jannaschii_medium`.

## Additional Notes

None found.
