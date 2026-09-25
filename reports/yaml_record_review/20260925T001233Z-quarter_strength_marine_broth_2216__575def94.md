# YAML Record Review: quarter_strength_marine_broth_2216
- Repository: CultureMech
- Record: data/merge_yaml/merged/quarter_strength_marine_broth_2216__575def94.yaml
- Started UTC: 2026-09-25T00:12:33Z
- Finished UTC: 2026-09-25T00:13:24Z
- Verdict: needs curation

## Target
Reviewed generated record `data/merge_yaml/merged/quarter_strength_marine_broth_2216__575def94.yaml`.

Owner record:

- `data/normalized_yaml/specialized/quarter_strength_marine_broth_2216.yaml`
- `merge_fingerprint`: `575def948e7e7cae04e28c45029f8f253a37b20a69aa9f1cbd11ebc7b4fe6757`
- `merged_from`: `quarter_strength_marine_broth_2216`

The generated YAML is stale relative to the current specialized owner: a 2026-09-06 repair added the missing distilled-water row, JCM reference, and source notes to `data/normalized_yaml/specialized/quarter_strength_marine_broth_2216.yaml`, but the generated file still contains only the `Marine broth 2216` ingredient.

## Validation
- Open LinkML validation against `MediaRecipe`: passed; no issues found.
- Strict validation: passed; `/private/tmp/quarter_strength_marine_broth_2216__575def94.strict.tsv` was header-only with 0 data rows.
- LinkML reference validation: passed; 0 reference checks, all validations passed.
- LinkML term validation with labels: passed.
- Owner spot-check: the current specialized owner also passed open and strict validation after its water-row repair.
- Embedded history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding
- Identity is correct for JCM `1049`, Quarter Strength Marine Broth 2216.
- Live JCM 1049 lists only `Marine broth 2216 (BD-Difco)` 9.35 g and distilled water 1 L.
- The exact ignored-file search for `mediadive.medium:J1049`, `JCM_J1049`, and `GRMD=1049` found this specialized owner and generated target, plus a bacterial TOGO M1115 owner and generated `Quarter_Strength_Marine_Broth_2216.yaml` for the same JCM page.

## Evidence
- The reviewed generated file still has the pre-repair direct JCM form with only `Marine broth 2216` at 9.35 g/L.
- `data/normalized_yaml/specialized/quarter_strength_marine_broth_2216.yaml` now has the complete JCM 1049 formula: `Marine broth 2216 (BD-Difco)` 9.35 g and distilled water 1.0 L.
- `data/normalized_yaml/bacterial/quarter_strength_marine_broth_2216.yaml` is a TOGO M1115 owner for the same JCM 1049 page and now also carries the repaired 9.35 g/L quarter-strength concentration and distilled water.

## Completeness
The current specialized owner is complete for the simple JCM 1049 formula. The generated record is incomplete because it predates that repair and omits distilled water.

## Findings
1. The generated file is stale and still omits the 1 L distilled-water row that the current specialized owner already added.
2. The same JCM 1049 source is still present through a bacterial TOGO M1115 owner and generated sibling, so two source routes for Quarter Strength Marine Broth 2216 have not been deduplicated.

## Recommended Edits
1. Regenerate `data/merge_yaml/merged/quarter_strength_marine_broth_2216__575def94.yaml` from `data/normalized_yaml/specialized/quarter_strength_marine_broth_2216.yaml` so distilled water and the September repair metadata reach the generated layer.
2. Merge or retire the bacterial TOGO M1115 owner after choosing a single canonical Quarter Strength Marine Broth 2216 record and preserving the concentration-variant relationship to full-strength Marine Broth 2216.

## Follow-up Checks
- Re-run open LinkML, strict, reference, and term validators for the regenerated specialized record.
- Re-run exact ignored-file searches for `mediadive.medium:J1049`, `JCM_J1049`, and `GRMD=1049` to confirm the TOGO M1115 exact-source duplicate has been intentionally merged or retired.

## Additional Notes
None.
