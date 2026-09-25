# YAML Record Review: desulfocella_medium__34fcb342

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfocella_medium__34fcb342.yaml`
- Started UTC: 2026-09-22T18:33:19Z
- Finished UTC: 2026-09-22T18:33:19Z
- Verdict: needs curation

## Target

Generated bacterial `desulfocella_medium` record for MediaDive/JCM Medium J1256.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is correctly grounded to MediaDive medium J1256 / JCM Medium J1256, `DESULFOCELLA MEDIUM`.

An exact ignored-file search found one separate TOGO M1352 same-name import, plus a distinct `DESULFOCELLA HALOPHILA MEDIUM` record. This generated record has a single `merged_from` source and is the direct MediaDive/JCM import.

The defined, bacterial, liquid classification is supported by the live source recipe.

## Evidence

The generated basal rows match MediaDive's J1256 normalization against a 1051 ml final volume: Na2SO4, KH2PO4, NH4Cl, NaCl, MgCl2 x 6 H2O, KCl, CaCl2 x 2 H2O, and resazurin are scaled from the JCM table.

The source also contains 1 ml each of FeCl2 solution, Trace element solution, and Selenite-tungstate solution before autoclaving, plus post-cooling additions of 10 ml Trace vitamins, 10 ml Substrate solution, 20 ml 8% NaHCO3 solution, and 8 ml 5% Na2S x 9H2O solution.

The generated YAML has no `solutions` block. FeCl2, JCM 187 trace elements, JCM 431 selenite-tungstate ingredients, JCM 197 vitamins, and the Substrate solution's butyrate/caproate/octanoate formula are all flattened into the top-level ingredient list.

NaHCO3 and Na2S x 9 H2O also use raw source addition volumes as final `G_PER_L` values: 20 and 8 respectively.

The 1 L main water row and the 10 ml Substrate solution water row are absent.

## Completeness

The main anaerobic boil, Balch-tube dispensing, autoclaving, and post-cooling aseptic addition paragraph survived.

The stock-addition table did not survive as structured milliliter additions, and the `*` marker for filter-sterilized Trace vitamins and bicarbonate is preserved only as prose.

## Findings

- Major issue: all FeCl2, trace-element, selenite-tungstate, trace-vitamin, substrate, bicarbonate, and sulfide stock additions are flattened instead of nested under `solutions`.
- Major issue: substrate-stock butyrate, caproate, and octanoate are represented as 70, 30, and 15 G_PER_L final concentrations.
- Major issue: 20 ml 8% NaHCO3 and 8 ml 5% Na2S x 9 H2O use raw addition volumes as G_PER_L final concentrations.
- Major issue: source water rows are missing.
- Minor issue: filter-sterilization markers are only retained in prose.

## Recommended Edits

- Rebuild the normalized source record from JCM 1256, MediaDive J1256, or TOGO M1352 with explicit milliliter additions for all stocks.
- Keep FeCl2 solution, Trace element solution, Selenite-tungstate solution, Trace vitamins, Substrate solution, 8% NaHCO3, and 5% Na2S x 9H2O as stock additions.
- Move trace metals, selenite/tungstate, vitamins, and substrate organic acids under nested stock solution records.
- Compute bicarbonate, sulfide, and substrate final concentrations from stock strengths and addition volumes.
- Restore main-solution and Substrate-solution water rows within their respective scopes.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after restructuring the record.
- Confirm the corrected top-level ingredients contain no full-strength JCM 187, JCM 431, JCM 197, or Substrate stock rows.
- Confirm butyrate/caproate/octanoate final amounts are computed from adding 10 ml of Substrate solution.
- Compare the repaired MediaDive/JCM record against TOGO M1352 before any same-name deduplication.

## Additional Notes

JCM GRMD 1256, MediaDive REST medium J1256, and TOGO M1352 were reachable during review.
