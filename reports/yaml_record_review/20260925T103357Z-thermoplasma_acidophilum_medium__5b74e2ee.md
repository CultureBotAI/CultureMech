# YAML Record Review: thermoplasma_acidophilum_medium__5b74e2ee

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoplasma_acidophilum_medium__5b74e2ee.yaml`
- Started UTC: 2026-09-25T10:30:00Z
- Finished UTC: 2026-09-25T10:33:57Z
- Verdict: needs curation

## Target

- Reviewed generated TOGO M2384 record `CultureMech:008967`.
- Media term: `TOGO:M2384`, `Thermoplasma Acidophilum Medium`.
- Source claims in the record point to `https://togomedium.org/medium/M2384` and DSMZ Medium 158.

## Validation

- Schema validation: passed; exited 0 with no diagnostics.
- Strict validation: passed; `/private/tmp/thermoplasma_acidophilum_medium__5b74e2ee.strict.tsv` was header-only with 1 line and 0 error rows.
- Reference validation: passed; 0 checks were configured for this record.
- Term validation: passed; exited 0 with no diagnostics.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged YAML.

## Identity and Grounding

- TOGO M2384, DSMZ Medium 158, and MediaDive medium 158 identify the same Thermoplasma Acidophilum Medium.
- DSMZ Medium 158 uses a main medium with 10 ml/L Trace element solution and a separate trace stock.
- An exact ignored-inclusive search found the same original DSMZ 158 source in the direct DSMZ merge `thermoplasma_acidophilum_medium__d7d3722d.yaml` and in the KOMODO DSMZ 158 merge `thermoplasma_acidophilum_medium__3d517987.yaml`.

## Evidence

- `/private/tmp/togo_M2384.json` preserves the TOGO top-level paragraph and the Trace element solution paragraph separately.
- `/private/tmp/DSMZ_Medium158.txt` and `/private/tmp/mediadive_158.json` confirm that the main recipe adds Trace element solution at 10 ml/L and that the stock contains 1000 ml distilled water plus full-strength trace salts.
- Local duplicate detection was run with `rg --no-ignore --hidden` and an explicit boundary on `mediadive.medium:158`, so ignored generated indexes were included without matching MediaDive IDs 1580 through 1589.

## Completeness

- The generated record includes the main salts, yeast extract, glucose, H2SO4 pH adjustment, and trace-stock salts.
- The source hierarchy is not preserved: Trace element solution exists only as an empty `Unknown solution` placeholder at `10 G_PER_L`, while its contents are also flattened into the top-level ingredient list.
- The TOGO importer summed the main 1000 ml water and stock 1000 ml water into a top-level 2000 g/L water row.

## Findings

- The 10 ml/L Trace element solution was migrated to a solution placeholder with unit `G_PER_L` instead of `ML_PER_L`.
- Stock milligram rows were imported as grams: Na2MoO4 x 2 H2O is 3 g/L instead of 0.003 g/L, ZnSO4 x 7 H2O is 22 g/L instead of 0.022 g/L, CuCl2 x 2 H2O is 5 g/L instead of 0.005 g/L, VOSO4 x 5 H2O is 3.8 g/L instead of 0.0038 g/L, and CoSO4 x 7 H2O is 2 g/L instead of 0.002 g/L.
- Full-strength trace-stock rows are incorrectly present in the basal medium.
- DSMZ 158 is split across three generated outputs instead of one canonical source representation.

## Recommended Edits

- Repair `data/normalized_yaml/archaea/TOGO_M2384_Thermoplasma_Acidophilum_Medium.yaml` so Trace element solution remains nested with a 10 ml/L main-medium addition.
- Convert milligram trace-stock rows to g/L values only when normalizing units.
- Keep main water and stock water in their own recipe compartments.
- Merge the repaired TOGO M2384 record with the direct DSMZ 158 and KOMODO 158 records once their normalized formulations agree.

## Follow-up Checks

- Rebuild the merged YAML and confirm that no trace-stock rows remain as top-level basal ingredients.
- Re-run schema, strict, reference, and term validation on the regenerated DSMZ 158 target.
- Re-run an exact ignored-inclusive search for `TOGO_M2384_Thermoplasma_Acidophilum_Medium`, `KOMODO_158_THERMOPLASMA_ACIDOPHILUM_medium`, and `mediadive.medium:158` to confirm that DSMZ 158 is no longer split.

## Additional Notes

None found.
