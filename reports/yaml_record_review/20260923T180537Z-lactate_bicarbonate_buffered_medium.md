# YAML Record Review: lactate_bicarbonate_buffered_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lactate_bicarbonate_buffered_medium.yaml
- Started UTC: 2026-09-23T18:04:44Z
- Finished UTC: 2026-09-23T18:05:37Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/lactate_bicarbonate_buffered_medium.yaml`, generated `MediaRecipe` record `CultureMech:010311` for TOGO/JCM lactate-bicarbonate buffered medium.

- Maintained owners: `data/normalized_yaml/bacterial/TOGO_M893_Lactate_bicarbonate_Buffered_Medium.yaml` and `data/normalized_yaml/bacterial/TOGO_M1377_Glucose_bicarbonate-Buffered_Medium.yaml`.
- Merge provenance: `merged_from` lists `TOGO_M1377_Glucose_bicarbonate-Buffered_Medium` and `TOGO_M893_Lactate_bicarbonate_Buffered_Medium`; generated merge fingerprint `660330623f57b013e3dc19bc6dd8cafa1bdb260c125ec96f4173587dfa38afde`.
- Source claim: TOGO `M893`, original JCM medium 857.
- Current generated identity: `medium_type: COMPLEX`, `composition_type: SEMI_DEFINED`, `physical_state: LIQUID`.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lactate_bicarbonate_buffered_medium.yaml`; the command exited 0 with no output. |
| Strict schema | Passed with `python scripts/validate_strict.py data/merge_yaml/merged/lactate_bicarbonate_buffered_medium.yaml --out /private/tmp/lactate_bicarbonate_buffered_medium.strict.tsv --workers 1 --quiet`. |
| Reference integrity | Passed with `linkml-reference-validator validate data data/merge_yaml/merged/lactate_bicarbonate_buffered_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; there were 0 checks. |
| Term integrity | Passed with `linkml-term-validator validate-data data/merge_yaml/merged/lactate_bicarbonate_buffered_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

An exact ignored-file-inclusive search of `data/normalized_yaml` and `data/merge_yaml` for `CultureMech:010311`, `TOGO:M893`, `TOGO:M1377`, `TOGO_M893_Lactate_bicarbonate_Buffered_Medium`, `TOGO_M1377_Glucose_bicarbonate-Buffered_Medium`, and `JCM_M857` found the two maintained normalized files and their one merged output.

TOGO M893 and the JCM 857 page both identify the lactate recipe as `Lactate+bicarbonate Buffered Medium` and say it uses JCM Medium 770 with 1.0 M sodium lactate in Solution B. TOGO M1377 and JCM 1281 identify a different `Glucose+bicarbonate-Buffered Medium` and say it uses 1.0 M glucose in Solution B. The generated merge therefore conflates two distinct carbon-source variants.

The generated record's top-level identity follows the lactate source, but `synonyms` demotes the glucose source to a synonym instead of preserving it as a separate medium. That makes `CultureMech:007916` disappear from generated `data/merge_yaml/merged` even though it differs by carbon source and by the amount of Solution A in TOGO's main solution.

## Evidence

TOGO M893 states that its main solution combines 900 ml Solution A, 50 ml Solution B, and 50 ml Solution C under CO2 and N2; Solution B contains 10 ml of 1.0 M lactate solution plus cross-referenced M798 trace-metal, vitamin, and mineral-salt solutions. It also carries JCM's final comment to use Medium 770 while replacing the betaine solution in Solution B with 1.0 M sodium lactate to yield 10.0 mM final lactate.

TOGO M1377 differs in two source-level ways: it combines 915 ml Solution A with 50 ml each of Solution B and Solution C, and its Solution B contains 10 ml of 1.0 M glucose solution instead of the lactate solution. JCM 1281 repeats the glucose replacement instruction.

The generated ingredient and solution amounts do not preserve TOGO's units or stock hierarchy. Examples:

- `Resazurin`, `Na2SeO3 x 5H2O`, and `Na2WO4 x 2H2O` are milligram rows in Solution A but are recorded as 0.5, 0.3, and 0.3 `G_PER_L`.
- Solution volumes such as 900 ml Solution A, 50 ml Solution B, 50 ml Solution C, 15 ml phosphate solution, and 10 ml lactate or glucose solution are recorded as `G_PER_L`.
- Distilled-water amounts from Solution A, B, and C are merged into a synthetic 975.5 g/L row, erasing which water belongs to which solution.

## Completeness

The record is not complete enough to reproduce the medium:

- It omits the source preparation comments: autoclave Solution A under N2-CO2, filter-sterilize Solutions B and C, stock them under N2-CO2, aseptically and anaerobically combine A, B, and C, and check the final pH at 6.9 to 7.2.
- It omits the cross-referenced compositions for the M798 phosphate, trace-metal, vitamin, and mineral-salt stock solutions.
- It flattens gas, stock solution, and water entries across multiple solution boundaries.
- It provides no structured source metadata beyond `media_term`, free-text TOGO/JCM notes, and the false glucose synonym.

Empty target organism slots are not defects in this record: the inspected TOGO and JCM source pages describe formulations and do not assert strain growth results.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The merge falsely collapses lactate and glucose carbon-source variants into one generated record. | TOGO M893/JCM 857 specify 1.0 M sodium lactate; TOGO M1377/JCM 1281 specify 1.0 M glucose, and TOGO gives different Solution A volumes for the two recipes. | Merge fingerprint logic plus both TOGO maintained owners |
| Major | Volumes and milligram rows are coerced into `G_PER_L`. | TOGO uses 900 ml, 50 ml, 15 ml, 10 ml, 1 ml, and 12.5 ml rows for solutions, and 0.5 mg or 0.3 mg rows for several Solution A components; the YAML records the numeric values as gram-per-litre concentrations. | TOGO importer or both TOGO maintained owners |
| Major | Cross-referenced M798 stock solution compositions are empty. | The source explicitly references phosphate, trace metal, vitamin, and mineral salt solutions from Medium M798, while the YAML stores those solution rows with `composition: []`. | TOGO importer or both TOGO maintained owners |
| Major | Preparation and anaerobic handling instructions are missing. | TOGO includes N2-CO2 autoclaving, N2-CO2 filter-sterile stock handling, anaerobic assembly, and final pH 6.9 to 7.2 checks; the record has no `preparation_steps`. | Both TOGO maintained owners |

## Recommended Edits

1. Split TOGO M893 and TOGO M1377 back into separate generated records by changing the merge fingerprint or duplicate-detection logic to include carbon-source solution identity and solution volumes.
2. Preserve each solution's millilitre, milligram, and gram units instead of coercing imported TOGO values to `G_PER_L`.
3. Resolve or inline the M798 phosphate, trace-metal, vitamin, and mineral-salt solution compositions.
4. Add source-supported preparation steps for Solution A, Solution B, Solution C, final anaerobic assembly, and the final pH 6.9 to 7.2 check.
5. Add structured TOGO and JCM source metadata for M893/JCM 857 and M1377/JCM 1281, then regenerate `data/merge_yaml/merged`.

## Follow-up Checks

- Rerun the open-schema, strict, reference, and term validators on regenerated records for both lactate-bicarbonate and glucose-bicarbonate media.
- Requery TOGO M893 and M1377 and confirm that lactate remains only in M893 while glucose remains only in M1377.
- Inspect the regenerated `merged_from` blocks to confirm the two TOGO records are no longer source duplicates.
- Manually verify every M893/M1377 solution amount against TOGO, including Solution A 900 ml versus 915 ml and the M798 cross-references.

## Additional Notes

The source pages contain gas labels in Japanese and hydrate separators as non-ASCII middle dots; this report normalizes them to ASCII spellings for readability only. The source data itself should preserve or explicitly normalize those labels during curation.
