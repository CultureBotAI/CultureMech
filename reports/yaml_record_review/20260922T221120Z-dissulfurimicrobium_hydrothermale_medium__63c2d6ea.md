# YAML Record Review: dissulfurimicrobium_hydrothermale_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/dissulfurimicrobium_hydrothermale_medium__63c2d6ea.yaml`
- Started UTC: 2026-09-22T22:10:24Z
- Finished UTC: 2026-09-22T22:11:20Z
- Verdict: needs curation

## Target

`CultureMech:002214` represents JCM Medium J1030, `DISSULFURIMICROBIUM HYDROTHERMALE MEDIUM`, from MediaDive. The generated record is a single-source merge from `data/normalized_yaml/bacterial/dissulfurimicrobium_hydrothermale_medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

A gitignore-independent `find` over `data/` found this MediaDive/JCM J1030 generated record, a separate TOGO M1094 generated record for the same JCM page, the corresponding normalized sources, and a nearby but different Desulfacinum hydrothermale medium. The two Dissulfurimicrobium imports should converge after their shared JCM 1030 structure is repaired.

## Evidence

- The live MediaDive J1030 payload defines `Main sol. J1030` as a medium with 10 ml Trace elements solution, 10 ml Trace vitamins, 800 ml distilled water, sulfur, NaHCO3, and five basal salts.
- MediaDive defines Trace elements solution as a 1000 ml stock with eighteen milligram-scale salts plus 1000 ml water.
- MediaDive defines Trace vitamins as a 1000 ml stock with ten milligram-scale vitamins plus 1000 ml water.
- The live JCM 1030 page additionally lists 200 ml Ferrihydrite suspension in the main table and gives the final ferrihydrite wash, centrifugation, and 200 ml water suspension instruction.
- The JCM page instructs boiling and cooling under 100% CO2, addition of trace vitamins and NaHCO3 while gassing, pH adjustment to 6.5-6.8, dispensing under CO2, and autoclaving sealed culture vessels at 105 C for 1 hr.

## Completeness

The record is incomplete because both stocks were flattened into top-level ingredients, their water rows were dropped, and the direct JCM 1030 ferrihydrite suspension row is absent.

## Findings

- There is no `solutions` block for the 10 ml Trace elements solution.
- There is no `solutions` block for the 10 ml Trace vitamins addition.
- Trace-element and trace-vitamin child rows were promoted to top-level ingredients at stock strength.
- The 800 ml main water, 1000 ml trace-elements water, and 1000 ml trace-vitamins water rows are absent.
- The current JCM 1030 page lists 200 ml Ferrihydrite suspension in the main recipe, but that row is absent from the MediaDive-derived generated record.
- The ferrihydrite preparation omits the final JCM wash, centrifugation, supernatant removal, and 200 ml suspension instruction.

## Recommended Edits

- Restore Trace elements solution as a 1000 ml stock and add it to the main medium at 10 ml.
- Restore Trace vitamins as a 1000 ml stock and add it to the main medium at 10 ml.
- Move the trace-element salts, trace vitamins, and stock water rows under their source stocks.
- Compare live JCM 1030 against MediaDive J1030 and add the missing 200 ml Ferrihydrite suspension row if JCM remains authoritative.
- Preserve the full ferrihydrite preparation from JCM, including the final 200 ml water suspension.
- Regenerate both the MediaDive/JCM and TOGO/JCM Dissulfurimicrobium records so they converge or carry an explicit source-duplicate relationship.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that no Trace elements solution or Trace vitamins child remains as a top-level ingredient.
- Verify that generated preparation text includes the complete ferrihydrite wash and 200 ml suspension step.
- Verify that the MediaDive and TOGO JCM 1030 imports no longer emit as unrelated fingerprints unless source-backed differences remain.

## Additional Notes

None found.
