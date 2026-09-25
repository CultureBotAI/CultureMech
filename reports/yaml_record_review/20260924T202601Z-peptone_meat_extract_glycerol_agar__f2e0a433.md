# YAML Record Review: peptone_meat_extract_glycerol_agar__f2e0a433

- Repository: CultureMech
- Record: data/merge_yaml/merged/peptone_meat_extract_glycerol_agar__f2e0a433.yaml
- Started UTC: 2026-09-24T20:26:01Z
- Finished UTC: 2026-09-24T20:26:01Z
- Verdict: needs curation

## Target

Generated bacterial MediaRecipe `CultureMech:009910`, `peptone_meat_extract_glycerol_agar`, from the maintained TOGO owner `data/normalized_yaml/bacterial/TOGO_M519_Peptone-Meat_Extract-Glycerol_Agar.yaml`.

The record represents TOGO M519 / JCM GRMD 518, Peptone-Meat Extract-Glycerol Agar. Its generated recipe has 1 g/L distilled water, 20 g/L glycerol, 15 g/L agar, 5 g/L Proteose peptone No. 3, and 3 g/L beef extract.

## Validation

- Open LinkML validation: Passed with no issues.
- Strict validator: Passed; `/private/tmp/peptone_meat_extract_glycerol_agar__f2e0a433.strict.tsv` was header-only, so there were 0 strict errors.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The TOGO identity is internally consistent: TOGO M519 maps to JCM `JCM_M518`, and the TOGO and live JCM pages both call the source Peptone-Meat Extract-Glycerol Agar.

An exact ignored-inclusive search found a separate direct MediaDive/JCM J518 owner at `data/normalized_yaml/bacterial/JCM_J518_PEPTONE-MEAT_EXTRACT-GLYCEROL_AGAR.yaml`, which generates `data/merge_yaml/merged/PEPTONE_MEAT_EXTRACT_GLYCEROL_AGAR.yaml`. It is the same JCM GRMD 518 source recipe and should be reconciled with this TOGO owner.

## Evidence

The live JCM GRMD 518 page and TOGO M519 both support 5 g Proteose peptone No. 3 (BD-Difco), 3 g beef extract (BD-Difco), 20 ml glycerol, 15 g agar, 1 L distilled water, and pH adjustment to 7.0.

MediaDive J518 points to the same JCM source. Its REST payload preserves the source 20 ml glycerol and 1000 ml water rows, but reports the solution volume as 1020 ml and consequently normalizes the 5 g, 3 g, and 15 g solids to 4.90196, 2.94118, and 14.7059 g/L.

The ontology choices in the TOGO record are otherwise reasonable: glycerol and agar are grounded to their expected CHEBI terms, and the BD-Difco Proteose peptone and beef extract are left ungrounded as branded complex ingredients.

## Completeness

The generated TOGO record has each source ingredient row and the correct JCM source link, but it loses the source pH and pH-adjustment instruction.

It is also split from the direct MediaDive/JCM J518 generated sibling. The sibling carries MediaDive-normalized solid concentrations, omits the source water row, and also encodes the source 20 ml glycerol addition as `20 G_PER_L`.

## Findings

1. Needs curation: `Distilled water` is encoded as `1 G_PER_L`, but JCM GRMD 518 and TOGO M519 specify `1 L`.
2. Needs curation: `Glycerol` is encoded as `20 G_PER_L`, but JCM GRMD 518, TOGO M519, and MediaDive J518 specify `20 ml`.
3. Needs curation: the source pH 7.0 and `Adjust pH to 7.0` preparation instruction are missing from the TOGO maintained owner and generated record.
4. Needs curation: JCM GRMD 518 is split between this TOGO M519 generated record and the direct MediaDive/JCM J518 generated sibling; the curation pass should decide how to reconcile the direct MediaDive 1020 ml normalization with the literal JCM/TOGO table amounts.

## Recommended Edits

1. Repair `Distilled water` and `Glycerol` in `data/normalized_yaml/bacterial/TOGO_M519_Peptone-Meat_Extract-Glycerol_Agar.yaml` so both remain source volume additions.
2. Add `ph_value: 7.0` and an `ADJUST_PH` preparation step from JCM GRMD 518.
3. Reconcile `data/normalized_yaml/bacterial/JCM_J518_PEPTONE-MEAT_EXTRACT-GLYCEROL_AGAR.yaml` with the same JCM/TOGO source and MediaDive J518 normalization.
4. Regenerate merged YAML and verify the TOGO M519 and direct MediaDive/JCM J518 owners have the intended relationship.

## Follow-up Checks

1. Re-run open, strict, reference, and term validation on the repaired maintained owners and regenerated merged record.
2. Repeat an exact ignored-inclusive search for `TOGO:M519`, `JCM_M518`, `mediadive.medium:J518`, and `GRMD=518` to verify the JCM 518 recipe is no longer unintentionally split.

## Additional Notes

The exact ignored-inclusive duplicate search covered `data`, `src`, and `scripts` for `TOGO:M519`, `JCM_M518`, `GRMD=518`, `CultureMech:009910`, and `TOGO_M519_Peptone-Meat_Extract-Glycerol_Agar`.
