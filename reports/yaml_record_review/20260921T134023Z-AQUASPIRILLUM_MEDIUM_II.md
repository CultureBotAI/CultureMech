# YAML Record Review: AQUASPIRILLUM MEDIUM II

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/AQUASPIRILLUM_MEDIUM_II.yaml
- Started UTC: 2026-09-21T13:39:17Z
- Finished UTC: 2026-09-21T13:40:24Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| Stable ID | CultureMech:000963 |
| Name | aquaspirillum_medium_ii |
| Original name | AQUASPIRILLUM MEDIUM II |
| Category | bacterial |
| Source | MediaDive / DSMZ Medium 1495 |
| Reviewed artifact | data/merge_yaml/merged/AQUASPIRILLUM_MEDIUM_II.yaml |
| Maintained owner | data/normalized_yaml/bacterial/aquaspirillum_medium_ii.yaml, with generated merge output under data/merge_yaml/merged/ |

This review targeted the generated canonical merge for `aquaspirillum_medium_ii`; `merged_from` contains only that normalized owner.

An ignored-file-inclusive exact search for `CultureMech:000963`, `mediadive.medium:1495`, `AQUASPIRILLUM MEDIUM II`, and `aquaspirillum_medium_ii` covered `data/normalized_yaml`, `data/merge_yaml`, `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, `reports/media_content_review_manifest.tsv`, `data/import_tracking/reports/concentration_plausibility.tsv`, and `data/import_tracking/reports/merged_duplicates.tsv`. It found this generated merge, the single normalized owner, generated indexes, registry/catalog rows, and the media content manifest row for the same CultureMech ID.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/AQUASPIRILLUM_MEDIUM_II.yaml`; no issues found. |
| Strict schema | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/AQUASPIRILLUM_MEDIUM_II.yaml --out /private/tmp/AQUASPIRILLUM_MEDIUM_II.strict.tsv --workers 1 --quiet`; 1 file scanned, 0 error rows. |
| Reference validator | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/AQUASPIRILLUM_MEDIUM_II.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; 1 file validated, 0 total active checks. |
| Term validator | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/AQUASPIRILLUM_MEDIUM_II.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`; only the upstream `eutils`/`pkg_resources` deprecation warning was emitted. |
| Embedded curation history | Not checked: this repository exposes `just validate-history` for standalone `history/` files, not a focused `MediaRecipe.curation_history` check for one merged recipe. |

Mechanical validators pass despite the stale generated merge and source-scope issues below.

## Identity and Grounding

The target identity is correct. DSMZ Medium 1495 is `AQUASPIRILLUM MEDIUM II`, the generated record points to `mediadive.medium:1495`, and this record is distinct from DSMZ Medium 888 / `AQUASPIRILLUM_MEDIUM.yaml`.

Two exact hydrate forms are grounded incorrectly:

| Ingredient | Current grounding | Issue |
| --- | --- | --- |
| FeSO4 x 6 H2O | CHEBI:75832, iron(2+) sulfate (anhydrous) | DSMZ 1495 trace stock uses the hexahydrate, not anhydrous ferrous sulfate. |
| NiCl2 x 6 H2O | CHEBI:34887, nickel dichloride | DSMZ 1495 trace stock uses the hexahydrate, not anhydrous nickel chloride. |

## Evidence

DSMZ Medium 1495 supports a main solution with these direct rows:

| Main-medium component | Source amount |
| --- | ---: |
| Peptone (BD) | 2.00 g |
| Succinic acid | 1.00 g |
| (NH4)2SO4 | 1.00 g |
| MgSO4 x 7 H2O | 1.00 g |
| CaCl2 x 2 H2O | 0.03 g |
| Vitamin solution, see below | 1.00 ml |
| Trace elements, see below | 1.00 ml |
| Distilled water | 1000.0 ml |
| Agar, for solid medium | 15.0 g/L |

The generated merge lists the bulk rows and optional agar, but it omits `Distilled water 1000.0 ml` and flattens both 1 ml stock additions into the top-level final ingredient list. DSMZ lists a 1000 ml trace stock with EDTA, FeSO4 x 6 H2O, ZnSO4 x 7 H2O, MnCl2 x 4 H2O, H3BO, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6H2O, and Na2MoO4 x 2 H2O at pH 3.0-4.0. DSMZ also lists a 1000 ml vitamin stock with Biotin, Folic acid, Pyridoxine-HCl, Thiamine-HCl, Riboflavin, Nicotinic acid, DL-Pantothenic acid, Vitamin B12, and p-Aminobenzoic acid, followed by filter sterilization.

`data/normalized_yaml/bacterial/aquaspirillum_medium_ii.yaml` contains a later 2026-08-07 `NESTED_FLATTENED_COCKTAIL` event that moved Biotin, Pyridoxine hydrochloride, Riboflavin, and FeSO4 x 6 H2O under two `solutions` at 1 ml/L. The reviewed generated merge was last merged on 2026-08-06, so it is stale relative to even that partial repair.

## Completeness

Consequential gaps:

- The final 1000 ml distilled water row is absent.
- The generated merge lacks `Vitamin solution` and `Trace elements solution` entries even though DSMZ 1495 adds both stocks at 1 ml/L.
- Most trace and vitamin stock components remain indistinguishable from direct final-medium grams per liter.
- The normalized owner only partially nested the stocks; it still leaves EDTA, ZnSO4, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, Na2MoO4, Folic acid, Thiamine-HCl, Nicotinic acid, DL-Pantothenic acid, Vitamin B12, and Para-aminobenzoic acid at top level.

Empty organism, growth-evidence, and variant fields are acceptable for a DSMZ formulation record with no asserted growth claim.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| major | The generated merge is stale relative to a partial stock-nesting repair. | The generated merge has no `solutions` array and still includes FeSO4, Biotin, Pyridoxine hydrochloride, and Riboflavin as direct final ingredients. The maintained normalized owner moved those four rows into `solutions` on 2026-08-07. | Regenerate `data/merge_yaml/merged/AQUASPIRILLUM_MEDIUM_II.yaml` from `data/normalized_yaml/bacterial/aquaspirillum_medium_ii.yaml` after the normalized owner is fully corrected. |
| major | Trace and vitamin stock components are flattened into final-medium ingredients. | DSMZ 1495 adds trace elements and vitamin solution as 1 ml stocks; the YAML presents most or all stock rows at the top level. The normalized owner still leaves most stock rows top-level, and the generated merge leaves all of them top-level. | Finish stock nesting in `data/normalized_yaml/bacterial/aquaspirillum_medium_ii.yaml`, preserving the 1000 ml stock volumes and 1 ml/L additions. |
| major | The final water row is missing. | DSMZ Medium 1495 lists `Distilled water 1000.0 ml` for the main solution; neither the generated merge nor the normalized owner has a top-level water ingredient. | Add the main-solution water row to the normalized owner or fix the MediaDive importer that omitted it. |
| major | Exact hydrate groundings are wrong for two trace salts. | DSMZ uses `FeSO4 x 6 H2O` and `NiCl2 x 6 H2O`; the record grounds those labels to anhydrous ferrous sulfate and anhydrous nickel chloride. | Re-ground to exact hydrate terms through the packaged MIM label index or leave unresolved if exact terms are unavailable. |
| minor | Preparation steps preserve only coarse prose and lose stock association. | The generated `AUTOCLAVE` step embeds pH adjustment, autoclaving, the 1 ml/L vitamin addition, and the optional agar note in one string; the trace stock pH and vitamin filtration are generic `MIX` / `FILTER_STERILIZE` steps no longer attached to their respective stock solutions. | Move preparation notes onto the final medium, trace stock, and vitamin stock objects that own them. |

No blocker findings: the record denotes the correct DSMZ Medium 1495 recipe.

## Recommended Edits

1. Finish nesting the DSMZ 1495 trace stock under a 1 ml/L `Trace elements` solution and move EDTA, ZnSO4 x 7 H2O, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O out of top-level ingredients.
2. Finish nesting the DSMZ 1495 vitamin stock under a 1 ml/L `Vitamin solution` and move Folic acid, Thiamine-HCl, Nicotinic acid, DL-Pantothenic acid, Vitamin B12, and Para-aminobenzoic acid out of top-level ingredients with the already-nested Biotin, Pyridoxine hydrochloride, and Riboflavin.
3. Add final `Distilled water` at 1000 ml/L.
4. Re-ground `FeSO4 x 6 H2O` and `NiCl2 x 6 H2O` to exact hydrate terms, or leave them explicitly unresolved.
5. Preserve the main pH 7.4-7.6, autoclave, 1 ml/L filter-sterilized vitamin addition, trace pH 3.0-4.0, vitamin filtration, and optional 15 g/L agar notes on the final or stock scopes they describe.
6. Regenerate `data/merge_yaml/merged/AQUASPIRILLUM_MEDIUM_II.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/aquaspirillum_medium_ii.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating the generated merge.
- Recompare the normalized and generated records against DSMZ Medium 1495 and live MediaDive Medium 1495, checking final water, the two 1 ml/L solution additions, all nested stock members, stock final volumes, and exact hydrate groundings.

## Additional Notes

- The exact search above included ignored files and generated indexes; it found only one normalized owner for Medium 1495 in the searched paths.
- The DSMZ Medium 1495 PDF visually prints `H3BO` in the trace stock where MediaDive uses `H3BO3`; future curation should preserve that MediaDive normalization decision if the boric acid row is retained.
