# YAML Record Review: plate_count_agar_pca

- Repository: CultureMech
- Record: data/merge_yaml/merged/plate_count_agar_pca.yaml
- Started UTC: 2026-09-24T21:28:06Z
- Finished UTC: 2026-09-24T21:28:06Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:008509
- Name: plate_count_agar_pca
- Source import: plate_count_agar_pca
- Primary external ID: TOGO:M1930
- Maintained input: data/normalized_yaml/bacterial/plate_count_agar_pca.yaml

This generated record represents TOGO Medium M1930 / NBRC Medium 1197, Plate Count Agar (PCA).

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/plate_count_agar_pca.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the correct TOGO M1930 / NBRC 1197 identity, but the generated merge is stale. Exact ignored-file searches across `data` for `TOGO:M1930`, `M1930`, `NBRC_M1197`, `NO=1197`, and `plate_count_agar_pca` found one normalized YAML recipe, this merged YAML record, and generated index/tracking references to that same recipe.

The maintained `data/normalized_yaml/bacterial/plate_count_agar_pca.yaml` has a later `RESOLVED_TOGO_M1930_PLATE_COUNT_AGAR_SCORE15` repair that corrected the imported 1 G_PER_L misspelled water row to 1 L distilled water, added pH 7.2, grounded the PCA components, and removed the stale `kg_microbe_match`. None of that repair is present in this generated merged copy.

The generated `kg_microbe_match: mediadive.medium:21` is not an equivalent PCA grounding. MediaDive Medium 21 is DSMZ SARCINA MEDIUM, with 30 g glucose, 5 g peptone, 5 g yeast extract, 1000 ml water, and pH 6.0.

## Evidence

- TOGO M1930 imports NBRC Medium 1197 and links the NBRC 1197 page.
- TOGO M1930 lists 1 L water, 2.5 g yeast extract, 1 g glucose, 15 g agar if needed, 5 g tryptone, and pH 7.2.
- NBRC 1197 lists the same PCA recipe: 5 g tryptone, 2.5 g yeast extract, 1 g glucose, 15 g agar if needed, 1 L water, and pH 7.2.
- The maintained normalized input records those values, the source pH, the source links, and the curation event that removed the MediaDive 21 false match.

## Completeness

The generated merged record is not complete against either the source or the maintained input:

- It leaves source water as misspelled `Disrilled water` and converts the source 1 L solvent row to 1 G_PER_L.
- It omits the source pH 7.2.
- It leaves yeast extract, agar, and tryptone ungrounded.
- It still carries a stale MediaDive 21 cross-match that the maintained input has already removed.

## Findings

1. Major: The generated merged record is stale relative to `data/normalized_yaml/bacterial/plate_count_agar_pca.yaml`; future repair belongs in regeneration from the maintained normalized recipe, not in direct edits to `data/merge_yaml/merged/plate_count_agar_pca.yaml`.
2. Major: The stale generated record misrepresents the source 1 L water solvent as `1 G_PER_L` and misses the source pH 7.2.
3. Major: The stale `kg_microbe_match: mediadive.medium:21` points PCA at DSMZ Sarcina Medium, a different recipe.

## Recommended Edits

- Regenerate the merged YAML from the already-corrected `data/normalized_yaml/bacterial/plate_count_agar_pca.yaml` so the 1 L water row, pH 7.2, ingredient groundings, source references, and removal of `kg_microbe_match` propagate into `data/merge_yaml/merged/plate_count_agar_pca.yaml`.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after regeneration.
- Run an exact ignored-file search for `TOGO:M1930`, `NBRC_M1197`, and `NO=1197` with ignored files included before adding any new PCA duplicate import.
- Spot-check the regenerated merged YAML and rendered page to verify `Distilled water` is 1 L, `ph_value` is 7.2, and no `mediadive.medium:21` match remains on the PCA record.

## Additional Notes

None found.
