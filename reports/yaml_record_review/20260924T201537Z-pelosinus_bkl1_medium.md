# YAML Record Review: pelosinus_bkl1_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/pelosinus_bkl1_medium.yaml`
- Started UTC: 2026-09-24T20:15:37Z
- Finished UTC: 2026-09-24T20:15:37Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pelosinus_bkl1_medium.yaml`, a generated `MediaRecipe` merge record.

- ID: `CultureMech:015835`
- Label: `pelosinus_bkl1_medium`
- Category: `bacterial`
- Source term: `jcm.grmd:1351`
- Source name: JCM Medium 1351, PELOSINUS BKL1 MEDIUM
- Physical state: `LIQUID`
- Maintained owner: `data/normalized_yaml/bacterial/JCM_J1351_PELOSINUS_BKL1_MEDIUM.yaml`
- Generated from: `JCM_J1351_PELOSINUS_BKL1_MEDIUM`

## Validation

- Passed: open LinkML validation of `data/merge_yaml/merged/pelosinus_bkl1_medium.yaml` against `src/culturemech/schema/culturemech.yaml` as `MediaRecipe`; no issues found.
- Passed: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pelosinus_bkl1_medium.yaml --out /private/tmp/pelosinus_bkl1_medium.strict.tsv --workers 1 --quiet`; the TSV contained only its header, so strict validation found 0 errors.
- Passed: focused `linkml-reference-validator validate data data/merge_yaml/merged/pelosinus_bkl1_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; 0 references were checked.
- Passed: focused `linkml-term-validator validate-data data/merge_yaml/merged/pelosinus_bkl1_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`.
- Not checked: embedded `curation_history`; the documented `just validate-history` target validates standalone `history/` YAML rather than `MediaRecipe.curation_history` embedded in generated records.

## Identity and Grounding

`jcm.grmd:1351` resolves to JCM Medium 1351, PELOSINUS BKL1 MEDIUM. The source supports the record's bacterial category, liquid physical state, pH 7.2 starting adjustment, and pH 7.0 to 7.2 final readjustment range.

The generated record preserves the JCM 1351 final-medium ingredient amounts, including 925 ml Distilled water, 30 ml 8.0 percent NaHCO3 solution, 30 ml 1.0 M Sodium lactate solution, and 5 ml 5 percent L-Cysteine HCl H2O solution. It also preserves the 1 ml FeCl2 solution, 1 ml Trace element solution, and 10 ml Trace vitamins additions, but those three named stocks remain opaque top-level ingredients instead of `solutions` with the child recipes supplied by JCM 187 and JCM 197.

## Evidence

- JCM 1351 lists NaCl, MgCl2 x 6 H2O, NaH2PO4 x 2 H2O, CaCl2 x 2 H2O, NH4Cl, Yeast extract, 1 ml FeCl2 solution, 1 ml Trace element solution, and 925 ml Distilled water before autoclaving.
- JCM 1351 lists 30 ml 8.0 percent NaHCO3 solution, 10 ml Trace vitamins, 30 ml 1.0 M Sodium lactate solution, and 5 ml 5 percent L-Cysteine HCl H2O solution as aseptic anaerobic additions.
- JCM 187 defines both the FeCl2 solution and the Trace element solution referenced by JCM 1351.
- JCM 197 defines the Trace vitamins stock referenced by JCM 1351.

## Completeness

The direct JCM 1351 final recipe is complete at the level of the scraped source table. The unresolved gap is nested stock completeness: cross-references to Medium 187 and Medium 197 should not stay as opaque ungrounded ingredient labels once the referenced stock recipes can be inspected.

The generated record is also stale relative to the maintained owner because the owner gained a September exact mapping for `Yeast extract (BD-Difco)` to `FOODON:03315426`, but this generated copy was last emitted on 2026-08-06 and still leaves the yeast extract ungrounded.

Empty optional fields are not defects.

An ignored-inclusive exact search of `data`, `src`, and `scripts` for `jcm.grmd:1351`, `CultureMech:015835`, `GRMD=1351`, and `JCM_J1351_PELOSINUS_BKL1_MEDIUM` found only this maintained owner, this generated record, index rows, import diagnostics for its ungrounded solution names, and the September exact-extract repair script.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Three referenced stock solutions remain unresolved as opaque top-level ingredients. | JCM 1351 imports 1 ml FeCl2 solution and 1 ml Trace element solution from Medium 187 and 10 ml Trace vitamins from Medium 197. JCM 187 and JCM 197 expose those child stock recipes, but the record has no `solutions` block and leaves the three additions as ungrounded `ingredients`. | `data/normalized_yaml/bacterial/JCM_J1351_PELOSINUS_BKL1_MEDIUM.yaml` |
| Minor | The generated record is stale relative to the exact yeast-extract grounding repair. | The maintained owner now grounds `Yeast extract (BD-Difco)` to `FOODON:03315426`, while the generated record emitted on 2026-08-06 does not. | `data/normalized_yaml/bacterial/JCM_J1351_PELOSINUS_BKL1_MEDIUM.yaml`, already repaired for the yeast extract row. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/JCM_J1351_PELOSINUS_BKL1_MEDIUM.yaml`, represent `FeCl2 solution`, `Trace element solution`, and `Trace vitamins` as volumetric `solutions`, with child compositions sourced narrowly from JCM 187 and JCM 197.
2. Preserve 8.0 percent NaHCO3 solution, 1.0 M Sodium lactate solution, and 5 percent L-Cysteine HCl H2O solution as aseptic post-autoclave additions unless a maintained stock recipe for those simple stocks is added.
3. Regenerate `data/merge_yaml/merged/pelosinus_bkl1_medium.yaml` after curation so the generated record picks up the solution nesting and the already repaired yeast-extract grounding.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on `data/normalized_yaml/bacterial/JCM_J1351_PELOSINUS_BKL1_MEDIUM.yaml`, then regenerate `data/merge_yaml/merged/pelosinus_bkl1_medium.yaml` and rerun the same focused validators on the generated record.
- Manually compare the regenerated record against JCM 1351, JCM 187, and JCM 197 to confirm only the FeCl2, Trace element, and Trace vitamins subrecipes were imported from the referenced media.

## Additional Notes

The local `data/import_tracking/reports/composition_type_semi_defined.tsv` row already flags the opaque solution names in this maintained owner as needing curation or an explicit undefined decision.
