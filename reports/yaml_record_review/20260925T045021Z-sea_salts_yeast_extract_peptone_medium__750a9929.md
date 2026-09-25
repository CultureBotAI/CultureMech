# YAML Record Review: sea_salts_yeast_extract_peptone_medium__750a9929

- Repository: CultureMech
- Record: data/merge_yaml/merged/sea_salts_yeast_extract_peptone_medium__750a9929.yaml
- Started UTC: 2026-09-25T04:50:21Z
- Finished UTC: 2026-09-25T04:50:21Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007750`, `sea_salts_yeast_extract_peptone_medium`, from `data/merge_yaml/merged/sea_salts_yeast_extract_peptone_medium__750a9929.yaml`.

The target record is a single-source TOGO M1222 import for `Sea Salts Yeast Extract Peptone Medium`, originally sourced from JCM_M1141.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The target record is correctly grounded to TOGO Medium M1222, which resolves to JCM Medium J1141.

The generated merge layer also contains `data/merge_yaml/merged/sea_salts_yeast_extract_peptone_medium__3154bd30.yaml`, the direct MediaDive/JCM J1141 import of the same liquid medium. The two records are true duplicates.

The generated merge layer also contains `data/merge_yaml/merged/Sea_Salts_Yeast_Extract_Peptone_Medium.yaml` from TOGO M1223, an optional 18 g/L agar derivative from the same JCM page.

## Evidence

JCM 1141 lists 40 g Sea salts (Sigma), 50 g NaCl, 1 g Yeast extract, 5 g Peptone, 0.1 g Ferric citrate, and 1 L Distilled water.

The preparation text says to mix components thoroughly and adjust pH to 7.5. It then says to add 18 g/L agar for solid medium.

The TOGO M1222 API records 1 L Distilled water and carries the same GRMD 1141 source URL.

## Completeness

The target preserves the non-water liquid JCM component masses at source scale.

The source 1 L Distilled water item is present but converted to 1 g/L water.

The target omits the JCM pH 7.5 preparation step that is present in the TOGO M1222 API comment.

The target has no agar row, which is correct for the JCM_M1141 liquid branch.

## Findings

The TOGO M1222 import is a true duplicate of the direct MediaDive/JCM J1141 generated record.

The importer converted the source 1 L Distilled water item to `G_PER_L`.

The pH 7.5 preparation text from TOGO/JCM did not make it into the generated record.

The optional solid-agar sibling from TOGO M1223 is still a standalone generated record with the same medium name, so JCM 1141 is represented by three generated files.

## Recommended Edits

Repair the TOGO M1222 normalized source so the source water row is not represented as 1 g/L water.

Restore the pH 7.5 preparation text from the TOGO M1222 comment.

Normalize the TOGO M1222 and direct MediaDive/JCM J1141 sources so the liquid branches merge.

Model the TOGO M1223 solid agar form as an 18 g/L agar variant or derivative of JCM 1141 rather than as an independent same-name base medium.

Regenerate the merge layer after the JCM J1141 and TOGO M1222/M1223 normalized sources are repaired.

## Follow-up Checks

Confirm the regenerated merge layer has one liquid JCM 1141 base record, not both `sea_salts_yeast_extract_peptone_medium__750a9929.yaml` and `sea_salts_yeast_extract_peptone_medium__3154bd30.yaml`.

Confirm the regenerated TOGO-derived liquid branch has no 1 g/L water concentration.

Confirm the regenerated liquid record has a pH 7.5 preparation step and no agar ingredient.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
