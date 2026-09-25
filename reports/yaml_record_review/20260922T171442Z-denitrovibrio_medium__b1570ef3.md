# YAML Record Review: denitrovibrio_medium__b1570ef3

- Repository: CultureMech
- Record: `data/merge_yaml/merged/denitrovibrio_medium__b1570ef3.yaml`
- Started UTC: 2026-09-22T17:14:42Z
- Finished UTC: 2026-09-22T17:14:42Z
- Verdict: needs curation

## Target

Generated bacterial `denitrovibrio_medium` record for TOGO M2551, linked to DSMZ Medium 881.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to TOGO M2551 and keeps the DSMZ Medium 881 PDF URL in `notes`.

The complex/undefined classification is not supported. Current DSMZ 881 and MediaDive mark the medium as defined and every substantive ingredient is a defined chemical or stock solution.

The linked DSMZ 881 source has diverged from the TOGO M2551 import. Current DSMZ/MediaDive 881 contains Na2CO3, Na2-fumarate, selenite-tungstate stock, Seven vitamins solution, Na2S, and pH 7.0-7.2; TOGO M2551 instead contains NaHCO3, NaNO3, no selenite-tungstate stock, no fumarate, no carbonate, and `ph: "6.8 - 7.2"`.

## Evidence

TOGO M2551 exposes Trace element solution SL-10 and Vitamin solution as 1 ml stock additions, and also includes the Trace element and Vitamin solution formulas inline. The generated record flattens those stock formulas into final-medium ingredients while leaving three empty solution placeholders for Na-resazurin, Trace element solution SL-10, and Vitamin solution.

Three stock-internal water rows were merged into the top-level water row, producing `2990.0 G_PER_L` distilled water from `1000.0`, `990.0`, and `1000.0` ml source rows.

Milligram quantities from Trace element solution SL-10 and the vitamin stock were imported as gram-per-liter final concentrations. Examples include 36 mg Na2MoO4 x 2 H2O as `36 G_PER_L`, 6 mg H3BO3 as `6 G_PER_L`, 100 mg MnCl2 x 4 H2O as `100 G_PER_L`, 190 mg CoCl2 x 6 H2O as `190 G_PER_L`, 80 mg p-Aminobenzoic acid as `80 G_PER_L`, and 300 mg Pyridoxine hydrochloride as `300 G_PER_L`.

The generated record models N2 gas as a variable-concentration ingredient. In both the TOGO import and the current DSMZ source, nitrogen or nitrogen/carbon dioxide gases are anaerobic preparation atmospheres.

The live DSMZ 881 recipe dissolves all ingredients except carbonate, fumarate, vitamins, and sulfide, sparges with 80% N2 / 20% CO2, dispenses under the same atmosphere, autoclaves, and adds carbonate, fumarate, vitamins, and sulfide from sterile anoxic stocks. None of those preparation details are present in the generated YAML.

## Completeness

The generated record lacks the current selenite-tungstate stock entirely and lacks the current carbonate and fumarate final substrates.

The Trace element solution SL-10 and vitamin stock are not usable as generated: their `composition` arrays are empty, their 1 ml additions are encoded as `1 G_PER_L`, and most of their stock ingredients are duplicated as top-level final ingredients.

The Na-resazurin 0.1% w/v 0.5 ml source addition is preserved only as an empty solution with a `0.5 G_PER_L` concentration.

## Findings

- Needs curation: TOGO M2551 is stale relative to the linked DSMZ Medium 881 source.
- Needs curation: `medium_type` and `composition_type` are complex/undefined even though DSMZ 881 is chemically defined.
- Needs curation: stock-internal water, trace metals, HCl, and vitamins are flattened into top-level final-medium ingredients.
- Needs curation: milligram stock quantities were converted to `G_PER_L` quantities.
- Needs curation: trace, vitamin, and resazurin solution additions are present as empty placeholders with gram-per-liter volumes.
- Needs curation: N2 gas is represented as an ingredient instead of an anoxic preparation atmosphere.
- Needs curation: current DSMZ pH, carbonate, fumarate, selenite-tungstate, and preparation steps are missing.
- Needs curation: `NiCl2 x 6 H2O` is grounded to an anhydrous `nickel dichloride` CHEBI term and should be rechecked during repair.

## Recommended Edits

- Refresh `data/normalized_yaml/bacterial/TOGO_M2551_Denitrovibrio_Medium.yaml` from live DSMZ Medium 881 before regenerating this record.
- Replace the stale NaHCO3 and NaNO3 rows with the current DSMZ carbonate and fumarate rows.
- Add the missing selenite-tungstate stock.
- Model Trace element solution SL-10, selenite-tungstate solution, Seven vitamins solution, sulfide, carbonate, fumarate, and resazurin at the correct DSMZ stock or final concentrations instead of flattening their stock contents as top-level rows.
- Change the medium and composition types to `DEFINED`.
- Move N2 and N2/CO2 handling into preparation or condition fields and retain pH 7.0-7.2 adjustment.
- Recheck the hydrated nickel chloride grounding.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after repair.
- Compare the regenerated record against both MediaDive REST medium 881 and the DSMZ Medium 881 PDF.
- Confirm no stock-internal water row contributes to top-level final water.
- Confirm no milligram stock quantity is emitted as an integer `G_PER_L` final concentration.

## Additional Notes

TOGO M2551, MediaDive REST medium 881, and the linked DSMZ Medium 881 PDF were all reachable during review.
