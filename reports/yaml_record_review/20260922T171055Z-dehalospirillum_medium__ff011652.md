# YAML Record Review: dehalospirillum_medium__ff011652

- Repository: CultureMech
- Record: `data/merge_yaml/merged/dehalospirillum_medium__ff011652.yaml`
- Started UTC: 2026-09-22T17:10:55Z
- Finished UTC: 2026-09-22T17:10:55Z
- Verdict: needs curation

## Target

Generated bacterial `dehalospirillum_medium` record for KOMODO Medium 833 and the MediaDive/DSMZ Medium 833 source duplicate.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to KOMODO Medium 833 and `mediadive.medium:833`. Its `parent_media` relationship to `data/normalized_yaml/bacterial/dehalospirillum_medium.yaml` is correct because the KOMODO record explicitly cites DSMZ Medium 833 and has no formulation change from the DSMZ parent.

The generated record is stale relative to both normalized sources. `repair_dsmz_833_family.py` corrected `data/normalized_yaml/bacterial/KOMODO_833_DEHALOSPIRILLUM_medium.yaml` and `data/normalized_yaml/bacterial/dehalospirillum_medium.yaml` against DSMZ 833 on 2026-08-25, reducing direct ingredients from 41 to 9, restoring 11 stock solutions, removing gas atmospheres from ingredients, and scaling the printed 1003 ml DSMZ batch to a one-litre final basis.

The complex/undefined classification is supported by yeast extract in Solution A.

## Evidence

MediaDive and the DSMZ PDF currently assemble the medium from a 1003 ml main solution: 892 ml Solution A, 10 ml Solution B, 2 ml Solution C, 35 ml Solution D, 20 ml Solution E, 40 ml Solution F, 3 ml Solution G, and 1 ml Solution H. The downloaded DSMZ Medium 833 PDF still has SHA-256 `35bf0077611e781af17c24f3786b51fc5ac8719df60ea06d8eb4d754d0f2fc33`, matching the hash recorded in the repaired normalized files.

The generated file keeps the pre-repair `g_l` values from the 892 ml Solution A sub-batch as if they were final-medium concentrations. For example, `Na2SO4` is `0.784753 G_PER_L`, `KH2PO4` is `0.224215 G_PER_L`, and `Yeast extract` is `2.24215 G_PER_L`; the repaired final-basis values are `0.697906`, `0.199402`, and `1.994018 G_PER_L`.

Stock ingredients were flattened as final direct ingredients. Examples include Solution D `Na2CO3` at `50 G_PER_L`, Solution E `Na-pyruvate` at `225 G_PER_L`, Solution F `Na2-fumarate` at `160 G_PER_L`, Solution G `FeSO4 x 7 H2O` at `4.28571 G_PER_L`, and Solution H `L-Cysteine HCl x H2O` at `50 G_PER_L`.

Trace element, selenite-tungstate, Wolin vitamin, and seven-vitamin stock contents were also promoted to top-level final ingredients at stock strength. Shared vitamins are partly summed across the two vitamin stocks, as shown by `Vitamin B12` at `0.101 G_PER_L`, `p-Aminobenzoic acid` at `0.13 G_PER_L`, and `Nicotinic acid` at `0.25 G_PER_L`, while alternate labels such as `Biotin` and `D-(+)-biotin` remain as separate duplicated rows.

The generated pH range is 7.3-7.7, but current DSMZ and MediaDive state 7.3-7.6. The `notes` string also retains KOMODO's `Aerobic: Yes` flag even though DSMZ Medium 833 is assembled under N2 or N2/CO2, reduced until resazurin is colorless, and optionally reduced further with anoxic sodium dithionite.

## Completeness

The generated record has no `solutions` block. It therefore loses all stock boundaries for Solutions A-H, Trace element solution SL-10, selenite-tungstate, resazurin, Wolin vitamins, seven vitamins, bicarbonate, pyruvate, fumarate, iron sulfate, and cysteine.

The generated record has no `preparation_steps`, so it drops the required anoxic sparging, separate autoclaving or filtration of the individual solutions, Solution B-H addition sequence, final pH adjustment, and the colorless-resazurin reduction check that are present in the repaired normalized DSMZ source.

## Findings

- Needs curation: the generated merged record predates the 2026-08-25 DSMZ 833 family repair in both normalized parents.
- Needs curation: all stock components are flattened as top-level final-medium ingredients at stock strength.
- Needs curation: direct Solution A ingredients are scaled to the Solution A sub-batch rather than the final 1003 ml medium.
- Needs curation: Wolin and seven-vitamin stock ingredients are partially summed across stock boundaries.
- Needs curation: `ph_range.max` is stale at 7.7 instead of 7.6.
- Needs curation: KOMODO's `Aerobic: Yes` text conflicts with the anaerobic DSMZ source preparation.
- Needs curation: `NiCl2 x 6 H2O` is grounded to an anhydrous `nickel dichloride` CHEBI term and should be rechecked during regeneration.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/dehalospirillum_medium__ff011652.yaml` from the repaired normalized KOMODO and DSMZ Medium 833 parents.
- Preserve the repaired DSMZ 833 direct ingredient scaling, pH 7.3-7.6 range, Solutions A-H volumes, and nested trace, selenite-tungstate, Wolin, and seven-vitamin stock compositions.
- Remove stock-internal trace metals, vitamins, carbonate, pyruvate, fumarate, FeSO4, and cysteine rows from top-level final-medium `ingredients`.
- Keep shared vitamin compounds separated by their source stock so vitamin rows are not summed across Wolin's vitamin solution and seven vitamins solution.
- Drop or qualify the KOMODO `Aerobic: Yes` note.
- Recheck the `NiCl2 x 6 H2O` grounding.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after regeneration.
- Confirm the generated direct-ingredient list matches the repaired parents' 9 direct ingredients.
- Confirm 11 solution records are present.
- Confirm `ph_range.max` is 7.6.
- Confirm the DSMZ 833 PDF SHA remains `35bf0077611e781af17c24f3786b51fc5ac8719df60ea06d8eb4d754d0f2fc33`, or re-review any source changes if the PDF changed.

## Additional Notes

MediaDive REST medium 833 and the linked DSMZ PDF were both reachable during review.
