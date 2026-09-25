# YAML Record Review: marine_ammonium_mineral_salts

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_ammonium_mineral_salts__742d01b7.yaml
- Started UTC: 2026-09-23T23:36:53Z
- Finished UTC: 2026-09-23T23:37:38Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/marine_ammonium_mineral_salts__742d01b7.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:015337` |
| Name | `marine_ammonium_mineral_salts` |
| Original name | `MARINE AMMONIUM MINERAL SALTS` |
| Media term | `mediadive.medium:1313` |
| Source lineage | DSMZ Medium 1313 via MediaDive |
| Generated status | Derived merged output under `data/merge_yaml/merged/` |
| Maintained DSMZ owner | `data/normalized_yaml/specialized/marine_ammonium_mineral_salts.yaml` |

An exact gitignore-independent search for `marine_ammonium_mineral_salts`, `medium_1313_modified_for_dsm_25384`, `mediadive.medium:1313`, `DSMZ Medium 1313`, `CultureMech:015337`, and `742d01b7` covered `data/normalized_yaml/bacterial`, `data/normalized_yaml/specialized`, `data/merge_yaml/merged`, the ID registry, the recipe catalog, `reports/media_content_review_manifest.tsv`, and `data/import_tracking/reports`. It found the maintained DSMZ owner, the KOMODO DSMZ-derived owners, the reviewed generated target, prior `merged_duplicates.tsv` rows flagging summed `Na2MoO4 x 2 H2O`, and a filename-collision row that classifies the bacterial and specialized `marine_ammonium_mineral_salts.yaml` files as different.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_ammonium_mineral_salts__742d01b7.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_ammonium_mineral_salts__742d01b7.yaml --out /private/tmp/marine_ammonium_mineral_salts__742d01b7.strict.tsv --workers 1 --quiet` | Passed: one file scanned, zero files with `ERROR`, zero total `ERROR` rows. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_ammonium_mineral_salts__742d01b7.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero PMID/DOI evidence checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_ammonium_mineral_salts__742d01b7.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Maintained DSMZ owner open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/normalized_yaml/specialized/marine_ammonium_mineral_salts.yaml` | Passed: `No issues found`. |
| Maintained DSMZ owner strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/normalized_yaml/specialized/marine_ammonium_mineral_salts.yaml --out /private/tmp/marine_ammonium_mineral_salts__742d01b7.normalized.strict.tsv --workers 1 --quiet` | Passed: one file scanned, zero files with `ERROR`, zero total `ERROR` rows. |
| Embedded `curation_history` | `just validate-history` | Not checked: repository history validation targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` arrays. |

## Identity and Grounding

The `mediadive.medium:1313` term resolves to DSMZ Medium 1313, MARINE AMMONIUM MINERAL SALTS, and links the DSMZ Medium 1313 PDF. The generated target's ID and name therefore identify the intended DSMZ medium.

The generated ingredient list does not preserve the source identity of several nested stock solutions. DSMZ Medium 1313 is prepared from 900 ml Solution A, 100 ml Solution B, and 1 ml/litre filter-sterilized Vitamin Solution V10; Solution A also receives 1 ml Trace element solution SL10. The generated copy instead publishes the component rows of Solution A, Solution B, SL10, and V10 as direct `ingredients`, all at stock concentration.

The `Na2MoO4 x 2 H2O` row is a clear symptom: DSMZ lists 0.020 g molybdate in Solution A and 0.036 g molybdate in a separate 1000 ml SL10 stock. The generated direct row is `0.0580431 G_PER_L` with a merged-duplicate note that sums those two source contexts.

## Evidence

Supported claims:

- MediaDive medium 1313 and the DSMZ PDF support the Marine Ammonium Mineral Salts source identity.
- The DSMZ PDF and MediaDive agree that Solution A and Solution B are autoclaved separately and combined after cooling.
- Both sources support adding 1 ml/litre filter-sterilized Vitamin Solution V10.
- Both sources support adjusting Solution A to pH 7.2 with NaOH/HCl if needed.
- Both sources support filter-sterilizing Vitamin Solution V10 and storing it in the dark at 4 C.

Unsupported or over-scoped claims:

- The generated direct ingredient concentrations for SL10 and Vitamin V10 components are unsupported as final-medium g/L concentrations.
- The generated `Na2MoO4 x 2 H2O` amount is a sum of Solution A molybdate and SL10 molybdate rather than either stock concentration or either final-medium contribution.
- The generated `preparation_steps[2]` scopes V10 filter sterilization and dark storage to the root medium, not to the Vitamin Solution V10 stock.

## Completeness

The generated copy is stale relative to `data/normalized_yaml/specialized/marine_ammonium_mineral_salts.yaml`: the maintained owner has an August 2026 `NESTED_FLATTENED_COCKTAIL` curation event that moved six stock-strength rows into `solutions`, while the generated target still has those rows at the root.

The maintained owner is still incomplete. It moved only five Vitamin V10 rows and only one SL10 row into nested stocks, leaving para-aminobenzoic acid, biotin, calcium pantothenate, lipoic acid, folic acid, HCl, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and `Na2MoO4 x 2 H2O` at the root. DSMZ and MediaDive make those V10 or SL10 stock components.

No `target_organisms` or PMID/DOI evidence claims are present. The inspected DSMZ and MediaDive pages are formulation sources, not growth studies.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The generated record denotes DSMZ Medium 1313 but flattens stock solutions into root ingredients at stock strength. | DSMZ and MediaDive define a main solution made from Solution A, Solution B, and Vitamin Solution V10, with nested Trace element solution SL10 inside Solution A. The generated YAML lists SL10 and V10 chemicals directly under `ingredients`. | Finish the nesting repair in `data/normalized_yaml/specialized/marine_ammonium_mineral_salts.yaml`, then regenerate `data/merge_yaml/merged/marine_ammonium_mineral_salts__742d01b7.yaml`. |
| Major | `Na2MoO4 x 2 H2O` merges two distinct source rows into one root ingredient. | DSMZ lists one molybdate amount in Solution A and a second molybdate amount in SL10. `data/import_tracking/reports/merged_duplicates.tsv` already flags `CultureMech:015337` because the current value is a sum of 0.0222222 and 0.0358209 g/L. | Keep the Solution A molybdate and SL10 molybdate in their respective solution contexts in the normalized DSMZ owner. |
| Major | Vitamin V10 and SL10 handling is only partially repaired upstream. | The maintained DSMZ owner has only five V10 components and one SL10 component under `solutions`; the rest of those stock components remain direct root ingredients despite the DSMZ stock headings. | Move every DSMZ V10 component into the `Vitamin Solution V10` solution and every DSMZ SL10 component into `Trace element solution SL10`. |

No minor findings.

## Recommended Edits

1. Complete stock-solution nesting in `data/normalized_yaml/specialized/marine_ammonium_mineral_salts.yaml` so root ingredients describe Solution A, Solution B, and stock additions at their final-medium addition volumes instead of flattening stock composition.
2. Preserve DSMZ's distinction between the Solution A molybdate row and the SL10 molybdate row.
3. Scope the filter-sterilization and dark-storage instruction to Vitamin Solution V10 rather than the root medium.
4. Regenerate `data/merge_yaml/merged/` from the corrected specialized owner and check whether the KOMODO-derived bacterial duplicates still merge cleanly or require source-specific variant handling.

## Follow-up Checks

- Rerun focused open-schema, strict, term, and reference validation on the corrected `data/normalized_yaml/specialized/marine_ammonium_mineral_salts.yaml` and regenerated generated output.
- Rerun `just review-media-content` and confirm the corrected specialized owner no longer emits a `merged_duplicates.tsv` `Na2MoO4 x 2 H2O` finding.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating merged outputs.
- Manually re-open MediaDive medium 1313 and the DSMZ Medium 1313 PDF to verify the final record preserves Solution A, Solution B, Trace element solution SL10, and Vitamin Solution V10 as separate preparation boundaries.

## Additional Notes

- The exact gitignore-independent search included ignored files in the scoped paths listed under Target. It was sufficient to resolve the DSMZ owner, the KOMODO-derived siblings, stale generated records, and the existing duplicate-merge diagnostic.
- A broader interrupted exploratory search also ran while resolving this record; it was not used for negative findings or source conclusions in this report.
