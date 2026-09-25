# YAML Record Review: thiomonas_medium__e90b5a7b

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thiomonas_medium__e90b5a7b.yaml`
- Started UTC: 2026-09-25T13:09:00Z
- Finished UTC: 2026-09-25T13:09:00Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:010023`
- Name: `thiomonas_medium`
- Source grounding: TOGO M623 and M624 derived from JCM Medium 615, `THIOMONAS MEDIUM`

## Validation

- Schema validation: passed with no issues.
- Strict validation: passed with zero errors; `/private/tmp/thiomonas_medium__e90b5a7b.strict.tsv` was header-only.
- Reference validation: passed with zero checks.
- Term validation: passed after the known EUtils warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The merged record is grounded to `TOGO:M623`.
- `TOGO:M623` and `TOGO:M624` both cite the same JCM GRMD 615 page.
- JCM 615 defines a base `THIOMONAS MEDIUM` at pH 6.0 and gives a pH 7.5 adjustment specifically for strain JCM 14806.
- The exact source search found only the expected M623/M624 local sources for JCM 615; the search included ignored and hidden files.

## Evidence

- The JCM 615 page lists yeast extract 5 g, Na2S2O3 x 5 H2O 5 g, KH2PO4 1.5 g, Na2HPO4 4.5 g, MgSO4 x 7 H2O 0.1 g, NH4Cl 0.3 g, agar 15 g, and 1 L distilled water.
- The base recipe is adjusted to pH 6.0.
- JCM 615 separately notes that strain JCM 14806 uses pH 7.5.
- TOGO M623 carries the pH 6.0 base and TOGO M624 carries the pH 7.5 strain variant.

## Completeness

- The ingredient list is complete for the JCM 615 base formulation.
- The generated record has no `ph_value` or `ph_range`.
- The generated record has no `target_organisms`; there are no growth claims to verify.

## Findings

- The M624 pH 7.5 JCM 14806 variant was merged into the M623 pH 6.0 base as an exact source duplicate.
- The merged record lost both source pH values; it has neither the pH 6.0 base value nor a variant describing the pH 7.5 strain-specific adjustment.
- The imported solvent row records `Distilled water` as `1` `G_PER_L`, which preserves neither the source volume unit nor the usual water-as-solvent semantics.

## Recommended Edits

- Keep the JCM 615 base at pH 6.0.
- Model the JCM 14806 pH 7.5 condition as a strain-specific or pH variant instead of an exact duplicate.
- Preserve the 1 L water row as solvent volume or omit it from mass-concentration rows according to local convention.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after pH repair.
- Confirm any downstream merge code keeps same-composition, different-pH media as variants.

## Additional Notes

- Empty optional fields were not treated as defects.
