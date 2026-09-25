# YAML Record Review: spirochaetea_ns_medium__f412ca67

- Repository: CultureMech
- Record: data/merge_yaml/merged/spirochaetea_ns_medium__f412ca67.yaml
- Started UTC: 2026-09-25T06:27:04Z
- Finished UTC: 2026-09-25T06:29:32Z
- Verdict: needs curation

## Target

Reviewed the generated record for JCM Medium J1301 / SPIROCHAETEA NS MEDIUM, produced from the `mediadive.medium:J1301` import and assigned `CultureMech:002465`.

## Validation

- LinkML validation: Passed; no issues found.
- Strict validation: Passed; the TSV contained only the header, with 0 error rows.
- LinkML reference validation: Passed; 0 reference checks were run and all passed.
- LinkML term validation: Passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The record identity is grounded to `mediadive.medium:J1301`, label `SPIROCHAETEA NS MEDIUM`, with source `JCM` and the archived JCM identifier `J1301`. The direct JCM URL currently returns a `Nothing found` page for `GRMD=1301`, but both the MediaDive `J1301` record and the TOGO `M1398` import retain the same JCM medium identity, and TOGO explicitly records original source `JCM_M1301`.

The physical state, pH 8.0, and defined composition type match the source-level description in MediaDive `J1301`.

## Evidence

The MediaDive `J1301` payload lists `Main sol. J1301` with 1 g `NaNO3`, 0.2 g `K2HPO4`, 0.25 g `NH4Cl`, 0.4 g `MgSO4 x 7 H2O`, 0.5 g `FeSO4 x 7 H2O`, 0.11 g `CaCl2 x 2 H2O`, 1 ml `Trace mineral solution`, 1 mg `Resazurin`, 1000 ml distilled water, 20 ml `Trace vitamins`, 10 ml 1.0 M `Maltose`, and 5 ml 5 percent `Na2S x 9 H2O`.

The same payload defines `Trace mineral solution` as 1000 ml `Trace minerals`, 0.03 g `NiCl2 x 6 H2O`, 0.3 mg `Na2SeO3 x 5 H2O`, and 0.4 mg `Na2WO4 x 2 H2O`. It defines `Trace vitamins` as a 1 L stock containing the listed vitamin masses. TOGO `M1398` mirrors the JCM medium with 1 ml trace mineral solution from `M1153`, 5 ml of 5 percent sulfide, 10 ml of 1.0 M maltose, and 20 ml trace vitamins from `M190`.

## Completeness

The generated record retains the top-level medium identity and the JCM anaerobic preparation note. It does not retain the source recipe as a hierarchy of a main solution plus stock additions, and its final ingredient list omits distilled water while promoting several stock contents into apparent final-medium `G_PER_L` ingredient rows.

## Findings

- High: Stock additions are flattened into parent ingredient rows. The source adds 1 ml of trace mineral solution and 20 ml of trace vitamins per liter, but the generated record lists `NiCl2 x 6 H2O`, `Na2SeO3 x 5 H2O`, `Na2WO4 x 2 H2O`, `Biotin`, `Folic acid`, `Pyridoxine hydrochloride`, `Thiamine HCl`, `Riboflavin`, `Nicotinic acid`, `Calcium pantothenate`, `Vitamin B12`, `p-Aminobenzoic acid`, and `Lipoic acid` at their stock concentrations as direct final-medium `G_PER_L` rows.
- High: The maltose and sulfide additions lose their addition semantics. The source calls for 10 ml of 1.0 M maltose and 5 ml of 5 percent `Na2S x 9 H2O` per liter from sterile anaerobic stocks; the generated parent has `Maltose` at `10 G_PER_L` and `Na2S x 9 H2O` at `5 G_PER_L`, which are imported from addition volumes rather than mass concentrations.
- Medium: The trace-mineral hierarchy is incomplete. MediaDive `J1301` defines its `Trace mineral solution` as the JCM trace-minerals stock plus nickel, selenite, and tungstate, while TOGO points the same addition at `M1153`; the generated record keeps the nickel/selenite/tungstate stock rows but drops the referenced trace-minerals base.
- Medium: The main solution water row is lost. Source `J1301` includes 1000 ml distilled water in the main solution before the 36 ml of post-sterilization additions, but the generated record has no water row and no explicit final volume context.

## Recommended Edits

- Fix the `mediadive.medium:J1301` normalized import or merge expansion so `Trace mineral solution`, `Trace vitamins`, 1.0 M maltose, and 5 percent sulfide remain modeled as stock solutions or additions with per-liter volumes.
- Include the referenced trace-minerals stock inside the trace-mineral solution, resolving MediaDive `solution_id: 3804` or the TOGO `M1153`/`M142` cross-reference instead of keeping only the nickel, selenite, and tungstate rows.
- Restore the 1000 ml distilled-water row on the main solution and keep the generated per-liter scaling tied to the 1036 ml post-addition volume so source masses are not confused with stock volumes.
- Re-run the generated merge and targeted validators after editing the normalized YAML; do not hand-edit `data/merge_yaml/merged/spirochaetea_ns_medium__f412ca67.yaml`.

## Follow-up Checks

- Confirm whether the direct JCM `GRMD=1301` endpoint has moved or been removed; the current JCM URL returned `Nothing found`, so MediaDive and TOGO acted as the available JCM mirrors for this review.
- Recheck the CHEBI grounding for `NiCl2 x 6 H2O` after stock hierarchy is restored because the row currently uses a generic nickel dichloride label for a hexahydrate source name.

## Additional Notes

None found
