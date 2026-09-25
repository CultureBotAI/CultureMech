# YAML Record Review: Desulfovibrio (MV) Medium (For DSM 13257)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_mv_medium_for_dsm_13257.yaml`
- Started UTC: 2026-09-22T20:57:34Z
- Finished UTC: 2026-09-22T20:57:34Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:009288` for `desulfovibrio_mv_medium_for_dsm_13257`, a TOGO M2738 import derived from DSMZ Medium 641 modification text.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The target is grounded to `TOGO:M2738`, `Desulfovibrio (MV) Medium (For DSM 13257)`, with an original DSMZ Medium 641 URL in `notes`.

A gitignore-independent exact lookup found the TOGO M2738 normalized source and the KOMODO `medium_641_modified_for_dsm_13257` record. The KOMODO record has already been linked under DSMZ Medium 641 as a strain-specific variant, while TOGO M2738 remains a separate generated target because it uses the pyruvate and bicarbonate DSM 13257 modification rather than the unmodified DSMZ 641 lactate and carbonate rows.

## Evidence

TOGO M2738 represents the DSM 13257 recipe as a main solution with 0.5 ml Na-resazurin solution, 1000 ml distilled water, basal salts, yeast extract, sodium sulfide, 2 g NaHCO3, 2.5 g Na-pyruvate, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, 10 ml Wolin's vitamin solution, and N2 gas.

The TOGO source also carries full subcomponent recipes for Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution. Their ingredient rows use milligram quantities for the trace metals and vitamins, except for HCl, FeCl2, NaOH, and the stock water rows.

## Completeness

The generated record is incomplete. It keeps empty `Unknown solution` stubs for Na-resazurin, Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution, but the actual stock compositions have been flattened into the top-level `ingredients` list.

The main-formula salts, pyruvate, bicarbonate, and yeast extract are present, but the 3990.0 G/L `Distilled water` row incorrectly sums the four 1000/990/1000/1000 ml water rows across the main recipe and all stocks.

## Findings

- High: Trace element solution SL-10 was flattened. Its milligram trace-metal rows became 36, 6, 100, 190, 24, 2, and 70 G/L top-level rows, and 10 ml HCl was copied as 10 G/L.
- High: Wolin's vitamin solution was flattened. Its 2, 5, 10, 2, 0.1, 5, 5, 5, and 5 mg vitamin rows became G/L top-level rows.
- High: Selenite-tungstate solution was flattened. The 3 mg selenite and 4 mg tungstate rows became 3 and 4 G/L top-level rows.
- High: Four source water rows were merged into one chemically invalid 3990.0 G/L `Distilled water` row.
- Medium: The Na-resazurin, Trace element, Selenite-tungstate, and Wolin's vitamin `solutions` entries have empty `composition` lists and use `G_PER_L` units for source-volume additions of 0.5 ml, 1 ml, 1 ml, and 10 ml.
- Medium: N2 and N2 gas are duplicated as variable top-level ingredients even though they are gas-atmosphere instructions.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfovibrio_mv_medium_for_dsm_13257.yaml` from TOGO M2738 so the main recipe keeps Na-resazurin, Trace element, Selenite-tungstate, and Wolin's vitamin as source-volume additions.
- Move the TOGO Trace element, Selenite-tungstate, and Wolin's vitamin subcomponent recipes into populated subordinate `solutions` entries with their own water rows.
- Split the summed 3990.0 G/L water row back into the 1000 ml main water, 990 ml Trace element stock water, 1000 ml Selenite-tungstate stock water, and 1000 ml Wolin's vitamin stock water rows.
- Model the 100% N2 entries as preparation gas context rather than duplicated variable ingredients.
- Keep this TOGO M2738 pyruvate/bicarbonate variant separate from the KOMODO 641_13257 DSMZ 641 wrapper unless a source confirms they should be reconciled.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized curation.
- Regenerate merged YAML and verify the output no longer has empty `Unknown solution` stubs, stock milligram rows copied as G/L final-medium ingredients, or a 3990.0 G/L water row.
- Compare the curated pyruvate/bicarbonate recipe against DSMZ Medium 641 to ensure only the DSM 13257 modifications diverge.

## Additional Notes

None found.
