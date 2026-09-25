# YAML Record Review: skirrows_selective_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/skirrows_selective_medium.yaml
- Started UTC: 2026-09-25T05:37:18Z
- Finished UTC: 2026-09-25T05:37:18Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:009467`, `skirrows_selective_medium`, from `data/merge_yaml/merged/skirrows_selective_medium.yaml`.

The target record is a TOGO M2935 import for `Skirrow's selective medium`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to TOGO medium M2935.

No same-source duplicate was found in the sorted generated YAML list.

## Evidence

The TOGO M2935 payload names the medium `Skirrow's selective medium`.

Its source comment identifies the base as Columbia Agar Base, Oxoid CM0331, supplemented with 5% sheep blood and Campylobacter selective supplement, Oxoid SR0117.

The same source comment reports 42 C microaerobic incubation for 24 h.

## Completeness

The generated record misclassifies the agar-base medium as `LIQUID`.

The generated record imports TOGO's 1 L Oxoid product row as `1 G_PER_L`.

The base and supplement identities from the source comment are absent from the generated ingredients.

The 5% sheep blood row uses `PERCENT_W_V`; the source context is a sheep-blood volume supplement.

The 42 C source temperature is absent from the generated record.

## Findings

The TOGO product volume was normalized into a gram-per-liter pseudo-ingredient.

The agar base and Campylobacter supplement named in source prose were lost.

Physical state and temperature context are stale relative to the repaired normalized source.

## Recommended Edits

Keep the repaired product-level structure in `data/normalized_yaml/bacterial/skirrows_selective_medium.yaml`.

Represent Columbia Agar Base Oxoid CM0331 and Campylobacter selective supplement Oxoid SR0117 as variable product rows because TOGO M2935 does not state their amounts.

Represent sheep blood as a 5% volume supplement.

Restore solid agar physical state and 42 C temperature.

Regenerate the merged YAML after repairing the normalized source.

## Follow-up Checks

Confirm the regenerated record has Columbia Agar Base, Sheep blood, and Campylobacter selective supplement rows.

Confirm no `1 G_PER_L` `Skirrow's selective medium (Oxoid)` row remains.

Confirm physical state is solid agar and temperature is 42 C.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
