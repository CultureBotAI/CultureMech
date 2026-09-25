# YAML Record Review: oceanithermus_medium__7ded95de

- Repository: CultureMech
- Record: data/merge_yaml/merged/oceanithermus_medium__7ded95de.yaml
- Started UTC: 2026-09-24T19:11:44Z
- Finished UTC: 2026-09-24T19:13:02Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/oceanithermus_medium__7ded95de.yaml`, a generated bacterial `MediaRecipe` with id `CultureMech:008122` and source term `TOGO:M1573`.

The generated record has one source owner, `data/normalized_yaml/bacterial/TOGO_M1573_Oceanithermus_medium.yaml`, for NBRC Medium 377.

## Validation

- LinkML open-schema validation: passed; no issues found.
- Strict validation: passed; `/private/tmp/oceanithermus_medium__7ded95de.strict.tsv` contained only the header row.
- Reference validation: passed; the validator reported 0 configured checks for this record.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The TOGO/NBRC identity is valid: TOGO M1573 imports NBRC Medium 377, Oceanithermus medium.

The hash-suffixed generated file is expected because another generated `OCEANITHERMUS_MEDIUM.yaml` exists for the distinct KOMODO/DSMZ 1149 Oceanithermus formulation. An ignored-inclusive exact search found both source groups; the current TOGO M1573 record should not be blindly merged with the DSMZ 1149 cluster because that sibling has a different provider id, pH, and recipe surface.

## Evidence

Checked the generated TOGO record, the normalized TOGO M1573 owner, an ignored-inclusive exact repository search for TOGO M1573, NBRC M377, and the `oceanithermus_medium` slug, the fetched TOGO M1573 REST payload, and the official NBRC 377 page.

NBRC 377 has three recipe scopes:

- Main medium: 1 L distilled water, salts and yeast extract, 10 ml trace element solution, 10 ml vitamin solution, and N2.
- Trace element stock: salts and 2Na-EDTA made up to 1 L.
- Vitamin stock: mg quantities of vitamins made up to 1 L.

The NBRC instructions also say to mix the ingredients except NaHCO3 and vitamin solution, dispense under N2, autoclave, and then add filter-sterile NaHCO3 and vitamin solutions.

## Completeness

The generated YAML does not preserve the three source scopes:

- Main-medium water, trace-stock water, and vitamin-stock water are collapsed into one `3.0 G_PER_L` final ingredient in generated YAML. The normalized owner has reduced this to `1.0 G_PER_L`, but it is still the wrong unit for 1 L final water and still loses the stock-water scopes.
- Main-medium NaCl at 20 G_PER_L is summed with trace-stock NaCl at 1 G_PER_L and emitted as a 21 G_PER_L final ingredient.
- Main-medium CaCl2 x 2 H2O at 0.1 G_PER_L is summed with trace-stock CaCl2 x 2 H2O at 0.13 G_PER_L and emitted as a 0.23 G_PER_L final ingredient.
- Trace-element and vitamin stock rows are flattened as final G_PER_L ingredients.
- `Trace element solution` and `Vitamin solution` are represented as 10 G_PER_L solution placeholders instead of 10 ML_PER_L supplements with nested stock composition.
- No preparation steps capture the N2 dispensing, autoclaving, or filter-sterile addition of NaHCO3 and vitamins.

## Findings

- BLOCKER: The TOGO M1573 owner flattens trace-element and vitamin stock components into final-medium rows, causing stock concentrations to be interpreted as final concentrations.
- BLOCKER: Duplicate chemical names from different source scopes are summed. The generated 21 G_PER_L NaCl and 0.23 G_PER_L CaCl2 x 2 H2O rows combine main-medium salts with trace-stock salts.
- MAJOR: Distilled water is represented as G_PER_L and collapsed across the main medium and two stock solutions.
- MAJOR: The two imported supplement rows use 10 G_PER_L placeholders even though the source adds 10 ml trace element solution and 10 ml vitamin solution per final liter.
- MAJOR: The generated record has no preparation steps for N2 dispensing, autoclaving, or filter-sterile post-autoclave additions.
- MAJOR: CoCl2 x 6 H2O and NiCl2 x 6 H2O are grounded to anhydrous CHEBI salts, and several trace salts lack `mediaingredientmech_chebi_term` mirrors.

## Recommended Edits

- Split the TOGO M1573 normalized representation into a main final medium plus nested `Trace element solution` and `Vitamin solution` stocks.
- Encode final distilled water as 1000 ML_PER_L in the main medium and keep stock waters inside the corresponding solutions.
- Keep 20 G_PER_L NaCl and 0.1 G_PER_L CaCl2 x 2 H2O in the final medium; keep 1 G_PER_L NaCl and 0.13 G_PER_L CaCl2 x 2 H2O only in the trace-element stock.
- Convert `Trace element solution` and `Vitamin solution` to 10 ML_PER_L solution additions and keep their components in stock concentration units.
- Add preparation steps for mixing all ingredients except NaHCO3 and vitamin solution, dispensing under N2, autoclaving, and adding filter-sterile NaHCO3 and vitamin solution after autoclaving.
- Correct hydrated-salt CHEBI groundings for CoCl2 x 6 H2O and NiCl2 x 6 H2O, then regenerate merged YAML.

## Follow-up Checks

- Run an ignored-inclusive exact search for `TOGO:M1573`, `NBRC_M377`, `NO=377`, and `TOGO_M1573_Oceanithermus_medium` after repair to confirm the TOGO/NBRC owner regenerates once.
- Rebuild merged YAML and verify the TOGO M1573 record keeps a distinct `merge_fingerprint` from the DSMZ/KOMODO 1149 Oceanithermus medium.
- Re-run open-schema, strict, reference, and term validation after the normalized owner is repaired and generated YAML is rebuilt.

## Additional Notes

None found.
