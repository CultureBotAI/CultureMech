# YAML Record Review: seawater_medium_with_0_5_tryptone

- Repository: CultureMech
- Record: data/merge_yaml/merged/seawater_medium_with_0_5_tryptone.yaml
- Started UTC: 2026-09-25T04:57:14Z
- Finished UTC: 2026-09-25T04:57:14Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:008902`, `seawater_medium_with_0_5_tryptone`, from `data/merge_yaml/merged/seawater_medium_with_0_5_tryptone.yaml`.

The target record is a single-source TOGO M2315 import for `seawater medium (with 0.5% tryptone)`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The target record is correctly grounded to TOGO Medium M2315.

No duplicate merge issue was found in the generated YAML.

## Evidence

The TOGO M2315 API records `conc_value: 3`, `conc_unit: %` for CrystalSea Marine Mix and 0.5% tryptone.

The TOGO source comment says the source organism was cultured at 30 C in seawater medium with 3% CrystalSea Marine Mix and 0.5% tryptone.

The normalized source `data/normalized_yaml/bacterial/seawater_medium_with_0_5_tryptone.yaml` has already been repaired to preserve 3% CrystalSea Marine Mix, 0.5% Tryptone, and a 30 C incubation temperature.

## Completeness

The generated target preserves the 0.5% tryptone row.

The generated target still represents the CrystalSea row as 1 g/L by mistaking the TOGO API's 1 L medium volume for a mass concentration.

The generated target lacks the repaired normalized-source 30 C temperature.

## Findings

The generated merge layer is stale relative to the repaired normalized TOGO M2315 source.

The stale generated record has a nonsensical 1 g/L CrystalSea Marine Mix row where the source specifies 3%.

The stale generated record lacks the repaired `temperature_value: 30.0` field.

## Recommended Edits

Regenerate the merge layer from `data/normalized_yaml/bacterial/seawater_medium_with_0_5_tryptone.yaml`.

Confirm the regenerated record has CrystalSea Marine Mix at 3% w/v and Tryptone at 0.5% w/v.

Confirm the regenerated record carries the 30 C source temperature.

## Follow-up Checks

Confirm no generated TOGO M2315 row has CrystalSea Marine Mix at 1 g/L.

Confirm the regenerated record's `curation_history` includes `RESOLVED_TOGO_LITERAL_PRODUCT_SCORE40_GRAPH`.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
