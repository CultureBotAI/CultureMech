# YAML Record Review: marine_aob_medium_b

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_aob_medium_b.yaml
- Started UTC: 2026-09-23T23:39:13Z
- Finished UTC: 2026-09-23T23:40:16Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | data/merge_yaml/merged/marine_aob_medium_b.yaml |
| Class | MediaRecipe |
| ID | CultureMech:007644 |
| Label | marine_aob_medium_b |
| Source identity | TOGO:M1123, Marine AOB Medium (B), original source JCM_M1056 |
| Generation state | Generated merge under data/merge_yaml/merged; repair data/normalized_yaml/bacterial/marine_aob_medium_b.yaml, data/normalized_yaml/bacterial/marine_aob_medium_a.yaml, or merge_recipes.py rather than this file |

The merged record resolves to the TOGO import of JCM 1056 for Marine AOB Medium B, but it has also merged in Marine AOB Medium A as a duplicate and synonym.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_aob_medium_b.yaml` | Passed; `No issues found` |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_aob_medium_b.yaml --out /private/tmp/marine_aob_medium_b.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_aob_medium_b.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_aob_medium_b.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning |
| Embedded curation history | Not checked | `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries |

## Identity and Grounding

- `TOGO:M1123` and the JCM URL `GRMD=1056` both identify Marine AOB Medium B.
- TOGO M1123 reports `original_media_id` `JCM_M1056`, `name` `Marine AOB Medium (B)`, JCM URL `GRMD=1056`, and post-autoclave `ph` 7.5.
- JCM 1056 reports `1056 MARINE AOB MEDIUM (B)`.
- MediaDive `J1056` reports the same JCM link and `MARINE AOB MEDIUM (B)` with `min_pH` 7 and `max_pH` 7.
- Marine AOB Medium A is a distinct salinity variant: TOGO M1122/JCM 1055 list 29.22 g NaCl, while TOGO M1123/JCM 1056 list 40.95 g NaCl. The generated B record incorrectly contains `synonyms` and `merged_from` entries for `marine_aob_medium_a`.
- Most ingredient groundings preserve the salt or hydrate named by JCM/TOGO. One exception is `CoCl2 x 6 H2O`: the B record names the hexahydrate but grounds it to generic `CHEBI:35696` cobalt dichloride; the sibling MediaDive J1056 import uses `CHEBI:53503` cobalt chloride hexahydrate.

## Evidence

- The inspected JCM 1056 and TOGO M1123 sources support the B recipe main-solution quantities of 40.95 g NaCl, 1.652 g `(NH4)2SO4`, 7.394 g `MgSO4 x 7 H2O`, 4.066 g `MgCl2 x 6 H2O`, 1.470 g `CaCl2 x 2 H2O`, 0.746 g KCl, 21.2 mg `Na2CO3`, 0.252 g `NaHCO3`, 15.7 mg `K2HPO4`, 1.0 ml of 1.0 mg/ml EDTA-Fe(III) solution, 1.0 ml trace elements solution, 2.5 ml phenol red 0.04%, and 1.0 L distilled water.
- The merged record is not evidence-faithful for B because it carries 29.22 g/L NaCl from the A source instead of B's 40.95 g/L NaCl.
- The TOGO import correctly captured `Na2CO3` and `K2HPO4` values numerically but converted the source `mg` rows to `G_PER_L`, inflating both by 1000x.
- The record also flattens the trace element stock into main-medium ingredients as 241.95, 197.91, 287.56, 237.93, and 249.68 `G_PER_L` rows. JCM and TOGO support those as mg amounts inside a 1 L trace-element stock, and support only a 1 ml addition of that stock to the main medium.
- The source supports 1.0 ml of 1.0 mg/ml EDTA-Fe(III) solution and 2.5 ml of phenol red 0.04%; the record stores those as `1` and `2.5` `G_PER_L`.
- JCM 1056 supports the preparation text `Adjust pH to 7.0 with HCl. After autoclave, pH goes up to around 7.5.` The B merged record has HCl as a variable ingredient but loses that text as a preparation step and has no explicit `ph_value`.

## Completeness

- The represented source recipe is materially incomplete because the two stock-solution entries have `name: Unknown solution` and empty `composition` arrays despite TOGO and MediaDive exposing the trace-element stock composition and the EDTA-Fe(III) stock identity.
- The record has no target-organism or growth-evidence claims. That is not a defect for this review because the source recipe pages inspected here only establish the formulation.
- Exact gitignore-independent searches were run for `marine_aob_medium_b`, `Marine AOB Medium (B)`, `TOGO:M1123`, `JCM_M1056`, `GRMD=1056`, `CultureMech:007644`, the A/B merge fingerprints, and `marine_aob_medium_a` across the scoped normalized and merged YAML/index trees with `--no-ignore --hidden`; the relevant maintained owners found were the bacterial TOGO A/B records and specialized MediaDive JCM A/B records.
- An exact `find reports/yaml_record_review -maxdepth 1 -name '*-marine_aob_medium_b.md' -print` search, which includes ignored files, found no pre-existing Marine AOB Medium B review before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | Marine AOB Medium A was merged into the generated Marine AOB Medium B canonical record as a duplicate and synonym, causing the B record to advertise TOGO M1123/JCM 1056 while carrying A-specific NaCl. | JCM 1055/TOGO M1122 list A with 29.22 g NaCl; JCM 1056/TOGO M1123 list B with 40.95 g NaCl. The merged B record lists `NaCl` as 29.22 g/L and `synonyms: marine_aob_medium_a`. | data/normalized_yaml/bacterial/marine_aob_medium_a.yaml, data/normalized_yaml/bacterial/marine_aob_medium_b.yaml, and the duplicate fingerprint logic in `merge_recipes.py` |
| major | TOGO milligram quantities were normalized as grams per liter. | JCM 1056 lists `Na2CO3` 21.2 mg and `K2HPO4` 15.7 mg; the record stores 21.2 and 15.7 `G_PER_L`. The MediaDive J1056 import shows the expected normalized values of 0.0211155 g/L and 0.0156374 g/L. | data/normalized_yaml/bacterial/marine_aob_medium_b.yaml and the TOGO importer |
| major | Trace-element stock contents are represented as main-medium grams-per-liter ingredients instead of a 1 ml stock addition backed by stock composition. | JCM/TOGO put `Na2MoO4 x 2 H2O`, `MnCl2 x 4 H2O`, `ZnSO4 x 7 H2O`, `CoCl2 x 6 H2O`, `CuSO4 x 5 H2O`, and distilled water under `Trace elements solution`; the record promotes the salt amounts as top-level `G_PER_L` rows and leaves the solution `composition` empty. | data/normalized_yaml/bacterial/marine_aob_medium_b.yaml and the TOGO solution migration/import path |
| major | Liquid stock additions are stored as mass concentrations. | JCM/TOGO support `1.0 ml` EDTA-Fe(III) solution and `2.5 ml` phenol red 0.04%, but the merged record stores `1 G_PER_L` and `2.5 G_PER_L`. | data/normalized_yaml/bacterial/marine_aob_medium_b.yaml and the TOGO importer |
| minor | The JCM pH/preparation instruction is not represented in structured preparation or pH fields. | JCM 1056 and TOGO M1123 include the pH-7.0 adjustment and the post-autoclave pH note; the specialized J1056 import has `ph_value: 7.0` and a preparation step, but the canonical merged B record has neither. | data/normalized_yaml/bacterial/marine_aob_medium_b.yaml |
| minor | `CoCl2 x 6 H2O` is grounded to generic cobalt dichloride. | The source ingredient is the hexahydrate; data/normalized_yaml/specialized/marine_aob_medium_b.yaml already resolves that label to `CHEBI:53503` cobalt chloride hexahydrate, while this generated record has `CHEBI:35696`. | data/normalized_yaml/bacterial/marine_aob_medium_b.yaml |

## Recommended Edits

1. Split Marine AOB Medium A and B during merge generation so the TOGO A/B pair remains two canonical records related as salinity variants, matching the already curated MediaDive JCM A/B parent/child relationship.
2. Re-import or repair `data/normalized_yaml/bacterial/marine_aob_medium_b.yaml` so JCM source `mg` rows normalize to g/L values, not raw milligram numbers tagged as `G_PER_L`.
3. Represent the trace-elements stock as a stock solution with its own 1 L composition, and keep only the 1 ml stock addition on the main medium.
4. Represent the EDTA-Fe(III) and phenol red rows as volume additions from liquid stocks or leave their volume semantics explicit rather than converting them to unsupported mass concentrations.
5. Carry the pH 7.0 preparation instruction and post-autoclave pH note from JCM/TOGO into a preparation step and an appropriately scoped pH field.
6. Re-ground `CoCl2 x 6 H2O` to a cobalt chloride hexahydrate term such as the `CHEBI:53503` mapping already present in the MediaDive J1056 import.

## Follow-up Checks

- Rebuild merged recipes and confirm `data/merge_yaml/merged/marine_aob_medium_b.yaml` no longer lists `marine_aob_medium_a` under `synonyms` or `merged_from`.
- Compare the regenerated B record against JCM 1056/TOGO M1123 row-by-row and verify NaCl is 40.95 g or 40.7869 g/L, not the A value 29.22 g.
- Run the open schema, strict schema, reference, and term validators on the repaired B record and on the regenerated merge.
- Manually confirm the trace-element stock, EDTA-Fe(III) addition, phenol red addition, and pH/preparation text against JCM 1056 after the importer or normalized YAML repair.
- Re-run exact `rg --no-ignore --hidden` checks for `160a1b38a910f2a483693d3686f973a55d9e6b149aad777381a8411ffaed63eb` and `c863190c56220917a9a2b27635924cc31145be527046c57467135a3c5df30503` under `data/merge_yaml/merged` to verify no A/B merge fingerprint continues to publish the false duplicate.

## Additional Notes

- The `high_metal: true` flag is very likely a derived artifact of the stock-solution flattening bug because the B record has trace-element stock ingredients at hundreds of g/L. Revisit it after the trace stock has been nested correctly.
- The maintained MediaDive import has correct B-source identity, pH 7.0, normalized main-solution g/L values, and correct A/B salinity-variant links; it is useful as a cross-check but should not be treated as an independent source overriding JCM.
