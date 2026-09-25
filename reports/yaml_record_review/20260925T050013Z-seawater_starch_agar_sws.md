# YAML Record Review: seawater_starch_agar_sws

- Repository: CultureMech
- Record: data/merge_yaml/merged/seawater_starch_agar_sws.yaml
- Started UTC: 2026-09-25T05:00:13Z
- Finished UTC: 2026-09-25T05:00:13Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007953`, `seawater_starch_agar_sws`, from `data/merge_yaml/merged/seawater_starch_agar_sws.yaml`.

The target record is a single-source TOGO M1416 import for `Seawater Starch Agar (SWS)`, originally sourced from NBRC_M13.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The target record is correctly grounded to TOGO Medium M1416 and NBRC Medium 13.

No duplicate merge issue was found in the generated YAML.

## Evidence

NBRC Medium 13 lists 1 g Soytone, 10 g Soluble starch, 1 L Seawater at 2% salinity, 15 g Agar, and pH 8.2.

NBRC adds a note to dilute artificial seawater or natural seawater with distilled water.

The TOGO M1416 API preserves the same component list, pH 8.2 comment, and NBRC_M13 source URL.

## Completeness

The generated target preserves 10 g/L Soluble starch, 15 g/L Agar, and 1 g/L Soytone.

The 1 L Seawater row is migrated into an empty `Unknown solution` with `composition: []` and `unit: G_PER_L`.

The generated target omits pH 8.2.

The generated target omits the NBRC note about diluting artificial or natural seawater with distilled water.

## Findings

The Seawater row is malformed as a 1 g/L empty solution instead of a 1 L seawater solvent.

The source pH is missing.

The NBRC seawater dilution note is missing, so the `Seawater (2% Salinity)*` asterisk is not explained.

## Recommended Edits

Repair the TOGO M1416 normalized source so `Seawater (2% Salinity)` is represented as a 1 L/L or 1000 ml/L seawater row, not as an empty 1 g/L solution.

Restore pH 8.2 from NBRC 13 and the TOGO M1416 `ph` field.

Add a preparation or ingredient note that the seawater can be prepared by diluting artificial seawater or natural seawater with distilled water.

Regenerate the merge layer after the normalized TOGO M1416 source is repaired.

## Follow-up Checks

Confirm the regenerated record has no `name: Unknown solution` entry for `Seawater (2% Salinity)`.

Confirm the regenerated record preserves 1 g/L Soytone, 10 g/L Soluble starch, 15 g/L Agar, 1 L/L Seawater at 2% salinity, and pH 8.2.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
