# YAML Record Review: NMS MEDIUM FOR METHYLOCYSTIS SP.

- Repository: CultureMech
- Record: data/merge_yaml/merged/nms_medium_for_methylocystis_sp.yaml
- Started UTC: 2026-09-24T17:45:55Z
- Finished UTC: 2026-09-24T17:45:55Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:000621`
- Name: `nms_medium_for_methylocystis_sp`
- Original name: `NMS MEDIUM FOR METHYLOCYSTIS SP.`
- Media term: `mediadive.medium:1179`, DSMZ Medium 1179
- Category: `bacterial`
- Source owners: `data/normalized_yaml/bacterial/nms_medium_for_methylocystis_sp.yaml`, `data/normalized_yaml/bacterial/nms_medium_for_methanotrophs.yaml`
- Merge state: DSMZ/MediaDive medium 1179 merged with KOMODO medium 1179

## Validation

- Open LinkML schema validation: passed with no issues.
- Strict validation: passed; `/private/tmp/nms_medium_for_methylocystis_sp.strict.tsv` contained only the TSV header.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

- The duplicate grouping is plausible: the KOMODO source explicitly says `DSMZ Medium: 1179 (mediadive.medium:1179)` and has the same ingredient signature as the direct DSMZ owner.
- The exact hidden, no-ignore search for `mediadive.medium:1179`, `komodo.medium:1179`, `DSMZ Medium 1179`, `nms_medium_for_methylocystis_sp`, and `nms_medium_for_methanotrophs` found the expected DSMZ and KOMODO normalized sources, their indexes, and this generated record. Ignored files were included.
- The source is related to DSMZ medium 632 because it reuses that medium's trace element solution, but the main formula is a distinct liquid NMS medium for Methylocystis.

## Evidence

- DSMZ 1179 defines the final liter as 1 g MgSO4 x 7 H2O, 0.2 g CaCl2 x 6 H2O, 4 mg Fe-EDTA, 1 g KNO3, 0.5 ml trace element solution from medium 632, 0.272 g KH2PO4, 0.717 g Na2HPO4 x 12 H2O, and 1000 ml distilled water.
- DSMZ 1179 instructs preparation at pH 6.8 and says to dispense into growth vessels, add 50% methane to the gas phase when using sealed vessels, and autoclave at 121 deg C for 15 min.
- Live MediaDive 1179 represents `Trace element solution` as a nested 1000 ml stock with 500 mg Na2-EDTA, 200 mg FeSO4 x 7 H2O, 10 mg ZnSO4 x 7 H2O, 3 mg MnCl2 x 4 H2O, 30 mg H3BO3, 20 mg CoCl2 x 6 H2O, 1 mg CaCl2 x 2 H2O, 2 mg NiCl2 x 6 H2O, and 3 mg Na2MoO4 x 2 H2O.
- The generated merged record preserves pH 6.8 and the main-solution ingredient values, including 4 mg/L Fe(III)-EDTA.

## Completeness

- The main-liquid formula and gas-phase handling note are present.
- The 0.5 ml/L trace element stock addition is not represented; only the undiluted trace-stock contents remain as top-level final-medium rows.

## Findings

- Critical: DSMZ 1179's trace element stock was flattened into top-level final-medium rows. The generated `Na2-EDTA 0.5 G_PER_L`, `FeSO4 x 7 H2O 0.2 G_PER_L`, `ZnSO4 x 7 H2O 0.01 G_PER_L`, `MnCl2 x 4 H2O 0.003 G_PER_L`, `H3BO3 0.03 G_PER_L`, `CoCl2 x 6 H2O 0.02 G_PER_L`, `CaCl2 x 2 H2O 0.001 G_PER_L`, `NiCl2 x 6 H2O 0.002 G_PER_L`, and `Na2MoO4 x 2 H2O 0.003 G_PER_L` rows are stock concentrations from a solution dosed at 0.5 ml/L.
- Major: the generated record cannot distinguish the main-solution calcium source, `CaCl2 x 6 H2O`, from the trace-stock `CaCl2 x 2 H2O`; both now look like final ingredients.

## Recommended Edits

- Recurate the DSMZ 1179 representation so `Trace element solution` remains a subordinate stock dosed at 0.5 ml/L.
- Keep the DSMZ 632 trace stock recipe attached to the stock solution, or encode the cross-reference to DSMZ 632 explicitly if the nested recipe should stay single-sourced there.
- Rebuild the DSMZ/KOMODO 1179 merged record after fixing the DSMZ normalized owner.

## Follow-up Checks

- Confirm the regenerated record still merges the direct DSMZ 1179 source with KOMODO 1179.
- Confirm no trace-stock ingredient appears as a final top-level row unless it is explicitly scaled by the 0.5 ml/L stock dose.
- Confirm pH 6.8 and the 50% methane gas-phase instruction still render after regeneration.
- Run open schema, strict, reference, and term validation on the regenerated target.

## Additional Notes

- None found.
