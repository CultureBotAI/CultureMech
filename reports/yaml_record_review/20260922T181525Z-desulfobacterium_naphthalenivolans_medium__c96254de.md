# YAML Record Review: desulfobacterium_naphthalenivolans_medium__c96254de

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfobacterium_naphthalenivolans_medium__c96254de.yaml`
- Started UTC: 2026-09-22T18:15:25Z
- Finished UTC: 2026-09-22T18:15:25Z
- Verdict: needs curation

## Target

Generated bacterial `desulfobacterium_naphthalenivolans_medium` record for MediaDive/JCM Medium J1151.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to MediaDive medium J1151 / JCM Medium J1151, `DESULFOBACTERIUM NAPHTHALENIVOLANS MEDIUM`.

The current JCM GRMD endpoint returns no record for GRMD 1151, but MediaDive J1151 is still reachable and TOGO M1233 also records the same name, original JCM medium id, and JCM GRMD 1151 source URL.

An exact ignored-file search found a separate TOGO M1233 same-name import. This generated record has a single `merged_from` source and is the direct MediaDive/JCM import.

The defined, bacterial, liquid classification is supported by the MediaDive and TOGO recipes.

## Evidence

The generated basal salt rows match MediaDive's J1151 normalization against a 1028 ml main solution: NaCl, KCl, MgCl2 x 6 H2O, KH2PO4, NH4Cl, CaCl2 x 2 H2O, Na2SO4, and resazurin are scaled from the archived JCM formula.

The main solution also contains 1 ml each of FeCl2 solution, Trace element solution, Selenite-tungstate solution, and Vitamin solution, followed by 30 ml 8% NaHCO3, 20 ml 1.5% Naphthalene solution in 2,2,4,4,6,8,8-heptamethylnonane, and 4 ml 5% Na2S x 9H2O.

Those stock additions were not represented in `solutions`. FeCl2, trace-element, selenite-tungstate, and vitamin stock ingredients are flattened at stock concentration as top-level final-medium ingredients.

The bicarbonate and sulfide additions are also flattened with the source milliliter amounts as `G_PER_L`: NaHCO3 is `30` and Na2S x 9 H2O is `4`.

The naphthalene stock is flattened as if the 1.5% stock concentration and heptamethylnonane solvent volume were final-medium gram-per-liter values: Naphthalene is `15` and 2,2,4,4,6,8,8-Heptamethylnonane is `100`.

The 970 ml source water row is absent from the generated ingredient list.

## Completeness

The three preparation steps preserve the main autoclave, post-cooling filter-sterilized additions, anaerobic serum-bottle distribution, pre-use reducing/naphthalene addition, and Vitamin solution filter-sterilization notes.

The structured table rows that name each stock addition did not survive, so the generated recipe cannot associate the MediaDive JCM 187, JCM 431, JCM 609, and Naphthalene solution components with their addition volumes.

## Findings

- Major issue: all referenced stock solutions are flattened into top-level ingredients instead of nested `solutions`.
- Major issue: 30 ml 8% NaHCO3 and 4 ml 5% Na2S x 9 H2O are represented as 30 and 4 G_PER_L final concentrations.
- Major issue: the 1.5% Naphthalene solution is represented with stock Naphthalene and heptamethylnonane quantities as final-medium G_PER_L rows.
- Major issue: FeCl2, trace-element, selenite-tungstate, and vitamin stock formulas are present at full stock concentrations in the final medium.
- Major issue: the 970 ml source water row is missing.
- Minor issue: the stock-addition table has been reduced to prose ending in colons rather than explicit addition rows.

## Recommended Edits

- Rebuild the normalized source record from MediaDive REST J1151 or TOGO M1233 with explicit stock solution records.
- Keep FeCl2 solution, Trace element solution, Selenite-tungstate solution, Vitamin solution, 8% NaHCO3, 1.5% Naphthalene solution, and 5% Na2S x 9H2O as milliliter additions.
- Move FeCl2, trace metals, selenite/tungstate, vitamins, naphthalene, and heptamethylnonane under their respective stock records.
- Restore the 970 ml water row or an equivalent total-volume representation for the main solution.
- Preserve the filtered, anaerobic, and N2-storage instructions on the specific stock solutions they modify.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after restructuring the record.
- Confirm the final naphthalene concentration is derived from adding 20 ml of 1.5% stock, not from treating 15 g/L as a final-medium quantity.
- Confirm bicarbonate and sulfide final amounts are computed from the 8% and 5% stock strengths and their addition volumes.
- Compare the direct MediaDive/JCM record against TOGO M1233 before any same-name deduplication.

## Additional Notes

MediaDive REST medium J1151 and TOGO M1233 were reachable during review. JCM GRMD 1151 was reachable but currently returned no medium record.
