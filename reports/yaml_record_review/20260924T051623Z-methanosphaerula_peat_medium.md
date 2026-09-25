# YAML Record Review: Methanosphaerula (Peat) Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanosphaerula_peat_medium.yaml
- Started UTC: 2026-09-24T05:14:19Z
- Finished UTC: 2026-09-24T05:16:23Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methanosphaerula_peat_medium.yaml`, a generated `MediaRecipe` for `CultureMech:009210` with `name: methanosphaerula_peat_medium`, `original_name: Methanosphaerula (Peat) Medium`, and medium grounding `TOGO:M2655`.

The merged record was generated from `TOGO_M2655_Methanosphaerula_Peat_Medium`; the maintained owner for future record-level edits is `data/normalized_yaml/archaea/TOGO_M2655_Methanosphaerula_Peat_Medium.yaml`. Regenerate `data/merge_yaml/merged/methanosphaerula_peat_medium.yaml` after fixing that input and any import or solution-migration code that produced the same lossy shape.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanosphaerula_peat_medium.yaml` | Passed; `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methanosphaerula_peat_medium.yaml --out /private/tmp/methanosphaerula_peat_medium.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methanosphaerula_peat_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methanosphaerula_peat_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The record label and `media_term` identify TOGO medium `M2655`, "Methanosphaerula (Peat) Medium", whose original URL is DSMZ medium 1094. The current DSMZ PDF and MediaDive REST record also identify DSMZ 1094 as `METHANOSPHAERULA (PEAT) MEDIUM`, so the base medium identity is correct.

The imported solution identity is not correct. DSMZ/MediaDive 1094 names the nested stocks `Solution A` through `Solution G`, `Trace element solution`, and `Wolin's vitamin solution (10x)` with MediaDive solution IDs 2201 through 2208 plus 5980 for the Wolin stock. The record instead links Solution A-G and the trace element stock to `mediadive.solution:5342`, `5343`, `5312`, `5313`, `4959`, `6293`, `3625`, and `6187`, none of which are the solution IDs for DSMZ medium 1094.

## Evidence

Supported source claims:

- TOGO `M2655` supports the record's name, TOGO grounding, pH 5.7 metadata, and DSMZ medium 1094 source URL.
- TOGO `M2655` supports final-medium entries for Solution A-G, 80% N2/20% CO2, 80% H2/20% CO2, Solution A constituents, trace element constituents, Solution C, Wolin vitamins, Solution E, Solution F, and Solution G.
- The DSMZ 1094 PDF and MediaDive REST record support the same nested stock structure, the final pH of 5.7, the special preparation of Solution A-G, the one-night equilibration step, the post-inoculation H2/CO2 overpressure, and the short stability note.

Unsupported or over-scoped generated claims:

- The record serializes the final additions of Solution A-G as `G_PER_L` concentrations rather than as milliliter additions to a final medium.
- The record serializes nested stocks from Solution A, Solution B, and the trace element stock as empty top-level `solutions` entries with `G_PER_L` values: `NH4Cl solution (0.1% w/v)`, `KH2PO4 solution (0.1% w/v)`, `KCl solution (0.1% w/v)`, `Trace element solution`, `TRIS-HCl (1.0 M solution, pH 8.0)`, `NaNTA (0.5 M solution)`, and `TiCl3 (15% w/v solution in HCl; Riedel-de Haen)`.
- The record serializes stock-only dry masses as final-medium `G_PER_L` ingredient concentrations. Examples include trace-stock rows such as `Na2Mo4 x 2 H2O: 24 G_PER_L`, `H3BO3: 19 G_PER_L`, and `CuSO4 x 5 H2O: 9 G_PER_L`, which are milligram rows in 1 L trace stock, and vitamin rows such as `Biotin: 2 G_PER_L`, which belongs inside the Wolin vitamin stock.
- The `Distilled water` ingredient is a cross-stock sum: its note shows 890, 1000, 20, 1000, 10, 10, and 10 ml water rows merged into one `2940.0 G_PER_L` ingredient, erasing the Solution A, trace stock, Solution C, Wolin stock, and Solution E-G boundaries.
- TOGO `M2655` and the imported record disagree with the current DSMZ 1094 PDF and MediaDive REST record on several source quantities. DSMZ/MediaDive use Solution A 943 ml, Solution B 13 ml, Solution D 1 ml, and Solution A water 900 ml; TOGO and this record use Solution A 932.9 ml, Solution B 12.55 ml, Solution D 10 ml, and Solution A water 890 ml.

## Completeness

The schema-optional evidence, discussions, growth, and target organism fields are empty; those empty slots are not defects by themselves for this imported medium.

Consequential gaps:

- The recipe is structurally incomplete because the Solution A-G, trace-element, and Wolin 10x stock hierarchy has been collapsed to flat ingredients and empty solution stubs.
- The pH 5.7 final-medium condition, pH 7.5 Solution C adjustment, pH 7 trace-stock adjustment, N2/CO2 sparging, filtration versus autoclaving boundaries, solution-addition order, overnight equilibration, H2/CO2 pressurization, and instability/storage warning are not represented.
- The DSMZ 1094 PDF carries in-source variants for DSM 25616 and DSM 25820. A focused gitignore-independent search over `data/normalized_yaml`, `data/merge_yaml`, `src`, `scripts`, and `.claude` found `methanosphaerula_peat_medium_for_dsm_25616` but found no exact `DSM 25820` or `methanosphaerula_peat_medium_for_dsm_25820` record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The nested solution hierarchy was flattened and units were changed from milliliter or milligram recipe amounts to `G_PER_L` concentrations. | DSMZ 1094 and MediaDive 1094 keep a final medium of Solution A-G, Solution A contains three 0.1% stocks plus the trace stock, the trace stock contains dry salts, Solution D contains 1 ml Wolin vitamin stock, and Solutions E-G each have their own 10 ml water boundary. The generated record lifts those children to top-level ingredients or empty top-level solution stubs and assigns mass concentration units to source volumes. | `data/normalized_yaml/archaea/TOGO_M2655_Methanosphaerula_Peat_Medium.yaml`; likely also the TOGO importer and solution migrator. |
| Major | Cross-scope duplicate merging created a nonsensical 2940 g/L water row. | The row note says seven source water rows were merged: Solution A, trace element stock, Solution C, Wolin vitamin stock, and Solutions E-G. Those rows are distinct solvent volumes for distinct stocks, not duplicate final-medium water concentrations. | `data/normalized_yaml/archaea/TOGO_M2655_Methanosphaerula_Peat_Medium.yaml`; likely also the duplicate ingredient cleanup/merge logic. |
| Major | The MediaDive solution IDs attached to Solution A-G and the trace element stock point to the wrong MediaDive solution records. | MediaDive medium 1094 exposes solution IDs 2201, 2202, 2203, 2204, 2205, 2206, 2207, and 2208 for those exact stocks; the record stores 5342, 5343, 5312, 5313, 4959, 6293, 3625, and 6187. | `data/normalized_yaml/archaea/TOGO_M2655_Methanosphaerula_Peat_Medium.yaml`; likely also the MediaDive solution linker. |
| Major | Authoritative DSMZ quantities are not preserved. | The live DSMZ PDF and MediaDive REST record agree on 943 ml Solution A, 13 ml Solution B, 1 ml Solution D, and 900 ml water in Solution A, while the imported TOGO record stores 932.9 ml, 12.55 ml, 10 ml, and 890 ml. | TOGO M2655 import input and `data/normalized_yaml/archaea/TOGO_M2655_Methanosphaerula_Peat_Medium.yaml`; a future fix should preserve or resolve the TOGO-vs-DSMZ discrepancy explicitly. |
| Major | Preparation and pH details were dropped. | DSMZ 1094 specifies final pH 5.7, trace-stock pH 7, Solution C pH 7.5, anoxic N2/CO2 sparging, Hungate or serum-vial dispensing, different sterilization treatments for Solution A-G, overnight equilibration, 80% H2/20% CO2 overpressure after inoculation, and short stability. The record has only gas pseudo-ingredients and no ordered preparation or pH representation. | `data/normalized_yaml/archaea/TOGO_M2655_Methanosphaerula_Peat_Medium.yaml`; importer support for preparation comments. |
| Major | One DSMZ in-source variant is not represented. | The DSMZ 1094 PDF has separate notes for DSM 25616 and DSM 25820. A generated `methanosphaerula_peat_medium_for_dsm_25616` record exists, but an ignored-inclusive exact search found no DSM 25820 counterpart. | TOGO/DSMZ import tables and normalized YAML for the DSMZ 1094 family. |

## Recommended Edits

1. Recurate `data/normalized_yaml/archaea/TOGO_M2655_Methanosphaerula_Peat_Medium.yaml` from inspected DSMZ 1094 and TOGO M2655 source text, preserving the final-medium additions, Solution A-G, the trace element stock, and Wolin's vitamin solution as scoped solution records rather than flattened final-medium ingredients.
2. Replace the incorrect `mediadive.solution:*` links with the DSMZ 1094 solution identifiers, or leave them absent until the linker can choose solution IDs in the context of medium 1094.
3. Preserve the TOGO-vs-DSMZ differences as an explicit unresolved source conflict if TOGO remains the imported source of record; otherwise update the imported source quantities to the current DSMZ/MediaDive values.
4. Encode the pH, gas atmosphere, sterilization, equilibration, post-inoculation pressurization, and stability instructions as preparation or condition fields instead of gas-only ingredient placeholders.
5. Add or import a DSM 25820-specific variant if the current schema represents DSMZ in-source variants as sibling records.
6. Regenerate `data/merge_yaml/merged/methanosphaerula_peat_medium.yaml` after fixing the maintained input.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on `data/merge_yaml/merged/methanosphaerula_peat_medium.yaml`.
- Diff the regenerated YAML against DSMZ 1094 and TOGO M2655 and verify that every stock row remains within its correct parent solution.
- Recheck MediaDive medium 1094 and confirm that the linked solution IDs are 2201-2208 and 5980, or intentionally blank where a local solution should not link to MediaDive.
- Search ignored and generated files again for `DSM 25820` and `methanosphaerula_peat_medium_for_dsm_25820` after adding the variant.

## Additional Notes

- Empty optional evidence and discussion arrays were not treated as defects.
- The exact owner search used `rg --no-ignore --hidden` so ignored files were included when resolving `CultureMech:009210`, `Methanosphaerula (Peat) Medium`, and `methanosphaerula_peat_medium`.
