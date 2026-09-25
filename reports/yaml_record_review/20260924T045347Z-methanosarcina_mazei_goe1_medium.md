# YAML Record Review: methanosarcina_mazei_goe1_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanosarcina_mazei_goe1_medium.yaml
- Started UTC: 2026-09-24T04:52:24Z
- Finished UTC: 2026-09-24T04:53:47Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:000663 |
| Name | methanosarcina_mazei_goe1_medium |
| Original name | METHANOSARCINA MAZEI (GOE1) MEDIUM |
| Category | archaea |
| Generated record | data/merge_yaml/merged/methanosarcina_mazei_goe1_medium.yaml |
| Maintained owner | data/normalized_yaml/archaea/methanosarcina_mazei_goe1_medium.yaml |
| Source accession | mediadive.medium:120c |
| Source page | DSMZ Medium 120c |
| Merge fingerprint | f4dadfe3fb0d3a5c4985d9b295ca92f02e11916e1892a64879bbd672731b9a66 |

This is a generated one-source merge of the direct MediaDive/DSMZ normalized owner. Corrections belong in `data/normalized_yaml/archaea/methanosarcina_mazei_goe1_medium.yaml` or in the MediaDive importer that flattens stock recipes; the derived YAML under `data/merge_yaml/merged/` should be regenerated afterward.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanosarcina_mazei_goe1_medium.yaml` | Passed; exited 0 with no diagnostics. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanosarcina_mazei_goe1_medium.yaml --out /private/tmp/methanosarcina_mazei_goe1_medium.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with ERROR, 0 total ERROR rows; the TSV has only its header row. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanosarcina_mazei_goe1_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks, all validations passed. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanosarcina_mazei_goe1_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The run emitted only the known `eutils` `pkg_resources` deprecation warning before `Validation passed`. |
| Embedded history | Not run: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in a merged record. |

`just` validators were not used because this checkout resolves `llvmlite==0.46.0` under Python 3.13 and fails during package build before reaching CultureMech validation. The focused Python 3.11 `uv --no-project --offline` commands above exercise the record-level schema, strict, reference, and term gates.

## Identity and Grounding

- The record denotes the right DSMZ source: `mediadive.medium:120c`, `DSMZ Medium 120c`, and the DSMZ PDF all identify `METHANOSARCINA MAZEI (GOE1) MEDIUM`.
- The `COMPLEX` and `UNDEFINED` classifications are appropriate because DSMZ 120c includes yeast extract and Casitone.
- The pH range 6.8-7.0 matches the DSMZ PDF and MediaDive REST metadata.
- Base salts, yeast extract, Casitone, sodium acetate, sucrose, bicarbonate, cysteine, and sulfide are grounded to plausible primary compounds, but several rows are stock-solution internals rather than final-medium ingredients.

## Evidence

- DSMZ 120c supports the main table values for 0.35 g K2HPO4, 0.23 g KH2PO4, 0.50 g NH4Cl, 0.50 g MgSO4 x 7 H2O, 0.25 g CaCl2 x 2 H2O, 2.25 g NaCl, 2 g yeast extract, 2 g Casitone, 10 g Na-acetate, 17.10 g sucrose, 0.5 ml sodium resazurin 0.1%, 2 g NaHCO3, 0.30 g L-cysteine HCl H2O, 0.30 g Na2S x 9 H2O, and 1000 ml distilled water.
- DSMZ 120c calls for 2 ml FeSO4 x 7 H2O solution, 1 ml trace element solution SL-10, and 1 ml Wolin's vitamin solution (10x). The generated record drops those solution addition rows.
- MediaDive exposes the FeSO4 stock as 1 g FeSO4 x 7 H2O in 1000 ml 0.1 N H2SO4. The generated final recipe stores `FeSO4 x 7 H2O` at `1 G_PER_L` and `H2SO4` at `1000 G_PER_L`, which are stock internals rather than the 2 ml stock addition in DSMZ 120c.
- MediaDive exposes SL-10 as a 1 L stock containing 10 ml 25% HCl, 1.5 g FeCl2 x 4 H2O, 70 mg ZnCl2, 100 mg MnCl2 x 4 H2O, 6 mg H3BO3, 190 mg CoCl2 x 6 H2O, 2 mg CuCl2 x 2 H2O, 24 mg NiCl2 x 6 H2O, and 36 mg Na2MoO4 x 2 H2O. DSMZ 120c calls for 1 ml of SL-10, but the generated record copies the stock g/L values directly into the final medium.
- MediaDive exposes Wolin's vitamin solution (10x) as a one-liter stock with milligram vitamin quantities. DSMZ 120c calls for 1 ml of that stock, but the generated record has each vitamin at its one-liter stock strength.
- The DSMZ PDF supports the imported anaerobic preparation: sparge with 80% N2 and 20% CO2 for 30-45 min, add bicarbonate, adjust pH to 6.8, autoclave in anoxic vessels, autoclave cysteine and sulfide separately under 100% N2, filter-sterilize vitamins under 100% N2, inject the stocks into sterile medium, and readjust complete-medium pH to 6.8-7.0 if necessary.

## Completeness

- The 1000 ml distilled water row from DSMZ 120c and MediaDive is absent, so the record has no explicit solvent or final-volume context.
- The FeSO4, SL-10, and Wolin vitamin stock boundaries are absent, and the generated record gives their components as final-medium `G_PER_L` rows.
- Sodium resazurin is represented as a final resazurin-equivalent row rather than a 0.5 ml addition of 0.1% sodium resazurin stock.
- Empty optional organism, variant, application-detail, discussion, and source_data fields are not defects by themselves; the consequential gaps are the water and stock-solution representation.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The FeSO4 stock was flattened at stock strength. | DSMZ 120c calls for 2 ml FeSO4 x 7 H2O solution; the record stores 1 g/L FeSO4 x 7 H2O and 1000 g/L H2SO4 as final ingredients. | MediaDive importer and `data/normalized_yaml/archaea/methanosarcina_mazei_goe1_medium.yaml` |
| major | Trace element solution SL-10 was flattened at stock strength. | DSMZ 120c calls for 1 ml SL-10; the record carries HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O at SL-10 stock concentrations. | MediaDive importer and `data/normalized_yaml/archaea/methanosarcina_mazei_goe1_medium.yaml` |
| major | Wolin's vitamin solution (10x) was flattened at stock strength. | DSMZ 120c calls for 1 ml of Wolin's vitamin solution; the generated Biotin, Folic acid, Pyridoxine hydrochloride, Thiamine HCl, Riboflavin, Nicotinic acid, Calcium pantothenate, Vitamin B12, p-Aminobenzoic acid, and lipoic acid rows are the stock concentrations. | MediaDive importer and `data/normalized_yaml/archaea/methanosarcina_mazei_goe1_medium.yaml` |
| major | Source water was dropped. | DSMZ 120c and the MediaDive REST payload both include 1000 ml distilled water; the generated record has no water row. | `data/normalized_yaml/archaea/methanosarcina_mazei_goe1_medium.yaml` |
| minor | Sodium resazurin lost its stock-addition form and exact salt label. | DSMZ 120c lists 0.5 ml of 0.1% sodium resazurin; the generated row is grounded to CHEBI:8806, Resazurin, as a final `G_PER_L` row. | MediaDive importer and ingredient grounding |

## Recommended Edits

1. Re-model the 2 ml FeSO4 x 7 H2O solution, 1 ml SL-10, and 1 ml Wolin vitamin solution as stock additions or nested solutions instead of flattening their one-liter stock concentrations into the final medium.
2. Restore the 1000 ml distilled-water row or an equivalent final-volume representation.
3. Keep H2SO4 scoped as the solvent of the FeSO4 stock and HCl scoped as part of SL-10; neither acid is a final 1000 g/L or 2.5 g/L main-medium ingredient.
4. Preserve the sodium resazurin 0.1% stock addition explicitly, or attach a note to any concentration conversion that documents the stock strength, volume, and conversion.
5. Regenerate `data/merge_yaml/merged/methanosarcina_mazei_goe1_medium.yaml` and inspect the diff for preserved stock boundaries.

## Follow-up Checks

- Re-run the focused open schema, strict, reference, and term validators on the repaired normalized owner and regenerated merged record.
- Inspect the regenerated YAML to confirm FeSO4 solution, SL-10, and Wolin vitamin solution are represented as 2 ml, 1 ml, and 1 ml additions.
- Inspect the main ingredient list to confirm no SL-10 or Wolin stock component remains as a final-medium row at stock strength.
- Verify the DSMZ PDF preparation remains associated with the repaired stock-solution boundary and still captures the N2-CO2, 100% N2, filter-sterilization, and pH instructions.

## Additional Notes

- The DSMZ Medium 120c PDF, extracted PDF text, MediaDive 120c REST payload, and maintained normalized owner were inspected directly.
- This review did not create or edit GitHub issues, pull requests, or comments.
