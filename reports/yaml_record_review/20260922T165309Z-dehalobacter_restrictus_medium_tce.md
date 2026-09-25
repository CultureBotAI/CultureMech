# YAML Record Review: dehalobacter_restrictus_medium_tce

- Repository: CultureMech
- Record: `data/merge_yaml/merged/dehalobacter_restrictus_medium_tce.yaml`
- Started UTC: 2026-09-22T16:53:09Z
- Finished UTC: 2026-09-22T16:53:09Z
- Verdict: needs curation

## Target

Generated bacterial `dehalobacter_restrictus_medium_tce` record for TOGO M2745, linked to DSMZ Medium 732.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to TOGO M2745 and keeps the linked DSMZ Medium 732 PDF URL in `notes`.

The external identity should be rechecked against the current DSMZ/MediaDive 732 record. TOGO's component payload still lists 860 ml Solution A and 10 ml Solution E, while both the current DSMZ PDF and MediaDive REST record list 870 ml Solution A and 2 ml Solution E in the 1008 ml main recipe.

Most chemical groundings for hydrate salts and vitamins are plausible, but nickel dichloride hexahydrate is grounded to CHEBI:34887, whose label is nickel dichloride rather than the hexahydrate. `N2 gas` lacks a CHEBI term despite the sibling `Nitrogen gas` rows being grounded to CHEBI:17997.

## Evidence

DSMZ 732 is assembled from stock solutions, not from one flat ingredient list: 870 ml Solution A, 100 ml Solution B, 10 ml Solution C, 1 ml Solution D, 2 ml Solution E, 10 ml Solution F, and 15 ml Solution G.

The generated record contains those solution placeholders, but every stock component is also promoted to a top-level ingredient. The result includes impossible water and stock-internal amounts in final-medium context, including `3980.0 G_PER_L` distilled water, trace-solution salts, both Wolin's vitamin solution components, Seven vitamins solution components, 13.5 ml hexadecane as `13.5 G_PER_L`, and 1.5 ml tetrachloroethene as `1.5 G_PER_L`.

Milligram stock quantities were imported as gram-per-liter quantities without mg-to-g conversion: Solution D has 36 mg Na2MoO4 x 2 H2O, 6 mg H3BO3, 100 mg MnCl2 x 4 H2O, 190 mg CoCl2 x 6 H2O, 24 mg NiCl2 x 6 H2O, 2 mg CuCl2 x 2 H2O, 70 mg ZnCl2, and 10 mg AlCl3 per liter, but the generated rows store 36, 6, 100, 190, 24, 2, 70, and 10 `G_PER_L`.

The two vitamin stocks were collapsed and duplicated inconsistently. For example, `Vitamin B12` was merged as `100.1 G_PER_L` from 0.1 and 100, `p-Aminobenzoic acid` was merged as `85.0 G_PER_L` from 5 and 80, and `Nicotinic acid` was merged as `205.0 G_PER_L` from 5 and 200, even though those values belong to separate Wolin and Seven vitamin stock recipes.

## Completeness

The nested stock structure of DSMZ 732 is mostly absent: Solutions A through G point at external `mediadive.solution:*` records rather than containing compositions, while Na-resazurin, Vitamin solution of medium 141, and Vitamin solution of medium 503 are empty.

Gas atmospheres and solution preparation instructions are represented as variable ingredients. CO2/N2 sparging, 80% H2 / 20% CO2 pressurization to 0.5 bar, 100% N2 stock preparation, autoclaving, filtration, pH 7.2 before inoculation, and "add Solution G only after inoculation" are all source procedure metadata, not normal ingredients.

`high_metal: true` is not reliable here because the trace element mg quantities have been scaled as grams per liter.

`medium_type: COMPLEX` and `composition_type: UNDEFINED` are supported by the 0.10 g Bacto peptone in Solution A.

## Findings

- Needs curation: DSMZ stock components are flattened to top-level ingredients and double-counted alongside their stock solution placeholders.
- Needs curation: milligram trace and vitamin stock amounts are off by a factor of 1000 as `G_PER_L`.
- Needs curation: volume additions for Solution A-G, resazurin, hexadecane, and tetrachloroethene are encoded as `G_PER_L`.
- Needs curation: the record uses stale TOGO volumes for Solution A and Solution E relative to the current linked DSMZ 732 source.
- Needs curation: vitamins shared by Wolin's vitamin solution and Seven vitamins solution were merged across stock boundaries.
- Needs curation: CO2, N2, and 2 N NaOH are preparation details or pH adjustment reagents rather than final top-level ingredients.

## Recommended Edits

- Re-curate from current DSMZ Medium 732 or MediaDive 732, not the stale TOGO main-solution amounts.
- Keep Solutions A-G as first-class stock additions with 870/100/10/1/2/10/15 ml volumes in the final medium.
- Move each stock's composition into the appropriate `solutions[].composition` entry and remove stock-internal water, salts, vitamins, gases, NaOH, hexadecane, and tetrachloroethene from top-level final-medium `ingredients`.
- Preserve milligram units for trace and vitamin stocks, or convert to g/L with the correct `0.001` factor.
- Keep Wolin's vitamin solution and Seven vitamins solution chemically separate so identically named vitamins are not summed across different stocks.
- Represent gas atmospheres, autoclaving, filtration, the pH-7 trace-element adjustment, final pH 7.2, and post-inoculation Solution G addition as preparation steps.
- Recheck `high_metal` after the trace-stock units have been corrected.
- Ground `N2 gas` consistently to CHEBI:17997 and ground `NiCl2 x 6 H2O` to the hydrated nickel chloride term if an appropriate CHEBI class exists.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after curation.
- Confirm the final recipe volumes sum to DSMZ's 1008 ml, not TOGO's 1006 ml.
- Confirm the final ingredient list no longer contains liters of stock water or milligram vitamin amounts as grams per liter.
- Confirm Wolin's vitamin solution and Seven vitamins solution still both contain their own vitamin B12, p-aminobenzoic acid, nicotinic acid, biotin, pantothenate, pyridoxine, and thiamine entries.

## Additional Notes

M2745 was checked through the TOGO API; the linked DSMZ `DSMZ_Medium732.pdf`; and MediaDive REST medium 732.
