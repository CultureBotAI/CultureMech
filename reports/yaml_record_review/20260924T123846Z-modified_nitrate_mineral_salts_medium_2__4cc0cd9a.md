# YAML Record Review: modified_nitrate_mineral_salts_medium_2

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_nitrate_mineral_salts_medium_2__4cc0cd9a.yaml
- Started UTC: 2026-09-24T12:38:46Z
- Finished UTC: 2026-09-24T12:39:38Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:002389`, `modified_nitrate_mineral_salts_medium_2`, generated from `data/normalized_yaml/bacterial/modified_nitrate_mineral_salts_medium_2.yaml`.
- The record represents MediaDive `J1221`, sourced from JCM `GRMD=1221`, named `MODIFIED NITRATE  MINERAL SALTS MEDIUM-2`.
- The generated MediaDive record was compared with MediaDive `J1221`, JCM `GRMD=1221`, and the parallel TOGO `M1312` import of the same JCM source.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` reported no issues.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- MediaDive `J1221`, TOGO `M1312`, and JCM `GRMD=1221` all identify the same Modified Nitrate Mineral Salts Medium-2 recipe.
- A gitignore-independent duplicate check for exact JCM/TOGO/MediaDive identifiers found the TOGO maintained record, `data/normalized_yaml/bacterial/TOGO_M1312_Modified_Nitrate_Mineral_Salts_Medium-2.yaml`, and its generated record, `data/merge_yaml/merged/modified_nitrate_mineral_salts_medium_2.yaml`, in parallel with this MediaDive record.
- No inspected source payload identified a target organism for this medium.

## Evidence

- JCM lists a 1 L basal medium with MgSO4 x 7 H2O, CaCl2 x 2 H2O, KNO3, 1 ml FeCl2 solution, 1 ml Trace element solution, 2 ml 1 M HEPES solution at pH 7.0, 4 mg ammonium ferric citrate, and 1 L distilled water.
- JCM then instructs adding 2 ml Phosphate buffer solution and 10 ml Vitamin solution after cooling.
- MediaDive preserves the same stock hierarchy: `Main sol. J1221` references FeCl2 solution, Trace element solution, Phosphate buffer solution, and Vitamin solution by solution identifiers rather than listing their members as basal ingredients.
- The local Phosphate buffer solution is 1.4 g KH2PO4 and 3.6 g Na2HPO4 x 2 H2O in 100 ml distilled water.
- The local Vitamin solution is 1 L Trace vitamins plus 20 mg Vitamin B12, 5 mg L-Ascorbic acid, and 5 mg Nicotinamide.
- JCM describes two substrate modes: a 75:25 air-methane gas mixture for methane and 4.0 ml per liter filter-sterilized methanol for methanol cultures.

## Completeness

- The basal salts and ammonium ferric citrate are present.
- FeCl2 solution, Trace element solution, Phosphate buffer solution, Vitamin solution, and Trace vitamins solution components are flattened into top-level ingredients with stock concentrations instead of final-medium concentrations.
- The 2 ml HEPES stock addition is represented as `2` `G_PER_L` HEPES and loses that it was a 1 M solution at pH 7.0.
- Local and trace Vitamin B12 rows are merged into one `0.0201` `G_PER_L` ingredient, losing the two stock scopes.
- The methanol supplement option is absent from structured ingredients or solutions.

## Findings

- Blocker: nested stock solutions from MediaDive are flattened into top-level ingredients without scaling by their final-medium addition volumes. For example, 1.5 g/L FeCl2 x 4 H2O from the FeCl2 stock, 14 g/L KH2PO4 from the 100 ml Phosphate buffer stock, and 0.07 g/L ZnCl2 from the Trace element stock appear as final medium concentrations even though JCM adds only 1 ml or 2 ml of those stocks to roughly 1 L of medium.
- Blocker: the 10 ml Vitamin solution addition is likewise flattened at stock strength. The local 0.02 g/L Vitamin B12 row and the nested Trace vitamins 0.0001 g/L Vitamin B12 row are merged into a final `0.0201` `G_PER_L` ingredient.
- Major: 2 ml of 1 M HEPES solution at pH 7.0 is converted to `2` `G_PER_L` HEPES, which copies the milliliter amount into a mass-per-volume row and drops the molarity and pH context.
- Major: the 4.0 ml per liter methanol substrate option from JCM is missing from structured ingredients or solutions.
- Major: the same JCM 1221 medium is maintained and generated twice, once through MediaDive `J1221` and once through TOGO `M1312`.

## Recommended Edits

- Preserve the MediaDive stock solution tree for FeCl2 solution, Trace element solution, Phosphate buffer solution, Vitamin solution, and Trace vitamins, or scale nested members to final concentrations while keeping source solution provenance.
- Model the 2 ml 1 M HEPES solution as a volume of stock solution, not as `2` `G_PER_L` HEPES.
- Keep local Vitamin solution and nested Trace vitamins components in separate scopes so their Vitamin B12 rows are not merged.
- Represent the methanol cultivation option as a 4.0 ml/L filter-sterilized methanol supplement or another structured optional substrate.
- Merge or explicitly cross-link the TOGO `M1312` and MediaDive `J1221` maintained records before regeneration so JCM `GRMD=1221` has one CultureMech identity.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting MediaDive solution flattening.
- Recompare the regenerated record against MediaDive `J1221` and JCM `GRMD=1221`, including all stock solutions and both methane and methanol substrate modes.
- Confirm that generated YAML no longer contains both `modified_nitrate_mineral_salts_medium_2.yaml` and `modified_nitrate_mineral_salts_medium_2__4cc0cd9a.yaml` as separate records for the same JCM recipe.

## Additional Notes

None found.
