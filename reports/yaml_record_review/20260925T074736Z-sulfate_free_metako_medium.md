# YAML Record Review: Sulfate-Free Metako Medium

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfate_free_metako_medium.yaml` (`CultureMech:007732`)
- Started UTC: `2026-09-25T07:47:36Z`
- Finished UTC: `2026-09-25T07:48:43Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfate_free_metako_medium.yaml` |
| Normalized source | `data/normalized_yaml/bacterial/TOGO_M1205_Sulfate-Free_Metako_Medium.yaml` |
| CultureMech ID | `CultureMech:007732` |
| Media term | `TOGO:M1205` |
| Original source | JCM `JCM_M1126`, Sulfate-Free Metako Medium |
| Merge fingerprint | `f69e2e4af5359991c5a3d70d0a9c5d604553e3245af7ee62fa844a9646e74a52` |
| Merged from | `TOGO_M1205_Sulfate-Free_Metako_Medium` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors, and the TSV contained only its header. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected stable identifier, media term, TOGO source, JCM original source, and single-source merge fingerprint for TOGO M1205/JCM 1126.

Exact gitignore-independent searches with `--no-ignore --hidden` for `TOGO:M1205`, `JCM_M1126`, `CultureMech:007732`, and `sulfate_free_metako_medium` found the TOGO M1205 owner, the paired TOGO M1206/JCM_M1126-2 strain-specific variant, and a same-JCM-source MediaDive import at `sulfate_free_metako_medium__b4a668be.yaml`. Those hits indicate duplicate source representations that should be compared after TOGO M1205 is reconstructed, but they do not show a wrong CultureMech ID or an accidental source swap in this generated file.

Most simple salts are grounded to plausible ChEBI terms. The hydrate-bearing `CoCl2*6H2O` and `NiCl2*6H2O` rows currently point at anhydrous cobalt dichloride and nickel dichloride labels, so those two exact hydrate groundings need a source-level check while repairing the formula.

## Evidence

The TOGO M1205 JSON and the current JCM 1126 page agree that the basal medium is prepared as a 1 L table containing NaCl, CaCl2*2H2O, KH2PO4, NH4Cl, 1 mg resazurin, MgCl2*6H2O, KCl, NaHCO3, 12 mg SrCl2*6H2O, 3 mg NaF, 85 mg KBr, 1 mg LiCl, 34 mg Na2B4O7*10H2O, 1 ml trace element solution, 0.4 ml selenite-tungstate solution, 2 ml trace vitamins solution, and an N2/CO2 headspace.

Both sources then add 10 ml of 1 M trimethylamine per liter from a sterile anaerobic stock and, immediately before inoculation, 2.5 ml/L each of 5% Na2S*9H2O and 5% L-Cysteine*HCl*H2O solutions. The trace-element stock is a separate 1 L stock; its salts are not final-medium gram-per-liter rows.

The generated YAML flattens stock-solution membership and volume additions into top-level ingredients or empty solution records. For example, the trace stock contributes 1 ml/L to the medium, but its `MnCl2*4H2O` stock row appears at `0.61 G_PER_L` in the final ingredient list instead of remaining nested under that stock or being converted to its final 0.001x contribution.

## Completeness

The generated record is incomplete for curation because it loses the recipe's hierarchy, stock addition sequence, anaerobic handling, overnight stand after autoclaving, and pre-inoculation reducing-solution additions.

`target_organisms` is absent. No growth target was inferred from the JCM medium page or TOGO recipe because neither fetched medium source asserts an organism that grew on the recipe.

The generated file is also stale relative to the maintained normalized source: the normalized source has the September water-duplicate repair, while the generated YAML still sums the basal 1 L water row and the trace-stock 1 L water row to `2.0 G_PER_L`.

## Findings

- The basal milligram salts were converted to gram-per-liter magnitudes: `Resazurin` is `1 G_PER_L` instead of 1 mg/L, `KBr` is `85 G_PER_L` instead of 85 mg/L, `Na2B4O7*10H2O` is `34 G_PER_L` instead of 34 mg/L, `SrCl2*6H2O` is merged to `12.01 G_PER_L` from separate basal and trace-stock scopes, `NaF` is `3 G_PER_L` instead of 3 mg/L, and `LiCl` is `1 G_PER_L` instead of 1 mg/L.
- The trace-element solution was flattened into final ingredients at full stock strength. Its 0.01 g/L `SrCl2*6H2O` stock row was also summed into the basal strontium chloride row, creating a cross-scope duplicate merge.
- All six solution additions are empty and use `G_PER_L` for what are volume additions: 1 ml/L trace elements, 0.4 ml/L selenite-tungstate solution, 2 ml/L trace vitamins, 10 ml/L 1 M trimethylamine, and two 2.5 ml/L reducing-agent stocks.
- The top-level gas rows duplicate nitrogen as both `Nitrogen gas` and `N2`; the sources use an N2/CO2 gas stream for the basal bottle atmosphere and N2 storage for the post-autoclave stock additions, not final soluble ingredient concentrations.
- Preparation instructions are absent, including the N2/CO2 distribution step, autoclaving under stoppers, overnight stand, sterile anaerobic trimethylamine addition, and aseptic pre-inoculation reducing-solution addition.
- `CoCl2*6H2O` and `NiCl2*6H2O` drop waters of crystallization in their current primary ChEBI labels.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M1205_Sulfate-Free_Metako_Medium.yaml` or the TOGO import/merge path, then regenerate `data/merge_yaml/merged/sulfate_free_metako_medium.yaml`.
- Keep basal salts at their source magnitudes, converting milligram rows to g/L values, and do not sum the basal `SrCl2*6H2O` row with the trace-stock `SrCl2*6H2O` row.
- Represent the trace-element stock as a nested solution, and represent the selenite-tungstate, trace-vitamin, trimethylamine, Na2S*9H2O, and L-Cysteine*HCl*H2O additions as volume-per-liter stock additions or equivalent structured solution references instead of empty `G_PER_L` solutions.
- Preserve the TOGO cross-references for M431 and M701 and make the JCM 431/JCM 682 provenance recoverable in notes or structured source metadata where the schema supports it.
- Add preparation steps for anaerobic dispensing under N2/CO2, sealed autoclaving, overnight standing, post-autoclave trimethylamine addition, and pre-inoculation reducing-solution addition.
- Check exact hydrate ChEBI mappings for `CoCl2*6H2O` and `NiCl2*6H2O` while the trace stock is being repaired.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `TOGO:M1205`, `JCM_M1126`, `CultureMech:007732`, and `sulfate_free_metako_medium` to confirm the repaired TOGO record, the TOGO M1206 variant, and the MediaDive J1126 representation still have intentional ownership boundaries.
- Compare the regenerated TOGO M1205 final concentrations against `data/merge_yaml/merged/sulfate_free_metako_medium__b4a668be.yaml`; its MediaDive J1126 import is the same JCM formula after dilution by stock additions and should agree in order of magnitude.

## Additional Notes

Empty optional fields that are unrelated to the missing stock hierarchy were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the maintained normalized TOGO source and the stock-aware generation path.
