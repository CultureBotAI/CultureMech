# YAML Record Review: geothermobacter_medium__23e4cbc2

- Repository: CultureMech
- Record: data/merge_yaml/merged/geothermobacter_medium__23e4cbc2.yaml
- Started UTC: 2026-09-23T06:03:03Z
- Finished UTC: 2026-09-23T06:05:34Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:007810` is the Togo import for Togo M1277, `Geothermobacter Medium`, whose original source is JCM 1192.

The generated record derives from `data/normalized_yaml/bacterial/TOGO_M1277_Geothermobacter_Medium.yaml`. An ignored-file-inclusive exact search found the sibling direct MediaDive/JCM import in `data/normalized_yaml/bacterial/JCM_J1192_GEOTHERMOBACTER_MEDIUM.yaml` and `data/merge_yaml/merged/GEOTHERMOBACTER_MEDIUM.yaml`; future deduplication needs both normalized inputs aligned.

## Validation

`linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/geothermobacter_medium__23e4cbc2.yaml` passed.

`scripts/validate_strict.py data/merge_yaml/merged/geothermobacter_medium__23e4cbc2.yaml --workers 1 --quiet` passed with 0 error rows.

`linkml-reference-validator validate data data/merge_yaml/merged/geothermobacter_medium__23e4cbc2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` passed with 0 checks.

`linkml-term-validator validate-data data/merge_yaml/merged/geothermobacter_medium__23e4cbc2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `TOGO:M1277` source identity, label, and JCM 1192 original URL agree with the live JCM 1192 `GEOTHERMOBACTER MEDIUM` page.

The record is split from the direct MediaDive `mediadive.medium:J1192` import. Both local source records point to the same current JCM 1192 formulation, but they now produce different generated records.

The basal salts are grounded to the expected CHEBI terms. The gas entries for carbon dioxide and hydrogen represent the H2-CO2 gas stream from the preparation instruction, not source table ingredients.

JCM 1192 is a defined medium in the direct MediaDive import, but the Togo branch is classified as `COMPLEX` and `UNDEFINED`.

## Evidence

JCM 1192 has five direct basal salts, three 1 ml pre-autoclave stock additions, and 840 ml distilled water in the first table.

After cooling, JCM 1192 adds four more solutions: 100 ml Iron(III) citrate solution from JCM 1014, 10 ml filter-sterilized Trace vitamins from JCM 197, 30 ml filter-sterilized 8% NaHCO3 solution, and 20 ml 0.1 M KH2PO4 solution.

The JCM 187, JCM 431, JCM 1014, and JCM 197 pages are reachable and contain the referenced FeCl2, Trace element, Selenite-tungstate, Iron(III) citrate, and Trace vitamins subrecipes.

Togo M1277 preserves the source volumes and reference medium IDs in separate components, but the normalized YAML migrates all seven stock rows to empty `solutions` entries with `G_PER_L` units.

## Completeness

All seven stock solutions are present only as empty `solutions` rows. The three 1 ml stocks are stored as `1 G_PER_L`; the 100 ml, 10 ml, 30 ml, and 20 ml post-cooling additions are stored as `100`, `10`, `30`, and `20 G_PER_L`.

The H2-CO2 4:1 gas stream, butyl stopper, autoclaving, cooling, and aseptic anaerobic post-addition instructions are absent from the normalized and generated Togo record.

The record has no `ph_value`; JCM 1192 also does not state a pH for this medium, so that absence is acceptable.

Empty growth-evidence, variant, discussion, and publication slots are acceptable for this imported source recipe.

## Findings

- Major: The seven JCM stock additions were migrated to empty `solutions` rows with source milliliter amounts recoded as `G_PER_L`. The normalized owner is `data/normalized_yaml/bacterial/TOGO_M1277_Geothermobacter_Medium.yaml`.
- Major: The Togo branch drops the JCM preparation sentence describing the H2-CO2 4:1 gas stream, butyl-stopper sealing, autoclaving, cooling, and aseptic anaerobic addition of filtered/autoclaved stocks.
- Major: The current generated Togo record remains split from the equivalent direct MediaDive J1192 generated record.
- Minor: The hydrogen and carbon dioxide gas stream is encoded as variable ingredients instead of atmosphere context.
- Minor: The Togo branch is classified as `COMPLEX` and `UNDEFINED`, while the source and direct MediaDive branch support a defined formulation.

## Recommended Edits

- Preserve the 1 ml FeCl2 solution, 1 ml Trace element solution, 1 ml Selenite-tungstate solution, 100 ml Iron(III) citrate solution, 10 ml Trace vitamins, 30 ml 8% NaHCO3 solution, and 20 ml 0.1 M KH2PO4 solution as solution additions with milliliter units.
- Populate or cross-link the referenced subrecipes from the live JCM stock pages: 187, 431, 1014, and 197.
- Restore the JCM 1192 preparation instruction in the Togo normalized row and keep the H2-CO2 stream as atmosphere context rather than variable gas ingredients.
- Reclassify the Togo row as a defined medium if no undefined component remains after stock expansion.
- Align `TOGO_M1277_Geothermobacter_Medium.yaml` and `JCM_J1192_GEOTHERMOBACTER_MEDIUM.yaml` so regeneration merges or explicitly cross-links the two imports.

## Follow-up Checks

- Regenerate the merged Geothermobacter records and confirm no stock addition has a 1, 10, 20, 30, or 100 `G_PER_L` concentration copied from a milliliter source amount.
- Confirm all seven stock additions either have populated subrecipes or resolvable cross-references to JCM 187, JCM 431, JCM 1014, and JCM 197.
- Re-run LinkML, strict, reference, and term validation on the regenerated generated YAML.
- Re-run an ignored-file-inclusive exact search for `TOGO:M1277`, `mediadive.medium:J1192`, `JCM_M1192`, and `GRMD=1192` to confirm the same JCM recipe no longer publishes as split equivalent generated records.

## Additional Notes

The exact source-ID search used `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged`, so ignored generated records and index files were included.
