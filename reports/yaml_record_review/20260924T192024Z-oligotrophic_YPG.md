# YAML Record Review: oligotrophic YPG

- Repository: CultureMech
- Record: data/merge_yaml/merged/oligotrophic_YPG.yaml
- Started UTC: 2026-09-24T19:20:24Z
- Finished UTC: 2026-09-24T19:22:00Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:009569`, the generated `oligotrophic_ypg` record merged from `data/normalized_yaml/bacterial/oligotrophic_ypg.yaml`.

## Validation

Passed LinkML validation against `MediaRecipe` with no issues reported.

Passed strict validation; the TSV contained only the header row.

Passed LinkML reference validation with zero reference checks.

Passed LinkML term validation.

Embedded `curation_history` validation was not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` blocks in generated YAML.

## Identity and Grounding

The identity is grounded to TOGO Medium M3055 / NBRC Medium 1611. TOGO and NBRC both identify the source as `oligotrophic YPG`, and the generated record preserves `media_term.term.id: TOGO:M3055`.

An ignored-inclusive exact search for `TOGO:M3055`, `NBRC_M1611`, `NO=1611`, and `oligotrophic_ypg` found only the normalized owner, generated derivative, and generated index/archive mentions. No extra direct source recipe or duplicate merged YAML record was found in the searched YAML/index scope.

## Evidence

TOGO M3055 reports the NBRC source URL for `NO=1611`, `original_media_id: NBRC_M1611`, `ph: 7.0`, and five components in one main solution: 1 L distilled water, 0.75 g D(+)-Glucose, 15 g agar, 0.75 g Yeast Extract(Difco), and 1.5 g Peptone(Difco).

The NBRC 1611 page reports the same medium name, the same five composition rows, and the same `pH 7.0`.

The generated and normalized records contain the same five components and carry the NBRC source URL in notes.

## Completeness

The glucose, agar, yeast extract, and peptone amounts match the TOGO and NBRC evidence after per-liter normalization.

Target organisms are absent. This is not a defect for this generated NBRC/TOGO import because neither fetched source lists strains or species for Medium 1611.

Preparation steps are absent. This is mostly source-limited because NBRC Medium 1611 only provides the composition table and pH line; however, the pH line itself is curatable and was dropped.

## Findings

- The imported water quantity is unit-corrupted: both TOGO and NBRC state `Distilled water` as `1 L`, but the normalized and generated YAML encode it as `value: '1'`, `unit: G_PER_L`.
- The evidence-backed `pH 7.0` line is missing from both the normalized and generated record even though TOGO exposes it in `meta.ph` and its comments array, and NBRC lists the same value below the composition table.

## Recommended Edits

- In `data/normalized_yaml/bacterial/oligotrophic_ypg.yaml`, recode `Distilled water` as a final-volume water component, for example `value: '1000'`, `unit: ML_PER_L`, to preserve the source's 1 L basis without treating water as 1 gram per liter.
- Add `ph_value: '7.0'` to the normalized record.
- Regenerate `data/merge_yaml/merged/oligotrophic_YPG.yaml` after the normalized owner is repaired.

## Follow-up Checks

- Rerun open-schema, strict, reference, and term validation on the regenerated `data/merge_yaml/merged/oligotrophic_YPG.yaml`.
- Recheck TOGO M3055 and NBRC 1611 after regeneration to confirm the water amount and pH line are faithfully represented.

## Additional Notes

None found.
