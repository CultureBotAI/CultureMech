# YAML Record Review: diazotrophic_medium_rba

- Repository: CultureMech
- Record: `data/merge_yaml/merged/diazotrophic_medium_rba.yaml`
- Started UTC: 2026-09-22T21:58:52Z
- Finished UTC: 2026-09-22T21:59:46Z
- Verdict: needs curation

## Target

`CultureMech:005288` represents KOMODO Medium 441 merged with the DSMZ Medium 441 MediaDive import for `DIAZOTROPHIC MEDIUM (RBA)`. The generated record merged `data/normalized_yaml/bacterial/KOMODO_441_DIAZOTROPHIC_medium_RBA.yaml` and `data/normalized_yaml/bacterial/diazotrophic_medium_rba.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

A gitignore-independent `find` over `data/` found this exact generated RBA record and its two normalized KOMODO/DSMZ sources. The same search also found taxon-named Bacillus alkalidiazotrophicus and Acetobacter diazotrophicus media, which are separate records and should not be merged with DSMZ 441.

## Evidence

- Live MediaDive DSMZ 441 defines the 1008 ml main medium as 953 ml Solution A, 50 ml Solution B, and 5 ml Standard vitamin solution.
- Solution A is a 953 ml stock with phosphate salts, NaCl, CaCl2, MgSO4, Na2MoO4, NaVO3, MnSO4, FeSO4, yeast extract, 3 ml Trace element solution SL-6, 950 ml water, and optional 15 g agar.
- Solution B is a 50 ml stock containing disodium succinate, DL-malate, Na-pyruvate, D-mannitol, D-glucose, and 50 ml water.
- Trace element solution SL-6 is a 1000 ml stock with ZnSO4, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, Na2MoO4, and water.
- Standard vitamin solution is a 100 ml stock with riboflavin, thiamine-HCl, nicotinic acid, pyridoxine hydrochloride, calcium pantothenate, biotin, folic acid, vitamin B12, and water.
- DSMZ sterilizes Solution A separately, filter-sterilizes Solution B and the standard vitamin solution, and mixes the components aseptically after Solution A cools to 50 C.

## Completeness

The record is incomplete because every DSMZ 441 sub-solution was flattened into top-level ingredients in the generated YAML. Later normalized-source repairs partially nest the Standard vitamin solution, but the generated record predates those repairs and the normalized repairs still leave most stocks flattened.

## Findings

- The generated record has no `solutions` block for 953 ml Solution A, 50 ml Solution B, 3 ml Trace element solution SL-6, or 5 ml Standard vitamin solution.
- Trace element solution SL-6 child rows are represented as top-level ingredients at stock strength.
- Solution B carbon-source rows are represented as top-level `G_PER_L` stock concentrations instead of a 50 ml filtered stock.
- All Standard vitamin solution rows remain top-level in the generated record; the normalized August repair only nests four of the eight vitamin ingredients.
- `Na2MoO4 x 2 H2O` from Solution A and Trace element solution SL-6 was merged into `0.03524659 G_PER_L` across solution boundaries.
- The 950 ml Solution A water, 50 ml Solution B water, 1000 ml SL-6 water, and 100 ml vitamin-stock water rows are absent.
- Solution A, Solution B, and Standard vitamin solution sterilization and mixing instructions are absent from generated YAML.

## Recommended Edits

- Restore DSMZ 441 as a 1008 ml main recipe assembled from 953 ml Solution A, 50 ml Solution B, and 5 ml Standard vitamin solution.
- Nest Trace element solution SL-6 under Solution A as a 3 ml addition, with all seven SL-6 salts plus water scoped to that stock.
- Nest all six Solution B carbon sources and water under Solution B and preserve its filter-sterilization scope.
- Nest all eight vitamin compounds and water under Standard vitamin solution, not only the four ingredients moved by the August repair.
- Keep Solution A molybdate separate from SL-6 molybdate.
- Preserve the Solution A autoclaving, 50 C cooling, aseptic mixing, and microaerophilic nitrogen-fixing notes as preparation steps.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that no SL-6, Solution B, or Standard vitamin child ingredient remains as a top-level ingredient.
- Verify that no duplicate merge crosses a solution boundary.
- Verify that all four DSMZ water rows are either represented in their source scopes or intentionally omitted according to the water-handling convention.

## Additional Notes

None found.
