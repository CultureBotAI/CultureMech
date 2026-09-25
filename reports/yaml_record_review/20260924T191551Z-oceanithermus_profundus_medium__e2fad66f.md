# YAML Record Review: oceanithermus_profundus_medium__e2fad66f

- Repository: CultureMech
- Record: data/merge_yaml/merged/oceanithermus_profundus_medium__e2fad66f.yaml
- Started UTC: 2026-09-24T19:15:51Z
- Finished UTC: 2026-09-24T19:17:06Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/oceanithermus_profundus_medium__e2fad66f.yaml`, a generated bacterial `MediaRecipe` with id `CultureMech:008277` and source term `TOGO:M1714`.

The generated record has one source owner, `data/normalized_yaml/bacterial/TOGO_M1714_Oceanithermus_profundus_medium.yaml`, for NBRC Medium 922.

## Validation

- LinkML open-schema validation: passed; no issues found.
- Strict validation: passed; `/private/tmp/oceanithermus_profundus_medium__e2fad66f.strict.tsv` contained only the header row.
- Reference validation: passed; the validator reported 0 configured checks for this record.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The TOGO/NBRC identity is valid: TOGO M1714 imports NBRC Medium 922, Oceanithermus profundus medium.

This record should remain distinct from the DSMZ 975 and NBRC 404 Oceanithermus profundus media. NBRC 922 resembles NBRC 377 but adds 6.8 g sucrose and has different post-autoclave instructions, so it also should not be blindly merged with TOGO M1573.

## Evidence

Checked the generated TOGO M1714 record, the normalized TOGO M1714 owner, an ignored-inclusive exact repository search for TOGO M1714 and NBRC M922 identifiers, the fetched TOGO M1714 REST payload, and the official NBRC 922 page.

NBRC 922 has three recipe scopes:

- Main medium: 1 L distilled water, salts, 6.8 g sucrose, yeast extract, 10 ml trace elements solution, 10 ml vitamin solution, and N2.
- Trace elements stock: salts and 2Na-EDTA made up to 1 L.
- Vitamin stock: mg quantities of vitamins made up to 1 L.

NBRC also says to mix all ingredients except sucrose, NaHCO3, and vitamin solution, dispense under N2, autoclave, and then add filter-sterile sucrose, NaHCO3, and vitamin solutions.

## Completeness

The generated YAML does not preserve the three source scopes:

- Main-medium water, trace-stock water, and vitamin-stock water are collapsed into one generated `3.0 G_PER_L` final ingredient. The normalized owner has reduced this to `1.0 G_PER_L`, but the unit is still wrong and the stock waters still are not nested.
- Main-medium NaCl at 20 G_PER_L is summed with trace-stock NaCl at 1 G_PER_L and emitted as 21 G_PER_L.
- Main-medium CaCl2 x 2 H2O at 0.1 G_PER_L is summed with trace-stock CaCl2 x 2 H2O at 0.13 G_PER_L and emitted as 0.23 G_PER_L.
- Trace-element and vitamin stock rows are flattened as final G_PER_L ingredients.
- `Trace elements solution` and `Vitamin solution` are represented as 10 G_PER_L solution placeholders instead of 10 ML_PER_L supplements with nested stock composition.
- No preparation steps capture N2 dispensing, autoclaving, or filter-sterile post-autoclave additions of sucrose, NaHCO3, and vitamin solution.

## Findings

- BLOCKER: The TOGO M1714 owner flattens trace-element and vitamin stock components into final-medium rows, causing stock concentrations to be interpreted as final concentrations.
- BLOCKER: Duplicate chemical names from different source scopes are summed. The generated 21 G_PER_L NaCl and 0.23 G_PER_L CaCl2 x 2 H2O rows combine main-medium salts with trace-stock salts.
- MAJOR: Distilled water is represented as G_PER_L and collapsed across the main medium and two stock solutions.
- MAJOR: The two imported supplement rows use 10 G_PER_L placeholders even though NBRC 922 adds 10 ml trace elements solution and 10 ml vitamin solution per final liter.
- MAJOR: The generated record has no preparation steps for N2 dispensing, autoclaving, or filter-sterile post-autoclave additions.
- MAJOR: CoCl2 x 6 H2O and NiCl2 x 6 H2O are grounded to anhydrous CHEBI salts, and several trace salts lack `mediaingredientmech_chebi_term` mirrors.

## Recommended Edits

- Split the TOGO M1714 normalized representation into a main final medium plus nested `Trace elements solution` and `Vitamin solution` stocks.
- Encode final distilled water as 1000 ML_PER_L in the main medium and keep stock waters inside the corresponding solutions.
- Keep 20 G_PER_L NaCl and 0.1 G_PER_L CaCl2 x 2 H2O in the final medium; keep 1 G_PER_L NaCl and 0.13 G_PER_L CaCl2 x 2 H2O only in the trace-elements stock.
- Convert `Trace elements solution` and `Vitamin solution` to 10 ML_PER_L solution additions and keep their components in stock concentration units.
- Add preparation steps for mixing all ingredients except sucrose, NaHCO3, and vitamin solution, dispensing under N2, autoclaving, and adding filter-sterile sucrose, NaHCO3, and vitamin solution after autoclaving.
- Correct hydrated-salt CHEBI groundings for CoCl2 x 6 H2O and NiCl2 x 6 H2O, then regenerate merged YAML.

## Follow-up Checks

- Run an ignored-inclusive exact search for `TOGO:M1714`, `NBRC_M922`, `NO=922`, and `TOGO_M1714_Oceanithermus_profundus_medium` after repair to confirm the NBRC 922 source owner regenerates once.
- Rebuild merged YAML and verify the TOGO M1714 record keeps a distinct `merge_fingerprint` from the NBRC 404, DSMZ/KOMODO 975, and other Oceanithermus profundus media.
- Re-run open-schema, strict, reference, and term validation after the normalized owner is repaired and generated YAML is rebuilt.

## Additional Notes

None found.
