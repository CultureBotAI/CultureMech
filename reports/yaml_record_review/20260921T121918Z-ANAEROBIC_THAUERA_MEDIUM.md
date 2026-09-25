# YAML Record Review: ANAEROBIC THAUERA MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml
- Started UTC: 2026-09-21T12:19:18Z
- Finished UTC: 2026-09-21T12:20:07Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:004072`
- Label: `ANAEROBIC THAUERA MEDIUM`
- Category: `bacterial`
- Source identity on canonical merge: KOMODO `1315`, cross-linked to DSMZ/MediaDive medium `1315`
- Generated status: generated merge record with fingerprint `18e315a896d9c1e58eb288abf03392c49c8066146504af5c1e4bcbb7818aa296`
- Merge lineage: three sources, `data/normalized_yaml/bacterial/anaerobic_thauera_medium.yaml`, `data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml`, and `data/normalized_yaml/specialized/anaerobic_thauera_medium.yaml`
- Maintained owner for future record edits: all three normalized records own their flattened DSMZ 1315 contents; the KOMODO resolver and MediaDive importer own any general fixes for DSMZ stock topology

## Validation

- Open schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml`
  - Result: passed
- Strict schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml --out /private/tmp/ANAEROBIC_THAUERA_MEDIUM.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 total checks
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed
- Embedded curation history: Not checked. The documented `just validate-history` recipe validates standalone records under `history/`; I did not find a focused embedded `MediaRecipe.curation_history` validator for one merge file.

## Identity and Grounding

The three inputs appear to be duplicate views of DSMZ Medium 1315. The inspected MediaDive payload reports `id: 1315`, `ANAEROBIC THAUERA MEDIUM`, pH 7.1 to 7.5, source `DSMZ`, and the DSMZ Medium 1315 PDF link; the inspected PDF has the same medium number and title. The KOMODO `1315.1` source label is a strain-specific view of the same DSMZ medium, not an independent formulation.

The canonical record still carries the KOMODO `Aerobic: Yes` note even though DSMZ says to gas the medium with 90 percent N2 plus 10 percent CO2 to achieve anaerobic conditions. It also flattens every source stock into the top-level ingredient list, so many chemically plausible primary terms are attached at the wrong recipe level.

`KNO3` still has a legacy `mediaingredientmech_term` despite the curation history saying all 31 legacy MIM links were replaced. `NiCl2 x 6 H2O` is grounded to `CHEBI:34887`/`nickel dichloride`, losing the hexahydrate form used in trace element solution SL-10.

## Evidence

Supported:

- DSMZ 1315 and MediaDive support the basal recipe with 0.85 g KNO3, 2.52 g NaHCO3, 0.01 g CaCl2, 0.50 g MgSO4.7H2O, 0.01 g MnSO4, 0.30 g NH4Cl, 0.05 g NaCl, 2 ml selenite-tungstate solution, and 884 ml distilled water.
- DSMZ 1315 and MediaDive support adding 100 ml phosphate solution, 10 ml acetate solution, 5 ml vitamin solution, and 1 ml trace element solution SL-10 after cooling.
- DSMZ 1315 and MediaDive support phosphate solution as 1.45 g Na2HPO4.2H2O plus 0.25 g KH2PO4 in 100 ml water, and acetate solution as 9.80 g potassium acetate in 100 ml water.
- DSMZ 1315 and MediaDive support the imported vitamin, SL-10, and selenite-tungstate stock recipes.
- DSMZ 1315 supports an acetate-to-sodium-capronate replacement only for named strains and reports the Na-capronate stock as 2.76 g per 100 ml.

Unsupported or over-scoped:

- Phosphate, acetate, vitamin, SL-10, and selenite-tungstate stocks are flattened into top-level ingredients at full stock strength.
- The 884 ml basal water row and all stock water rows are missing.
- The capronate replacement is preserved only in free text and not as a strain-specific variant.
- The KOMODO `Aerobic: Yes` note conflicts with the DSMZ anaerobic gas handling.
- DSMZ preparation steps are broad text steps and are not attached structurally to the basal medium, phosphate stock, acetate stock, vitamin stock, trace stock, and selenite-tungstate stock.

## Completeness

Consequential gaps:

- The source medium's stock additions and stock compositions are not represented as separate solution boundaries.
- The water rows needed to audit the basal and stock volumes are absent.
- The sodium-capronate substitution for DSM 12141, DSM 12142, DSM 11243, and DSM 12144 is not represented as a structured variant.
- No structured preparation distinguishes basal gassing and autoclaving from the phosphate autoclave, acetate filtering and N2 gassing, vitamin filtering, SL-10 autoclaving, and selenite-tungstate autoclaving.
- No structured `references` entry captures the DSMZ PDF, MediaDive source, or KOMODO sources beyond prose `notes`.

Correctly empty or not scored:

- `target_organisms` and `growth_metrics` are empty. DSMZ Medium 1315 is a recipe source, not primary growth evidence.
- The merge of KOMODO 1315, KOMODO 1315.1, and MediaDive 1315 appears appropriate because all three owners resolve to the same DSMZ medium.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ANAEROBIC_THAUERA_MEDIUM.md' -print` found no prior report for this generated record before the report was written; `find` included ignored report files.
- `find data/normalized_yaml -type f -name 'anaerobic_thauera_medium.yaml' -print` found same-stem normalized owners under `bacterial` and `specialized`; `find` included ignored files.
- `find data/normalized_yaml -type f -name 'for_strains_dsm_12138_12139_12140_and_12143.yaml' -print` found the KOMODO 1315.1 owner under `bacterial`; `find` included ignored files.
- `rg --no-ignore --hidden -F 'mediadive.medium:1315' data/normalized_yaml data/merge_yaml data/culturemech_recipe_catalog.tsv data/culturemech_id_registry.tsv` found all three normalized owners and this generated merge.

## Findings

| ID | Severity | Finding | Maintained owner |
| --- | --- | --- | --- |
| F1 | major | Phosphate, acetate, vitamin, trace-element, and selenite-tungstate stocks are flattened into top-level final-medium ingredients at stock strength instead of remaining 100 ml, 10 ml, 5 ml, 1 ml, and 2 ml additions. | All three normalized owners and the KOMODO/MediaDive importers |
| F2 | major | Source water rows are missing across the basal solution and all imported stocks, preventing volume and dilution checks. | All three normalized owners and the importers |
| F3 | major | The DSMZ sodium-capronate replacement for four strains is free text only and not a structured strain-scoped variant. | All three normalized owners |
| F4 | major | Preparation steps do not structurally preserve the different sterilization and gas treatments for the basal medium and each stock, and the KOMODO `Aerobic: Yes` note conflicts with DSMZ anaerobic preparation. | All three normalized owners, especially the two KOMODO owners for the stale note |
| F5 | major | `NiCl2 x 6 H2O` is grounded as anhydrous `CHEBI:34887` nickel dichloride rather than a hexahydrate-specific material. | All three normalized owners |
| F6 | minor | `KNO3` still carries `mediaingredientmech_term: MediaIngredientMech:000170` instead of `mediaingredientmech_chebi_term` despite the migration history claiming all legacy links were replaced. | All three normalized owners or the MIM legacy migration |
| F7 | minor | DSMZ, MediaDive, and KOMODO sources are present only in `notes`/`curation_history`, with no structured `references` entry available for future evidence validation. | All three normalized owners |

## Recommended Edits

1. Restore the DSMZ solution topology: basal 884 ml plus 2 ml selenite-tungstate stock, 100 ml phosphate stock, 10 ml acetate stock, 5 ml vitamin stock, and 1 ml SL-10 stock.
2. Keep phosphate, acetate, vitamin, SL-10, and selenite-tungstate compositions nested under their stock solution records rather than inlining them into the final medium.
3. Restore water rows for the basal medium and every stock.
4. Model the Na-capronate replacement as a DSM 12141/12142/11243/12144-specific variant or conditional stock substitution, preserving 2.76 g per 100 ml.
5. Replace the stale KOMODO `Aerobic: Yes` note with source-faithful anaerobic preparation metadata.
6. Correct `NiCl2 x 6 H2O` by either grounding it to a hydrate-specific term or leaving the unresolved source label ungrounded; do not keep the anhydrous nickel dichloride term.
7. Finish migrating `KNO3` from `mediaingredientmech_term` to `mediaingredientmech_chebi_term`.
8. Add structured references for KOMODO 1315, KOMODO 1315.1, MediaDive 1315, and DSMZ Medium 1315.
9. Regenerate `data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml` from the corrected normalized owners.

## Follow-up Checks

- Re-run open schema, strict schema, reference validation, and term validation on the two `anaerobic_thauera_medium.yaml` owners and `data/normalized_yaml/bacterial/for_strains_dsm_12138_12139_12140_and_12143.yaml`.
- Re-run the same focused validators on regenerated `data/merge_yaml/merged/ANAEROBIC_THAUERA_MEDIUM.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration to prove all normalized owners merge cleanly into one source-faithful canonical record.
- Manually compare the regenerated record against MediaDive 1315 and DSMZ Medium 1315, checking stock volumes, water rows, the capronate strain variant, NiCl2 hexahydrate grounding, gas handling, and final pH.

## Additional Notes

- Direct `just validate-schema`, `just validate-strict`, `just validate-terms`, and `just validate-references` were not used for this report because the project `uv` environment attempted to build `llvmlite==0.46.0` under Python 3.13 and failed before target-specific validation. The no-project Python 3.11 commands above were used as focused equivalents.
- The generated merge selects the KOMODO 1315 source ID and stable ID but also merges KOMODO 1315.1 and the direct MediaDive/DSMZ import; that duplicate merge is source-plausible even though all inputs need the same stock-topology repair.
