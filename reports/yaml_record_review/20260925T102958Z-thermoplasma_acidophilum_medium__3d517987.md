# YAML Record Review: thermoplasma_acidophilum_medium__3d517987

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoplasma_acidophilum_medium__3d517987.yaml`
- Started UTC: 2026-09-25T10:24:00Z
- Finished UTC: 2026-09-25T10:29:58Z
- Verdict: needs curation

## Target

- Reviewed generated KOMODO/DSMZ 158 merge record `CultureMech:004181`.
- Media term: `komodo.medium:158`, `THERMOPLASMA ACIDOPHILUM medium`.
- Source claims in the record point to KOMODO ModelSEED ID 158 and DSMZ Medium 158 via `mediadive.medium:158`.

## Validation

- Schema validation: passed with `linkml-validate`; no issues found.
- Strict validation: passed; `/private/tmp/thermoplasma_acidophilum_medium__3d517987.strict.tsv` was header-only with 1 line and 0 error rows.
- Reference validation: passed; 0 checks were configured for this record.
- Term validation: passed; only the known `eutils`/`pkg_resources` deprecation warning was emitted.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged YAML.

## Identity and Grounding

- DSMZ Medium 158, MediaDive medium 158, KOMODO 158, and TOGO M2384 all refer to Thermoplasma Acidophilum Medium.
- DSMZ Medium 158 adds 10 ml/L Trace element solution to the main medium and defines the trace stock separately.
- An exact ignored-inclusive search found the same `mediadive.medium:158` source in the direct DSMZ merge `data/merge_yaml/merged/thermoplasma_acidophilum_medium__d7d3722d.yaml` and the TOGO M2384 merge `data/merge_yaml/merged/thermoplasma_acidophilum_medium__5b74e2ee.yaml`.

## Evidence

- `/private/tmp/DSMZ_Medium158.txt` extracted from the DSMZ Medium 158 PDF lists the main mineral salts, 10 ml Trace element solution, 2 g yeast extract, 20 g glucose, and 1000 ml freshly distilled water.
- `/private/tmp/mediadive_158.json` mirrors DSMZ 158 and keeps the trace stock as solution 274.
- `/private/tmp/togo_M2384.json` shows how TOGO M2384 imports the same source and exposes the top-level 10 ml Trace element solution separately from the trace-stock paragraph.
- Local duplicate detection was rerun with `rg --no-ignore --hidden` and an explicit boundary on `mediadive.medium:158`, so ignored generated indexes were included without pulling in MediaDive IDs 1580 through 1589.

## Completeness

- The KOMODO-derived target has the core main salts, yeast extract, glucose, and the trace-stock salts.
- The source 1000 ml freshly distilled water row is absent.
- The 10 ml/L Trace element solution addition is absent; its stock ingredients are flattened as top-level ingredients at full stock concentration.
- The target has `ph_range` 1.0 to 2.0 plus `ph_value` 1.0 even though DSMZ Medium 158 specifies pH 1.0.

## Findings

- The entire Trace element solution was flattened into the basal medium: stock FeCl3 x 6 H2O 1.93 g/L, MnCl2 x 4 H2O 0.18 g/L, and Na2B4O7 x 10 H2O 0.45 g/L are treated as main-medium rows instead of as a stock added at 10 ml/L.
- Stock milligram rows were converted to stock g/L values and still flattened into the basal medium; for example ZnSO4 x 7 H2O is 0.022 g/L in the stock, not 0.022 g/L in the main medium.
- The direct DSMZ 158, TOGO M2384, and KOMODO 158 records are split into three generated outputs for the same original DSMZ source.
- The KOMODO-derived generated record omits the source preparation instruction for adjusting to pH 1.0 and separately sterilizing yeast extract and glucose.

## Recommended Edits

- Repair the normalized KOMODO 158 and TOGO M2384 inputs, or their import path, so Trace element solution remains a nested stock with a 10 ml/L addition in the main DSMZ 158 recipe.
- Preserve 1000 ml freshly distilled water from the source.
- Use one canonical DSMZ 158 representation for the direct DSMZ, KOMODO, and TOGO imports after their formulations agree.
- Use the source pH 1.0 for DSMZ 158 unless a non-DSMZ source explicitly supports the broader pH range.

## Follow-up Checks

- Rebuild the merged YAML and confirm the trace-stock ingredients are nested rather than top-level.
- Re-run schema, strict, reference, and term validation on the regenerated DSMZ 158 merge target.
- Re-run an exact ignored-inclusive search for `mediadive.medium:158`, `KOMODO_158_THERMOPLASMA_ACIDOPHILUM_medium`, and `TOGO_M2384_Thermoplasma_Acidophilum_Medium` to confirm DSMZ 158 is represented once.

## Additional Notes

- An initial local duplicate search used an unbounded `mediadive.medium:158` pattern and also matched MediaDive IDs 1580 through 1589; I discarded that output and reran the search with an explicit non-alphanumeric boundary.
