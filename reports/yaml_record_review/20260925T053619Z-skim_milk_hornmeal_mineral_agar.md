# YAML Record Review: skim_milk_hornmeal_mineral_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/skim_milk_hornmeal_mineral_agar.yaml
- Started UTC: 2026-09-25T05:36:19Z
- Finished UTC: 2026-09-25T05:36:19Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:001549`, `skim_milk_hornmeal_mineral_agar`, from `data/merge_yaml/merged/skim_milk_hornmeal_mineral_agar.yaml`.

The target record is a direct MediaDive/DSMZ import for DSMZ medium 440, `SKIM MILK-HORNMEAL-MINERAL AGAR`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to DSMZ medium 440.

No same-source duplicate was found in the sorted generated YAML list.

## Evidence

The DSMZ medium 440 PDF and MediaDive REST payload define a final agar medium with skim milk powder, bovine horn meal, Ca(NO3)2 x 4H2O, MgSO4 x 7H2O, K2HPO4, NaHCO3, FeCl3, agar, and 900 ml distilled water.

The DSMZ preparation text autoclaves the skim milk powder separately in 100 ml H2O and adds it to the cooled 60 C agar medium.

## Completeness

The generated record preserves all non-water ingredient amounts from DSMZ 440.

The 900 ml distilled water row for the agar phase is absent.

The separate 100 ml H2O for skim milk is retained only in preparation text, which is acceptable because it is scoped to the separate skim-milk autoclave step.

## Findings

The final distilled-water solvent row was dropped during import.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/skim_milk_hornmeal_mineral_agar.yaml` to include the 900 ml distilled water row from DSMZ medium 440.

Keep the 100 ml skim-milk water in the existing preparation step rather than adding it as a top-level ingredient.

Regenerate the merged YAML after repairing the normalized source.

## Follow-up Checks

Confirm the regenerated record has 900 ml/L distilled water.

Confirm the existing skim-milk preparation text remains present.

Confirm the solid agar state remains present.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
