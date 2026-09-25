# YAML Record Review: thiohalorhabdus_methylotrophus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thiohalorhabdus_methylotrophus_medium.yaml
- Started UTC: 2026-09-25T13:04:35Z
- Finished UTC: 2026-09-25T13:04:59Z
- Verdict: pass

## Target

- Generated YAML for the direct JCM GRMD 1405 THIOHALORHABDUS METHYLOTROPHUS MEDIUM import.
- The record was merged from `JCM_J1405_THIOHALORHABDUS_METHYLOTROPHUS_MEDIUM`.
- The checked source was the JCM 1405 medium page.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to local JCM GRMD 1405, THIOHALORHABDUS METHYLOTROPHUS MEDIUM.
- The JCM page agrees on medium 1405, the medium name, and pH 6.8.
- No duplicate or conflicting merge was observed.

## Evidence

- JCM 1405 lists 180 g NaCl, 5 g KCl, 2.5 g K2HPO4, and 0.2 g NH4Cl brought to 1 L with distilled water.
- JCM 1405 adds, after autoclaving and cooling, 1 ml 1 M MgSO4 solution, 1 ml trace element solution, 1 ml 0.002% CuCl2 x 2H2O solution, 5 ml trace vitamins, 20 ml 3% trimethylamine solution, and 1 ml 2 M sodium thiosulfate solution.
- JCM 1405 instructs use of culture vessels with more than 80% head space, butyl rubber stoppers, and shaking at the designated temperature.

## Completeness

- The basal salts, pH 6.8 adjustment, and post-autoclave stock-addition volumes are present.
- Filter-sterilized entries marked with source asterisks are preserved in the stock labels and preparation text.
- Head-space, stopper, and shaking instructions are present.

## Findings

- None found.

## Recommended Edits

- None found.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after any future regeneration.
- Verify JCM 1079 and JCM 197 only if their stock contents are expanded rather than referenced.

## Additional Notes

- None found.
