# YAML Record Review: germination_medium_for_sordaria_fimicola__b919d736

- Repository: CultureMech
- Record: data/merge_yaml/merged/germination_medium_for_sordaria_fimicola__b919d736.yaml
- Started UTC: 2026-09-23T06:09:51Z
- Finished UTC: 2026-09-23T06:11:54Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:002511` is the direct MediaDive/JCM import for JCM 152, `GERMINATION MEDIUM FOR SORDARIA FIMICOLA`.

The generated record derives from `data/normalized_yaml/bacterial/germination_medium_for_sordaria_fimicola.yaml`. An ignored-file-inclusive exact search for `mediadive.medium:J152`, `JCM_M152`, and `GRMD=152'` also found the equivalent Togo M143 import in `data/normalized_yaml/bacterial/TOGO_M143_Germination_Medium_For_Sordaria_Fimicola.yaml` and `data/merge_yaml/merged/GERMINATION_MEDIUM_FOR_SORDARIA_FIMICOLA.yaml`.

## Validation

`linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/germination_medium_for_sordaria_fimicola__b919d736.yaml` passed.

`scripts/validate_strict.py data/merge_yaml/merged/germination_medium_for_sordaria_fimicola__b919d736.yaml --workers 1 --quiet` passed with 0 error rows.

`linkml-reference-validator validate data data/merge_yaml/merged/germination_medium_for_sordaria_fimicola__b919d736.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` passed with 0 checks.

`linkml-term-validator validate-data data/merge_yaml/merged/germination_medium_for_sordaria_fimicola__b919d736.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `mediadive.medium:J152` identity matches the MediaDive archival payload for JCM 152. The live JCM 152 URL now returns `Nothing found`, so it cannot independently confirm the formula.

The source name denotes a Sordaria fimicola germination medium; Sordaria fimicola is fungal, but the maintained input and generated record are under `category: bacterial`.

The sucrose, glucose, sodium acetate, and agar groundings are appropriate. `Corn meal agar` is a BD-Difco complex ingredient in MediaDive and a `Corn meal agar (BD-Difco)` complex component in Togo, but the direct MediaDive branch grounds it to `CHEBI:2509` agar.

## Evidence

MediaDive J152 represents one 1000 ml main solution with 4 g Corn meal agar, attribute BD-Difco; 30 g sucrose; 20 g glucose; 2 g sodium acetate; 20 g agar; and 1000 ml distilled water.

Togo M143 archives the same JCM_M152 source and carries the same substantive formula, including a distinct ungrounded `Corn meal agar (BD-Difco)` row.

The generated direct MediaDive record has the five non-water recipe rows and no preparation steps, matching the limited MediaDive J152 payload aside from water elision and the corn-meal-agar grounding.

## Completeness

The 1000 ml distilled-water row is absent from the generated direct MediaDive record.

The equivalent Togo M143 import is not merged with this direct MediaDive J152 generated record.

Empty preparation, pH, growth-evidence, variant, discussion, and publication slots are acceptable for the archived JCM formula because MediaDive and Togo do not expose those claims for JCM 152.

## Findings

- Major: `Corn meal agar` is grounded to plain agar, conflating the 4 g/L BD-Difco corn meal agar component with the separate 20 g/L agar solidifier.
- Major: The Sordaria fimicola germination medium is filed under `data/normalized_yaml/bacterial` and `category: bacterial` despite denoting a fungal target medium.
- Major: The direct MediaDive/JCM record is split from the equivalent Togo M143 import.
- Major: The 1000 ml distilled-water row is absent from the direct MediaDive branch and generated record.

## Recommended Edits

- In `data/normalized_yaml/bacterial/germination_medium_for_sordaria_fimicola.yaml`, leave `Corn meal agar` ungrounded or ground it to a product-specific complex-medium term rather than `CHEBI:2509`.
- Move or recategorize the MediaDive J152 and Togo M143 normalized inputs as fungal records if the repository supports JCM fungal recipes outside `data/normalized_yaml/bacterial`.
- Preserve the 1000 ml distilled-water row as formulation context.
- Align the MediaDive J152 and Togo M143 normalized rows so regeneration merges or explicitly cross-links the two archives of JCM_M152.

## Follow-up Checks

- Regenerate the merged JCM 152 outputs and confirm there are no two `CHEBI:2509` rows for corn meal agar and agar.
- Confirm the corrected record retains an explicit 1000 ml water row and is no longer categorized as bacterial.
- Re-run LinkML, strict, reference, and term validation on the regenerated generated YAML.
- Re-run an ignored-file-inclusive exact search for `mediadive.medium:J152`, `JCM_M152`, and `TOGO:M143` to confirm the two source imports no longer produce split equivalent generated records.

## Additional Notes

The exact source search used `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged`, so ignored generated records and index files were included.
