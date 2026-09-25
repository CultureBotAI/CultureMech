# YAML Record Review: desulfitobacterium_medium__9eabf335

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfitobacterium_medium__9eabf335.yaml`
- Started UTC: 2026-09-22T17:44:10Z
- Finished UTC: 2026-09-22T17:44:10Z
- Verdict: needs curation

## Target

Generated bacterial `desulfitobacterium_medium` record for DSMZ Medium 663.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to DSMZ Medium 663 and the live MediaDive REST payload agrees that DSMZ 663 is `DESULFITOBACTERIUM MEDIUM`.

The complex/undefined classification is supported by yeast extract.

The generated record was emitted from the MediaDive-derived normalized source `data/normalized_yaml/bacterial/desulfitobacterium_medium.yaml`; a second KOMODO shadow record for the same DSMZ medium remains separate and carries the unsupported `Aerobic: Yes` note.

## Evidence

DSMZ 663 adds 5.00 ml Trace element solution and 2.00 ml Wolin's vitamin solution (10x) to the main liter-scale recipe. The generated record has no `solutions` block, so both stock formulations are flattened into ordinary final-medium ingredients.

The generated `CaCl2 x 2 H2O` row is `0.1297915 G_PER_L` with a merge note for `0.0297915` and `0.1`; this incorrectly sums the main-solution calcium chloride final contribution with the 0.1 g/L CaCl2 stock concentration from the trace element solution.

All other trace-element components are present at stock strength as top-level rows: Nitrilotriacetic acid `12.8 G_PER_L`, FeCl2 x 4 H2O `0.2 G_PER_L`, MnCl2 x 4 H2O `0.1 G_PER_L`, CoCl2 x 6 H2O `0.17 G_PER_L`, ZnCl2 `0.1 G_PER_L`, CuCl2 `0.02 G_PER_L`, H3BO3 `0.01 G_PER_L`, Na2MoO4 x 2 H2O `0.01 G_PER_L`, NiCl2 x 6 H2O `0.03 G_PER_L`, NaCl `1 G_PER_L`, and Na2SeO3 x 5 H2O `0.03 G_PER_L`.

Every Wolin's vitamin solution component is likewise emitted at stock strength even though the source adds only 2 ml 10x vitamin solution per liter: Biotin `0.02 G_PER_L`, Folic acid `0.02 G_PER_L`, Pyridoxine hydrochloride `0.1 G_PER_L`, Thiamine HCl `0.05 G_PER_L`, Riboflavin `0.05 G_PER_L`, Nicotinic acid `0.05 G_PER_L`, Calcium D-(+)-pantothenate `0.05 G_PER_L`, Vitamin B12 `0.001 G_PER_L`, p-Aminobenzoic acid `0.05 G_PER_L`, and (DL)-alpha-Lipoic acid `0.05 G_PER_L`.

DSMZ 663 lists 1000 ml distilled water in the main solution and 1000 ml water in each stock solution; no water row is present in the generated record.

## Completeness

The generated preparation steps preserve DSMZ's main anoxic autoclaving procedure and the trace-element pH 6.5 preparation note.

Stock boundaries are missing for the Trace element solution from DSMZ Medium 144 and Wolin's vitamin solution from DSMZ Medium 120, and the source instruction to add pyruvate, thiosulfate, vitamins, cysteine, and sulfide from sterile anoxic stocks is represented only as text.

The generated file lacks equipment context for Hungate tubes, filtration, autoclaving, and gassing from the MediaDive REST payload.

## Findings

- Needs curation: 5.00 ml Trace element solution was flattened at stock concentrations into top-level final-medium ingredients.
- Needs curation: 2.00 ml Wolin's vitamin solution (10x) was flattened at stock concentrations into top-level final-medium ingredients.
- Needs curation: direct main-solution CaCl2 and trace-stock CaCl2 were summed into `0.1297915 G_PER_L`.
- Needs curation: the record has no structured `solutions` block for either DSMZ stock solution.
- Needs curation: water rows from the main solution and both stocks are absent.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfitobacterium_medium.yaml` so Trace element solution and Wolin's vitamin solution stay as stock solutions added at 5.00 ml/L and 2.00 ml/L.
- Keep the main-solution `0.0297915 G_PER_L` CaCl2 contribution separate from the trace-stock CaCl2 row.
- Preserve DSMZ Medium 144 and DSMZ Medium 120 stock identities on the nested stock records.
- Add distilled water to the main recipe and to the two stock definitions if water rows are in scope for generated output.
- Consider structured stock records, where possible, for pyruvate, thiosulfate, cysteine, and sulfide because DSMZ says they are added from sterile anoxic stocks after autoclaving.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after regeneration.
- Confirm no Trace element solution component remains as a top-level final-medium ingredient.
- Confirm no Wolin's vitamin solution component remains as a top-level final-medium ingredient.
- Confirm top-level CaCl2 is no longer a sum across the main solution and the trace stock.
- Confirm the anaerobic preparation step still survives regeneration.

## Additional Notes

MediaDive REST medium 663 and the DSMZ Medium 663 PDF were reachable during review and agreed on the source composition.
