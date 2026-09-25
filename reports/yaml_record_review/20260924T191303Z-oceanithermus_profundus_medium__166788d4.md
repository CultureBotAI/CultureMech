# YAML Record Review: oceanithermus_profundus_medium__166788d4

- Repository: CultureMech
- Record: data/merge_yaml/merged/oceanithermus_profundus_medium__166788d4.yaml
- Started UTC: 2026-09-24T19:13:03Z
- Finished UTC: 2026-09-24T19:14:42Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/oceanithermus_profundus_medium__166788d4.yaml`, a generated bacterial `MediaRecipe` with id `CultureMech:008146` and source term `TOGO:M1595`.

The generated record has one source owner, `data/normalized_yaml/bacterial/TOGO_M1595_Oceanithermus_profundus_Medium.yaml`, for NBRC Medium 404.

## Validation

- LinkML open-schema validation: passed; no issues found.
- Strict validation: passed; `/private/tmp/oceanithermus_profundus_medium__166788d4.strict.tsv` contained only the header row.
- Reference validation: passed; the validator reported 0 configured checks for this record.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The TOGO/NBRC identity is valid: TOGO M1595 imports NBRC Medium 404, Oceanithermus profundus Medium.

The exact ignored-inclusive source search found several other `oceanithermus_profundus_medium` records, including the KOMODO/DSMZ 975 source-duplicate cluster and TOGO M1714/M2283 records. This review is scoped to NBRC 404 / TOGO M1595 because the sibling files use different provider ids and need their own source checks.

## Evidence

Checked the generated TOGO M1595 record, the normalized TOGO M1595 owner, an ignored-inclusive exact repository search for TOGO M1595, NBRC M404, and the `oceanithermus_profundus_medium` slug, the fetched TOGO M1595 REST payload, and the official NBRC 404 page.

NBRC 404 has three recipe scopes:

- Main medium: 1 L distilled water, salts, sucrose, HEPES, yeast extract, tryptone, 1 ml vitamin solution, 1 ml trace element solution, and N2.
- Vitamin stock: mg quantities of vitamins made up to 1 L.
- Trace element stock: salts and nitrilotriacetic acid made up to 1 L, with pH adjusted to 6.5 using KOH.

NBRC also says to prepare the medium anaerobically under N2, omit CaCl2, MgCl2, KNO3, tryptone, yeast extract, vitamins, and sucrose before autoclaving, and add those sterile stock solutions to the cooled sterile medium.

## Completeness

The generated YAML does not preserve the three source scopes:

- Main-medium water, vitamin-stock water, and trace-stock water are collapsed into one generated `3.0 G_PER_L` ingredient. The normalized owner has reduced this to `1.0 G_PER_L`, but the unit is still wrong and the stock waters are still not nested.
- Main-medium NaCl at 30 G_PER_L is summed with trace-stock NaCl at 1 G_PER_L and emitted as 31 G_PER_L.
- Main-medium CaCl2 x 2 H2O at 0.33 G_PER_L is summed with trace-stock CaCl2 x 2 H2O at 0.1 G_PER_L and emitted as `0.43000000000000005` G_PER_L.
- Vitamin and trace-element stock rows are flattened as final G_PER_L ingredients.
- `Vitamin solution` and `Trace element solution` are represented as 1 G_PER_L solution placeholders instead of 1 ML_PER_L stock additions with nested composition.
- KOH is emitted as a variable final ingredient, but the source uses it in pH adjustment of the trace stock and final medium.
- No preparation steps capture anaerobic N2 handling, pH 7.0-7.5, autoclaving, or sterile post-autoclave additions.

## Findings

- BLOCKER: The TOGO M1595 owner flattens vitamin and trace-element stock components into final-medium rows, causing stock concentrations to be interpreted as final concentrations.
- BLOCKER: NaCl and CaCl2 x 2 H2O are summed across the main medium and trace stock; the generated values 31 and 0.43000000000000005 G_PER_L are not source rows.
- MAJOR: The two imported stock rows use 1 G_PER_L placeholders even though the source adds 1 ml vitamin solution and 1 ml trace element solution per final liter.
- MAJOR: Distilled water is represented as G_PER_L and is collapsed across the main medium and two stock solutions.
- MAJOR: Na2SeO3 x 5 H2O is imported as 0.3 G_PER_L even within the stock list, while the NBRC trace stock lists 0.3 mg per liter.
- MAJOR: KOH and the anaerobic post-autoclave stock-addition instructions are not represented in `preparation_steps`.
- MINOR: KNO3 still has a legacy `mediaingredientmech_term`, and several hydrated trace salts lack exact CHEBI mirrors.

## Recommended Edits

- Split the TOGO M1595 normalized representation into a main final medium plus nested `Vitamin solution` and `Trace element solution` stocks.
- Encode final distilled water as 1000 ML_PER_L in the main medium and keep stock waters inside the corresponding solutions.
- Keep 30 G_PER_L NaCl and 0.33 G_PER_L CaCl2 x 2 H2O in the final medium; keep 1 G_PER_L NaCl and 0.1 G_PER_L CaCl2 x 2 H2O only in the trace-element stock.
- Convert `Vitamin solution` and `Trace element solution` to 1 ML_PER_L stock additions and keep their components in stock concentration units, including 0.3 MG_PER_L Na2SeO3 x 5 H2O for the trace stock.
- Move KOH into pH-adjustment preparation steps and add steps for N2 anaerobic preparation, autoclaving, cooling, and stock-solution additions.
- Finish CHEBI mirror cleanup for KNO3 and hydrated trace salts, then regenerate merged YAML.

## Follow-up Checks

- Run an ignored-inclusive exact search for `TOGO:M1595`, `NBRC_M404`, `NO=404`, and `TOGO_M1595_Oceanithermus_profundus_Medium` after repair to confirm the NBRC 404 source owner regenerates once.
- Rebuild merged YAML and verify the TOGO M1595 record keeps a distinct `merge_fingerprint` from the DSMZ/KOMODO 975 cluster and the other TOGO Oceanithermus profundus media.
- Re-run open-schema, strict, reference, and term validation after the normalized owner is repaired and generated YAML is rebuilt.

## Additional Notes

None found.
