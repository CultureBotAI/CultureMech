# YAML Record Review: nutrient_broth_with_1_0_nacl

- Repository: CultureMech
- Record: `data/merge_yaml/merged/nutrient_broth_with_1_0_nacl.yaml`
- Started UTC: 2026-09-24T18:35:10Z
- Finished UTC: 2026-09-24T18:36:13Z
- Verdict: needs curation

## Target

Generated bacterial record `CultureMech:009783`, `nutrient_broth_with_1_0_nacl`, merging TOGO M3/JCM 7 with its TOGO M5/JCM 12 0.5% NaCl salinity variant.

## Validation

Open LinkML validation passed with `No issues found`.

Strict validation passed; `/private/tmp/nutrient_broth_with_1_0_nacl.strict.tsv` contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: the history validator operates over standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The TOGO M3 parent is grounded to the intended source: TOGO M3 mirrors JCM Medium 7, `NUTRIENT BROTH WITH 1.0% NaCl`.

The TOGO M5 parent is also a real related source, but it is JCM Medium 12, `NUTRIENT BROTH WITH 0.5% NaCl`. The normalized records correctly annotate that relationship as `SALINITY_VARIANT`, not `SOURCE_DUPLICATE`.

An exact ignored-inclusive, hidden-inclusive search for `TOGO:M3`, `GMDB:M3`, `TOGO:M5`, `GMDB:M5`, `JCM_M7`, `GRMD=7`, `JCM_M12`, `GRMD=12`, both TOGO source slugs, and the two nutrient-broth slugs found the expected TOGO normalized records, parallel direct JCM normalized records, generated merge artifacts for both import paths, and source/deep-research index rows.

## Evidence

TOGO M3 and JCM Medium 7 list 5 g Bacto peptone, 3 g Beef extract, 10 g NaCl, 1 L Distilled water, and pH 7.0.

TOGO M5 and JCM Medium 12 list the same base formulation but lower NaCl: 5 g Bacto peptone, 3 g Beef extract, 5 g NaCl, 1 L Distilled water, and pH 7.0.

The generated record preserves the TOGO M3 10 g/L NaCl value and correctly describes the M5 parent as a salinity variant with NaCl increased from 5 g/L to 10 g/L.

## Completeness

Both normalized TOGO parents still carry the imported water-unit error: `Distilled water` is `1 G_PER_L` instead of the source-supported 1000 ml/L. Both TOGO parents also lack the source pH 7.0 and the source `Adjust pH to 7.0` preparation step.

The generated record is structurally incomplete because two salinity variants were merged into one canonical YAML. The 0.5% NaCl source survives only as a synonym and `merged_from` member even though it is a distinct formula.

Direct JCM normalized siblings for the same JCM 7 and JCM 12 media are present, so the TOGO records should be reconciled to those corresponding direct JCM records once both paths have been repaired.

## Findings

Needs curation:

- The generated YAML merges TOGO M3 and TOGO M5 even though the records differ by NaCl concentration and are only `SALINITY_VARIANT` records.
- `Distilled water` is encoded as `1 G_PER_L`; each source record lists `1 L Distilled water`.
- The TOGO parents and this generated record are missing the JCM-supported pH 7.0 and pH-adjustment step.
- The 0.5% NaCl TOGO source is demoted to a synonym on the 1.0% NaCl generated record, which conflates two source formulas.

## Recommended Edits

Repair the two TOGO normalized records first:

- Convert `Distilled water` to `1000 ML_PER_L` in both TOGO M3 and TOGO M5.
- Add pH 7.0 and an `ADJUST_PH` step to both records.
- Keep `TOGO_M3_Nutrient_Broth_With_1.0_NaCl` and `TOGO_M5_Nutrient_Broth_With_0.5_NaCl` as separate normalized records connected by `SALINITY_VARIANT`.
- Reconcile TOGO M3 with the direct JCM 7 record as the same source formula, and TOGO M5 with the direct JCM 12 record as the same source formula, after preserving the 10 g/L versus 5 g/L NaCl distinction.

Regenerate the merged YAML so the 1.0% and 0.5% NaCl formulas remain separate generated records rather than `merged_from` siblings in one artifact.

## Follow-up Checks

After repair, rerun open schema, strict, reference, and term validation for the regenerated YAMLs. Confirm the TOGO M3/JCM 7 generated record has 10 g/L NaCl, the TOGO M5/JCM 12 generated record has 5 g/L NaCl, both have 1000 ml/L Distilled water and pH 7.0, and neither lists the other salinity variant under `merged_from`.

## Additional Notes

None found.
