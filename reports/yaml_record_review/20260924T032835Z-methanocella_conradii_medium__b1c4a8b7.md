# YAML Record Review: methanocella_conradii_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/methanocella_conradii_medium__b1c4a8b7.yaml`
- Started UTC: 2026-09-24T03:28:35Z
- Finished UTC: 2026-09-24T03:28:35Z
- Verdict: needs curation

## Target

- Stable ID: `CultureMech:009130`
- Label: `methanocella_conradii_medium`
- Category: `archaea`
- Maintained owner: `data/normalized_yaml/archaea/TOGO_M2561_Methanocella_Conradii_Medium.yaml`
- Source identity: TOGO medium M2561, linked directly to the DSMZ Medium 1318 PDF

## Validation

- Open schema: Passed; `linkml-validate` reported no issues.
- Strict validator: Passed; 1 file scanned, 0 files with errors, and 0 error rows.
- Reference validator: Passed; 0 reference checks were applicable.
- Term validator: Passed.
- Embedded history: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

- `media_term` grounds this record to `TOGO:M2561`.
- Exact ignored-file search for `CultureMech:009130`, `TOGO_M2561_Methanocella_Conradii_Medium`, `TOGO:M2561`, `mediadive.solution:4178`, `mediadive.solution:5543`, `mediadive.solution:6241`, and `mediadive.solution:4611` confirms a single TOGO M2561 owner for this generated fingerprint.
- TOGO M2561 links to the DSMZ 1318 PDF rather than an independent formula. The current normalized owner correctly records `CultureMech:000776` / DSMZ Medium 1318 as its `SOURCE_DUPLICATE` parent, but the generated YAML predates that identity repair and publishes M2561 as a standalone record.
- The generated record is stale relative to its maintained owner, which received the August 25 `CORRECTED_DSMZ_1318_SOLUTION_STRUCTURE` repair.

## Evidence

- DSMZ/MediaDive 1318 encodes a 1004 ml printed batch with 1 ml additions of SL-10, selenite-tungstate, Wolin 10x vitamin, and seven-vitamin stocks plus 0.5 ml 0.1% resazurin.
- The current TOGO M2561 owner records the August 25 DSMZ 1318 repair, with `ingredients 39 -> 11` and `solutions 5 -> 5`.
- The generated record was last built on August 6 and still contains the pre-repair flat ingredient list, five `Unknown solution` stock stubs, and no `ph_value`, `preparation_steps`, `parent_media`, or `variant_relationship`.

## Completeness

- The DSMZ PDF and MediaDive REST source provide enough evidence to encode all direct ingredients, the five stock additions, pH 7.0, and DSMZ 1318 preparation details.
- Empty `target_organisms` and `growth_data` are optional-field omissions, not review findings for this record.

## Findings

- Blocker: generated YAML still publishes the pre-repair flattened recipe. SL-10 components, selenite-tungstate components, Wolin vitamin components, seven-vitamin components, and the resazurin solution all appear as top-level `ingredients` even though the current normalized owner has already moved them into five nested `solutions`.
- Blocker: the generated record contains five `Unknown solution` objects for stocks that are already structured in the current normalized owner.
- Blocker: stock-only rows are off by orders of magnitude because source milligram stock rows became gram-per-litre final rows. Examples include `Na2MoO4 x 2 H2O` at `36` g/L, `MnCl2 x 4 H2O` at `100` g/L, `CoCl2 x 6 H2O` at `190` g/L, vitamin B12 at `100.1` g/L, and nicotinic acid at `205.0` g/L.
- Major: the generated file sums chemically equivalent vitamin rows across the Wolin 10x vitamin and seven-vitamin stocks, as shown by `p-Aminobenzoic acid` at `85.0` g/L and `Vitamin B12` at `100.1` g/L.
- Major: final-medium water is `4990.0` g/L because water from five different solution scopes was merged into the top-level final ingredient list.
- Major: the generated record lacks the current owner's pH 7.0 and DSMZ 1318 preparation steps for N2/CO2 sparging, filter-sterilized vitamin addition, anoxic carbonate/cysteine/DTT stocks, SL-10 preparation, and 100% H2 overpressure.
- Major: the generated record lacks the current `SOURCE_DUPLICATE` relationship to the canonical DSMZ 1318 parent.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/methanocella_conradii_medium__b1c4a8b7.yaml` from the current normalized TOGO M2561 owner.
- Ensure merge generation preserves the five nested stocks from the August 25 repair instead of re-flattening solution components into top-level ingredients.
- Ensure the regenerated record retains `ph_value: 7.0`, DSMZ 1318 preparation steps, and the `SOURCE_DUPLICATE` relationship to `data/normalized_yaml/archaea/methanocella_conradii_medium.yaml`.
- Verify TOGO M2561 is collapsed with the canonical DSMZ 1318 generated record after regeneration.

## Follow-up Checks

- Rerun open-schema, strict, reference, and term validation after regenerating merged YAML.
- Search regenerated output for `Unknown solution` scoped to this record and confirm no stale solution stubs remain.
- Search regenerated output for `4990.0`, `100.1`, `205.0`, and `Merged 5 duplicates` and confirm those stale flattened values are gone.
- Confirm the regenerated M2561 record includes the August 25 `CORRECTED_DSMZ_1318_SOLUTION_STRUCTURE` history entry and the `CultureMech:000776` source-duplicate parent.

## Additional Notes

None found.
