# YAML Record Review: HICKEY-TRESNER-AGAR
- Repository: CultureMech
- Record: data/merge_yaml/merged/hickey_tresner_agar.yaml
- Started UTC: 2026-09-23T12:03:14Z
- Finished UTC: 2026-09-23T12:03:59Z
- Verdict: needs curation

## Target

Reviewed the generated source-duplicate merge for DSMZ Medium 658, `HICKEY-TRESNER-AGAR`, at `data/merge_yaml/merged/hickey_tresner_agar.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/hickey_tresner_agar.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The generated record merges the direct DSMZ Medium 658 branch with the KOMODO Medium 658 mirror. Both normalized source records point to DSMZ 658 and have the same ingredient signature, so the duplicate merge is appropriate.

## Evidence

The DSMZ PDF lists 10.0 g dextrin, 2.0 g enzymatic digest of casein, 1.0 g meat extract, 1.0 g yeast extract, 2.0 mg CoCl2 x 6 H2O, 15.0 g agar, and 1000.0 ml distilled water, then instructs adjustment to pH 7.2. MediaDive 658 has the same pH and same final g/L concentrations.

The generated record keeps the six non-water ingredients at the correct concentrations and pH 7.2. It omits the 1000 ml distilled-water row, and the source-duplicate merge drops the direct DSMZ parent's `Adjust pH to 7.2.` preparation step.

## Completeness

The chemical formula and source identity are mostly complete, and the direct DSMZ/KOMODO merge is valid. Solvent handling and preparation-step preservation still need source-level or merge-level curation.

## Findings

- The 1000 ml distilled-water row is missing from both normalized parents and from the generated record.
- The generated merge omits the pH-adjustment preparation step that is present in the direct DSMZ normalized parent.
- The record has no explicit DSMZ PDF reference beyond free text in `notes`.

## Recommended Edits

- Add the 1000 ml distilled-water row to both DSMZ 658 normalized parents or to the import logic that produces them.
- Preserve the pH 7.2 adjustment step during source-duplicate merging.
- Add a structured reference to the DSMZ 658 PDF.
- Regenerate the merged artifact after the normalized parents are corrected.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Confirm the regenerated source-duplicate merge keeps one DSMZ/KOMODO record while preserving distilled water and the pH-adjustment step.

## Additional Notes

None.
