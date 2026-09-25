# YAML Record Review: Sulfurisphaera Medium (pH 5.0)

- Repository: CultureMech
- Record: data/merge_yaml/merged/sulfurisphaera_medium_ph_5_0.yaml
- Started UTC: 2026-09-25T08:40:31Z
- Finished UTC: 2026-09-25T08:42:49Z
- Verdict: needs curation

## Target

- Reviewed generated record `CultureMech:008215` in `data/merge_yaml/merged/sulfurisphaera_medium_ph_5_0.yaml`.
- Canonical source: `data/normalized_yaml/archaea/sulfurisphaera_medium_ph_5_0.yaml`.
- Merged source: `data/normalized_yaml/archaea/sulfurisphaera_medium_ph_2_5.yaml`.
- Canonical media term: `TOGO:M1658`, `Sulfurisphaera Medium (pH 5.0)`.
- Merged synonym media term: `TOGO:M1657`, `Sulfurisphaera Medium (pH 2.5)`.
- Merge fingerprint: `93c5db9fdcc006bd07f0bc78b32dbf5e101d4f6cdadbc37ce74d3e57e4e2fceb`.

## Validation

- LinkML schema validation passed: `No issues found`.
- Strict validation passed with 0 error rows.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

- The canonical source is TOGO `M1658`, derived from NBRC medium 862, `Sulfurisphaera Medium (pH 5.0)`.
- The merged synonym is TOGO `M1657`, derived from NBRC medium 861, `Sulfurisphaera Medium (pH 2.5)`.
- Exact ignored-file-inclusive searches found `CultureMech:008215`, `TOGO:M1658`, `TOGO:M1657`, `source_id: TOGO:M1657`, and the `93c5db9fdcc006bd07f0bc78b32dbf5e101d4f6cdadbc37ce74d3e57e4e2fceb` fingerprint in the generated record or normalized sources at expected locations.
- NBRC 861 and 862 confirm that the two media use the same base composition but differ by the explicit final pH and H2SO4 adjustment target.

## Evidence

- NBRC 862 lists `Sulfurisphaera Medium (pH 5.0)` with a final `pH 5.0` line and the instruction to adjust pH to 5.0 with H2SO4 before autoclaving.
- NBRC 861 lists `Sulfurisphaera Medium (pH 2.5)` with a final `pH 2.5` line and the instruction to adjust pH to 2.5 with H2SO4 before autoclaving.
- TOGO M1658 and M1657 reproduce the same pH-specific comments from NBRC 862 and 861.
- The source formulas include milligram-scale trace salts: 1.8 mg MnCl2 x 4 H2O, 4.5 mg Na2B4O7 x 10 H2O, 0.22 mg ZnSO4 x 7 H2O, 0.05 mg CuCl2 x 2 H2O, 0.03 mg Na2MoO4 x 2 H2O, 0.03 mg VOSO4 x nH2O, and 0.01 mg CoSO4 x 7 H2O per liter.
- Both NBRC records instruct curators to mix all ingredients except Bacto Yeast Extract, adjust pH with H2SO4, autoclave at 121C for 15 min, separately autoclave Bacto Yeast Extract as a 10% solution, and add the yeast extract solution before inoculation.

## Completeness

- The generated record preserves the TOGO M1658 canonical identity, TOGO M1657 as a synonym, the NBRC 862 and 861 source names through `merged_from`, and the shared ingredient names.
- The generated record does not preserve pH 5.0 or pH 2.5 as a structured `ph_value`, `ph_range`, or preparation step.
- The Bacto Yeast Extract separate-autoclave instruction is absent from the generated record.

## Findings

- The merge conflates two intentional pH variants. NBRC 861 and 862 differ by final pH 2.5 versus pH 5.0 and should remain distinct records or be represented as pH variants, not collapsed into a single source duplicate.
- The pH-specific H2SO4 adjustment was lost. The generated record keeps `H2SO4` as a variable ingredient but carries neither the pH 5.0 canonical target nor the pH 2.5 synonym target.
- TOGO milligram quantities were converted as if they were gram quantities. For example, 1.8 mg MnCl2 x 4 H2O became `1.8` `G_PER_L`, 4.5 mg Na2B4O7 x 10 H2O became `4.5` `G_PER_L`, and 0.01 mg CoSO4 x 7 H2O became `0.01` `G_PER_L`.
- The generated record is missing NBRC's Bacto Yeast Extract preparation requirement.

## Recommended Edits

- Split `sulfurisphaera_medium_ph_2_5.yaml` and `sulfurisphaera_medium_ph_5_0.yaml` back into pH-specific generated records, or model them with an explicit pH variant relationship that preserves both target pH values.
- Fix the TOGO import path so `mg` values are converted to `G_PER_L` by dividing by 1000 before normalizing per liter.
- Convert the `pH 5.0` and `pH 2.5` source comments into source-specific `ph_value` entries and H2SO4 pH-adjustment preparation steps.
- Preserve the separate 10% Bacto Yeast Extract autoclave/addition step from NBRC.
- Regenerate `data/merge_yaml/merged/sulfurisphaera_medium_ph_5_0.yaml`; do not hand-edit this generated file.

## Follow-up Checks

- Revalidate the two normalized TOGO/NBRC sources after milligram conversion and pH extraction fixes.
- Regenerate merged YAML and verify that NBRC 861 and 862 no longer collapse into one indistinguishable duplicate.
- Verify that milligram trace salts such as MnCl2 x 4 H2O and Na2B4O7 x 10 H2O are three orders of magnitude lower than their current generated values.

## Additional Notes

- Empty optional fields were not treated as defects.
- NBRC 861 and 862 were checked directly after comparing TOGO M1657 and M1658.
