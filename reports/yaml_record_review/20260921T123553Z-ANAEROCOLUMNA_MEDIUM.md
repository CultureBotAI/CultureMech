# YAML Record Review: ANAEROCOLUMNA MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROCOLUMNA_MEDIUM.yaml
- Started UTC: 2026-09-21T12:34:35Z
- Finished UTC: 2026-09-21T12:35:53Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ANAEROCOLUMNA_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:002019` |
| Name | `anaerocolumna_medium` |
| Source accession | `mediadive.medium:860` |
| Source label | `ANAEROCOLUMNA MEDIUM` |
| Generated status | Generated merge from `anaerocolumna_medium`, `for_dsm_12503`, `for_dsm_12504`, `for_dsm_12505`, `for_dsm_13105`, `for_dsm_13106_and_dsm_23801`, `for_dsm_13116`, and `hesp1_sr1_tmc4_lup_medium` |

The reviewed file is a generated DSMZ Medium 860 merge. Its immediate maintained parent is `data/normalized_yaml/bacterial/anaerocolumna_medium.yaml`; all corrections should land in that parent or the KOMODO children under `data/normalized_yaml/bacterial/`, followed by merge regeneration.

The bounded identity search used `rg --no-ignore --hidden` across `data/normalized_yaml`, `data/merge_yaml/merged`, `scripts`, `tests`, and `history` for the target label, exact source accessions, child slugs, and `CultureMech:002019`. It found the reviewed merge, the DSMZ parent, the seven expected KOMODO children, generated indexes, and the `scripts/repair_komodo_860_anaerocolumna_score10.py` topology repair plus its regression test. An accidental broader search also matched many unrelated records and was not used for absence claims.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROCOLUMNA_MEDIUM.yaml` | Passed with no issues reported |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROCOLUMNA_MEDIUM.yaml --out /private/tmp/ANAEROCOLUMNA_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROCOLUMNA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were available |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROCOLUMNA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` inside one generated merge |

The documented `just` validation wrappers still cannot run for one-record review in this checkout because project `uv` resolves through Python 3.13 and attempts to build `llvmlite==0.46.0`, whose setuptools build aborts with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The Python 3.11 no-project commands above exercise the same focused validators without building the package.

## Identity and Grounding

The root DSMZ/MediaDive identity is right: `mediadive.medium:860` and `DSMZ Medium 860` both denote ANAEROCOLUMNA MEDIUM. The record is stale relative to the maintained duplicate/variant topology, however. `data/normalized_yaml/bacterial/anaerocolumna_medium.yaml` was re-rooted on 2026-09-13 and now has seven children: exact duplicate `hesp1_sr1_tmc4_lup_medium` as `SOURCE_DUPLICATE`, plus six `STRAIN_SPECIFIC_VARIANT` KOMODO wrappers for DSM 12503, DSM 12504, DSM 12505, DSM 13105, DSM 13106/DSM 23801, and DSM 13116.

The generated merge still reflects the 2026-08-06 merge state: it has no `variant_children`, points `parent_media` at `for_dsm_12503` as a `SOURCE_DUPLICATE`, and stores all seven KOMODO records as undifferentiated `synonyms`.

DSMZ Medium 860 supports several, but not all, strain-specific child assertions:

- DSM 12504 should replace fructose with 1.0 g/L syringic acid.
- DSM 13105 and DSM 19740 should replace fructose with 2.5 g/L `Na2S2O3 x 5 H2O` and adjust complete-medium pH to 7.4.
- DSM 13106 and DSM 23801 should replace fructose with 2.0 g/L D-glucose and adjust complete-medium pH to 7.4.

The generated and maintained child recipes still carry the base 3.99202 g/L D-Fructose ingredient and do not contain syringic acid, thiosulfate, or D-glucose in the three modified KOMODO children. A gitignore-independent exact search of `for_dsm_12504.yaml`, `for_dsm_13105.yaml`, and `for_dsm_13106_and_dsm_23801.yaml` found `D-Fructose` in all three and found no `syringic`, `Na2S2O3`, or `D-glucose` rows.

The `NiCl2 x 6 H2O` stock ingredient remains grounded to anhydrous `CHEBI:34887` nickel dichloride instead of an exact nickel chloride hexahydrate term.

## Evidence

The generated merge has no structured `references` or `source_data` object; source support is carried by the DSMZ link in `notes`, source accessions, curation history, and generated merge metadata.

I inspected `DSMZ_Medium860.pdf`. It supports the base medium label, pH 7.0-7.2, the first thirteen direct medium ingredients through `Na2S x 9 H2O`, use of 1.50 ml/L Trace element solution SL-10, 1000 ml base distilled water, anoxic N2/CO2 preparation, sterile stock additions of carbonate/fructose/cysteine/sulfide, and the three DSM-specific substitution instructions above.

The generated HCl through `Na2MoO4 x 2 H2O` rows are not final-medium rows. DSMZ lists them inside Trace element solution SL-10 from Medium 320, makes the stock up to 1000 ml with 990 ml distilled water, and adds only 1.50 ml of that stock to each liter of ANAEROCOLUMNA MEDIUM.

## Completeness

The record covers the correct DSMZ/MediaDive accession, a bacterial category, liquid physical state, complex/undefined classification, a cultivation application, pH range, and DSMZ preparation text for the base recipe. Empty optional growth-evidence fields are not intrinsically wrong for this source recipe.

The consequential omissions and stale fields are:

- no stock-solution boundary for Trace element solution SL-10;
- no 1.50 ml/L final-medium addition of Trace element solution SL-10;
- no distilled-water rows for either the base medium or the SL-10 stock;
- no current generated `variant_children` list from the maintained 2026-09-13 parent;
- no syringic-acid version of the DSM 12504 wrapper;
- no thiosulfate/pH 7.4 version of the DSM 13105 wrapper;
- no glucose/pH 7.4 version of the DSM 13106/23801 wrapper.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated merge is stale relative to the maintained September 13 topology repair. | `data/normalized_yaml/bacterial/anaerocolumna_medium.yaml` now lists seven children with one exact duplicate and six strain-specific variants. The generated merge still lists no children, points to `for_dsm_12503` as a duplicate parent, and moves all KOMODO records into `synonyms`. | Merge regeneration from `data/normalized_yaml/bacterial/anaerocolumna_medium.yaml` and its seven children |
| Major | Trace element solution SL-10 is flattened into final-medium ingredients at stock concentrations. | DSMZ Medium 860 adds 1.50 ml Trace element solution SL-10 per liter. The generated merge stores HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O as direct g/L final ingredients. | `data/normalized_yaml/bacterial/anaerocolumna_medium.yaml`, the seven KOMODO children, and any source transform that flattened DSMZ Medium 320 stock components |
| Major | The formula-changing DSM 12504, DSM 13105, and DSM 13106/23801 variants still carry the base fructose recipe. | DSMZ Medium 860 says DSM 12504 replaces fructose with syringic acid, DSM 13105 replaces fructose with thiosulfate and pH 7.4, and DSM 13106/23801 replaces fructose with D-glucose and pH 7.4. The corresponding normalized wrappers still contain D-Fructose and lack those substitutes. | `data/normalized_yaml/bacterial/for_dsm_12504.yaml`, `data/normalized_yaml/bacterial/for_dsm_13105.yaml`, and `data/normalized_yaml/bacterial/for_dsm_13106_and_dsm_23801.yaml` |
| Minor | The DSMZ water rows are absent. | The source lists 1000 ml distilled water in the base recipe and 990 ml distilled water in the SL-10 stock; neither appears in the generated ingredient list. | `data/normalized_yaml/bacterial/anaerocolumna_medium.yaml`, the seven KOMODO children, and stock-solution repair |
| Minor | Nickel chloride hexahydrate is grounded to anhydrous nickel dichloride. | The source ingredient is `NiCl2 x 6 H2O`; the generated row stores `CHEBI:34887` with label `nickel dichloride`. | All eight normalized inputs, followed by merge regeneration |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/ANAEROCOLUMNA_MEDIUM.yaml` from normalized inputs so the generated projection uses the `anaerocolumna_medium.yaml` child list and no longer points back to `for_dsm_12503`.
2. In `data/normalized_yaml/bacterial/anaerocolumna_medium.yaml`, split Trace element solution SL-10 into a stock-solution record and a 1.50 ml/L final-medium reference, then propagate the same representation to the exact KOMODO duplicate and applicable strain variants.
3. Edit `data/normalized_yaml/bacterial/for_dsm_12504.yaml` to replace D-Fructose with 1.0 g/L syringic acid.
4. Edit `data/normalized_yaml/bacterial/for_dsm_13105.yaml` to replace D-Fructose with 2.5 g/L `Na2S2O3 x 5 H2O` and represent pH 7.4 as the complete-medium adjustment.
5. Edit `data/normalized_yaml/bacterial/for_dsm_13106_and_dsm_23801.yaml` to replace D-Fructose with 2.0 g/L D-glucose and represent pH 7.4 as the complete-medium adjustment.
6. Add DSMZ base and SL-10 distilled-water makeup rows in the same stock repair.
7. Remove the anhydrous `CHEBI:34887` grounding from `NiCl2 x 6 H2O` unless the packaged MediaIngredientMech label index has an exact hexahydrate term.

## Follow-up Checks

1. Run `just validate-schema` and `just validate-strict` on every edited normalized record.
2. Run `just validate-terms` on every edited normalized record after fixing or clearing the nickel chloride grounding.
3. Run `just verify-merges` and `just audit-merge-freshness` after regenerating the merge.
4. Re-open `data/merge_yaml/merged/ANAEROCOLUMNA_MEDIUM.yaml` and verify that it has the maintained seven-child topology, direct base ingredients plus a 1.50 ml/L SL-10 reference, exact water makeup rows, and formula-specific child wrappers for DSM 12504, DSM 13105, and DSM 13106/23801.

## Additional Notes

The 2026-09-13 `repair_komodo_860_anaerocolumna_score10.py` script deliberately required the same 22 direct ingredients in the parent and all KOMODO children before linking them. That guarded the topology edit but also codified the preexisting base signature in the three children that DSMZ documents as substrate variants.
