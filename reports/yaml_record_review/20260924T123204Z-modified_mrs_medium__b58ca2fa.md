# YAML Record Review: modified_mrs_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_mrs_medium__b58ca2fa.yaml
- Started UTC: 2026-09-24T12:32:04Z
- Finished UTC: 2026-09-24T12:32:04Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:002649`, `modified_mrs_medium`, generated from `data/normalized_yaml/bacterial/modified_mrs_medium.yaml`.
- The record represents JCM Medium J291 / MediaDive `mediadive.medium:J291`, named `MODIFIED MRS MEDIUM`.
- The generated record was compared with the maintained MediaDive normalized record, JCM `GRMD=291`, MediaDive `J291`, and the parallel TOGO `M285` import of the same JCM source.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- MediaDive `J291`, JCM `GRMD=291`, and TOGO `M285` all identify the same Modified MRS Medium source recipe.
- A gitignore-independent duplicate check for the exact normalized name and JCM/MediaDive identifiers found `data/normalized_yaml/bacterial/TOGO_M285_Modified_MRS_Medium.yaml` and the generated `data/merge_yaml/merged/MODIFIED_MRS_MEDIUM.yaml` as a second CultureMech representation of JCM 291.
- The maintained MediaDive and TOGO normalized records both already contain `SOURCE_DUPLICATE` links documenting that they import the same JCM 291 formulation.
- No inspected JCM, MediaDive, or TOGO source payload identified a target organism for this medium.

## Evidence

- JCM lists 55.0 g Lactobacilli MRS broth from BD-Difco, 0.5 g L-Cysteine HCl x H2O, and 1.0 L distilled water, followed by an instruction to adjust pH to 6.5.
- MediaDive `J291` preserves the same three-row recipe, including the `BD-Difco` attribute on Lactobacilli MRS broth and the 1000 ml distilled-water row.
- The current maintained MediaDive normalized record has the water row, the vendor-qualified `Lactobacilli MRS broth (BD-Difco)` label, explicit 1.0 L water, a mix step, an adjust-pH step, default JCM autoclave evidence, references, and a source-duplicate link to TOGO `M285`.
- The generated merged YAML still has only the broth and cysteine rows, lacks the distilled-water row, truncates the BD-Difco qualifier from the commercial medium name, lacks the mix and default autoclave steps, and lacks the source-duplicate metadata.

## Completeness

- The two non-water JCM ingredients are present at the source quantities.
- The 1.0 L distilled-water row is missing from the generated record.
- The generated commercial-medium row drops the `BD-Difco` source qualifier that is present in JCM, MediaDive, and the maintained normalized record.
- September 2026 curation fields from the maintained normalized record are absent from generated YAML, including references, the repaired preparation steps, sterilization details, and source-duplicate links.

## Findings

- Blocker: `data/merge_yaml/merged/modified_mrs_medium__b58ca2fa.yaml` is stale relative to `data/normalized_yaml/bacterial/modified_mrs_medium.yaml`. The maintained owner has the repaired JCM 291 water row, vendor-qualified broth row, JCM evidence, default autoclave metadata, and TOGO M285 duplicate link, but the generated record still reflects the older two-ingredient import.
- Major: the generated record omits the 1.0 L distilled-water row listed by JCM and MediaDive.
- Major: the generated record drops the `BD-Difco` attribute from `Lactobacilli MRS broth`, making the commercial ingredient less specific than the source.
- Major: the same JCM 291 medium still appears as a separate TOGO-generated record even though both maintained normalized records already identify the relationship as a source duplicate.

## Recommended Edits

- Regenerate merged YAML from the current normalized MediaDive and TOGO records for JCM 291.
- Confirm that the regenerated MediaDive record keeps the 1.0 L distilled-water ingredient, the `Lactobacilli MRS broth (BD-Difco)` row, JCM references, the default autoclave step, and the source-duplicate metadata.
- Ensure the MediaDive `J291` and TOGO `M285` records merge or cross-link consistently so one JCM 291 formulation does not remain as two generated records.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after regeneration.
- Recompare the regenerated file against JCM `GRMD=291` and MediaDive `J291`.
- Confirm that generated YAML no longer contains both `modified_mrs_medium__b58ca2fa.yaml` and `MODIFIED_MRS_MEDIUM.yaml` as independent records for the same JCM recipe.

## Additional Notes

None found.
