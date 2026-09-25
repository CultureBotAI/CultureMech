# YAML Record Review: defined_medium_for_sulfate_reducing_bacteria_with_butyrate

- Repository: `CultureBotAI/CultureMech`
- Record: `data/merge_yaml/merged/defined_medium_for_sulfate_reducing_bacteria_with_butyrate__4aab3777.yaml`
- Started UTC: 2026-09-22T16:38:20Z
- Finished UTC: 2026-09-22T16:39:39Z
- Verdict: needs curation

## Target

- Reviewed generated record: `data/merge_yaml/merged/defined_medium_for_sulfate_reducing_bacteria_with_butyrate__4aab3777.yaml`
- Class: `MediaRecipe`
- ID: `CultureMech:010140`
- Name / original name: `defined_medium_for_sulfate_reducing_bacteria_with_butyrate` / `Defined Medium For Sulfate-Reducing Bacteria With Butyrate`
- Source term: `TOGO:M731`, label `Defined Medium For Sulfate-Reducing Bacteria With Butyrate`
- Original source: `JCM_M708-2`, TOGO's solid-medium projection of JCM medium 708
- Maintained owner: `data/normalized_yaml/bacterial/TOGO_M731_Defined_Medium_For_Sulfate-Reducing_Bacteria_With_Butyrate.yaml`
- Merge provenance: `merge_recipes.py` merged one source, `TOGO_M731_Defined_Medium_For_Sulfate-Reducing_Bacteria_With_Butyrate.yaml`, on fingerprint `4aab3777f75683d71915b27c93d032166e289d6c8e3f3adf223a734675e22173`.
- Exact ignored-file-inclusive search for `CultureMech:010140`, `TOGO:M731`, `JCM_M708-2`, the TOGO M731 owner basename, and the merge fingerprint across `data/normalized_yaml/bacterial`, `data/merge_yaml/merged`, `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, and `reports/yaml_record_review` resolved this target to the maintained TOGO M731 owner and reviewed generated merge.

## Validation

| Check | Result |
|---|---|
| Open schema, equivalent to `just validate-schema data/merge_yaml/merged/defined_medium_for_sulfate_reducing_bacteria_with_butyrate__4aab3777.yaml` | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`. |
| Strict closed schema | Passed with `scripts/validate_strict.py`: one file scanned, zero files with errors, zero error rows. |
| Reference integrity | Passed with `linkml-reference-validator validate data ... --target-class MediaRecipe`; the validator reported zero checks. |
| Term labels | Passed with `linkml-term-validator validate-data ... --labels -c conf/oak_config.yaml`. |
| Embedded `curation_history` | Not checked separately: `just validate-history` targets standalone `history/*.yaml` records, not `MediaRecipe.curation_history` entries embedded in a medium YAML. The embedded event shape was still covered by schema and strict validation. |

## Identity and Grounding

- This record denotes the TOGO M731 solid-agar projection of JCM medium 708. TOGO M731 uses the JCM 708 source page and lifts JCM's optional `15.0 g/L agar (BD-Difco)` solid-medium instruction into the component list.
- `physical_state: SOLID_AGAR` and the `15 G_PER_L` agar row are supported for this M731 projection.
- `medium_type: COMPLEX` and `composition_type: UNDEFINED` are not supported by the inspected formulation. The JCM 708 components, TOGO M731 components, and JCM 187 cross-referenced stocks are chemically defined apart from the agar solidifier.
- Nitrogen and carbon dioxide are correctly grounded as chemicals, but they are mis-modeled as variable-concentration ingredients. JCM 708 uses them as a preparation atmosphere, specifically an `N2-CO2 (95:5, v/v)` gas mixture.

## Evidence

- JCM 708 and TOGO M731 support the solid recipe's base rows: `0.5 g` KH2PO4, `1.0 g` NH4Cl, `0.1 g` CaCl2.2H2O, `2.5 g` MgSO4.7H2O, `1.0 g` NaCl, `10.0 ml` FeCl2 solution from Medium 187, `10.0 ml` Trace element solution from Medium 187, `1.0 mg` Resazurin, `870.0 ml` distilled water, and `15.0 g/L` agar.
- JCM 708 and TOGO M731 support the after-autoclave additions per liter: `100.0 ml` 2.2% Sodium butyrate solution, `2.5 ml` filter-sterilized 8% NaHCO3 solution, and `10.0 ml` 5% L-Cysteine.H2O.HCl solution.
- JCM 187 and TOGO M180 support the two cross-referenced stock definitions:
  - FeCl2 solution: `10 ml` 25% HCl, `1.5 g` FeCl2.4H2O, and `990 ml` distilled water.
  - Trace element solution: `70 mg` ZnCl2, `100 mg` MnCl2.4H2O, `6 mg` H3BO3, `190 mg` CoCl2.6H2O, `2 mg` CuCl2.2H2O, `24 mg` NiCl2.6H2O, `36 mg` Na2MoO4.2H2O, and `1 L` distilled water.
- The YAML preserves the direct salts and agar, but changes several source dimensions:
  - `Resazurin` is `1 G_PER_L`, but the source value is `1 mg`.
  - `870 ml` distilled water is represented as `870 G_PER_L`; this is a preparation volume, not a final mass concentration.
  - Five solution additions are represented as `G_PER_L` instead of the source `ml` volumes.
- The YAML omits JCM 708 preparation claims that materially affect the formulation: adjust pH to 7.5 before dispensing, distribute under 95:5 N2-CO2, seal with butyl rubber stoppers, autoclave, anaerobically and aseptically add the three solutions, filter-sterilize the starred bicarbonate solution, and readjust pH to 7.5 if necessary.

## Completeness

- Consequential gaps:
  - The M187-derived FeCl2 and trace stocks have no structured stock composition or resolvable stock reference beyond a free-text `Cross-reference to Medium M180` note.
  - All five solution additions have source `ml` quantities but YAML `G_PER_L` units.
  - The record lacks pH 7.5 and the anaerobic preparation sequence.
  - N2 and CO2 are ingredients without the source 95:5 ratio or atmosphere role.
  - Resazurin has a 1000-fold unit slip from `mg` to `G_PER_L`.
- Empty optional slots correctly left empty:
  - No `target_organisms` or growth evidence should be filled from the inspected JCM 708, TOGO M731, or JCM 187 formulation pages.
- Bounded searches:
  - Ignored-file-inclusive exact search for `CultureMech:010140`, `TOGO:M731`, `JCM_M708-2`, and the merge fingerprint under `reports/yaml_record_review` found no existing review report for this generated file.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Five solution additions have the wrong unit family. | JCM 708 and TOGO M731 list FeCl2 solution `10 ml`, Trace element solution `10 ml`, 8% NaHCO3 `2.5 ml`, 2.2% Sodium butyrate `100 ml`, and 5% L-Cysteine.H2O.HCl `10 ml`; the YAML stores all five as `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M731_Defined_Medium_For_Sulfate-Reducing_Bacteria_With_Butyrate.yaml` and the TOGO solution migrator. |
| Major | Resazurin is inflated from milligrams to grams. | JCM 708 lists `1.0 mg` Resazurin, but the YAML stores `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M731_Defined_Medium_For_Sulfate-Reducing_Bacteria_With_Butyrate.yaml` and the TOGO unit importer. |
| Major | Preparation conditions and pH are dropped. | The source requires pH 7.5 adjustment, 95:5 N2-CO2 dispensing, butyl rubber stopper sealing, autoclaving before the three final solutions, aseptic anaerobic addition, filter sterilization of the starred bicarbonate solution, and final pH readjustment if needed; none are modeled structurally. | `data/normalized_yaml/bacterial/TOGO_M731_Defined_Medium_For_Sulfate-Reducing_Bacteria_With_Butyrate.yaml`. |
| Major | The M187 FeCl2 and trace stocks are unresolved. | JCM 708 references stocks from JCM 187. TOGO maps them through M180/JCM 187, but the YAML keeps empty `composition: []` rows with only free-text M180 notes, so the cross-reference is not machine-resolvable. | `data/normalized_yaml/bacterial/TOGO_M731_Defined_Medium_For_Sulfate-Reducing_Bacteria_With_Butyrate.yaml` and the TOGO cross-reference resolver. |
| Major | The medium is classified as complex/undefined despite a defined source formulation. | JCM 708's solid variant adds agar to a chemically defined butyrate formulation. Neither the base salts nor the cross-referenced M187 stocks support `COMPLEX` or `UNDEFINED`. | `data/normalized_yaml/bacterial/TOGO_M731_Defined_Medium_For_Sulfate-Reducing_Bacteria_With_Butyrate.yaml`. |
| Minor | The import event conflates TOGO and JCM accessions. | The top-level notes and TOGO API identify original source `JCM_M708-2`, but the `togo-import` event says `Source: JCM, ID: M731`; `M731` is the TOGO accession. | `data/normalized_yaml/bacterial/TOGO_M731_Defined_Medium_For_Sulfate-Reducing_Bacteria_With_Butyrate.yaml`. |

## Recommended Edits

1. Change all five `solutions` additions from `G_PER_L` to the source milliliter additions and preserve which ones belong to the pre-autoclave base versus anaerobic post-autoclave additions.
2. Correct `Resazurin` from `1 G_PER_L` to `1 mg` per liter, or the closest schema-supported representation that cannot be mistaken for 1 gram.
3. Add structured preparation and condition claims for pH 7.5, 95:5 N2-CO2 dispensing, butyl stopper sealing, autoclaving, anaerobic aseptic post-addition, filter sterilization of 8% NaHCO3, and final pH readjustment.
4. Resolve the two M180/JCM 187 cross-referenced stocks by linking to reviewed source-local FeCl2 and trace solution recipes or by embedding source-supported compositions with their JCM 187 provenance.
5. Reclassify the record as defined rather than complex/undefined while keeping `physical_state: SOLID_AGAR` and `15 G_PER_L` agar.
6. Add a curation history event that describes the unit, stock-reference, pH, and atmosphere repair without rewriting the older import events.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/bacterial/TOGO_M731_Defined_Medium_For_Sulfate-Reducing_Bacteria_With_Butyrate.yaml`, `just validate-strict data/normalized_yaml/bacterial/TOGO_M731_Defined_Medium_For_Sulfate-Reducing_Bacteria_With_Butyrate.yaml`, `just validate-terms data/normalized_yaml/bacterial/TOGO_M731_Defined_Medium_For_Sulfate-Reducing_Bacteria_With_Butyrate.yaml`, and `just validate-references data/normalized_yaml/bacterial/TOGO_M731_Defined_Medium_For_Sulfate-Reducing_Bacteria_With_Butyrate.yaml`.
- Regenerate merges, then run the merge freshness check to prove the generated M731 record reflects the normalized repair.
- Manually compare the regenerated record against TOGO M731, JCM 708, and JCM 187: the M731 base table should retain 15 g/L agar, 870 ml water, and 1 mg Resazurin; all five solution additions should be in milliliters; the FeCl2 and trace stock references should resolve; and the N2-CO2 condition should retain the 95:5 ratio.

## Additional Notes

- TOGO's `Medium [M180]` cross-reference is not necessarily wrong even though the JCM 708 page links to `GRMD=187`; TOGO M180 declares `original_media_id: JCM_M187`.
- This report did not edit any YAML record or append a curation event.
