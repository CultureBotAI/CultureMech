# YAML Record Review: gauzes_synthetic_medium_no_1_with_18_nacl

- Repository: CultureMech
- Record: data/merge_yaml/merged/gauzes_synthetic_medium_no_1_with_18_nacl.yaml
- Started UTC: 2026-09-23T05:33:19Z
- Finished UTC: 2026-09-23T05:35:28Z
- Verdict: needs curation

## Target

Generated CultureMech:010341 is the TOGO/JCM solid high-salt Gauze synthetic medium variant named "Gauze's Synthetic Medium NO. 1 With 18% NaCl". It is grounded to TOGO:M920, the JCM_M879-2 agar form of JCM 879.

## Validation

`linkml-validate` passed against `MediaRecipe`.

`scripts/validate_strict.py` passed with 0 error rows.

`linkml-reference-validator` passed with 0 checks.

`linkml-term-validator` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The target identity is correct for TOGO:M920/JCM_M879-2, but the merge attached the low-salt parent `TOGO_M72_Gauze_s_Synthetic_Medium_NO._1` to the same generated record and made M72 a synonym/source. M920 is a concentration variant of M72, not a duplicate of it.

The generated `variant_modifications` text correctly says the child increases NaCl from 0.5 g/L to 180 g/L, lowers FeSO4 from 10 g/L to 0.01 g/L, and changes agar from 15 g/L to 18 g/L, but the actual generated ingredient rows still use the parent 0.5 g/L NaCl, 10 g/L FeSO4, and 15 g/L agar values.

The normalized MediaDive/JCM record for J879 represents the same high-salt basal medium with pH 7.1 and a preparation note for 18 g/L agar in the solid form. That direct source is absent from `merged_from`, so the generated record only merges the low-salt TOGO M72 parent and the solid high-salt TOGO M920 child.

## Evidence

JCM medium 879 lists 20.0 g soluble starch, 180.0 g NaCl, 1.0 g KNO3, 0.5 g K2HPO4, 0.5 g MgSO4 x 7H2O, and 0.01 g FeSO4 x 7H2O, then says to bring the volume to 1.0 L, adjust pH to 7.0-7.2, and add 18.0 g/L agar for solid medium.

MediaDive J879 has the same six base salts/carbon source amounts, a fixed pH of 7.1, and the same three preparation steps.

The normalized TOGO M920 source already carries the correct high-salt solid values: 180 g/L NaCl, 0.01 g/L FeSO4 x 7H2O, and 18 g/L agar. Its TOGO M919 sibling has the same liquid recipe without agar.

The generated merged YAML instead contains TOGO M72's low-salt 0.5 g/L NaCl, 10 g/L FeSO4 x 7H2O, and 15 g/L agar while retaining the high-salt medium name, `media_term`, and parent-media notes.

## Completeness

The generated record omits the JCM/MediaDive pH range and preparation steps:

- Add components to distilled water and bring volume to 1.0 L.
- Adjust pH to 7.0-7.2.
- Add 18.0 g/L agar for solid medium.
- Autoclave at 121 C for 15 min unless otherwise stated, per JCM's page-level instruction.

The direct JCM/MediaDive normalized record for J879 is not merged into the generated high-salt record, which makes the generated evidence set incomplete even before the parent/child ingredient conflict is considered.

## Findings

- Major: The generated record merges the low-salt M72 parent as if it were a duplicate of the 18% NaCl M920 child, so `synonyms` and `merged_from` overstate identity equivalence.
- Major: The NaCl row is 0.5 g/L from M72, but JCM 879, MediaDive J879, TOGO M919, and TOGO M920 all specify 180 g/L for the high-salt variant.
- Major: The FeSO4 x 7H2O row is 10 g/L from M72, but the high-salt JCM/TOGO records specify 0.01 g/L. This makes `high_metal: true` an artifact of the bad parent value.
- Major: The agar row is 15 g/L from M72; the M920/JCM solid variant specifies 18 g/L.
- Major: Distilled water is encoded as 1 g/L even though TOGO encodes a 1 L final volume and JCM says to bring components to 1.0 L.
- Major: `ph_value` 7.1 and the JCM preparation steps are absent.
- Minor: The KNO3 row still has the stale `mediaingredientmech_term` mapping instead of a CHEBI-keyed `mediaingredientmech_chebi_term`.

## Recommended Edits

- Prevent the merger from treating `TOGO_M72_Gauze_s_Synthetic_Medium_NO._1` as an equivalent duplicate of `TOGO_M920_Gauze_s_Synthetic_Medium_NO._1_With_18_NaCl`; preserve M72 only as the `CONCENTRATION_VARIANT` parent.
- Merge the normalized MediaDive/JCM J879 high-salt source with TOGO M919/M920 instead of leaving J879 as an unmerged same-name record.
- Regenerate the M920 solid record with 180 g/L NaCl, 0.01 g/L FeSO4 x 7H2O, 18 g/L agar, and the JCM pH/preparation metadata.
- Represent TOGO's 1 L distilled-water row as final-volume context, not as a 1 g/L solute.
- Refresh the KNO3 MediaIngredientMech link to the CHEBI-keyed form.

## Follow-up Checks

- After merge repair, confirm that the M72 low-salt record and M920 high-salt record have different ingredient amounts and different merge fingerprints.
- Confirm that the M919 liquid high-salt form and M920 solid high-salt form remain separate or are joined only with explicit solid/liquid variant structure.
- Re-run strict, reference, term, and LinkML validation on regenerated `gauzes_synthetic_medium_no_1_with_18_nacl.yaml`.

## Additional Notes

None found
