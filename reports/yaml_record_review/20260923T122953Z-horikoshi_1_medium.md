# YAML Record Review: HORIKOSHI-1 medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/horikoshi_1_medium.yaml
- Started UTC: 2026-09-23T12:28:53Z
- Finished UTC: 2026-09-23T12:29:53Z
- Verdict: needs curation

## Target

Reviewed the generated merged Horikoshi-1 branch at `data/merge_yaml/merged/horikoshi_1_medium.yaml`. The generated record is grounded to KOMODO Medium 1081 but merges DSMZ Medium 1081 and DSMZ Medium 1081a sources.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/horikoshi_1_medium.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The retained identity is `komodo.medium:1081`, `HORIKOSHI-1 medium`, which points to DSMZ Medium 1081. The merge also absorbs KOMODO 1081a and KOMODO 1081a_18086 records that denote DSMZ Medium 1081a, `HORIKOSHI-1 MEDIUM WITH 10% NaCl`, a real variant that adds 100 g NaCl to Main sol. 1081.

## Evidence

DSMZ 1081 lists glucose, polypeptone, yeast extract, K2HPO4, MgSO4 x 7 H2O, agar, and 900 ml distilled water, then adds 100 ml of 10% Na2CO3 after autoclaving and checks the final pH around 10.0. MediaDive 1081a represents DSMZ 1081a as 1000 ml of Main sol. 1081 plus 100 g NaCl.

The direct DSMZ `data/normalized_yaml/bacterial/horikoshi_1_medium.yaml` source preserves the post-autoclave Na2CO3 preparation text. The KOMODO 1081 and 1081a normalized files copied only the DSMZ 1081 ingredient signature; they lack 900 ml water, lack the late carbonate step, and the 1081a files lack the 100 g NaCl row that makes 1081a distinct.

## Completeness

The generated record has the base non-water DSMZ 1081 ingredients and pH, but no preparation steps and no 900 ml distilled water. It also demotes 1081a and the DSM 18086 1081a modification to synonyms rather than preserving them as a NaCl concentration variant.

## Findings

- DSMZ Medium 1081 and DSMZ Medium 1081a were merged even though 1081a adds 100 g NaCl.
- The two 1081a maintained sources are incomplete; they were populated from DSMZ 1081 and lost the 100 g NaCl addition.
- The merged record lacks the 900 ml distilled-water row from DSMZ 1081.
- The merged record represents Na2CO3 as an unconditional 10 G_PER_L ingredient instead of a 100 ml post-autoclave 10% stock addition.
- The source-backed DSMZ 1081 preparation text was dropped because the KOMODO 1081 branch became canonical.

## Recommended Edits

- Keep DSMZ/KOMODO 1081a records separate from the base 1081 record, or model them as explicit NaCl concentration variants.
- Repair `data/normalized_yaml/bacterial/KOMODO_1081a_HORIKOSHI-1_medium_WITH_10_NaCl.yaml` and `data/normalized_yaml/bacterial/medium_1081a_modified_for_dsm_18086.yaml` so they include the 100 g NaCl addition.
- Preserve the DSMZ 1081 900 ml distilled-water row and the 100 ml late 10% Na2CO3 stock addition.
- Ensure canonical merge selection retains source-backed preparation steps.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Confirm regenerated 1081a records have NaCl at 100 g/L and are not synonyms of the base Horikoshi-1 medium.
- Re-open DSMZ 1081 and MediaDive 1081a to confirm water, Na2CO3, pH, and NaCl handling.

## Additional Notes

None.
