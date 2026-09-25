# YAML Record Review: GAM Broth (Gifu Anaerobic Medium Broth)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/gam_broth_gifu_anaerobic_medium_broth.yaml
- Started UTC: 2026-09-23T05:21:56Z
- Finished UTC: 2026-09-23T05:22:48Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:015347`, `gam_broth_gifu_anaerobic_medium_broth`, category `specialized`, for DSMZ Medium 1713 / MediaDive `mediadive.medium:1713`.

The generated file has one source, `gam_broth_gifu_anaerobic_medium_broth`, and merge fingerprint `7925c898dc565a37ab284e1741822242c2294d80a76c28602bfb84712ad3f991`; future YAML edits belong in `data/normalized_yaml/specialized/gam_broth_gifu_anaerobic_medium_broth.yaml`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gam_broth_gifu_anaerobic_medium_broth.yaml` | Passed with `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/gam_broth_gifu_anaerobic_medium_broth.yaml --out /private/tmp/gam_broth_gifu_anaerobic_medium_broth.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and no error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/gam_broth_gifu_anaerobic_medium_broth.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator reported zero checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/gam_broth_gifu_anaerobic_medium_broth.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository documents `just validate-history` for standalone files under `history/`, not for generated `MediaRecipe.curation_history` entries. |

## Identity and Grounding

MediaDive REST resolves medium `1713` to DSMZ `GAM Broth (Gifu Anaerobic Medium Broth)` and the DSMZ Medium 1713 PDF. The PDF title is also `1713. GAM Broth (Gifu Anaerobic Medium Broth)`.

An ignored-file-inclusive search over `data/normalized_yaml` and `data/merge_yaml/merged` for `mediadive.medium:1713`, `CultureMech:015347`, and `gam_broth_gifu_anaerobic_medium_broth` found only this normalized specialized source, this generated merge, and generated indexes. It did not find a duplicate generated record for DSMZ 1713 in that scope.

The commercial GAM Broth powder is correctly left without a chemical CHEBI grounding; the source names a product powder, not a defined compound.

## Evidence

DSMZ Medium 1713 and MediaDive agree on a one-liter liquid recipe:

| Ingredient | Source amount | Generated August value | Current normalized value |
|---|---:|---:|---:|
| GAM Broth powder (HyServe) | 59 g | `GAM Broth powder`, 59 g/L | `GAM Broth powder (HyServe)`, 59 g/L |
| Deionized water | to 1000 ml | absent | 1.0 L |

The generated record also keeps the source preparation as one combined `DISSOLVE` step. The current normalized YAML, repaired on 2026-09-07 by `repair_dsmz_products_score40.py`, splits that source text into a heat-to-dissolve step plus an autoclave step at 115 C for 15 minutes and adds explicit `sterilization` metadata.

## Completeness

The generated August merge is stale relative to `data/normalized_yaml/specialized/gam_broth_gifu_anaerobic_medium_broth.yaml`. The normalized source now contains the HyServe qualifier, deionized-water ingredient, DSMZ PDF reference, quality flags, split preparation steps, and sterilization block that would make the record substantially complete after regeneration.

No pH, temperature, atmosphere, stock solution, or organism-specific growth claims are present in the DSMZ 1713 source or needed in this generated record.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The generated merge predates a maintained normalized repair. | The generated record still has one unqualified `GAM Broth powder` ingredient and one combined preparation step; the normalized source has the 2026-09-07 `RESOLVED_DSMZ_PRODUCT_SCORE40_GRAPH` curation with water, the HyServe qualifier, references, sterilization, and split steps. | Regenerate from `data/normalized_yaml/specialized/gam_broth_gifu_anaerobic_medium_broth.yaml`. |
| Major | The generated ingredient list omits deionized water. | DSMZ and MediaDive both bring the powder to 1000 ml with deionized water; the generated merged record has no water row. | Regenerate from `data/normalized_yaml/specialized/gam_broth_gifu_anaerobic_medium_broth.yaml`. |
| Minor | The generated powder row omits the HyServe supplier qualifier. | DSMZ names `GAM Broth powder (HyServe)` and MediaDive stores `attribute: HyServe`; the generated merged row says only `GAM Broth powder`. | Regenerate from `data/normalized_yaml/specialized/gam_broth_gifu_anaerobic_medium_broth.yaml`. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/gam_broth_gifu_anaerobic_medium_broth.yaml` from the repaired normalized specialized source.
2. After regeneration, confirm the merged record keeps the `GAM Broth powder (HyServe)` label, deionized water to 1 L, the heat and autoclave steps, `sterilization`, `references`, and the existing `data_quality_flags`.

## Follow-up Checks

After regeneration, rerun focused schema, strict, reference, and term validation on `data/merge_yaml/merged/gam_broth_gifu_anaerobic_medium_broth.yaml`.

Manually compare the regenerated output against:

- MediaDive REST `https://mediadive.dsmz.de/rest/medium/1713`
- DSMZ `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1713.pdf`

## Additional Notes

No stock-solution flattening, duplicate-ingredient merge, or source-identity conflict was found.
