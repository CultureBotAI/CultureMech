# YAML Record Review: desulfuromonas_thiophila_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfuromonas_thiophila_medium__07832454.yaml`
- Started UTC: 2026-09-22T21:44:07Z
- Finished UTC: 2026-09-22T21:46:01Z
- Verdict: needs curation

## Target

`CultureMech:001785` represents MediaDive DSMZ Medium 647, `DESULFUROMONAS THIOPHILA MEDIUM`, merged with two KOMODO 647 aliases. The generated record merged `data/normalized_yaml/bacterial/desulfuromonas_acetexigenes_medium.yaml`, `data/normalized_yaml/bacterial/desulfuromonas_thiophila_medium.yaml`, and `data/normalized_yaml/bacterial/for_dsm_8988.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

DSMZ 647 is a defined 1003 ml recipe with three 1 ml nested stock additions. A gitignore-independent, case-insensitive `find` over `data/` found this DSMZ 647/KOMODO merge and a distinct DSMZ 647a `DESULFUROMONAS_THIOPHILA_MEDIUM` generated record; DSMZ 647a adds NaCl and MgCl2, changes the sterilization of sulfur, and should remain a separate variant rather than merge with DSMZ 647.

## Evidence

- MediaDive DSMZ 647 defines `Main sol. 647` as a 1003 ml recipe containing the base salts, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, 0.5 ml 0.1% resazurin, powdered sulfur, carbonate, pyruvate, 1 ml Seven vitamins solution, sulfide, and 1000 ml distilled water.
- Trace element solution SL-10 is a 1000 ml stock with HCl, FeCl2, ZnCl2, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, Na2MoO4, and 990 ml water.
- Selenite-tungstate solution is a 1000 ml stock with NaOH, Na2SeO3, Na2WO4, and 1000 ml water.
- Seven vitamins solution is a 1000 ml stock with vitamin B12, p-aminobenzoic acid, D-(+)-biotin, nicotinic acid, calcium pantothenate, pyridoxine hydrochloride, thiamine-HCl x 2 H2O, and 1000 ml water.
- The current normalized DSMZ 647 source has September 2026 repair history and `variant_children`; the generated record was built in August 2026 and still carries the older flat source-duplicate merge.

## Completeness

The generated record is incomplete because it has no `solutions` block. The normalized source has started nesting SL-10 and Seven vitamins, but that repair is partial and absent from the generated artifact.

## Findings

- Trace element solution SL-10, Selenite-tungstate solution, and Seven vitamins solution were flattened into top-level final-medium ingredients in the generated YAML.
- The normalized source now nests SL-10 only partially: FeCl2 is nested, but the HCl, ZnCl2, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, Na2MoO4, and water rows are still top-level or missing from the stock.
- The normalized source now nests Seven vitamins only partially: vitamin B12, nicotinic acid, pyridoxine hydrochloride, and thiamine are nested, while p-aminobenzoic acid, D-(+)-biotin, calcium pantothenate, and the stock water row are still top-level or missing.
- Selenite-tungstate solution was not nested at all; NaOH, Na2SeO3, and Na2WO4 remain top-level stock-strength rows.
- The 1000 ml main water and three stock water rows are missing from generated YAML.
- `Sulfur` is grounded to `CHEBI:26833` / sulfur atom even though the MediaDive source specifies powdered sulfur.

## Recommended Edits

- Finish the normalized DSMZ 647 repair by nesting all children of Trace element solution SL-10, Selenite-tungstate solution, and Seven vitamins solution, including their water rows.
- Keep the 1 ml stock additions in the 1003 ml main recipe rather than promoting stock contents to final-medium ingredients.
- Regenerate the merged record so it picks up the repaired September 2026 parent/variant relationships and no longer shows the stale August 2026 `parent_media` topology.
- Re-ground powdered `Sulfur` to an elemental sulfur or sulfur powder term consistent with the MediaDive source.
- Keep DSMZ 647, DSMZ 647a, and the nearby `Desulfuromonas thiophila` TOGO/KOMODO imports distinct unless formulas match exactly.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that all nine SL-10 solutes plus SL-10 water are nested under Trace element solution SL-10.
- Verify that all seven Seven vitamins solutes plus the vitamin-stock water row are nested under Seven vitamins solution.
- Verify that Selenite-tungstate solution is nested under the main medium as a 1 ml stock addition.

## Additional Notes

None found.
