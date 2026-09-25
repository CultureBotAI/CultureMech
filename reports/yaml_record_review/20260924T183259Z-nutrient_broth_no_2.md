# YAML Record Review: nutrient_broth_no_2

- Repository: CultureMech
- Record: `data/merge_yaml/merged/nutrient_broth_no_2.yaml`
- Started UTC: 2026-09-24T18:32:59Z
- Finished UTC: 2026-09-24T18:32:59Z
- Verdict: needs curation

## Target

Generated bacterial record `CultureMech:008765`, `nutrient_broth_no_2`, from `TOGO:M2170` and NBRC Medium 1559.

## Validation

Open LinkML validation passed; the validator exited 0 with no diagnostics.

Strict validation passed; `/private/tmp/nutrient_broth_no_2.strict.tsv` contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: the history validator operates over standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated identity is grounded to the intended source medium. `TOGO:M2170` is Nutrient broth No.2 imported from NBRC Medium 1559, and an exact ignored-inclusive search for `TOGO:M2170`, `GMDB:M2170`, `M2170`, `NBRC_M1559`, `NO=1559`, `nutrient_broth_no_2`, and `Nutrient broth No.2` found only this generated record, its maintained normalized source, and expected generated/index/deep-research references.

## Evidence

TOGO M2170 and NBRC Medium 1559 agree on the core formula: 10 g Lab-Lemco powder, 10 g Peptone, 5 g Sodium chloride, 1 L Distilled water, and 15 g Agar if needed, adjusted to pH 7.5 +/- 0.2.

The generated non-water ingredients match those source values: Lab-Lemco powder 10 g/L, Peptone 10 g/L, Sodium chloride 5 g/L, and Agar if needed 15 g/L.

## Completeness

The generated record is stale relative to the maintained normalized source. `data/normalized_yaml/bacterial/nutrient_broth_no_2.yaml` has the repaired 1000 ml/L distilled water concentration, the pH 7.3-7.7 range, an `ADJUST_PH` preparation step, source annotations, ontology mappings for Lab-Lemco powder, Peptone, sodium chloride, agar, and water, `ingredients_curated` and `has_ontology_mappings` data-quality flags, and references to both TOGO M2170 and NBRC Medium 1559.

## Findings

Needs curation:

- `Distilled water` is encoded as `1 G_PER_L`; the source formula says `1 L Distilled water`, so the generated record currently reports one gram of water per final liter instead of 1000 ml/L.
- The generated record is stale relative to the repaired maintained YAML and is missing the source-supported pH range, pH-adjustment preparation step, ingredient source annotations, updated ontology mappings, data-quality flags, and references.

## Recommended Edits

Regenerate `data/merge_yaml/merged/nutrient_broth_no_2.yaml` from `data/normalized_yaml/bacterial/nutrient_broth_no_2.yaml` so the generated artifact carries the repaired water concentration, pH, provenance, ontology, quality-flag, and reference metadata.

Do not patch this generated YAML by hand unless the merge pipeline cannot be rerun; the authoritative fix is already present in the normalized source record.

## Follow-up Checks

After regenerating, rerun open schema, strict, reference, and term validation for the generated YAML and confirm `Distilled water` is `1000.0 ML_PER_L`, `ph_range` is 7.3-7.7, the `ADJUST_PH` step is present, and the references include both source URLs.

## Additional Notes

None found.
