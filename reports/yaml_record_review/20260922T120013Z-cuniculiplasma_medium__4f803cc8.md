# YAML Record Review: CUNICULIPLASMA MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/cuniculiplasma_medium__4f803cc8.yaml`
- Started UTC: 2026-09-22T12:00:13Z
- Finished UTC: 2026-09-22T12:00:13Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:002255` / `cuniculiplasma_medium`, a one-source generated merge from `data/normalized_yaml/archaea/cuniculiplasma_medium.yaml` for JCM Medium J1075.

## Validation

- Open schema validation passed for `MediaRecipe`.
- Strict validation passed and wrote `/private/tmp/cuniculiplasma_medium__4f803cc8.strict.tsv`.
- LinkML reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded `curation_history` was not separately checked because the available `validate-history` target validates standalone files under `history/`, not history entries embedded in generated `MediaRecipe` YAML.

## Identity and Grounding

The record identity is correct: JCM GRMD 1075 is `CUNICULIPLASMA MEDIUM`, an archaeal liquid medium adjusted to pH 1.0 to 1.2 with H2SO4.

The source composition is a compact 1 L recipe containing these rows:

- basal salts, FeCl3 x 6 H2O, beef extract, yeast extract, tryptone, betaine, and distilled water
- 1 mL Trace element solution from JCM Medium 187
- 10 mL Kao and Michayluk vitamin solution

The generated record inlines the Medium 187 trace-metal stock as top-level final ingredients and leaves the Kao and Michayluk vitamin solution as an empty `Unknown solution` with `10 G_PER_L`.

## Evidence

Primary source checks:

- JCM GRMD 1075 was fetched to `/private/tmp/jcm_grmd_1075.html`; it lists 1 mL Trace element solution from Medium 187 and 10 mL Kao and Michayluk vitamin solution per 1 L recipe.
- JCM GRMD 187 was fetched to `/private/tmp/jcm_grmd_187.html`; its Trace element solution stock lists ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O per 1 L stock.
- TogoMedium M1144 was fetched to `/private/tmp/togo_M1144.json`; it is named `Cuniculiplasma Medium` and points at the same JCM 1075 source.

Local record checks:

- `data/normalized_yaml/archaea/cuniculiplasma_medium.yaml` and the generated `cuniculiplasma_medium__4f803cc8.yaml` both flatten the JCM 187 trace stock into top-level ingredients.
- `data/normalized_yaml/archaea/TOGO_M1144_Cuniculiplasma_Medium.yaml` preserves both JCM solution rows but keeps them as empty `Unknown solution` stubs using `G_PER_L`.
- The same direct JCM and TOGO M1144 imports are split across generated `cuniculiplasma_medium__4f803cc8.yaml` and `CUNICULIPLASMA_MEDIUM.yaml`.

## Completeness

The direct generated record has the basal ingredient list, pH target, and final amounts for the non-stock rows. It is incomplete for both cross-referenced additives: the trace element solution has been flattened at stock concentrations instead of being represented as a 1 mL/L stock addition, and the Kao and Michayluk vitamin solution has no composition and the wrong unit.

## Findings

1. Needs curation: trace metals from JCM Medium 187 are represented as final top-level ingredients.

   JCM 1075 adds 1 mL of the JCM 187 Trace element solution per liter. The generated record lists the stock concentrations directly, for example 0.07 g/L ZnCl2, 0.1 g/L MnCl2 x 4 H2O, and 0.19 g/L CoCl2 x 6 H2O. Final CTM-level concentrations should be 1000-fold lower if expanded, or the stock should be preserved under a `Trace element solution` entry at 1 mL/L.

2. Needs curation: Kao and Michayluk vitamin solution is an empty solution with a mass concentration.

   The source calls for 10 mL of a named commercial vitamin solution per liter. The generated `solutions` entry has no composition, `name: Unknown solution`, and `unit: G_PER_L`; at minimum the addition should be 10 mL/L and should not be modeled as 10 g/L.

3. Needs curation: the same JCM 1075 recipe is split into direct JCM and TOGO generated records.

   TogoMedium M1144 points at the same JCM 1075 recipe, but its generated record is separate and has a different projection of the same solution rows. After unit and solution repairs, these should merge as source duplicates.

## Recommended Edits

- Recurate the trace element row as `Trace element solution` from JCM Medium 187 at 1 mL/L, with either a link to the JCM 187 solution or nested Zn/Mn/B/Co/Cu/Ni/Mo stock composition kept under the solution.
- Convert the Kao and Michayluk vitamin addition to `10 ML_PER_L` and remove `name: Unknown solution`.
- Avoid inlining the JCM 187 trace stock as top-level final `ingredients` unless the dilution factor from 1 mL/L is applied.
- Link `TOGO_M1144_Cuniculiplasma_Medium.yaml` to the repaired direct JCM record as a source duplicate.
- Regenerate `data/merge_yaml/merged/cuniculiplasma_medium__4f803cc8.yaml` after upstream repairs.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation for regenerated Cuniculiplasma Medium.
- Search generated output for `cuniculiplasma_medium` and `CUNICULIPLASMA_MEDIUM` with ignored files included and confirm JCM 1075 and TOGO M1144 no longer emit split generated records.
- Confirm no regenerated top-level Cuniculiplasma ingredient is one of the JCM 187 trace metals.
- Confirm the Kao and Michayluk vitamin row uses a volume concentration rather than `G_PER_L`.

## Additional Notes

The exact GRMD 1075 search used `rg --no-ignore --hidden`, so ignored report files and generated outputs were included.
