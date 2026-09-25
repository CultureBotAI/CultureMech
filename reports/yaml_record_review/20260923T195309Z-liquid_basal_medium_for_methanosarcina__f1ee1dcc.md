# YAML Record Review: LIQUID BASAL MEDIUM FOR METHANOSARCINA

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/liquid_basal_medium_for_methanosarcina__f1ee1dcc.yaml
- Started UTC: 2026-09-23T19:50:39Z
- Finished UTC: 2026-09-23T19:53:09Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002284 |
| Name | liquid_basal_medium_for_methanosarcina |
| Original name | LIQUID BASAL MEDIUM FOR METHANOSARCINA |
| Category | archaea |
| Medium/composition type | DEFINED / DEFINED |
| Physical state | LIQUID |
| Structured pH | 7.2 |
| Media grounding | mediadive.medium:J1107 |
| Source provenance | JCM Medium 1107 via MediaDive |
| Generated file | data/merge_yaml/merged/liquid_basal_medium_for_methanosarcina__f1ee1dcc.yaml |
| Maintained owner | data/normalized_yaml/archaea/liquid_basal_medium_for_methanosarcina.yaml |
| Merge fingerprint | f1ee1dcc27b9dd906032ed478d6094c099123a4731a66fad795b2df51128772f |

The reviewed target is the generated MediaDive import of JCM GRMD 1107. Future fixes belong in `data/normalized_yaml/archaea/liquid_basal_medium_for_methanosarcina.yaml` or the MediaDive importer, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/liquid_basal_medium_for_methanosarcina__f1ee1dcc.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/liquid_basal_medium_for_methanosarcina__f1ee1dcc.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The MediaDive REST record and the live JCM GRMD 1107 page both identify the source as `LIQUID BASAL MEDIUM FOR METHANOSARCINA`, a pH 7.2 archaeal defined liquid medium.

The generated record keeps the JCM 1107/MediaDive identity, class, pH, category, and all non-water stock component names, but it flattens both stock recipes: the 1 ml/L JCM 1107 trace-elements solution and the 10 ml/L JCM 944 vitamin solution are represented as main-medium ingredient rows.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:002284`, `mediadive.medium:J1107`, `GRMD=1107`, the maintained filename, the merge fingerprint, and the shared slug found this MediaDive/JCM owner, a separate Togo M1184 owner that also points at JCM 1107, both generated siblings, and source indexes.

## Evidence

Supported in the inspected JCM and MediaDive sources:

- JCM 1107 supplies 0.5 g KH2PO4, 0.4 g NH4Cl, 0.4 g MgCl2 x 6 H2O, 0.05 g CaCl2 x 2 H2O, 0.4 g NaCl, 4.2 g MOPS, 1 ml trace-elements solution, 1 mg resazurin, and 930 ml distilled water before autoclaving at pH 7.2 under N2-CO2.
- After cooling, the medium receives 50 ml 8 percent NaHCO3 stock, 10 ml vitamin solution from JCM 944, and 10 ml 50 percent v/v methanol.
- After dispensing, it receives 10 ml 5 percent L-cysteine-HCl-H2O stock and 10 ml 5 percent Na2S x 9 H2O stock.
- JCM 1107 defines the trace-elements stock as an 11-component 1 L solution; JCM 944 and MediaDive define the vitamin stock as a 10-component 1 L solution.

Unsupported or incomplete in the generated record:

- The trace-elements stock and vitamin stock are flattened into top-level ingredient rows at stock concentration.
- The maintained owner has an unmerged 2026-08-13 `apply_cocktail_nesting.py` event that moved only seven trace-element rows into a `Trace elements solution`; the generated target still lacks that partial solution, and the owner still leaves nitrilotriacetic acid trisodium salt monohydrate, Na2SeO3 x 5 H2O, H3BO3, and CuSO4 x 5 H2O at top level.
- The 50 ml NaHCO3, 10 ml methanol, 10 ml L-cysteine-HCl-H2O, and 10 ml Na2S x 9 H2O stock additions are represented as 50, 10, 10, and 10 g/L solute rows.
- NiCl2 x 6 H2O is grounded to CHEBI:34887 / nickel dichloride, which loses the source hydrate form.
- The main 930 ml water row and the 1 L water rows for the trace-elements and vitamin stocks are absent.
- The generated record has no structured reference to MediaDive J1107, JCM GRMD 1107, or the linked JCM GRMD 944 vitamin source.

## Completeness

The record is complete for the JCM 1107 source identity, archaeal category, pH, main basal salts, final pH readjustment, N2-CO2 atmosphere, post-autoclave and final stock-addition timing, and all visible non-water trace and vitamin stock component names.

It is incomplete for stock-solution nesting, the four liquid stock-addition units, water amounts, exact hydrate grounding for NiCl2 x 6 H2O, cross-import linkage to the Togo M1184 sibling, and structured references. Empty optional target-organism, incubation, and storage fields are acceptable for this review because the inspected MediaDive/JCM sources do not state those values.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | `Trace elements solution` is flattened and incomplete in the maintained partial fix. | JCM 1107 adds a 1 ml/L trace-elements stock with 11 non-water rows. The generated target flattens all 11 rows; the normalized owner now nests only seven of them and still leaves four trace-stock rows at top level. | `data/normalized_yaml/archaea/liquid_basal_medium_for_methanosarcina.yaml` |
| Major | `Vitamin solution` from JCM 944 is flattened into ten top-level vitamin rows. | JCM 1107 adds 10 ml vitamin solution, and JCM 944 defines the stock; the generated record lists all ten vitamin stock components as if their stock concentrations were main-medium concentrations. | `data/normalized_yaml/archaea/liquid_basal_medium_for_methanosarcina.yaml` |
| Major | Four milliliter stock additions were converted to gram-per-liter solute rows. | JCM 1107 gives 50 ml of 8 percent NaHCO3 stock, 10 ml of 50 percent v/v methanol, 10 ml of 5 percent L-cysteine-HCl-H2O stock, and 10 ml of 5 percent Na2S x 9 H2O stock; the YAML stores them as 50, 10, 10, and 10 `G_PER_L`. | `data/normalized_yaml/archaea/liquid_basal_medium_for_methanosarcina.yaml` or the MediaDive importer |
| Major | NiCl2 x 6 H2O is over-broadly grounded. | The JCM 1107 trace-elements stock names nickel chloride hexahydrate, while the YAML maps that row to CHEBI:34887 / nickel dichloride. | `data/normalized_yaml/archaea/liquid_basal_medium_for_methanosarcina.yaml` |
| Minor | Distilled water rows are missing. | JCM and MediaDive list 930 ml water for the main medium, 1000 ml for the trace-elements stock, and 1000 ml for the vitamin stock; no water context is represented in the generated target. | `data/normalized_yaml/archaea/liquid_basal_medium_for_methanosarcina.yaml` |
| Minor | JCM's page-level autoclave temperature and time are missing. | The JCM page states that media are sterilized by autoclaving at 121 C for 15 min unless otherwise stated; the YAML records autoclaving under N2-CO2 but omits the default temperature and duration. | `data/normalized_yaml/archaea/liquid_basal_medium_for_methanosarcina.yaml` or the MediaDive importer |
| Minor | A Togo M1184 sibling also resolves to JCM 1107 but remains a separate generated record. | The ignored-inclusive search found `data/normalized_yaml/archaea/TOGO_M1184_Liquid_Basal_Medium_For_Methanosarcina.yaml`, and its notes name the same JCM GRMD 1107 URL as the original source. | Both maintained owners or merge reconciliation logic |
| Minor | Structured references are missing. | The generated target carries only a free-text JCM URL in `notes`, and the reference validator performed zero checks. | `data/normalized_yaml/archaea/liquid_basal_medium_for_methanosarcina.yaml` |

## Recommended Edits

1. Complete `Trace elements solution` nesting in the maintained owner so all 11 JCM 1107 trace-stock components live under the 1 ml/L solution, with 1 L water context preserved.
2. Move all ten vitamin rows under a 10 ml/L `Vitamin solution` sourced from JCM 944, with 1 L water context preserved.
3. Restore 8 percent NaHCO3, 50 percent v/v methanol, 5 percent L-cysteine-HCl-H2O, and 5 percent Na2S x 9 H2O as 50, 10, 10, and 10 ml stock additions.
4. Replace the NiCl2 x 6 H2O CHEBI grounding with a hydrate-specific term if one is available in the ingredient index; otherwise leave the exact preferred term unresolved.
5. Add the JCM default autoclave condition, 121 C for 15 min, to the preparation detail.
6. Add structured references for MediaDive J1107, JCM GRMD 1107, and JCM GRMD 944.
7. Reconcile or explicitly link the MediaDive J1107 and Togo M1184 Liquid Basal Medium for Methanosarcina records.
8. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated record against MediaDive J1107, JCM 1107, and JCM 944 for the 1 ml trace-elements stock, 10 ml vitamin stock, and four other milliliter stock additions.
- Re-run an ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:002284`, `mediadive.medium:J1107`, `GRMD=1107`, `TOGO:M1184`, and `liquid_basal_medium_for_methanosarcina` to confirm the MediaDive and Togo siblings are linked or intentionally distinguished.

## Additional Notes

The generated record predates the August owner-side partial trace-elements nesting. Regenerating without further curation would move seven rows out of the top-level ingredient list, but it would still leave four trace-stock rows and all vitamin-stock rows flattened.
