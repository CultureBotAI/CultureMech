# YAML Record Review: neutral_oligotrophic_haloarchaeal_medium_no_3

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3.yaml
- Started UTC: 2026-09-24T17:12:35Z
- Finished UTC: 2026-09-24T17:13:22Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3.yaml` as a generated `MediaRecipe` for TOGO M1001, `CultureMech:007514`, label `neutral_oligotrophic_haloarchaeal_medium_no_3`, category `archaea`, and physical state `LIQUID`.

The generated record was merged from `data/normalized_yaml/archaea/TOGO_M1001_Neutral_Oligotrophic_Haloarchaeal_Medium_NO.3.yaml`. It is derived; future fixes belong in that normalized TOGO owner, the shared Medium 574 solution owners, and its relationship to the JCM 954 source family.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3.yaml` | Passed; `No issues found`. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3.yaml --out /private/tmp/neutral_oligotrophic_haloarchaeal_medium_no_3.strict.tsv --workers 1 --quiet` | Passed; TSV had the header only, 1 line and 0 errors. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were available. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/neutral_oligotrophic_haloarchaeal_medium_no_3.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: `just validate-history` validates the standalone `history/` tree, not embedded `MediaRecipe.curation_history` entries inside a single merged YAML file. |

## Identity and Grounding

- The target denotes TOGO M1001, Neutral Oligotrophic Haloarchaeal Medium NO.3, original source `JCM_M954`.
- The inspected live JCM GRMD 954 page and TOGO M1001 API payload agree on the liquid formulation: 767 ml MDS salt water, 233 ml distilled water, 1 g yeast extract, 0.25 g each fish peptone, sodium formate, sodium acetate, sodium lactate, and sodium pyruvate, followed by 5 ml 1 M NH4Cl solution and 2 ml potassium phosphate buffer after autoclaving.
- A gitignore-independent hidden-file search for `TOGO:M1001`, `TOGO:M1002`, `JCM_M954`, `JCM_M954-2`, `GRMD=954`, and `mediadive.medium:J954` across `data/normalized_yaml` and `data/merge_yaml` found TOGO M1001, TOGO M1002, and direct JCM/MediaDive J954 normalized owners plus three separate generated outputs for the same JCM source family.

## Evidence

JCM and TOGO both support a two-stage recipe. The base is mixed from MDS salt water, distilled water, and the organic nutrient salts, then pH is adjusted to 7.0 and the base is autoclaved. After cooling, 5 ml of 1 M NH4Cl solution and 2 ml of potassium phosphate buffer are added; JCM marks the ammonium chloride solution as filter-sterilized or autoclaved.

The generated YAML preserves the base masses, but it moves all three solution additions to empty `Unknown solution` rows. The 767 ml MDS salt water addition, 5 ml 1 M NH4Cl solution, and 2 ml potassium phosphate buffer addition are recorded as `767`, `5`, and `2 G_PER_L`, respectively, and the pH/autoclave/post-cooling addition order is absent.

## Completeness

- Consequential gap: MDS salt water and potassium phosphate buffer do not resolve to their Medium 578 compositions.
- Consequential gap: all three source milliliter additions are represented with gram-per-liter units.
- Consequential gap: pH 7.0 adjustment, autoclaving, cooling, and post-autoclave solution additions are missing.
- Consequential duplicate gap: the TOGO M1002 agar variant and the direct JCM/MediaDive J954 record are active as independent generated records rather than explicit members of a JCM 954 source family.
- Empty optional fields are not defects. The inspected sources do not provide a target organism or incubation temperature.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Source milliliter additions were migrated to empty gram-per-liter solution rows. | JCM 954 and TOGO M1001 list 767 ml MDS salt water, 5 ml 1 M NH4Cl solution, and 2 ml potassium phosphate buffer. The generated record has three empty `Unknown solution` wrappers with `G_PER_L` units. | Recurate `data/normalized_yaml/archaea/TOGO_M1001_Neutral_Oligotrophic_Haloarchaeal_Medium_NO.3.yaml` so these rows remain volume additions and resolve Medium 578 references where possible. |
| major | Preparation ordering is missing. | JCM 954 instructs pH adjustment to 7.0, autoclaving, cooling, and then addition of NH4Cl solution and potassium phosphate buffer; the generated record has no `preparation_steps`. | Add the source preparation sequence to the normalized M1001 owner. |
| major | The liquid, agar, and direct-JCM records for JCM 954 are not reconciled. | Exact hidden-file search found TOGO M1001, TOGO M1002, and direct `mediadive.medium:J954` owners, each with a separate generated output under `data/merge_yaml/merged`. | Resolve `TOGO_M1001_Neutral_Oligotrophic_Haloarchaeal_Medium_NO.3.yaml`, `TOGO_M1002_Neutral_Oligotrophic_Haloarchaeal_Medium_NO.3.yaml`, and `neutral_oligotrophic_haloarchaeal_medium_no_3.yaml` into one source family. |

## Recommended Edits

1. Preserve MDS salt water, 1 M NH4Cl solution, and potassium phosphate buffer as milliliter solution additions rather than `G_PER_L` placeholder solutions.
2. Add the pH 7.0, autoclave, cooling, and post-autoclave addition steps to the M1001 owner.
3. Link M1002 as the 20 g/L agar variant of M1001 and reconcile the direct JCM/MediaDive J954 expansion.
4. Regenerate merged YAML after the normalized owners are corrected.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the repaired normalized records and regenerated merged outputs.
- Re-run a gitignore-independent hidden-file search for `TOGO:M1001`, `TOGO:M1002`, `JCM_M954`, and `mediadive.medium:J954` under `data/normalized_yaml` and `data/merge_yaml`.
- Manually compare the regenerated liquid and agar records against live JCM GRMD 954 plus the TOGO M1001/M1002 API payloads.

## Additional Notes

The live JCM GRMD 954 page was available and agreed with TOGO M1001 for the liquid formulation. TOGO M1002 is the same JCM source with a 20 g/L agar row.
