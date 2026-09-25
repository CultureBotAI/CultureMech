# YAML Record Review: Mollicutes MZ-XQ Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mollicutes_mz_xq_medium.yaml
- Started UTC: 2026-09-24T13:57:41Z
- Finished UTC: 2026-09-24T13:58:44Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:007772 |
| Name | mollicutes_mz_xq_medium |
| Original name | Mollicutes MZ-XQ Medium |
| Primary source owner | data/normalized_yaml/bacterial/TOGO_M1242_Mollicutes_MZ-XQ_Medium.yaml |
| Merged source owner | data/normalized_yaml/bacterial/medium_for_marine_spirochaetes.yaml |
| Generated record | Yes; produced under data/merge_yaml/merged with merge_fingerprint 932a7b0611f5fdff572bc00307ef6199a810e883f2ab2701437d1f4cb5b684e7 |

## Validation

| Check | Result |
| --- | --- |
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mollicutes_mz_xq_medium.yaml` | Passed; `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/mollicutes_mz_xq_medium.yaml --out /private/tmp/mollicutes_mz_xq_medium.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows, and the TSV contained only the header. |
| `linkml-reference-validator validate data data/merge_yaml/merged/mollicutes_mz_xq_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 references were checked. |
| `linkml-term-validator validate-data data/merge_yaml/merged/mollicutes_mz_xq_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the expected `eutils` / `pkg_resources` warning. |
| Embedded `curation_history` | Not checked: the documented history validator targets the standalone `history/` corpus, not inline `MediaRecipe.curation_history`. |

## Identity and Grounding

The primary identity is TOGO M1242 / JCM_M1160, `Mollicutes MZ-XQ Medium`, and JCM GRMD 1160. TOGO M1242 and the live JCM GRMD 1160 page agree on the basal formula, 2 ml of M278 trace vitamins, 1 ml of M888 trace minerals, 1 ml of M888 Se/W solution, 25/6/6 ml post-autoclave stock additions, and N2-CO2 4:1 preparation.

The merged synonym `medium_for_marine_spirochaetes` is not an exact duplicate. It resolves to TOGO M1232 / JCM_M1150, `Medium For Marine Spirochaetes`, and the live JCM GRMD 1150 page differs from M1242 in at least three material amounts: 40 g NaCl instead of 25 g, 1.7 g glucose instead of 1.8 g, and 1 ml trace vitamins from M278 instead of 2 ml.

An ignored-inclusive search over `data/normalized_yaml` and `data/merge_yaml` for M1242, JCM_M1160, GRMD 1160, M1232, JCM_M1150, GRMD 1150, and `medium_for_marine_spirochaetes` found this merged TOGO record, the normalized TOGO M1232 source, an unrelated NBRC_M1232 string, and old direct-JCM generated siblings for both JCM pages: `data/merge_yaml/merged/mollicutes_mz_xq_medium__aa7ddd0e.yaml` and `data/merge_yaml/merged/MEDIUM_FOR_MARINE_SPIROCHAETES.yaml`. Those direct-JCM records use the same GRMD 1160 and 1150 URLs but have separate CultureMech IDs.

The CHEBI groundings for NaCl, KH2PO4, NH4Cl, resazurin, glucose, carbon dioxide, and nitrogen are appropriate. CaCl2 x 2 H2O and MgCl2 x 6 H2O have direct CHEBI `term` values but no mirrored `mediaingredientmech_chebi_term` values.

## Evidence

| Source claim | Generated representation | Assessment |
| --- | --- | --- |
| TOGO M1242 / JCM 1160 has 25 g NaCl, 1.8 g glucose, and 2 ml M278 trace vitamins | The final merged recipe keeps those M1242 values and demotes M1232 to a synonym | M1232 is over-merged because its formula has 40 g NaCl, 1.7 g glucose, and 1 ml M278 trace vitamins. |
| 1 mg resazurin per liter | `Resazurin` is `1 G_PER_L` | The dose is 1000x too high if interpreted as grams per liter. |
| 2 ml M278 trace vitamins, 1 ml M888 trace minerals, 1 ml M888 Se/W solution | Three empty `Unknown solution` rows with `2`, `1`, and `1 G_PER_L` | These are ml stock additions and the referenced stock compositions are not structured. |
| 25 ml 8% NaHCO3, 6 ml 5% Na2S x 9 H2O, and 6 ml 5% L-Cysteine-HCl-H2O | Three empty `Unknown solution` rows with `25`, `6`, and `6 G_PER_L` | These are post-autoclave ml additions, not gram-per-liter ingredients. |
| Adjust pH to 7.5, boil/cool under N2-CO2 4:1, dispense under the same gas, seal with butyl rubber stoppers, autoclave, then aseptically and anaerobically add the listed stocks | No preparation steps in the generated record | The anaerobic workflow is unsupported by the structured record. |

M278 and M888 are whole TOGO records that contain the referenced stocks. The MZ-XQ recipe should reference only the `Trace vitamins solution` from M278 and the `Trace mineral solution` and `Se/W solution` from M888, or copy those subcomponents narrowly.

## Completeness

No empty optional scalar fields are present, and the absent target organism list is not a schema defect for this provider recipe.

The generated record is incomplete for stock handling: all six stock rows have empty `composition`, default `Unknown solution` names, and gram-per-liter units copied from milliliter source amounts. It is also incomplete for cultivation setup because the N2-CO2 4:1 atmosphere and anaerobic post-autoclave additions only survive as two unquantified gas ingredient rows.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | TOGO M1232 was merged into TOGO M1242 even though it is a distinct JCM recipe. | JCM GRMD 1160 / TOGO M1242 uses 25 g NaCl, 1.8 g glucose, and 2 ml M278 trace vitamins; JCM GRMD 1150 / TOGO M1232 uses 40 g NaCl, 1.7 g glucose, and 1 ml M278 trace vitamins. | Merge de-duplication over `data/normalized_yaml/bacterial/TOGO_M1242_Mollicutes_MZ-XQ_Medium.yaml` and `data/normalized_yaml/bacterial/medium_for_marine_spirochaetes.yaml`. |
| Major | Six solution rows store source milliliter additions as grams per liter. | TOGO M1242 lists 2, 1, 1, 25, 6, and 6 ml additions; the YAML stores those numbers as `G_PER_L`. | The two TOGO normalized owners and the TOGO solution import / `solution-migrator-v1.0` path. |
| Major | M278 and M888 stock references are empty placeholders. | The referenced trace vitamins, trace minerals, and Se/W stocks resolve to subcomponents of whole media M278 and M888; the YAML has only `Unknown solution` rows with no `composition`. | The two TOGO normalized owners; cross-reference handling needs to import only the named subcomponents. |
| Major | The resazurin concentration is 1000x too high. | JCM and TOGO list 1 mg resazurin, while both normalized inputs and the merged output store `1 G_PER_L`. | The TOGO unit importer for M1242 and M1232. |
| Major | The anaerobic preparation instructions are absent from the generated record. | The live JCM and TOGO comments specify pH 7.5, N2-CO2 4:1 boiling/cooling, anaerobic dispensing, butyl stoppers, autoclaving, and sterile post-autoclave stock additions. | The two TOGO normalized owners. |
| Major | Direct-JCM duplicates for both merged sources are still present. | The ignored-inclusive search found generated direct-JCM records for GRMD 1160 and GRMD 1150 with separate CultureMech IDs. | Legacy JCM/MediaDive normalized records and source de-duplication before `merge_recipes.py`. |
| Minor | Hydrate salts lack mirrored MediaIngredientMech CHEBI terms. | CaCl2 x 2 H2O has CHEBI:86158 and MgCl2 x 6 H2O has CHEBI:86345, but neither row has `mediaingredientmech_chebi_term`. | MediaIngredientMech enrichment over the normalized TOGO owners. |

## Recommended Edits

1. Split TOGO M1232 / JCM_M1150 back out of the TOGO M1242 merge unless a curator documents why the NaCl, glucose, and trace-vitamin differences are equivalent.
2. In both TOGO normalized owners, encode all six solution additions as milliliter stock additions with source-specific volumes and useful stock names.
3. Resolve M278 and M888 stock references by copying or linking only their named trace vitamins, trace minerals, and Se/W subcomponents.
4. Correct resazurin from `1 G_PER_L` to `0.001 G_PER_L` or an equivalent 1 mg/L representation.
5. Add the pH 7.5 and N2-CO2 4:1 anaerobic preparation text to both TOGO normalized owners, preserving the wording difference about cooling and post-autoclave addition timing between GRMD 1160 and GRMD 1150.
6. Reconcile or suppress the old direct-JCM normalized records for GRMD 1160 and GRMD 1150 so neither provider page emits a second generated record.
7. Refresh MediaIngredientMech CHEBI enrichment for CaCl2 x 2 H2O and MgCl2 x 6 H2O after curation.

## Follow-up Checks

- Rerun `linkml-validate`, `scripts/validate_strict.py`, `linkml-reference-validator`, and `linkml-term-validator` on the regenerated M1242 and M1232 records.
- Manually compare regenerated YAML against live JCM GRMD 1160 and 1150 to verify that M1242 remains 25 g NaCl / 1.8 g glucose / 2 ml trace vitamins and M1232 remains 40 g NaCl / 1.7 g glucose / 1 ml trace vitamins.
- Run an ignored-inclusive search for `GRMD=1160`, `GRMD=1150`, `TOGO:M1242`, and `TOGO:M1232` across `data/normalized_yaml` and `data/merge_yaml` to confirm that stale direct-JCM duplicates were de-duplicated.
- Inspect M278 and M888 handling and verify that whole SI Medium and Spirochaeta Medium recipes were not inlined where only local stock subcomponents are referenced.

## Additional Notes

Live JCM pages for GRMD 1160 and GRMD 1150 were available during review and agreed with the corresponding TOGO API records.
