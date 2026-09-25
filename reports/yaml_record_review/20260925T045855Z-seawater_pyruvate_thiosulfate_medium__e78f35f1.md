# YAML Record Review: seawater_pyruvate_thiosulfate_medium__e78f35f1

- Repository: CultureMech
- Record: data/merge_yaml/merged/seawater_pyruvate_thiosulfate_medium__e78f35f1.yaml
- Started UTC: 2026-09-25T04:58:55Z
- Finished UTC: 2026-09-25T04:58:55Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002276`, `seawater_pyruvate_thiosulfate_medium`, from `data/merge_yaml/merged/seawater_pyruvate_thiosulfate_medium__e78f35f1.yaml`.

The target record is a single-source direct MediaDive/JCM J1097 import for `SEAWATER PYRUVATE THIOSULFATE MEDIUM`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The target record is correctly grounded to JCM Medium J1097.

The generated merge layer also contains `data/merge_yaml/merged/SEAWATER_PYRUVATE_THIOSULFATE_MEDIUM.yaml`, a TOGO M1170 import whose metadata identifies the same recipe as `JCM_M1097` from the same JCM GRMD 1097 URL. The two generated records are true duplicate source imports that did not merge.

## Evidence

JCM 1097 lists a base with 20 g NaCl, 3 g MgCl2 x 6H2O, 0.15 g CaCl2 x 2H2O, 0.25 g NH4Cl, 0.2 g KH2PO4, 0.5 g KCl, 10 ml RST trace elements from JCM 933, 1 mg Resazurin, and 922.5 ml Distilled water.

JCM 1097 then adds 37.5 ml 8% NaHCO3 solution, 10 ml RST vitamin solution, 20 ml 1 M Sodium pyruvate solution, and 10 ml 1% Yeast extract solution after cooling.

JCM 1097 finally distributes the medium under N2-CO2 and adds 10 ml Reducing agent solution from JCM 521 per liter.

## Completeness

The generated target scales the direct base salts and Resazurin below their source values.

The target represents 37.5 ml/L 8% NaHCO3 solution, 20 ml/L 1 M Sodium pyruvate solution, and 10 ml/L 1% Yeast extract solution as direct 37.5 g/L, 20 g/L, and 10 g/L parent rows.

The target flattens the RST vitamin solution, RST trace elements from JCM 933, and Reducing agent solution from JCM 521 into parent rows at stock strength.

The target omits the source 922.5 ml Distilled water base row and has no structured N2 or CO2 gas ingredients.

The JCM 933 RST trace element pH 6.0 preparation note, JCM 521 reducing-agent storage note, and JCM 521 strain-specific inoculation comment all leaked into the parent JCM 1097 preparation steps.

## Findings

The direct MediaDive import flattened multiple stock additions and linked stock recipes into final-medium ingredients.

Post-cooling liquid additions were interpreted as mass concentrations rather than as ml/L stock volumes.

The parent preparation procedure is polluted by linked-stock preparation notes from JCM 933 and JCM 521.

The TOGO M1170 duplicate has the same JCM source and remains a separate generated record.

## Recommended Edits

Repair the direct MediaDive/JCM J1097 normalized source so the RST trace elements, RST vitamin solution, NaHCO3, Sodium pyruvate, Yeast extract, and Reducing agent solution additions remain solution-scoped with their source ml/L volumes.

Move JCM 933 and JCM 521 components and preparation notes under nested stock scopes instead of parent `ingredients` and parent `preparation_steps`.

Restore the source-scale parent rows and the 922.5 ml Distilled water row.

Regenerate the merge layer after the JCM J1097 and TOGO M1170 normalized sources are repaired.

## Follow-up Checks

Confirm the regenerated parent has no direct 37.5 g/L NaHCO3, 20 g/L Sodium pyruvate, or 10 g/L Yeast extract rows.

Confirm the regenerated parent has no direct stock-strength rows such as 2 g/L Nitrilotriacetic acid, 0.005 g/L Coenzyme M, or 12.5 g/L Na2S x 9H2O.

Confirm the regenerated parent has no JCM 933 RST trace element pH instruction and no JCM 521 strain-specific inoculation comment.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
