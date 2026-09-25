# YAML Record Review: desulfuromonas_medium_tce

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfuromonas_medium_tce.yaml`
- Started UTC: 2026-09-22T21:42:23Z
- Finished UTC: 2026-09-22T21:44:06Z
- Verdict: needs curation

## Target

`CultureMech:001868` represents MediaDive DSMZ Medium 732a, `DESULFUROMONAS MEDIUM (TCE)`, merged with three KOMODO aliases for the DSMZ 732-series TCE formulation. The generated record merged `data/normalized_yaml/bacterial/dehalobacter_restrictus_medium.yaml`, `data/normalized_yaml/bacterial/desulfuromonas_medium_tce.yaml`, `data/normalized_yaml/bacterial/for_dsm_13726.yaml`, and `data/normalized_yaml/bacterial/for_dsm_15941.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

DSMZ 732a is a structured seven-solution recipe for TCE-amended medium. A gitignore-independent, case-insensitive `find` over `data/` found this DSMZ 732a/KOMODO merge, a distinct TOGO M2745 `Dehalobacter Restrictus Medium TCE` record, and other TCE-named generated records that should stay separate unless source formulas match.

## Evidence

- MediaDive DSMZ 732a defines `Main sol. 732a` as a 1008 ml recipe assembled from 870 ml Solution A, 100 ml Solution B, 10 ml Solution C, 1 ml Solution D, 2 ml Solution E, 10 ml Solution F, and 15 ml Solution G.
- Solution A contains phosphate, peptone, acetate, 1 ml Selenite-tungstate solution, resazurin, and 870 ml water.
- Solution B contains carbonate, bicarbonate, and 100 ml water; Solution C contains calcium chloride, magnesium chloride, and 10 ml water; Solution D is 1 ml Trace element solution; Solution F contains sodium sulfide and 10 ml water.
- Solution E combines 1 ml Seven vitamins solution and 1 ml Wolin's vitamin solution (10x).
- Solution G is a post-inoculation 15 ml mixture of 13.5 ml hexadecane plus 1.5 ml tetrachloroethene.

## Completeness

The record is incomplete because the generated YAML has no `solutions` block. It flattens Solutions A-G, Selenite-tungstate solution, Trace element solution, Seven vitamins solution, and Wolin's vitamin solution into a single top-level `ingredients` array.

## Findings

- Solution B, Solution C, Solution F, and the nested selenite-tungstate, trace-element, seven-vitamin, and Wolin-vitamin stocks all appear at stock strength as top-level ingredients.
- Solution G's 13.5 ml hexadecane and 1.5 ml tetrachloroethene liquid doses were converted to `13.5 G_PER_L` and `1.5 G_PER_L` final-medium concentrations.
- The Solution E vitamins were merged across the Seven vitamins and Wolin stocks; for example pyridoxine is stored as `0.4 G_PER_L`, nicotinic acid as `0.25 G_PER_L`, vitamin B12 as `0.101 G_PER_L`, and p-aminobenzoic acid as `0.13 G_PER_L`.
- The 870 ml, 100 ml, 10 ml, 10 ml, and four 1000 ml source water rows are missing from their solution scopes.
- The Trace element solution EDTA preparation step was appended as a generic top-level `ADJUST_PH` step.
- The four merged source records are duplicates only of the flattened signature; their generated canonical record still does not carry the DSMZ solution structure that should underlie all four views.

## Recommended Edits

- Rebuild the DSMZ 732a source as a 1008 ml main recipe with Solution A through Solution G additions.
- Move carbonate/bicarbonate, calcium/magnesium, sulfide, and the hexadecane plus tetrachloroethene mixture under Solutions B, C, F, and G respectively.
- Represent Solution D as 1 ml Trace element solution and Solution E as 1 ml Seven vitamins plus 1 ml Wolin vitamins, with each nested stock retaining its own composition and water row.
- Move the selenite-tungstate row under Solution A as a 1 ml nested stock and preserve its 1000 ml stock composition.
- Undo duplicate vitamin merges that cross Seven vitamins and Wolin solution boundaries.
- Keep the post-inoculation Solution G instruction attached to Solution G or to the main recipe as a post-inoculation addition, not as ordinary top-level ingredients.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that no child of the selenite-tungstate, trace-element, Seven vitamins, or Wolin stocks remains top-level.
- Verify that hexadecane and tetrachloroethene retain milliliter units and their post-inoculation timing.
- Verify that merged KOMODO aliases remain linked to the repaired DSMZ 732a structure.

## Additional Notes

None found.
