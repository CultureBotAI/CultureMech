# YAML Record Review: thiobacillus_prosperus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thiobacillus_prosperus_medium__a7863b37.yaml
- Started UTC: 2026-09-25T13:01:00Z
- Finished UTC: 2026-09-25T13:01:24Z
- Verdict: needs curation

## Target

- Generated YAML for the TOGO M1153 Thiobacillus Prosperus Medium import derived from JCM_M1084.
- The record was merged from `TOGO_M1153_Thiobacillus_Prosperus_Medium`.
- The checked sources were TOGO M1153, JCM 1084 via the TOGO metadata, and MediaDive J1084.

## Validation

- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to TOGO M1153.
- TOGO M1153 identifies the original source as JCM_M1084 with a JCM GRMD 1084 URL.
- A separate exact JCM/MediaDive J1084 import exists for THIOBACILLUS PROSPERUS MEDIUM.

## Evidence

- JCM/TOGO M1153 uses 940 ml distilled water, basal salts, 2 mg NiCl2 x 6 H2O, 10 ml trace mineral solution, and a 50 ml FeSO4 x 7H2O solution addition.
- TOGO stores the FeSO4 stock as 40 g FeSO4 x 7H2O in 100 ml 0.1 N H2SO4 and notes N2 storage for that stock.
- MediaDive J1084 confirms the pH 2.5 JCM parent recipe, 10 ml trace mineral solution, and 50 ml FeSO4 stock addition.

## Completeness

- The parent identity and most source component names are present.
- The record has no `ph_value` even though the JCM parent medium is pH 2.5.
- TOGO milliliter and liter volumes were imported as `G_PER_L` concentrations, including 940 g/L for distilled water and 100 g/L for H2SO4 stock solvent.
- The parsed `solutions` entries have empty `composition` arrays and their 10 ml, 50 ml, and 1 L quantities were also converted to `G_PER_L`.

## Findings

- The TOGO source volumes are unit-swapped into final g/L ingredient values.
- The 2 mg basal nickel row is merged with a 0.03 g trace-stock nickel row to make a false 2.03 g/L top-level ingredient.
- The 40 g FeSO4 stock row and 100 ml H2SO4 solvent row were copied into the final ingredient list instead of remaining inside the 50 ml stock addition.
- N2 from the FeSO4 storage instruction is modeled as a top-level variable ingredient.
- The pH 2.5 source condition is omitted.

## Recommended Edits

- Prefer the exact JCM/MediaDive J1084 import or rebuild TOGO M1153 with explicit volume units.
- Model the 10 ml trace mineral solution and 50 ml FeSO4 solution as stock additions.
- Remove N2 as a final ingredient and keep it as stock-storage context.
- Restore pH 2.5 and parent preparation text from JCM 1084.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that TOGO volume units are not normalized to `G_PER_L`.
- Verify that M1153 and the direct JCM J1084 record are deduplicated or explicitly linked as source duplicates.

## Additional Notes

- None found.
