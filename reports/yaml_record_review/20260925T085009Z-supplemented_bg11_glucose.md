# YAML Record Review: Supplemented BG11 + Glucose

- Repository: CultureMech
- Record: data/merge_yaml/merged/supplemented_bg11_glucose.yaml
- Started UTC: 2026-09-25T08:48:36Z
- Finished UTC: 2026-09-25T08:50:09Z
- Verdict: needs curation

## Target

- Reviewed generated record `CultureMech:007291` in `data/merge_yaml/merged/supplemented_bg11_glucose.yaml`.
- Source: `data/normalized_yaml/bacterial/supplemented_bg11_glucose.yaml`.
- Media term: `MEDIADB:387`, `Supplemented BG11 + Glucose`.
- Merge fingerprint: `7651ea520e330a74c0d31959649e08012084dadc4dc3c85a72358ba4ee9b9f48`.

## Validation

- LinkML schema validation passed: `No issues found`.
- Strict validation passed with 0 error rows.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

- The generated record is grounded to MediaDB medium `387`, `Supplemented bg11 + glucose`.
- Exact ignored-file-inclusive searches found `CultureMech:007291`, `MEDIADB:387`, `source: supplemented_bg11_glucose.yaml`, `supplemented_bg11_glucose`, and the `7651ea520e330a74c0d31959649e08012084dadc4dc3c85a72358ba4ee9b9f48` fingerprint in the generated record, normalized source, and normalized indexes at expected locations.
- A prior search that included a generic `BG11` alternation was too broad, matched unrelated BG11-family records, and was discarded.

## Evidence

- The MediaDB 387 page and its tab-delimited export list 17 compounds with millimolar amounts matching the normalized source and generated record.
- MediaDB 387 links to the Anderson SL et al. 1991 source record and to two growth data records for `Synechocystis pcc6803` on `Supplemented bg11 + glucose`.
- The MediaDB source page for source 136 identifies the source as Anderson SL, Journal of Bacteriology, 1991, `Light-activated heterotrophic growth of the cyanobacterium Synechocystis sp. strain PCC 6803: a blue-light-requiring process`, PMID 1902208.
- The normalized source has an August 31, 2026 `repair_mediadb_names.py` curation history entry restoring the ferric dicitrate name from MediaDB 387's own compound list.

## Completeness

- The generated record preserves the MediaDB medium ID, all 17 compounds, the MediaDB concentrations in mM, and the general MediaDB applications.
- The generated record does not expose the MediaDB organism, source ID 136, or growth-data links as structured target-organism or citation metadata.
- MediaDB provides no source-specific preparation protocol on the medium page; the generated preparation steps are generic placeholders.

## Findings

- The generated YAML is stale relative to the normalized source: it still has `'''Fe(III'` as a truncated preferred term where `data/normalized_yaml/bacterial/supplemented_bg11_glucose.yaml` now has `Fe(III)dicitrate`.
- Source metadata is undercaptured. MediaDB 387 links the recipe to source 136, Anderson SL et al. 1991, and two `Synechocystis pcc6803` growth records, but the generated `MediaRecipe` only has generic MediaDB applications.
- The generated preparation steps are not evidence-backed by MediaDB 387. The source table gives compound concentrations but no pH or sterilization protocol, while the YAML says to adjust pH if specified and filter-sterilize through 0.22 um.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/supplemented_bg11_glucose.yaml` from the repaired normalized source so `Fe(III)dicitrate` replaces the stale truncated token.
- Extend the MediaDB import or a downstream enrichment step to carry MediaDB source ID 136, PMID 1902208, and the linked `Synechocystis pcc6803` growth context into structured citation or target-organism fields.
- Do not emit generic pH/filtration preparation steps for MediaDB recipes unless the MediaDB source or linked publication provides them.
- Do not hand-edit this generated file.

## Follow-up Checks

- Revalidate the regenerated MediaDB 387 merge after regeneration.
- Verify that no generated MediaDB medium still contains a preferred term truncated at an opening parenthesis.
- Verify that the regenerated record either omits source-unsupported preparation steps or ties them to publication evidence.

## Additional Notes

- Empty optional fields were not treated as defects.
- `/defined_media/sources/387/` was checked and returned 404 because `387` is the medium ID; source ID 136 from the MediaDB 387 page was then checked directly.
