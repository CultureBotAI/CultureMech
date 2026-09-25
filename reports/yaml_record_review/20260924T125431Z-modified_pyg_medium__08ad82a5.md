# YAML Record Review: modified_pyg_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_pyg_medium__08ad82a5.yaml
- Started UTC: 2026-09-24T12:54:31Z
- Finished UTC: 2026-09-24T12:55:10Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:008619`, `modified_pyg_medium`, generated from `data/normalized_yaml/bacterial/modified_pyg_medium.yaml`.
- The record represents TOGO `M2030`, sourced from NBRC `NBRC_M1322`, named `Modified PYG Medium`.
- The generated TOGO record was compared with TOGO `M2030` and the primary NBRC `NO=1322` page.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` reported no issues.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- TOGO `M2030` points to NBRC `NBRC_M1322`, and NBRC `NO=1322` identifies Modified PYG Medium.
- A gitignore-independent exact search for the TOGO and NBRC identifiers found only one maintained YAML record, `data/normalized_yaml/bacterial/modified_pyg_medium.yaml`, plus this generated record and index metadata.
- The three undefined proteinaceous products, `Bacto Yeast Extract (Difco)`, `Bacto Tryptone (Difco)`, and `Hipolypepton`, have no primary ontology grounding.
- No inspected source payload identified a target organism for this medium.

## Evidence

- NBRC lists 0.01 g CaCl2 x 2 H2O, 0.016 g MgSO4 x 7 H2O, 0.04 g K2HPO4, 0.04 g KH2PO4, 0.4 g NaHCO3, 0.08 g NaCl, 5 g Hipolypepton, 5 g Bacto Tryptone, 10 g Bacto Yeast Extract, 10 g Glucose, and 1 L distilled water.
- NBRC sets pH to 7.2.
- NBRC's asterisk on `Hipolypepton*` points only to the supplier footnote `Wako Pure Chemical Ind., Ltd., Osaka, Japan`.
- NBRC instructs mixing ingredients and autoclaving under an N2 atmosphere.

## Completeness

- The salts, Glucose, Bacto Yeast Extract, and Bacto Tryptone are present.
- The 5 g Hipolypepton source row was migrated from `ingredients` to an empty `solutions` stub.
- The 1 L Distilled water row is present as `1` `G_PER_L`.
- The pH 7.2 target is absent.
- N2 is present as a variable ingredient, but the autoclave-under-N2 instruction is absent from preparation steps.

## Findings

- Blocker: `Hipolypepton*` is a 5 g ingredient with a supplier footnote, not a solution. Migrating it to an empty `solutions` stub removes a required peptone component from the usable ingredient list.
- Major: 1 L Distilled water is represented as `1` `G_PER_L`, conflating source volume with a mass concentration.
- Major: the source pH 7.2 adjustment is not represented.
- Minor: the source N2 atmosphere survives only as a variable `N2` ingredient and loses the autoclaving context.

## Recommended Edits

- Keep Hipolypepton as a 5 g/L ingredient and preserve the Wako Pure Chemical supplier footnote as a note, not as a solution.
- Preserve the 1 L Distilled water row as a volume or final-volume statement rather than `G_PER_L`.
- Add a structured pH value of 7.2 or a preparation step that records the adjustment.
- Preserve the instruction to mix all ingredients and autoclave under N2.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting TOGO solution migration.
- Recompare the regenerated record against NBRC `NBRC_M1322`, especially the Hipolypepton row, pH target, water unit, and N2 autoclave instruction.
- Confirm with a gitignore-independent exact identifier search that TOGO `M2030` remains represented by only one generated record.

## Additional Notes

None found.
