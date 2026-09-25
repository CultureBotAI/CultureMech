# YAML Record Review: Thermaerobacter TY Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermaerobacter_ty_medium__cc9fc2e5.yaml
- Started UTC: 2026-09-25T11:34:05Z
- Finished UTC: 2026-09-25T11:38:50Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M758, Thermaerobacter TY Medium.
- The record was merged from `TOGO_M758_Thermaerobacter_TY_Medium`.
- The checked sources were the normalized TOGO M758 record, TOGO M758, JCM Medium 734, and MediaDive J734.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; exited 0 after startup diagnostics and emitted no failed checks.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- TOGO M758 cites JCM M734-2 and the JCM Medium 734 page.
- JCM Medium 734 is THERMAEROBACTER TY MEDIUM, matching the direct MediaDive/JCM J734 import.
- An exact `TOGO:M758`, `TOGO_M758`, and `mediadive.medium:J734` search used `rg --no-ignore --hidden` scoped to `data`; it found this TOGO M758 record as a separate generated record from the direct JCM J734 import.

## Evidence

- JCM Medium 734 lists 1 g tryptone, 2 g yeast extract, 1 g NaCl, 1 g MgSO4 x 7 H2O, 2 g CaCl2 x 2 H2O, and 1 L distilled water.
- JCM Medium 734 adds a separate preparation note: for solid medium, add 20.0 g/L gellan gum.
- MediaDive J734 keeps the same 1 L main solution and stores the 20 g/L gellan gum statement as a step rather than as a main-medium ingredient.
- TOGO M758 lists the same six main rows plus a blank gellan gum row.

## Completeness

- The core TY Medium solute amounts are present.
- The 1 L water row is encoded as 1 G_PER_L.
- The 20 g/L solid-medium gellan gum note is not preserved; gellan gum was defaulted to a variable-concentration ingredient while the recipe is still typed as `LIQUID`.
- The record is not merged or duplicate-linked with the direct JCM J734 import.

## Findings

- Distilled water has a unit error: the source gives 1 L, but the YAML stores `1 G_PER_L`.
- The optional solid-medium branch was mis-modeled as variable gellan gum in a liquid parent medium.
- The TOGO M758 transcription and direct JCM J734 import describe the same JCM 734 formula but remain separate generated records.

## Recommended Edits

- Regenerate TOGO M758 so the 1 L water row is retained as a volume or deliberately omitted.
- Preserve the 20 g/L gellan gum solid-medium branch as a preparation note or `MediaVariant` instead of a variable ingredient in the liquid parent formula.
- Merge or source-duplicate-link the corrected TOGO M758 record with the direct JCM J734 import.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that JCM 734 has one canonical CultureMech recipe or explicit TOGO/JCM source-duplicate links after the optional gellan gum branch is modeled.

## Additional Notes

- None found.
