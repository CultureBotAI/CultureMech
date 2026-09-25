# YAML Record Review: HIPPEA JASONIAE MEDIUM
- Repository: CultureMech
- Record: data/merge_yaml/merged/hippea_jasoniae_medium__dfedbffc.yaml
- Started UTC: 2026-09-23T12:07:22Z
- Finished UTC: 2026-09-23T12:08:10Z
- Verdict: needs curation

## Target

Reviewed the generated direct DSMZ branch for DSMZ Medium 1360, `HIPPEA JASONIAE MEDIUM`, at `data/merge_yaml/merged/hippea_jasoniae_medium__dfedbffc.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/hippea_jasoniae_medium__dfedbffc.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is correctly grounded to `mediadive.medium:1360`, DSMZ Medium 1360 `HIPPEA JASONIAE MEDIUM` at final pH 4.5.

## Evidence

DSMZ 1360 lists a 1000 ml main medium with 10 ml Allen trace element solution, 0.5 ml 0.1% sodium resazurin, 1 ml Wolin vitamin solution (10x), 10 g powdered sulfur, late sterile yeast extract and sodium sulfide additions, and pH-specific anaerobic preparation under 80% N2 / 20% CO2. Allen's trace element solution and Wolin's vitamin solution are separate one-liter stock recipes that each contain their own distilled water.

The generated record preserves DSMZ's main-medium salts and pH 4.5, but it omits main-medium distilled water, omits water from both stock solutions, and flattens every Allen and Wolin stock ingredient into the final ingredient list at stock strength.

## Completeness

The broad DSMZ preparation paragraph is present, but the solution structure is incomplete. Allen trace metals, Wolin vitamins, resazurin, yeast extract, sodium sulfide, and powdered sulfur have different addition timing or subrecipe scopes that should not all be represented as indistinguishable final top-level ingredients.

## Findings

- Allen's trace element solution is added at 10 ml/L, but its metal salts appear at their full one-liter stock concentrations.
- Wolin's vitamin solution is added at 1 ml/L, but all vitamin rows appear at full 10x-stock concentrations.
- The 1000 ml main-medium distilled-water row is missing.
- Distilled water is missing from both Allen's trace element solution and Wolin's vitamin solution.
- `Adjust pH of final solution to 2 with 1 N HCl.` is scoped to the Allen trace-element stock but appears as a top-level preparation step.
- Yeast extract and sodium sulfide are top-level rows even though DSMZ adds them from sterile anoxic stocks under 100% N2 after the base medium is sterilized.

## Recommended Edits

- Preserve Allen's trace element solution and Wolin's vitamin solution as nested stocks, or dilute their ingredients by the 10 ml/L and 1 ml/L addition volumes before flattening.
- Restore the main-medium and stock-solution distilled-water rows.
- Scope the pH-2 HCl adjustment to Allen's trace element solution only.
- Represent sulfur, yeast extract, vitamins, and sulfide as preparation-scoped additions with the anaerobic gas conditions specified by DSMZ.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the regenerated artifact.
- Confirm no regenerated top-level ingredient retains full-strength Allen trace-element or Wolin vitamin stock concentrations.

## Additional Notes

None.
