# YAML Record Review: n_z_amine_with_soluble_starch_and_glucose

- Repository: CultureMech
- Record: data/merge_yaml/merged/n_z_amine_with_soluble_starch_and_glucose.yaml
- Started UTC: 2026-09-24T16:25:15Z
- Finished UTC: 2026-09-24T16:26:14Z
- Verdict: needs curation

## Target

Reviewed the generated MediaRecipe `CultureMech:009822` for
`n_z_amine_with_soluble_starch_and_glucose`, a TOGO import grounded to
`TOGO:M437`.

## Validation

Focused validation passed:

- LinkML `MediaRecipe` validation: passed; no issues found.
- Strict validation: passed with zero error rows in `/private/tmp/n_z_amine_with_soluble_starch_and_glucose.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The TOGO identity is internally consistent: `TOGO:M437` is a mirror of JCM
`GRMD=437`, `N-Z AMINE WITH SOLUBLE STARCH AND GLUCOSE`.

An exact ignored-inclusive search across `data/normalized_yaml`,
`data/merge_yaml/merged`, and top-level `data/*.tsv` files found the active
direct JCM owner `CultureMech:002788` for the same source. That direct owner is
currently merged into the DSMZ 554/KOMODO 554 generated family even though JCM
437 has a different agar amount.

## Evidence

The live JCM `GRMD=437` page lists:

- 10 g Glucose
- 20 g Soluble starch
- 5 g Yeast extract
- 5 g N-Z Amine, type A (Sheffield)
- 1 g CaCO3
- 15 g Agar
- 1 L Distilled water

JCM also says to adjust pH to 7.2. The live TOGO `M437` API mirrors those seven
source rows and the pH-adjustment comment.

## Completeness

The generated TOGO record has all seven ingredient names, including the source
15 g agar row. It does not preserve distilled water's source unit: JCM and TOGO
give 1 L, while generated YAML has `1 G_PER_L`.

The generated record also drops pH 7.2 and the pH-adjustment step. The
equivalent direct JCM record preserves `ph_value: 7.2` and a pH-adjustment
step, but drops the water row. Neither JCM 437 owner is fully source-faithful.

## Findings

1. `Distilled water` is modeled as `1 G_PER_L` instead of 1 L.

2. The source pH 7.2 and `Adjust pH to 7.2.` instruction are missing.

3. The equivalent direct JCM `GRMD=437` owner is active but not linked to this
   TOGO mirror.

4. The direct JCM owner was also incorrectly folded into the DSMZ 554 generated
   family even though DSMZ 554 and JCM 437 need agar reconciliation before any
   merge.

## Recommended Edits

Repair and reconcile the JCM 437 family:

- Correct TOGO M437 `Distilled water` to a 1 L addition.
- Preserve pH 7.2 and the pH-adjustment step.
- Add the missing water row to the direct JCM J437 owner.
- Link TOGO M437 and direct JCM J437 as source duplicates.
- Keep the JCM 437 family separate from DSMZ 554 until the DSMZ 554 15 g versus
  20 g agar conflict is explicitly adjudicated.

## Follow-up Checks

- Re-fetch TOGO `M437` and JCM `GRMD=437` after repair and confirm all seven
  source rows and pH 7.2 are represented.
- Regenerate merged YAML and confirm the JCM 437 owners merge with each other,
  not with an unresolved DSMZ 554 20 g/L agar record.
- Re-run LinkML, strict, reference, and term validation on the regenerated
  record.

## Additional Notes

None found.
