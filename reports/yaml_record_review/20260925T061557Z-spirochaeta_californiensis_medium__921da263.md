# YAML Record Review: spirochaeta_californiensis_medium__921da263

- Repository: CultureMech
- Record: data/merge_yaml/merged/spirochaeta_californiensis_medium__921da263.yaml
- Started UTC: 2026-09-25T06:14:12Z
- Finished UTC: 2026-09-25T06:15:57Z
- Verdict: needs curation

## Target

Generated merged YAML for JCM 454, SPIROCHAETA CALIFORNIENSIS MEDIUM.

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/spirochaeta_californiensis_medium__921da263.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The record is nominally grounded to JCM 454, SPIROCHAETA CALIFORNIENSIS MEDIUM, but the merged YAML also contains `halolactibacillus_9g_medium` from MediaDive J1101 as a synonym and source.

That merge is not supported. JCM 454 and MediaDive J1101 have related but distinct main recipes, and the generated JCM 454 record now carries J1101-scaled concentrations for several parent ingredients.

## Evidence

JCM 454 lists 30.0 g NaCl, 2.76 g Na2CO3, 24.0 g NaHCO3, 0.2 g KCl, 0.2 g K2HPO4, 0.1 g MgCl2 x 6 H2O, 1.0 g NH4Cl, 0.4 g Na2S x 9 H2O, 0.5 g yeast extract, 5.0 g glucose, 2.0 ml trace vitamins from JCM 197, 1.0 ml trace minerals solution from JCM 228, and 1.0 mg resazurin. It directs dissolving all components except Na2CO3, NaHCO3, and Na2S x 9 H2O in 700 ml distilled water, autoclaving under N2, separately dissolving Na2CO3 and NaHCO3 in 300 ml distilled water, filter sterilizing, and adjusting to pH 9.0-9.5 if necessary.

MediaDive J1101 is HALOLACTIBACILLUS 9G MEDIUM at pH 9.0. Its 1011 ml main solution uses 10 g NaCl, 0.1 g yeast extract, 2 ml trace vitamins, 1 ml trace minerals solution, 0.5 mg resazurin, 680 ml distilled water, 300 ml alkaline solution, 20 ml autoclaved 1.0 M glucose, and 8 ml of a 5% Na2S x 9 H2O stock.

JCM 228 defines the trace minerals solution as a separate 1.0 L stock with nitrilotriacetic acid, Fe(NH4)2(SO4)2 x 6 H2O, Na2SeO3, Na2MoO4 x 2 H2O, Na2WO4 x 2 H2O, MnSO4 x n H2O, ZnSO4 x 7 H2O, NiCl2 x 6 H2O, CuSO4 x 5 H2O, and distilled water. JCM 197 defines trace vitamins as a separate 1.0 L stock.

## Completeness

The generated record loses the JCM 454 700 ml and 300 ml water structure, flattens trace-vitamin and trace-mineral stocks into direct parent ingredients, and overwrites the JCM 454 formula with J1101-derived quantities such as 9.8912 g/L NaCl, 0.098912 g/L yeast extract, 20 g/L glucose, and 8 g/L Na2S x 9 H2O.

## Findings

- Major: `halolactibacillus_9g_medium` is falsely merged into `spirochaeta_californiensis_medium` even though MediaDive J1101 is a distinct Halolactibacillus 9G medium with different NaCl, yeast extract, glucose, and Na2S handling.
- Major: the generated primary JCM 454 formula contains J1101-scaled concentrations instead of the 30.0 g NaCl, 0.5 g yeast extract, 5.0 g glucose, and 0.4 g Na2S x 9 H2O listed by JCM 454.
- Major: the JCM 454 pH range 9.0-9.5 was collapsed to `ph_value: 9.2`.
- Major: trace vitamins and trace minerals solution were flattened as direct parent ingredients, so the 2.0 ml and 1.0 ml stock-addition rows are missing and the stock compositions are no longer nested.
- Major: Na2CO3 and NaHCO3 are listed at alkaline-solution stock concentrations instead of being represented as the JCM 454 2.76 g and 24.0 g amounts dissolved in 300 ml distilled water.

## Recommended Edits

- Split `halolactibacillus_9g_medium` and `spirochaeta_californiensis_medium` by repairing the normalized records or tightening the merge fingerprint so JCM 1101 and JCM 454 do not collapse into one generated record.
- Repair `data/normalized_yaml/bacterial/spirochaeta_californiensis_medium.yaml` to preserve the JCM 454 pH range 9.0-9.5 and the exact JCM 454 parent amounts.
- Model the Na2CO3/NaHCO3 300 ml filtered solution, the 2.0 ml trace-vitamins addition, the 1.0 ml trace-minerals addition, and the 5% Na2S x 9 H2O pre-inoculation reducing solution explicitly.
- Preserve JCM 197 and JCM 228 stock compositions under their named solutions, including distilled-water rows.
- Regenerate `data/merge_yaml/merged/spirochaeta_californiensis_medium__921da263.yaml` from the repaired normalized records.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated records.
- Confirm `merged_from` no longer contains both `halolactibacillus_9g_medium` and `spirochaeta_californiensis_medium`.
- Confirm the JCM 454 generated record contains 30.0 g NaCl, 5.0 g glucose, and a pH range of 9.0-9.5.
- Confirm trace vitamins and trace minerals remain as 2.0 ml and 1.0 ml additions rather than direct stock ingredients.

## Additional Notes

None found.
