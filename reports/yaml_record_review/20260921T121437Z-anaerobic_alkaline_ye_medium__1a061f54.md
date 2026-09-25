# YAML Record Review: ANAEROBIC ALKALINE YE MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/anaerobic_alkaline_ye_medium__1a061f54.yaml
- Started UTC: 2026-09-21T12:14:37Z
- Finished UTC: 2026-09-21T12:15:17Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/anaerobic_alkaline_ye_medium__1a061f54.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:015429`
- Label: `ANAEROBIC ALKALINE YE MEDIUM`
- Category: `specialized`
- Source identity: MediaDive `mediadive.medium:J993`, source `JCM`, original JCM URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=993`
- Generated status: generated merge record with fingerprint `1a061f545724abdf2cc504de7046fc0e3fb24eb49db5fdf12ea537caade6596f`
- Merge lineage: one source, `data/normalized_yaml/specialized/anaerobic_alkaline_ye_medium.yaml`
- Maintained owner for future record edits: `data/normalized_yaml/specialized/anaerobic_alkaline_ye_medium.yaml`; the MediaDive importer owns any general fix for child-solution and milliliter-stock flattening

## Validation

- Open schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/anaerobic_alkaline_ye_medium__1a061f54.yaml`
  - Result: passed
- Strict schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/anaerobic_alkaline_ye_medium__1a061f54.yaml --out /private/tmp/anaerobic_alkaline_ye_medium__1a061f54.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/anaerobic_alkaline_ye_medium__1a061f54.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 total checks
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/anaerobic_alkaline_ye_medium__1a061f54.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed
- Embedded curation history: Not checked. The documented `just validate-history` recipe validates standalone records under `history/`; I did not find a focused embedded `MediaRecipe.curation_history` validator for one merge file.

## Identity and Grounding

The MediaDive source identity is internally consistent: the record is `mediadive.medium:J993`, the inspected MediaDive REST payload reports `id: J993`, `ANAEROBIC ALKALINE YE MEDIUM`, pH 9.0, source `JCM`, and a `GRMD=993` link, and the inspected JCM 993 page is the same named medium.

The merge identity is not canonical because the TOGO M1047 import of the same JCM 993 page is generated separately as `data/merge_yaml/merged/Anaerobic_Alkaline_YE_Medium.yaml`. The two normalized JCM 993 owners must be made source-faithful and then collapsed together or explicitly reconciled.

Most primary terms describe the literal ingredient names, but `NiCl2 x 6 H2O` is grounded to `CHEBI:34887`/`nickel dichloride`, losing the explicit hexahydrate in the source stock recipe. Several other top-level terms are chemically plausible only for the nested trace-element stock; they should not be final-medium ingredients at stock strength.

## Evidence

Supported:

- MediaDive J993 and JCM 993 support the JCM source identity, medium name, pH 9.0, the base salts, 1 mg resazurin, 900 ml distilled water, and one 1 ml addition of trace element solution.
- MediaDive solution `4186` and the trace-element table on JCM 439 support a 1 L stock containing 12.5 ml 25 percent HCl, 2.1 g FeSO4.7H2O, 30 mg H3BO3, 100 mg MnCl2.4H2O, 190 mg CoCl2.6H2O, 24 mg NiCl2.6H2O, 2 mg CuCl2.2H2O, 144 mg ZnSO4.7H2O, 36 mg Na2MoO4.2H2O, and 987 ml distilled water.
- JCM 993 supports adding 20 ml of 10 percent yeast extract, 30 ml of 8 percent NaHCO3, and 8 ml of 5 percent Na2S.9H2O from sterile anaerobic stocks after cooling and N2-CO2 gas-phase replacement.

Unsupported or over-scoped:

- The trace-element stock recipe is flattened into final-medium ingredients at stock strength even though JCM 993 uses only 1 ml of that stock.
- The final 20 ml yeast extract, 30 ml NaHCO3, and 8 ml Na2S.9H2O stock additions are represented as `20 G_PER_L`, `30 G_PER_L`, and `8 G_PER_L` dry ingredients.
- The 900 ml main-solution water row and the 987 ml trace-element-stock water row are missing.
- HCl is recorded as `12.5 G_PER_L` hydrogen chloride, but the source row is 12.5 ml of 25 percent HCl in the trace-element stock.
- NiCl2.6H2O is grounded to an anhydrous nickel chloride term.
- The single `AUTOCLAVE` preparation step also contains the post-cooling N2-CO2 gas replacement and sterile stock additions.

## Completeness

Consequential gaps:

- The trace-element solution is not preserved as a stock with 1 ml used in the J993 main recipe.
- The final yeast extract, bicarbonate, and sulfide stock additions are not preserved as sterile anaerobic volume additions.
- The two water rows needed to audit the main medium and trace-element stock volumes are absent.
- Preparation needs separate operations for pH 9.0 adjustment with NaOH, N2 autoclaving, N2-CO2 4:1 gas replacement, and addition from sterile anaerobic stocks.
- No structured `references` entry captures the JCM or MediaDive source beyond the prose `notes` field.

Correctly empty or not scored:

- `target_organisms`, `growth_metrics`, and variant links are empty. The inspected source pages are recipe sources, not primary growth evidence.
- The absence of a ChEBI term on `Yeast extract` is acceptable for a complex undefined stock.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*anaerobic_alkaline_ye_medium__1a061f54.md' -print` found no prior report for this generated record before the report was written; `find` included ignored report files.
- `rg --no-ignore --hidden -F 'mediadive.medium:J993' data/normalized_yaml data/merge_yaml data/culturemech_recipe_catalog.tsv data/culturemech_id_registry.tsv` found only the specialized J993 normalized owner and this generated merge among recipe records and ID/catalog data.
- `rg --no-ignore --hidden -F 'GRMD=993' data/normalized_yaml data/merge_yaml` found this J993 normalized owner and merge plus the TOGO M1047/JCM 993 normalized owner and its separate merge.

## Findings

| ID | Severity | Finding | Maintained owner |
| --- | --- | --- | --- |
| F1 | blocker | MediaDive J993 is the same JCM 993 recipe as TOGO M1047 but is emitted as a separate canonical merge. | `data/normalized_yaml/specialized/anaerobic_alkaline_ye_medium.yaml`, `data/normalized_yaml/bacterial/anaerobic_alkaline_ye_medium.yaml`, and the merge rules |
| F2 | major | MediaDive solution `4186` was flattened into undiluted final-medium trace-element rows even though only 1 ml of that 1 L stock is added. | `data/normalized_yaml/specialized/anaerobic_alkaline_ye_medium.yaml` and the MediaDive importer |
| F3 | major | The 20 ml 10 percent yeast extract, 30 ml 8 percent NaHCO3, and 8 ml 5 percent Na2S.9H2O stocks were retyped as grams-per-liter dry-compound additions. | `data/normalized_yaml/specialized/anaerobic_alkaline_ye_medium.yaml` and the MediaDive importer |
| F4 | major | The source's 900 ml main-water row and 987 ml trace-stock water row are both missing. | `data/normalized_yaml/specialized/anaerobic_alkaline_ye_medium.yaml` and the MediaDive importer |
| F5 | major | The preparation text is compressed into one `AUTOCLAVE` step that also includes post-cooling gas replacement and stock additions. | `data/normalized_yaml/specialized/anaerobic_alkaline_ye_medium.yaml` and the MediaDive step importer |
| F6 | major | `NiCl2 x 6 H2O` is grounded as anhydrous `CHEBI:34887` nickel dichloride rather than a hexahydrate-specific material. | `data/normalized_yaml/specialized/anaerobic_alkaline_ye_medium.yaml` |
| F7 | minor | The JCM and MediaDive sources are present only in `notes`/`curation_history`, with no structured `references` entry available for future evidence validation. | `data/normalized_yaml/specialized/anaerobic_alkaline_ye_medium.yaml` |

## Recommended Edits

1. Preserve `Trace element solution` as a nested stock solution and add 1 ml of it to the J993 main recipe instead of inlining stock concentrations into the final medium.
2. Replace the top-level yeast extract, NaHCO3, and Na2S.9H2O rows with 20 ml, 30 ml, and 8 ml sterile anaerobic stock additions at the percentages in the source.
3. Restore the 900 ml and 987 ml distilled-water rows in the main recipe and trace-element stock, respectively.
4. Correct `NiCl2 x 6 H2O` by either grounding it to a hydrate-specific term or leaving the unresolved source label ungrounded; do not keep the anhydrous nickel dichloride term.
5. Split the preparation into the source operations: mix and adjust pH to 9.0; autoclave under N2; cool; replace the gas phase with N2-CO2 4:1 v/v; add the sterile anaerobic stocks.
6. Add structured references for MediaDive J993, JCM 993, and the JCM 439 trace-element stock source.
7. Regenerate `data/merge_yaml/merged/*.yaml` and verify this MediaDive J993 source merges with the corrected TOGO M1047 source instead of remaining a standalone canonical record.

## Follow-up Checks

- Re-run open schema, strict schema, reference validation, and term validation on `data/normalized_yaml/specialized/anaerobic_alkaline_ye_medium.yaml`.
- Re-run the same focused validators on the regenerated merge that replaces `data/merge_yaml/merged/anaerobic_alkaline_ye_medium__1a061f54.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration to prove the normalized owner and generated merge match.
- Manually compare the regenerated record against MediaDive J993, JCM 993, and the JCM 439 trace-element stock to verify all stock volumes, dilution boundaries, water rows, and the NiCl2 hexahydrate label.
- Search ignored and tracked data again for `GRMD=993`, `TOGO:M1047`, and `mediadive.medium:J993` to confirm the TOGO and MediaDive source records are no longer split across conflicting generated merges.

## Additional Notes

- Direct `just validate-schema`, `just validate-strict`, `just validate-terms`, and `just validate-references` were not used for this report because the project `uv` environment attempted to build `llvmlite==0.46.0` under Python 3.13 and failed before target-specific validation. The no-project Python 3.11 commands above were used as focused equivalents.
- The inspected generated merge and normalized owner are identical through the source-owned fields; the generated record only adds the `merge_recipes.py` curation event, `merge_fingerprint`, and `merged_from`.
- The TOGO M1047/JCM 993 source record was checked in the adjacent `Anaerobic_Alkaline_YE_Medium` review.
