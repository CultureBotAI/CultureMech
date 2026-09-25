# YAML Record Review: 1_2_tryptic_soy_broth_anaerobe

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobe.yaml`
- Started UTC: 20260921T053312Z
- Finished UTC: 20260921T053455Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:003953` |
| Slug | `1_2_tryptic_soy_broth_anaerobe` |
| Original name | `1/2 TRYPTIC SOY BROTH (ANAEROBE)` |
| Category | `bacterial` |
| Generated or maintained | Generated merge artifact |
| Maintained owner | `data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobe.yaml` |
| Source accession | `komodo.medium:1205` |
| Cross-source accession in notes | `mediadive.medium:1205`, DSMZ Medium 1205 |
| Merge fingerprint | `47b64747b32f3d6885853f0a440e964b2ae7481db0b7b74199be87e82517bb62` |

Reviewed the singleton generated merge for KOMODO 1205. A gitignore-independent exact search for `CultureMech:003953`, `komodo.medium:1205`, `1_2_tryptic_soy_broth_anaerobe`, and the merge fingerprint found only this generated record, its normalized owner, catalog/index rows, the `deep_research_priority.json` inventory entry, historical aggregate reports, and the July 2026 label-plausibility report that flagged the record's two now-removed FoodOn groundings as implausible.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobe.yaml` | Passed with no output |
| Strict validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobe.yaml --out /private/tmp/1_2_tryptic_soy_broth_anaerobe.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 `ERROR` rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobe.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobe.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded `curation_history` | Not checked | Not checked: no focused validator is documented for generated merge-file `MediaRecipe.curation_history`; the repository's `validate-history` target validates standalone history files under `history/`. |

The documented `just` validator wrappers remain blocked by the project `llvmlite==0.46.0` build under Python 3.13; the no-project `uv` commands above were used as focused equivalents.

## Identity and Grounding

- The record denotes KOMODO Medium 1205 / `1/2 TRYPTIC SOY BROTH (ANAEROBE)`, and its free-text notes crosswalk the record to DSMZ Medium 1205.
- The inspected DSMZ Medium 1205 PDF identifies the underlying DSMZ recipe as `1/2 TRYPTIC SOY BROTH (ANAEROBIC)` and lists six recipe rows: Trypticase soy broth 13.75 g, yeast extract 1.00 g, NaCl 2.50 g, D-glucose 3.60 g, DL-Dithiothreitol 0.15 g, and distilled water 1000.00 ml.
- The generated record preserves the DSMZ yeast extract, NaCl, D-glucose, and DL-Dithiothreitol rows, and the pH 7.2 value is source-supported.
- The DSMZ Trypticase soy broth row is missing. The first six generated ingredients are a researched decomposition of full-strength Tryptic Soy Broth / Tryptic Soy Agar, including 17 g/L pancreatic digest of casein, 3 g/L soybean digest, 2.5 g/L glucose, 5 g/L NaCl, 2.5 g/L dipotassium phosphate, and 15 g/L agar. Those rows are not DSMZ 1205 rows and are not scaled to the source's 13.75 g commercial powder.
- The DSMZ distilled-water row is missing entirely.
- `HCl` is a supported pH-adjustment reagent, but the record has flattened it to a variable ingredient and dropped the surrounding anaerobic sparging, dispensing, autoclaving, and filter-sterilized stock-addition procedure.

## Evidence

- The inspected DSMZ 1205 PDF supports the aggregate `Trypticase soy broth` row and all four scalar additions that survived into the KOMODO owner: yeast extract, NaCl, D-glucose, and DL-Dithiothreitol.
- The same PDF supports pH adjustment to 7.2 with HCl, sparging the glucose- and DTT-free basal medium with 100% N2 for 30 to 45 min, dispensing under the same gas into anoxic Hungate-type tubes or serum vials, autoclaving at 121 C for 20 min, and adding glucose and DTT from anoxic filter-sterilized stock solutions prepared under N2.
- The six commercial TSB/TSA subcomponent rows cite Wikipedia through `supplier_catalog.product_url`; the inspected DSMZ source does not decompose Trypticase soy broth into subcomponents and does not add agar to this liquid anaerobic broth.
- A gitignore-independent exact search for `mediadive.medium:1205` found `data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml`, which already preserves the five non-water DSMZ ingredient rows and the DSMZ preparation text, but the current generated target is not merged with that direct DSMZ owner.
- A gitignore-independent exact search over the KOMODO normalized owner and generated record found no top-level `references` or `reference` entries; the KOMODO, DSMZ, Wikipedia, supplier, and access-date claims are preserved only as free text in `notes` and `supplier_catalog` blocks.

## Completeness

- Consequential gap: the recipe is quantitatively wrong because the supported Trypticase soy broth aggregate and 1000 ml water rows are absent, while a full-strength TSB/TSA decomposition and agar are present.
- Consequential gap: DSMZ 1205's anaerobic preparation instructions are absent.
- Consequential gap: the same DSMZ Medium 1205 appears separately under `data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml`; this KOMODO owner should either merge with the direct DSMZ owner or be reconciled as a true KOMODO cross-reference.
- Non-blocking grounding gap: Yeast extract has an exact packaged label-index mapping to `FOODON:03315426` but is ungrounded here.
- Non-blocking provenance gap: the record has no structured `references`, so focused reference validation has no source objects to traverse.
- The record has no target-organism evidence; that is acceptable because the inspected DSMZ recipe page makes no organism-specific growth claim.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Six commercial TSB/TSA subcomponent rows are unsupported and double-count the source TSB powder. | DSMZ Medium 1205 lists `Trypticase soy broth (BD BACTO)` as a single 13.75 g row. The record instead omits that row and adds full-strength TSB/TSA constituents, including 15 g/L agar despite `physical_state: LIQUID`. | `data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobe.yaml` |
| Major | Distilled water is missing. | DSMZ Medium 1205 lists 1000.00 ml distilled water; the normalized owner has no water row. | `data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobe.yaml` |
| Major | The anaerobic preparation protocol is missing. | DSMZ 1205 specifies N2 sparging, pH adjustment, dispensing under N2, 121 C autoclaving for 20 min, and filter-sterilized glucose and DTT stock additions; the record has no `preparation_steps`. | `data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobe.yaml` |
| Major | DSMZ Medium 1205 exists as a separate direct MediaDive owner and generated merge record. | `data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml` uses `mediadive.medium:1205` and preserves the DSMZ ingredients and preparation text, but it is not listed in this generated record's `merged_from`. | Duplicate reconciliation across the KOMODO and MediaDive DSMZ 1205 owners |
| Minor | The DSMZ, KOMODO, and commercial enrichment sources are not represented as structured references. | URLs and catalog claims appear only in `notes` or `supplier_catalog`, so reference validation performed 0 checks. | `data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobe.yaml` |
| Minor | Yeast extract is ungrounded even though an exact mapping exists. | A gitignore-independent exact search of `src/culturemech/data/mediaingredientmech/label_index.csv` found `Yeast extract,preferred_term,FOODON:03315426,Yeast extract,FOODON:03315426,MAPPED,unique`; the row has no `term` or `mediaingredientmech_chebi_term`. | `data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobe.yaml` |

## Recommended Edits

1. Replace the six commercial TSB/TSA subcomponent rows with DSMZ's single `Trypticase soy broth` row at `13.75 G_PER_L`; leave it ungrounded unless the local wrapper mapping to `MICRO:0000113` is accepted for this exact product name.
2. Add `Distilled water` as `1000 ML_PER_L`.
3. Preserve the DSMZ pH 7.2 value but move the variable `HCl` claim into an ordered preparation step.
4. Add ordered preparation steps for N2 sparging, dispensing into anoxic Hungate-type tubes or serum vials, autoclaving at 121 C for 20 min, and filter-sterilized glucose and DTT stock additions under N2.
5. Ground `Yeast extract` to the exact packaged label-index mapping.
6. Add a structured DSMZ Medium 1205 reference and remove unsupported Wikipedia and broad multi-supplier TSB/TSA catalog assertions from this record.
7. Reconcile this KOMODO DSMZ-1205 owner with `data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml` so merge generation emits one DSMZ Medium 1205 recipe instead of two spellings.

## Follow-up Checks

- Re-run strict, term, and reference validation for `data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobe.yaml`.
- Re-run merge generation and verify `data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobe.yaml` no longer contains the TSB/TSA decomposition or agar row.
- Re-run merge generation and verify the KOMODO and MediaDive DSMZ-1205 owners either merge together or have a documented source-level reason to remain separate.

## Additional Notes

- `data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml` is the next sorted generated record and points at TOGO M2766; it was not adjudicated as part of this KOMODO 1205 review.
- `data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml` is the direct MediaDive/DSMZ generated copy of DSMZ Medium 1205 and should be reviewed separately.
