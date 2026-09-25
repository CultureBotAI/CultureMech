# YAML Record Review: thermoproteus_medium__8de60bd4

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoproteus_medium__8de60bd4.yaml`
- Started UTC: 2026-09-25T10:34:00Z
- Finished UTC: 2026-09-25T10:39:03Z
- Verdict: needs curation

## Target

- Reviewed generated TOGO M2676 record `CultureMech:009231`.
- Media term: `TOGO:M2676`, `Thermoproteus Medium`.
- Source claims in the record point to DSMZ Medium 185.

## Validation

- Schema validation: passed with `linkml-validate`; no issues found.
- Strict validation: passed; `/private/tmp/thermoproteus_medium__8de60bd4.strict.tsv` was header-only with 1 line and 0 error rows.
- Reference validation: passed; 0 checks were configured for this record.
- Term validation: passed; only the known `eutils`/`pkg_resources` deprecation warning was emitted.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged YAML.

## Identity and Grounding

- TOGO M2676, DSMZ Medium 185, and MediaDive medium 185 identify Thermoproteus Medium at pH 5.5.
- DSMZ 185 uses one main medium with a 1 ml/L Trace elements solution stock.
- An exact ignored-inclusive search found the same DSMZ 185 source as a direct generated record at `thermoproteus_medium__ec4b4683.yaml` and a KOMODO generated record at `THERMOPROTEUS_MEDIUM.yaml`.

## Evidence

- `/private/tmp/DSMZ_Medium185.txt` lists 1 ml Trace elements solution in the main recipe, a separate Trace elements stock, 1 mg/L resazurin, and 1000 ml distilled water.
- `/private/tmp/mediadive_185.json` mirrors DSMZ 185 as main solution 185 plus Trace elements solution 312.
- `/private/tmp/togo_M2676.json` shows that TOGO M2676 also preserves the top-level 1 ml Trace elements solution separately from its stock paragraph.
- Local duplicate detection was rerun with `rg --no-ignore --hidden` against exact current source IDs and filenames, so ignored generated indexes were included.

## Completeness

- The generated record includes the DSMZ 185 main ingredients and the Trace elements stock contents.
- It flattens the Trace elements stock into the top-level ingredient list.
- It leaves the Trace elements addition as an empty `Unknown solution` placeholder at `1 G_PER_L`.
- The preparation steps are absent.

## Findings

- Basal water and trace-stock water were summed into one 2000 g/L top-level `Distilled water` ingredient.
- The source 1 ml/L Trace elements addition was migrated to an empty solution placeholder with unit `G_PER_L`.
- Source milligram rows were imported as grams: NaF 840 g/L, MnCl2 x 4 H2O 180 g/L, Na2B4O7 x 10 H2O 450 g/L, ZnSO4 x 7 H2O 22 g/L, CuCl2 x 2 H2O 5 g/L, Na2MoO4 x 2 H2O 3 g/L, and CoSO4 x 7 H2O 1 g/L.
- DSMZ 185 is split across TOGO, direct DSMZ, and KOMODO generated outputs.

## Recommended Edits

- Repair `data/normalized_yaml/archaea/TOGO_M2676_Thermoproteus_Medium.yaml` so Trace elements solution remains nested with a 1 ml/L main-medium addition.
- Convert source milligram rows to g/L only when normalizing units.
- Keep basal water and stock water in their own recipe compartments.
- De-duplicate the repaired TOGO M2676 record with the existing direct DSMZ and KOMODO DSMZ 185 records after all three preserve the same nested Trace elements stock.

## Follow-up Checks

- Rebuild the merged YAML and confirm no Trace elements stock rows remain in the top-level ingredient list.
- Re-run schema, strict, reference, and term validation on the regenerated DSMZ 185 target.
- Re-run exact ignored-inclusive searches for `TOGO_M2676_Thermoproteus_Medium` and `mediadive.medium:185` to confirm DSMZ 185 has one generated output.

## Additional Notes

- An initial local source search for this batch included speculative `mediadive.medium:88` and `mediadive.medium:1149` patterns that matched unrelated Sulfolobus and Oceanithermus records; I discarded that output and reran the search with exact current source IDs.
