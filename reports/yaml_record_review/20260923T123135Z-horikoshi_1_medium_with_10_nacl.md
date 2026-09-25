# YAML Record Review: HORIKOSHI-1 MEDIUM WITH 10% NaCl
- Repository: CultureMech
- Record: data/merge_yaml/merged/horikoshi_1_medium_with_10_nacl.yaml
- Started UTC: 2026-09-23T12:30:57Z
- Finished UTC: 2026-09-23T12:31:35Z
- Verdict: needs curation

## Target

Reviewed the generated direct DSMZ branch for DSMZ Medium 1081a, `HORIKOSHI-1 MEDIUM WITH 10% NaCl`, at `data/merge_yaml/merged/horikoshi_1_medium_with_10_nacl.yaml`. The maintained source is `data/normalized_yaml/bacterial/horikoshi_1_medium_with_10_nacl.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/horikoshi_1_medium_with_10_nacl.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is grounded to `mediadive.medium:1081a`, DSMZ Medium 1081a `HORIKOSHI-1 MEDIUM WITH 10% NaCl`, and correctly represents the defining 100 g/L NaCl addition to Medium 1081.

## Evidence

DSMZ 1081a instructs users to use DSMZ Medium 1081 and add 100 g NaCl. DSMZ 1081 contains glucose, polypeptone, yeast extract, K2HPO4, MgSO4 x 7 H2O, 15 g agar, and 900 ml distilled water, then directs addition of 100 ml of 10% Na2CO3 after autoclaving and checking the final pH around 10.0.

The generated record includes the 100 g NaCl row and all non-water Medium 1081 rows. It flattens the 10% Na2CO3 addition to 10 G_PER_L and omits the inherited 900 ml distilled-water row.

## Completeness

The record retains the 1081a overlay instruction and the inherited DSMZ 1081 post-autoclave carbonate instruction as preparation prose. It does not carry the inherited final pH of about 10.0 as a structured pH value, and it does not distinguish the late Na2CO3 stock addition from ordinary pre-autoclave ingredients.

## Findings

- The inherited 900 ml distilled-water row from DSMZ Medium 1081 is missing.
- The 100 ml post-autoclave 10% Na2CO3 solution is represented as an unconditional 10 G_PER_L ingredient.
- The inherited final pH of about 10.0 is missing from structured pH fields.

## Recommended Edits

- Restore the inherited 900 ml distilled-water row in `data/normalized_yaml/bacterial/horikoshi_1_medium_with_10_nacl.yaml`.
- Represent the 10% Na2CO3 addition as a late stock addition, or keep it as a final concentration while preserving the late-addition semantics.
- Carry the inherited final pH of about 10.0 into a structured pH field.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Re-open DSMZ 1081 and 1081a to confirm the regenerated variant contains all Medium 1081 rows, the 100 g NaCl addition, and the inherited post-autoclave carbonate step.

## Additional Notes

None.
