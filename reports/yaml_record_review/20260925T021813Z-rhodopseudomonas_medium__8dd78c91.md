# YAML Record Review: rhodopseudomonas_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rhodopseudomonas_medium__8dd78c91.yaml`
- Started UTC: 2026-09-25T02:18:12Z
- Finished UTC: 2026-09-25T02:18:21Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:002483` for JCM Medium J131 / `mediadive.medium:J131`, generated from `data/normalized_yaml/bacterial/rhodopseudomonas_medium.yaml`.

## Validation

- Open schema validation: passed with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The target ID, label, category, and `mediadive.medium:J131` grounding match MediaDive for Rhodopseudomonas medium. The live JCM `GRMD=131` page returned `Nothing found`, so the direct JCM URL is no longer sufficient evidence by itself.

TOGO M123 is the same source medium: it cites original media ID `JCM_M131`, the same JCM 131 URL, and the same pH and recipe. An exact ignored-inclusive search for `mediadive.medium:J131`, `TOGO:M123`, `JCM_M131`, and `GRMD=131` found only the expected JCM and TOGO maintained owners, their two generated records, and their indexes under the relevant data trees.

## Evidence

MediaDive J131 lists 2.5 g sodium succinate, 0.9 g K2HPO4, 0.6 g KH2PO4, 0.2 g MgSO4 x 7H2O, 1.25 g (NH4)2SO4, 70 mg CaCl2, 3 mg ferric citrate, 3 mg EDTA, 0.5 g yeast extract, 1000 ml distilled water, and pH 7.0 per 1 L recipe. TOGO M123 reports the same recipe as JCM_M131, including 1 L distilled water and pH 7.0.

The generated JCM target has the nine non-water ingredients and pH 7.0, but omits the 1000 ml distilled-water row. The TOGO owner preserves the same original source but emits 1 L water as `1 G_PER_L`, 70 mg CaCl2 as `70 G_PER_L`, 3 mg ferric citrate as `3 G_PER_L`, and 3 mg EDTA as `3 G_PER_L`.

## Completeness

The target is missing the source water row, and the generated corpus has two records for JCM_M131 because the TOGO M123 owner was not merged into the direct JCM J131 owner.

Empty optional literature, strain, and solution fields are not defects for this medium.

## Findings

- Major: `data/normalized_yaml/bacterial/rhodopseudomonas_medium.yaml` omits the 1000 ml distilled-water row that MediaDive J131 lists in its main solution, so the generated target is not a complete rendering of J131.
- Major: `data/normalized_yaml/bacterial/TOGO_M123_Rhodopseudomonas_Medium.yaml` imported mass and volume units as gram-per-liter values: 1 L water became `1 G_PER_L`, 70 mg CaCl2 became `70 G_PER_L`, and 3 mg ferric citrate and EDTA became `3 G_PER_L`.
- Major: `data/normalized_yaml/bacterial/TOGO_M123_Rhodopseudomonas_Medium.yaml` did not carry TOGO's pH 7.0 comment into `ph_value` or `preparation_steps`.
- Major: `data/merge_yaml/merged` contains both `rhodopseudomonas_medium__8dd78c91.yaml` for `mediadive.medium:J131` and `RHODOPSEUDOMONAS_MEDIUM.yaml` for TOGO M123/JCM_M131 instead of a single merged source-duplicate target.

## Recommended Edits

- Add the 1000 ml/L distilled-water row to `data/normalized_yaml/bacterial/rhodopseudomonas_medium.yaml`.
- Repair `data/normalized_yaml/bacterial/TOGO_M123_Rhodopseudomonas_Medium.yaml` so water stays volumetric, milligram inputs are converted to 0.07, 0.003, and 0.003 g/L, and pH 7.0 is represented.
- Add a source-duplicate relationship between TOGO M123 and direct MediaDive/JCM J131, then regenerate `data/merge_yaml/merged`.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation for the regenerated Rhodopseudomonas medium.
- Confirm the regenerated final recipe has ten MediaDive J131 rows, including distilled water.
- Confirm `data/merge_yaml/merged` no longer emits both uppercase TOGO and lowercase JCM Rhodopseudomonas targets.

## Additional Notes

The direct JCM endpoint for `GRMD=131` appears stale or retired, but both imported source APIs identify the same original JCM 131 recipe.
