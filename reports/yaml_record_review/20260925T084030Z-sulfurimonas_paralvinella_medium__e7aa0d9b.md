# YAML Record Review: SULFURIMONAS PARALVINELLA MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/sulfurimonas_paralvinella_medium__e7aa0d9b.yaml
- Started UTC: 2026-09-25T08:39:02Z
- Finished UTC: 2026-09-25T08:40:30Z
- Verdict: needs curation

## Target

- Reviewed generated record `CultureMech:000481` in `data/merge_yaml/merged/sulfurimonas_paralvinella_medium__e7aa0d9b.yaml`.
- Source: `data/normalized_yaml/bacterial/sulfurimonas_paralvinella_medium.yaml`.
- Media term: `mediadive.medium:1053`, `DSMZ Medium 1053`, `SULFURIMONAS PARALVINELLA MEDIUM`.
- Merge fingerprint: `e7aa0d9b9ca802040a8f1234f72f80b8875e649b4bfee3bca9e3be5694fcc5b3`.

## Validation

- LinkML schema validation passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation passed with 0 error rows.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

- The generated identity matches MediaDive/DSMZ medium `1053`, `SULFURIMONAS PARALVINELLA MEDIUM`.
- Exact ignored-file-inclusive searches found `CultureMech:000481`, `mediadive.medium:1053`, `source: sulfurimonas_paralvinella_medium.yaml`, and the `e7aa0d9b9ca802040a8f1234f72f80b8875e649b4bfee3bca9e3be5694fcc5b3` fingerprint in the generated record and normalized MediaDive source at expected locations.
- The DSMZ `DSMZ_Medium1053.pdf` recipe agrees with MediaDive 1053 on the base chemicals, 10 ml Modified Wolin's mineral solution, 1 ml Wolin's vitamin solution (10x), bicarbonate/vitamin post-autoclave addition, and modified Wolin stock composition.

## Evidence

- DSMZ/MediaDive 1053 represent the main recipe as a 1011 ml solution with 1000 ml water, 10 ml Modified Wolin's mineral solution, 1 ml Wolin's vitamin solution (10x), 0.5 ml of 0.1% sodium resazurin, and main-medium salts.
- The source adds sulfur before autoclaving and adds vitamins and bicarbonate from sterile anoxic stock solutions after autoclaving.
- Modified Wolin's mineral solution is a 1 L stock; only 10 ml is added to the main recipe.
- Wolin's vitamin solution (10x) is a 1 L stock; only 1 ml is added to the main recipe.
- DSMZ distinguishes the pre-autoclave pH adjustment to 6.8 from the complete-medium pH adjustment to 6.5.

## Completeness

- The generated record preserves the DSMZ 1053 identity, main defined ingredients, sulfur/resazurin/bicarbonate additions, modified Wolin stock components, Wolin vitamin components, and source preparation text.
- The generated record does not preserve Modified Wolin's mineral solution or Wolin's vitamin solution as stock recipes with 10 ml and 1 ml addition rates.
- The generated `ph_value: 6.8` captures the first pH adjustment, but the complete medium is adjusted to pH 6.5 after vitamins and bicarbonate are added.

## Findings

- Modified Wolin's mineral solution was flattened at full stock strength. Its Nitrilotriacetic acid, MgSO4 x 7 H2O, MnSO4 x H2O, NaCl, FeSO4 x 7 H2O, trace sulfates, and selenite/tungstate rows should be retained in a stock solution that is added at 10 ml per 1011 ml.
- Wolin's vitamin solution (10x) was flattened at full stock strength. The generated vitamin concentrations are the 1 L vitamin-stock values even though the source adds only 1 ml stock per 1011 ml main recipe.
- Duplicate ingredient cleanup summed rows across unrelated contexts. The generated `NaCl` value adds the main medium's 19.7824 g/L to the 1 g/L concentration inside Modified Wolin's mineral solution, and `MgSO4 x 7 H2O` similarly adds the main medium's 3.95648 g/L to the mineral-stock 3 g/L value.
- The record exposes an intermediate pH as the top-level `ph_value`; the source's last pH instruction adjusts the complete medium to 6.5.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/sulfurimonas_paralvinella_medium.yaml` or the MediaDive import path so Modified Wolin's mineral solution and Wolin's vitamin solution remain nested stock recipes with 10 ml and 1 ml addition volumes.
- Prevent duplicate cleanup from summing ingredients that share a name but belong to different stock-solution contexts.
- Preserve both pH adjustments and treat the post-vitamin/bicarbonate pH 6.5 as the final complete-medium pH.
- Regenerate `data/merge_yaml/merged/sulfurimonas_paralvinella_medium__e7aa0d9b.yaml`; do not hand-edit this generated file.

## Follow-up Checks

- Revalidate the normalized DSMZ 1053 source after stock-solution and pH fixes.
- Regenerate merged YAML and verify that `NaCl` and `MgSO4 x 7 H2O` are not cross-summed between the main recipe and Modified Wolin's mineral solution.
- Verify that Wolin vitamin components no longer appear as final-medium ingredients at full 10x stock concentration.

## Additional Notes

- Empty optional fields were not treated as defects.
- DSMZ PDF agreement with MediaDive 1053 was checked before judging source completeness.
