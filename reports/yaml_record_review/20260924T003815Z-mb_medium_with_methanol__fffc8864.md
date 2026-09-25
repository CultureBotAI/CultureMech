# YAML Record Review: MB MEDIUM WITH METHANOL

- Repository: CultureMech
- Record: `data/merge_yaml/merged/mb_medium_with_methanol__fffc8864.yaml`
- Started UTC: 2026-09-24T00:37:33Z
- Finished UTC: 2026-09-24T00:38:14Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/mb_medium_with_methanol__fffc8864.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:003032`
- Name: `mb_medium_with_methanol`
- Original name: `MB MEDIUM WITH METHANOL`
- Source accession: `mediadive.medium:J687`, labeled `MB MEDIUM WITH METHANOL`
- Maintained owner for future fixes: `data/normalized_yaml/bacterial/mb_medium_with_methanol.yaml`
- Generated status: generated canonical merge of one normalized record. The generated file matches the direct normalized owner, including the empty methanol `solutions:` placeholder.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mb_medium_with_methanol__fffc8864.yaml` exited 0 with `No issues found`. |
| Strict schema | Passed. `scripts/validate_strict.py data/merge_yaml/merged/mb_medium_with_methanol__fffc8864.yaml --out /private/tmp/mb_medium_with_methanol__fffc8864.strict.tsv --workers 1 --quiet` scanned 1 file with 0 error rows; the TSV was header-only. |
| References | Passed. `linkml-reference-validator validate data data/merge_yaml/merged/mb_medium_with_methanol__fffc8864.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` exited 0 with 0 checks and no failures. |
| Terms | Passed. `linkml-term-validator validate-data data/merge_yaml/merged/mb_medium_with_methanol__fffc8864.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. It emitted the expected `eutils` `pkg_resources` warning before reporting `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The record denotes JCM/MediaDive J687, `MB MEDIUM WITH METHANOL`. The `media_term`, source link, and MediaDive J687 REST payload all agree with the live JCM `GRMD=687` page.

The basal Solution A salts and complex nutrients are recognizable, but the stock boundary is not. JCM 687 explicitly lists 10 ml trace minerals, 1 ml selenite-tungstate solution, 50 ml Methanol solution, 10 ml trace vitamins, 5 ml 5 percent `L-Cysteine HCl x H2O`, and 5 ml 5 percent `Na2S x 9 H2O` as solution additions; the normalized owner flattens those stocks into root ingredients.

The `TOGO:M707` sibling is a same-source import of JCM 687 and was inspected as a corroborating source lead. It has the same stock-boundary defect pattern and is not merged into this canonical JCM record.

## Evidence

### Supported

- The live JCM 687 page and MediaDive J687 JSON support the source identity.
- JCM 687 supports the Solution A root quantities for 10 g NaCl, 2 g yeast extract, 2 g Trypticase peptone, 1 g NH4Cl, 1 g `MgCl2 x 6 H2O`, 0.5 g KCl, 0.4 g `CaCl2 x 2 H2O`, 0.4 g `K2HPO4`, 0.5 mg resazurin, 4 g `NaHCO3`, and 920 ml distilled water.
- JCM 687 supports 10 ml/L trace minerals from Medium 151, 1 ml/L selenite-tungstate solution from Medium 431, 50 ml/L Methanol solution, 10 ml/L trace vitamins from Medium 197, and 5 ml/L each of sterile 5 percent `L-Cysteine HCl x H2O` and 5 percent `Na2S x 9 H2O`.
- MediaDive J687 supports the Methanol solution as its own stock containing 2.28 ml methanol plus 50 ml distilled water.

### Unsupported or over-scoped

- The trace-mineral ingredients are stock ingredients, not root final-medium ingredients. Flattening that stock also caused the basal and trace-mineral NaCl values to be merged into one 10.99001 `G_PER_L` root ingredient and the basal and trace-mineral calcium chloride values to be merged into one 0.49960000000000004 `G_PER_L` root ingredient.
- The selenite-tungstate ingredients are stock ingredients, not direct root ingredients.
- The record stores `Methanol` as 2.28 `G_PER_L`; the source stock uses 2.28 ml methanol plus 50 ml water and is added at 50 ml/L.
- `Trace vitamins (see Medium No. 197)` is a 10 ml/L stock addition, not a 10 `G_PER_L` root ingredient.
- `L-Cysteine HCl x H2O` and `Na2S x 9 H2O` are 5 percent solutions added at 5 ml/L, not 5 `G_PER_L` root ingredients.
- The Trace minerals pH adjustment is a stock preparation step, not a root medium pH step.

## Completeness

- A gitignore-independent exact field scan of `data/merge_yaml/merged/mb_medium_with_methanol__fffc8864.yaml`, `data/normalized_yaml/bacterial/mb_medium_with_methanol.yaml`, and `data/normalized_yaml/bacterial/TOGO_M707_MB_Medium_With_Methanol.yaml` found no top-level `references:` or `target_organisms:` slots in the generated JCM file or its direct normalized owner.
- The generated and owner records have a `solutions:` slot, but it contains only an empty `Methanol solution (see below)` placeholder with `50 G_PER_L`; that misses its methanol and water composition and uses the wrong unit for the 50 ml/L addition.
- Missing `references:` is a minor provenance gap. The JCM source URL is present in `notes`, but a structured reference to JCM 687, JCM 151, JCM 431, and JCM 197 would make the stock recipes recoverable.
- Missing `target_organisms:` is acceptable. The inspected JCM 687 and MediaDive J687 sources did not assert a specific taxon growth result.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Stock solution ingredients were flattened into root final-medium ingredients. | JCM and MediaDive encode trace minerals, selenite-tungstate solution, Methanol solution, trace vitamins, 5 percent cysteine, and 5 percent sulfide as additions to Solution A. The record stores most stock members under root `ingredients` and merges duplicated NaCl and calcium chloride into root amounts. | `data/normalized_yaml/bacterial/mb_medium_with_methanol.yaml` |
| major | The only `solutions:` entry is empty and unit-misencoded. | The record stores `Methanol solution (see below)` as an unknown solution with empty `composition` and `50 G_PER_L`; MediaDive J687 gives a 50 ml/L addition of a stock made from 2.28 ml methanol and 50 ml distilled water. | `data/normalized_yaml/bacterial/mb_medium_with_methanol.yaml` |
| minor | `MnSO4 x n H2O` has a primary CHEBI term but no `mediaingredientmech_chebi_term` mirror. | The normalized and generated records include `term: CHEBI:86360` for this ingredient but no CHEBI-keyed MediaIngredientMech link, unlike the neighboring mineral salts. | `data/normalized_yaml/bacterial/mb_medium_with_methanol.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/mb_medium_with_methanol.yaml`, keep the JCM 687 Solution A table as root ingredients and move trace minerals, selenite-tungstate solution, Methanol solution, trace vitamins, 5 percent cysteine, and 5 percent sulfide into `solutions:` with ML_PER_L addition amounts.
2. Populate Methanol solution with 2.28 ml methanol plus 50 ml distilled water, added at 50 ml/L.
3. Encode trace minerals from JCM 151, selenite-tungstate solution from JCM 431, and trace vitamins from JCM 197 under `solutions:` instead of root `ingredients`.
4. Scope the trace-minerals pH adjustment to the Trace minerals stock.
5. Add the CHEBI-keyed `mediaingredientmech_chebi_term` mirror for `MnSO4 x n H2O` only if the packaged MIM label index resolves that exact variable-hydrate label to the same checked identity.

## Follow-up Checks

- Run open schema, strict schema, reference, and term validation on the corrected normalized owner.
- Regenerate the merged YAML and verify the generated `mb_medium_with_methanol__fffc8864.yaml` preserves the stock boundaries and no longer merges Solution A salts with trace-mineral stock salts.
- Manually compare the regenerated record against JCM 687, JCM 151, JCM 431, JCM 197, and MediaDive J687.
- Recheck `data/normalized_yaml/bacterial/TOGO_M707_MB_Medium_With_Methanol.yaml` after the direct JCM owner is corrected because it has the same empty cross-reference solution placeholders.

## Additional Notes

- The live JCM 687 page, live MediaDive J687 JSON, and live TOGO M707 API response were inspected for this review. JCM 151, 431, and 197 were also inspected during the adjacent J688 review and provide the stock formulas referenced by JCM 687.
- This review did not patch generated YAML, normalized YAML, or GitHub state.
