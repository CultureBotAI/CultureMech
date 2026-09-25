# YAML Record Review: freshwater_medium_with_rhamnose

- Repository: CultureMech
- Record: data/merge_yaml/merged/freshwater_medium_with_rhamnose__21889617.yaml
- Started UTC: 2026-09-23T04:39:21Z
- Finished UTC: 2026-09-23T04:40:48Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:002468` / `freshwater_medium_with_rhamnose`, the direct MediaDive/JCM Medium J1304 import.
- Compared it with maintained source `data/normalized_yaml/bacterial/freshwater_medium_with_rhamnose.yaml`.
- Cross-checked the MediaDive REST payload for JCM J1304 and the live JCM GRMD=1304 page.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass with 0 error rows.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- `mediadive.medium:J1304` correctly identifies JCM Medium 1304, FRESHWATER MEDIUM WITH RHAMNOSE.
- Exact ignored-inclusive lookup for `mediadive.medium:J1304`, `CultureMech:002468`, and `freshwater_medium_with_rhamnose__21889617` covered normalized and generated YAML; it found this single maintained JCM J1304 owner and the suffixed generated file.
- The generated record's base medium identity is correct, but its ingredients do not preserve Modified trace element mixture, JCM 556 Vitamin solution, JCM 431 Selenite-tungstate solution, or sterile addition boundaries.
- NiCl2 x 6 H2O is grounded only to nickel dichloride, losing the source hexahydrate form.

## Evidence

- JCM 1304 defines a 955 ml base with 1 g NaCl, 0.4 g MgCl2 x 6 H2O, 0.15 g CaCl2 x 2 H2O, 0.25 g NH4Cl, 0.2 g KH2PO4, 0.5 g KCl, and 0.5 mg Resazurin before post-autoclave stock additions.
- MediaDive represents the main solution as 1008 ml after adding 30 ml 8% NaHCO3 solution, 1 ml Modified trace element mixture, 1 ml JCM 556 Vitamin solution, 0.5 ml JCM 431 Selenite-tungstate solution, 10 ml 0.5 M L-Rhamnose solution, 5 ml 10% Yeast extract solution, and 5 ml 5% Na2S x 9 H2O solution. The generated base rows use MediaDive's 1008 ml `g_l` projections, so 1 g NaCl becomes 0.992063 g/L and 0.5 mg Resazurin becomes 0.000496032 g/L.
- The generated NaHCO3, L-Rhamnose, Yeast extract, and Na2S x 9 H2O rows convert the source milliliter stock additions into 30, 10, 5, and 5 g/L final-medium rows.
- Modified trace element mixture rows are flattened into the final ingredient list at stock concentrations: for example, EDTA x Na2 at 5.2 g/L and FeCl2 x 4 H2O at 1 g/L.
- JCM 556 Vitamin solution and JCM 431 Selenite-tungstate solution are likewise flattened into final-medium ingredients at stock concentrations while losing their 1 ml/L and 0.5 ml/L addition volumes.
- JCM marks several anaerobic stocks as filter-sterilized and the sodium sulfide stock as autoclaved and stored under N2; the generated record only carries that handling as preparation prose, not on the corresponding stock rows.

## Completeness

- Modified trace element mixture, JCM 556 Vitamin solution, and JCM 431 Selenite-tungstate solution are not structurally represented.
- The 30 ml/L NaHCO3, 1 ml/L Vitamin solution, 0.5 ml/L Selenite-tungstate solution, 10 ml/L L-Rhamnose, 5 ml/L Yeast extract, and 5 ml/L Na2S x 9 H2O stock additions are not modeled as stock additions.
- Filter-sterile versus autoclaved stock handling is incomplete.
- The generated final `ph_value: 6.5` follows the MediaDive summary but conflicts with JCM's final-medium instructions to adjust and readjust pH to 7.2-7.4; the 6.5 value appears to belong only to the Modified trace element mixture.

## Findings

- Major: source base ingredients were normalized over MediaDive's 1008 ml post-addition volume instead of preserving the JCM 1304 base amounts before additive stocks.
- Major: milliliter additions of NaHCO3, L-Rhamnose, Yeast extract, and Na2S x 9 H2O stocks were imported as gram-per-liter final ingredient rows.
- Major: Modified trace element mixture, JCM 556 Vitamin solution, and JCM 431 Selenite-tungstate solution are flattened into top-level stock-strength ingredients.
- Major: filter-sterilized and separately autoclaved anaerobic stock boundaries from JCM 1304 are not represented structurally.
- Major: the generated record reports final pH 6.5 even though the JCM final medium is adjusted to pH 7.2-7.4.
- Minor: the NiCl2 x 6 H2O source form is grounded to an anhydrous nickel dichloride term.

## Recommended Edits

- Rebuild the maintained JCM 1304 record with the main freshwater base, Modified trace element mixture, JCM 556 Vitamin solution, and JCM 431 Selenite-tungstate solution as explicit solution structures.
- Restore the main-solution ingredients to their JCM source amounts before the 1008 ml post-addition normalization.
- Represent NaHCO3, Vitamin solution, Selenite-tungstate solution, L-Rhamnose, Yeast extract, and Na2S x 9 H2O as stock additions with source milliliter volumes and the correct sterilization status.
- Keep trace-element, vitamin, and selenite-tungstate stock ingredients inside their stock recipes instead of exporting them as final-medium top-level rows.
- Resolve the final pH discrepancy against the JCM source and keep the Modified trace element mixture pH 6.5 separate from the final pH 7.2-7.4.
- Regenerate `data/merge_yaml/merged/freshwater_medium_with_rhamnose__21889617.yaml` after normalized/import curation.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated JCM J1304 YAML.
- Confirm the main freshwater base keeps the 955 ml source base context and its salt rows are not divided over 1008 ml.
- Confirm stock-only trace-element, vitamin, and selenite-tungstate ingredients do not appear as top-level final-medium rows.
- Confirm each anaerobic stock addition carries its source volume and sterilization status.
- Confirm pH 6.5 is scoped only to Modified trace element mixture preparation.

## Additional Notes

- The generated file is derived data and is a one-source merge. The same JCM J1304 flattening is present in normalized YAML.
