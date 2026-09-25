# YAML Record Review: neutral_oligotrophic_haloarchaeal_medium_no_3

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3__6aabd4ce.yaml
- Started UTC: 2026-09-24T17:14:44Z
- Finished UTC: 2026-09-24T17:15:30Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3__6aabd4ce.yaml` as a generated `MediaRecipe` for the direct JCM/MediaDive `J954` import, `CultureMech:003302`, label `neutral_oligotrophic_haloarchaeal_medium_no_3`, category `archaea`, and physical state `LIQUID`.

The generated record was merged from `data/normalized_yaml/archaea/neutral_oligotrophic_haloarchaeal_medium_no_3.yaml`. It is derived and should be regenerated after the direct JCM owner is reconciled with TOGO M1001 and M1002.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3__6aabd4ce.yaml` | Passed; `No issues found`. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3__6aabd4ce.yaml --out /private/tmp/neutral_oligotrophic_haloarchaeal_medium_no_3__6aabd4ce.strict.tsv --workers 1 --quiet` | Passed; TSV had the header only, 1 line and 0 errors. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3__6aabd4ce.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were available. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3__6aabd4ce.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: `just validate-history` validates the standalone `history/` tree, not embedded `MediaRecipe.curation_history` entries inside a single merged YAML file. |

## Identity and Grounding

- The target denotes JCM/MediaDive `J954`, Neutral Oligotrophic Haloarchaeal Medium NO.3, pH 7.0.
- The inspected live JCM GRMD 954 page, MediaDive REST `J954` response, and TOGO M1001/M1002 API payloads agree on the source family: the base medium uses 767 ml MDS salt water, 233 ml distilled water, organic nutrient additions, 5 ml 1 M NH4Cl solution, and 2 ml potassium phosphate buffer; the M1002 solid form adds 20 g/L agar.
- A gitignore-independent hidden-file search for `TOGO:M1001`, `TOGO:M1002`, `JCM_M954`, `JCM_M954-2`, `GRMD=954`, and `mediadive.medium:J954` across `data/normalized_yaml` and `data/merge_yaml` found this direct owner plus separate TOGO liquid and agar owners for the same JCM source family.

## Evidence

The MediaDive REST `J954` payload represents the final medium as `Main sol. J954` with a 767 ml `MDS salt water` solution reference and a 2 ml `Potassium phosphate buffer` solution reference. It then defines those referenced solutions separately: MDS salt water has NaCl, MgCl2 x 6 H2O, MgSO4 x 7 H2O, KCl, and CaCl2 at per-liter stock strength, and potassium phosphate buffer is prepared from 1 M K2HPO4 plus 1 M KH2PO4.

The generated direct-JCM record loses those stock boundaries. It lists the MDS salt water salts at their full stock `G_PER_L` concentrations in the final ingredient list, lists K2HPO4 and KH2PO4 at potassium phosphate buffer strength in the final ingredient list, and appends both stock-solution pH 7.5 preparation steps to the final pH 7.0 medium.

## Completeness

- Consequential error: 767 ml MDS salt water was expanded without dilution into final-medium salts.
- Consequential error: 2 ml potassium phosphate buffer was expanded without dilution into final-medium K2HPO4 and KH2PO4 rows.
- Consequential gap: the 5 ml 1 M NH4Cl solution is converted to final NH4Cl mass and loses its source post-autoclave solution boundary.
- Consequential duplicate gap: direct JCM `J954`, TOGO M1001, and TOGO M1002 are separate active generated records.
- Empty optional fields are not defects. The inspected providers do not supply incubation temperature or a target organism.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Referenced Medium 574 stock solutions were flattened into the final J954 ingredient list at stock strength. | MediaDive `J954` uses 767 ml MDS salt water and 2 ml potassium phosphate buffer; the generated record lists 240 g/L NaCl, 30 g/L MgCl2 x 6 H2O, 35 g/L MgSO4 x 7 H2O, 7 g/L KCl, 14.5263 g/L K2HPO4, and 2.25901 g/L KH2PO4 as final ingredients. | Recurate `data/normalized_yaml/archaea/neutral_oligotrophic_haloarchaeal_medium_no_3.yaml` to keep MDS salt water and potassium phosphate buffer as solution references or expand them at final diluted concentrations. |
| major | Stock-solution preparation steps are attached to the final medium. | The final JCM 954 target pH is 7.0; pH 7.5 with Tris belongs to MDS salt water, and combining K2HPO4/KH2PO4 to pH 7.5 belongs to the potassium phosphate buffer. | Move the stock steps to their Medium 574 solution records and keep the JCM 954 pH/autoclave/post-addition step on the final recipe. |
| major | Same-source TOGO and direct-JCM records are not reconciled. | Exact hidden-file search found TOGO M1001, TOGO M1002, and direct `mediadive.medium:J954` records with separate generated outputs. | Resolve the direct J954 owner with TOGO M1001 and link TOGO M1002 as the agar variant. |

## Recommended Edits

1. Recurate the direct JCM `J954` owner so MDS salt water and potassium phosphate buffer remain referenced solution additions with 767 ml and 2 ml volumes.
2. Keep stock-solution preparation steps on the Medium 574 solution records, not in the final J954 medium.
3. Preserve 5 ml 1 M NH4Cl as a post-autoclave solution addition.
4. Reconcile the direct JCM owner with TOGO M1001 and TOGO M1002, then regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the repaired direct owner and regenerated merge.
- Re-run a gitignore-independent hidden-file search for `JCM_M954`, `JCM_M954-2`, `GRMD=954`, `TOGO:M1001`, `TOGO:M1002`, and `mediadive.medium:J954` under `data/normalized_yaml` and `data/merge_yaml`.
- Manually compare the regenerated record against MediaDive REST `J954` and live JCM GRMD 954 to confirm the Medium 574 solution boundaries are preserved.

## Additional Notes

The live JCM GRMD 954 page was available. MediaDive REST `J954` was also inspected to verify that the generated record's unusual 0.993049 and 0.248262 main-solute concentrations come from scaling by the 1007 ml final volume.
