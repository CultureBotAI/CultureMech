# YAML Record Review: dehalobacter_restrictus_medium_tce__3ce89046

- Repository: CultureMech
- Record: `data/merge_yaml/merged/dehalobacter_restrictus_medium_tce__3ce89046.yaml`
- Started UTC: 2026-09-22T16:55:08Z
- Finished UTC: 2026-09-22T16:55:08Z
- Verdict: needs curation

## Target

Generated bacterial `dehalobacter_restrictus_medium_tce` record for MediaDive / DSMZ Medium 732.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to `mediadive.medium:732` / DSMZ Medium 732 and preserves `ph_value: 7.2`, which matches the current DSMZ PDF.

Most ingredient groundings are plausible, but nickel dichloride hexahydrate is still grounded to CHEBI:34887, whose label is nickel dichloride rather than a hexahydrate.

This generated file is stale relative to `data/normalized_yaml/bacterial/dehalobacter_restrictus_medium_tce.yaml`: an `apply_cocktail_nesting.py` entry from 2026-08-07 partially moved flattened stock-strength components into `Trace element solution`, `Seven vitamins solution`, and `Wolin's vitamin solution (10x)`, while the generated file was built one day earlier and has no `solutions` section.

## Evidence

DSMZ 732 is assembled from 870 ml Solution A, 100 ml Solution B, 10 ml Solution C, 1 ml Solution D, 2 ml Solution E, 10 ml Solution F, and 15 ml Solution G to a 1008 ml main recipe.

The generated record has no Solutions A-G. Instead, it promotes the `g_l` values from each MediaDive stock directly to top-level final-medium ingredients. This is wrong for every stock other than a 1 liter stock dosed at 1 liter per liter: for example, NaHCO3 is stored at the 37.3 g/L concentration of 100 ml Solution B, CaCl2 x 2 H2O is stored at the 11 g/L concentration of 10 ml Solution C, and Na2S x 9 H2O is stored at the 30 g/L concentration of 10 ml Solution F.

Solution G is a 15 ml two-liquid stock containing 13.5 ml hexadecane and 1.50 ml tetrachloroethene, added only after inoculation. The generated record stores those two volume amounts as `13.5 G_PER_L` and `1.5 G_PER_L` top-level concentrations.

The trace element solution and both vitamin stocks were also flattened. Shared vitamins were summed across distinct stocks, including pyridoxine hydrochloride as `0.4 G_PER_L` from 0.1 and 0.3, nicotinic acid as `0.25 G_PER_L` from 0.05 and 0.2, vitamin B12 as `0.101 G_PER_L` from 0.001 and 0.1, and p-aminobenzoic acid as `0.13 G_PER_L` from 0.05 and 0.08.

## Completeness

The stock assembly model is missing. The final medium should reference Solutions A-G and nested Trace, Wolin, and Seven vitamin stocks rather than a single flat list of stock-strength salts, vitamins, oil, and chlorinated solvent.

The three broad `preparation_steps` preserve useful DSMZ prose, but the stock-specific gas atmospheres, filtration/autoclave boundaries, and post-inoculation Solution G addition are not machine-structured enough to reconstruct the recipe sequence reliably.

`medium_type: COMPLEX` and `composition_type: UNDEFINED` are supported by the 0.10 g Bacto peptone in Solution A.

## Findings

- Needs curation: MediaDive stock-strength `g_l` values are imported as final-medium `G_PER_L` concentrations.
- Needs curation: Solutions A-G and Solution E's nested vitamin stocks are absent from generated output.
- Needs curation: hexadecane and tetrachloroethene volumes are encoded as grams per liter.
- Needs curation: vitamins shared by Wolin's vitamin solution and Seven vitamins solution were summed across stock boundaries.
- Needs curation: generated output is stale relative to the 2026-08-07 partial cocktail-nesting repair in normalized YAML.
- Minor: `NiCl2 x 6 H2O` is grounded to an anhydrous nickel dichloride label.

## Recommended Edits

- Regenerate this merged record from the updated normalized MediaDive source after reviewing the 2026-08-07 partial cocktail-nesting repair.
- Model Solutions A-G explicitly with 870/100/10/1/2/10/15 ml additions to the main recipe.
- Move all stock-strength salts, vitamins, hexadecane, and tetrachloroethene into the correct nested stock compositions.
- Recompute any flat final concentrations from stock amount and final 1008 ml volume only if the schema needs denormalized final values.
- Preserve the two vitamin stocks separately so pyridoxine, nicotinic acid, vitamin B12, and p-aminobenzoic acid are not summed across distinct stocks.
- Represent Solution G as an oil/TCE post-inoculation addition with ml amounts, not `G_PER_L`.
- Ground `NiCl2 x 6 H2O` to the hydrated nickel chloride term if an appropriate CHEBI class exists.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after curation.
- Confirm the generated record has a non-empty `solutions` section.
- Confirm NaHCO3, CaCl2 x 2 H2O, and Na2S x 9 H2O no longer retain the B/C/F stock concentrations as final-medium concentrations.
- Confirm the generated record reflects the 2026-08-07 normalized cocktail-nesting work or a superseding complete stock reconstruction.

## Additional Notes

DSMZ Medium 732 was checked against the current DSMZ PDF and the MediaDive REST medium 732 payload.
