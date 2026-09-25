# YAML Record Review: desulfitobacterium_pcp_1_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfitobacterium_pcp_1_medium.yaml`
- Started UTC: 2026-09-22T17:51:42Z
- Finished UTC: 2026-09-22T17:51:42Z
- Verdict: needs curation

## Target

Generated bacterial `desulfitobacterium_pcp_1_medium` record for DSMZ Medium 836.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to DSMZ Medium 836 and its MediaDive identity matches the current DSMZ `DESULFITOBACTERIUM PCP-1 MEDIUM`.

The complex/undefined classification is supported by yeast extract.

The generated record incorrectly merged `medium_836_modified_for_dsm_13498` as a `SOURCE_DUPLICATE`. DSMZ 836 states that DSM 13498 requires 3.00 g/L Na-formate, so the DSM 13498 medium should be a variant of this base recipe rather than an exact duplicate.

## Evidence

DSMZ 836 adds 2.00 ml FeCl2 x 4 H2O stock, 1.00 ml Trace element solution SL-10, and 0.50 ml 0.1% sodium resazurin stock to the main 1000 ml water recipe. The generated record keeps the direct FeCl2 contribution as `0.002 G_PER_L`, but it also flattens the 1.5 g/L FeCl2 row from SL-10 and merges both rows into `1.502 G_PER_L`.

Every other SL-10 component is emitted as a top-level final-medium ingredient at stock strength: HCl `2.5 G_PER_L`, ZnCl2 `0.07 G_PER_L`, MnCl2 x 4 H2O `0.1 G_PER_L`, H3BO3 `0.006 G_PER_L`, CoCl2 x 6 H2O `0.19 G_PER_L`, CuCl2 x 2 H2O `0.002 G_PER_L`, NiCl2 x 6 H2O `0.024 G_PER_L`, and Na2MoO4 x 2 H2O `0.036 G_PER_L`.

The generated record preserves DSMZ's anaerobic preparation text and the SL-10 dissolution note, but has no `solutions` block for Trace element solution SL-10 or for the separate FeCl2, sodium resazurin, carbonate, sulfite, and sulfide stock additions.

DSMZ's 1000 ml distilled-water row is absent from the generated recipe.

The normalized `medium_836_modified_for_dsm_13498.yaml` source has the same ingredients as the base DSMZ 836 source and lacks the required 3.00 g/L Na-formate supplement.

## Completeness

The main DSMZ pH and anoxic preparation instructions survived into `preparation_steps`.

Structured stock records are missing for SL-10 and for the DSMZ stock additions that are added before use.

The DSM 13498 formate supplement is missing from the normalized child record and, as a result, from this generated merge.

## Findings

- Needs curation: Trace element solution SL-10 was flattened into final-medium ingredient rows at stock concentrations.
- Needs curation: direct FeCl2 and SL-10 FeCl2 were summed across different recipe contexts into `1.502 G_PER_L`.
- Needs curation: DSMZ 836 stock additions have no structured solution records.
- Needs curation: the DSMZ water row is absent.
- Needs curation: the DSM 13498 Na-formate variant is missing its 3.00 g/L Na-formate supplement.
- Needs curation: `medium_836_modified_for_dsm_13498` was merged as a source duplicate of the unsupplemented DSMZ 836 base medium.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfitobacterium_pcp_1_medium.yaml` so Trace element solution SL-10 is represented as a 1 ml/L stock addition with nested composition.
- Keep the direct 2 ml 0.1% FeCl2 stock separate from the FeCl2 in SL-10.
- Add a structured representation for the DSMZ carbonate, sulfite, sulfide, and resazurin stock additions where possible.
- Add the missing 3.00 g/L Na-formate supplement to `data/normalized_yaml/bacterial/medium_836_modified_for_dsm_13498.yaml`.
- Keep `medium_836_modified_for_dsm_13498` as a DSM 13498 variant rather than a `SOURCE_DUPLICATE` once its formate supplement is restored.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after regeneration.
- Confirm SL-10 components are nested under a Trace element solution SL-10 solution.
- Confirm FeCl2 is no longer a sum across direct and SL-10 contexts.
- Confirm the DSM 13498 child has a Na-formate row and a distinct merge fingerprint.
- Confirm DSMZ 836 preparation text survives regeneration.

## Additional Notes

MediaDive REST medium 836 and the DSMZ Medium 836 PDF were reachable during review and agreed on the base composition and the DSM 13498 Na-formate note.
