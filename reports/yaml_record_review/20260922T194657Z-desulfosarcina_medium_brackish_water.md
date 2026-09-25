# YAML Record Review: desulfosarcina_medium_brackish_water

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfosarcina_medium_brackish_water.yaml
- Started UTC: 2026-09-22T19:47:04Z
- Finished UTC: 2026-09-22T19:47:04Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/desulfosarcina_medium_brackish_water.yaml` |
| Generated or maintained | Generated merge output |
| Maintained owners | `data/normalized_yaml/bacterial/desulfosarcina_medium_brackish_water.yaml`, `data/normalized_yaml/bacterial/desulfosarcina_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:001296` |
| Label | `desulfosarcina_medium_brackish_water` |
| Original label | `DESULFOSARCINA MEDIUM (BRACKISH WATER)` |
| Source identity | DSMZ Medium 198 / KOMODO Medium 198 |
| Merge lineage | `merge_recipes.py` merged `desulfosarcina_medium.yaml` and `desulfosarcina_medium_brackish_water.yaml` into fingerprint `ea1cf63d307cc9362ed2866e9a7c60724dc4e975c05576a73351afb92632dd73` |

I read the full generated record and both maintained normalized owners. A gitignore-independent exact search for the target label and brackish Desulfosarcina names found the two normalized owners, this generated merge, and no ignored prior review for `desulfosarcina_medium_brackish_water`.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfosarcina_medium_brackish_water.yaml` | Passed |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/desulfosarcina_medium_brackish_water.yaml --out /private/tmp/desulfosarcina_medium_brackish_water.strict.tsv --workers 1 --quiet` | Passed; 0 error rows in the TSV |
| Reference validator, `linkml-reference-validator validate data data/merge_yaml/merged/desulfosarcina_medium_brackish_water.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator, `linkml-term-validator validate-data data/merge_yaml/merged/desulfosarcina_medium_brackish_water.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only the known `eutils` / `pkg_resources` deprecation warning was emitted |
| Embedded `curation_history` | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` entries |

The documented `just` wrappers were not used for this focused record check because the local project `uv` environment currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools`. The equivalent validators above were run offline with Python 3.11 and the cached `linkml`, `pyyaml`, `linkml-reference-validator`, and `linkml-term-validator` packages.

## Identity and Grounding

The high-level identity is correct: MediaDive 198 and the inspected DSMZ PDF both identify medium 198 as `DESULFOSARCINA MEDIUM (BRACKISH WATER)`, and the KOMODO owner cites the same DSMZ 198 accession as a source duplicate. The generated `parent_media`, `variant_relationship`, `synonyms`, and `merged_from` metadata coherently preserve that duplicate relationship.

The simple salt CHEBI groundings match their source labels, but many top-level ingredient rows are not actually final-medium ingredients. They are constituents of Solution B, C, E, selenite-tungstate stock, Trace element solution SL-10, or Wolin's vitamin solution (10x).

## Evidence

DSMZ Medium 198 and MediaDive 198 support a five-solution final assembly: 952 ml Solution A, 30 ml Solution B, 10 ml Solution C, 1 ml Solution D, and 10 ml Solution E for 1003 ml final medium at pH 7.1-7.4. The generated record has no `solutions:` block and no A-to-E assembly boundary.

DSMZ and MediaDive support a nested Solution A with salts, 1 ml selenite-tungstate solution, 1 ml Trace element solution SL-10, 0.5 ml 0.1% sodium resazurin, and 950 ml water. They also support Solution B as 1.50 g Na2CO3 in 30 ml water, Solution C as 0.60 g sodium benzoate in 10 ml water, Solution D as 1 ml Wolin's vitamin solution, and Solution E as 0.40 g Na2S x 9H2O in 10 ml water.

Selenite-tungstate solution, Trace element solution SL-10, and Wolin's vitamin solution each have their own per-liter compositions in the DSMZ PDF. The generated record instead promotes the stock-strength NaOH, selenite, tungstate, HCl, FeCl2, trace metals, and vitamin concentrations to top-level ingredients.

The preparation text is source-backed but only because it still narrates the missing scopes. It tells the reader to autoclave Solutions A and B under 80% N2 / 20% CO2, to autoclave Solutions C and E under 100% N2, to filter-sterilize Solution D under 100% N2, and to add B through E to sterile A. The third generated step, dissolving FeCl2 in HCl, belongs specifically to Trace element solution SL-10, not to the main medium.

## Completeness

The record is missing every solution boundary needed to make DSMZ 198 reproducible: Solution A through E, selenite-tungstate solution, Trace element solution SL-10, and Wolin's vitamin solution. The water rows for all of those solutions are also absent.

The empty `target_organisms` and `references` slots are not defects for this imported source recipe because DSMZ, MediaDive, and KOMODO provide formulation provenance, not primary growth-study evidence.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The DSMZ 198 A-through-E solution topology is flattened. | DSMZ 198 assembles the final 1003 ml medium from Solutions A, B, C, D, and E. The generated record has only one top-level `ingredients` list. | `data/normalized_yaml/bacterial/desulfosarcina_medium_brackish_water.yaml`, `data/normalized_yaml/bacterial/desulfosarcina_medium.yaml`, and DSMZ/MediaDive import logic. |
| Major | Stock concentrations are represented as final-medium ingredient concentrations. | Solution B carbonate is 50 g/L stock, Solution C benzoate is 60 g/L stock, Solution E sulfide is 40 g/L stock, and the selenite-tungstate, SL-10, and Wolin vitamin rows are all per-liter stock recipes. All appear as top-level `G_PER_L` rows in the generated target. | Same normalized owners plus the MediaDive solution-flattening path. |
| Major | The nested selenite-tungstate, SL-10, and Wolin vitamin stocks are flattened instead of scoped to Solution A or D. | DSMZ 198 adds selenite-tungstate and SL-10 inside Solution A and adds 1 ml Wolin's vitamin solution as Solution D; the generated record promotes every stock constituent to a final medium row. | Same normalized owners. |
| Major | Preparation-step scoping is internally inconsistent with the ingredient model. | The record has no Solution A through E objects, but its first step instructs the curator to add B through E to A; its third step is the SL-10 stock preparation note attached to the main MediaRecipe. | Same normalized owners and preparation-step import logic. |
| Minor | Distilled-water rows are missing from every solution scope. | The DSMZ PDF lists water for Solution A, B, C, E, selenite-tungstate, SL-10, and Wolin's vitamin solution. The generated target has no water row. | Same normalized owners. |

## Recommended Edits

1. Restore `data/normalized_yaml/bacterial/desulfosarcina_medium_brackish_water.yaml` as a solution-structured DSMZ 198 recipe with the 952/30/10/1/10 ml final A-to-E assembly.
2. Scope the selenite-tungstate, SL-10, and Wolin vitamin stocks under the correct parent solutions instead of flattening them into the main `ingredients` list.
3. Propagate the same repaired DSMZ 198 topology to `data/normalized_yaml/bacterial/desulfosarcina_medium.yaml` or keep the KOMODO record as a metadata-only source duplicate so the merge cannot reintroduce the flattened rows.
4. Attach preparation text to the scopes it describes: main assembly for the anaerobic autoclaving sequence and Trace element solution SL-10 for the FeCl2/HCl dissolution step.
5. Preserve the water rows for the component stocks and regenerate `data/merge_yaml/merged/desulfosarcina_medium_brackish_water.yaml`.

## Follow-up Checks

1. Rerun open schema, strict schema, term, and reference validation on both edited normalized records and on the regenerated merged output.
2. Compare the regenerated record against DSMZ Medium 198, checking every Solution A-E addition volume, every nested stock component, and the final pH range.
3. Check that carbonate, benzoate, sulfide, selenite-tungstate, SL-10, and vitamin stock concentrations are no longer top-level final-medium rows.
4. Confirm the KOMODO duplicate still merges with the MediaDive/DSMZ owner without changing the corrected solution topology.

## Additional Notes

- `find` and `rg --no-ignore --hidden` were used for absence-sensitive searches, so ignored review reports and generated files were included where relevant.
- No report for `desulfosarcina_medium_brackish_water` existed under `reports/yaml_record_review/` before this one; that ignored directory was checked with `find`.
