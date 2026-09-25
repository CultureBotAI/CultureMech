# YAML Record Review: sea_salts_yeast_extract_peptone_medium__3154bd30

- Repository: CultureMech
- Record: data/merge_yaml/merged/sea_salts_yeast_extract_peptone_medium__3154bd30.yaml
- Started UTC: 2026-09-25T04:49:22Z
- Finished UTC: 2026-09-25T04:49:22Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:010492`, `sea_salts_yeast_extract_peptone_medium`, from `data/merge_yaml/merged/sea_salts_yeast_extract_peptone_medium__3154bd30.yaml`.

The target record is a single-source direct MediaDive/JCM J1141 import for `SEA SALTS YEAST EXTRACT PEPTONE MEDIUM`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The target record is correctly grounded to JCM Medium J1141.

The generated merge layer also contains a TOGO M1222 import at `data/merge_yaml/merged/sea_salts_yeast_extract_peptone_medium__750a9929.yaml`; its metadata identifies the same JCM page as `JCM_M1141` and the same GRMD 1141 URL. That record is a true duplicate of the direct MediaDive/JCM liquid import.

The generated merge layer also contains `data/merge_yaml/merged/Sea_Salts_Yeast_Extract_Peptone_Medium.yaml` from TOGO M1223. Its metadata identifies `JCM_M1141-2` from the same JCM page and it represents the optional 18 g/L agar clause as a separate solid-agar record.

## Evidence

JCM 1141 lists 40 g Sea salts (Sigma), 50 g NaCl, 1 g Yeast extract, 5 g Peptone, 0.1 g Ferric citrate, and 1 L Distilled water.

The preparation text says to mix components thoroughly and adjust pH to 7.5. It then says to add 18 g/L agar for solid medium.

TOGO M1222 identifies the same GRMD 1141 URL as `JCM_M1141`, and TOGO M1223 identifies it as `JCM_M1141-2`.

## Completeness

The direct MediaDive/JCM target preserves all non-water liquid source rows at source scale.

The 1 L Distilled water row is absent from the direct target.

The direct target preserves pH 7.5 and the optional 18 g/L agar instruction as preparation prose.

The TOGO M1222 duplicate contains the water row but imports it as 1 g/L water instead of 1 L/L water and omits the pH 7.5 preparation step.

The TOGO M1223 agar derivative contains the same 1 g/L water row and an 18 g/L agar row.

## Findings

JCM 1141 is split into three generated records: the direct MediaDive liquid target, a TOGO liquid duplicate, and a TOGO solid-agar derivative.

The direct target is missing Distilled water.

The TOGO liquid duplicate failed to merge back into the direct record, in part because the TOGO importer converts the 1 L water source item to 1 g/L.

The optional solid-medium agar clause is represented as a separate generated medium with the same normalized name rather than as a variant of the JCM 1141 liquid base.

## Recommended Edits

Restore the 1 L Distilled water row in the direct MediaDive/JCM J1141 normalized source.

Repair the TOGO M1222 and M1223 normalized sources so the 1 L Distilled water item is not represented as 1 g/L water.

Normalize the direct MediaDive/JCM J1141 source and TOGO M1222 source so they merge into a single liquid JCM 1141 record.

Model the optional 18 g/L agar form as a solid-medium variant of JCM 1141, or otherwise mark the TOGO M1223 import as a derivative of the same JCM page instead of leaving it as an apparently independent same-name medium.

Regenerate the merge layer after the JCM J1141 and TOGO M1222/M1223 normalized sources are repaired.

## Follow-up Checks

Confirm the regenerated merge layer has one liquid JCM 1141 base record, not both `sea_salts_yeast_extract_peptone_medium__3154bd30.yaml` and `sea_salts_yeast_extract_peptone_medium__750a9929.yaml`.

Confirm the regenerated liquid base has Distilled water without a 1 g/L water concentration.

Confirm the optional agar form retains 18 g/L agar only as a solid-medium variant or marked derivative.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
