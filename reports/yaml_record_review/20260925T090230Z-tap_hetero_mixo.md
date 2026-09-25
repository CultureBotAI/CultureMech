# YAML Record Review: tap_hetero_mixo

- Repository: CultureMech
- Record: `data/merge_yaml/merged/tap_hetero_mixo.yaml`
- Started UTC: 2026-09-25T09:01:44Z
- Finished UTC: 2026-09-25T09:02:30Z
- Verdict: needs curation

## Target

Generated merged record `CultureMech:007272` for `tap_hetero_mixo`, with
`MEDIADB:36`, fingerprint
`6fb0e31ed874b93aa155226ee47c8888fc0d4f6e70039b2f29e969e0bbfcf6d4`, and one
merged source, `tap_hetero_mixo`.

## Validation

- LinkML schema: passed.
- Strict validator: passed with 0 ERROR rows.
- Reference validator: passed with 0 checks.
- Term validator: passed.
- Embedded `curation_history`: Not checked: the available history validator checks
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The record is correctly grounded to MediaDB medium 36, `Tap (hetero/mixo)`, but
the generated merge is stale relative to
`data/normalized_yaml/bacterial/tap_hetero_mixo.yaml`. The normalized source has
already repaired the broken MediaDB label, grounded all 18 mM components, added
pH 7.0 and 25 C growth evidence for Chlamydomonas reinhardtii, and linked the
record to `tap_auto` as the 17.4 mM acetate-supplemented TAP variant.

## Evidence

MediaDB 36 lists the same 18 millimolar compounds and amounts as the generated
record: the 17 TAP(auto) components plus 17.4 mM acetate. MediaDB 36 links
source 15, Boyle et al. 2009, and two Chlamydomonas reinhardtii growth records.

MediaDB growth-data record 85 reports heterotrophic Chlamydomonas reinhardtii on
MediaDB 36 at growth rate `0.035` 1/h, pH 7.0, temperature 25.0 C, and acetate
uptake 12.06 mmol/gDW/h. Growth-data record 87 reports mixotrophic
Chlamydomonas reinhardtii on the same medium at growth rate `0.066` 1/h, pH
7.0, and temperature 25.0 C.

MediaDB source 15 identifies the publication as Boyle et al., 2009, and PubMed
record `PMID:19128495` confirms DOI `10.1186/1752-0509-3-4`.

## Completeness

The generated ingredient amounts are complete for the MediaDB 36 export, but the
generated record is missing most normalized TAP curation: the repaired name,
CHEBI links for ions, `ph_value`, `temperature_value`, `target_organisms`,
growth records 85 and 87, Boyle et al. references, `data_quality_flags`,
`parent_media`, `variant_relationship`, and `variant_modifications`.

The generated record also keeps generic `DISSOLVE`, `ADJUST_PH`, and 0.22 um
`FILTER_STERILIZE` steps that are not present on the fetched MediaDB 36 page or
tab-delimited export.

## Findings

- `original_name` and `media_term.term.label` still contain the old MediaDB
  parenthesis-truncation artifact.
- The generated merge is missing the MediaDB TAP curation already present on the
  normalized source from `repair_mediadb_tap_score15.py`.
- Most ion ingredients still lack CHEBI-keyed `term` and
  `mediaingredientmech_chebi_term` entries in the generated record.
- Growth-data records 85 and 87, the Boyle et al. DOI, and the explicit
  Chlamydomonas reinhardtii target are absent from the generated merge.
- The acetate-supplemented relationship to `tap_auto` is absent from the
  generated merge.
- The generic preparation steps are not source-backed by MediaDB 36.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/tap_hetero_mixo.yaml` from the curated
  normalized MediaDB 36 source so the repaired name, pH/temperature fields,
  Chlamydomonas evidence, DOI, and TAP(auto) parent link are carried forward.
- Keep the 18 MediaDB ingredient concentrations unchanged while regenerating;
  they already match `media_text/36`.
- Remove the generic preparation placeholders unless a MediaDB SQL field or
  Boyle et al. passage supports them.

## Follow-up Checks

- After regeneration, verify that `parent_media.id` remains
  `CultureMech:007283` and `variant_relationship` remains
  `SUPPLEMENTED_VARIANT`.
- Confirm that both MediaDB growth records, 85 and 87, are present in the
  generated target-organism evidence.
- Confirm the generated record no longer contains the broken label
  `'''TAP (hetero/mixo`.

## Additional Notes

None found
