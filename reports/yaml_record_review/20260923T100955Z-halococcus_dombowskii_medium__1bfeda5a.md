# YAML Record Review: halococcus_dombowskii_medium__1bfeda5a

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halococcus_dombowskii_medium__1bfeda5a.yaml`
- Started UTC: 2026-09-23T10:09:55Z
- Finished UTC: 2026-09-23T10:10:31Z
- Verdict: needs curation

## Target

Generated merged YAML for the TOGO `M400` import of `Halococcus Dombowskii Medium`, corresponding to the sea-salts supplement parsed from JCM medium 402.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches TOGO `M400`, original source `JCM_M402-3`, and the same JCM 402 page used by the direct `mediadive.medium:J402` import.
- A gitignore-independent exact search in `data/merge_yaml` and `data/normalized_yaml` found this TOGO identifier only in the expected merged and normalized source record plus TOGO source indexes.
- The chloride salts and Tris base use appropriate CHEBI terms.
- `sea salts (Sigma)` and `Casamino acids (BD-Difco)` are ungrounded, which is acceptable because both are complex branded or product-qualified materials.

## Evidence

- The TOGO API for `M400` carries the same JCM 402 source URL and parses the `10.0 g/L sea salts (Sigma)` comment as an additional ingredient.
- JCM describes the sea-salts addition as a comment specifically for cultivation of `JCM 19729`; the generated ingredient is not scoped to that strain-specific condition.
- JCM instructs the curator to add components to distilled water, bring the volume to 1.0 L, adjust pH to 7.4, and, unless otherwise stated, autoclave at 121 C for 15 min; none of those instructions are present as structured preparation steps in this generated TOGO record.

## Completeness

- Missing pH: the recipe has no `ph_value`, although JCM 402 uses pH 7.4 and the direct MediaDive import preserves it.
- Missing preparation: the source water-to-volume and pH-adjustment steps are absent, along with the default JCM autoclaving instruction.
- Missing variant context: the source sea-salts comment applies to `JCM 19729`; the generated record makes sea salts a plain required ingredient without preserving that strain specificity.
- Water is present only as a `1 G_PER_L` ingredient, which is a TOGO import artifact for a final-volume solvent, not a real mass concentration.

## Findings

1. The solvent is quantitatively wrong. `Distilled water` is represented as `1 G_PER_L`, but the source states a final preparation volume of 1.0 L.
2. The sea-salts supplement is missing its JCM 19729 condition. Treating `sea salts (Sigma)` as an unconditional 10.0 g/L ingredient changes a strain-specific JCM comment into a required component for the whole medium variant.
3. Core preparation semantics are absent. The record lacks pH 7.4, the water-to-1.0-L step, pH adjustment, and the JCM default autoclaving condition.
4. The record is split from the direct JCM 402 and TOGO `M398`/`M399` records instead of being linked as the Sigma sea-salts variant of the same medium family.

## Recommended Edits

- Replace the `1 G_PER_L` water row with the correct final-volume solvent modelling used by curated records.
- Add `ph_value: 7.4`, pH adjustment, and the default JCM autoclaving condition.
- Preserve the `JCM 19729` qualifier on the sea-salts supplement.
- Link this record to the JCM 402 base liquid and solid agar variants rather than leaving it as an unrelated CultureMech recipe.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Verify that Sigma sea salts remains exactly 10.0 g/L and is scoped only to the JCM 19729 supplement.
- Re-run an exact ignored-file-inclusive search for `TOGO:M400` and `JCM_M402-3` to confirm the normalized source and merged record stay synchronized.

## Additional Notes

- Empty optional fields were not treated as defects.
- The TOGO sibling search used `rg --no-ignore --hidden`, so ignored files were included.
