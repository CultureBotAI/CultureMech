# YAML Record Review: sporosalibacterium_medium__454959b3

- Repository: CultureMech
- Record: data/merge_yaml/merged/sporosalibacterium_medium__454959b3.yaml
- Started UTC: 2026-09-25T07:01:13Z
- Finished UTC: 2026-09-25T07:02:13Z
- Verdict: needs curation

## Target

Reviewed the generated record for TOGO Medium M728, `Sporosalibacterium Medium`, imported from JCM medium 706 and assigned `CultureMech:010136`.

## Validation

- LinkML validation: Passed; no issues found.
- Strict validation: Passed; the TSV contained only the header, with 0 error rows.
- LinkML reference validation: Passed; 0 reference checks were run and all passed.
- LinkML term validation: Passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The record is a single-source TOGO import for `TOGO:M728`; TOGO identifies this as `Sporosalibacterium Medium`, original medium `JCM_M706`, with source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=706`.

The live JCM page still renders medium 706 as `SPOROSALIBACTERIUM MEDIUM`. MediaDive's JCM mirror also resolves `J706` to `SPOROSALIBACTERIUM MEDIUM`, source `JCM`, pH 7.2, and the same JCM GRMD 706 link.

## Evidence

JCM specifies the base medium as 0.3 g KH2PO4, 0.3 g K2HPO4, 1.0 g NH4Cl, 40.0 g NaCl, 0.2 g CaCl2 x 2 H2O, 2.0 g yeast extract, 2.0 g Trypticase peptone, 3.6 g glucose, 1 ml trace element solution from JCM Medium 439, 1 mg resazurin, and 940 ml distilled water. The generated record carries those main-solution names, but it stores `Resazurin` as `1` `G_PER_L` rather than a milligram-scale row and leaves the 1 ml trace-element stock as an empty solution placeholder.

JCM then instructs curators to adjust the base to pH 7.2, distribute 4.7 ml portions under N2-CO2 4:1, autoclave, and add per 4.7 ml: 0.1 ml 15 percent MgCl2 x 6 H2O, 0.2 ml 5 percent NaHCO3, 0.05 ml 5 percent L-cysteine HCl x H2O, and 0.04 ml 5 percent Na2S x 9 H2O. The generated record stores those source aliquot volumes as `G_PER_L` solution concentrations and does not preserve any preparation steps.

## Completeness

The generated record is incomplete because the JCM 439 trace-element solution remains an empty `solutions` placeholder. MediaDive J706 resolves that stock as solution 4186 with FeSO4 x 7 H2O, H3BO3, MnCl2 x 4 H2O, CoCl2 x 6 H2O, NiCl2 x 6 H2O, CuCl2 x 2 H2O, ZnSO4 x 7 H2O, and Na2MoO4 x 2 H2O.

The record is also missing the source pH 7.2 and the anaerobic preparation procedure.

## Findings

- High: Several source units were imported at the wrong scale. `Resazurin` is 1 mg in the JCM table but 1 g/l in the target, and the 0.2 ml NaHCO3, 0.1 ml MgCl2, 0.05 ml L-cysteine, and 0.04 ml Na2S stock aliquots were migrated to empty `solutions` rows with `G_PER_L` units.
- High: The JCM 439 trace-element stock is unresolved. The target has `composition: []` for `Trace element solution (see Medium [M439])` even though MediaDive J706 exposes the stock composition as solution 4186.
- Medium: The generated record has no preparation steps, dropping the pH 7.2 adjustment, N2-CO2 distribution into Hungate tubes, autoclaving, final stock-addition instructions, and distinct sterilization/storage requirements for NaHCO3 and the other stock solutions.
- Low: The TOGO import carries `Sol. 1` and `Sol. 2` as 4.7 g/l and 0.39 g/l ingredient rows, even though those are section labels and per-vessel aliquots in the TOGO structure, not ingredients.

## Recommended Edits

- Fix the TOGO/JCM import path so source mg amounts remain milligram-scale and per-volume ml additions remain solution aliquots until converted from their percent-stock solute concentrations.
- Expand the JCM 439 trace-element stock from MediaDive solution 4186 or an equivalent JCM source into the normalized record.
- Add JCM's pH 7.2 and anaerobic preparation instructions to `data/normalized_yaml/bacterial/TOGO_M728_Sporosalibacterium_Medium.yaml`, then regenerate `data/merge_yaml/merged/sporosalibacterium_medium__454959b3.yaml`.

## Follow-up Checks

- After regeneration, confirm that `Sol. 1` and `Sol. 2` no longer appear as pseudo-ingredients and that the final MgCl2, NaHCO3, cysteine, and sulfide solute amounts are derived from the per-4.7-ml stock additions.

## Additional Notes

None found
