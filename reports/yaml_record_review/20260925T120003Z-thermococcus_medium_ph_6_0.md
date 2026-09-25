# YAML Record Review: thermococcus_medium_ph_6_0
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermococcus_medium_ph_6_0.yaml
- Started UTC: 2026-09-25T12:00:03Z
- Finished UTC: 2026-09-25T12:00:03Z
- Verdict: needs curation

## Target
Reviewed the generated JCM Medium J350 merge for Thermococcus medium, pH 6.0.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with 0 checks.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to mediadive.medium:J350.
- JCM J350 is a pH 6.0 wrapper around 1 L of JCM Medium 280, followed by pH adjustment with 1.0 N H2SO4 after reduction.
- The generated parent_media relationship incorrectly marks J350 as a SOURCE_DUPLICATE of J280; J350 should be treated as a pH 6.0 variant of the J280 parent.

## Evidence
- MediaDive J350 represents the recipe as 1000 ml Main sol. J280.
- The J350 preparation instruction is limited to readjusting the reduced medium to pH 6.0 with 1.0 N H2SO4.
- The nested J280 parent contains 10 ml Trace minerals and 10 ml Trace vitamins additions, sulfur, Na2S x 9H2O, 1000 ml water, and anaerobic N2 preparation.

## Completeness
- The pH 6.0 value and J350 acid-adjustment step are present.
- The generated record flattened J280 and its trace stock recipes into one ingredient list.
- Distilled water is absent.

## Findings
- J350 was collapsed into a SOURCE_DUPLICATE of J280 even though the source defines J350 as a pH 6.0 derivative.
- Trace minerals and Trace vitamins were flattened at full stock strength; their stock MgSO4 x 7H2O, NaCl, and FeSO4 x 7H2O rows were also summed with same-named rows from Main sol. J280.
- The recipe omits the 1000 ml distilled water row from the nested J280 parent.
- The nested J280 comment about a maltodextrin, sulfur-omitted Thermococcus variant was imported as preparation_steps even though it is not part of the J350 preparation workflow.
- The trace-minerals stock pH adjustment was imported as a top-level preparation step instead of being attached to the stock recipe.

## Recommended Edits
- Model J350 as a variant of JCM J280 with final pH 6.0 and a 1.0 N H2SO4 readjustment step.
- Preserve 10 ml Trace minerals and 10 ml Trace vitamins as stock additions, or expand them only at their final diluted concentrations.
- Prevent duplicate summing between parent-solution compounds and nested stock compounds.
- Keep the JCM 280 maltodextrin comment with the M274 variant, not as a J350 preparation step.
- Keep stock-specific preparation instructions attached to their source stock recipes.

## Follow-up Checks
- Rebuild the J350 merge and verify that J280 is represented as a parent/variant relationship rather than a source duplicate.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
