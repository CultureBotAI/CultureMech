# YAML Record Review: ANAEROBIC AZOSPIRILLUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml
- Started UTC: 2026-09-21T12:16:15Z
- Finished UTC: 2026-09-21T12:16:56Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:015346`
- Label: `ANAEROBIC AZOSPIRILLUM MEDIUM`
- Category: `specialized`
- Source identity: MediaDive `mediadive.medium:1701`, source `DSMZ`, original DSMZ PDF `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1701.pdf`
- Generated status: generated merge record with fingerprint `d26b75c88eec68aab103f3bc15fe70c9609f7360a059ad9e5f73f8e90e7c6a3b`
- Merge lineage: one source, `data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml`
- Maintained owner for future record edits: `data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml`; the MediaDive importer owns any general fix for multi-solution DSMZ media and trace-stock flattening

## Validation

- Open schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml`
  - Result: passed; no issues found
- Strict schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml --out /private/tmp/ANAEROBIC_AZOSPIRILLUM_MEDIUM.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 total checks
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed
- Embedded curation history: Not checked. The documented `just validate-history` recipe validates standalone records under `history/`; I did not find a focused embedded `MediaRecipe.curation_history` validator for one merge file.

## Identity and Grounding

The record correctly denotes DSMZ/MediaDive medium 1701, `ANAEROBIC AZOSPIRILLUM MEDIUM`: the inspected MediaDive payload reports `id: 1701`, the same name, source `DSMZ`, the DSMZ Medium 1701 PDF link, and pH range 7.2 to 7.4. The inspected DSMZ PDF has the same medium number and title.

Primary ingredient grounding is mostly plausible for the literal labels, but `NiCl2 x 6 H2O` is grounded to `CHEBI:34887`/`nickel dichloride`, dropping the hexahydrate specified by DSMZ. Many other grounded ingredients are only members of stock solutions and should not be top-level final-medium ingredients at their stock strengths.

## Evidence

Supported:

- MediaDive and DSMZ support Solution A with 0.70 g KH2PO4, 0.30 g NH4Cl, 2.80 g Na2SO4, 1.70 g MgCl2.6H2O, 0.05 g CaCl2.2H2O, 10.00 g NaCl, 0.5 g yeast extract, 1 ml Trace element solution SL-10, 0.50 ml 0.1 percent sodium resazurin solution, and 940 ml distilled water.
- MediaDive and DSMZ support completing the medium by adding 10 ml Solution C, 20 ml Solution D, and 10 ml Solution E to sterile Solution A, where those stocks contain 1.62 g sodium succinate in 10 ml water, 1.00 g Na2CO3 in 20 ml water, and 0.30 g Na2S.9H2O in 10 ml water.
- MediaDive and DSMZ support the 1 L Trace element solution SL-10 recipe with 10 ml 25 percent HCl, 1.50 g FeCl2.4H2O, seven mg-scale salts, and 990 ml distilled water.
- MediaDive and DSMZ support sparging Solution A with 80 percent N2 and 20 percent CO2 for at least 30 min, autoclaving Solutions C and E under 100 percent N2, autoclaving Solution D under the 80/20 gas mixture, and a final pH of 7.2 to 7.4.

Unsupported or over-scoped:

- The record flattens Solution C, Solution D, Solution E, and Trace element solution SL-10 into top-level ingredients at their stock concentrations.
- The 940 ml Solution A water, 10 ml Solution C water, 20 ml Solution D water, 10 ml Solution E water, and 990 ml SL-10 water rows are missing.
- HCl is represented as `2.5 G_PER_L` hydrogen chloride, but DSMZ lists 10 ml of 25 percent HCl as an SL-10 stock component.
- `high_metal: true` appears to be a byproduct of inlining FeCl2 and other trace metals at full stock strength into the final medium.
- The preparation representation keeps the DSMZ text only as two broad steps and does not attach the separate gas atmosphere and autoclaving rules to Solutions A, C, D, and E.

## Completeness

Consequential gaps:

- No solution structure preserves the 940 ml, 10 ml, 20 ml, and 10 ml top-level additions or the nested SL-10 trace-element stock.
- No water rows remain for any solution.
- No structured stock-preparation details distinguish Solution A's N2-CO2 sparging from the 100 percent N2 autoclaving of Solutions C and E and the N2-CO2 autoclaving of Solution D.
- No structured `references` entry captures the DSMZ PDF or MediaDive source beyond the prose `notes` field.

Correctly empty or not scored:

- `target_organisms`, `growth_metrics`, and variant links are empty. DSMZ Medium 1701 is a recipe source, not primary growth evidence.
- The absence of a ChEBI term on `Yeast extract` is acceptable for a complex undefined ingredient.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ANAEROBIC_AZOSPIRILLUM_MEDIUM.md' -print` found no prior report for this generated record before the report was written; `find` included ignored report files.
- `rg --no-ignore --hidden -F 'mediadive.medium:1701' data/normalized_yaml data/merge_yaml data/culturemech_recipe_catalog.tsv data/culturemech_id_registry.tsv` found only the specialized normalized owner and this generated merge among recipe records and ID/catalog data.

## Findings

| ID | Severity | Finding | Maintained owner |
| --- | --- | --- | --- |
| F1 | major | Solutions C, D, and E are flattened into top-level final-medium rows at stock strength: 162 g/L sodium succinate, 50 g/L Na2CO3, and 30 g/L Na2S.9H2O instead of 10 ml, 20 ml, and 10 ml stock additions. | `data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml` and the MediaDive importer |
| F2 | major | Trace element solution SL-10 is flattened into top-level final-medium rows even though only 1 ml is added to Solution A. | `data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml` and the MediaDive importer |
| F3 | major | Five source water rows are missing across Solution A, Solutions C to E, and SL-10, preventing volume and dilution checks. | `data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml` and the MediaDive importer |
| F4 | major | DSMZ solution-specific sparging and autoclaving instructions are stored as two broad text steps rather than structured preparation tied to individual solutions. | `data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml` and the MediaDive step importer |
| F5 | major | `NiCl2 x 6 H2O` is grounded as anhydrous `CHEBI:34887` nickel dichloride rather than a hexahydrate-specific material. | `data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml` |
| F6 | minor | The DSMZ and MediaDive sources are present only in `notes`/`curation_history`, with no structured `references` entry available for future evidence validation. | `data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml` |

## Recommended Edits

1. Restore the DSMZ solution hierarchy: 940 ml Solution A plus 10 ml Solution C, 20 ml Solution D, and 10 ml Solution E as the main medium.
2. Preserve Trace element solution SL-10 as a 1 L stock and add only 1 ml of it to Solution A.
3. Restore distilled-water rows for Solution A, C, D, E, and SL-10.
4. Recompute or remove `high_metal: true` after trace metals are no longer inlined into the final medium at stock strength.
5. Split preparation into structured steps for Solution A N2-CO2 sparging, Solution A distribution and autoclaving, Solutions C/E 100 percent N2 autoclaving, Solution D N2-CO2 autoclaving, addition of C to E to sterile A, and the final pH 7.2 to 7.4 check.
6. Correct `NiCl2 x 6 H2O` by either grounding it to a hydrate-specific term or leaving the unresolved source label ungrounded; do not keep the anhydrous nickel dichloride term.
7. Add structured references for MediaDive 1701 and the DSMZ Medium 1701 PDF.
8. Regenerate `data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml` from the corrected normalized owner.

## Follow-up Checks

- Re-run open schema, strict schema, reference validation, and term validation on `data/normalized_yaml/specialized/anaerobic_azospirillum_medium.yaml`.
- Re-run the same focused validators on regenerated `data/merge_yaml/merged/ANAEROBIC_AZOSPIRILLUM_MEDIUM.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration to prove the normalized owner and generated merge match.
- Manually compare the regenerated record against MediaDive 1701 and DSMZ Medium 1701, checking all solution volumes, SL-10 dilution, five water rows, NiCl2 hexahydrate grounding, gas atmospheres, and final pH.

## Additional Notes

- Direct `just validate-schema`, `just validate-strict`, `just validate-terms`, and `just validate-references` were not used for this report because the project `uv` environment attempted to build `llvmlite==0.46.0` under Python 3.13 and failed before target-specific validation. The no-project Python 3.11 commands above were used as focused equivalents.
- The inspected generated merge and normalized owner are identical through the source-owned fields; the generated record only adds the `merge_recipes.py` curation event, `merge_fingerprint`, and `merged_from`.
