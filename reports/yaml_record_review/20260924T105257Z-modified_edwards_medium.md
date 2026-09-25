# YAML Record Review: modified_edwards_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_edwards_medium.yaml
- Started UTC: 2026-09-24T10:52:10Z
- Finished UTC: 2026-09-24T10:52:57Z
- Verdict: needs curation

## Target

Generated record `CultureMech:008797` for TOGO medium `M2205`, `Modified Edward's medium`.

The generated record merges `modified_edwards_medium` from `data/normalized_yaml/bacterial/modified_edwards_medium.yaml`. The generated YAML was compared with that maintained owner and its 2026-09-12 TOGO M2205 repair metadata.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed with no error rows.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record has the correct TOGO `M2205` identity and preserves the seven original ingredient quantities.

The generated artifact is stale relative to a 2026-09-12 `RESOLVED_TOGO_M2205_SCORE15` repair in `data/normalized_yaml/bacterial/modified_edwards_medium.yaml`. The maintained owner now adds source-specific notes, pH 7.6, growth at 37 C, a `NaOAc` sodium-acetate grounding, MICRO terms for horse serum and tryptose, and explicit flags documenting that yeast dialysate intentionally remains unmapped.

## Evidence

The maintained owner and generated YAML agree that TOGO `M2205` lists 5 g/L NaCl, 1.3 g/L KCl, 5 g/L NaOAc, 6% horse serum, 0.5% glucose, 20 g/L tryptose, and 5% yeast dialysate.

The generated YAML predates the repair and therefore lacks the structured `ph_value: 7.6`, `temperature_value: 37.0`, source annotations on each ingredient, NaOAc mapping to `CHEBI:32954`, horse-serum mapping to `MICRO:0001235`, tryptose mapping to `MICRO:0000183`, and the curated `references` and `data_quality_flags` blocks.

The TOGO public `M2205` page currently returns a single-page application shell, and the TOGO JSON endpoint returned an empty body during this review, so no fresh TOGO payload comparison was available.

## Completeness

The generated record is complete for the original seven row labels and numeric quantities.

It is incomplete for pH, temperature, three repaired ingredient groundings, source-per-row annotations, and the explicit curation metadata that marks yeast dialysate as intentionally unmapped.

## Findings

- High: The generated YAML is stale relative to the 2026-09-12 source-backed repair in `modified_edwards_medium.yaml`.
- Medium: Source pH 7.6 and 37 C growth temperature are absent.
- Medium: `NaOAc`, horse serum, and tryptose lack the repaired ontology mappings present in the maintained owner.
- Low: The generated artifact lacks the repaired `references`, `data_quality_flags`, and source-per-row notes.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/modified_edwards_medium.yaml` from the repaired 2026-09-12 maintained owner.
- Confirm that the regenerated artifact keeps pH 7.6, 37 C, all seven TOGO M2205 ingredient rows, the NaOAc/horse-serum/tryptose groundings, and the intentional-unmapped treatment for yeast dialysate.
- Preserve the `https://togomedium.org/medium/M2205` reference and the repaired curation flags.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Recompare the regenerated record against the repaired maintained owner to verify the pH, temperature, all seven ingredients, and each repaired ontology mapping.

## Additional Notes

None found.
