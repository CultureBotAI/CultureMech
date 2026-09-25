# YAML Record Review: aminobacterium_shuijingfangii_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/aminobacterium_shuijingfangii_medium__b20dcce5.yaml`
- Started UTC: 2026-09-21T11:25:29Z
- Finished UTC: 2026-09-21T11:26:13Z
- Verdict: needs curation

## Target

| Field | Observed value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:002195` |
| Name | `aminobacterium_shuijingfangii_medium` |
| Original name | `AMINOBACTERIUM SHUIJINGFANGII MEDIUM` |
| Source identity | JCM Medium J1010, `mediadive.medium:J1010` |
| Generated status | Generated one-source merge |
| Generated path | `data/merge_yaml/merged/aminobacterium_shuijingfangii_medium__b20dcce5.yaml` |
| Maintained input | `data/normalized_yaml/bacterial/aminobacterium_shuijingfangii_medium.yaml` |

The generated record is a one-source merge and matches the normalized JCM owner. A separate TOGO M1067 owner imports the same original JCM_M1010 recipe.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/aminobacterium_shuijingfangii_medium__b20dcce5.yaml` | Passed; no issues found. |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/aminobacterium_shuijingfangii_medium__b20dcce5.yaml --out /private/tmp/aminobacterium_shuijingfangii_medium__b20dcce5.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 `ERROR` rows emitted. |
| Reference | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/aminobacterium_shuijingfangii_medium__b20dcce5.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/aminobacterium_shuijingfangii_medium__b20dcce5.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Documented focused validator | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/`. |

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints are unavailable in this checkout because project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before target-specific validation. The no-project commands above exercise the same schema and validation code with Python 3.11.

## Identity and Grounding

The record's top-level identity says this is JCM J1010:

- `id: CultureMech:002195`
- `name: aminobacterium_shuijingfangii_medium`
- `media_term.preferred_term: JCM Medium J1010`
- `media_term.term.id: mediadive.medium:J1010`
- `notes: Source: JCM | Link: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1010`

The direct JCM `GRMD=1010` URL now returns a JCM search page with no recipe body. TOGO M1067 still carries `original_media_id: JCM_M1010`, the same original JCM URL, and a structured copy of the JCM_M1010 formula.

The CultureMech ingredient model is wrong because stock additions are represented as final grams per liter:

- `CaCl2 x 2 H2O: 15 G_PER_L` comes from 15 ml of 1% stock.
- `MgCl2 x 6 H2O: 20 G_PER_L` comes from 20 ml of 2% stock.
- `Resazurin: 1 G_PER_L` comes from 1 ml of 1% stock.
- `NaHCO3: 0.25 G_PER_L`, `Na2S x 9 H2O: 0.1 G_PER_L`, and `L-Serine: 0.1 G_PER_L` come from 0.25 ml, 0.1 ml, and 0.1 ml solution additions per 5 ml culture, not direct g/L values.

Grounding is exact for the basal salts and most exact stock components. `Yeast extract` is ungrounded, and `NiCl2 x 6 H2O` is grounded to anhydrous `CHEBI:34887`.

## Evidence

Inspected source documents:

- JCM J1010 at `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1010`
- TOGO Medium M1067 API at `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1067`

Supported by TOGO M1067:

- The Aminobacterium shuijingfangii medium identity and JCM_M1010 original accession.
- The basal recipe: 1 g NaCl, 0.3 g KH2PO4, 0.3 g NH4Cl, 0.2 g K2HPO4, 0.5 g KCl, 2 g yeast extract, 1.38 g L-cysteine HCl x H2O, and 1 L distilled water.
- The pH 7.0 to 7.8 adjustment and anaerobic N2-CO2 4:1 preparation.
- The stock-addition set: 15 ml 1% CaCl2 x 2H2O, 20 ml 2% MgCl2 x 6H2O, 1 ml 1% resazurin, 1 ml SL-10 trace element solution from M433, 10 ml trace vitamins from M190, 0.25 ml 10% NaHCO3, 0.1 ml 3% Na2S x 9H2O, and 0.1 ml 0.5 M L-serine per 5 ml culture.

Unsupported or mismatched claims:

- The direct JCM URL no longer supports the formula.
- Stock volumes are interpreted as final `G_PER_L` concentrations throughout the JCM owner.
- SL-10 trace-element and M190 vitamin stock components are flattened into root ingredients.
- The post-autoclave stock-addition list is truncated from `preparation_steps`.

## Completeness

Consequential gaps:

- Eight stock additions are missing as structured `solutions`.
- Many stock components are at the wrong concentration layer.
- The TOGO copy of the same JCM_M1010 source is not reconciled with the JCM import.
- The primary JCM source URL is stale and needs a durable provenance note or archive.
- Target organisms are absent; no focused growth-evidence search was performed during this review.

Empty optional slots correctly left empty:

- No target organism was asserted, so there is no unsupported growth claim.
- No storage condition was asserted by the inspected TOGO mirror.

Bounded absence checks:

- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -type f -name '*aminobacterium_shuijingfangii_medium__b20dcce5.md'` search found no pre-existing report for this generated record before this report was written.
- A gitignore-independent `rg --no-ignore --hidden` search over `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for the Aminobacterium shuijingfangii slug, labels, and `b20dcce5` found this JCM owner, the adjacent TOGO M1067 owner, a distinct IRD Aminobacterium medium, this generated output, and the older uppercase TOGO generated artifact.

## Findings

### Blocker

1. **JCM_M1010 stock additions are stored as direct final-medium ingredients.**

   Evidence: TOGO M1067 encodes the stock rows as solution volumes, including 15 ml of 1% CaCl2 x 2H2O, 20 ml of 2% MgCl2 x 6H2O, 1 ml of 1% resazurin, 1 ml SL-10 trace element solution, 10 ml trace vitamins, 0.25 ml of 10% NaHCO3, 0.1 ml of 3% Na2S x 9H2O, and 0.1 ml of 0.5 M L-serine per 5 ml culture. The generated JCM record puts those additions directly in the final ingredient list as `G_PER_L` facts, including 15 g/L CaCl2 x 2 H2O, 20 g/L MgCl2 x 6 H2O, and 1 g/L resazurin.

   Owner: re-curate `data/normalized_yaml/bacterial/aminobacterium_shuijingfangii_medium.yaml` with explicit stock `solutions`, remove stock-only components from the top-level final recipe, and regenerate.

### Major

1. **The SL-10 and trace-vitamin stocks were flattened into root ingredients.**

   Evidence: the JCM owner contains HCl, FeCl2, trace metals, biotin, folic acid, pyridoxine, thiamine, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid as top-level ingredients. TOGO M1067 represents these as references to `Trace element solution SL--10 (see Medium [M433])` and `Trace vitamins (see Medium [M190])`.

   Owner: model M433 and M190 as referenced stock solutions at the volumes given by JCM_M1010.

2. **The post-autoclave stock-addition list is truncated.**

   Evidence: generated preparation step 2 ends immediately after "add per 5.0 ml the following solutions from anaerobic stocks (autoclaved or *filter-sterilized and stored under a N2 atmosphere):". The TOGO payload contains the following stock rows separately and they are not represented in prose.

   Owner: preserve the after-autoclave stock list as complete `solutions` or explicit preparation substeps in the normalized JCM owner.

3. **The JCM and TOGO copies of JCM_M1010 are unreconciled and both stock-broken.**

   Evidence: `data/normalized_yaml/bacterial/TOGO_M1067_Aminobacterium_Shuijingfangii_Medium.yaml` names the same JCM_M1010 source, but stores the same eight stock additions as empty `Unknown solution` rows with `G_PER_L` amounts and keeps N2/CO2 as variable root ingredients. Those artifacts keep it separate from the JCM generated output.

   Owner: repair TOGO M1067 with the same stock model, drop gas pseudo-ingredients from the root ingredients, and reconcile it with the JCM import during merge generation.

4. **The cited primary JCM URL is stale.**

   Evidence: fetching the current JCM `GRMD=1010` URL returned a "Nothing found" medium-search page instead of the JCM_M1010 recipe body. TOGO M1067 is only an imported mirror of that original source.

   Owner: add a durable mirror citation, archived URL, or source note to `data/normalized_yaml/bacterial/aminobacterium_shuijingfangii_medium.yaml`, then regenerate.

5. **One exact hydrated stock ingredient is misgrounded.**

   Evidence: `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride, not to the exact hexahydrate form named in the stock composition.

   Owner: preserve the hydrated label and replace or clear the ChEBI mapping unless an exact nickel chloride hexahydrate term is available.

### Minor

1. **Yeast extract is ungrounded.**

   Evidence: the inspected TOGO mirror supports the 2 g/L yeast-extract row, but the generated JCM row lacks an ontology term and `mediaingredientmech_chebi_term`.

   Owner: ground yeast extract during ingredient enrichment if an exact accepted term is available.

## Recommended Edits

1. Model the calcium chloride, magnesium chloride, resazurin, M433 trace-element, M190 trace-vitamin, bicarbonate, sulfide, and serine stocks as explicit `solutions` with source volume additions.
2. Remove stock-only salts, trace elements, vitamins, bicarbonate, sulfide, and serine from the final ingredient list.
3. Complete the post-autoclave anaerobic-stock preparation step.
4. Repair TOGO M1067 with the same stock model and reconcile the JCM and TOGO imports of JCM_M1010.
5. Add durable provenance for the now-unavailable JCM J1010 URL.
6. Fix or clear the `NiCl2 x 6 H2O` grounding and ground yeast extract.
7. Regenerate generated merge records and rendered products.

## Follow-up Checks

- Rerun schema, strict, reference, and term validators on the corrected JCM and TOGO normalized owners plus the regenerated output.
- Rerun concentration plausibility and confirm the resazurin and FeCl2 stock-strength findings disappear.
- Rerun duplicate merging and confirm the JCM and TOGO copies of JCM_M1010 no longer remain separate generated records.
- Manually compare the regenerated record against TOGO M1067 to verify every post-autoclave stock remains a nested solution with a volume, not a final `G_PER_L` value.

## Additional Notes

- This review is read-only. It intentionally leaves `data/merge_yaml/merged/aminobacterium_shuijingfangii_medium__b20dcce5.yaml`, its normalized owner, the TOGO sibling, and generated pages unchanged.
- Generated files under `data/merge_yaml/merged/` are derived artifacts. Corrections belong in `data/normalized_yaml/bacterial/aminobacterium_shuijingfangii_medium.yaml`, `data/normalized_yaml/bacterial/TOGO_M1067_Aminobacterium_Shuijingfangii_Medium.yaml`, and the import/merge rules that currently flatten or empty stock solution references.
