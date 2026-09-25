# YAML Record Review: methanohalophilus_mg_nacl_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanohalophilus_mg_nacl_medium.yaml
- Started UTC: 2026-09-24T04:05:43Z
- Finished UTC: 2026-09-24T04:09:54Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:000270` / `methanohalophilus_mg_nacl_medium`, a four-way merge of MediaDive/DSMZ and KOMODO imports:

- `data/normalized_yaml/archaea/methanohalophilus_mg_nacl_medium.yaml`
- `data/normalized_yaml/archaea/methanohalophilus_mg_medium.yaml`
- `data/normalized_yaml/bacterial/for_dsm_5700_dsm_5701_dsm_5702_dsm_5703_and_dsm_5814.yaml`
- `data/normalized_yaml/bacterial/mg_medium.yaml`
- `merged_from`: `methanohalophilus_mg_medium`, `methanohalophilus_mg_nacl_medium`, `for_dsm_5700_dsm_5701_dsm_5702_dsm_5703_and_dsm_5814`, `mg_medium`
- `merge_fingerprint`: `55372dd39c687df7401831d79dc671d0ba61186299abb0bbbc4ad24ab9426fb5`

The exact normalized paths above were found with an ignored-file-inclusive `rg --files --no-ignore --hidden` search.

## Validation

- LinkML open validation: Passed; printed `No issues found`.
- Strict validation: Passed with 0 error rows in `/private/tmp/methanohalophilus_mg_nacl_medium.strict.tsv`.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The generated record carries the `DSMZ Medium 525a` / `METHANOHALOPHILUS (MG+NaCl) MEDIUM` identity, but its NaCl value is from DSMZ `525`, not from DSMZ `525a`. The normalized `methanohalophilus_mg_nacl_medium`, `for_dsm_5700_dsm_5701_dsm_5702_dsm_5703_and_dsm_5814`, and `mg_medium` owners each have `149.368 G_PER_L` NaCl after an already-wrong duplicate sum; the normalized `methanohalophilus_mg_medium` owner and this generated canonical record have `99.912 G_PER_L`. The merge grouped non-identical DSMZ `525` and `525a` formulas while leaving a `525a` media term on a `525` concentration profile.

## Evidence

- DSMZ/MediaDive `525a` and the current DSMZ 525a PDF list 0.34 g KCl, 2.75 g `MgCl2 x 6 H2O`, 3.45 g `MgSO4 x 7 H2O`, 0.25 g `NH4Cl`, 0.14 g each of `K2HPO4 x 3 H2O` and `CaCl2 x 2 H2O`, 150 g NaCl, 10 ml Modified Wolin's mineral solution, 1 g Na-acetate, 0.5 ml 0.1% sodium resazurin, 4 g `NaHCO3`, 0.5 g `Na2CO3`, 5 g trimethylamine-HCl, 1 ml Wolin's vitamin solution (10x), 0.5 g `L-Cysteine HCl x H2O`, 0.5 g `Na2S x 9 H2O`, and 1000 ml distilled water.
- DSMZ/MediaDive `525` has the same formula except that the main NaCl amount is 100 g, not 150 g.
- Modified Wolin's mineral solution is a separate 1 L stock added at 10 ml/L and contains nitrilotriacetic acid, `MgSO4 x 7 H2O`, `MnSO4 x H2O`, NaCl, `FeSO4 x 7 H2O`, `CoSO4 x 7 H2O`, `CaCl2 x 2 H2O`, `ZnSO4 x 7 H2O`, `CuSO4 x 5 H2O`, `AlK(SO4)2 x 12 H2O`, `H3BO3`, `Na2MoO4 x 2 H2O`, `NiCl2 x 6 H2O`, `Na2SeO3 x 5 H2O`, `Na2WO4 x 2 H2O`, and distilled water.
- Wolin's vitamin solution (10x) is a separate 1 L stock added at 1 ml/L and contains biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium D-pantothenate, vitamin B12, p-aminobenzoic acid, DL-alpha-lipoic acid, and distilled water.
- DSMZ instructs sparging the base with 80% `N2` / 20% `CO2` for 30 to 45 min, autoclaving under that gas, adding trimethylamine, vitamins, cysteine, and sulfide from sterile anoxic stocks under 100% `N2`, adding bicarbonate and carbonate from stocks under 80% `N2` / 20% `CO2`, and adjusting final pH to 6.9 to 7.0.

## Completeness

The MediaDive preparation text and pH range are retained, but the formula is not usable as a source-faithful recipe. The generated YAML has no `solutions` array, collapses two DSMZ NaCl strengths into one canonical medium, stores Modified Wolin and Wolin vitamin stock formulas as final-medium ingredients, and sums stock components with matching main-medium components.

## Findings

- The four-way merge grouped non-equivalent media. DSMZ `525a` has 150 g NaCl in the source main solution, while DSMZ `525` has 100 g; the generated record advertises `mediadive.medium:525a` but its `99.912 G_PER_L` NaCl row comes from `525` plus a wrongly summed 1 g/L NaCl from the Modified Wolin stock.
- Three duplicate ingredient rows were summed across formula scopes. `MgSO4 x 7 H2O` combines the 3.41246 g/L main-medium value with the 3 g/L stock concentration from Modified Wolin; `CaCl2 x 2 H2O` combines 0.138477 and 0.1; and NaCl combines a main-medium value with a 1 g/L stock value.
- Modified Wolin's mineral solution is flattened at stock strength. Ingredients such as 1.5 g/L nitrilotriacetic acid, 3 g/L magnesium sulfate, 0.5 g/L manganese sulfate, and 0.0003 g/L sodium selenite are the contents of a 1 L stock added at 10 ml/L, not direct final-medium concentrations.
- Wolin's vitamin solution (10x) is also flattened at stock strength. The generated biotin, folic acid, pyridoxine, thiamine, riboflavin, nicotinic acid, calcium pantothenate, B12, p-aminobenzoic acid, and lipoic acid values are stock concentrations despite the source adding only 1 ml/L.
- Source stock boundaries and addition volumes are absent. The generated record cannot express "10 ml Modified Wolin's mineral solution" or "1 ml Wolin's vitamin solution (10x)" because both stock invocations were deleted from the recipe.
- The canonical record retains `categories: [archaea, bacterial]` only because two KOMODO aliases were categorized as bacterial; the source DSMZ media are archaeal methanogen media.

## Recommended Edits

- Split DSMZ `525` from DSMZ `525a` unless curation deliberately models them as variants with distinct NaCl levels under one parent recipe.
- Restore `Modified Wolin's mineral solution` and `Wolin's vitamin solution (10x)` as structured stock solutions or source-preserving solution references in the normalized MediaDive owners.
- Remove final-medium rows that were copied from stock recipes, or recompute them from the 10 ml/L and 1 ml/L stock addition volumes while preserving the stock hierarchy.
- Prevent duplicate cleanup from summing main-medium NaCl, `MgSO4 x 7 H2O`, and `CaCl2 x 2 H2O` with the same chemicals inside Modified Wolin's mineral solution.
- Ensure the regenerated canonical medium term and primary NaCl concentration agree: `525` should carry 100 g source NaCl, and `525a` should carry 150 g source NaCl.
- Regenerate `data/merge_yaml/merged/methanohalophilus_mg_nacl_medium.yaml` from curated normalized owners after the merge boundary is fixed.

## Follow-up Checks

- Re-run open, strict, reference, and term validation after regeneration.
- Compare regenerated DSMZ `525` and `525a` records against MediaDive REST `/rest/medium/525` and `/rest/medium/525a`.
- Confirm that KOMODO aliases do not force `bacterial` onto an archaeal canonical record after the merge is split or annotated.

## Additional Notes

None found
