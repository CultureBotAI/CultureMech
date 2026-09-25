# YAML Record Review: minimal_vitamin_mv_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/minimal_vitamin_mv_medium.yaml
- Started UTC: 2026-09-24T07:28:54Z
- Finished UTC: 2026-09-24T07:29:22Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:008998`
- Generated name: `minimal_vitamin_mv_medium`
- Generated source file: `data/merge_yaml/merged/minimal_vitamin_mv_medium.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/minimal_vitamin_mv_medium.yaml`
- Declared upstream source: TOGO Medium `M2415`, `minimal vitamin (MV) medium`

## Validation

- Open LinkML validation passed: `No issues found`.
- Strict validation passed with 0 ERROR rows in `/private/tmp/minimal_vitamin_mv_medium.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The generated `media_term` points to `TOGO:M2415`.
- The 20 generated top-level ingredients are structurally valid.
- Several hydrated salts have no `mediaingredientmech_chebi_term`, although they do have primary CHEBI terms.
- `CoCl2 x 6H2O` is grounded to generic cobalt dichloride rather than cobalt chloride hexahydrate.
- `NaH2PO4 x H2O` is grounded to generic sodium dihydrogenphosphate rather than the monohydrate.

## Evidence

- Not checked: `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2415` returned an empty body twice.
- Not checked: `https://togomedium.org/medium/M2415` returned the TogoMedium single-page application shell, not embedded medium data.
- Not checked: `https://mediadive.dsmz.de/rest/medium/2415` returned `DataNotFound`.
- An ignored-file-inclusive exact local search found `TOGO:M2415` only in indexes plus this normalized and merged record; it did not find another local imported source record with a recoverable M2415 formula.

## Completeness

- The record has no pH, temperature, preparation note, source publication, organism, or strain metadata beyond the generic `Microbial cultivation` application.
- Because the upstream TOGO payload was unavailable, the ingredient count, ordering, units, and stock structure could not be rechecked against source evidence.
- The normalized owner and generated merged record have the same ingredient data, so any formula issue would need to be repaired in `data/normalized_yaml/bacterial/minimal_vitamin_mv_medium.yaml`.

## Findings

- High: The declared upstream source `TOGO:M2415` could not be recovered through the normal TOGO API, and no alternate authoritative formula was present locally under ignored-file-inclusive exact search. The generated recipe is therefore currently not auditable from its cited source.
- Medium: The record lacks organism, pH, temperature, and preparation context; this may be source loss if those fields were present in the original TOGO page.
- Low: Cobalt chloride hexahydrate and sodium dihydrogenphosphate monohydrate have overbroad CHEBI grounding.
- Low: `high_metal: true` should be reviewed after source recovery because the visible formula uses mostly microgram-per-liter trace metals.

## Recommended Edits

- Recover TOGO `M2415` from an upstream dump, the original TOGO import artifact, or the source publication behind `minimal vitamin (MV) medium`.
- Verify all 20 generated ingredient rows, including the microgram-per-liter vitamins and trace metals, against that recovered source.
- Correct the cobalt chloride and sodium dihydrogenphosphate hydrate groundings if the recovered formula confirms the hydrate labels.
- Remove or recompute `high_metal` after the formula is source-checked.
- Add pH, preparation, organism, strain, and publication context if recovered source evidence supports it.

## Follow-up Checks

- Re-run the TOGO M2415 API check before editing in case the empty-body response was transient.
- Repeat the exact ignored-file-inclusive search for `TOGO:M2415` if import archives or source dumps are added to the repository.
- Re-run open LinkML, strict, reference, and term validation after any recovered-source curation.
- The normalized-owner lookup used `rg --no-ignore --hidden`; repeat ignored-file-inclusive checks for exact owner and duplicate source paths after the edit.

## Additional Notes

- None found.
