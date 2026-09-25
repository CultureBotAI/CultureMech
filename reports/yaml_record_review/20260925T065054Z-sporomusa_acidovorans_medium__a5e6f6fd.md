# YAML Record Review: sporomusa_acidovorans_medium__a5e6f6fd

- Repository: CultureMech
- Record: data/merge_yaml/merged/sporomusa_acidovorans_medium__a5e6f6fd.yaml
- Started UTC: 2026-09-25T06:49:14Z
- Finished UTC: 2026-09-25T06:50:54Z
- Verdict: needs curation

## Target

Reviewed the generated record for TOGO Medium M1290, `Sporomusa Acidovorans Medium`, imported from JCM medium 1204 and assigned `CultureMech:007825`.

## Validation

- LinkML validation: Passed; no issues found.
- Strict validation: Passed; the TSV contained only the header, with 0 error rows.
- LinkML reference validation: Passed; 0 reference checks were run and all passed.
- LinkML term validation: Passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The record is a single-source TOGO import for `TOGO:M1290`; TOGO identifies this as `Sporomusa Acidovorans Medium`, original medium `JCM_M1204`, with source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1204`.

The live JCM page still renders medium 1204 as `SPOROMUSA ACIDOVORANS MEDIUM`. MediaDive's JCM mirror also resolves `J1204` to `SPOROMUSA ACIDOVORANS MEDIUM`, source `JCM`, and the same JCM GRMD 1204 link.

## Evidence

The generated target preserves the direct TOGO Solution A and Solution B ingredient names, the TOGO gas rows for N2 and CO2, and the JCM cross-reference placeholders for FeCl2 solution, trace element solution, Se/W solution, and trace vitamins. It does not expand the referenced stock recipes and does not preserve JCM's autoclaving, mixing, filter-sterilized addition, anaerobic N2-CO2 dispensing, per-liter reducing-stock addition, or final pH-adjustment instructions as preparation steps.

JCM lists `Resazurin` as 0.5 mg in Solution A. The target records `Resazurin` as `0.5` `G_PER_L`, so the milligram amount was promoted to a gram-per-liter concentration. JCM also lists 2 ml of 0.1 percent FeSO4 x 7 H2O solution, 50 ml of 8 percent NaHCO3 solution, 10 ml of 40 percent D-fructose solution, 6 ml of 5 percent L-cysteine HCl x H2O solution, and 6 ml of 5 percent Na2S x 9 H2O solution; the target carries those milliliter amounts as `G_PER_L` solution concentrations with empty compositions.

## Completeness

The generated record is incomplete because every external stock reference remains an empty `solutions` placeholder. MediaDive J1204 expands the same JCM recipe into solution 3846 for FeCl2, solution 3847 for trace elements, solution 4034 for Se/W, and solution 3861 for trace vitamins, each with a concrete stock composition.

TOGO reports the medium pH as 6.5-7.0 and the JCM page instructs final adjustment to 6.5-7.0 if necessary, but the generated target has no `ph_value`.

## Findings

- High: Milligram and milliliter source amounts were stored as `G_PER_L` concentrations. `Resazurin` is 0.5 mg in JCM but 0.5 g/l in the target, and the FeSO4, NaHCO3, D-fructose, Na2S, and L-cysteine stock additions use their ml addition volumes as fake gram-per-liter concentrations.
- High: Cross-referenced stock media are unresolved. The FeCl2, trace element, Se/W, and trace-vitamin rows all have empty `composition: []` arrays even though MediaDive J1204 exposes concrete recipes for those stock solutions.
- Medium: The generated record has no preparation steps, dropping the source's N2 autoclaving, post-autoclave combination of Solutions A and B, filter-sterilized additions, N2-CO2 4:1 dispensing gas, per-liter reducing-stock additions, and final pH adjustment to 6.5-7.0.
- Low: The source pH range 6.5-7.0 is not represented in the generated record.

## Recommended Edits

- Fix the TOGO/JCM import path for this record so source mg amounts remain milligram-scale, source ml additions are represented as solution aliquots rather than `G_PER_L`, and percentage stocks are converted only after the stock solute and final volume are known.
- Expand or explicitly link the FeCl2, trace element, Se/W, and trace-vitamin stock recipes from their referenced JCM/MediaDive definitions instead of leaving empty `composition` arrays.
- Add the JCM preparation procedure and the pH 6.5-7.0 adjustment from the source to `data/normalized_yaml/bacterial/TOGO_M1290_Sporomusa_Acidovorans_Medium.yaml`, then regenerate the merged output.

## Follow-up Checks

- After stock expansion, confirm that `Nitrogen gas` and `N2` do not remain as separate duplicate dinitrogen rows unless the model intentionally distinguishes the headspace gas stream from the N2 autoclaving atmosphere.

## Additional Notes

None found
