# YAML Record Review: thermoproteus_neutrophilus_medium__35522aa7

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoproteus_neutrophilus_medium__35522aa7.yaml`
- Started UTC: 2026-09-25T10:39:00Z
- Finished UTC: 2026-09-25T10:42:22Z
- Verdict: needs curation

## Target

- Reviewed generated TOGO M188 record `CultureMech:008464`.
- Media term: `TOGO:M188`, `Thermoproteus Neutrophilus Medium`.
- Source claims in the record point to JCM Medium 195.

## Validation

- Schema validation: passed; exited 0 with no diagnostics.
- Strict validation: passed; `/private/tmp/thermoproteus_neutrophilus_medium__35522aa7.strict.tsv` was header-only with 1 line and 0 error rows.
- Reference validation: passed; 0 checks were configured for this record.
- Term validation: passed; only the known `eutils`/`pkg_resources` deprecation warning was emitted.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged YAML.

## Identity and Grounding

- JCM Medium 195 and MediaDive medium J195 identify Thermoproteus Neutrophilus Medium at pH 6.5.
- TOGO M188 cites `JCM_M195` and carries the same Modified Brock salt base addition plus NaHCO3, yeast extract, sodium dithionite, sulfur powder, and resazurin.
- An exact ignored-inclusive search found a direct JCM 195 generated record at `thermoproteus_neutrophilus_medium__dcefca4b.yaml` in addition to this TOGO M188 target.

## Evidence

- `/private/tmp/jcm_195.html` lists 1 L Modified Brock salt base solution, NaHCO3 0.85 g/L, yeast extract 0.2 g/L, sodium dithionite 25 mg/L, sulfur powder 8 g/L, and resazurin 0.4 mg/L.
- `/private/tmp/mediadive_J195.json` preserves the Modified Brock salt base as a separate referenced solution.
- `/private/tmp/togo_M188.json` shows the same JCM-derived rows and the H2-CO2 / N2 gas handling comments.
- Local duplicate detection was rerun with `rg --no-ignore --hidden` against exact JCM 195 and TOGO M188 identifiers, so ignored generated indexes were included.

## Completeness

- The generated record keeps the Modified Brock salt base as a cross-reference to M156.
- It leaves that base as an empty `Unknown solution` at `1 G_PER_L` instead of 1 L.
- It inflates source milligram rows into g/L rows.
- It drops pH 6.5 and the source preparation instructions.

## Findings

- Modified Brock salt base solution is recorded with unit `G_PER_L` instead of `L`.
- Resazurin 0.4 mg/L became 0.4 g/L.
- Sodium dithionite 25 mg/L became 25 g/L.
- JCM 195 is split across TOGO M188 and the direct JCM generated record.

## Recommended Edits

- Repair `data/normalized_yaml/archaea/TOGO_M188_Thermoproteus_Neutrophilus_Medium.yaml` so Modified Brock salt base solution remains a 1 L referenced solution.
- Convert milligram rows to g/L values during unit normalization.
- Preserve pH 6.5 and the JCM preparation instructions.
- De-duplicate TOGO M188 with the direct JCM 195 import once both are source-equivalent.

## Follow-up Checks

- Rebuild the merged YAML and confirm resazurin and sodium dithionite are no longer 0.4 g/L and 25 g/L.
- Re-run schema, strict, reference, and term validation on the regenerated JCM 195 target.
- Re-run exact ignored-inclusive searches for `TOGO_M188_Thermoproteus_Neutrophilus_Medium` and `mediadive.medium:J195`.

## Additional Notes

None found.
