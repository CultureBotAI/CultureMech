# YAML Record Review: neutral_oligotrophic_haloarchaeal_medium_no_3

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3__33669e34.yaml
- Started UTC: 2026-09-24T17:13:47Z
- Finished UTC: 2026-09-24T17:14:21Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3__33669e34.yaml` as a generated `MediaRecipe` for TOGO M1002, `CultureMech:007515`, label `neutral_oligotrophic_haloarchaeal_medium_no_3`, category `archaea`, and physical state `SOLID_AGAR`.

The generated record was merged from `data/normalized_yaml/archaea/TOGO_M1002_Neutral_Oligotrophic_Haloarchaeal_Medium_NO.3.yaml`. It is derived; fixes belong in that normalized owner and in the JCM 954 source-family relationships.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3__33669e34.yaml` | Passed; `No issues found`. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3__33669e34.yaml --out /private/tmp/neutral_oligotrophic_haloarchaeal_medium_no_3__33669e34.strict.tsv --workers 1 --quiet` | Passed; TSV had the header only, 1 line and 0 errors. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3__33669e34.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were available. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3__33669e34.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: `just validate-history` validates the standalone `history/` tree, not embedded `MediaRecipe.curation_history` entries inside a single merged YAML file. |

## Identity and Grounding

- The target denotes TOGO M1002, Neutral Oligotrophic Haloarchaeal Medium NO.3, original source `JCM_M954-2`.
- The inspected TOGO M1002 API payload supports the same JCM 954 formulation as TOGO M1001 plus 20 g/L agar in the main solution.
- The live JCM GRMD 954 page supports the JCM 954 recipe family and describes 20 g/L agar as the solid-medium addition.
- A gitignore-independent hidden-file search for `TOGO:M1001`, `TOGO:M1002`, `JCM_M954`, `JCM_M954-2`, `GRMD=954`, and `mediadive.medium:J954` across `data/normalized_yaml` and `data/merge_yaml` found separate normalized owners and generated records for TOGO M1001, TOGO M1002, and the direct JCM/MediaDive J954 import.

## Evidence

The inspected TOGO M1002 payload places these items in the main solution: 233 ml distilled water, 1 g yeast extract, 0.25 g each sodium acetate, sodium pyruvate, sodium lactate, fish peptone, and sodium formate, 20 g/L agar, and 767 ml MDS salt water. It then lists a second solution group containing 5 ml 1 M NH4Cl solution and 2 ml potassium phosphate buffer. JCM GRMD 954 instructs pH adjustment to 7.0, autoclaving, cooling, and addition of the latter two solutions after cooling.

The generated record keeps the M1002 agar row but drops the source step order and records MDS salt water, 1 M NH4Cl solution, and potassium phosphate buffer as empty `Unknown solution` rows with `G_PER_L` units.

## Completeness

- Consequential gap: the three milliliter additions are present only as empty solution wrappers with gram-per-liter units.
- Consequential gap: pH 7.0 adjustment, autoclaving, cooling, and post-autoclave addition steps are absent.
- Consequential gap: M1002 is not linked as the agar variant of the M1001 liquid record or reconciled with the direct JCM/MediaDive J954 record.
- Empty optional fields are not defects. The inspected sources do not provide an incubation temperature or target organism.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Source milliliter additions were migrated to empty gram-per-liter solution rows. | TOGO M1002 lists 767 ml MDS salt water, 5 ml 1 M NH4Cl solution, and 2 ml potassium phosphate buffer; the generated record has these as empty `Unknown solution` rows at `767`, `5`, and `2 G_PER_L`. | Recurate `data/normalized_yaml/archaea/TOGO_M1002_Neutral_Oligotrophic_Haloarchaeal_Medium_NO.3.yaml` so those rows remain volume additions and resolve Medium 578 references where possible. |
| major | Preparation ordering is missing. | JCM GRMD 954 instructs pH 7.0 adjustment, autoclaving, cooling, and post-cooling addition of NH4Cl solution and potassium phosphate buffer. The generated M1002 record has no `preparation_steps`. | Add the source preparation sequence to the normalized M1002 owner. |
| major | The agar variant is unlinked from the liquid parent and direct JCM duplicate. | Exact hidden-file search found TOGO M1001, TOGO M1002, and direct `mediadive.medium:J954` owners as three separate active/generated records for JCM 954. | Model M1002 as the 20 g/L agar variant of M1001 and reconcile the direct JCM/MediaDive J954 owner. |

## Recommended Edits

1. Keep MDS salt water, 1 M NH4Cl solution, and potassium phosphate buffer as milliliter solution additions rather than generated `G_PER_L` placeholders.
2. Add the pH 7.0, autoclave, cooling, and post-autoclave addition instructions to the M1002 owner.
3. Link M1002 as the agar variant of M1001, then reconcile both TOGO records with the direct JCM/MediaDive J954 expansion.
4. Regenerate merged YAML after normalized records and relationships are corrected.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the repaired M1002 owner and regenerated merge.
- Re-run a gitignore-independent hidden-file search for `TOGO:M1001`, `TOGO:M1002`, `JCM_M954`, `JCM_M954-2`, and `mediadive.medium:J954` under `data/normalized_yaml` and `data/merge_yaml`.
- Manually compare the regenerated M1001/M1002 records against the live JCM GRMD 954 page and the TOGO M1001/M1002 API payloads.

## Additional Notes

The live JCM GRMD 954 page was available and supports the post-autoclave addition order that was lost during solution migration.
