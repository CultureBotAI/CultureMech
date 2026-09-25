# YAML Record Review: 1_2_tryptic_soy_broth_anaerobic

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml`
- Started UTC: 20260921T053542Z
- Finished UTC: 20260921T053610Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:009314` |
| Slug | `1_2_tryptic_soy_broth_anaerobic` |
| Original name | `1/2 Tryptic Soy Broth (Anaerobic)` |
| Category | `bacterial` |
| Generated or maintained | Generated merge artifact |
| Maintained owner | `data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml` |
| Source accession | `TOGO:M2766` |
| Original source | DSMZ Medium 1205 |
| Merge fingerprint | `370bba1248dc95f3f3745ad1fbf48b1ed3729acc7b0e59109fe4eed939d0ec91` |

Reviewed the singleton generated merge for TOGO M2766. A gitignore-independent exact search for `CultureMech:009314`, `TOGO:M2766`, `1_2_tryptic_soy_broth_anaerobic`, and the merge fingerprint found this generated record, its normalized owner, the expected catalog/index rows, the `deep_research_priority.json` inventory entry, old validation reports, the existing filename-collision report for bacterial and specialized `1_2_tryptic_soy_broth_anaerobic.yaml`, and the direct MediaDive/DSMZ Medium 1205 owner.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml` | Passed with no output |
| Strict validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml --out /private/tmp/1_2_tryptic_soy_broth_anaerobic.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 `ERROR` rows |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded `curation_history` | Not checked | Not checked: no focused validator is documented for generated merge-file `MediaRecipe.curation_history`; the repository's `validate-history` target validates standalone history files under `history/`. |

The documented `just` validator wrappers remain blocked by the project `llvmlite==0.46.0` build under Python 3.13; the no-project `uv` commands above were used as focused equivalents.

## Identity and Grounding

- The record correctly denotes TOGO M2766, `1/2 Tryptic Soy Broth (Anaerobic)`. The inspected live TOGO `gmdb_medium_by_gmid?gm_id=M2766` payload reports `gm: http://togomedium.org/medium/M2766`, `name: 1/2 Tryptic Soy Broth (Anaerobic)`, `src_url: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1205.pdf`, and `ph: 7.2`.
- The inspected DSMZ Medium 1205 PDF identifies the original recipe as `1/2 TRYPTIC SOY BROTH (ANAEROBIC)` and lists Trypticase soy broth 13.75 g, yeast extract 1.00 g, NaCl 2.50 g, D-glucose 3.60 g, DL-Dithiothreitol 0.15 g, and distilled water 1000.00 ml.
- The inspected TOGO payload agrees with the DSMZ recipe, with the product row labeled `Tryptic Soy Broth (BD BACTO)` at 13.75 g and distilled water at 1000 ml.
- The generated record omits the Tryptic Soy Broth aggregate and inserts six full-strength commercial TSB/TSA subcomponent rows, including 15 g/L agar in a liquid anaerobic broth.
- The generated record imports TOGO's 1000 ml `Distilled water` row as `1000 G_PER_L`.
- The generated record imports the N2 and HCl cues as variable ingredients but does not preserve the source protocol that makes N2 the sparging/dispensing atmosphere and HCl the pH-adjustment reagent.

## Evidence

- The live TOGO payload supports the source identity, DSMZ URL, pH 7.2, six recipe components, N2/HCl rows, and the DSMZ anaerobic preparation paragraph.
- The inspected DSMZ PDF independently supports the 13.75 g Trypticase soy broth row, the four scalar additives, 1000 ml distilled water, pH 7.2, N2 sparging and dispensing, 121 C autoclaving for 20 min, and post-autoclave glucose and DTT stock additions.
- The six commercial TSB/TSA subcomponent rows cite Wikipedia through `supplier_catalog.product_url`; neither inspected source decomposes the 13.75 g commercial powder, and neither source includes agar.
- `src/culturemech/data/mediaingredientmech/label_index.csv` has exact mappings for Yeast extract, D-Glucose, DL-Dithiothreitol, HCl, and Trypticase-soy labels; `data/import_tracking/reports/ungrounded_ingredients.tsv` still lists `DL-Dithiothreitol (DTT)` for `CultureMech:009314`.
- A gitignore-independent exact search over the TOGO normalized owner and generated record found no top-level `references` or `reference` entries; the TOGO, DSMZ, Wikipedia, supplier, and access-date claims are preserved only as free text in `notes` and `supplier_catalog` blocks.

## Completeness

- Consequential gap: the formulation is wrong because it drops the supported 13.75 g Tryptic Soy Broth aggregate, adds unsupported subcomponents, and adds agar.
- Consequential gap: the water row has the wrong dimension.
- Consequential gap: DSMZ 1205's anaerobic preparation instructions are absent.
- Consequential gap: the same DSMZ Medium 1205 appears separately as `data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml`.
- Non-blocking grounding gap: the source-supported `Yeast Extract` and `DL-Dithiothreitol (DTT)` rows are ungrounded even though exact packaged label-index mappings exist.
- Non-blocking provenance gap: the record has no structured `references`, so focused reference validation has no source objects to traverse.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Six commercial TSB/TSA subcomponent rows are unsupported and double-count the source TSB powder. | TOGO M2766 and DSMZ 1205 list a single 13.75 g Tryptic Soy Broth/Trypticase soy broth row. The record instead omits that row and adds full-strength TSB/TSA constituents, including 15 g/L agar despite `physical_state: LIQUID`. | `data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml` |
| Major | Distilled water has the wrong unit. | TOGO M2766 lists 1000 ml distilled water, which matches DSMZ 1205; the record stores `Distilled water` as `1000 G_PER_L`. | `data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml` |
| Major | The anaerobic preparation protocol is missing. | TOGO M2766 and DSMZ 1205 specify N2 sparging, pH adjustment, dispensing under N2, 121 C autoclaving for 20 min, and filter-sterilized glucose and DTT stock additions; the record has no `preparation_steps`. | `data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml` |
| Major | DSMZ Medium 1205 exists as a separate direct MediaDive owner and generated merge record. | `data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml` uses `mediadive.medium:1205` and preserves the DSMZ ingredients and preparation text, but it is not listed in this generated record's `merged_from`. | Duplicate reconciliation across the TOGO and MediaDive DSMZ 1205 owners |
| Minor | The TOGO, DSMZ, and commercial enrichment sources are not represented as structured references. | URLs and catalog claims appear only in `notes` or `supplier_catalog`, so reference validation performed 0 checks. | `data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml` |
| Minor | Two supported ingredients are ungrounded despite exact mappings. | The packaged label index maps `Yeast extract` to `FOODON:03315426` and `DL-Dithiothreitol` to `CHEBI:18320`; the `Yeast Extract` and `DL-Dithiothreitol (DTT)` rows lack primary `term` values. | `data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml` |

## Recommended Edits

1. Replace the six commercial TSB/TSA subcomponent rows with TOGO's single `Tryptic Soy Broth (BD BACTO)` row at `13.75 G_PER_L`; leave it ungrounded unless the local wrapper mapping to `MICRO:0000113` is accepted for this exact product name.
2. Convert `Distilled water` from `1000 G_PER_L` to `1000 ML_PER_L`.
3. Preserve pH 7.2 but move the variable `N2` and `HCl` context into ordered preparation steps.
4. Add ordered preparation steps for N2 sparging, dispensing into anoxic Hungate-type tubes or serum vials, autoclaving at 121 C for 20 min, and filter-sterilized glucose and DTT stock additions under N2.
5. Ground `Yeast Extract` and `DL-Dithiothreitol (DTT)` using their exact packaged label-index mappings.
6. Add structured TOGO M2766 and DSMZ Medium 1205 references and remove unsupported Wikipedia and broad multi-supplier TSB/TSA catalog assertions from this record.
7. Reconcile this TOGO DSMZ-1205 owner with `data/normalized_yaml/specialized/1_2_tryptic_soy_broth_anaerobic.yaml` so merge generation emits one DSMZ Medium 1205 recipe.

## Follow-up Checks

- Re-run strict, term, and reference validation for `data/normalized_yaml/bacterial/1_2_tryptic_soy_broth_anaerobic.yaml`.
- Re-run merge generation and verify `data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic.yaml` carries the commercial TSB aggregate, `1000 ML_PER_L` water, no agar row, structured source references, and DSMZ anaerobic preparation text.
- Re-run merge generation and verify the TOGO and MediaDive DSMZ-1205 owners either merge together or have a documented source-level reason to remain separate.
- Add or run a TOGO import regression check that proves `ml` water rows are not mapped to `G_PER_L`.

## Additional Notes

- `data/merge_yaml/merged/1_2_tryptic_soy_broth_anaerobic__d70593aa.yaml` is the next sorted generated record and should be reviewed separately as the direct MediaDive/DSMZ singleton.
