# YAML Record Review: sabourauds_agar

- Repository: CultureMech
- Record: `data/merge_yaml/merged/sabourauds_agar.yaml`
- Started UTC: `2026-09-25T03:35:29Z`
- Finished UTC: `2026-09-25T03:35:29Z`
- Verdict: pass with minor issues

## Target

Reviewed the generated merge record for `sabourauds_agar`, a single-source merge of `data/normalized_yaml/bacterial/sabourauds_agar.yaml`.

The record represents TOGO Medium `M1411`, an NBRC Medium 6 `Sabouraud's Agar` import. The main chemical formula is preserved, but pH 6.0 is missing and the water row is expressed with the wrong unit.

## Validation

- Open schema validation: Passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: Passed; `scripts/validate_strict.py` exited 0 and reported 0 total error rows.
- Reference validation: Passed; `linkml-reference-validator` ran 0 checks and reported all checks passed.
- Term validation: Passed; `linkml-term-validator` exited 0 after the expected `eutils` / `pkg_resources` warning.
- Embedded `curation_history`: Not checked. `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The generated identity is correctly grounded to TOGO `M1411` and to the NBRC Medium 6 source page. No false duplicate merge was found for this generated YAML.

## Evidence

TOGO `M1411` and NBRC Medium 6 list 10 g Peptone, 40 g Glucose, 1 L Distilled water, and 20 g Agar for `Sabouraud's Agar`. TOGO also carries pH 6.0 from the NBRC comment.

## Completeness

The generated record preserves Peptone at 10 g/L, Glucose at 40 g/L, and Agar at 20 g/L.

It loses or corrupts these details:

- 1 L distilled water is represented as `1 G_PER_L`.
- pH 6.0 is absent from the generated structured pH fields.

## Findings

- `pass with minor issues`: The water row is a volume, not a 1 g/L solute. NBRC lists 1 L Distilled water, but the generated record reports `Distilled water` at `1 G_PER_L`.
- `pass with minor issues`: The generated record drops pH 6.0 even though TOGO and NBRC both expose it.
- `pass`: The Peptone, Glucose, and Agar amounts match the TOGO and NBRC source amounts.

## Recommended Edits

- Do not hand-edit `data/merge_yaml/merged/sabourauds_agar.yaml`; fix `data/normalized_yaml/bacterial/sabourauds_agar.yaml`, then rerun the merge.
- Preserve Distilled water as a 1 L volume row or omit it instead of converting it to `1 G_PER_L`.
- Carry pH 6.0 from the NBRC source into a structured pH field.
- Leave Peptone 10 g/L, Glucose 40 g/L, and Agar 20 g/L unchanged.

## Follow-up Checks

- Rerun open schema, strict, reference, and term validation on `data/normalized_yaml/bacterial/sabourauds_agar.yaml`.
- Regenerate `data/merge_yaml/merged/sabourauds_agar.yaml` and verify that no water row appears at `1 G_PER_L`.
- Verify that pH 6.0 survives regeneration.
- Run an exact ignored-file-inclusive search for `TOGO:M1411`, `NBRC_M6`, and `sabourauds_agar` before changing duplicate links.

## Additional Notes

The absence of `target_organisms` was not treated as a defect for this generated record review. An earlier broad report search for `sabourauds_agar` matched unrelated `1/10 Sabouraud's Agar` reviews and was discarded; the follow-up ignored-file-inclusive search for the exact report title found no existing `sabourauds_agar` report.
