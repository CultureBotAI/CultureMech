# YAML Record Review: acidicaldus_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml`
- Started UTC: 2026-09-21T08:53:28Z
- Finished UTC: 2026-09-21T08:54:42Z
- Verdict: needs curation

## Target

Generated merge record `ACIDICALDUS_MEDIUM.yaml` represents a merge of `KOMODO_1038_ACIDICALDUS_medium.yaml` and `acidicaldus_medium.yaml` for ACIDICALDUS MEDIUM / DSMZ Medium 1038. The direct DSMZ source is recorded as `mediadive.medium:1038`; the KOMODO duplicate is `komodo.medium:1038`.

## Validation

- PASS: open LinkML schema validation with `linkml-validate`.
- PASS: strict schema layer validation with `scripts/validate_strict.py`.
- PASS: linkml-reference-validator on this generated record.
- PASS: linkml-term-validator on this generated record.
- Not checked: embedded `MediaRecipe.curation_history` entries; no focused generated-record history validator is documented, and `just validate-history` targets standalone `history/` files.

## Identity and Grounding

The source duplicate relationship is well grounded. An ignored-inclusive exact source-ID search found only one normalized `mediadive.medium:1038` record and only one normalized `komodo.medium:1038` record, and both point to ACIDICALDUS MEDIUM with the same seven non-water ingredients at the same concentrations.

The generated record's displayed identity is weaker than the merge metadata. It uses the KOMODO child as the top-level recipe and exposes `komodo.medium:1038` as `media_term`, while `parent_media` correctly identifies the direct DSMZ source as `data/normalized_yaml/bacterial/acidicaldus_medium.yaml`. For a DSMZ/KOMODO source duplicate, the DSMZ import carries the primary formulation and should be the generated body when it contains fields that KOMODO lacks.

## Evidence

- DSMZ Medium 1038 PDF fetched during review: lists 0.45 g `(NH4)2SO4`, 0.05 g `KCl`, 0.50 g `MgSO4 x 7 H2O`, 0.05 g `KH2PO4`, 0.02 g `Ca(NO3)2 x 4 H2O`, 1.00 g `D-Glucose`, 0.20 g `Yeast extract (OXOID)`, and 1000 ml distilled water, then instructs dissolving ingredients except glucose and yeast extract, adjusting pH to 2.5, autoclaving, and adding glucose plus yeast extract from sterile stocks after autoclaving.
- Direct DSMZ normalized record `data/normalized_yaml/bacterial/acidicaldus_medium.yaml`: preserves the DSMZ ingredient masses, pH 2.5, and the complete post-autoclave glucose/yeast-extract preparation step.
- KOMODO normalized record `data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml`: contains the same seven mass ingredients copied from DSMZ Medium 1038, but it has no `preparation_steps`.

## Completeness

The generated target preserves the DSMZ mass formula and pH, and the DSMZ/KOMODO merge itself correctly recognizes the source duplicate. It drops both the source water line and the OXOID yeast-extract brand, which are minor omissions for the mass recipe.

It is incomplete for preparation. DSMZ explicitly makes glucose and yeast extract post-autoclave additions from sterile stock solutions; the generated target has no `preparation_steps`, so consumers cannot recover the source's heat-treatment order from this merged view.

## Findings

- MAJOR: Merge generation selected the KOMODO duplicate as the top-level record and dropped the DSMZ `preparation_steps`. The omitted DSMZ instruction changes the protocol: glucose and yeast extract are not to be autoclaved in the basal medium, but the generated record has no preparation text at all.
- MINOR: The generated record exposes `komodo.medium:1038` as its primary `media_term` even though the merge metadata marks direct DSMZ Medium 1038 as the `parent_media`. This makes the derivative KOMODO entry look canonical and hides the DSMZ URL that contains the missing preparation instructions.

## Recommended Edits

- Adjust source-duplicate merge selection or field union logic so DSMZ direct records win over KOMODO DSMZ-resolver children when both are merged.
- Regenerate `data/merge_yaml/merged/ACIDICALDUS_MEDIUM.yaml` from `data/normalized_yaml/bacterial/acidicaldus_medium.yaml`, preserving its DSMZ `media_term`, DSMZ notes, pH 2.5, seven non-water ingredients, and post-autoclave glucose/yeast-extract `preparation_steps`.
- Optionally preserve `Yeast extract (OXOID)` in the DSMZ normalized ingredient `preferred_term` so the generated record retains the vendor qualifier from Medium 1038.

## Follow-up Checks

- After merge regeneration, confirm `ACIDICALDUS_MEDIUM.yaml` still lists both `KOMODO_1038_ACIDICALDUS_medium` and `acidicaldus_medium` in `merged_from`.
- Confirm the regenerated target carries `mediadive.medium:1038` as the displayed source and contains the DSMZ post-autoclave preparation step.
- Re-run an ignored-inclusive exact search for `mediadive.medium:1038` and `komodo.medium:1038` to verify no same-source split was introduced.

## Additional Notes

No same-name TOGO duplicate was found in the ignored-inclusive local name search. The only ACIDICALDUS MEDIUM normalized sources found were the DSMZ Medium 1038 import and the KOMODO Medium 1038 DSMZ-resolver duplicate.
