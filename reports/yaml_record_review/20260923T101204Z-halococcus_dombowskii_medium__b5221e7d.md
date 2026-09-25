# YAML Record Review: halococcus_dombowskii_medium__b5221e7d

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halococcus_dombowskii_medium__b5221e7d.yaml`
- Started UTC: 2026-09-23T10:12:04Z
- Finished UTC: 2026-09-23T10:12:40Z
- Verdict: needs curation

## Target

Generated merged YAML for the TOGO `M399` import of `Halococcus Dombowskii Medium`, corresponding to the 20.0 g/L agar solid-medium variant parsed from JCM medium 402.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed; `/private/tmp/halococcus_dombowskii_medium__b5221e7d.strict.tsv` contained only the header row.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches TOGO `M399`, original source `JCM_M402-2`, and the solid-medium note from JCM 402.
- A gitignore-independent exact search in `data/merge_yaml` and `data/normalized_yaml` found this TOGO identifier only in the expected merged and normalized source record plus TOGO source indexes.
- The agar ingredient is present at 20 g/L, matching the JCM solid-medium comment.
- Hydrated calcium and magnesium chloride salts are grounded to hydrate-specific CHEBI terms.

## Evidence

- The JCM 402 page lists the base Halococcus dombowskii liquid recipe, then states that 20.0 g/L agar should be added to prepare solid medium.
- TOGO `M399` parses this comment as an agar-containing variant and includes the same core medium ingredients plus agar.
- The generated record has no `ph_value` and no `preparation_steps`, even though JCM states pH 7.4, water to 1.0 L, pH adjustment, and the default 121 C for 15 min autoclaving condition.

## Completeness

- Missing pH: the solid variant should retain pH 7.4 from JCM 402.
- Missing preparation: the 1.0 L final-volume, pH-adjustment, and default autoclaving steps are absent.
- Water is present only as a `1 G_PER_L` ingredient, a unit artifact inherited from TOGO's 1 L solvent row.
- Missing relationship: this solid agar recipe is split from the direct JCM 402 base recipe and the TOGO `M398` base parse.

## Findings

1. `Distilled water` is encoded with the wrong unit. The source is a 1.0 L final-volume instruction, not 1 g/L water.
2. Required preparation details were dropped. This record lacks the source pH 7.4 adjustment and the JCM default autoclaving condition.
3. The solid-medium variant is isolated from the JCM 402 base recipe. The agar addition is a variant of the base liquid formula, but the generated record has no relation to the base recipe or to the direct `mediadive.medium:J402` import.

## Recommended Edits

- Replace the water mass-concentration artifact with the correct final-volume solvent modelling.
- Add `ph_value: 7.4`, pH adjustment, and default JCM autoclaving.
- Link TOGO `M399` as the solid agar form of the JCM 402 base rather than leaving it as a standalone duplicate.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Verify that agar remains a 20.0 g/L solidifying ingredient and the recipe keeps `physical_state: SOLID_AGAR`.
- Re-run an ignored-file-inclusive exact search for `TOGO:M399` and `JCM_M402-2` to confirm all normalized and merged copies agree after the source edit and merge.

## Additional Notes

- Empty optional fields were not treated as defects.
- The TOGO source search used `rg --no-ignore --hidden`, so ignored files were included.
