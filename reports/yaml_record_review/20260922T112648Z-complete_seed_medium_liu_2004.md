# YAML Record Review: Complete Seed Medium (Liu 2004)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/complete_seed_medium_liu_2004.yaml`
- Started UTC: 2026-09-22T11:24:30Z
- Finished UTC: 2026-09-22T11:26:48Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:007282`
- Normalized source: `data/normalized_yaml/bacterial/complete_seed_medium_liu_2004.yaml`
- Source identity: MediaDB Medium 379, `Complete seed medium (liu 2004)`
- Current generated merge: one source recipe, `complete_seed_medium_liu_2004`

## Validation

- Open schema validation: pass.
- Strict validation: pass.
- Reference validation: pass with 0 checks.
- Term validation: pass.
- Embedded `curation_history`: not checked by the standalone history validator.

## Identity and Grounding

- MediaDB Medium 379 lists ten compounds and millimolar amounts; all ten are present with matching concentrations in the generated record.
- MediaDB ties Medium 379 to two `Candida glabrata` organisms and Liu LM et al. 2004.
- CultureMech has a `fungal` category, but both the generated and normalized records set `category: bacterial` and the owner lives under `data/normalized_yaml/bacterial`.
- The normalized owner repaired the truncated MediaDB name on August 31, 2026, but this August 6 generated record still emits `'''Complete Seed Medium (Liu 2004`.

## Evidence

- MediaDB HTML checked: `https://mediadb.systemsbiology.net/defined_media/media/379/`.
- MediaDB tab-delimited export checked: `https://mediadb.systemsbiology.net/defined_media/media_text/379/`.
- MediaDB source page checked: `https://mediadb.systemsbiology.net/defined_media/sources/125/`.
- Local normalized owner checked: `data/normalized_yaml/bacterial/complete_seed_medium_liu_2004.yaml`.
- The schema category enum includes `fungal`.

## Completeness

- The defined liquid formulation, ten compound identities, and millimolar concentrations are complete with respect to MediaDB.
- Generic preparation steps are plausible for a defined liquid medium and do not contradict MediaDB.
- The medium is assigned to the wrong repository category for its source organisms.

## Findings

1. `category: bacterial` is unsupported for MediaDB 379; MediaDB lists only `Candida glabrata` growth data, and this should be curated as a fungal medium.
2. `original_name` and `media_term.term.label` are stale in generated output; the normalized owner has already restored `Complete Seed Medium (Liu 2004)`.
3. The generated and normalized notes cite only the MediaDB database URL and do not capture the underlying Liu LM et al. 2004 / PMID 15242462 source exposed by MediaDB source 125.

## Recommended Edits

1. Move the normalized owner to the fungal category and update `category` accordingly.
2. Regenerate this record so the repaired full MediaDB name appears in generated output.
3. Add the exact MediaDB source 125 / PMID 15242462 citation to normalized evidence metadata.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after moving and regenerating the record.
- Diff the regenerated ingredients against MediaDB `media_text/379` to confirm all ten millimolar values survive the category move.
- Confirm no stale bacterial-path reference to `complete_seed_medium_liu_2004.yaml` remains after the move; this should use an ignored-inclusive search.

## Additional Notes

- No ingredient-count or concentration defect was found.
- The source search for this record included gitignored files.
