# YAML Record Review: NB-PYRUVATE AGAR

- Repository: CultureMech
- Record: data/merge_yaml/merged/nb_pyruvate_agar.yaml
- Started UTC: 2026-09-24T16:58:48Z
- Finished UTC: 2026-09-24T16:58:49Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:000979` for direct DSMZ Medium 1509, `NB-PYRUVATE AGAR`.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to DSMZ Medium 1509.

An exact repository search including ignored and hidden files for `CultureMech:000979`, `mediadive.medium:1509`, `DSMZ_Medium1509`, `nb_pyruvate_agar`, and `NB-PYRUVATE AGAR` found only this generated record and its normalized owner.

No incorrect ingredient grounding was found.

## Evidence

DSMZ Medium 1509 lists Solution A with 6.0 g Nutrient Broth, 1.5 g NaCl, 1.0 g Na-Pyruvate, 14.0 g agar, and 1000.0 ml distilled water.

The source instructs adjusting Solution A to pH 7.0.

The generated record preserves the four non-water ingredient masses, pH 7.0, and `SOLID_AGAR` physical state.

## Completeness

The source 1000.0 ml distilled-water row is absent.

## Findings

- Major: Solution A's 1000.0 ml distilled-water row is missing from the structured recipe.

## Recommended Edits

- In `data/normalized_yaml/bacterial/nb_pyruvate_agar.yaml`, add the source 1000.0 ml distilled-water row to Solution A.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/nb_pyruvate_agar.yaml` and verify distilled water is present.
- Re-run open schema, strict, reference, and term validation after curation.

## Additional Notes

None found.
