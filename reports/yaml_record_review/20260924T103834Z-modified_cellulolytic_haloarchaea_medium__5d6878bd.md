# YAML Record Review: modified_cellulolytic_haloarchaea_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_cellulolytic_haloarchaea_medium__5d6878bd.yaml
- Started UTC: 2026-09-24T10:37:39Z
- Finished UTC: 2026-09-24T10:38:34Z
- Verdict: needs curation

## Target

Generated record `CultureMech:007798` for TOGO medium `M1266`, `Modified Cellulolytic Haloarchaea Medium`, a TOGO import of JCM medium `JCM_M1181-2`.

The exact maintained owner is `data/normalized_yaml/archaea/TOGO_M1266_Modified_Cellulolytic_Haloarchaea_Medium.yaml`. The generated YAML was compared with that owner, the TOGO M1266 API payload, JCM medium 1181, and the referenced JCM stock pages 574, 1079, and 197.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed; `/private/tmp/modified_cellulolytic_haloarchaea_medium__5d6878bd.strict.tsv` contained only the header row.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The TOGO identity is correct, but the generated artifact is stale relative to its maintained owner.

The maintained owner has a 2026-09-10 `RESOLVED_TOGO_JCM_ARCHAEA_SCORE15` repair that expands the JCM 1181 stock additions, keeps `Distilled water` as `124.0` `ML_PER_L`, preserves pH 7.0, and grounds stock members such as `NiCl2 x 6H2O` to hydrate-specific `CHEBI:53542`. The generated file was last merged on 2026-08-06 and still has the earlier empty-stub representation.

## Evidence

The TOGO M1266 payload lists `124 ml` distilled water, 20 g/L agar, 0.1 g yeast extract, 833 ml MDS salt water, and 1 ml Trace element solution in the first main section. Its post-autoclave section lists 5 ml of 1 M `NH4Cl`, 30 ml of 0.2 M Cellobiose solution, 2 ml Potassium phosphate buffer, 5 ml Trace vitamins, and a 10% `Na2CO3` solution for pH readjustment. Those rows mirror JCM 1181, while JCM 574, 1079, and 197 provide the referenced stock formulae.

The maintained TOGO owner now models the main root rows as water, agar, and yeast extract, then represents MDS salt water, Trace element solution, 1 M `NH4Cl`, Potassium phosphate buffer, Trace vitamins, 0.2 M Cellobiose solution, and 10% `Na2CO3` solution as structured `solutions` entries with source-specific `ML_PER_L` additions and nested compositions.

The generated record has only four root ingredients and six `solutions` entries whose names are all `Unknown solution`. Each generated solution has an empty `composition`, and the volume additions are stored as `G_PER_L`; for example, 833 ml MDS salt water is encoded as 833 g/L, 30 ml Cellobiose solution is encoded as 30 g/L, and the 10% sodium carbonate pH-adjustment stock has no sodium carbonate composition. The generated artifact also lacks the owner's restored `ph_value: 7.0`.

## Completeness

The generated record preserves the TOGO M1266 identifier, source note, solid agar row, and the high-level set of referenced solution names.

It is incomplete relative to both the live TOGO payload and the repaired maintained owner: all solution compositions are empty, pH is absent, the water row has the wrong unit, and every solution addition lost its `ML_PER_L` unit and stock contents.

## Findings

- High: The generated YAML is stale relative to the 2026-09-10 repair in `data/normalized_yaml/archaea/TOGO_M1266_Modified_Cellulolytic_Haloarchaea_Medium.yaml`.
- High: MDS salt water, Trace element solution, 1 M `NH4Cl`, Potassium phosphate buffer, Trace vitamins, 0.2 M Cellobiose solution, and 10% `Na2CO3` solution are empty `Unknown solution` stubs in the generated artifact.
- Medium: Volume additions are stored as `G_PER_L`, including 124 ml distilled water and all ml-scale solution additions.
- Medium: pH 7.0 is absent from the generated record even though it is present in TOGO M1266, JCM 1181, and the repaired owner.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/modified_cellulolytic_haloarchaea_medium__5d6878bd.yaml` from the repaired 2026-09-10 maintained owner.
- Confirm that the regenerated record keeps water at `124.0` `ML_PER_L`, restores `ph_value: 7.0`, and expands all six solution entries with their nested compositions.
- Preserve the TOGO/JCM source lineage for JCM 1181 plus referenced stock pages 574, 1079, and 197.
- Keep the record distinct from `CultureMech:002353`, the MediaDive/JCM liquid sibling reviewed under fingerprint `51fd74be`.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Check the regenerated artifact for any remaining `Unknown solution` names or empty `composition` lists.
- Compare the regenerated solution units against the maintained owner to verify the `ML_PER_L`, `MOLAR`, `MG_PER_L`, and `PERCENT_W_V` units survive merging.

## Additional Notes

The exact owner was found with `find`, which included ignored files.
