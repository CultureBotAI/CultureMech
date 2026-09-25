# YAML Record Review: ebios_glucose_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/ebios_glucose_agar__f620f7f5.yaml
- Started UTC: 2026-09-22T23:04:15Z
- Finished UTC: 2026-09-22T23:04:49Z
- Verdict: needs curation

## Target

Generated JCM/MediaDive J969 record `CultureMech:003317`, named `ebios_glucose_agar`.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation against `scripts/validate_strict.py`: passed with 0 error rows.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the focused history validator targets standalone files under `history/`, not inline `MediaRecipe.curation_history` entries.

## Identity and Grounding

The JCM J969 identity and link are correct. Exact ignored-inclusive source searches for J969 / JCM_M969 also found the duplicate Togo M1019 generated record at `data/merge_yaml/merged/ebios_glucose_agar.yaml`; the direct JCM and Togo copies come from the same JCM page but did not merge.

Glucose and agar are grounded correctly. EBIOS dried yeast tablets are an undefined product and reasonably have no ChEBI term.

## Evidence

JCM 969 lists 10 g EBIOS dried yeast tablets, 20 g glucose, 15 g agar, and 1 L distilled water for EBIOS-Glucose Agar. The JCM page also says to autoclave media at 121 C for 15 minutes unless otherwise stated and adds the note that the pH is not adjusted.

The generated JCM record keeps the three non-water mass concentrations exactly. It omits distilled water instead of misrepresenting it, but it also fails to state that the recipe is made to a 1 L final volume.

## Completeness

The substantive recipe is mostly complete, but the final volume basis and default sterilization step are absent. The only preparation entry is a `MIX` step whose description is actually the EBIOS vendor footnote plus the pH-not-adjusted note; the pH note is useful, but it should not be typed as a mixing instruction.

## Findings

- The equivalent JCM J969 and TOGO M1019 imports failed to merge, creating two generated records for one source recipe.
- The 1 L distilled-water basis is absent; all g/L values are correct, but the volume basis should still be preserved.
- JCM's default "autoclave at 121 C for 15 min" instruction was dropped.
- The pH-not-adjusted note is hidden inside a `MIX` preparation step along with the EBIOS vendor footnote.

## Recommended Edits

- Merge this JCM J969 record with the TOGO M1019 record once water/final-volume normalization is fixed.
- Preserve the JCM 1 L distilled-water basis without generating a `1 G_PER_L` water ingredient.
- Add the JCM default autoclave instruction and carry `pH not adjusted` as a note or pH policy rather than as a `MIX` step.
- Preserve both `mediadive.medium:J969` and `TOGO:M1019` as structured source identities on the canonical generated record.

## Follow-up Checks

- Re-run open, strict, reference, and term validators after rebuilding.
- Compare the rebuilt record against JCM 969 and Togo M1019.
- Search with ignored files included for stale split `ebios_glucose_agar` generated records after regeneration.

## Additional Notes

The generated record has no explicit organism growth data to review.
