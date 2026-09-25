# YAML Record Review: Thermoanaeromonas Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoanaeromonas_medium__1ea5b1c7.yaml
- Started UTC: 2026-09-25T11:49:20Z
- Finished UTC: 2026-09-25T11:52:26Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M808, Thermoanaeromonas Medium.
- The record was generated directly from `TOGO_M808_Thermoanaeromonas_Medium`.
- The checked sources were TOGO M808, JCM Medium 778, and MediaDive J778.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to TOGO Medium M808.
- TOGO M808 cites JCM Medium 778 as its original source.
- This TOGO transcription is separate from the direct JCM 778 generated record.

## Evidence

- JCM 778 lists a 1 L main recipe with 10 ml Trace minerals, 1 mg Resazurin, 1 L Distilled water, and 1 g/L each of Yeast extract and Trypticase peptone.
- JCM 778 instructs the curator to add 25 ml 8% NaHCO3 solution, 8 ml 5.0% Na2S x 9H2O solution, and 20 ml 1 M Glucose solution per liter after autoclaving.
- TOGO M808 preserves the same main recipe, JCM 778 provenance, and post-autoclave solution additions.
- The JCM 778 preparation uses an N2-CO2 4:1 gas mixture.

## Completeness

- The main inorganic and complex nutrient rows are present.
- Trace minerals and the three post-autoclave solution additions are present in `solutions`.
- The 1 L Distilled water row is represented as 1 G_PER_L.
- The source solution volumes were stored as G_PER_L amounts rather than solution-addition volumes.

## Findings

- The 1 L Distilled water row was converted to 1 G_PER_L instead of preserved as a 1 L solvent volume.
- The 1 mg Resazurin row was converted to 1 G_PER_L instead of 0.001 G_PER_L.
- The 10 ml Trace minerals addition was stored as 10 G_PER_L in `solutions`.
- The 25 ml 8% NaHCO3 solution, 20 ml 1 M Glucose solution, and 8 ml 5.0% Na2S x 9H2O solution additions were stored as 25, 20, and 8 G_PER_L instead of volume additions with stock strengths.

## Recommended Edits

- Regenerate TOGO M808 with Distilled water retained as a 1 L source volume or normalized to an explicit 1000 ml water row.
- Convert milligram amounts to G_PER_L by dividing by 1000 before final-volume normalization.
- Preserve the Trace minerals, 8% NaHCO3, 1 M Glucose, and 5.0% Na2S x 9H2O rows as solution additions with milliliter amounts.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that corrected TOGO M808 has no 1 G_PER_L water, 1 G_PER_L Resazurin, or solution-volume values stored under G_PER_L.

## Additional Notes

- None found.
