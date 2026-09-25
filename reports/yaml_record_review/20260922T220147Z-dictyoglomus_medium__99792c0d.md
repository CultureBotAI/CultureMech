# YAML Record Review: dictyoglomus_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/dictyoglomus_medium__99792c0d.yaml`
- Started UTC: 2026-09-22T22:00:45Z
- Finished UTC: 2026-09-22T22:01:47Z
- Verdict: needs curation

## Target

`CultureMech:009137` represents TOGO Medium M2569, `Dictyoglomus medium`, imported from an ATCC medium PDF. The generated record is a single-source merge from `data/normalized_yaml/bacterial/TOGO_M2569_Dictyoglomus_medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

A gitignore-independent `find` over `data/` found this TOGO M2569 record and a separate `DICTYOGLOMUS_MEDIUM` KOMODO/DSMZ 388 generated record with its KOMODO and DSMZ normalized sources. TOGO M2569 and DSMZ 388 should stay distinct: both normalize to `dictyoglomus_medium`, but their stock sets, vitamin compositions, and final ingredient quantities differ.

## Evidence

- The live TOGO M2569 API lists a main Dictyoglomus medium containing 980 ml distilled water, yeast extract, salts, 2 mg resazurin, 10 ml Wolfe's Vitamin Solution, 2 g Polypeptone Peptone, 1 g L-Cysteine HCl, 10 ml Trace Metals, and 100% nitrogen gas.
- The same API defines Trace Metals as a separate stock with 1 L distilled water, 240 mg Na2MoO4 x 2H2O, 200 mg MnCl2 x 4H2O, 290 mg CoCl2 x 6H2O, 280 mg ZnSO4 x 7H2O, and 17 mg Na2SeO3.
- TOGO records pH 7.2 and comments instructing final pH adjustment if necessary, filter sterilization and aseptic addition of the vitamin solution, and anaerobic preparation and dispensing under a 100% nitrogen atmosphere.

## Completeness

The record is incomplete because the Trace Metals stock was flattened into top-level ingredients, the Wolfe's Vitamin Solution addition became an empty unknown solution, and the source comments were dropped.

## Findings

- `Trace Metals` is stored as a top-level `10 G_PER_L` ingredient instead of a 10 ml stock addition.
- `Wolfe's Vitamin Solution` is stored as an empty `Unknown solution` with `10 G_PER_L`; the source adds 10 ml of the stock.
- The Trace Metals child salts were promoted to top-level ingredients and their milligram amounts were stored as `G_PER_L` values, for example `240 mg` Na2MoO4 x 2H2O became `240 G_PER_L`.
- The main 980 ml water row and Trace Metals 1 L water row were merged into `981.0 G_PER_L`.
- The 2 mg resazurin row was stored as `2 G_PER_L`, a 1000-fold unit error.
- The generated record does not carry the source pH 7.2.
- The filter-sterilized vitamin addition and 100% nitrogen Hungate preparation comments are absent.

## Recommended Edits

- Restore `Trace Metals` as a stock added at 10 ml to the main recipe and nest its five metal salts plus 1 L water under that stock.
- Represent `Wolfe's Vitamin Solution` as a 10 ml stock addition rather than an empty solution with a gram-per-liter concentration.
- Convert all milligram rows, including resazurin and Trace Metals children, to gram-per-liter values only in their correct source scopes.
- Keep the main 980 ml water row separate from the 1 L Trace Metals stock water row.
- Preserve pH 7.2, the vitamin filter-sterilization instruction, and the anaerobic 100% nitrogen Hungate preparation.
- Keep this TOGO/ATCC record separate from the KOMODO/DSMZ 388 `DICTYOGLOMUS_MEDIUM` formulation.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that no Trace Metals child remains as a top-level ingredient.
- Verify that no source milligram or milliliter amount remains as an unconverted `G_PER_L` concentration.
- Verify that the TOGO M2569 and DSMZ 388 Dictyoglomus records still emit as distinct generated variants.

## Additional Notes

None found.
