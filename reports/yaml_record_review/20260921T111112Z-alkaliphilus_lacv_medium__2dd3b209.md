# YAML Record Review: alkaliphilus_lacv_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/alkaliphilus_lacv_medium__2dd3b209.yaml`
- Started UTC: 2026-09-21T11:10:02Z
- Finished UTC: 2026-09-21T11:11:13Z
- Verdict: needs curation

## Target

| Field | Observed value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:002257` |
| Name | `alkaliphilus_lacv_medium` |
| Original name | `ALKALIPHILUS LACV MEDIUM` |
| Source identity | JCM Medium J1077, `mediadive.medium:J1077` |
| Generated status | Generated merged record |
| Generated path | `data/merge_yaml/merged/alkaliphilus_lacv_medium__2dd3b209.yaml` |
| Maintained inputs | `data/normalized_yaml/bacterial/alkaliphilus_lacv_medium.yaml`; `data/normalized_yaml/bacterial/alkaliphilus_3b_medium.yaml` |

The merged output joins two JCM media that are already represented as a concentration-variant pair in the normalized layer:

- `alkaliphilus_lacv_medium.yaml`: JCM Medium J1077, `CultureMech:002257`
- `alkaliphilus_3b_medium.yaml`: JCM Medium J1078, `CultureMech:002258`

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/alkaliphilus_lacv_medium__2dd3b209.yaml` | Passed; no issues found. |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/alkaliphilus_lacv_medium__2dd3b209.yaml --out /private/tmp/alkaliphilus_lacv_medium__2dd3b209.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 `ERROR` rows emitted. |
| Reference | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/alkaliphilus_lacv_medium__2dd3b209.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/alkaliphilus_lacv_medium__2dd3b209.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Documented focused validator | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/`. |

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints are unavailable in this checkout because project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before target-specific validation. The no-project commands above exercise the same schema and validation code with Python 3.11.

## Identity and Grounding

The stable identity says this record is Alkaliphilus LacV medium from JCM J1077:

- `id: CultureMech:002257`
- `name: alkaliphilus_lacv_medium`
- `media_term.term.id: mediadive.medium:J1077`
- `notes: Source: JCM | Link: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1077`

The recipe body no longer matches that identity. The generated `ingredients` list contains the 3B/JCM J1078 values for three distinguishing concentrations:

| Ingredient | Generated value | JCM J1077 LacV source | JCM J1078 3B source |
| --- | ---: | ---: | ---: |
| NaCl | 0.993049 g/L | 10 g in the source base recipe | 1 g in the source base recipe |
| Na2S2O3 x 5 H2O | 1.48957 g/L | 3 g in the source base recipe | 1.5 g in the source base recipe |
| Yeast extract | 50 g/L | 20 ml of 10% sterile anaerobic stock | 50 ml of 10% sterile anaerobic stock |

This also conflicts with the normalized variant metadata embedded into the same generated record. Its `variant_modifications` state that LacV should increase NaCl from 0.993049 to 9.93049 g/L, increase thiosulfate from 1.48957 to 2.97915 g/L, and lower yeast extract from 50 to 20 g/L, but the merged top-level concentrations remain 0.993049, 1.48957, and 50.

Grounding is partially correct for exact salts but has these identity gaps:

- `Yeast extract` is still ungrounded even though the local label index contains `FOODON:03315426`.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride, `CHEBI:34887`, not a hexahydrate-specific term.
- `HCl` is modeled as a direct 12.5 g/L ingredient even though JCM 439 lists 12.5 ml of 25% HCl inside a trace-element stock solution, and that stock is added to JCM 1077 at 1 ml/L.

## Evidence

Inspected source documents:

- JCM J1077, fetched from `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1077`
- JCM J1078, fetched from `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1078`
- JCM 439 trace-element solution, fetched from `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439`

Supported claims:

- JCM J1077 supports the LacV identity, pH 8.5 final target, liquid complex undefined classification, the same basal salts, Tris base, resazurin, and the N2 to N2-CO2 gas replacement recorded in the preparation prose.
- JCM J1077 supports using JCM 439 trace-element solution at 1 ml per liter of medium.
- JCM J1078 supports the same Alkaliphilus 3B identity and the current generated 0.993049 g/L NaCl, 1.48957 g/L thiosulfate, and 50 ml 10% yeast-extract formulation.
- JCM 439 supports the individual trace-element stock recipe that was flattened into the record.

Unsupported or mismatched claims:

- The generated LacV recipe does not support its own source identity because the distinguishing J1077 concentrations were overwritten with J1078 values during duplicate merging.
- The generated `merged_from` claim treats J1077 and J1078 as duplicate recipes, but the normalized records intentionally model them as `CONCENTRATION_VARIANT` siblings.
- The top-level trace-element ingredients are present at full JCM 439 stock strength, approximately 1000 times the intended final-medium concentration before accounting for the stock's final volume.
- The sterile anaerobic additions of 20 ml 10% yeast extract, 20 ml 0.5 M crotonic acid at pH 7.0, 20 ml 8% Na2CO3, and 6 ml 5% Na2S x 9H2O are truncated from `preparation_steps` and partly misrepresented as `G_PER_L` ingredient concentrations.

## Completeness

Consequential gaps:

- The generated record does not preserve both members of the Alkaliphilus 3B/LacV concentration-variant pair.
- The post-autoclave stock additions are not fully represented as stock volumes or solution references.
- JCM 439 is not modeled as a nested trace-element solution added at 1 ml/L.
- The preparation text loses the source table that names each sterile anaerobic stock addition.
- Growth targets are absent; no focused target-organism search was performed during this review.

Empty optional slots correctly left empty:

- No target organism was asserted in the generated record, so no unsupported growth claim is present.
- No storage conditions were asserted.
- No discussion or quality flags were asserted; the merge error should be represented in the normalized owner records or merge rules as part of a future curation edit.

Bounded absence checks:

- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -type f -name '*alkaliphilus_lacv_medium__2dd3b209.md'` search found no pre-existing report for this generated record before this report was written.

## Findings

### Blocker

1. **J1077 and J1078 were merged even though they are concentration variants, leaving the LacV record with the wrong J1078 concentrations.**

   Evidence: `data/merge_yaml/merged/alkaliphilus_lacv_medium__2dd3b209.yaml` has the JCM J1077 ID, label, source URL, and stable `CultureMech:002257` identity, but its root concentrations for NaCl, Na2S2O3 x 5 H2O, and yeast extract match JCM J1078. The normalized JCM J1077 input already contains LacV-specific 9.93049 g/L NaCl, 2.97915 g/L thiosulfate, and 20 ml yeast-extract stock values, while the normalized 3B input contains 0.993049 g/L NaCl, 1.48957 g/L thiosulfate, and 50 ml yeast-extract stock values.

   Owner: fix `data/normalized_yaml/bacterial/alkaliphilus_lacv_medium.yaml`, `data/normalized_yaml/bacterial/alkaliphilus_3b_medium.yaml`, or the merge exclusion/rule that generated `merge_fingerprint: 2dd3b209...`, then regenerate `data/merge_yaml/merged/`.

### Major

1. **Post-autoclave sterile stock volumes are stored as gram-per-liter ingredient concentrations.**

   Evidence: JCM J1077 lists 20 ml 10% yeast extract, 20 ml 0.5 M crotonic acid, 20 ml 8% Na2CO3, and 6 ml 5% Na2S x 9H2O as stocks added after autoclaving. The record stores `Crotonic acid: 20 G_PER_L`, `Na2CO3: 20 G_PER_L`, and `Na2S x 9 H2O: 6 G_PER_L`; those numbers are source stock volumes, not final grams per liter.

   Owner: model these as `solutions` with `ML_PER_L` additions or derive final amounts from explicit stock concentrations in `data/normalized_yaml/bacterial/alkaliphilus_lacv_medium.yaml`, then regenerate.

2. **JCM 439 trace-element stock was flattened into the main medium at stock strength.**

   Evidence: JCM J1077 calls for 1 ml JCM 439 trace-element solution per liter. JCM 439 itself contains HCl, FeSO4 x 7H2O, H3BO3, MnCl2 x 4H2O, CoCl2 x 6H2O, NiCl2 x 6H2O, CuCl2 x 2H2O, ZnSO4 x 7H2O, and Na2MoO4 x 2H2O in the trace stock; the current medium places those stock concentrations directly into the root ingredient list.

   Owner: introduce or reuse a normalized JCM 439 solution reference and link it from `data/normalized_yaml/bacterial/alkaliphilus_lacv_medium.yaml` at 1 ml/L before regenerating.

3. **The preparation procedure truncates the sterile anaerobic addition table.**

   Evidence: generated step 1 ends immediately after "Add the following solutions from sterile anaerobic stocks (autoclaved and stored under a N2 atmosphere):" and step 2 only says to check final pH around 8.5. The four additions that JCM J1077 lists after cooling are missing from the prose.

   Owner: complete the maintained `preparation_steps` in `data/normalized_yaml/bacterial/alkaliphilus_lacv_medium.yaml` or improve the JCM importer so the post-autoclave addition table is preserved, then regenerate.

4. **Two ingredient groundings are absent or hydration-inexact.**

   Evidence: `Yeast extract` has no ontology term, and `NiCl2 x 6 H2O` is grounded to anhydrous `CHEBI:34887`. Hydration state changes the source reagent identity for an exact JCM trace solution.

   Owner: resolve `Yeast extract` against `FOODON:03315426`, keep nickel chloride hexahydrate unresolved or map it to an exact hydrated term only if one is available, and rerun the ingredient enrichment over the normalized owners.

### Minor

None found.

## Recommended Edits

1. Exclude the Alkaliphilus LacV and 3B normalized records from duplicate merging so JCM J1077 and JCM J1078 remain distinct `CONCENTRATION_VARIANT` recipes in generated outputs.
2. Restore the JCM J1077 LacV concentrations for NaCl, Na2S2O3 x 5 H2O, and yeast-extract stock addition in the LacV normalized owner record.
3. Model 20 ml 10% yeast extract, 20 ml 0.5 M crotonic acid at pH 7.0, 20 ml 8% Na2CO3, and 6 ml 5% Na2S x 9H2O as post-autoclave stock additions rather than top-level `G_PER_L` facts.
4. Model JCM 439 as a trace-element solution used at 1 ml/L instead of flattening full-strength stock rows onto the main medium.
5. Complete the preparation step so the post-autoclave stock list is not truncated.
6. Ground `Yeast extract` to `FOODON:03315426`, and replace or clear the hydration-inexact nickel chloride hexahydrate mapping.
7. Regenerate generated merge records and rendered products from the normalized owner data.

## Follow-up Checks

- Rerun schema, strict, reference, and term validators on both normalized owners and the regenerated JCM J1077 and JCM J1078 merged records.
- Rerun the merge verifier to confirm `alkaliphilus_lacv_medium.yaml` and `alkaliphilus_3b_medium.yaml` no longer collapse to one `merge_fingerprint`.
- Manually diff the regenerated JCM J1077 ingredients against the JCM page to confirm 10 g NaCl, 3 g Na2S2O3 x 5 H2O, 20 ml 10% yeast extract, and the 1 ml/L JCM 439 trace solution are preserved.
- Manually inspect the rendered pages to verify LacV and 3B still cross-link as concentration variants.
- Check the ingredient enrichment report for exact yeast-extract and nickel chloride hexahydrate outcomes.

## Additional Notes

- This review is read-only. It intentionally leaves `data/merge_yaml/merged/alkaliphilus_lacv_medium__2dd3b209.yaml`, the normalized owners, and generated pages unchanged.
- Generated files under `data/merge_yaml/merged/` are derived artifacts. Corrections belong in `data/normalized_yaml/bacterial/alkaliphilus_lacv_medium.yaml`, `data/normalized_yaml/bacterial/alkaliphilus_3b_medium.yaml`, or the merge/importer/enrichment rule that owns the bad transform.
