# YAML Record Review: BAP+ MEDIUM FOR FRANKIA

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/bap_medium_for_frankia.yaml`
- Started UTC: 2026-09-21T18:31:02Z
- Finished UTC: 2026-09-21T18:32:16Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:001014` |
| Merged record | `data/merge_yaml/merged/bap_medium_for_frankia.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/bap_medium_for_frankia.yaml` |
| Source identity | DSMZ Medium 1536 / MediaDive `mediadive.medium:1536` |
| Merge status | Generated from one normalized source, `bap_medium_for_frankia` |

The reviewed record is the generated merge for DSMZ 1536, "BAP+ MEDIUM FOR FRANKIA". A gitignore-independent search for `CultureMech:001014`, `bap_medium_for_frankia`, `BAP+ MEDIUM FOR FRANKIA`, `DSMZ Medium 1536`, `mediadive.medium:1536`, and `DSMZ_Medium1536` across `data`, `history`, `src`, `scripts`, `reports/yaml_record_review`, and `.claude` found one live normalized owner plus the generated merge and registry/index/import-tracking rows. It found no prior report for this record. The search included ignored files.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bap_medium_for_frankia.yaml`. |
| Strict schema | Passed with `scripts/validate_strict.py`; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference snippets | Passed with `linkml-reference-validator validate data ...`; 1 file validated, 0 snippet checks, all validations passed. |
| Term labels | Passed with `linkml-term-validator validate-data ... --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: no documented focused validator exists for embedded `MediaRecipe.curation_history` on one generated merge record; `just validate-history` targets standalone history files. |

The direct `just` validators remain unavailable in this checkout because project `uv` tries to build `llvmlite==0.46.0` under Python 3.13 and exits inside `setuptools`. I used the no-project Python 3.11 validator workaround for the focused schema, strict, reference, and term checks above.

## Identity and Grounding

The record ID, label, DSMZ/MediaDive accession, `bacterial` category, `DEFINED` classification, `LIQUID` physical state, and final pH 6.3 all match DSMZ Medium 1536.

Most exact simple salts are grounded to the right hydrated forms, and the vitamin solution's thiamine, nicotinic acid, and pyridoxine HCl components all use exact local MIM labels. The `Eisencitrat` row is still over-specific and stale: the record grounds DSMZ `Eisencitrat` to `CHEBI:144434` `iron(III) citrate monohydrate` and keeps a legacy `mediaingredientmech_term`, while `src/culturemech/data/mediaingredientmech/label_index.csv` has an exact `Eisencitrat` row for `CHEBI:144421` `Fe(III) citrate`.

## Evidence

DSMZ Medium 1536 directly supports six bulk final-medium ingredients: 0.95 g/L KH2PO4, 0.6 g/L K2HPO4, 0.27 g/L NH4Cl, 0.48 g/L Na-propionate, 0.025 g/L MgSO4 x 7 H2O, and 0.01 g/L CaCl2 x 2 H2O.

DSMZ then adds three stock solutions to the final medium: 1 ml/L vitamin solution prepared in 100 ml water, 1 ml/L chelated iron solution prepared in 100 ml water, and 0.1 ml/L trace element solution prepared in 100 ml water. The generated merge predates the normalized owner's `2026-08-07` `NESTED_FLATTENED_COCKTAIL` event, so it still flattens vitamin and trace-stock concentrations as top-level final grams per liter. The current normalized owner has nested the vitamin and trace stocks under `solutions`, but still leaves the chelated-iron stock's citric acid and `Eisencitrat` at stock concentration on the top-level ingredient list.

DSMZ also specifies 1000 ml distilled water for the final medium and 100 ml distilled water for each of the three stock solutions. None of those solvent rows are represented.

The generated autoclave note for the chelated iron solution is source-supported. DSMZ says to autoclave that solution before adding it to the medium.

## Completeness

The generated merge is stale relative to its maintained normalized owner and therefore incomplete as a generated artifact: it is missing both `solutions` blocks now present upstream, and it preserves obsolete top-level vitamin and trace rows that upstream curation already nested.

The maintained owner still needs a chelated-iron solution boundary and water rows for the final medium and three stock solutions. The vitamin and trace solution nesting in the maintained owner matches DSMZ's stock component concentrations and addition rates, but the generated merge will remain misleading until `data/merge_yaml/merged/` is regenerated.

The absent target-organism, atmosphere, incubation-temperature, and storage fields are optional and not automatically defects for this DSMZ recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | The generated merge is stale relative to its normalized owner. | `data/merge_yaml/merged/bap_medium_for_frankia.yaml` was generated on `2026-08-06` and has only top-level vitamin and trace ingredients; `data/normalized_yaml/bacterial/bap_medium_for_frankia.yaml` has a `2026-08-07` `NESTED_FLATTENED_COCKTAIL` event and now carries `Vitamine solution` and `Trace element solution` blocks at 1 ml/L and 0.1 ml/L. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/bacterial/bap_medium_for_frankia.yaml` |
| Major | The chelated iron solution is still flattened and 1000-fold too concentrated. | DSMZ adds 1 ml/L of a 100 ml stock containing 1 g citric acid and 1 g `Eisencitrat`; the generated and normalized records both store `Citric acid` and `Eisencitrat` as 10 g/L top-level ingredients instead of as 10 g/L stock components added at 1 ml/L. | `data/normalized_yaml/bacterial/bap_medium_for_frankia.yaml` |
| Major | The formula drops all four DSMZ water rows. | DSMZ lists 1000 ml distilled water in the final medium and 100 ml distilled water in each of the vitamin, chelated-iron, and trace-element stock recipes; none are represented in the normalized owner or stale generated merge. | `data/normalized_yaml/bacterial/bap_medium_for_frankia.yaml` |
| Major | `Eisencitrat` has a legacy MIM link and is over-grounded to ferric citrate monohydrate. | The local exact MIM row for `Eisencitrat` maps to `CHEBI:144421` `Fe(III) citrate`; the record instead uses `CHEBI:144434` and preserves `MediaIngredientMech:000664`. | `data/normalized_yaml/bacterial/bap_medium_for_frankia.yaml` |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/bap_medium_for_frankia.yaml` from the current normalized record so the generated page stops exposing pre-`2026-08-07` flattened vitamin and trace stocks.
2. Move `Citric acid` and `Eisencitrat` into a `Chelated iron solution` block added at 1 ml/L, with both stock components at 10 g/L.
3. Add 1000 ml distilled water to the final medium and 100 ml distilled water to each DSMZ stock solution.
4. Replace the `Eisencitrat` row's `CHEBI:144434` and legacy `mediaingredientmech_term` with the exact local `CHEBI:144421` mapping.

## Follow-up Checks

1. Re-run the focused schema, strict, term, and reference validators on the regenerated `data/merge_yaml/merged/bap_medium_for_frankia.yaml`.
2. Re-run `verify-merges` or `audit-merge-freshness` after regeneration to prove the generated merge is no longer stale relative to the normalized owner.
3. Re-open DSMZ Medium 1536 and confirm that the generated merge has six top-level bulk solutes, 1 ml/L vitamin solution, 1 ml/L chelated iron solution, 0.1 ml/L trace element solution, all four distilled-water rows, final pH 6.3, and no stock-strength solutes left at the top level.

## Additional Notes

The source spelling `Vitamine solution` is retained in the normalized owner. That spelling matches the DSMZ heading and should not be normalized away during a stock-boundary fix.
