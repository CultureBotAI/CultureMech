# YAML Record Review: MOLLICUTES MZ-XQ MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mollicutes_mz_xq_medium__aa7ddd0e.yaml
- Started UTC: 2026-09-24T13:59:33Z
- Finished UTC: 2026-09-24T14:00:06Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:002333 |
| Name | mollicutes_mz_xq_medium |
| Original name | MOLLICUTES MZ-XQ MEDIUM |
| Source owner | data/normalized_yaml/bacterial/mollicutes_mz_xq_medium.yaml |
| Generated record | Yes; produced under data/merge_yaml/merged with merge_fingerprint aa7ddd0eac5bfdd985ac624aff4c56f285b0fb7a9286dfca8e092082224cc135 |

## Validation

| Check | Result |
| --- | --- |
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mollicutes_mz_xq_medium__aa7ddd0e.yaml` | Passed; `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/mollicutes_mz_xq_medium__aa7ddd0e.yaml --out /private/tmp/mollicutes_mz_xq_medium__aa7ddd0e.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows, and the TSV contained only the header. |
| `linkml-reference-validator validate data data/merge_yaml/merged/mollicutes_mz_xq_medium__aa7ddd0e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 references were checked. |
| `linkml-term-validator validate-data data/merge_yaml/merged/mollicutes_mz_xq_medium__aa7ddd0e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the expected `eutils` / `pkg_resources` warning. |
| Embedded `curation_history` | Not checked: the documented history validator targets the standalone `history/` corpus, not inline `MediaRecipe.curation_history`. |

## Identity and Grounding

The local name and JCM URL identify this record as JCM GRMD 1160, `MOLLICUTES MZ-XQ MEDIUM`. The live JCM page and TOGO M1242 agree on that identity, so the source recipe is real, but it is already represented by `data/merge_yaml/merged/mollicutes_mz_xq_medium.yaml` with TOGO:M1242.

The `media_term` is not well grounded: it stores `mediadive.medium:J1160` even though the page is JCM GRMD 1160. An ignored-inclusive search over `data/normalized_yaml` and `data/merge_yaml` for `GRMD=1160`, `JCM_M1160`, `mediadive.medium:J1160`, `MOLLICUTES MZ-XQ MEDIUM`, `Mollicutes MZ-XQ Medium`, and `TOGO:M1242` found exactly this direct-JCM source and the TOGO M1242 source, plus their generated outputs and indexes.

Most direct ingredient CHEBI groundings are plausible, but the flattened M888 row `NiCl2 x 6 H2O` is grounded to CHEBI:34887 `nickel dichloride`, which does not capture the hexahydrate named by the source.

## Evidence

The live JCM GRMD 1160 page supports 0.1 g KH2PO4, 4 g MgCl2 x 6 H2O, 1 g CaCl2 x 2 H2O, 0.5 g NH4Cl, 25 g NaCl, 1 g yeast extract, 1.8 g glucose, 2 ml trace vitamins from Medium 284, 1 ml trace mineral solution from Medium 852, 1 ml Se/W solution from Medium 852, 1 mg resazurin, and 1 L distilled water before the three post-autoclave stock additions.

The legacy import changed that evidence in several ways:

| Source claim | Generated representation | Assessment |
| --- | --- | --- |
| Basal formula is listed against 1 L distilled water | Basal masses are divided by the later stock volumes, for example 25 g NaCl became 24.0154 g/L and 1.8 g glucose became 1.72911 g/L | The record no longer preserves the source recipe amounts. |
| 25 ml 8% NaHCO3, 6 ml 5% L-Cysteine-HCl-H2O, and 6 ml 5% Na2S x 9 H2O | Top-level `25 G_PER_L`, `6 G_PER_L`, and `6 G_PER_L` ingredient rows | These are stock-solution volumes, not final grams per liter. |
| M278 trace vitamins and M888 trace minerals are milliliter additions | M278 and M888 stock components are flattened into final ingredients at their stock concentrations | The record confuses stock recipes with final medium ingredients. |
| 1 ml M888 Se/W solution | A `Selenite-tungstate solution` with `1 G_PER_L` and a MediaDive solution link | The source reference is a 1 ml addition from JCM Medium 852, not a gram-per-liter MediaDive solution dose. |

The first preparation step is copied from JCM GRMD 1160 and correctly preserves the pH 7.5 adjustment and N2-CO2 4:1 anaerobic workflow.

## Completeness

No empty optional scalar fields are present, and the absent target organism list is not a schema defect for this provider recipe.

The stock hierarchy is missing. The generated record has one placeholder solution for Se/W and flattens the M278 trace-vitamin stock, M888 trace-mineral stock, 8% NaHCO3 stock, 5% L-Cysteine-HCl-H2O stock, and 5% Na2S x 9 H2O stock into top-level ingredients, so downstream users cannot reconstruct which components are final recipe ingredients and which are added as stock solutions.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | This generated record duplicates TOGO M1242 and assigns a second CultureMech ID to JCM GRMD 1160. | Both this file and `data/merge_yaml/merged/mollicutes_mz_xq_medium.yaml` point to GRMD 1160 / JCM_M1160 for Mollicutes MZ-XQ Medium. | `data/normalized_yaml/bacterial/mollicutes_mz_xq_medium.yaml` and source de-duplication before `merge_recipes.py`. |
| Major | The basal formula was normalized away from source amounts. | The JCM page lists 25 g NaCl, 1.8 g glucose, 1 g yeast extract, and 4 g MgCl2 x 6 H2O; the generated values are 24.0154, 1.72911, 0.960615, and 3.84246 g/L. | The legacy JCM/MediaDive import that produced `data/normalized_yaml/bacterial/mollicutes_mz_xq_medium.yaml`. |
| Major | Referenced M278 and M888 stock rows were flattened at stock concentration. | The source adds 2 ml trace vitamins, 1 ml trace minerals, and 1 ml Se/W solution; this record makes many stock ingredients, such as Vitamin B12 at 0.0271 g/L and FeCl2 x 4 H2O at 1.99 g/L, look like final ingredients. | The legacy JCM/MediaDive stock flattener. |
| Major | Three post-autoclave stock additions are represented as final gram-per-liter ingredients. | JCM GRMD 1160 lists 25 ml 8% NaHCO3, 6 ml 5% L-Cysteine-HCl-H2O, and 6 ml 5% Na2S x 9 H2O; the record has `25`, `6`, and `6 G_PER_L` rows. | `data/normalized_yaml/bacterial/mollicutes_mz_xq_medium.yaml`. |
| Major | The Se/W solution row has the wrong source and unit semantics. | JCM refers to a 1 ml Se/W solution from Medium 852; the row points to `mediadive.solution:5543` and stores `1 G_PER_L`. | The legacy JCM/MediaDive stock migration. |
| Major | NiCl2 x 6 H2O is grounded to an anhydrous nickel chloride class. | The preferred term names a hexahydrate but the CHEBI term is CHEBI:34887 `nickel dichloride`. | CHEBI enrichment over flattened stock ingredients. |
| Minor | The source CURIE is not a resolvable JCM term. | The record stores `mediadive.medium:J1160` for a JCM GRMD 1160 page. | `data/normalized_yaml/bacterial/mollicutes_mz_xq_medium.yaml`. |

## Recommended Edits

1. Reconcile `data/normalized_yaml/bacterial/mollicutes_mz_xq_medium.yaml` with `data/normalized_yaml/bacterial/TOGO_M1242_Mollicutes_MZ-XQ_Medium.yaml` so GRMD 1160 emits one generated record and one CultureMech ID.
2. Prefer the TOGO M1242 owner unless the legacy import contains source evidence missing from TOGO.
3. If this owner is retained, rebuild it from the JCM table so basal rows keep the JCM gram amounts and all six stock additions stay as milliliter additions.
4. Preserve M278 and M888 references as named stock links or copy only the trace-vitamins, trace-minerals, and Se/W subcomponents.
5. Replace `mediadive.medium:J1160` and `mediadive.solution:5543` with resolvable JCM or TOGO source references.
6. Correct the NiCl2 x 6 H2O CHEBI grounding after the stock rows are either structured or removed from the final flat recipe.

## Follow-up Checks

- Rerun `linkml-validate`, `scripts/validate_strict.py`, `linkml-reference-validator`, and `linkml-term-validator` after regenerating Mollicutes MZ-XQ.
- Run an ignored-inclusive search for `GRMD=1160`, `JCM_M1160`, `mediadive.medium:J1160`, and `TOGO:M1242` across `data/normalized_yaml` and `data/merge_yaml` to confirm that the duplicate direct-JCM record was reconciled or intentionally mapped.
- Manually compare the regenerated record against live JCM GRMD 1160 and TOGO M1242, including the six stock volumes and the N2-CO2 4:1 preparation text.

## Additional Notes

This record is a stale flat import of the same JCM page represented by TOGO M1242, so the future fix should start with source de-duplication rather than direct edits to the generated YAML.
