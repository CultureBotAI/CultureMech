# YAML Record Review: methanosarcina_jl01_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanosarcina_jl01_medium__56e005e2.yaml
- Started UTC: 2026-09-24T04:50:22Z
- Finished UTC: 2026-09-24T04:52:23Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002347 |
| Name | methanosarcina_jl01_medium |
| Original name | METHANOSARCINA JL01 MEDIUM |
| Category | archaea |
| Generated record | data/merge_yaml/merged/methanosarcina_jl01_medium__56e005e2.yaml |
| Maintained owner | data/normalized_yaml/archaea/methanosarcina_jl01_medium.yaml |
| Source accession | mediadive.medium:J1176 |
| Source page | JCM 1176 |
| Merge fingerprint | 56e005e2906d89a899cddd18125829b35fb034cb0d6a2cc2ed4bdab0d2b11979 |

This is a generated one-source merge of the direct MediaDive/JCM normalized owner. Future corrections belong in `data/normalized_yaml/archaea/methanosarcina_jl01_medium.yaml`, the MediaDive importer that flattens stock solutions, or merge deduplication with the TOGO M1260 duplicate; `data/merge_yaml/merged/methanosarcina_jl01_medium__56e005e2.yaml` is generated output.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanosarcina_jl01_medium__56e005e2.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanosarcina_jl01_medium__56e005e2.yaml --out /private/tmp/methanosarcina_jl01_medium_56e005e2.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with ERROR, 0 total ERROR rows; the TSV has only its header row. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanosarcina_jl01_medium__56e005e2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks, all validations passed. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanosarcina_jl01_medium__56e005e2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The run emitted only the known `eutils` `pkg_resources` deprecation warning before `Validation passed`. |
| Embedded history | Not run: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in a merged record. |

`just` validators were not used because this checkout resolves `llvmlite==0.46.0` under Python 3.13 and fails during package build before reaching CultureMech validation. The focused Python 3.11 `uv --no-project --offline` commands above exercise the record-level schema, strict, reference, and term gates.

## Identity and Grounding

- The main identity is correct: the record denotes JCM 1176, `METHANOSARCINA JL01 MEDIUM`, and the live JCM page, MediaDive REST record, and TOGO M1260 duplicate all agree on that medium identity.
- The `COMPLEX` and `UNDEFINED` classifications are appropriate because the source includes yeast extract.
- One chemical grounding is wrong for the cited live JCM source. JCM 1176 and TOGO M1260 list 0.2 g MgCl2 x 6 H2O, but the MediaDive-derived record carries MgCl2 x 2 H2O and grounds it to CHEBI:131394, magnesium dichloride dihydrate.
- The same JCM 1176 source also exists in `data/normalized_yaml/archaea/TOGO_M1260_Methanosarcina_JL01_Medium.yaml` as `CultureMech:007792` and in `data/merge_yaml/merged/METHANOSARCINA_JL01_MEDIUM.yaml`, so TOGO and direct MediaDive imports have not been reconciled to one generated record.

## Evidence

- JCM 1176 supports the base ingredient table: KH2PO4 0.15 g, K2HPO4 0.29 g, NH4Cl 1.0 g, MgCl2 x 6 H2O 0.2 g, CaCl2 x 2 H2O 0.1 g, NaCl 0.9 g, 1 ml FeCl2 solution from JCM 187, 1 ml trace-element solution from JCM 187, 2 g yeast extract, 0.5 mg resazurin, 2 g NaHCO3, and 1 L distilled water.
- JCM 1176 supports four post-autoclave additions per liter: 10 ml trace vitamins from JCM 197, 10 ml 50% v/v methanol, 10 ml 5% L-cysteine HCl H2O, and 10 ml 5% Na2S x 9 H2O.
- JCM 1176 supports the retained preparation text for boiling without NaHCO3, cooling under N2-CO2 80:20, adding NaHCO3, dispensing 20 ml into 120 ml serum bottles under the same gas, autoclaving, standing until re-dissolved, adding the listed stocks, and adjusting pH to 6.8-7.0 if needed.
- JCM 187 and MediaDive solution 3846 support the FeCl2 stock as 10 ml 25% HCl plus 1.5 g FeCl2 x 4 H2O brought to 1 L. JCM 1176 calls for 1 ml of this stock, but the generated final medium has the stock's 2.5 g/L HCl and 1.5 g/L FeCl2 x 4 H2O as top-level rows.
- JCM 187 and MediaDive solution 3847 support the trace-element stock as a one-liter stock with 70 mg ZnCl2, 100 mg MnCl2 x 4 H2O, 6 mg H3BO3, 190 mg CoCl2 x 6 H2O, 2 mg CuCl2 x 2 H2O, 24 mg NiCl2 x 6 H2O, and 36 mg Na2MoO4 x 2 H2O. JCM 1176 calls for 1 ml of this stock, but the generated final medium copied those stock concentrations as final `G_PER_L` values.

## Completeness

- Distilled water is absent even though both JCM 1176 and MediaDive J1176 include a 1 L / 1000 ml water row.
- FeCl2 solution, trace-element solution, trace vitamins, 50% methanol, 5% cysteine, and 5% sulfide are not represented as solution additions; their internals or pure compounds were flattened into the final ingredient list.
- The flattened trace vitamins are 100-fold too high as final-medium concentrations because 10 ml of a 1 L vitamin stock was copied at stock strength.
- The flattened FeCl2 and trace-element stocks are 1000-fold too high as final-medium concentrations because 1 ml of each 1 L stock was copied at stock strength.
- Empty optional organism, variant, application-detail, discussion, and source_data fields are not defects by themselves; the actionable omissions are water and the stock boundaries above.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | MgCl2 is hydrated and grounded incorrectly for the live JCM source. | JCM 1176 and TOGO M1260 state MgCl2 x 6 H2O; the MediaDive-derived owner stores MgCl2 x 2 H2O and grounds it to CHEBI:131394. | `data/normalized_yaml/archaea/methanosarcina_jl01_medium.yaml` or the MediaDive compound mapping |
| major | FeCl2 and trace-element stocks were copied at stock strength into the final medium. | JCM 1176 calls for 1 ml each of the JCM 187 FeCl2 and trace-element stocks; the record carries the one-liter stock concentrations for HCl, FeCl2 x 4 H2O, and seven trace metals as top-level `G_PER_L` rows. | MediaDive importer and `data/normalized_yaml/archaea/methanosarcina_jl01_medium.yaml` |
| major | Post-autoclave stock additions were converted into unsupported pure-compound concentrations. | The source calls for 10 ml 50% methanol, 10 ml 5% L-cysteine HCl H2O, and 10 ml 5% Na2S x 9 H2O; the record stores Methanol, L-Cysteine HCl x H2O, and Na2S x 9 H2O each as `10 G_PER_L`. | MediaDive importer and `data/normalized_yaml/archaea/methanosarcina_jl01_medium.yaml` |
| major | Trace vitamins were flattened without the 10 ml per liter dilution. | JCM 1176 calls for 10 ml of the JCM 197 trace-vitamin stock; the record stores the vitamin stock's 0.002, 0.01, 0.005, and 0.0001 g/L values as final-medium values. | MediaDive importer and `data/normalized_yaml/archaea/methanosarcina_jl01_medium.yaml` |
| major | Source water was dropped. | JCM 1176 and the MediaDive REST payload both include 1 L / 1000 ml distilled water; the generated ingredient list has no water row or final-volume representation. | `data/normalized_yaml/archaea/methanosarcina_jl01_medium.yaml` |
| major | The TOGO import of the same JCM medium is a separate generated record. | An exact gitignore-independent search for `CultureMech:007792`, `TOGO Medium M1260`, and `TOGO:M1260` covered `data/merge_yaml/merged` plus the TOGO owner and found `data/merge_yaml/merged/METHANOSARCINA_JL01_MEDIUM.yaml`. | Merge deduplication and ID reconciliation |

## Recommended Edits

1. Correct the maintained MediaDive/JCM owner to MgCl2 x 6 H2O, or fix the upstream MediaDive compound mapping if it is responsible for the hydrate substitution.
2. Re-model FeCl2 solution, trace-element solution, trace vitamins, 50% methanol, 5% L-cysteine HCl H2O, and 5% Na2S x 9 H2O as stock additions with source volumes; do not flatten one-liter stock concentrations into the final medium without dilution.
3. Restore the 1 L distilled-water row or an equivalent final-volume representation from JCM 1176.
4. Keep the existing JCM 1176 preparation text attached to the stock-addition boundary and verify that pH 6.8-7.0 remains represented.
5. Reconcile `CultureMech:002347` with the TOGO M1260 duplicate `CultureMech:007792` so the same JCM 1176 source does not emit two generated records.
6. Regenerate the merged YAML after fixing the maintained owner and importer behavior.

## Follow-up Checks

- Re-run the focused open schema, strict, reference, and term validators on the corrected normalized owner and the regenerated merged record.
- Inspect the regenerated final-medium rows and verify that FeCl2/trace-element stock components are not present at one-liter stock strength.
- Inspect the regenerated solution records or nested solution references and confirm the 1 ml FeCl2, 1 ml trace-element, 10 ml trace-vitamin, 10 ml 50% methanol, 10 ml cysteine, and 10 ml sulfide additions are recoverable.
- Inspect generated JL01 records after deduplication and confirm the direct JCM/MediaDive and TOGO M1260 imports no longer publish as separate stable IDs for one JCM source.

## Additional Notes

- The live JCM 1176 page, MediaDive J1176 REST payload, live JCM 187 page, live JCM 197 page, TOGO M1260 API record, and TOGO M1260 normalized owner were inspected.
- The exact duplicate search for `CultureMech:007792`, `TOGO Medium M1260`, and `TOGO:M1260` used `rg --no-ignore --hidden` and included ignored files in the searched paths.
- This review did not create or edit GitHub issues, pull requests, or comments.
