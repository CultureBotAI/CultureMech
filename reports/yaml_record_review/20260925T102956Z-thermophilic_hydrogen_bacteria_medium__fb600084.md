# YAML Record Review: thermophilic_hydrogen_bacteria_medium__fb600084

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermophilic_hydrogen_bacteria_medium__fb600084.yaml`
- Started UTC: 2026-09-25T10:24:00Z
- Finished UTC: 2026-09-25T10:29:56Z
- Verdict: needs curation

## Target

- Reviewed generated TOGO M3125 record `CultureMech:009595`.
- Media term: `TOGO:M3125`, `Thermophilic Hydrogen Bacteria Medium`.
- Source claims in the record point to `https://togomedium.org/medium/M3125` and DSMZ Medium 533.

## Validation

- Schema validation: passed with `linkml-validate`; no issues found.
- Strict validation: passed; `/private/tmp/thermophilic_hydrogen_bacteria_medium__fb600084.strict.tsv` was header-only with 1 line and 0 error rows.
- Reference validation: passed; 0 checks were configured for this record.
- Term validation: passed; only the known `eutils`/`pkg_resources` deprecation warning was emitted.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged YAML.

## Identity and Grounding

- The TOGO M3125 API record identifies the medium as Thermophilic Hydrogen Bacteria Medium, cites DSMZ Medium 533 as the original URL, and reports pH 7.0.
- DSMZ Medium 533 and MediaDive medium 533 confirm the basal DSMZ formula: NH4NO3 1 g/L, Na2HPO4 x 12 H2O 4.5 g/L, KH2PO4 1.5 g/L, MgSO4 x 7 H2O 0.2 g/L, FeSO4 x 7 H2O 10 mg/L, CaCl2 x 2 H2O 10 mg/L, NaCl 1 g/L, 0.5 ml/L Trace element solution, and 1000 ml deionized water.
- An exact ignored-inclusive search found the same DSMZ 533 source in `data/normalized_yaml/bacterial/DSMZ_533_THERMOPHILIC_HYDROGEN_BACTERIA_MEDIUM.yaml` and in the generated `data/merge_yaml/merged/THERMOPHILIC_HYDROGEN_BACTERIA_MEDIUM.yaml` direct DSMZ/KOMODO merge.

## Evidence

- `/private/tmp/togo_M3125.json` preserves the TOGO top-level paragraph and the Trace element solution paragraph separately.
- `/private/tmp/DSMZ_Medium533.txt` and `/private/tmp/mediadive_533.json` agree that the trace stock contains H2O 1000 ml, MoO3 4 mg, ZnSO4 x 7 H2O 28 mg, CuSO4 x 5 H2O 2 mg, H3BO3 4 mg, MnSO4 x 5 H2O 4 mg, and CoCl2 x 6 H2O 4 mg per liter.
- Local duplicate detection was run with `rg --no-ignore --hidden` against `data/normalized_yaml` and `data/merge_yaml/merged`, so ignored generated indexes were included in the source-ID search.

## Completeness

- The generated record keeps the gas headspace components as variable ingredients, but the source expresses them as incubation atmosphere rather than medium solutes.
- The source's nested 0.5 ml/L Trace element solution is present only as a generated `solutions` placeholder with unit `G_PER_L`.
- The TOGO subcomponent rows are also flattened into top-level ingredients, so stock water is summed with basal water and trace-salt stock concentrations are interpreted in the main ingredient list.

## Findings

- The source 1000 ml basal water and 1000 ml stock water were summed into one `H2O (deionized)` ingredient at 2000 g/L.
- Source `mg` rows were imported as `g` rows: FeSO4 x 7 H2O and CaCl2 x 2 H2O are 10 g/L instead of 0.01 g/L, and the trace-stock 2 to 28 mg/L rows appear as 2 to 28 g/L top-level ingredients.
- The 0.5 ml/L Trace element solution addition was migrated to an empty solution placeholder with concentration `0.5 G_PER_L`, losing both the source unit and the stock hierarchy.
- The same DSMZ 533 recipe is also represented by the direct DSMZ/KOMODO generated merge `THERMOPHILIC_HYDROGEN_BACTERIA_MEDIUM.yaml`.

## Recommended Edits

- Correct `data/normalized_yaml/bacterial/TOGO_M3125_Thermophilic_Hydrogen_Bacteria_Medium.yaml` so the main medium retains a 0.5 ml/L nested Trace element solution rather than flattening its stock contents into the main ingredient list.
- Convert source milligram rows to grams only when their unit is normalized, not by preserving the numeric milligram quantity as g/L.
- Keep basal water separate from stock-solution water during import and merging.
- Model the 5% O2, 80% H2, 10% CO2 headspace as a preparation or incubation condition, not as three variable medium ingredients.
- Merge or de-duplicate the TOGO M3125 representation with the existing DSMZ 533 direct/KOMODO group after the TOGO normalization is repaired.

## Follow-up Checks

- Rebuild the merged YAML from normalized sources and confirm no 2 to 28 g/L trace-stock salts remain in the top-level ingredient list.
- Re-run schema, strict, reference, and term validation on the regenerated TOGO M3125 or unified DSMZ 533 merge target.
- Re-run an exact ignored-inclusive search for `mediadive.medium:533`, `TOGO_M3125_Thermophilic_Hydrogen_Bacteria_Medium`, and `DSMZ_533_THERMOPHILIC_HYDROGEN_BACTERIA_MEDIUM` to confirm that DSMZ 533 is represented once.

## Additional Notes

None found.
