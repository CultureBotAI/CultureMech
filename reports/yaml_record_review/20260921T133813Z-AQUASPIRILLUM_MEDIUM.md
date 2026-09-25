# YAML Record Review: AQUASPIRILLUM medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/AQUASPIRILLUM_MEDIUM.yaml
- Started UTC: 2026-09-21T13:35:55Z
- Finished UTC: 2026-09-21T13:38:14Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| Stable ID | CultureMech:006738 |
| Name | aquaspirillum_medium |
| Original name | AQUASPIRILLUM medium |
| Category | bacterial |
| Source | KOMODO Medium 888 copied from DSMZ / MediaDive Medium 888 |
| Reviewed artifact | data/merge_yaml/merged/AQUASPIRILLUM_MEDIUM.yaml |
| Merged sources | data/normalized_yaml/bacterial/KOMODO_888_AQUASPIRILLUM_medium.yaml; data/normalized_yaml/bacterial/aquaspirillum_medium.yaml |

The reviewed record is the generated canonical merge for two source duplicates: a KOMODO 888 import and a DSMZ/MediaDive 888 import. Both normalized inputs already declare a `SOURCE_DUPLICATE` relationship to each other, and the merge fingerprint combines `KOMODO_888_AQUASPIRILLUM_medium` with `aquaspirillum_medium`.

An ignored-file-inclusive exact search for `CultureMech:006738`, `CultureMech:002048`, `komodo.medium:888`, `mediadive.medium:888`, `DSMZ Medium 888`, and `AQUASPIRILLUM` covered `data/normalized_yaml`, `data/merge_yaml`, `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, `reports/media_content_review_manifest.tsv`, `data/import_tracking/reports/concentration_plausibility.tsv`, and `data/import_tracking/reports/merged_duplicates.tsv`. It found the KOMODO owner, the DSMZ/MediaDive duplicate owner, their generated merge, generated indexes, registry/catalog rows, manifest rows for both owners, the adjacent but distinct `AQUASPIRILLUM_MEDIUM_II`, and concentration-plausibility rows for this same duplicated medium.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/AQUASPIRILLUM_MEDIUM.yaml`; no issues found. |
| Strict schema | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/AQUASPIRILLUM_MEDIUM.yaml --out /private/tmp/AQUASPIRILLUM_MEDIUM.strict.tsv --workers 1 --quiet`; 1 file scanned, 0 error rows. |
| Reference validator | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/AQUASPIRILLUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; 1 file validated, 0 total active checks. |
| Term validator | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/AQUASPIRILLUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`; only the upstream `eutils`/`pkg_resources` deprecation warning was emitted. |
| Embedded curation history | Not checked: this repository exposes `just validate-history` for standalone `history/` files, not a focused `MediaRecipe.curation_history` check for one merged recipe. |

Mechanical validators pass despite the stock-scope and preparation losses below.

## Identity and Grounding

The generated record denotes the right source medium. DSMZ Medium 888 is `AQUASPIRILLUM MEDIUM`, and both normalized owners carry that same formulation.

The sibling `AQUASPIRILLUM_MEDIUM_II.yaml` is distinct: it points to MediaDive medium 1495 and should not be merged into this Medium 888 record.

Most groundings are exact for the flattened row labels. One source hydrate is not: `NiCl2 x 6 H2O` is grounded to CHEBI:34887 / nickel dichloride, the anhydrous salt, even though DSMZ trace stock 1369 uses nickel chloride hexahydrate.

The phosphate row also needs explicit source adjudication. The DSMZ Medium 888 PDF visibly prints `Na2H2PO4`, while the live MediaDive Medium 888 page has normalized that row to `Na2HPO4`. The record silently stores `Na2HPO4` grounded to disodium hydrogenphosphate; future curation should preserve the DSMZ-vs-MediaDive normalization decision instead of presenting it as a direct PDF transcription.

## Evidence

DSMZ Medium 888 supports only these final-medium rows directly:

| Component | Source amount |
| --- | ---: |
| (NH4)2SO4 | 1.0 g |
| MgSO4 x 7 H2O | 1.0 g |
| CaCl2 x 6 H2O | 30.0 mg |
| Na2H2PO4 in the PDF; Na2HPO4 on MediaDive | 10.0 mg |
| Sodium succinate | 1.00 g |
| Casamino acids (DIFCO) | 1.5 g |
| Trace element solution, see medium 1369 | 1.0 ml |
| Agar (DIFCO) | 0.5 g |
| Distilled water | 1000.0 ml |

It then instructs addition after autoclaving of sterile solutions:

| Post-autoclave addition | Source amount |
| --- | ---: |
| Na2S2O3 x 5 H2O, 10% solution | 1.0 ml |
| Vitamin solution, see medium 1478 | 1.0 ml |

The generated record flattens Medium 1369's trace stock into final rows for EDTA, FeSO4, ZnSO4, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, Na2MoO4, and NaOH. It likewise flattens the Medium 1478 vitamin-mix stock rows into final rows for thiamine, calcium pantothenate, biotin, PABA, nicotinic acid, pyridoxine, folic acid, riboflavin, and B12. Those rows are stock ingredients, not direct weighed additions to one liter of AQUASPIRILLUM Medium 888.

The generated record also drops the final `Distilled water 1000.0 ml` row and all preparation context. The source specifies pH 7.5 for the final medium and says the thiosulfate and vitamin stocks are added after autoclaving as sterile solutions; the Medium 1369 trace stock carries pH 3.0-4.0; the Medium 1478 vitamin mix is assembled from four 100 ml solutions, sterilized by filtration, and mixed in a 1:1:1:1 ratio before a 1.0 ml/L addition.

## Completeness

Consequential gaps:

- The final 1000 ml distilled water component from DSMZ Medium 888 is absent.
- There is no representation of the `Trace element solution (see medium 1369)`, `Na2S2O3 x 5 H2O (10% solution)`, or `vitamin solution (see medium 1478)` post-autoclave stock additions.
- Stock rows from DSMZ Medium 1369 and DSMZ Medium 1478 are present as top-level final ingredients without dilution scope.
- The record loses the pH and filtration/preparation boundaries for the referenced stock solutions.

No organism growth claims or variants are asserted, and those optional fields do not need generic placeholder values for a DSMZ formulation page.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| major | DSMZ stock solutions are flattened into final-medium ingredients. | DSMZ Medium 888 calls for 1.0 ml of trace element stock 1369 and 1.0 ml of vitamin stock 1478; the generated recipe instead lists the trace and vitamin stock components at their stock concentrations as top-level final ingredients. | Repair the DSMZ/MediaDive import in `data/normalized_yaml/bacterial/aquaspirillum_medium.yaml`, propagate the duplicate relationship to `data/normalized_yaml/bacterial/KOMODO_888_AQUASPIRILLUM_medium.yaml`, and regenerate the merge. |
| major | Post-autoclave additions are reduced to unsupported direct concentrations. | DSMZ adds sterile 10% Na2S2O3 x 5 H2O and vitamin solution after autoclaving, each at 1.0 ml. The generated record has `Na2S2O3 x 5 H2O` as a direct `0.1 G_PER_L` ingredient and no preparation steps. | Model the 10% thiosulfate stock, vitamin-stock addition, and final assembly in the normalized DSMZ owner. |
| major | Final distilled water is missing. | DSMZ Medium 888 lists `Distilled water 1000.0 ml`; the generated record has no water ingredient. | Add the final water row to the normalized owner or fix the MediaDive importer branch that omitted it. |
| major | Preparation semantics are incomplete. | The merge has `ph_value: 7.5` but lacks the post-autoclave stock additions from Medium 888, the trace-stock pH 3.0-4.0 from Medium 1369, and the Medium 1478 filtration plus four-solution 1:1:1:1 vitamin-mix instruction. | Preserve source preparation and stock preparation notes on the normalized record and verify the merge keeps them. |
| major | One hydrate salt is grounded to the anhydrous salt. | DSMZ Medium 1369 specifies `NiCl2 x 6H2O`; the record grounds `NiCl2 x 6 H2O` to CHEBI:34887 / nickel dichloride. | Re-ground to an exact nickel chloride hexahydrate term through the packaged MIM index or leave the row unresolved until one is available. |
| minor | The source conflict around the phosphate label is hidden. | The DSMZ PDF prints `Na2H2PO4`; MediaDive exposes `Na2HPO4`; the YAML silently keeps the MediaDive-normalized spelling and a disodium hydrogenphosphate grounding. | Add a discussion or quality flag documenting that the curated value follows MediaDive's normalized ingredient label despite the DSMZ PDF text. |

No blocker findings: the merge points to the correct Medium 888 record and does not conflate the adjacent Medium 1495 / AQUASPIRILLUM MEDIUM II sibling.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/aquaspirillum_medium.yaml`, restore the Medium 888 final recipe as direct ingredients plus three stock additions: 1.0 ml trace element solution 1369, 1.0 ml 10% Na2S2O3 x 5 H2O after autoclaving, and 1.0 ml vitamin solution 1478 after autoclaving.
2. Move all Medium 1369 and 1478 stock components out of top-level final ingredients and into referenced stock-solution scopes, preserving their own final volumes, pH or filtration notes, and vitamin-mix 1:1:1:1 assembly.
3. Add `Distilled water` at 1000 ml/L to the final Medium 888 representation.
4. Re-ground `NiCl2 x 6 H2O` to an exact hydrate term or leave it explicitly unresolved.
5. Record the DSMZ-PDF versus MediaDive `Na2H2PO4` / `Na2HPO4` difference as a concrete discussion item instead of silently collapsing the mismatch.
6. Reconcile `data/normalized_yaml/bacterial/KOMODO_888_AQUASPIRILLUM_medium.yaml` with the corrected DSMZ owner and regenerate `data/merge_yaml/merged/AQUASPIRILLUM_MEDIUM.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validators on both normalized source records.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating the Medium 888 merge.
- Recompare the regenerated record against DSMZ Medium 888, Medium 1369, Medium 1478, and the live MediaDive Medium 888 page to ensure only final components stay top-level and all referenced stock rows remain scoped.
- Rebuild or recheck `data/import_tracking/reports/concentration_plausibility.tsv`; stock-only trace/vitamin concentrations should no longer be reported as top-level final ingredients for either duplicate owner.

## Additional Notes

- `data/merge_yaml/merged/AQUASPIRILLUM_MEDIUM_II.yaml` is adjacent in case-folded order but represents MediaDive Medium 1495, not this Medium 888 formulation.
- The exact search above included ignored files and generated indexes; it still found no third normalized owner for Medium 888 in the searched paths.
