# YAML Record Review: methanosarcina_acetivorans_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanosarcina_acetivorans_medium__9ce1381f.yaml
- Started UTC: 2026-09-24T04:45:25Z
- Finished UTC: 2026-09-24T04:48:31Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009762 |
| Name | methanosarcina_acetivorans_medium |
| Original name | Methanosarcina Acetivorans Medium |
| Category | archaea |
| Generated record | data/merge_yaml/merged/methanosarcina_acetivorans_medium__9ce1381f.yaml |
| Maintained owner | data/normalized_yaml/archaea/TOGO_M380_Methanosarcina_Acetivorans_Medium.yaml |
| Source accession | TOGO:M380 |
| Original source | JCM_M385 |
| Merge fingerprint | 9ce1381fca4fc00ee0a785723a180b01e2aabd91615dd717295b6fcc7a731a28 |

This is a generated one-source merge of the TOGO M380 import. Any correction belongs in `data/normalized_yaml/archaea/TOGO_M380_Methanosarcina_Acetivorans_Medium.yaml`, the TOGO import mapping for cross-medium stock references, or the recipe merger; the derived YAML under `data/merge_yaml/merged/` should be regenerated after the maintained owner is repaired.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanosarcina_acetivorans_medium__9ce1381f.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanosarcina_acetivorans_medium__9ce1381f.yaml --out /private/tmp/methanosarcina_acetivorans_medium_9ce1381f.strict.rerun.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with ERROR, 0 total ERROR rows; the TSV has only its header row. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanosarcina_acetivorans_medium__9ce1381f.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks, all validations passed. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanosarcina_acetivorans_medium__9ce1381f.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The run emitted only the known `eutils` `pkg_resources` deprecation warning before `Validation passed`. |
| Embedded history | Not run: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in a merged record. |

`just` validators were not used because this checkout resolves `llvmlite==0.46.0` under Python 3.13 and fails during package build before reaching CultureMech validation. The focused Python 3.11 `uv --no-project --offline` commands above exercise the same schema, strict, reference, and term gates without touching the project lockfile.

## Identity and Grounding

- The record identity is internally consistent: `CultureMech:009762` names `methanosarcina_acetivorans_medium`, the label and notes identify TOGO M380, and the TOGO API identifies M380 as `Methanosarcina Acetivorans Medium` imported from `JCM_M385`.
- The media term `TOGO:M380` exactly matches the immediate TOGO source accession, so this is not a wrong-medium merge.
- The `COMPLEX` and `UNDEFINED` classifications are appropriate for a recipe that includes yeast extract.
- The source provenance is underspecified. The only structured source identity is `media_term`; the live JCM 385 page and MediaDive J385 now list a post-autoclave bicarbonate/cysteine/sulfide formulation that differs from the older TOGO M380 snapshot, and the record does not preserve that version conflict in `source_data`, references, or a discussion item.

## Evidence

- TOGO M380 supports the older imported base formula: 1 L distilled water, 9.45 g MgSO4 x 7 H2O, 23.4 g NaCl, 0.14 g CaCl2 x 2 H2O, 1 g NH4Cl, 1 mg resazurin, 0.3 g Na2S x 9 H2O, 0.8 g KCl, 5 g Na2CO3, 0.6 g Na2HPO4, 6.5 ml methanol, 1 g yeast extract, 0.3 g L-cysteine HCl H2O, 10 ml of trace minerals from TOGO M142, HCl, carbon dioxide gas, and nitrogen gas.
- The generated record changes several source units during normalization: 1 L water is recorded as `1 G_PER_L`, 1 mg resazurin is recorded as `1 G_PER_L`, 6.5 ml methanol is recorded as `6.5 G_PER_L`, and the 10 ml trace-mineral addition is recorded as `10 G_PER_L`.
- TOGO M380 carries one preparation paragraph specifying methanol, cysteine, and sulfide exclusions before boiling; 5-10 seconds of boiling; cooling under N2-CO2 80:20; pH adjustment to 7.0 with HCl; anaerobic dispensing and sealing; autoclaving; overnight standing; separate autoclaving of 5% cysteine and 5% sulfide stocks under N2; and anaerobic stock addition before inoculation. None of that survives as `preparation_steps`.
- TOGO M142 resolves the trace-mineral cross-reference to a maintained stock section with nitrilotriacetic acid, MgSO4 x 7 H2O, MnSO4 x H2O, NaCl, FeSO4 x 7 H2O, CoSO4 x 7 H2O, CaCl2 x 2 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2, H3BO3, Na2MoO4 x 2 H2O, distilled water, and KOH-dependent preparation notes. The generated `Trace minerals (see Medium [M142])` solution is an empty `Unknown solution` stub.
- The live JCM 385 and MediaDive J385 records now omit Na2CO3 from the base table and instead add 30 ml of 8% NaHCO3, 6 ml of 5% L-cysteine HCl H2O, and 6 ml of 5% Na2S x 9 H2O after autoclaving. That conflict is source drift, not evidence that the old TOGO snapshot should be blended into the current JCM recipe.

## Completeness

- The record is not complete enough for use as a recipe: following the generated fields alone would weigh liters and milliliters as grams per liter, drop the actual trace-mineral stock composition, and omit the anaerobic gas, pH, autoclaving, and post-autoclave addition instructions.
- No source-backed `pH` field is present even though the TOGO paragraph adjusts the medium to pH 7.0 before dispensing.
- `HCl`, `Carbon dioxide gas`, and `Nitrogen gas` were normalized into variable-concentration ingredients without the procedural context that explains them as a pH-adjustment reagent and anaerobic gas mixture.
- Exact hydrate ingredients such as MgSO4 x 7 H2O, CaCl2 x 2 H2O, Na2S x 9 H2O, and L-cysteine HCl H2O have primary ChEBI grounding but still lack `mediaingredientmech_chebi_term` links in this generated copy.
- Empty optional organism, growth, variant, application-detail, and discussion fields are not defects by themselves; the consequential omissions here are the source recipe, stock, pH, and preparation details above.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The record has source drift with the live JCM 385 formula but does not record the conflict. | TOGO M380 has the older direct 5 g Na2CO3 and 0.3 g cysteine/sulfide entries; live JCM 385 and MediaDive J385 now use 30 ml 8% NaHCO3, 6 ml 5% cysteine, and 6 ml 5% sulfide post-autoclave additions. | `data/normalized_yaml/archaea/TOGO_M380_Methanosarcina_Acetivorans_Medium.yaml` or the TOGO importer |
| major | Multiple source volumes and masses were converted to `G_PER_L` without dimensional support. | TOGO M380 gives water as 1 L, resazurin as 1 mg, methanol as 6.5 ml, and trace minerals as 10 ml; the record stores each as `G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M380_Methanosarcina_Acetivorans_Medium.yaml` |
| major | The 10 ml trace-minerals stock is an empty stub. | The source points to TOGO M142, which exposes the JCM 151 trace-minerals stock formula and its pH-adjustment notes; the generated solution has `composition: []`, `name: Unknown solution`, and `10 G_PER_L`. | TOGO cross-medium solution import plus `data/normalized_yaml/archaea/TOGO_M380_Methanosarcina_Acetivorans_Medium.yaml` |
| major | Preparation conditions were lost, leaving HCl and gas ingredients detached from their protocol roles. | TOGO M380 states pH 7.0, N2-CO2 80:20, anaerobic dispensing, autoclaving, overnight standing, and separate anaerobic cysteine/sulfide stock handling; the record has no `pH` and no `preparation_steps`. | `data/normalized_yaml/archaea/TOGO_M380_Methanosarcina_Acetivorans_Medium.yaml` |
| minor | Hydrate and cysteine ingredient rows are only partially enriched. | Exact primary ChEBI terms are present, but several rows with non-ASCII imported labels lack the parallel `mediaingredientmech_chebi_term` links that simpler rows received. | MediaIngredientMech enrichment and `data/normalized_yaml/archaea/TOGO_M380_Methanosarcina_Acetivorans_Medium.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/archaea/TOGO_M380_Methanosarcina_Acetivorans_Medium.yaml`, decide whether this TOGO-derived record preserves the TOGO M380 snapshot or is promoted to the live JCM 385 formulation. Keep the two versions explicitly separated; do not merge Na2CO3 from TOGO with NaHCO3 stock additions from current JCM.
2. Correct units in the maintained M380 owner: model water as 1 L or final volume context, resazurin as 1 mg, methanol as 6.5 ml, and the trace-mineral addition as 10 ml per liter.
3. Resolve TOGO `M142` into the JCM 151 trace-mineral stock, migrate that stock into the generated solution boundary, and preserve its KOH/pH preparation note.
4. Add source-backed preparation and condition fields for boiling, anaerobic N2-CO2 handling, pH 7.0 adjustment with HCl, dispensing/sealing, autoclaving, overnight standing, and cysteine/sulfide stock treatment.
5. Re-run ingredient enrichment after ASCII-safe normalization of hydrate and cysteine labels so rows that already have ChEBI terms can also receive MediaIngredientMech CHEBI links where a packaged exact match exists.
6. Regenerate `data/merge_yaml/merged/methanosarcina_acetivorans_medium__9ce1381f.yaml` from the maintained normalized owner and inspect the merge diff for unit, stock-boundary, and preparation-step preservation.

## Follow-up Checks

- Re-run the focused open schema, strict, reference, and term validators on the repaired normalized owner and on the regenerated merged record.
- Inspect the regenerated M380 YAML to confirm that no liter, milliliter, or milligram source quantity became `G_PER_L` unless a real, documented concentration conversion supports it.
- Inspect the regenerated trace-mineral solution to confirm that the M142/JCM 151 cross-reference is populated as a stock recipe rather than flattened into the final medium or left as an empty stub.
- Compare the maintained source notes with TOGO M380, TOGO M142, live JCM 385, and MediaDive J385 and confirm that source drift is either curated as a discussion item or resolved by a clear source-version choice.

## Additional Notes

- The TOGO M380 API record, TOGO M142 API record, MediaDive J385 REST record, live JCM 385 HTML page, and live JCM 151 HTML page were inspected directly.
- TOGO M142 identifies the referenced stock through the same API path as the immediate M380 source, so the empty trace-mineral solution is not a permanent external-access gap.
- This review did not create or edit GitHub issues, pull requests, or comments.
