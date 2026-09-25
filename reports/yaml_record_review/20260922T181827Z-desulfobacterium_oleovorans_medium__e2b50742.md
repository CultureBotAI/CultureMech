# YAML Record Review: desulfobacterium_oleovorans_medium__e2b50742

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfobacterium_oleovorans_medium__e2b50742.yaml`
- Started UTC: 2026-09-22T18:18:27Z
- Finished UTC: 2026-09-22T18:18:27Z
- Verdict: needs curation

## Target

Generated bacterial `desulfobacterium_oleovorans_medium` record for MediaDive/JCM Medium J1258.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is correctly grounded to MediaDive medium J1258 / JCM Medium J1258, `DESULFOBACTERIUM OLEOVORANS MEDIUM`.

An exact ignored-file search found separate TOGO M1354 and KOMODO 517 same-name imports; the KOMODO record also appears in the `DESULFOSUDIS_MEDIUM` merge. This generated record has a single `merged_from` source and is the MediaDive/JCM import.

The defined, bacterial, liquid classification is supported by the live source recipe.

## Evidence

The generated basal salt rows match MediaDive's J1258 normalization against a 1052 ml main solution: Na2SO4, KH2PO4, NH4Cl, NaCl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, and resazurin are scaled from the JCM formula.

The source also adds 1 ml each of FeCl2 solution, Trace element solution, and Selenite-tungstate solution before autoclaving, then after cooling adds 10 ml Trace vitamins, 1 ml Vitamin B12 solution, 10 ml Stearic solution, 20 ml 8% NaHCO3, and 8 ml 5% Na2S x 9H2O.

The generated record has only one empty `Steric solution` stub with concentration `10` G_PER_L. All other stocks and post-cooling additives are flattened into the top-level `ingredients` list.

The flattening caused cross-stock duplicate merges: `NaOH` was summed from 0.63 ml 2 N NaOH in the Stearic solution plus 0.4 g/L NaOH in the Selenite-tungstate solution, and `Vitamin B12` was summed from Trace vitamins plus the standalone 0.05 g/L Vitamin B12 stock.

Several raw volumes or stock concentrations are top-level final-medium rows: NaHCO3 is `20`, Na2S x 9 H2O is `8`, and Stearic acid is the stock concentration `32.7273` G_PER_L rather than the final amount from adding 10 ml of the stock.

The 1 L source water row is absent.

## Completeness

The main anaerobic boil, Balch-tube autoclave, aseptic post-cooling addition paragraph, and Stearic solution boiling/autoclave instructions survived as `preparation_steps`.

The actual stock-addition table did not survive structurally: its JCM 187, JCM 431, JCM 197, JCM 403, 8% NaHCO3, 5% Na2S x 9H2O, and Stearic solution rows have no milliliter addition records.

The source spells the table row as `Steric solution` but the detailed stock as `Stearic solution`; the generated stub preserves the table typo while separating it from the flattened stearic-acid stock contents.

## Findings

- Major issue: all referenced FeCl2, trace-element, selenite-tungstate, vitamin, B12, bicarbonate, sulfide, and stearic stock additions are missing as structured milliliter additions.
- Major issue: FeCl2, trace-element, selenite-tungstate, and vitamin stock formulas are flattened into the final medium at their stock concentrations.
- Major issue: NaHCO3 and Na2S x 9 H2O use raw source addition volumes as G_PER_L final concentrations.
- Major issue: Stearic acid and 2 N NaOH from the Stearic solution are flattened into the final recipe instead of nested under the stock.
- Major issue: `NaOH` and `Vitamin B12` each merge quantities from unrelated stocks.
- Major issue: the 1 L source water component is missing.
- Minor issue: the only `solutions` entry is an empty `Steric solution` stub with a G_PER_L concentration.

## Recommended Edits

- Rebuild the normalized source record from JCM 1258, MediaDive J1258, or TOGO M1354 with nested solution records and milliliter addition rows.
- Keep FeCl2 solution, Trace element solution, Selenite-tungstate solution, Trace vitamins, Vitamin B12 solution, Stearic solution, 8% NaHCO3, and 5% Na2S x 9H2O as stock additions.
- Move stearic acid, 2 N NaOH, vitamins, B12, FeCl2, trace metals, selenite, tungstate, and stock NaOH rows under their own stock formulas.
- Preserve the 10 ml Stearic solution preparation step on that stock, including heating under N2, autoclaving, and re-melting if needed.
- Restore the 1 L distilled-water row or an equivalent total-volume representation for the main solution.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after restructuring the record.
- Confirm `NaOH` and `Vitamin B12` are not deduplicated across unrelated stock scopes.
- Confirm final stearic acid, bicarbonate, and sulfide concentrations are computed from stock strengths and addition volumes.
- Compare the repaired MediaDive/JCM record against the TOGO and KOMODO same-name records before any future merge.

## Additional Notes

JCM GRMD 1258, MediaDive REST medium J1258, and TOGO M1354 were reachable during review.
