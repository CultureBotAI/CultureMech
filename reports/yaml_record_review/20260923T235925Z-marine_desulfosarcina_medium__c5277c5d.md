# YAML Record Review: marine_desulfosarcina_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_desulfosarcina_medium__c5277c5d.yaml
- Started UTC: 2026-09-23T23:59:25Z
- Finished UTC: 2026-09-23T23:59:38Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | data/merge_yaml/merged/marine_desulfosarcina_medium__c5277c5d.yaml |
| Class | MediaRecipe |
| ID | CultureMech:015403 |
| Label | marine_desulfosarcina_medium |
| Source identity | mediadive.medium:J391, JCM Medium 391, MARINE DESULFOSARCINA MEDIUM |
| Generation state | Generated one-source merge under data/merge_yaml/merged; repair data/normalized_yaml/specialized/marine_desulfosarcina_medium.yaml or the MediaDive importer rather than this file |

The generated record denotes JCM Medium 391 from MediaDive. Its ID, pH, source accession, name, and main salt amounts agree, but the record flattens several stock solutions into the final-medium ingredient list and omits the JCM/MediaDive final-water row.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_desulfosarcina_medium__c5277c5d.yaml` | Passed; exited 0 with no diagnostics |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_desulfosarcina_medium__c5277c5d.yaml --out /private/tmp/marine_desulfosarcina_medium__c5277c5d.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_desulfosarcina_medium__c5277c5d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_desulfosarcina_medium__c5277c5d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning |
| Embedded curation history | Not checked | `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries |

## Identity and Grounding

- CultureMech:015403, `marine_desulfosarcina_medium`, and `mediadive.medium:J391` agree on the intended source: JCM Medium 391, `MARINE DESULFOSARCINA MEDIUM`.
- MediaDive and the live JCM page both report pH 7.2.
- The first seven salt rows and Resazurin correspond to MediaDive's final-volume-normalized main solution: for example, 20 g NaCl in 1025 ml becomes 19.5122 g/L.
- JCM and MediaDive both model Trace element, Selenite-tungstate, Vitamin, Thiamine, and Vitamin B12 solutions as stock additions, but the YAML publishes their stock components as top-level final-medium ingredients.
- NaHCO3, Sodium lactate, and Na2S x 9 H2O are final ml/L solution additions in JCM and MediaDive, not 30, 10, and 10 g/L final chemical concentrations.

## Evidence

- JCM Medium 391 lists 970 ml distilled water in the base formula, and MediaDive lists 970 ml Distilled water in `Main sol. J391`. The YAML omits this final-water row.
- JCM lists 1 ml/L Trace element solution from Medium 439. MediaDive exposes that stock as solution 4186, but the YAML flattens FeSO4 x 7 H2O, H3BO3, MnCl2 x 4 H2O, CoCl2 x 6 H2O, NiCl2 x 6 H2O, CuCl2 x 2 H2O, ZnSO4 x 7 H2O, Na2MoO4 x 2 H2O, and 25% HCl stock rows into the final medium.
- JCM lists 1 ml/L Selenite-tungstate solution from Medium 431. MediaDive exposes that stock as solution 4172, but the YAML flattens NaOH, Na2SeO3 x 5 H2O, and Na2WO4 x 2 H2O into the final medium.
- JCM lists 1 ml/L additions of Vitamin solution, Thiamine solution, and Vitamin B12 solution from Medium 403. The YAML flattens p-Aminobenzoic acid, Biotin, Nicotinic acid, DL-Calcium pantothenate, Pyridoxine hydrochloride, Sodium phosphate buffer, Thiamine HCl, and Vitamin B12 into the final medium.
- The generated YAML still shows `Sodium phosphate buffer` at 200 g/L with a generated note saying two 100.0 duplicates were merged, while the maintained YAML had already been collapsed to 100.0 before generation. Neither value preserves MediaDive's distinct 10 mM pH 7.1 and 25 mM pH 3.4 buffer attributes.

## Completeness

- The final recipe is materially incomplete without the 970 ml final-water row.
- The current record cannot be followed safely until the trace element, Selenite-tungstate, Vitamin, Thiamine, Vitamin B12, bicarbonate, lactate, and sulfide additions are represented as solution additions instead of flattened final ingredients.
- The preparation sequence preserves the major JCM steps and the JCM 31729 sodium fumarate/yeast extract comment.
- No target organism or growth metric is asserted. That is acceptable for this JCM formulation record.
- Exact gitignore-independent searches were run for `CultureMech:015403`, `marine_desulfosarcina_medium`, `mediadive.medium:J391`, `JCM Medium 391`, and the merge fingerprint prefix across the scoped specialized normalized YAML directory, this target merged YAML, and the specialized and recipe index files with `--no-ignore --hidden`; the searches found the maintained input, generated target, and expected index entries.
- An exact `find data/merge_yaml/merged -maxdepth 1 -name 'marine_desulfosarcina_medium*.yaml' -print` search, which includes ignored files, found only this generated target.
- An exact `find reports/yaml_record_review -maxdepth 1 -name '*-marine_desulfosarcina_medium__c5277c5d.md' -print` search, which includes ignored files, found no pre-existing review report for this generated record before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Multiple stock solutions are flattened into top-level final-medium rows. | JCM 391 and MediaDive J391 model trace element, Selenite-tungstate, Vitamin, Thiamine, and Vitamin B12 as 1 ml/L stock additions, but the YAML lists their internal stock ingredients as final-medium ingredients. | data/normalized_yaml/specialized/marine_desulfosarcina_medium.yaml and the MediaDive importer |
| major | Three ml/L solution additions are represented as g/L chemical rows. | JCM and MediaDive list 30 ml 8% NaHCO3, 10 ml 1.0 M Sodium lactate, and 10 ml 5% Na2S x 9 H2O per liter; the YAML records 30, 10, and 10 g/L. | data/normalized_yaml/specialized/marine_desulfosarcina_medium.yaml and the MediaDive importer |
| major | The 970 ml final-water row is missing. | JCM Medium 391 and MediaDive `Main sol. J391` both list Distilled water at 970 ml; the YAML has no final water ingredient. | data/normalized_yaml/specialized/marine_desulfosarcina_medium.yaml and the MediaDive importer |
| minor | The generated Sodium phosphate buffer row is stale and chemically collapsed. | The generated merge still sums two 100 ml buffer rows to 200.0, while MediaDive distinguishes the 10 mM pH 7.1 vitamin-solution buffer from the 25 mM pH 3.4 thiamine-solution buffer. | data/normalized_yaml/specialized/marine_desulfosarcina_medium.yaml and data/merge_yaml generation |

## Recommended Edits

1. Rework data/normalized_yaml/specialized/marine_desulfosarcina_medium.yaml so final main-solution ingredients, stock additions, and nested stock compositions stay separate.
2. Add the missing 970 ml distilled-water row for JCM/MediaDive main solution J391.
3. Encode NaHCO3, Sodium lactate, and Na2S x 9 H2O as 30, 10, and 10 ml/L stock-solution additions instead of g/L final ingredients.
4. Preserve the distinct sodium phosphate buffer concentration and pH contexts inside the Vitamin and Thiamine stock formulas.
5. Regenerate `data/merge_yaml/merged/` and verify the generated J391 record no longer has stock-only ingredients at top level.

## Follow-up Checks

- Compare the repaired normalized YAML against the live JCM Medium 391 page and the MediaDive J391 REST payload.
- Confirm the regenerated merge has 970 ml Distilled water, the final-volume-normalized main salts, and one row per final stock addition.
- Run open schema, strict schema, reference, and term validation on the maintained specialized input and regenerated merge.
- Re-check the `high_metal: true` flag after stock rows are nested so stock metal concentrations do not masquerade as final-medium concentrations.

## Additional Notes

- A failed J771 fetch made while resolving this target was discarded as unrelated; the reviewed local record is unambiguously JCM/MediaDive J391.
