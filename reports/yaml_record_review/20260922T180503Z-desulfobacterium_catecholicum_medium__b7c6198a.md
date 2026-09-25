# YAML Record Review: desulfobacterium_catecholicum_medium__b7c6198a

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfobacterium_catecholicum_medium__b7c6198a.yaml`
- Started UTC: 2026-09-22T18:05:03Z
- Finished UTC: 2026-09-22T18:05:03Z
- Verdict: needs curation

## Target

Generated bacterial `desulfobacterium_catecholicum_medium` record for MediaDive/JCM Medium J1257.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is correctly grounded to MediaDive medium J1257 / JCM Medium J1257, `DESULFOBACTERIUM CATECHOLICUM MEDIUM`.

An exact ignored-file search found separate KOMODO and TOGO records for the same named medium, but this generated record has a single `merged_from` source and is the MediaDive/JCM import rather than a cross-source merge.

The defined, bacterial, liquid classification is supported by the live source recipe.

## Evidence

The generated basal salts are recognizable as the JCM 1257 main solution imported through MediaDive: Na2SO4, KH2PO4, NH4Cl, NaCl, MgCl2 x 6 H2O, KCl, CaCl2 x 2 H2O, and resazurin are scaled from the source formula.

The source also adds FeCl2 solution from JCM 187, Trace element solution from JCM 187, and Selenite-tungstate solution from JCM 431 to the basal medium, then after cooling adds Trace vitamins from JCM 197, 10 ml 4% Sodium benzoate, 10 ml Pyrocatechol solution, 20 ml 8% NaHCO3, and 8 ml 5% Na2S x 9H2O.

Those stock solutions are not represented in `solutions`. Their internal stock ingredients were flattened into top-level ingredients, including 1.5 g/L FeCl2 x 4 H2O, 2.5 g/L FeCl2-stock HCl merged with the 0.06 ml pyrocatechol-stock HCl, the JCM 187 trace metals, the JCM 431 selenite-tungstate NaOH/selenite/tungstate rows, and the JCM 197 vitamin rows.

Several post-cooling additives also carry stock-volume or stock-concentration values as top-level `G_PER_L` rows: Sodium benzoate is `10`, NaHCO3 is `20`, Na2S x 9 H2O is `8`, and Pyrocatechol is `6`.

The source water row is absent from the generated ingredient list.

## Completeness

The anaerobic boiling, N2-CO2 cooling, dispensing, butyl-stopper sealing, autoclaving, and post-cooling aseptic anaerobic addition text survived in `preparation_steps`.

The detailed table of post-cooling solution additions did not survive as structured additions, so the recipe no longer says which component is a milliliter-per-liter stock addition and which component belongs inside a stock bottle.

The Pyrocatechol solution instructions survived only as a generic second `FILTER_STERILIZE` step; they are not linked to a Pyrocatechol stock that contains 0.06 g pyrocatechol, 0.06 ml 1 N HCl, and 10 ml water and must be freshly prepared prior to inoculation.

## Findings

- Major issue: no referenced stock solution is nested under `solutions`; JCM 187, JCM 431, and JCM 197 stock ingredients are flattened into the final recipe.
- Major issue: Sodium benzoate, NaHCO3, Na2S x 9 H2O, and Pyrocatechol use raw stock volumes or stock concentrations as `G_PER_L` final-medium concentrations.
- Major issue: unrelated HCl quantities from FeCl2 stock and Pyrocatechol stock were merged into one top-level `HCl` row.
- Major issue: the 1 L source water component is missing.
- Minor issue: the JCM instruction table and its stock-specific sterilization markers are only partially captured as prose.

## Recommended Edits

- Rebuild the normalized source record from JCM 1257 or the MediaDive J1257 REST structure with explicit solution records.
- Keep FeCl2 solution, Trace element solution, Selenite-tungstate solution, Trace vitamins, 4% Sodium benzoate, Pyrocatechol solution, 8% NaHCO3, and 5% Na2S x 9H2O as `ML_PER_L` stock additions.
- Move FeCl2, trace metals, selenite/tungstate, vitamins, pyrocatechol-stock HCl, and stock water rows into their respective `solutions` blocks.
- Restore the 1 L source water row or an equivalent total-volume representation for the main solution.
- Preserve Pyrocatechol solution's fresh, filter-sterilized, pre-inoculation preparation as stock-specific preparation metadata.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after restructuring the record.
- Confirm no JCM 187, JCM 431, or JCM 197 stock ingredient remains as a top-level final-medium ingredient.
- Confirm sodium benzoate, bicarbonate, sulfide, and pyrocatechol final concentrations are computed from their stock strengths and addition volumes, not from the addition volumes alone.
- Confirm the separate KOMODO 385 and TOGO M1353 records still deduplicate by evidence rather than by name alone.

## Additional Notes

JCM GRMD 1257 and MediaDive REST medium J1257 were reachable during review.
