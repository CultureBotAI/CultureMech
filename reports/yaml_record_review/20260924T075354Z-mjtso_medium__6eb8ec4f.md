# YAML Record Review: mjtso_medium__6eb8ec4f

- Repository: CultureMech
- Record: data/merge_yaml/merged/mjtso_medium__6eb8ec4f.yaml
- Started UTC: 2026-09-24T07:53:54Z
- Finished UTC: 2026-09-24T07:54:17Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002796`
- Generated name: `mjtso_medium`
- Generated source file: `data/merge_yaml/merged/mjtso_medium__6eb8ec4f.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/mjtso_medium.yaml`
- Upstream source: MediaDive/JCM medium `J446`, `MJTSO MEDIUM`

## Validation

- Open LinkML validation passed: `No issues found`.
- Strict validation passed with 0 ERROR rows in `/private/tmp/mjtso_medium__6eb8ec4f.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The generated record identity is aligned with MediaDive/JCM `J446`.
- The `media_term` points to `mediadive.medium:J446`.
- `Na2WO2 x 2 H2O` lacks ontology grounding and preserves the source formula typo for sodium tungstate.
- `NiSO4 x 6 H2O` is grounded to generic nickel sulfate.

## Evidence

- MediaDive `J446` main solution `4193` contains 1000 ml water plus 3 g NaCl, 0.34 g `MgCl2 x 6 H2O`, 0.42 g `MgSO4 x 7 H2O`, 0.05 g KCl, 0.14 g K2HPO4, 0.25 g NH4Cl, 0.07 g `CaCl2 x 2 H2O`, 10 ml Trace mineral solution `4194`, 1 g `Na2S2O3 x 5 H2O`, 3 g sulfur, and 1 g NaHCO3.
- MediaDive Trace mineral solution `4194` is a 1000 ml stock containing Na2-EDTA, CoCl2, MnCl2, FeSO4, ZnCl2, AlCl3, `Na2WO2 x 2 H2O`, CuCl2, NiSO4, selenous acid, H3BO3, Na2MoO4, and water.
- The generated direct main-solution rows match MediaDive's final `g_l` values.
- The generated rows from Na2-EDTA through Na2MoO4 match raw Trace mineral solution `4194` concentrations even though the main solution uses only 10 ml of that stock.

## Completeness

- The generated record has no `solutions` array.
- The 10 ml Trace mineral solution `4194` addition was flattened into direct top-level rows at raw stock concentration.
- The 8% NaHCO3 addition survives only as a final direct NaHCO3 ingredient plus preparation prose.
- Water rows for the main solution and trace-mineral stock are not represented structurally.

## Findings

- High: The 10 ml Trace mineral solution stock was flattened at undiluted stock concentration.
- Medium: The 8% NaHCO3 stock semantics were not preserved.
- Medium: `Na2WO2 x 2 H2O` lacks ontology grounding.
- Medium: `NiSO4 x 6 H2O` is grounded to generic nickel sulfate.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/mjtso_medium.yaml` with an explicit 10 ml Trace mineral solution `4194` addition.
- Dilute the Trace mineral stock through the 10 ml addition to the 1010 ml J446 main solution, or preserve it as a nested stock with its usage volume recorded.
- Represent bicarbonate as an 8% NaHCO3 stock addition while preserving the final 1 g mass.
- Regenerate the merged record after repairing the normalized source.

## Follow-up Checks

- Re-fetch MediaDive `J446` and verify no raw `4194` stock concentration is present as a direct final-medium concentration.
- Confirm the 10 ml Trace mineral addition and 8% NaHCO3 addition are preserved.
- Confirm the sodium tungstate source typo is either intentionally preserved with grounding or corrected with a curation note.
- Re-run open LinkML, strict, reference, and term validation after regenerating the merged record.

## Additional Notes

- None found.
