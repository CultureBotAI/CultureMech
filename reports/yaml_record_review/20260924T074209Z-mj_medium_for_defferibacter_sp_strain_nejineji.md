# YAML Record Review: mj_medium_for_defferibacter_sp_strain_nejineji

- Repository: CultureMech
- Record: data/merge_yaml/merged/mj_medium_for_defferibacter_sp_strain_nejineji.yaml
- Started UTC: 2026-09-24T07:42:09Z
- Finished UTC: 2026-09-24T07:43:12Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:010187`
- Generated name: `mj_medium_for_defferibacter_sp_strain_nejineji`
- Generated source file: `data/merge_yaml/merged/mj_medium_for_defferibacter_sp_strain_nejineji.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/TOGO_M779_MJ_Medium_For_Defferibacter_SP._Strain_Nejineji.yaml`
- Duplicate generated record: `data/merge_yaml/merged/mj_medium_for_defferibacter_sp_strain_nejineji__fb1ffbb2.yaml`
- Upstream source: TOGO Medium `M779`, preserving retired JCM medium `M754`

## Validation

- Open LinkML validation passed: `No issues found`.
- Strict validation passed with 0 ERROR rows in `/private/tmp/mj_medium_for_defferibacter_sp_strain_nejineji.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The generated record identity is aligned with TOGO `M779`, whose metadata points at JCM `M754`.
- The live JCM `GRMD=754` endpoint now returns `Nothing found`; TOGO still has the preserved JCM-derived formula.
- An ignored-file-inclusive exact path search found a separate hashed generated record for the same snake-cased JCM recipe from the MediaDive import.
- `media_term` points to `TOGO:M779`.
- Calcium chloride dihydrate, magnesium chloride hexahydrate, manganese chloride tetrahydrate, sodium molybdate dihydrate, sodium selenite pentahydrate, and iron chloride tetrahydrate have primary CHEBI terms but no `mediaingredientmech_chebi_term`.
- Cobalt chloride hexahydrate and nickel chloride hexahydrate are grounded to generic cobalt dichloride and nickel dichloride.
- The sodium tungstate row has no ontology grounding and preserves the source formula typo `Na2WO2 x 2 H2O`.

## Evidence

- TOGO `M779` lists 1 L distilled water, 30 g NaCl, 0.5 g `CaCl2 x 2 H2O`, 0.25 g NH4Cl, 0.14 g K2HPO4, 0.4 mg `Na2MoO4 x 2 H2O`, 0.5 mg resazurin, 6.5 g `MgCl2 x 6 H2O`, 0.1 mg H3BO3, 0.33 g KCl, 4 mg `MnCl2 x 4 H2O`, 2 mg `CoCl2 x 6 H2O`, 2 mg `NiCl2 x 6 H2O`, 0.5 mg ZnCl2, 4 mg `Na2SeO3 x 5 H2O`, 0.1 mg `Na2WO2 x 2 H2O`, 10 g sulfur, 0.25 mg `FeCl2 x 4 H2O`, carbon dioxide gas, and nitrogen gas in the first main-solution block.
- The generated record stores all of the TOGO `M779` milligram rows as gram-per-liter values; for example 0.4 mg molybdate is imported as `0.4` `G_PER_L`, 0.5 mg resazurin as `0.5` `G_PER_L`, 4 mg manganese chloride as `4` `G_PER_L`, and 0.25 mg ferrous chloride as `0.25` `G_PER_L`.
- TOGO `M779` then adds 12.5 ml of 8% NaHCO3 solution and 1 ml Trace vitamins from Medium `M190`, adds sulfide from an anaerobic stock to final 0.1 g/L, and switches the gas phase to H2-CO2.
- TOGO `M190` defines the referenced Trace vitamins stock as 1 L water plus 2 mg biotin, 5 mg p-aminobenzoic acid, 5 mg thiamine hydrochloride, 5 mg calcium pantothenate, 10 mg pyridoxine hydrochloride, 2 mg folic acid, 0.1 mg vitamin B12, 5 mg riboflavin, 5 mg nicotinic acid, and 5 mg lipoic acid.

## Completeness

- The generated record has `composition: []` for the 8% NaHCO3, Trace vitamins, and `Na2S x 9H2O` solution entries.
- The 8% bicarbonate addition was migrated as `12.5 G_PER_L`, losing both the 12.5 ml addition volume and the 8% stock concentration.
- The 1 ml M190 Trace vitamins addition is present only as an empty solution stub, so all ten vitamin-stock ingredients are absent.
- The sulfide stock entry is present only as a variable-concentration empty solution even though the source specifies a final 0.1 g/L sulfide concentration.
- The generated record keeps a literal water ingredient at 1 g/L from TOGO's 1 L solvent row.

## Findings

- High: Ten milligram-scale TOGO rows were imported as grams per liter, inflating molybdate, resazurin, borate, manganese, cobalt, nickel, zinc, selenite, tungstate, and ferrous chloride by 1000-fold.
- High: Three source solution semantics were lost during `solution-migrator-v1.0`; the generated `solutions` array has empty compositions and uses concentration values where the source gave ml additions or a final sulfide concentration.
- High: The M190 Trace vitamins reference was not resolved, so the generated recipe has no biotin, folate, pyridoxine, thiamine, riboflavin, nicotinic acid, pantothenate, B12, aminobenzoate, or lipoate content.
- Medium: A separate MediaDive/JCM import generated `mj_medium_for_defferibacter_sp_strain_nejineji__fb1ffbb2.yaml` for the same recipe identity instead of merging with the TOGO `M779` record.
- Medium: Several hydrated salts are partially grounded or missing `mediaingredientmech_chebi_term` entries after migration.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M779_MJ_Medium_For_Defferibacter_SP._Strain_Nejineji.yaml` by converting TOGO milligram quantities to gram-per-liter concentrations.
- Preserve 8% NaHCO3, M190 Trace vitamins, and sulfide as explicit solution additions with non-empty compositions.
- Import the ten M190 Trace vitamins ingredients into the Trace vitamins stock and keep their concentrations diluted through the 1 ml addition to `M779`.
- Store the sulfide addition as a final 0.1 g/L `Na2S x 9H2O` concentration instead of `VARIABLE`.
- Merge or otherwise reconcile the TOGO `M779` and MediaDive/JCM `J754` duplicate records so the same JCM recipe does not publish twice.
- Regenerate merged YAML after repairing the normalized source records.

## Follow-up Checks

- Re-fetch TOGO `M779` and TOGO `M190` and confirm every mg source row is represented as mg, not g, after import.
- Repeat the ignored-file-inclusive exact path search for `mj_medium_for_defferibacter_sp_strain_nejineji` to verify that the duplicate hashed generated record is gone or intentionally aliased.
- Confirm the M190 Trace vitamins stock has ten ingredients and no empty `composition: []` in the regenerated record.
- Confirm the 8% NaHCO3 and sulfide additions preserve their source concentrations.
- Re-run open LinkML, strict, reference, and term validation after regenerating the merged record.

## Additional Notes

- None found.
