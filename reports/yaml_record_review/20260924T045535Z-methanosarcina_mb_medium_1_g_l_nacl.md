# YAML Record Review: methanosarcina_mb_medium_1_g_l_nacl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanosarcina_mb_medium_1_g_l_nacl.yaml
- Started UTC: 2026-09-24T04:53:48Z
- Finished UTC: 2026-09-24T04:55:35Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002096 |
| Name | methanosarcina_mb_medium_1_g_l_nacl |
| Original name | METHANOSARCINA MB MEDIUM (1 g/l NaCl) |
| Category | archaea |
| Generated record | data/merge_yaml/merged/methanosarcina_mb_medium_1_g_l_nacl.yaml |
| Maintained owner | data/normalized_yaml/archaea/methanosarcina_mb_medium_1_g_l_nacl.yaml |
| Source accession | mediadive.medium:924b |
| Source page | DSMZ Medium 924b |
| Merge fingerprint | 4308afa09ec7cd3748a1e646dc327ff28fceb39da9b757488ec7d6d3caf06b49 |

This generated record merged seven source recipes into the DSMZ 924b low-NaCl title record. Future fixes belong partly in `data/normalized_yaml/archaea/methanosarcina_mb_medium_1_g_l_nacl.yaml`, which already flattens DSMZ 924b stock recipes, and partly in the merge/deduplication layer that conflates DSMZ 924b with DSMZ 924 and KOMODO 924 variants.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanosarcina_mb_medium_1_g_l_nacl.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanosarcina_mb_medium_1_g_l_nacl.yaml --out /private/tmp/methanosarcina_mb_medium_1_g_l_nacl.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with ERROR, 0 total ERROR rows; the TSV has only its header row. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanosarcina_mb_medium_1_g_l_nacl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks, all validations passed. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanosarcina_mb_medium_1_g_l_nacl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The run emitted only the known `eutils` `pkg_resources` deprecation warning before `Validation passed`. |
| Embedded history | Not run: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in a merged record. |

`just` validators were not used because this checkout resolves `llvmlite==0.46.0` under Python 3.13 and fails during package build before reaching CultureMech validation. The focused Python 3.11 `uv --no-project --offline` commands above exercise the record-level schema, strict, reference, and term gates.

## Identity and Grounding

- The title, ID, `media_term`, and note initially identify the DSMZ 924b low-salt variant, `METHANOSARCINA MB MEDIUM (1 g/l NaCl)`.
- The generated composition no longer matches the low-salt identity. It merged `methanocalculus_mb_medium` from DSMZ 924 plus five KOMODO 924 variants into the DSMZ 924b canonical record and now reports 10.8912 g/L NaCl.
- The `categories` array combines `archaea` and `bacterial` because the 924b archaeal record merged with KOMODO bacterial-normalized variants. That cross-category output is a merge artifact, not a source claim in DSMZ 924b.
- `COMPLEX` and `UNDEFINED` are appropriate because the DSMZ 924b source includes yeast extract and Trypticase peptone.

## Evidence

- DSMZ 924b and MediaDive 924b support the low-salt main recipe: 1 g NaCl, 1 g MgCl2 x 6 H2O, 0.5 g KCl, 0.4 g CaCl2 x 2 H2O, 0.4 g K2HPO4, 1 g NH4Cl, 10 ml Modified Wolin's mineral solution, 2 g yeast extract, 2 g Trypticase peptone, 0.5 ml sodium resazurin 0.1%, 4 g NaHCO3, 6.8 g Na-formate, 1.6 g Na-acetate, 1 ml Wolin's vitamin solution, 0.25 g L-cysteine HCl H2O, 0.25 g Na2S x 9 H2O, and 1000 ml distilled water.
- DSMZ 924 uses 10 g NaCl in its main recipe. The generated 10.8912 g/L NaCl combines the DSMZ 924 9.8912 g/L main NaCl value with the 1 g/L Modified Wolin stock's NaCl row after stock flattening.
- DSMZ 924b calls for 10 ml Modified Wolin's mineral solution from a 1 L stock. The maintained 924b owner and generated record copy the stock's 1.5 g/L nitrilotriacetic acid, 3 g/L MgSO4 x 7 H2O, 0.5 g/L MnSO4 x H2O, 1 g/L NaCl, 0.1 g/L FeSO4 x 7 H2O, 0.18 g/L CoSO4 x 7 H2O, 0.1 g/L CaCl2 x 2 H2O, 0.18 g/L ZnSO4 x 7 H2O, 0.01 g/L CuSO4 x 5 H2O, 0.02 g/L AlK(SO4)2 x 12 H2O, 0.01 g/L H3BO3, 0.01 g/L Na2MoO4 x 2 H2O, 0.03 g/L NiCl2 x 6 H2O, 0.0003 g/L Na2SeO3 x 5 H2O, and 0.0004 g/L Na2WO4 x 2 H2O as final-medium rows.
- DSMZ 924b calls for 1 ml Wolin's vitamin solution (10x). The generated Biotin, Folic acid, Pyridoxine hydrochloride, Thiamine HCl, Riboflavin, Nicotinic acid, Calcium pantothenate, Vitamin B12, p-Aminobenzoic acid, and lipoic acid rows are stock concentrations from the 1 L vitamin solution.
- The DSMZ 924b PDF supports the retained preparation text, including N2-CO2 80:20 sparging, pH 6.8-7.0 before dispensing, addition of bicarbonate before autoclaving, and formate/acetate/vitamin/reducing-agent stock additions after autoclaving.

## Completeness

- The generated record is not complete enough for the named 1 g/l NaCl variant because the composition now mixes the low-salt 924b variant with DSMZ 924 / KOMODO 924 higher-salt variants.
- The 1000 ml water row is absent.
- Modified Wolin's mineral solution and Wolin's vitamin solution are absent as stock boundaries, and their one-liter stock formulas are flattened into the main ingredient list.
- The DSMZ 924b source lists explicit branch variants for DSM 27722 and DSM 27785 that omit formate/acetate and add trimethylamine-HCl or methanol; the generated record has no variant representation for those alternatives.
- Empty optional organism, growth, and discussion fields are not defects by themselves; the consequential gaps are the variant conflation, water omission, and stock-boundary loss above.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated record conflates DSMZ 924b with DSMZ 924 and KOMODO 924 variants. | The source title says `1 g/l NaCl`; DSMZ 924b has 1 g NaCl, while the generated record carries 10.8912 g/L NaCl after merging DSMZ 924's 10 g NaCl source and KOMODO variants into the 924b canonical record. | Merge deduplication |
| major | The Modified Wolin stock was flattened at stock strength. | DSMZ 924b calls for 10 ml Modified Wolin's mineral solution; the record carries the one-liter stock concentrations for nitrilotriacetic acid, MgSO4, MnSO4, NaCl, CaCl2, FeSO4, CoSO4, ZnSO4, CuSO4, AlK(SO4)2, H3BO3, Na2MoO4, NiCl2, Na2SeO3, and Na2WO4 as main rows. | MediaDive importer and `data/normalized_yaml/archaea/methanosarcina_mb_medium_1_g_l_nacl.yaml` |
| major | Wolin's vitamin solution was flattened at stock strength. | DSMZ 924b calls for 1 ml Wolin's vitamin solution (10x); each vitamin row in the generated record is the one-liter stock value. | MediaDive importer and `data/normalized_yaml/archaea/methanosarcina_mb_medium_1_g_l_nacl.yaml` |
| major | Source water was dropped. | DSMZ 924b and MediaDive 924b list 1000 ml distilled water; the generated record has no water row. | `data/normalized_yaml/archaea/methanosarcina_mb_medium_1_g_l_nacl.yaml` |
| major | Cross-scope duplicate summing changes main-medium salts. | The maintained 924b owner already sums 0.395648 g/L final CaCl2 with 0.1 g/L CaCl2 from a stock, and the generated record further sums the 924b low-salt NaCl context with DSMZ 924 high-salt NaCl. | Ingredient deduplication and merge logic |

## Recommended Edits

1. Split DSMZ 924b from DSMZ 924 and KOMODO 924 variants unless a curator can prove exact equivalence; the 1 g/l NaCl variant must not inherit DSMZ 924's 10 g NaCl formulation.
2. Restore Modified Wolin's mineral solution as a 10 ml stock addition and keep its preparation note scoped to the stock.
3. Restore Wolin's vitamin solution as a 1 ml stock addition.
4. Restore 1000 ml distilled water or an equivalent final-volume representation.
5. Prevent ingredient deduplication from summing compounds across main medium, mineral stocks, and higher-salt variant recipes.
6. Regenerate the merge YAML and inspect the canonical record, synonyms, `categories`, and `merged_from` list for unsupported cross-variant merging.

## Follow-up Checks

- Re-run the focused open schema, strict, reference, and term validators on the repaired DSMZ 924b owner and regenerated generated record.
- Inspect the regenerated 924b output and confirm the main NaCl row reflects DSMZ 924b's 1 g low-salt recipe, not DSMZ 924's 10 g NaCl recipe or stock-summed NaCl.
- Confirm Modified Wolin's mineral solution and Wolin's vitamin solution survive as solution additions rather than final-medium trace rows.
- Inspect generated DSMZ 924 and 924b records side by side to confirm they remain separate variants or are linked by a source-backed parent/variant relationship rather than value-level ingredient merging.

## Additional Notes

- The DSMZ Medium 924b PDF, DSMZ Medium 924 PDF, extracted PDF text for both PDFs, MediaDive 924b REST payload, MediaDive 924 REST payload, and the maintained DSMZ 924b and DSMZ 924 normalized owners were inspected directly.
- This review did not create or edit GitHub issues, pull requests, or comments.
