# YAML Record Review: l_wenstein_jensen_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/l_wenstein_jensen_medium.yaml
- Started UTC: 2026-09-23T18:00:16Z
- Finished UTC: 2026-09-23T18:01:36Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/l_wenstein_jensen_medium.yaml`, generated `MediaRecipe` record `CultureMech:005071` for the KOMODO and DSMZ Lowenstein-Jensen Medium merge.

- Maintained owners: `data/normalized_yaml/bacterial/KOMODO_354_L_WENSTEIN-JENSEN_medium.yaml`, `data/normalized_yaml/bacterial/l_wenstein_jensen_medium.yaml`, `data/normalized_yaml/bacterial/medium_354_modified_for_dsm_44338.yaml`, and `data/normalized_yaml/bacterial/medium_354_modified_for_dsm_44339.yaml`.
- Merge provenance: `merged_from` lists all four maintained owners; generated merge fingerprint `5427140da26e5cbf92ff0d43eae015d550736f48173f9e390d37c1a4013d7af4`.
- Source claim: KOMODO ModelSEED ID 354 with DSMZ Medium 354, plus two KOMODO 354 strain-specific source duplicates.
- Current generated identity: `medium_type: COMPLEX`, `composition_type: UNDEFINED`, `physical_state: LIQUID`, pH 7.0.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/l_wenstein_jensen_medium.yaml`. |
| Strict schema | Passed with `python scripts/validate_strict.py data/merge_yaml/merged/l_wenstein_jensen_medium.yaml --out /private/tmp/l_wenstein_jensen_medium.strict.tsv --workers 1 --quiet`. |
| Reference integrity | Passed with `linkml-reference-validator validate data data/merge_yaml/merged/l_wenstein_jensen_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; there were 0 checks. |
| Term integrity | Passed with `linkml-term-validator validate-data data/merge_yaml/merged/l_wenstein_jensen_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

DSMZ Medium 354 and MediaDive medium 354 resolve to Lowenstein-Jensen Medium at pH 7.0, so the generated recipe is grounded to the right source medium. An exact ignored-file-inclusive search of `data/normalized_yaml` and `data/merge_yaml` for `CultureMech:005071`, `CultureMech:001454`, `CultureMech:005069`, `CultureMech:005070`, `mediadive.medium:354`, and the three KOMODO 354 accessions found the four maintained normalized records merged into this generated record and no additional maintained YAML duplicates.

The generated record chose the KOMODO copy as canonical even though the direct DSMZ import has the clean DSMZ label and source accession. That leaves `original_name: L?WENSTEIN-JENSEN medium` and `media_term: komodo.medium:354` at the top level, while the cleaner `L...WENSTEIN-JENSEN MEDIUM` DSMZ record is only stored as `parent_media`.

Ingredient identities are mostly grounded. The source lists the same KH2PO4, MgSO4, Mg-citrate, L-asparagine, potato flour, malachite green, glycerol, and fresh egg mixture ingredients. The first six gram amounts are normalized through MediaDive's 1612 ml final volume, but the two volume additions are not safely representable as `G_PER_L`.

## Evidence

The DSMZ PDF for Medium 354 lists the same six dry ingredients in 600 ml distilled water, followed by glycerol and fresh egg mixture additions. It sets pH to 7.0, sterilizes for 30 min at 121 C, cools to 30 C, and then carefully adds the fresh egg mixture. MediaDive serializes that source with a calculated 1612 ml main-solution volume, yielding the record's 1.55087 g/L KH2PO4, 0.148883 g/L MgSO4, 0.372208 g/L Mg-citrate, 2.23325 g/L L-asparagine, 18.6104 g/L potato flour, and 0.248139 g/L malachite green values.

The source does not state 12 g/L glycerol or 1000 g/L fresh egg mixture. DSMZ records glycerol as 12 ml and fresh egg mixture as 1000 ml. Representing those millilitre additions as grams per litre assumes an unstated density and obscures that the egg mixture is a volume addition prepared from fresh eggs.

## Completeness

The merged duplicate relationships are complete for maintained YAML files: the ignored-inclusive search found the DSMZ record, the KOMODO source duplicate, and both KOMODO strain-specific source duplicates that reference DSMZ 354.

The record is incomplete in these consequential places:

- It lacks structured `sources` or `source_data`; DSMZ and KOMODO provenance are present only through `media_term`, `notes`, `synonyms`, and merge fields.
- The direct DSMZ PDF URL is not present at top level after the KOMODO copy becomes canonical.
- Volume additions are not represented with millilitre units, and no note warns that `G_PER_L` is a lossy coercion for glycerol and egg mixture.

Empty `target_organisms` is acceptable here because DSMZ Medium 354 is a medium recipe and the inspected DSMZ PDF does not assert a growth result for DSM 44338 or DSM 44339.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Glycerol and fresh egg mixture are recorded as unsupported `G_PER_L` concentrations. | DSMZ Medium 354 and MediaDive 354 list glycerol as 12 ml and fresh egg mixture as 1000 ml; the generated record stores them as `12 G_PER_L` and `1000 G_PER_L`. | All four maintained owners or the DSMZ/KOMODO import normalization |
| Minor | The generated record canonicalizes to the noisier KOMODO copy instead of the direct DSMZ parent. | `CultureMech:005071` preserves `L?WENSTEIN-JENSEN medium` and `komodo.medium:354`; `CultureMech:001454` carries the exact DSMZ Medium 354 source accession and clean source label. | `data/normalized_yaml/bacterial/KOMODO_354_L_WENSTEIN-JENSEN_medium.yaml` plus merge canonicalization |
| Minor | Source provenance is free text after merge. | The generated record names DSMZ 354 only in `notes` and `parent_media`; no `sources` or `source_data` object carries `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium354.pdf`. | All four maintained owners |

## Recommended Edits

1. In the four maintained owners or the DSMZ/KOMODO import path, preserve glycerol and fresh egg mixture as volume additions or add a representation that does not claim unsupported gram-per-litre concentrations.
2. Prefer the direct DSMZ record as the canonical source within the source-duplicate merge, or copy its clean DSMZ label and `mediadive.medium:354` identity to the generated canonical record while retaining KOMODO IDs as source synonyms.
3. Add structured DSMZ/KOMODO source metadata to the maintained records so the DSMZ Medium 354 PDF URL and KOMODO source IDs do not need to be recovered from notes.
4. Regenerate `data/merge_yaml/merged/l_wenstein_jensen_medium.yaml` and affected pages.

## Follow-up Checks

- Rerun the open-schema, strict, reference, and term validators against the regenerated merged record.
- Recompare the six dry ingredients against DSMZ Medium 354 and confirm their final g/L values still use the documented 1612 ml MediaDive volume.
- Manually confirm glycerol and fresh egg mixture no longer appear as density-free gram-per-litre conversions.
- Repeat the exact `rg --no-ignore --hidden` search over `data/normalized_yaml` and `data/merge_yaml` for DSMZ 354 and KOMODO 354 IDs to make sure all maintained source duplicates were updated together.

## Additional Notes

The two KOMODO `medium_354_modified_for_dsm_44338` and `medium_354_modified_for_dsm_44339` records have no local formula difference from DSMZ 354, and the generated `SOURCE_DUPLICATE` relationship matches the inspected YAML. This review did not find a source-level modification for either strain-specific KOMODO accession.
