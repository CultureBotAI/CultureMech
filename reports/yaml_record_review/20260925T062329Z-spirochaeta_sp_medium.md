# YAML Record Review: spirochaeta_sp_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/spirochaeta_sp_medium.yaml
- Started UTC: 2026-09-25T06:21:59Z
- Finished UTC: 2026-09-25T06:23:30Z
- Verdict: needs curation

## Target

Generated merged YAML for DSMZ 1264 / KOMODO 1264, SPIROCHAETA SP. MEDIUM.

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/spirochaeta_sp_medium.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The record is grounded to DSMZ Medium 1264 and to KOMODO records that cite DSMZ Medium 1264.

The base DSMZ 1264 identity is valid, but the generated merge incorrectly treats the `for_dsm_14994` source as a duplicate instead of preserving the DSM 14994 changes described in the DSMZ PDF.

## Evidence

DSMZ 1264 lists a 1000 ml base medium for DSM 14957, DSM 14958, and DSM 14994 with 30.0 g NaCl, 0.3 g NH4Cl, 0.3 g CaCl2 x 2 H2O, 3.0 g MgCl2 x 2 H2O, 5.0 g soluble starch, 1.0 g yeast extract, 5.0 g peptone (Difco), 10.0 ml 10% pH 7.4 phosphate buffer, 1.0 ml Pfennig trace elements, 0.5 ml resazurin, and 1000.0 ml distilled water.

DSMZ 1264 directs boiling under N2, checking pH 7.4, autoclaving aliquots, and adding sterile 3% Na2S and vitamin B12 per 10 ml. It then has a DSM 14994-specific change block with 70.00 g NaCl, 0.20 ml 3% Na2S, and 0.25 ml 40% glucose.

The Pfennig trace elements stock is a separate 1000 ml solution containing EDTA, FeSO4 x 7 H2O, ZnSO4 x 7 H2O, H3BO3, CoCl2 x 6 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, MnCl2 x 4 H2O, CuCl2 x 2 H2O, and distilled water.

## Completeness

The generated record drops the 1000.0 ml distilled-water row, the 10.0 ml phosphate-buffer row, the 1.0 ml Pfennig trace-elements row, and the Pfennig stock water row. It also loses the DSM 14994-specific formulation by merging `for_dsm_14994` as a source duplicate.

## Findings

- Major: `for_dsm_14994` is merged as a duplicate even though the DSMZ PDF lists DSM 14994-specific NaCl, Na2S, and glucose changes.
- Major: Pfennig trace elements are flattened into the parent ingredients instead of being modeled as a 1.0 ml stock addition.
- Major: phosphate buffer, resazurin, 3% Na2S, and vitamin B12 source volumes are represented as `G_PER_L` concentrations; the generated `50` `G_PER_L` vitamin B12 row comes from a 50 ul per-10-ml sterile addition.
- Major: the source's 1000.0 ml main distilled water and 1000 ml Pfennig stock water rows are missing.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/spirochaeta_sp_medium.yaml` to preserve 10.0 ml phosphate buffer, 1.0 ml Pfennig trace elements, 0.5 ml resazurin, and 1000.0 ml distilled water.
- Keep Pfennig trace elements as a named 1.0 ml stock addition with its 1000 ml stock composition nested.
- Repair `data/normalized_yaml/bacterial/for_dsm_14994.yaml` to represent the DSM 14994 NaCl/Na2S/glucose changes as a variant of DSMZ 1264.
- Tighten the KOMODO/DSMZ merge so the DSM 14994 variant is no longer collapsed as a `SOURCE_DUPLICATE`.
- Regenerate `data/merge_yaml/merged/spirochaeta_sp_medium.yaml` from the repaired normalized records.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated record.
- Confirm `for_dsm_14994` is a variant child rather than a merged duplicate.
- Confirm the generated base record keeps 30.0 g NaCl and the DSM 14994 variant keeps 70.0 g NaCl plus its Na2S/glucose changes.
- Confirm Pfennig trace elements are nested under a 1.0 ml solution addition.

## Additional Notes

None found.
