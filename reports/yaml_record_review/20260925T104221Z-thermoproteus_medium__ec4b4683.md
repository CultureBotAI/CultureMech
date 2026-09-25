# YAML Record Review: thermoproteus_medium__ec4b4683

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoproteus_medium__ec4b4683.yaml`
- Started UTC: 2026-09-25T10:39:00Z
- Finished UTC: 2026-09-25T10:42:21Z
- Verdict: needs curation

## Target

- Reviewed generated direct DSMZ 185 record `CultureMech:001275`.
- Media term: `mediadive.medium:185`, `THERMOPROTEUS MEDIUM`.
- Source claims in the record point to DSMZ Medium 185 through MediaDive.

## Validation

- Schema validation: passed; exited 0 with no diagnostics.
- Strict validation: passed; `/private/tmp/thermoproteus_medium__ec4b4683.strict.tsv` was header-only with 1 line and 0 error rows.
- Reference validation: passed; exited 0 with no diagnostics.
- Term validation: passed; exited 0 with no diagnostics.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged YAML.

## Identity and Grounding

- DSMZ Medium 185 and MediaDive medium 185 identify Thermoproteus Medium at pH 5.5.
- DSMZ 185 adds 1 ml/L Trace elements solution to the main medium and defines that trace stock separately.
- An exact ignored-inclusive search found the same DSMZ 185 source in this direct record, the KOMODO 185 record, and TOGO M2676.

## Evidence

- `/private/tmp/DSMZ_Medium185.txt` lists the main DSMZ 185 ingredients, 1 ml Trace elements solution, 1 mg/L resazurin, 1000 ml distilled water, and the separate Trace elements stock.
- `/private/tmp/mediadive_185.json` mirrors DSMZ 185 as main solution 185 plus Trace elements solution 312.
- `/private/tmp/togo_M2676.json` confirms that TOGO M2676 is another import of DSMZ Medium 185.
- Local duplicate detection was rerun with `rg --no-ignore --hidden` against exact DSMZ 185 and Thermoproteus Neutrophilus identifiers, so ignored generated indexes were included.

## Completeness

- The generated record keeps pH 5.5 and the DSMZ preparation text.
- It omits the source 1000 ml distilled-water row.
- It flattens Trace elements solution into the top-level ingredient list and loses the explicit 1 ml/L stock addition.
- The trace-stock values are at the stock g/L concentrations, not inflated as in the TOGO M2676 record.

## Findings

- The source Trace elements stock is not modeled as a nested solution.
- The source 1 ml/L Trace elements addition is missing from the main recipe.
- Distilled water is absent.
- DSMZ 185 is split across direct, KOMODO, and TOGO generated outputs.

## Recommended Edits

- Repair `data/normalized_yaml/archaea/thermoproteus_medium.yaml` or the MediaDive import path so Trace elements solution remains nested with a 1 ml/L addition.
- Preserve the main 1000 ml distilled-water row.
- Reground sulfur from sulfur atom to elemental sulfur.
- Merge the repaired direct DSMZ 185 source with the repaired KOMODO and TOGO DSMZ 185 records.

## Follow-up Checks

- Rebuild the merged YAML and confirm Trace elements is nested.
- Re-run schema, strict, reference, and term validation on the regenerated DSMZ 185 target.
- Re-run exact ignored-inclusive searches for `mediadive.medium:185`, `KOMODO_185_THERMOPROTEUS_medium`, and `TOGO_M2676_Thermoproteus_Medium`.

## Additional Notes

None found.
