# YAML Record Review: thermoproteus_medium__0078092d

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoproteus_medium__0078092d.yaml`
- Started UTC: 2026-09-25T10:34:00Z
- Finished UTC: 2026-09-25T10:39:02Z
- Verdict: needs curation

## Target

- Reviewed generated TOGO M2677 record `CultureMech:009232`.
- Media term: `TOGO:M2677`, `Thermoproteus medium`.
- Source claims in the record point to ATCC Medium 1538.

## Validation

- Schema validation: passed with `linkml-validate`; no issues found.
- Strict validation: passed; `/private/tmp/thermoproteus_medium__0078092d.strict.tsv` was header-only with 1 line and 0 error rows.
- Reference validation: passed; 0 checks were configured for this record.
- Term validation: passed; only the known `eutils`/`pkg_resources` deprecation warning was emitted.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged YAML.

## Identity and Grounding

- The ATCC PDF identifies this source as ATCC Medium 1538, Thermoproteus medium.
- TOGO M2677 preserves the ATCC three-part Solution A/B/C structure plus a Trace Elements stock and pH 4.8 to 5.6.
- An exact ignored-inclusive search found TOGO M2677 as its own generated target, separate from the DSMZ 185 Thermoproteus records.

## Evidence

- `/private/tmp/ATCC_C45C5A59BB764197A28F2DF969186C86.txt` lists 500 ml Solution A, 450 ml Solution B, 50 ml Solution C, a 10 ml Trace Elements addition, and pH adjustment to 4.8 to 5.6.
- `/private/tmp/togo_M2677.json` preserves Solution A, Solution B, Solution C, and Trace Elements as separate subcomponents.
- Local duplicate detection was rerun with `rg --no-ignore --hidden` against exact current source IDs and filenames, so ignored generated indexes were included.

## Completeness

- The generated record includes recognizable ATCC main-solution and stock ingredients.
- It flattens Solution A, B, C, and Trace Elements into one top-level ingredient list.
- It leaves each source solution as an empty `Unknown solution` placeholder with g/L units instead of ml addition volumes.
- The pH 4.8 to 5.6 range is absent.

## Findings

- Solution volumes were normalized as g/L placeholders: Solution A 500, Solution B 450, Solution C 50, and Trace Elements 10 all have unit `G_PER_L`.
- Source water was summed across Solution A, B, C, and Trace Elements, producing one 991 g/L water row and losing the ATCC compartments.
- Solution C's 850 mg Na2S x 9 H2O was imported as 850 g/L.
- Trace Elements stock milligram rows were imported as gram values and flattened into the basal ingredient list.
- The two H2SO4 solution placeholders are empty and duplicate a pH-adjustment condition.

## Recommended Edits

- Repair `data/normalized_yaml/archaea/TOGO_M2677_Thermoproteus_medium.yaml` so Solution A, Solution B, Solution C, and Trace Elements remain separate nested solutions with their source volumes.
- Convert source milligram rows to g/L only during unit normalization.
- Keep H2SO4 and the 97% N2 / 3% H2 headspace as preparation conditions rather than empty variable solutions or top-level ingredients.
- Preserve pH range 4.8 to 5.6 from ATCC.

## Follow-up Checks

- Rebuild the merged YAML and confirm the ATCC compartments survive as nested solutions.
- Re-run schema, strict, reference, and term validation on the regenerated TOGO M2677 target.
- Confirm that no 850 g/L sodium sulfide or full-strength Trace Elements rows remain in the top-level ingredient list.

## Additional Notes

None found.
