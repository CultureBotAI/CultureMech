# YAML Record Review: desulfitobacterium_pce_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfitobacterium_pce_medium.yaml`
- Started UTC: 2026-09-22T17:49:25Z
- Finished UTC: 2026-09-22T17:49:25Z
- Verdict: needs curation

## Target

Generated bacterial `desulfitobacterium_pce_medium` record for KOMODO Medium 717 and DSMZ Medium 717.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The generated record merges two duplicates for DSMZ Medium 717: a KOMODO shadow source and a MediaDive/DSMZ source. The live DSMZ PDF and MediaDive REST payload agree that 717 is `DESULFITOBACTERIUM (PCE) MEDIUM`.

The canonical generated record kept the KOMODO identity and its `Aerobic: Yes` note even though DSMZ 717 is prepared anoxically under 80% N2 and 20% CO2 and then amended with sterile anoxic stock solutions.

## Evidence

DSMZ 717 adds three nested stocks to the main recipe: 10.00 ml Modified Wolin's mineral solution, 1.00 ml Wolin's vitamin solution (10x), and 1.00 ml Seven vitamins solution. The generated file has no `solutions` block and emits all three stock recipes as top-level ingredients.

The top-level `MgSO4 x 7 H2O` row is `3.0988142 G_PER_L` because the direct main-medium contribution `0.0988142` was summed with the Modified Wolin stock concentration `3.0`.

The entire Modified Wolin's mineral formula is otherwise flattened at stock concentration, including nitrilotriacetic acid `1.5 G_PER_L`, MnSO4 x H2O `0.5 G_PER_L`, NaCl `1 G_PER_L`, FeSO4 x 7 H2O `0.1 G_PER_L`, CoSO4 x 7 H2O `0.18 G_PER_L`, CaCl2 x 2 H2O `0.1 G_PER_L`, and the remaining trace salts.

The source adds both Wolin's vitamin solution (10x) and Seven vitamins solution at 1 ml/L. Four chemicals that occur in both vitamin stocks were summed at stock strength: Pyridoxine hydrochloride is `0.4 G_PER_L`, Nicotinic acid is `0.25 G_PER_L`, Vitamin B12 is `0.101 G_PER_L`, and p-Aminobenzoic acid is `0.13 G_PER_L`.

The normalized DSMZ 717 and KOMODO 717 records gained a partial 2026-08-07 `apply_cocktail_nesting.py` repair after this generated record was emitted. The generated file is stale relative to that repair and still lacks nested vitamin stocks.

## Completeness

The generated record lacks DSMZ 717's anoxic preparation steps: sparging under 80% N2 and 20% CO2, Hungate or serum-vial dispensing, post-autoclave addition of lactate/fumarate/vitamins/sulfide/carbonate from sterile anoxic stocks, filter sterilization of fumarate and vitamin stocks, and the final pH 7.0-7.2 condition.

The generated record also lacks Modified Wolin's mineral preparation at pH 6.5/7.0 with KOH and all DSMZ water rows.

## Findings

- Needs curation: Modified Wolin's mineral solution was flattened at stock concentration instead of being represented as a 10.00 ml/L stock addition.
- Needs curation: Wolin's vitamin solution (10x) and Seven vitamins solution were flattened at stock concentrations instead of being represented as separate 1.00 ml/L stock additions.
- Needs curation: MgSO4 x 7 H2O and four vitamin rows were summed across different recipe contexts.
- Needs curation: the generated record predates the partial normalized vitamin-stock repair.
- Needs curation: duplicate merging chose the KOMODO source and dropped DSMZ preparation steps.
- Needs curation: the retained KOMODO `Aerobic: Yes` note contradicts the DSMZ anoxic recipe.

## Recommended Edits

- Finish the stock nesting in `data/normalized_yaml/bacterial/desulfitobacterium_pce_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_717_DESULFITOBACTERIUM_PCE_MEDIUM.yaml`.
- Keep Modified Wolin's mineral solution, Wolin's vitamin solution, and Seven vitamins solution as three distinct stock additions.
- Prevent duplicate cleanup from summing chemicals that appear in different stocks.
- Preserve the DSMZ preparation steps, equipment context, pH 7.0-7.2 condition, and stock-preparation text when merging the KOMODO and DSMZ duplicates.
- Remove or correct the KOMODO `Aerobic: Yes` note.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after regeneration.
- Confirm Modified Wolin's mineral components are nested and no longer top-level ingredients.
- Confirm both vitamin stocks are present separately and no vitamin row is a sum across the two stocks.
- Confirm the generated record includes DSMZ's anoxic N2/CO2 preparation.
- Confirm `Aerobic: Yes` is absent.

## Additional Notes

MediaDive REST medium 717 and the DSMZ Medium 717 PDF were reachable during review and agreed on the source composition.
