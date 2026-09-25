# YAML Record Review: ANAEROLINEA medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml
- Started UTC: 2026-09-21T12:38:05Z
- Finished UTC: 2026-09-21T12:38:57Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:003504` |
| Name | `anaerolinea_medium` |
| Source accession | `komodo.medium:1004` |
| Source label | `ANAEROLINEA medium` |
| Generated status | Generated merge from `KOMODO_1004_ANAEROLINEA_medium`, `anaerolinea_medium`, `for_dsm_16554_dsm_16555_and_dsm_17877`, `for_dsm_16556`, and `for_dsm_22659` |

The reviewed file is the generated merge for KOMODO Medium 1004, an exact duplicate of DSMZ/MediaDive Medium 1004. It is distinct from the JCM/NBRC `anaerolinea_medium*` records in the merge corpus.

The exhaustive identity search used `rg --no-ignore --hidden` across `data/normalized_yaml`, `data/merge_yaml/merged`, `scripts`, `tests`, and `history` for exact labels, accessions, five CultureMech IDs, and the three child slugs. It found the DSMZ and KOMODO normalized records, three KOMODO child records, the reviewed merge, generated indexes, and `scripts/repair_komodo_1004_anaerolinea_score10.py`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml` | Passed with no issues reported |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml --out /private/tmp/ANAEROLINEA_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were available |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` inside one generated merge |

The documented `just` wrappers still fail before focused validation in this checkout because project `uv` resolves with Python 3.13 and attempts to build `llvmlite==0.46.0`, whose setuptools build aborts with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project Python 3.11 commands above validate the generated record without building the project.

## Identity and Grounding

The root is correctly identified as KOMODO Medium 1004 and points to the DSMZ/MediaDive Medium 1004 duplicate. The generated topology is stale: the maintained `KOMODO_1004_ANAEROLINEA_medium.yaml` was repaired on 2026-09-13 to keep DSMZ Medium 1004 as a `SOURCE_DUPLICATE` parent and to classify `for_dsm_16554_dsm_16555_and_dsm_17877`, `for_dsm_16556`, and `for_dsm_22659` as `STRAIN_SPECIFIC_VARIANT` children. The generated merge still marks all three as `SOURCE_DUPLICATE` children and synonyms.

DSMZ Medium 1004 proves that at least three of those child wrappers are formula-changing:

- DSM 16554, DSM 16555, and DSM 17877 replace glucose with 7.20 g/L sucrose and reduce yeast extract to 0.10 g/L.
- DSM 16556 omits glucose and reduces yeast extract to 0.10 g/L.
- DSM 22659 increases glucose to 5.00 g/L.

All three maintained KOMODO child files still contain the base `D-Glucose` and `Yeast extract` rows. A gitignore-independent exact search of those three files found `D-Glucose` and `Yeast extract`, but found no `sucrose` or `cellobiose` rows.

DSMZ Medium 1004 also documents two variants that are not represented by named normalized wrappers in this family: DSM 23815 replaces glucose with 2.00 g/L cellobiose, and DSM 103421 reduces yeast extract to 0.1 g/L. An `rg --no-ignore --hidden` search for the exact strings `DSM 23815` and `DSM 103421` across `data`, `scripts`, `tests`, and `history` found no exact matches; digit-only searches for `23815` and `103421` produced only unrelated numeric substrings.

The `NiCl2 x 6 H2O` ingredient is grounded to anhydrous `CHEBI:34887` nickel dichloride instead of exact nickel chloride hexahydrate.

## Evidence

The generated record has no structured `references` or `source_data` block. I inspected `DSMZ_Medium1004.pdf`; it supports the root label, final pH 7.0, final volume 1003 ml, the first ten direct base rows from KH2PO4 through Na2S x 9 H2O, the three 1.00 ml/L stock-solution additions, the base preparation sequence, and the five DSM-specific modification notes.

Trace element solution SL-11 from DSMZ Medium 722 is flattened. The generated Na2-EDTA x 2 H2O through Na2MoO4 x 2 H2O rows belong inside that 1000 ml stock, not directly in final ANAEROLINEA MEDIUM.

Selenite-tungstate solution from DSMZ Medium 385 is flattened. The generated NaOH, Na2SeO3 x 5 H2O, and Na2WO4 x 2 H2O rows are a 1000 ml stock added at 1.00 ml/L.

Wolin's vitamin solution from DSMZ Medium 120 is flattened. The generated Biotin through `(DL)-alpha-Lipoic acid` rows are stock ingredients, not direct final g/L amounts.

## Completeness

The root duplicate and base pH are present, and the generated record carries DSMZ's base preparation and SL-11 preparation text.

The important gaps are:

- no stock-solution representation for Trace element solution SL-11;
- no stock-solution representation for Selenite-tungstate solution;
- no stock-solution representation for Wolin's vitamin solution;
- no 1.00 ml/L final-medium references for those three stocks;
- no base-water, trace-stock water, selenite-tungstate-stock water, or vitamin-stock water rows;
- no generated strain-variant relationships from the maintained 2026-09-13 repair;
- no sucrose and low-yeast-extract recipe for DSM 16554/DSM 16555/DSM 17877;
- no glucose-free low-yeast-extract recipe for DSM 16556;
- no 5.00 g/L glucose recipe for DSM 22659;
- no normalized variant wrappers found for DSM 23815 or DSM 103421.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated merge is stale relative to the maintained 2026-09-13 topology. | `KOMODO_1004_ANAEROLINEA_medium.yaml` now marks the three KOMODO children as `STRAIN_SPECIFIC_VARIANT`; the generated merge still marks them as `SOURCE_DUPLICATE` and emits them as synonyms. | Merge regeneration from `data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml` and its children |
| Major | Three documented strain variants still carry the base glucose and yeast-extract formulation. | DSMZ Medium 1004 changes glucose and/or yeast extract for DSM 16554/16555/17877, DSM 16556, and DSM 22659. Exact searches of their normalized wrappers still found base `D-Glucose` and `Yeast extract` rows and no replacement sucrose. | `data/normalized_yaml/bacterial/for_dsm_16554_dsm_16555_and_dsm_17877.yaml`, `data/normalized_yaml/bacterial/for_dsm_16556.yaml`, and `data/normalized_yaml/bacterial/for_dsm_22659.yaml` |
| Major | Three DSMZ stock solutions are flattened into direct ingredients. | The source adds 1.00 ml/L each of Trace element solution SL-11, Selenite-tungstate solution, and Wolin's vitamin solution. The generated record stores every stock component as a direct final g/L ingredient. | `data/normalized_yaml/bacterial/anaerolinea_medium.yaml`, `data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml`, and the three child variants |
| Major | Two DSMZ-documented strain variants have no named CultureMech wrappers found. | DSMZ Medium 1004 lists additional formula changes for DSM 23815 and DSM 103421; the exhaustive exact search found no exact string match for either strain number. | New normalized variant records or a maintained KOMODO/DSMZ Medium 1004 variant source, if one exists upstream |
| Minor | The water makeup rows are absent. | DSMZ lists 1000 ml distilled water in the 1003 ml base recipe and 1000 ml distilled water in each of the three stock solutions; these water rows are not represented. | Same normalized owner set as the stock-solution repair |
| Minor | Nickel chloride hexahydrate is grounded to anhydrous nickel dichloride. | The source ingredient is `NiCl2 x 6 H2O`; the generated row stores `CHEBI:34887` with label `nickel dichloride`. | All five normalized inputs, followed by merge regeneration |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/ANAEROLINEA_MEDIUM.yaml` from normalized inputs so it picks up the 2026-09-13 `STRAIN_SPECIFIC_VARIANT` links.
2. In the DSMZ and KOMODO base records, replace the flattened SL-11, Selenite-tungstate, and Wolin-vitamin ingredients with structured stock solutions plus 1.00 ml/L final-medium additions.
3. Apply the DSMZ glucose/sucrose/yeast-extract modifications to `for_dsm_16554_dsm_16555_and_dsm_17877.yaml`, `for_dsm_16556.yaml`, and `for_dsm_22659.yaml`.
4. Decide whether DSM 23815 and DSM 103421 need new maintained variant records; if so, allocate IDs and add wrappers for the cellobiose and low-yeast variants.
5. Preserve DSMZ water rows in the base and three stock recipes.
6. Clear `CHEBI:34887` from `NiCl2 x 6 H2O` unless an exact nickel chloride hexahydrate grounding is present in the packaged ingredient index.

## Follow-up Checks

1. Run `just validate-schema`, `just validate-strict`, and `just validate-terms` on all edited normalized records.
2. Run `just assign-ids-check` if new DSM 23815 or DSM 103421 wrappers are added.
3. Run `just verify-merges` and `just audit-merge-freshness` after merge regeneration.
4. Re-open the regenerated merge and verify that the three existing KOMODO children remain strain variants with the correct substrate/yeast changes and that stock components no longer appear as direct final-medium g/L ingredients.

## Additional Notes

The searched source set included ignored files wherever the report makes a negative claim. The similarly named `JCM_J434_ANAEROLINEA_MEDIUM.yaml`, `anaerolinea_medium_b.yaml`, and `anaerolinea_medium_c.yaml` records are separate JCM/NBRC media and were not treated as duplicates of DSMZ/KOMODO Medium 1004.
