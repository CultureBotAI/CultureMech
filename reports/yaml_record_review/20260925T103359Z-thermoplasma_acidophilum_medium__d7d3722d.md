# YAML Record Review: thermoplasma_acidophilum_medium__d7d3722d

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoplasma_acidophilum_medium__d7d3722d.yaml`
- Started UTC: 2026-09-25T10:30:00Z
- Finished UTC: 2026-09-25T10:33:59Z
- Verdict: needs curation

## Target

- Reviewed generated direct DSMZ 158 record `CultureMech:001066`.
- Media term: `mediadive.medium:158`, `THERMOPLASMA ACIDOPHILUM MEDIUM`.
- Source claims in the record point to DSMZ Medium 158 through MediaDive.

## Validation

- Schema validation: passed with `linkml-validate`; no issues found.
- Strict validation: passed; `/private/tmp/thermoplasma_acidophilum_medium__d7d3722d.strict.tsv` was header-only with 1 line and 0 error rows.
- Reference validation: passed; exited 0 with no diagnostics.
- Term validation: passed; only the known `eutils`/`pkg_resources` deprecation warning was emitted.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged YAML.

## Identity and Grounding

- DSMZ Medium 158 and MediaDive medium 158 identify Thermoplasma Acidophilum Medium at pH 1.0.
- The source main recipe adds Trace element solution at 10 ml/L and stores the trace salts in a distinct stock.
- An exact ignored-inclusive search found the same DSMZ 158 source split across the direct MediaDive import, KOMODO 158, and TOGO M2384.

## Evidence

- `/private/tmp/DSMZ_Medium158.txt` lists the main salts, 10 ml Trace element solution, yeast extract, glucose, and 1000 ml freshly distilled water before the trace-stock formula.
- `/private/tmp/mediadive_158.json` preserves that structure as main solution 158 plus solution 274.
- `/private/tmp/togo_M2384.json` corroborates that TOGO M2384 is another import of the same DSMZ Medium 158 PDF.
- Local duplicate detection was run with `rg --no-ignore --hidden` and an explicit `mediadive.medium:158` boundary, so ignored generated indexes were included while MediaDive IDs 1580 through 1589 were excluded.

## Completeness

- The direct DSMZ generated record carries pH 1.0 and the DSMZ pH and sterilization preparation text.
- The generated record omits the source 1000 ml freshly distilled water row.
- It flattens Trace element solution stock salts into top-level ingredients and loses the explicit 10 ml/L stock addition.

## Findings

- The source Trace element solution is not modeled as a nested solution in the generated record.
- Trace-stock concentrations such as FeCl3 x 6 H2O 1.93 g/L and MnCl2 x 4 H2O 0.18 g/L are present as if they were basal medium concentrations.
- The main recipe is missing the source 1000 ml freshly distilled water.
- DSMZ 158 is split across direct, KOMODO, and TOGO generated records for the same original source.

## Recommended Edits

- Repair `data/normalized_yaml/archaea/thermoplasma_acidophilum_medium.yaml` or the MediaDive import logic so solution 274 stays nested under a 10 ml/L Trace element solution addition.
- Preserve the main 1000 ml freshly distilled water row.
- Merge the repaired direct DSMZ 158 source with repaired KOMODO 158 and TOGO M2384 sources into one canonical DSMZ 158 generated record.

## Follow-up Checks

- Rebuild the merged YAML and confirm the Trace element solution is nested.
- Re-run schema, strict, reference, and term validation on the regenerated DSMZ 158 target.
- Re-run an exact ignored-inclusive search for `mediadive.medium:158`, `KOMODO_158_THERMOPLASMA_ACIDOPHILUM_medium`, and `TOGO_M2384_Thermoplasma_Acidophilum_Medium` to confirm the DSMZ 158 source has one generated output.

## Additional Notes

None found.
