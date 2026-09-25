# YAML Record Review: marine_agar_broth_2216_3_nacl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_agar_broth_2216_3_nacl.yaml
- Started UTC: 2026-09-23T23:30:42Z
- Finished UTC: 2026-09-23T23:31:31Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/marine_agar_broth_2216_3_nacl.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:009579` |
| Name | `marine_agar_broth_2216_3_nacl` |
| Original name | `Marine Agar/Broth 2216 + 3 % NaCl` |
| Media term | `TOGO:M3064` |
| Source lineage | TOGO M3064 imported from NBRC Medium 1644 |
| Generated status | Derived merged output under `data/merge_yaml/merged/` |
| Maintained 3% owner | `data/normalized_yaml/bacterial/marine_agar_broth_2216_3_nacl.yaml` |
| Maintained 10% child | `data/normalized_yaml/bacterial/marine_agar_broth_2216_10_nacl.yaml` |
| Merge code owner | `src/culturemech/merge/` |

An exact gitignore-independent search for `marine_agar_broth_2216_3_nacl`, `Marine Agar/Broth 2216 + 3 % NaCl`, `TOGO:M3064`, `NBRC_M1644`, `NO=1644`, and `CultureMech:009579` covered `data/normalized_yaml/bacterial`, `data/merge_yaml/merged`, the ID registry, the recipe catalog, `reports/media_content_review_manifest.tsv`, and `data/import_tracking/reports`. It found the maintained 3% owner, the generated target, its ID registry/catalog rows, and the media-content manifest row.

The review also checked the linked salinity child with an exact gitignore-independent search for `marine_agar_broth_2216_10_nacl`, `Marine Agar/Broth 2216 + 10 % NaCl`, `TOGO:M2112`, `NBRC_M1436`, `NO=1436`, and `CultureMech:008705` across the same paths. That found the 10% maintained owner and the stale merge edges inside the reviewed generated target.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_agar_broth_2216_3_nacl.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_agar_broth_2216_3_nacl.yaml --out /private/tmp/marine_agar_broth_2216_3_nacl.strict.tsv --workers 1 --quiet` | Passed: one file scanned, zero files with `ERROR`, zero total `ERROR` rows. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_agar_broth_2216_3_nacl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero PMID/DOI evidence checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_agar_broth_2216_3_nacl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Maintained 3% owner open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/normalized_yaml/bacterial/marine_agar_broth_2216_3_nacl.yaml` | Passed: `No issues found`. |
| Maintained 3% owner strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/normalized_yaml/bacterial/marine_agar_broth_2216_3_nacl.yaml --out /private/tmp/marine_agar_broth_2216_3_nacl.normalized.strict.tsv --workers 1 --quiet` | Passed: one file scanned, zero files with `ERROR`, zero total `ERROR` rows. |
| Embedded `curation_history` | `just validate-history` | Not checked: repository history validation targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` arrays. |

## Identity and Grounding

TOGO M3064 identifies the source as `NBRC_M1644`, names the recipe Marine Agar/Broth 2216 + 3 % NaCl, links the NBRC Medium 1644 page, and reports pH 7.5-8.0. The live NBRC 1644 page has the same medium number and name. The target ID and media term therefore identify the intended 3% NaCl NBRC recipe.

The generated record no longer denotes only that recipe. It merges `marine_agar_broth_2216_3_nacl` with `marine_agar_broth_2216_10_nacl`, advertises the 3% NBRC 1644 identity, but contains `NaCl` at `100 G_PER_L`, which is the NBRC 1436 / TOGO M2112 10% child amount. NBRC 1644 and TOGO M3064 both give 30 g NaCl per 1 L.

The water row has the right material identity but the wrong unit dimension in both the generated target and the maintained normalized owner: NBRC 1644 and TOGO M3064 report 1 L distilled water, not `1 G_PER_L`. The generated and normalized 3% records also omit the source pH range.

## Evidence

Supported claims:

- TOGO M3064 and NBRC 1644 support the 3% recipe identity.
- NBRC 1644 supports 37.4 g Bacto Marine Broth 2216 (Difco), 30 g NaCl, optional 15 g agar, and 1 L distilled water.
- TOGO M3064 preserves the same four rows and the pH comment.
- NBRC 1436 and TOGO M2112 support the related 10% child recipe with the same non-NaCl rows and 100 g NaCl.
- The source pages support modeling the 10% record as a salinity variant of the 3% record; the normalized parent and child already carry reciprocal `SALINITY_VARIANT` references.

Unsupported or stale claims:

- `ingredients[1].concentration.value: "100"` is unsupported in a record labeled and grounded as the 3% recipe.
- `ingredients[0].concentration.unit: G_PER_L` is unsupported for the water row.
- The generated `merged_from` set is source-conflating for publication: the 3% and 10% records differ by NaCl amount and should remain distinct canonical merged records.

## Completeness

Consequential gaps remain in the maintained 3% owner and flow through to the generated target:

- no `ph_range` for the pH 7.5-8.0 line in NBRC 1644 and TOGO M3064;
- water is still normalized as mass per liter rather than a 1 L final-volume row;
- `Agar (if needed)` is explicit but ungrounded despite the source exposing the agar identity through TOGO.

The unresolved Bacto Marine Broth 2216 (Difco) commercial component is acceptable as explicit text; it should not be forced to a narrow CHEBI chemical.

No `target_organisms` or PMID/DOI evidence claims are present. The inspected NBRC and TOGO pages establish the medium recipe but do not make a strain-specific growth claim.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The generated merge conflates a 3% NaCl parent with its 10% NaCl salinity child and publishes the 10% NaCl quantity under the 3% identity. | NBRC 1644 / TOGO M3064 give 30 g NaCl, while NBRC 1436 / TOGO M2112 give 100 g NaCl. The generated output merged both normalized records on fingerprint `340df8a51923e01a31b62a415de4579b0e32e6d7226569f44d4522c4521443a6` and selected `100 G_PER_L`. | `src/culturemech/merge/` should keep concentration-changing `SALINITY_VARIANT` records distinct in `data/merge_yaml/merged/`; regenerate merged outputs after the rule change. |
| Major | The generated and maintained 3% water row uses `1 G_PER_L` for a final-volume row. | NBRC 1644 and TOGO M3064 give distilled water as 1 L. | `data/normalized_yaml/bacterial/marine_agar_broth_2216_3_nacl.yaml`; make the same correction in `data/normalized_yaml/bacterial/marine_agar_broth_2216_10_nacl.yaml` because NBRC 1436 also gives 1 L. |
| Major | The source pH range is missing. | NBRC 1644 and TOGO M3064 both carry pH 7.5-8.0. | Add `ph_range` to `data/normalized_yaml/bacterial/marine_agar_broth_2216_3_nacl.yaml`. |
| Minor | The optional agar row is ungrounded. | TOGO M3064 maps `Agar (if needed)` to its agar GMO component, and the row is chemically groundable while preserving the optional text. | Ground `Agar (if needed)` in `data/normalized_yaml/bacterial/marine_agar_broth_2216_3_nacl.yaml` and `data/normalized_yaml/bacterial/marine_agar_broth_2216_10_nacl.yaml`. |

## Recommended Edits

1. Update the merge pipeline so concentration-only salinity variants are not deduplicated as identical canonical formulas, then regenerate `data/merge_yaml/merged/`.
2. Correct the NBRC 1644 normalized owner to use the source-supported 30 g/L NaCl value, a 1 L water row represented with an appropriate volume unit, the pH 7.5-8.0 range, and a grounded but still optional agar component.
3. Correct the NBRC 1436 10% normalized child to keep the source-supported 100 g/L NaCl value while fixing the 1 L water row and grounding optional agar.
4. Keep the reciprocal `SALINITY_VARIANT` links between the 3% and 10% normalized records; they describe a real source relationship and should be validated after the content fixes.

## Follow-up Checks

- Rerun focused open-schema, strict, term, and reference validation on both normalized records and on the regenerated generated outputs.
- Run `just validate-media-variant-links` to verify the 3% and 10% salinity pair still link reciprocally.
- Run `just verify-merges` and `just audit-merge-freshness` after changing `src/culturemech/merge/`.
- Manually re-open TOGO M3064, NBRC 1644, TOGO M2112, and NBRC 1436 after regeneration to confirm the 30 g and 100 g NaCl values remain separated.

## Additional Notes

- The exact gitignore-independent searches listed under Target included ignored files in the scoped paths and were sufficient to resolve the 3% owner, the 10% child, their source IDs, and the stale generated merge.
- A broader interrupted exploratory search also ran while resolving this record; it was not used for negative findings or source conclusions in this report.
