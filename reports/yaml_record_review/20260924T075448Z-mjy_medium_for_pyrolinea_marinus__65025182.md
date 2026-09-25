# YAML Record Review: mjy_medium_for_pyrolinea_marinus__65025182

- Repository: CultureMech
- Record: data/merge_yaml/merged/mjy_medium_for_pyrolinea_marinus__65025182.yaml
- Started UTC: 2026-09-24T07:54:48Z
- Finished UTC: 2026-09-24T07:55:12Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:003046`
- Generated name: `mjy_medium_for_pyrolinea_marinus`
- Generated source file: `data/merge_yaml/merged/mjy_medium_for_pyrolinea_marinus__65025182.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/mjy_medium_for_pyrolinea_marinus.yaml`
- Upstream source: MediaDive/JCM medium `J700`, `MJY MEDIUM FOR PYROLINEA MARINUS`

## Validation

- Open LinkML validation passed: `No issues found`.
- Strict validation passed with 0 ERROR rows in `/private/tmp/mjy_medium_for_pyrolinea_marinus__65025182.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The generated record identity is aligned with MediaDive/JCM `J700`.
- The `media_term` points to `mediadive.medium:J700`.
- NaNO3 still carries legacy `mediaingredientmech_term: MediaIngredientMech:000171`.
- `NiCl2 x 6 H2O` is grounded to generic nickel dichloride.

## Evidence

- MediaDive `J700` main solution `4612` contains 1000 ml MJ(-N) synthetic seawater solution `3957`, 0.25 g NH4Cl, 0.5 g NaNO3, 1 g yeast extract, 5 ml 8% NaHCO3, and 10 ml 5% `Na2S x 9 H2O`.
- MediaDive solution `3957`, MJ(-N) synthetic seawater, contains seawater salts, 10 ml Modified Wolin's mineral solution `241`, and water.
- The generated direct NH4Cl, NaNO3, and yeast-extract values match MediaDive's 1015 ml final `g_l` values.
- The generated 5 `G_PER_L` NaHCO3 and 10 `G_PER_L` `Na2S x 9 H2O` rows came from J700's 5 ml and 10 ml stock addition volumes, not final gram-per-liter source values.

## Completeness

- The generated record has no `solutions` array.
- The 5 ml 8% bicarbonate and 10 ml 5% sulfide additions were flattened as direct 5 g/L and 10 g/L ingredients.
- The 1000 ml MJ(-N) synthetic seawater addition was flattened to raw solution `3957` concentrations rather than the final 1000/1015 dilution.
- The 10 ml Modified Wolin's mineral solution nested inside MJ(-N) synthetic seawater is missing.
- The optional 10 ml/L clarified rumen fluid stimulation note from the source survives only in preparation prose.

## Findings

- High: The 5 ml 8% NaHCO3 stock and 10 ml 5% `Na2S x 9 H2O` stock were imported as 5 g/L and 10 g/L direct ingredients.
- High: Modified Wolin's mineral solution `241` was dropped from the structured composition.
- Medium: The MJ(-N) synthetic seawater rows were not diluted through the 1000 ml addition into the 1015 ml J700 main solution.
- Medium: Sodium nitrate still uses the deprecated `mediaingredientmech_term` slot.
- Medium: `NiCl2 x 6 H2O` is grounded to generic nickel dichloride.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/mjy_medium_for_pyrolinea_marinus.yaml` with explicit MJ(-N) synthetic seawater, 8% NaHCO3, and 5% `Na2S x 9 H2O` stock additions.
- Preserve MJ(-N) synthetic seawater as a 1010 ml stock with 10 ml Modified Wolin's mineral solution `241`.
- Replace the direct 5 g/L bicarbonate and 10 g/L sulfide rows with the 5 ml and 10 ml stock additions.
- Replace the legacy nitrate `mediaingredientmech_term` with the ingredient's CHEBI key.
- Regenerate the merged record after repairing the normalized source.

## Follow-up Checks

- Re-fetch MediaDive `J700` and solution `3957` and verify the regenerated record preserves the 1000 ml, 10 ml, 5 ml, and 10 ml stock additions.
- Confirm no 8% bicarbonate or 5% sulfide stock volume is imported as a gram-per-liter concentration.
- Confirm Modified Wolin's mineral solution components, including tungstate, are represented.
- Re-run open LinkML, strict, reference, and term validation after regenerating the merged record.

## Additional Notes

- None found.
