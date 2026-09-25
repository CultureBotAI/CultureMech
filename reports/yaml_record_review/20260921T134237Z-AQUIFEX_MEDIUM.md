# YAML Record Review: Aquifex Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml
- Started UTC: 2026-09-21T13:41:22Z
- Finished UTC: 2026-09-21T13:42:38Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| Stable ID | CultureMech:009054 |
| Name | aquifex_medium |
| Original name | Aquifex Medium |
| Category | bacterial |
| Source | TOGO:M247 imported from JCM_M255 |
| Reviewed artifact | data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml, with generated merge output under data/merge_yaml/merged/ |

This review targeted the generated canonical merge for the TOGO/JCM Aquifex import; `merged_from` contains only `TOGO_M247_Aquifex_Medium`.

An ignored-file-inclusive exact search for `AQUIFEX_MEDIUM`, `Aquifex`, `aquifex_medium`, and `AQUIFEX` covered `data/normalized_yaml`, `data/merge_yaml`, `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, `reports/media_content_review_manifest.tsv`, `data/import_tracking/reports/concentration_plausibility.tsv`, and `data/import_tracking/reports/merged_duplicates.tsv`. It found this TOGO/JCM owner and merge, a separate MediaDive/JCM `aquifex_medium.yaml` owner for the same JCM Medium 255 source, generated indexes, registry/catalog rows, manifest rows for both owners, and the Hydrogenothermus medium that reuses the MediaDive Aquifex record.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml`; no issues found. |
| Strict schema | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml --out /private/tmp/AQUIFEX_MEDIUM.strict.tsv --workers 1 --quiet`; 1 file scanned, 0 error rows. |
| Reference validator | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; 1 file validated, 0 total active checks. |
| Term validator | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`; only the upstream `eutils`/`pkg_resources` deprecation warning was emitted. |
| Embedded curation history | Not checked: this repository exposes `just validate-history` for standalone `history/` files, not a focused `MediaRecipe.curation_history` check for one merged recipe. |

Mechanical validators pass; they do not detect the unit, solution-reference, and duplicate-source issues below.

## Identity and Grounding

The source identity is correct: TOGO `M247` names `Aquifex Medium`, carries `original_media_id: JCM_M255`, and points at the live JCM Medium 255 page, which is titled `AQUIFEX MEDIUM`.

This record is split from another normalized owner for the same source. `data/normalized_yaml/bacterial/aquifex_medium.yaml` is `mediadive.medium:J255`, cites the same JCM GRMD 255 page, and uses the same `aquifex_medium` slug but a different stable ID, `CultureMech:002613`. That sibling expands Medium 151 and Medium 197 stocks into top-level rows; this TOGO import instead leaves both stock references empty. They should be reconciled as one JCM Medium 255 representation rather than curated independently.

The three gases mentioned in JCM preparation are represented as variable ingredients. Carbon dioxide and hydrogen are grounded, but Oxygen gas has no CHEBI term even though it should ground to dioxygen when retained as a gas component.

## Evidence

The live JCM Medium 255 page supports these top-level formulation rows:

| Component | Source amount |
| --- | ---: |
| NaCl | 30.0 g |
| MgSO4.7H2O | 7.0 g |
| MgCl2.6H2O | 5.5 g |
| KCl | 0.65 g |
| NaBr | 0.1 g |
| NaHCO3 | 2.0 g |
| NH4Cl | 0.15 g |
| K2HPO4 | 0.15 g |
| CaCl2.2H2O | 0.5 g |
| Trace minerals, see Medium No. 151 | 10.0 ml |
| (NH4)2Ni(SO4)2.6H2O | 20.0 mg |
| Na2WO4.2H2O | 0.1 mg |
| Na2SeO4 | 0.1 mg |
| Trace vitamins, see Medium No. 197 | 10.0 ml |
| Distilled water | 1.0 L |

The reviewed generated record incorrectly keeps the source numeric values but assigns `G_PER_L` to the two 10 ml stock additions, three milligram rows, and 1 L water row. It therefore records `Trace minerals` as `10 G_PER_L`, `Trace vitamins` as `10 G_PER_L`, ammonium nickel sulfate as `20 G_PER_L`, tungstate and selenate as `0.1 G_PER_L`, and water as `1 G_PER_L`.

JCM Medium 151 defines the trace minerals used by Medium 255: nitrilotriacetic acid, MgSO4.7H2O, MnSO4.xH2O, NaCl, FeSO4.7H2O, CoSO4.7H2O, CaCl2.2H2O, ZnSO4.7H2O, CuSO4.5H2O, AlK(SO4)2, H3BO3, Na2MoO4.2H2O, and distilled water, with an NTA/KOH pH adjustment. JCM Medium 197 defines the trace vitamins used by Medium 255: Biotin, Folic acid, Pyridoxine.HCl, Thiamine.HCl, Riboflavin, Nicotinic acid, Calcium pantothenate, Vitamin B12, p-Aminobenzoic acid, Lipoic acid, and distilled water.

The generated record drops JCM Medium 255's procedure: adjust pH to 6.0, filter-sterilize, dispense under H2-CO2 4:1, seal with butyl rubber stoppers, replace the gas phase with H2-CO2-O2 79:20:1, pressurize to 200 kPa with the same gas mixture, and readjust pH to 5.5-6.0 if necessary.

## Completeness

Consequential gaps:

- `Trace minerals` and `Trace vitamins` are unresolved empty `solutions`, and their 10 ml amounts use the wrong unit.
- Three source milligram rows are off by factors of 1000 or more.
- The final water row has the wrong concentration unit.
- The JCM filtration, gas-handling, pressure, and pH instructions are absent.
- The TOGO/JCM and MediaDive/JCM imports for JCM Medium 255 remain separate records despite having the same source page.

No organism growth claims or variants are asserted, and those optional fields do not need generic placeholders for this source formulation.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| major | Source units are corrupted during the TOGO import. | JCM Medium 255 lists 10 ml trace minerals, 20 mg ammonium nickel sulfate, 0.1 mg tungstate, 0.1 mg selenate, 10 ml trace vitamins, and 1 L water; the YAML stores those exact numbers with `G_PER_L`. | Correct `data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml` or the TOGO importer unit mapping. |
| major | JCM stock-solution references are empty and dimensionally wrong. | The record has empty `Trace minerals` and `Trace vitamins` solutions at `10 G_PER_L`; JCM Medium 255 adds 10 ml of the Medium 151 trace minerals and 10 ml of the Medium 197 trace vitamins. | Resolve the JCM Medium 151 and 197 stock compositions in the normalized owner or model them as source-local solution references with 10 ml/L additions. |
| major | Preparation, pH, atmosphere, and pressure are missing. | The inspected JCM page includes filter sterilization, pH 6.0 and final 5.5-6.0 adjustment, H2-CO2 4:1 dispensing, an H2-CO2-O2 79:20:1 replacement gas phase, and 200 kPa pressurization. None of those steps are represented except for generic gas rows. | Add structured preparation notes to the normalized TOGO/JCM record. |
| major | The same JCM Medium 255 source is curated twice under divergent IDs. | `TOGO_M247_Aquifex_Medium.yaml` and `aquifex_medium.yaml` both cite JCM GRMD 255 and share the `aquifex_medium` slug, but they are separate active recipes with different source transforms and incompatible stock expansion. | Reconcile the TOGO and MediaDive JCM 255 owners as source duplicates and regenerate downstream merges, including the Hydrogenothermus copy relationship that currently points at the MediaDive owner. |
| major | Classification is unsupported. | JCM Medium 255 and its referenced Medium 151/197 stocks contain only defined salts, gases, trace minerals, and trace vitamins. The TOGO record classifies the medium as `COMPLEX` / `UNDEFINED`; the MediaDive J255 sibling already classifies the same source as `DEFINED`. | Change `medium_type` and `composition_type` on the authoritative JCM 255 owner after source reconciliation. |
| minor | Oxygen gas lacks a term grounding. | The source preparation uses an H2-CO2-O2 gas phase. The generated Oxygen gas row has a variable concentration but no CHEBI term, unlike the CO2 and H2 rows. | Ground Oxygen gas to dioxygen or leave it as preparation text rather than a variable ingredient if gas rows are not intended. |

No blocker findings: the record still denotes JCM Medium 255 / Aquifex Medium, and the YAML is mechanically valid.

## Recommended Edits

1. Repair milligram, milliliter, and liter unit handling on the TOGO/JCM owner: the three milligram trace additives need milligram-derived final concentrations, the two stock additions need 10 ml/L volume additions, and water needs 1 L.
2. Replace the empty solution placeholders with JCM Medium 151 `Trace minerals` and JCM Medium 197 `Trace vitamins` compositions, scoped as stocks rather than flattened final ingredients.
3. Add the JCM Medium 255 pH, filtration, H2-CO2, H2-CO2-O2, pressure, and readjustment instructions.
4. Reconcile `data/normalized_yaml/bacterial/TOGO_M247_Aquifex_Medium.yaml` with `data/normalized_yaml/bacterial/aquifex_medium.yaml` so the same JCM GRMD 255 recipe has one authoritative normalized representation and one duplicate relationship.
5. Change the final reconciled Medium 255 classification to `DEFINED`.
6. Ground or remove the standalone Oxygen gas ingredient according to the final gas-handling representation.

## Follow-up Checks

- Run focused schema, strict, reference, and term validators on every normalized owner touched by the JCM 255 reconciliation.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/AQUIFEX_MEDIUM.yaml` and affected Hydrogenothermus merges.
- Recompare the normalized JCM 255 record against JCM Medium 255, Medium 151, and Medium 197: top-level amounts, two 10 ml stock additions, three mg rows, water, pH, gases, 200 kPa pressure, and stock compositions should all align.

## Additional Notes

- The Togo payload maps the JCM Medium 255 stock links to GMDB `M142` and `M190`; the live JCM source names those references as Medium No. 151 and Medium No. 197.
- The exact duplicate/source search included ignored files and generated indexes; it found the MediaDive J255 sibling and no other source-owned Aquifex Medium 255 normalized owner in the searched paths.
