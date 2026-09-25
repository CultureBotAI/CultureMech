# YAML Record Review: flexibacter_canadensis_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/flexibacter_canadensis_medium__31c9c474.yaml
- Started UTC: 2026-09-23T03:30:19Z
- Finished UTC: 2026-09-23T03:31:23Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:010097` / `flexibacter_canadensis_medium`, the TOGO M691 import sourced from JCM Medium 672.
- Confirmed that this generated record comes from `data/normalized_yaml/bacterial/TOGO_M691_Flexibacter_Canadensis_Medium.yaml`.
- Cross-checked TOGO M691 against the live JCM 672 page and the MediaDive REST payload for JCM J672.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass; 0 total ERROR rows in `/private/tmp/flexibacter_canadensis_medium_31c9c474.strict.tsv`.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- The Togo/JCM identity is coherent: `media_term` is `TOGO:M691`, the source note records original source `JCM_M672`, and JCM GRMD 672 plus MediaDive J672 both serve FLEXIBACTER CANADENSIS MEDIUM.
- The normalized Togo source and generated merge use centered-dot hydrate labels from Togo; prefer the ASCII hydrate spelling used elsewhere during any manual repair.
- MgSO4.7H2O, CaCl2.2H2O, and Thiamine-HCl have primary CHEBI terms but no mirrored `mediaingredientmech_chebi_term`.
- KNO3 still has a legacy `mediaingredientmech_term` identifier rather than an id-safe CHEBI mirror.
- Sodium glycerophosphate and Casamino acids are ungrounded; Casamino acids is an undefined complex ingredient, so only sodium glycerophosphate needs a small-molecule grounding pass.

## Evidence

- Togo M691, JCM 672, and MediaDive J672 all assert pH 7.5 and a liquid main recipe with MgSO4.7H2O, KNO3, CaCl2.2H2O, Sodium glycerophosphate, Trace element solution SL-10, Tris, Thiamine-HCl, Casamino acids, Glucose, Vitamin B12, and Distilled water.
- No agar is present in M691/JCM 672, so `physical_state: LIQUID` is appropriate for this split.
- Togo and JCM both assert 1 mg/L Thiamine-HCl and 1 ug/L Vitamin B12; the generated record stores both as 1 `G_PER_L`.
- The source Trace element solution SL-10 addition is 1 ml/L and references JCM Medium 433; the generated `solutions` row preserves the cross-reference text but uses 1 `G_PER_L` and has only a default `Unknown solution` name.
- The source distilled water amount is 1 L; the generated row records it as 1 `G_PER_L`.

## Completeness

- The generated record omits `ph_value: 7.5` and the source pH-adjustment preparation step.
- Ingredient coverage is otherwise complete for the main JCM 672 formula.
- The SL-10 addition is present but incomplete because its unit is wrong and it is not grounded to the available MediaDive SL-10 solution term.

## Findings

- Needs curation: source pH 7.5 and the pH-adjustment instruction were dropped.
- Needs curation: Trace element solution SL-10 should be a 1 `ML_PER_L` addition, not a 1 `G_PER_L` addition with `Unknown solution`.
- Needs curation: 1 mg/L Thiamine-HCl and 1 ug/L Vitamin B12 were imported as 1 g/L each.
- Needs curation: source Distilled water at 1 L was imported as 1 g/L water.
- Needs curation: KNO3 still uses a legacy MediaIngredientMech ID, while multiple defined ingredients with primary CHEBI terms are missing id-safe CHEBI mirrors.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M691_Flexibacter_Canadensis_Medium.yaml` or the TOGO import logic before regenerating this derived merge.
- Restore `ph_value: 7.5` and a preparation step for adjusting pH to 7.5.
- Convert Thiamine-HCl to 0.001 `G_PER_L` and Vitamin B12 to 0.000001 `G_PER_L`.
- Represent Trace element solution SL-10 as a 1 `ML_PER_L` addition and ground it to the same SL-10 solution used by MediaDive J672.
- Fix the 1 L distilled water row or omit water consistently with other generated final recipes.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated M691 YAML.
- Confirm no 1 `G_PER_L` rows remain for Distilled water, Thiamine-HCl, Vitamin B12, or Trace element solution SL-10.
- Confirm M691 remains liquid and is not collapsed with the agar-containing DSMZ 357/Togo M2591 split.
- Confirm KNO3, MgSO4.7H2O, CaCl2.2H2O, and Thiamine-HCl have id-safe CHEBI mirrors after curation.

## Additional Notes

- Unlike the Togo M2591 split, this JCM 672-derived split did not flatten the SL-10 stock composition into top-level final ingredients.
