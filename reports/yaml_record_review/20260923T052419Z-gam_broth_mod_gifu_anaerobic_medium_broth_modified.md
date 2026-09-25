# YAML Record Review: GAM Broth, mod. (Gifu Anaerobic Medium Broth, modified)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/gam_broth_mod_gifu_anaerobic_medium_broth_modified.yaml
- Started UTC: 2026-09-23T05:23:37Z
- Finished UTC: 2026-09-23T05:24:19Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:015348`, `gam_broth_mod_gifu_anaerobic_medium_broth_modified`, category `specialized`, for DSMZ Medium 1715 / MediaDive `mediadive.medium:1715`.

The generated file has one source, `gam_broth_mod_gifu_anaerobic_medium_broth_modified`, and merge fingerprint `8caace555cf6c064ded6d05948618e5bd3f561f6cea5adc200255daf07099c38`; future YAML edits belong in `data/normalized_yaml/specialized/gam_broth_mod_gifu_anaerobic_medium_broth_modified.yaml`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gam_broth_mod_gifu_anaerobic_medium_broth_modified.yaml` | Passed with `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/gam_broth_mod_gifu_anaerobic_medium_broth_modified.yaml --out /private/tmp/gam_broth_mod_gifu_anaerobic_medium_broth_modified.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and no error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/gam_broth_mod_gifu_anaerobic_medium_broth_modified.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed. |
| `linkml-term-validator validate-data data/merge_yaml/merged/gam_broth_mod_gifu_anaerobic_medium_broth_modified.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository documents `just validate-history` for standalone files under `history/`, not for generated `MediaRecipe.curation_history` entries. |

## Identity and Grounding

MediaDive REST resolves medium `1715` to DSMZ `GAM Broth, mod. (Gifu Anaerobic Medium Broth, modified)` and the DSMZ Medium 1715 PDF. The PDF title uses the same DSMZ medium number and label.

An ignored-file-inclusive search over `data/normalized_yaml` and `data/merge_yaml/merged` for `mediadive.medium:1715`, `CultureMech:015348`, and `gam_broth_mod_gifu_anaerobic_medium_broth_modified` found only this normalized specialized source, this generated merge, and generated indexes. It did not find a second generated recipe for DSMZ 1715 in that scope.

`GAM Broth mod. powder` is a commercial dehydrated medium and is correctly left without a chemical CHEBI grounding.

## Evidence

DSMZ Medium 1715 and MediaDive agree on a one-liter liquid recipe:

| Ingredient | Source amount | Generated August value | Current normalized value |
|---|---:|---:|---:|
| GAM Broth mod. powder (HyServe) | 41.7 g | `GAM Broth mod. powder`, 41.7 g/L | `GAM Broth mod. powder (HyServe)`, 41.7 g/L |
| Deionized water | to 1000 ml | absent | 1.0 L |

The current normalized YAML, repaired on 2026-09-07 by `repair_dsmz_products_score40.py`, also splits the source preparation into a heat-to-dissolve step and an autoclave step at 115 C for 15 minutes, adds explicit `sterilization`, and references the DSMZ PDF. Those fields are absent from the stale generated merge.

## Completeness

The generated August merge is incomplete relative to both the source PDF and the current maintained normalized source. It lacks the deionized-water row, HyServe supplier qualifier, explicit sterilization metadata, data-quality flags, and DSMZ PDF reference.

The DSMZ 1715 source has no pH value, atmosphere, stock solution, or organism-specific growth claim to represent, so those fields are not missing.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The generated merge predates the maintained September repair. | The generated record has one unqualified powder row and one combined preparation step; the normalized source has the 2026-09-07 `RESOLVED_DSMZ_PRODUCT_SCORE40_GRAPH` curation with water, the HyServe qualifier, references, sterilization, and split steps. | Regenerate from `data/normalized_yaml/specialized/gam_broth_mod_gifu_anaerobic_medium_broth_modified.yaml`. |
| Major | The generated record omits the deionized-water ingredient. | DSMZ and MediaDive both bring the 41.7 g powder to 1000 ml with deionized water; the generated merge has no water row. | Regenerate from `data/normalized_yaml/specialized/gam_broth_mod_gifu_anaerobic_medium_broth_modified.yaml`. |
| Minor | The generated powder row omits the HyServe supplier qualifier. | DSMZ names `GAM Broth mod. powder (HyServe)` and MediaDive stores `attribute: HyServe`; the generated row says only `GAM Broth mod. powder`. | Regenerate from `data/normalized_yaml/specialized/gam_broth_mod_gifu_anaerobic_medium_broth_modified.yaml`. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/gam_broth_mod_gifu_anaerobic_medium_broth_modified.yaml` from the repaired normalized specialized source.
2. Verify the regenerated record keeps the `GAM Broth mod. powder (HyServe)` label, deionized water to 1 L, heat and autoclave steps, `sterilization`, `references`, and quality flags.

## Follow-up Checks

After regeneration, rerun focused schema, strict, reference, and term validation on `data/merge_yaml/merged/gam_broth_mod_gifu_anaerobic_medium_broth_modified.yaml`.

Manually compare the regenerated output against:

- MediaDive REST `https://mediadive.dsmz.de/rest/medium/1715`
- DSMZ `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1715.pdf`

## Additional Notes

No source-identity duplicate, stock-solution flattening, or duplicate-ingredient arithmetic issue was found for DSMZ 1715.
