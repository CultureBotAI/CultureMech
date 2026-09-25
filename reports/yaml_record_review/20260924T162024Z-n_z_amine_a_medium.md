# YAML Record Review: n_z_amine_a_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/n_z_amine_a_medium.yaml
- Started UTC: 2026-09-24T16:19:08Z
- Finished UTC: 2026-09-24T16:20:24Z
- Verdict: needs curation

## Target

Reviewed the generated MediaRecipe `CultureMech:010127` for
`n_z_amine_a_medium`, a TOGO import grounded to `TOGO:M71`.

## Validation

Focused validation passed:

- LinkML `MediaRecipe` validation: passed; no issues found.
- Strict validation: passed with zero error rows in `/private/tmp/n_z_amine_a_medium.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The TOGO identity is internally consistent. `TOGO:M71` is `N-Z Amine A Medium`,
cites original source `JCM_M80`, and points to the JCM `GRMD=80` page.

An exact ignored-inclusive search across `data/normalized_yaml`,
`data/merge_yaml/merged`, and top-level `data/*.tsv` files also found
`CultureMech:003155`, the active direct JCM `mediadive.medium:J80` owner for
the same `GRMD=80` source. That JCM owner is generated separately as
`data/merge_yaml/merged/n_z_amine_a_medium__74b0c3f4.yaml`.

## Evidence

The live JCM `GRMD=80` page lists:

- 5 g N-Z amine, type A (Sheffield)
- 1 g Beef extract (BD-Difco)
- 80 ml Glycerol
- 15 g Agar
- 1 L Distilled water

JCM also gives the default instruction to autoclave at 121 C for 15 minutes
unless a medium states otherwise. The live TOGO `M71` API mirrors the same five
ingredients from `JCM_M80` and has no additional pH or preparation comment.

## Completeness

The generated TOGO record has all five source ingredient names, but it does not
preserve the two liquid source units. It stores `Distilled water` as `1 G_PER_L`
and `Glycerol` as `80 G_PER_L` even though JCM and TOGO give 1 L water and
80 ml glycerol.

The direct JCM duplicate has a different import artifact: it omits the water
row and scales 5 g N-Z amine, 1 g beef extract, and 15 g agar down to
4.62963, 0.925926, and 13.8889 g/L respectively, apparently dividing by
1.08 L after adding the 80 ml glycerol volume.

## Findings

1. `Distilled water` is modeled as `1 G_PER_L` instead of 1 L.

2. `Glycerol` is modeled as `80 G_PER_L` instead of 80 ml.

3. The default JCM autoclave instruction, 121 C for 15 minutes, is missing.

4. The equivalent direct JCM `GRMD=80` owner remains active and generated as a
   separate independent record.

5. The direct JCM duplicate is also source-inaccurate because it drops water
   and rescales dry weights against the glycerol volume.

## Recommended Edits

Repair and reconcile both normalized owners:

- Correct TOGO M71 water to 1 L and glycerol to 80 ml.
- Add the default JCM autoclave step.
- Repair the direct JCM J80 owner so its dry ingredient amounts match the JCM
  table and its water and glycerol rows preserve their source liquid units.
- Link TOGO M71 and JCM J80 as source duplicates so regeneration does not keep
  two independent generated records for JCM 80.

## Follow-up Checks

- Re-fetch TOGO `M71` and JCM `GRMD=80` and compare every ingredient row after
  repair.
- Regenerate `data/merge_yaml/merged` and confirm the TOGO and direct JCM
  owners merge or link as source duplicates.
- Re-run LinkML, strict, reference, and term validation on the regenerated
  record.

## Additional Notes

None found.
