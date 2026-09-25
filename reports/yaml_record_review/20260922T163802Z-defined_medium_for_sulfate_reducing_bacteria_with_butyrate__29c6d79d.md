# YAML Record Review: defined_medium_for_sulfate_reducing_bacteria_with_butyrate

- Repository: `CultureBotAI/CultureMech`
- Record: `data/merge_yaml/merged/defined_medium_for_sulfate_reducing_bacteria_with_butyrate__29c6d79d.yaml`
- Started UTC: 2026-09-22T16:36:20Z
- Finished UTC: 2026-09-22T16:37:59Z
- Verdict: needs curation

## Target

- Reviewed generated record: `data/merge_yaml/merged/defined_medium_for_sulfate_reducing_bacteria_with_butyrate__29c6d79d.yaml`
- Class: `MediaRecipe`
- ID: `CultureMech:003054`
- Name / original name: `defined_medium_for_sulfate_reducing_bacteria_with_butyrate` / `DEFINED MEDIUM FOR SULFATE-REDUCING BACTERIA WITH BUTYRATE`
- Source term: `mediadive.medium:J708`, label `DEFINED MEDIUM FOR SULFATE-REDUCING BACTERIA WITH BUTYRATE`
- Source URL: JCM medium 708
- Maintained owner: `data/normalized_yaml/bacterial/defined_medium_for_sulfate_reducing_bacteria_with_butyrate.yaml`
- Merge provenance: `merge_recipes.py` merged one source, `defined_medium_for_sulfate_reducing_bacteria_with_butyrate.yaml`, on fingerprint `29c6d79dab822fd6ca11f98c9557402b42dcc7c2632713fb255fc688d71603c0`.
- Exact ignored-file-inclusive search for `CultureMech:003054`, the fingerprint, `mediadive.medium:J708`, `GRMD=708`, and `defined_medium_for_sulfate_reducing_bacteria_with_butyrate` across `data/normalized_yaml/bacterial`, `data/merge_yaml/merged`, `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, and `reports/yaml_record_review` resolved this target to the maintained direct-JCM owner and the reviewed generated merge. The same search also found the TOGO M730 import of JCM 708 and a TOGO M731 `JCM_M708-2` variant; neither shares this record's ID or fingerprint.

## Validation

| Check | Result |
|---|---|
| Open schema, equivalent to `just validate-schema data/merge_yaml/merged/defined_medium_for_sulfate_reducing_bacteria_with_butyrate__29c6d79d.yaml` | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`. |
| Strict closed schema | Passed with `scripts/validate_strict.py`: one file scanned, zero files with errors, zero error rows. |
| Reference integrity | Passed with `linkml-reference-validator validate data ... --target-class MediaRecipe`; the validator reported zero checks. |
| Term labels | Passed with `linkml-term-validator validate-data ... --labels -c conf/oak_config.yaml`. |
| Embedded `curation_history` | Not checked separately: `just validate-history` targets standalone `history/*.yaml` records, not `MediaRecipe.curation_history` entries embedded in a medium YAML. The embedded event shape was still covered by schema and strict validation. |

## Identity and Grounding

- The record denotes JCM medium 708, `DEFINED MEDIUM FOR SULFATE-REDUCING BACTERIA WITH BUTYRATE`; the ID registry and recipe catalog point `CultureMech:003054` to the normalized owner reviewed here.
- This direct JCM 708 owner and `data/normalized_yaml/bacterial/TOGO_M730_Defined_Medium_For_Sulfate-Reducing_Bacteria_With_Butyrate.yaml` both represent the same JCM source formulation. They failed to merge because their importers represented stock additions differently, not because the source recipes differ.
- The record is correctly classified as defined, liquid medium at pH 7.5.
- `NiCl2 x 6 H2O` is grounded to `CHEBI:34887` / `nickel dichloride`, which collapses a hexahydrate source row to non-hydrated nickel chloride. The source and local ingredient label both require nickel chloride hexahydrate.

## Evidence

- JCM 708 directly supports the base recipe: `0.5 g` KH2PO4, `1.0 g` NH4Cl, `0.1 g` CaCl2.2H2O, `2.5 g` MgSO4.7H2O, `1.0 g` NaCl, `10.0 ml` FeCl2 solution from Medium 187, `10.0 ml` Trace element solution from Medium 187, `1.0 mg` Resazurin, and `870.0 ml` distilled water.
- JCM 708 directly supports the after-autoclave additions per liter: `100.0 ml` 2.2% Sodium butyrate solution, `2.5 ml` filter-sterilized 8% NaHCO3 solution, and `10.0 ml` 5% L-Cysteine.H2O.HCl solution.
- JCM 187 directly supports the two referenced stocks:
  - FeCl2 solution: `10 ml` 25% HCl, `1.5 g` FeCl2.4H2O, and `990 ml` distilled water.
  - Trace element solution: `70 mg` ZnCl2, `100 mg` MnCl2.4H2O, `6 mg` H3BO3, `190 mg` CoCl2.6H2O, `2 mg` CuCl2.2H2O, `24 mg` NiCl2.6H2O, `36 mg` Na2MoO4.2H2O, and `1 L` distilled water.
- The first six source rows are present and near the source amounts, though the imported values have been rescaled by about 0.2% instead of preserving JCM's printed grams and milligrams.
- All final stock additions are misrepresented:
  - `100 ml` of 2.2% Sodium butyrate solution is stored as `100 G_PER_L` sodium butyrate.
  - `2.5 ml` of 8% NaHCO3 solution is stored as `2.5 G_PER_L` NaHCO3.
  - `10 ml` of 5% L-Cysteine.H2O.HCl solution is stored as `10 G_PER_L` L-cysteine hydrochloride hydrate.
  - `10 ml` of FeCl2 stock from JCM 187 is stored as full-strength `2.5 G_PER_L` HCl and `1.5 G_PER_L` FeCl2.4H2O.
  - `10 ml` of the JCM 187 trace stock is stored as full-strength trace salts at the stock grams per liter.
- The preparation text preserves pH 7.5 and the anaerobic N2-CO2 autoclave/post-addition sequence, but it refers to "the following solutions" after those solutions have been flattened out of the record.

## Completeness

- Consequential gaps:
  - Five stock additions are absent as solutions and were replaced with incorrect final ingredient amounts.
  - The two Medium 187 stock recipes are not linked or nested; only their stock solutes survive as final ingredients.
  - The source-specific 8%, 2.2%, 5%, 25%, and trace-stock strengths are not represented, so the final concentration arithmetic is unrecoverable from the YAML.
  - The record duplicates the TOGO M730 import of the same JCM 708 source instead of merging with or being marked equivalent to it.
- Empty optional slots correctly left empty:
  - No `target_organisms` or growth evidence should be filled from the inspected JCM 708 formulation page.
  - The optional solid-medium agar line should not be promoted to a liquid-medium ingredient.
- Bounded searches:
  - Ignored-file-inclusive exact search for `CultureMech:003054`, the merge fingerprint, `mediadive.medium:J708`, and `GRMD=708` under `reports/yaml_record_review` found no existing review report for this generated file.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Milliliter stock additions were flattened to incorrect final grams per liter. | JCM 708 lists five solution additions in milliliters, but the YAML stores their solution volumes or stock concentrations as final `G_PER_L` simple ingredients. | `data/normalized_yaml/bacterial/defined_medium_for_sulfate_reducing_bacteria_with_butyrate.yaml` and the MediaDive/JCM stock-solution import transform. |
| Major | Medium 187 stock recipe boundaries are erased. | JCM 708 references FeCl2 and trace solutions from JCM 187. JCM 187 prints each stock's recipe, but this record has no `solutions` rows and stores JCM 187 HCl, FeCl2, and trace salts as final-medium solutes. | `data/normalized_yaml/bacterial/defined_medium_for_sulfate_reducing_bacteria_with_butyrate.yaml` and the MediaDive/JCM cross-reference resolver. |
| Major | The direct JCM and TOGO imports of the same source are duplicate canonical records. | This record and the TOGO M730 record both cite JCM 708 and have the same printed formulation; only importer-specific unit and stock modeling prevented fingerprint merging. | `data/normalized_yaml/bacterial/defined_medium_for_sulfate_reducing_bacteria_with_butyrate.yaml`, `data/normalized_yaml/bacterial/TOGO_M730_Defined_Medium_For_Sulfate-Reducing_Bacteria_With_Butyrate.yaml`, and merge duplicate rules. |
| Major | Nickel chloride hexahydrate has the wrong ontology grounding. | The source row is NiCl2.6H2O and the local label says `NiCl2 x 6 H2O`, but both `term` and `mediaingredientmech_chebi_term` point to `CHEBI:34887` / `nickel dichloride`. | `data/normalized_yaml/bacterial/defined_medium_for_sulfate_reducing_bacteria_with_butyrate.yaml`; if automated MIM matching is reused, repair the hydrate synonym conflict in the packaged MIM snapshot or resolver. |
| Minor | Printed JCM amounts were slightly rescaled. | JCM 708 lists 0.5, 1.0, 0.1, 2.5, and 1.0 g for the base salts, but the YAML stores 0.499002, 0.998004, 0.0998004, 2.49501, and 0.998004 g/L. | `data/normalized_yaml/bacterial/defined_medium_for_sulfate_reducing_bacteria_with_butyrate.yaml` and the MediaDive/JCM unit normalizer. |
| Minor | An optional solid-medium note is modeled as a required mixing step. | JCM says "For preparation of solid medium, add 15.0 g/L agar"; this liquid record stores the line as `step_number: 3`, `action: MIX`, making an optional variant read like part of the base protocol. | `data/normalized_yaml/bacterial/defined_medium_for_sulfate_reducing_bacteria_with_butyrate.yaml`. |

## Recommended Edits

1. Replace the flattened sodium butyrate, NaHCO3, L-cysteine, HCl, FeCl2, and trace-salt rows with five explicit solution additions: 10 ml/L FeCl2 solution, 10 ml/L Trace element solution, 100 ml/L 2.2% Sodium butyrate, 2.5 ml/L 8% NaHCO3, and 10 ml/L 5% L-Cysteine.H2O.HCl.
2. Link or nest the JCM 187 FeCl2 and trace stock recipes without changing their stock concentrations into final-medium grams per liter.
3. Preserve the source post-autoclave preparation boundary and mark the 8% NaHCO3 addition as the filter-sterilized starred solution.
4. Reground `NiCl2 x 6 H2O` to nickel chloride hexahydrate instead of nickel dichloride.
5. Resolve the source duplicate with the TOGO M730 normalized record after both import paths preserve the same stock structure and units.
6. Move the optional 15 g/L agar solidification instruction to a variant or optional note that cannot be read as a required liquid-medium step.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/bacterial/defined_medium_for_sulfate_reducing_bacteria_with_butyrate.yaml`, `just validate-strict data/normalized_yaml/bacterial/defined_medium_for_sulfate_reducing_bacteria_with_butyrate.yaml`, `just validate-terms data/normalized_yaml/bacterial/defined_medium_for_sulfate_reducing_bacteria_with_butyrate.yaml`, and `just validate-references data/normalized_yaml/bacterial/defined_medium_for_sulfate_reducing_bacteria_with_butyrate.yaml`.
- Regenerate merges, then run the merge freshness and duplicate checks to prove the repaired direct-JCM and TOGO M730 records no longer diverge solely because of importer artifacts.
- Manually compare against JCM 708 and JCM 187: five source additions should be solutions, no JCM 187 stock solute should be present as a final ingredient, and NiCl2.6H2O should remain hydrate-specific.

## Additional Notes

- The pH and N2-CO2 preparation text are more complete here than in the TOGO M730 record, so a future duplicate repair should not discard this preparation context.
- This report did not edit any YAML record or append a curation event.
