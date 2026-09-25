# YAML Record Review: ANAEROCELLUM medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml
- Started UTC: 2026-09-21T12:30:25Z
- Finished UTC: 2026-09-21T12:33:47Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:005874` |
| Name | `anaerocellum_medium` |
| Source accession | `komodo.medium:516` |
| Source label | `ANAEROCELLUM medium` |
| Generated status | Generated merge from `KOMODO_516_ANAEROCELLUM_medium`, `anaerocellum_medium`, `for_dsm_6724`, and `medium_516_modified_for_dsm_9003` |

The reviewed file is a generated merge rooted on the KOMODO Medium 516 duplicate. It keeps `data/normalized_yaml/bacterial/anaerocellum_medium.yaml` as a `SOURCE_DUPLICATE` parent and treats the two KOMODO strain records, `for_dsm_6724` and `medium_516_modified_for_dsm_9003`, as duplicate children.

The exhaustive identity search used `rg --no-ignore --hidden` across `data`, `scripts`, `tests`, `history`, and `src` for the target label, exact source accessions, and all four CultureMech IDs. It found the DSMZ parent, three KOMODO normalized records, the generated merge, generated indexes/import reports, the `scripts/repair_komodo_516_anaerocellum_score10.py` topology repair, and its regression test.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml` | Passed with no issues reported |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml --out /private/tmp/ANAEROCELLUM_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were available |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` inside one generated merge |

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` wrappers remain unavailable for focused review in this checkout because project `uv` resolves through Python 3.13 and attempts to build `llvmlite==0.46.0`, whose setuptools build currently aborts with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project Python 3.11 commands above exercise the same record-level validators without building the project.

## Identity and Grounding

The root identity is a KOMODO/ModelSEED duplicate of DSMZ/MediaDive Medium 516. Its own `media_term` and accession are internally aligned with `komodo.medium:516`, and the maintained normalized KOMODO record was intentionally kept under the DSMZ/MediaDive `CultureMech:001648` record as `SOURCE_DUPLICATE` on 2026-09-13.

The generated merge is stale relative to the maintained topology. `data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml` now marks `for_dsm_6724` and `medium_516_modified_for_dsm_9003` as `STRAIN_SPECIFIC_VARIANT` children, and both child files point back to the KOMODO hub with `variant_relationship: STRAIN_SPECIFIC_VARIANT`. The generated merge still emits both children as `SOURCE_DUPLICATE` records because it preserves the 2026-08-06 merge state.

DSMZ Medium 516 shows that the strain-specific relationship is real and formula-changing:

- DSM 6724 replaces 5.00 g/L cellobiose with 5.00 g/L soluble starch.
- DSM 9003 adds 1.00 g/L Trypticase peptone and raises yeast extract to 2.00 g/L.

The generated merge includes cellobiose at 4.99002 g/L and yeast extract at 0.499002 g/L, has no soluble starch or Trypticase peptone entry, and therefore cannot represent either strain-specific formula.

Ingredient grounding is mostly plausible for the simple salts. The `NiCl2 x 6 H2O` ingredient is grounded to anhydrous `CHEBI:34887` nickel dichloride, which is a hydration-form mismatch and should be left unresolved or re-grounded to the exact hexahydrate.

## Evidence

The generated record has no structured `references` or `source_data` block, so all source claims are carried only by `notes`, `media_term`, and merge history. I inspected DSMZ Medium 516 from `DSMZ_Medium516.pdf`; it supports the record's root label, base pH 7.1-7.3, first ten base ingredients, the use of 1.00 ml/L Trace element solution SL-10 from DSMZ Medium 320, the use of 1.00 ml/L Wolin's vitamin solution (10x) from DSMZ Medium 120, the anoxic N2/CO2 preparation, and the two DSM 6724 and DSM 9003 modifications.

The ingredients from HCl through Na2MoO4 x 2 H2O are not direct final-medium ingredients. They are the composition of Trace element solution SL-10, which DSMZ adds to the final liter at 1.00 ml/L. The generated record flattens those stock ingredients at their stock-recipe concentrations and omits the stock volume boundary.

The ingredients from Biotin through `(DL)-alpha-Lipoic acid` are not direct final-medium ingredients either. They are the composition of Wolin's vitamin solution (10x), which DSMZ adds at 1.00 ml/L after autoclaving. The generated record again stores stock-recipe concentrations as final g/L values.

The generated record also omits the DSMZ distilled-water rows: 1000 ml for the base medium, 990 ml for Trace element solution SL-10, and 1000 ml for Wolin's vitamin solution (10x).

## Completeness

The record is valid YAML and covers the base KOMODO/DSMZ accession, pH range, physical state, bacterial category, complex and semi-defined classification, and a cultivation application. Empty optional organism and growth-evidence fields are not defects in this source-only recipe review.

The consequential gaps are structural:

- no stock-solution representation for Trace element solution SL-10;
- no stock-solution representation for Wolin's vitamin solution (10x);
- no direct final-medium references that state those stock solutions are added at 1.00 ml/L;
- no distilled-water components for the base medium or the two stocks;
- no generated `preparation_steps`, even though the DSMZ parent has the N2/CO2 sparging, anoxic Hungate/serum-vial dispensing, autoclaving, sterile post-autoclave addition, filtration, and trace-stock dissolution steps;
- no exact recipe for the DSM 6724 soluble-starch variant;
- no exact recipe for the DSM 9003 Trypticase and high-yeast-extract variant.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Trace element solution SL-10 is flattened into final-medium ingredients at the wrong concentration boundary. | DSMZ Medium 516 adds 1.00 ml of Trace element solution SL-10 per 1000 ml base medium and lists HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O inside that 1000 ml stock. The generated merge stores all nine stock components as direct g/L final ingredients. | `data/normalized_yaml/bacterial/anaerocellum_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml`, followed by merge regeneration |
| Major | Wolin's vitamin solution (10x) is flattened into final-medium ingredients at stock concentrations. | DSMZ Medium 516 adds 1.00 ml of the 10x Wolin vitamin stock per 1000 ml medium. The generated record stores the stock's Biotin, Folic acid, Pyridoxine hydrochloride, Thiamine HCl, Riboflavin, Nicotinic acid, Calcium D-(+)-pantothenate, Vitamin B12, p-Aminobenzoic acid, and `(DL)-alpha-Lipoic acid` rows as direct g/L ingredients. | `data/normalized_yaml/bacterial/anaerocellum_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml`, followed by merge regeneration |
| Major | DSM 6724 and DSM 9003 are formula-changing variants, but the generated merge still treats their KOMODO children as exact source duplicates. | The generated `variant_children` entries for `CultureMech:005872` and `CultureMech:005873` are `SOURCE_DUPLICATE`. The maintained KOMODO child files now declare `STRAIN_SPECIFIC_VARIANT`, and DSMZ Medium 516 changes the carbon source for DSM 6724 and supplements the recipe for DSM 9003. | `data/normalized_yaml/bacterial/for_dsm_6724.yaml`, `data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml`, and merge regeneration |
| Major | The strain-specific child recipes still contain the unmodified base formulation. | `for_dsm_6724.yaml` still contains Cellobiose and lacks soluble starch. `medium_516_modified_for_dsm_9003.yaml` still contains 0.499002 g/L Yeast extract and lacks the 1.00 g/L Trypticase peptone supplement. DSMZ Medium 516 requires the opposite for those strains. | `data/normalized_yaml/bacterial/for_dsm_6724.yaml` and `data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml` |
| Major | DSMZ preparation details are lost from the generated KOMODO-rooted merge. | The maintained DSMZ parent carries preparation text for N2/CO2 sparging, anoxic dispensing, autoclaving, stock-solution atmospheres, filtration of vitamin and cellobiose stocks, carbonate handling, final pH, and SL-10 stock preparation. The generated merge has no `preparation_steps`. | Merge rule or canonical-root selection for the four-record family |
| Minor | The nickel chloride hexahydrate row is grounded to anhydrous nickel dichloride. | The source and preferred term are `NiCl2 x 6 H2O`; the record stores `CHEBI:34887` with label `nickel dichloride`. Hydration is identity-significant. | All four normalized inputs, followed by merge regeneration |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/anaerocellum_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml`, replace the flattened SL-10 and Wolin-vitamin direct rows with structured stock solutions and 1.00 ml/L final-medium additions, retaining DSMZ stock formulations and distilled-water makeup volumes.
2. Regenerate `data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml` from the normalized inputs so the generated record no longer preserves the 2026-08-06 duplicate topology.
3. Edit `data/normalized_yaml/bacterial/for_dsm_6724.yaml` so the DSM 6724 variant replaces cellobiose with 5.00 g/L soluble starch from a sterile anoxic stock solution.
4. Edit `data/normalized_yaml/bacterial/medium_516_modified_for_dsm_9003.yaml` so the DSM 9003 variant has 2.00 g/L Yeast extract and adds 1.00 g/L Trypticase peptone.
5. Fix the merge rule or canonical-root selection so the generated KOMODO-rooted merge inherits the maintained DSMZ preparation steps or picks the DSMZ/MediaDive parent as the canonical projection for Medium 516.
6. Remove the anhydrous `CHEBI:34887` grounding from `NiCl2 x 6 H2O` in the normalized inputs unless an exact nickel chloride hexahydrate term is available in the packaged MediaIngredientMech label index.

## Follow-up Checks

1. Run `just validate-schema` and `just validate-strict` on each edited normalized YAML file.
2. Run `just validate-terms` on each edited normalized YAML file after replacing or removing the nickel chloride grounding.
3. Run `just verify-merges` and `just audit-merge-freshness` after regenerating the merge.
4. Re-open the regenerated `data/merge_yaml/merged/ANAEROCELLUM_MEDIUM.yaml` and manually verify that the direct ingredients contain only DSMZ final-medium ingredients plus stock additions, that both stock-solution formulas retain their own water makeup, and that DSM 6724/DSM 9003 remain formula-changing strain variants.

## Additional Notes

The source lookup covered ignored files where relevant: the exact record/ID/accession search used `rg --no-ignore --hidden`. A broader follow-up search for the DSMZ variant terms was noisy across unrelated records and did not support any absence claim.

The 2026-09-13 repair script correctly repaired the parent/child relationship fields in the normalized KOMODO files but asserted a hard-coded shared ingredient signature for all three KOMODO records. That same signature is exactly why the two formula-changing DSMZ variants still project as base-medium copies.
