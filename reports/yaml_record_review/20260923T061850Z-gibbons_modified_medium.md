# YAML Record Review: gibbons_modified_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/gibbons_modified_medium.yaml
- Started UTC: 2026-09-23T06:17:27Z
- Finished UTC: 2026-09-23T06:18:50Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:015876` is the direct JCM GRMD import for JCM 1477, `GIBBONS MODIFIED MEDIUM`.

The generated record derives from `data/normalized_yaml/bacterial/JCM_J1477_GIBBONS_MODIFIED_MEDIUM.yaml`. An ignored-file-inclusive exact search for `jcm.grmd:1477`, `GRMD=1477`, and `JCM_J1477_GIBBONS_MODIFIED_MEDIUM` found only that maintained source row, this generated record, and normalized source indexes.

## Validation

`linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gibbons_modified_medium.yaml` passed.

`scripts/validate_strict.py data/merge_yaml/merged/gibbons_modified_medium.yaml --workers 1 --quiet` passed with 0 error rows.

`linkml-reference-validator validate data data/merge_yaml/merged/gibbons_modified_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` passed with 0 checks.

`linkml-term-validator validate-data data/merge_yaml/merged/gibbons_modified_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `jcm.grmd:1477` identity, label, category, complex/undefined classification, agar physical state, and pH 7.5 agree with the live JCM 1477 `GIBBONS MODIFIED MEDIUM` page.

The Casamino acids, yeast extract, and Bacto peptone rows are complex BD-Difco products and are correctly left without single small-molecule CHEBI groundings.

The simple KCl, MgSO4 x 7H2O, NaCl, agar, and water groundings are appropriate. `Trisodium citrate x 2H2O` is grounded to generic `CHEBI:53258` sodium citrate, which loses the hydrate text but is not as severe as grounding to a different ingredient.

## Evidence

JCM 1477 lists 10 g Casamino acids, 5 g trisodium citrate dihydrate, 10 g yeast extract, 5 g Bacto peptone, 2 g KCl, 2 g MgSO4 x 7H2O, 30 g NaCl, 15 g agar, and 1 L distilled water.

The generated record preserves all nine rows in source order and preserves the single preparation instruction to adjust pH to 7.5.

## Completeness

The source's 1 L distilled-water row is present but recoded as `1.0 ML_PER_L`, which is dimensionally wrong for a one-liter solvent row.

No preparation detail, stock recipe, atmosphere, or variant from the live JCM 1477 page is missing.

Empty growth-evidence, discussion, and publication slots are acceptable for this direct source recipe.

## Findings

- Major: Distilled water was recoded from the source's `1.0 L` row to `1.0 ML_PER_L`, so the generated record under-represents the solvent volume by 1000-fold and uses a final-concentration unit for a source volume.
- Minor: Trisodium citrate x 2H2O is grounded to generic sodium citrate rather than a hydrate-specific term.

## Recommended Edits

- Correct the water row in `data/normalized_yaml/bacterial/JCM_J1477_GIBBONS_MODIFIED_MEDIUM.yaml` to preserve 1 L of distilled water or an equivalent 1000 ml representation.
- Re-ground trisodium citrate dihydrate if a precise term is available; otherwise keep the exact source string explicit.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/gibbons_modified_medium.yaml` and confirm the water row is no longer `1.0 ML_PER_L`.
- Confirm the generated record still has exactly the eight non-water JCM ingredients and the pH 7.5 preparation instruction.
- Re-run LinkML, strict, reference, and term validation on the regenerated generated YAML.

## Additional Notes

The exact source search used `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged`, so ignored generated records and index files were included.
