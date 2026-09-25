# YAML Record Review: thermoplasma_acidophilum_medium__3d517987

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoplasma_acidophilum_medium__3d517987.yaml
- Started UTC: 2026-09-25T12:00:26Z
- Finished UTC: 2026-09-25T12:00:26Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:004181`, `thermoplasma_acidophilum_medium`, generated from KOMODO Medium 158 with a DSMZ Medium 158 / MediaDive `mediadive.medium:158` cross-reference.

## Validation

- LinkML schema: Passed with `linkml-validate`; no issues found.
- Strict validation: Passed with 0 ERROR rows; `/private/tmp/thermoplasma_acidophilum_medium__3d517987.strict.tsv` contained only the header.
- Reference validation: Passed; the validator ran 0 checks for this record.
- Term validation: Passed.
- Embedded curation history: Not checked; the available history validator covers standalone `history/` records, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The record points to KOMODO 158 and DSMZ 158, "THERMOPLASMA ACIDOPHILUM MEDIUM". DSMZ 158 is the same source also represented by the direct MediaDive record `thermoplasma_acidophilum_medium__d7d3722d` and by the TOGO M2384 record reviewed separately.

## Evidence

- DSMZ Medium 158 lists 1.320 g (NH4)2SO4, 0.372 g KH2PO4, 0.247 g MgSO4 x 7 H2O, 0.074 g CaCl2 x 2 H2O, 10 ml Trace element solution, 2.000 g Oxoid yeast extract, 20.000 g glucose, and 1000 ml freshly distilled water.
- DSMZ Medium 158 adjusts pH to 1.0 with 1 N H2SO4.
- DSMZ Medium 158 separately autoclaves yeast extract as a 10% w/v stock and glucose as a 50% w/v stock, then adds them to the sterile mineral salt medium.

## Completeness

The main salts, yeast extract, and glucose match DSMZ 158. The generated record omits both distilled-water rows, lacks all preparation steps, and flattens the 10 ml/L Trace element solution into direct top-level ingredients at their full 1 L stock strengths.

## Findings

- FeCl3 x 6 H2O, MnCl2 x 4 H2O, Na2B4O7 x 10 H2O, ZnSO4 x 7 H2O, CuCl2 x 2 H2O, Na2MoO4 x 2 H2O, VOSO4 x 5 H2O, and CoSO4 x 7 H2O are Trace element solution stock rows that are 100-fold too high if interpreted as final concentrations.
- The 1000 ml freshly distilled main water and 1000 ml Trace element solution water rows are both absent.
- The DSMZ pH-adjustment and separate 10% yeast extract and 50% glucose stock autoclaving instructions are absent.
- The recipe carries `ph_range: 1.0-2.0` from KOMODO plus `ph_value: 1.0` after merge; DSMZ 158 itself states pH 1.0.
- `H2SO4` is represented as a variable top-level ingredient even though the source uses 1 N H2SO4 only for pH adjustment.

## Recommended Edits

- Merge or reconcile this KOMODO/DSMZ 158 record with the direct DSMZ 158 and TOGO M2384 generated records instead of curating three independent Thermoplasma acidophilum records.
- Restore the 10 ml/L Trace element solution as stock structure and keep its 1 L ingredient rows scoped to that stock.
- Add main and trace-solution distilled-water rows.
- Add preparation steps for pH 1.0 adjustment with 1 N H2SO4 and separate autoclaving of 10% yeast extract and 50% glucose stocks.
- Prefer the DSMZ pH value of 1.0 unless another explicit source is curated as a named variant.

## Follow-up Checks

- Confirm whether KOMODO's apparent pH 1.0-2.0 range is from a secondary curation layer before preserving it.
- Re-run duplicate detection across `mediadive.medium:158`, `komodo.medium:158`, and TOGO M2384 after stock-aware repair.

## Additional Notes

No target-organism evidence was reviewed. The narrowed exact source search included ignored and hidden files and found the current KOMODO 158 record, TOGO M2384, and the direct DSMZ 158 `thermoplasma_acidophilum_medium__d7d3722d.yaml` record.
