# YAML Record Review: SULFURIMONAS JS MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/sulfurimonas_js_medium__93c986f9.yaml
- Started UTC: 2026-09-25T08:37:27Z
- Finished UTC: 2026-09-25T08:39:01Z
- Verdict: needs curation

## Target

- Reviewed generated record `CultureMech:002291` in `data/merge_yaml/merged/sulfurimonas_js_medium__93c986f9.yaml`.
- Source: `data/normalized_yaml/bacterial/sulfurimonas_js_medium.yaml`.
- Media term: `mediadive.medium:J1118`, `JCM Medium J1118`, `SULFURIMONAS JS MEDIUM`.
- Merge fingerprint: `93c986f9336e81e827ca51858a608a1ab466e73e652d6c2e539a7c8ebce3e46c`.

## Validation

- LinkML schema validation passed: `No issues found`.
- Strict validation passed with 0 error rows.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

- The generated identity matches MediaDive/JCM medium `J1118`, `SULFURIMONAS JS MEDIUM`, with pH 6.5.
- Exact ignored-file-inclusive searches found `CultureMech:002291`, `mediadive.medium:J1118`, `source: sulfurimonas_js_medium.yaml`, and the `93c986f9336e81e827ca51858a608a1ab466e73e652d6c2e539a7c8ebce3e46c` fingerprint in the generated record and normalized MediaDive source at expected locations.
- JCM 1118 confirms the same base recipe, post-autoclave NaHCO3 and Na2S2O3 additions, vitamin mixture, metal mixture, and artificial seawater recipe.

## Evidence

- MediaDive J1118 represents the main solution as NH4NO3, KH2PO4, Fe(III)-EDTA, 2.5 ml Vitamin mixture, 1 ml Metal mixture, PIPES, 1000 ml Artificial seawater, 10 ml 8% NaHCO3, and 10 ml 1 M Na2S2O3 in a 1024 ml final recipe.
- JCM 1118 directs mixing the base components, pH adjustment to 6.5 with NaOH, distribution into sealed culture vessels, autoclaving at 110C for 5 min, and post-cooling addition of the filter-sterilized 8% NaHCO3 and 1 M Na2S2O3 solutions per liter.
- MediaDive/JCM define the Vitamin mixture as a 1 L stock containing 1.1 mg Vitamin B12, 1 mg Biotin, and 200 mg Thiamine HCl, added at 2.5 ml.
- MediaDive/JCM define the Metal mixture as a 1 L stock containing EDTA, CuSO4 x 5 H2O, ZnSO4 x 7 H2O, MnCl2 x 6 H2O, CoCl2 x 6 H2O, and ammonium molybdate tetrahydrate, added at 1 ml.
- Artificial seawater is a separate 1 L stock and is the major liquid component of the final recipe.

## Completeness

- The generated record preserves the JCM identity, pH value, defined/liquid classification, base NH4NO3, KH2PO4, Fe(III)-EDTA, PIPES amounts scaled to the 1024 ml final volume, the seawater salts, and the two source preparation comments.
- The generated record does not preserve the Vitamin mixture, Metal mixture, or Artificial seawater as subrecipes or additions.
- The two post-autoclave 10 ml additions are not represented as 8% NaHCO3 and 1 M Na2S2O3 filter-sterilized liquid additions.

## Findings

- Several nested stocks are flattened at stock strength. The record stores the Vitamin mixture, Metal mixture, and Artificial seawater components as if they were all final medium ingredients, although the source adds only 2.5 ml of vitamin stock and 1 ml of metal stock to a 1024 ml recipe.
- The NaHCO3 and Na2S2O3 rows are unit-corrupted. MediaDive/JCM specify 10 ml of 8% NaHCO3 and 10 ml of 1 M Na2S2O3 added after cooling; the generated YAML records both as `10` `G_PER_L`.
- The preparation step says to add `the following solutions (filter-sterilized)` after cooling, but the generated model has no solution rows or additions corresponding to the following NaHCO3 and Na2S2O3 solutions.
- The Artificial seawater note is imported with replacement-character mojibake in the pore-size text inherited from MediaDive.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/sulfurimonas_js_medium.yaml` or the MediaDive import path so Vitamin mixture, Metal mixture, and Artificial seawater remain separate stock recipes with their addition volumes.
- Preserve the 8% NaHCO3 and 1 M Na2S2O3 post-autoclave additions as volumetric additions, not `G_PER_L` concentration rows.
- Keep the post-cooling filter-sterilized additions linked to the corresponding NaHCO3 and Na2S2O3 solution records.
- Repair the imported pore-size text only from a source-backed JCM value; the current MediaDive text is already corrupted.
- Regenerate `data/merge_yaml/merged/sulfurimonas_js_medium__93c986f9.yaml`; do not hand-edit this generated file.

## Follow-up Checks

- Revalidate the normalized MediaDive J1118 source after nested-stock and liquid-addition fixes.
- Regenerate merged YAML and verify that vitamin and metal stock components are no longer present at full stock strength in the final ingredient list.
- Verify the artificial-seawater replacement note against the upstream JCM page after any text-decoding repair.

## Additional Notes

- Empty optional fields were not treated as defects.
- JCM 1118 was checked against MediaDive J1118 as the primary source link.
