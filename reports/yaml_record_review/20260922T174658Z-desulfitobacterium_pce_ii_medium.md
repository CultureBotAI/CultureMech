# YAML Record Review: desulfitobacterium_pce_ii_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfitobacterium_pce_ii_medium.yaml`
- Started UTC: 2026-09-22T17:46:58Z
- Finished UTC: 2026-09-22T17:46:58Z
- Verdict: needs curation

## Target

Generated bacterial `desulfitobacterium_pce_ii_medium` record for KOMODO Medium 1062 and DSMZ Medium 1062.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The generated record merges two duplicates for DSMZ Medium 1062: a KOMODO shadow source and a MediaDive/DSMZ source. The medium-number identity is correct, and the live DSMZ PDF and MediaDive REST payload agree that 1062 is `DESULFITOBACTERIUM (PCE II) MEDIUM`.

The complex/undefined classification is supported by yeast extract.

The canonical generated record kept the KOMODO source as its main identity even though the MediaDive duplicate contains the DSMZ preparation steps and source PDF link.

## Evidence

DSMZ 1062 adds 10.00 ml Modified Wolin's mineral solution and 1.00 ml Seven vitamins solution to the main recipe. The generated file has no `solutions` block, so both source stocks are flattened into top-level ingredients.

Three generated top-level rows are sums across the main recipe and Modified Wolin's mineral stock: main `NaCl` `0.98912 G_PER_L` plus stock-strength `1.0` became `1.98912 G_PER_L`, main `CaCl2 x 2 H2O` `0.148368` plus stock-strength `0.1` became `0.248368 G_PER_L`, and main `FeSO4 x 7 H2O` `0.0217606` plus stock-strength `0.1` became `0.12176060000000001 G_PER_L`.

All other Modified Wolin's mineral components were emitted at stock concentration as if they were direct final-medium additions, including `1.5 G_PER_L` nitrilotriacetic acid, `3 G_PER_L` MgSO4 x 7 H2O, `0.5 G_PER_L` MnSO4 x H2O, `0.18 G_PER_L` CoSO4 x 7 H2O, and the selenium/tungsten rows.

Every Seven vitamins solution component is also emitted at stock strength even though the source adds only 1 ml of that stock per liter: Vitamin B12 `0.1 G_PER_L`, p-Aminobenzoic acid `0.08 G_PER_L`, D-(+)-biotin `0.02 G_PER_L`, Nicotinic acid `0.2 G_PER_L`, Calcium pantothenate `0.1 G_PER_L`, Pyridoxine hydrochloride `0.3 G_PER_L`, and Thiamine-HCl x 2 H2O `0.2 G_PER_L`.

The DSMZ import gained a partial 2026-08-07 `apply_cocktail_nesting.py` repair for four Seven vitamins components after this generated record was emitted. The generated file is stale relative to that partial normalized repair and still lacks a nested vitamin solution.

## Completeness

The generated record lacks DSMZ 1062's preparation sequence: 80% N2/20% CO2 sparging, Hungate or serum-vial dispensing, post-autoclave additions of ferrous sulfate, vitamins, pyruvate, fumarate, yeast extract, and carbonate from sterile anoxic stocks, filtration of ferrous sulfate/vitamins/pyruvate/fumarate stocks, final pH 7.5 adjustment, and the optional 10-20 mg/L sodium dithionite growth-stimulation note.

The Modified Wolin's mineral solution preparation at pH 6.5/7.0 with KOH was also lost during the KOMODO/DSMZ merge.

The three DSMZ water rows are absent: 1000 ml main-solution water, 1000 ml Modified Wolin's mineral water, and 1000 ml Seven vitamins water.

## Findings

- Needs curation: Modified Wolin's mineral solution was flattened at stock concentrations instead of being represented as a 10.00 ml/L stock addition.
- Needs curation: Seven vitamins solution was flattened at stock concentrations instead of being represented as a 1.00 ml/L stock addition.
- Needs curation: NaCl, CaCl2 x 2 H2O, and FeSO4 x 7 H2O were summed across main and stock contexts.
- Needs curation: the generated record predates the partial normalized Seven vitamins repair.
- Needs curation: the duplicate merge chose the KOMODO source and dropped DSMZ preparation steps.
- Needs curation: water rows and the sodium dithionite note are missing.

## Recommended Edits

- Complete the Seven vitamins nesting in both normalized DSMZ 1062 source records; the 2026-08-07 repair nested only part of that stock.
- Model Modified Wolin's mineral solution as a 10.00 ml/L stock, not as top-level ingredient rows.
- Keep main-solution NaCl, CaCl2, and FeSO4 separate from the same chemicals inside Modified Wolin's mineral solution.
- Preserve the MediaDive/DSMZ preparation steps, equipment context, optional sodium dithionite note, and stock-solution preparation text when merging the KOMODO duplicate with the DSMZ duplicate.
- Regenerate this merged record after the normalized stock nesting and duplicate-merge precedence are fixed.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after regeneration.
- Confirm `NaCl`, `CaCl2 x 2 H2O`, and `FeSO4 x 7 H2O` are no longer marked as merged duplicate sums.
- Confirm Seven vitamins and Modified Wolin's mineral components are nested below `solutions`.
- Confirm the DSMZ anaerobic preparation steps and sodium dithionite note survive duplicate merging.

## Additional Notes

MediaDive REST medium 1062 and the DSMZ Medium 1062 PDF were reachable during review and agreed on the source composition.
