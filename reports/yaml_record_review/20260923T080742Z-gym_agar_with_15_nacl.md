# YAML Record Review: GYM Agar With 15% NaCl

- Repository: CultureMech
- Record: `data/merge_yaml/merged/gym_agar_with_15_nacl.yaml`
- Started UTC: 2026-09-23T08:06:17Z
- Finished UTC: 2026-09-23T08:07:42Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:007571`, `gym_agar_with_15_nacl`, imported from Togo Medium `M1055` / `JCM_M999`.

## Validation

- LinkML validation: passed.
- Strict validation: passed with 0 ERROR rows in `/private/tmp/gym_agar_with_15_nacl.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked: the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record is the Togo view of JCM medium 999: `TOGO:M1055`, `JCM_M999`, and `GYM Agar With 15% NaCl`. Exact ignored-file-inclusive search in `data/normalized_yaml/bacterial` and `data/merge_yaml/merged` also found `data/normalized_yaml/bacterial/gym_agar_with_15_nacl.yaml`, a direct JCM/MediaDive import for the same formula with `mediadive.medium:J999`, `ph_value: 7.2`, a pH-adjustment preparation step, and salinity-variant metadata pointing at the 10% NaCl parent.

The simple ingredients are grounded. `Malt extract (BD-Difco)` and `Yeast extract (BD-Difco)` are ungrounded complex components.

## Evidence

The Togo `M1055` API payload contains one solution with 1 L Distilled water, 150 g NaCl, 2 g CaCO3, 10 g Malt extract, 4 g Glucose, 15 g Agar, and 4 g Yeast extract. It also records `ph: "7.2"` and the comment `Adjust pH to 7.2.`

The generated record preserves all seven Togo ingredient names and mass values, but it drops pH 7.2 and the pH-adjustment comment. The direct JCM/MediaDive normalized parent has the same non-water ingredient concentrations, plus `ph_value: 7.2`, an `ADJUST_PH` preparation step, and curated variant metadata that states the 15% formulation increases NaCl from 100 g/L to 150 g/L while the other GYM agar ingredients remain unchanged.

## Completeness

The ingredient mass concentrations are materially complete, but the generated record is missing the pH target, the pH preparation step, and the JCM parent/variant context. Its 1 L water row is also emitted as a mass concentration.

## Findings

- The Togo pH target is missing. Togo records pH 7.2 and `Adjust pH to 7.2.`, and the direct JCM parent also has `ph_value: 7.2`; the generated record has neither.
- Direct duplicate sources were not grouped. The Togo `JCM_M999` parent and direct JCM/MediaDive `J999` parent describe the same GYM Agar With 15% NaCl formula, but the generated record merged only `TOGO_M1055_GYM_Agar_With_15_NaCl`.
- The curated salinity-variant metadata from the direct JCM parent is absent from the generated Togo record.
- Distilled water is misunitized as `1 G_PER_L` even though Togo records it as 1 L.
- Malt extract and yeast extract remain ungrounded. This is a minor issue for complex components, but they should be checked against available mappings.

## Recommended Edits

- Merge the Togo `M1055` and direct JCM/MediaDive `J999` normalized records as the same JCM medium.
- Preserve pH 7.2 and the pH-adjustment preparation step when regenerating the record.
- Preserve the `SALINITY_VARIANT` relationship to the 10% NaCl GYM parent.
- Correct Togo liter-water handling so 1 L Distilled water is not emitted as `1 G_PER_L`.
- Attempt complex-component groundings for the BD-Difco malt and yeast extracts.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validators after recuration.
- Verify that the regenerated record has both `TOGO:M1055` / `JCM_M999` and `mediadive.medium:J999` provenance, pH 7.2, and the 150 g/L NaCl salinity-variant annotation.

## Additional Notes

Fetching the embedded JCM `GRMD=999` page during review returned a `Nothing found` page, so source verification relied on the Togo API payload and the existing direct JCM/MediaDive normalized record.
