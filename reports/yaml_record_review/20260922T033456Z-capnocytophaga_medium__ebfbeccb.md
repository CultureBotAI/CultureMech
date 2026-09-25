# YAML Record Review: capnocytophaga_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/capnocytophaga_medium__ebfbeccb.yaml
- Started UTC: 2026-09-22T03:34:56Z
- Finished UTC: 2026-09-22T03:34:56Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:008769`, `capnocytophaga_medium`, class `MediaRecipe`.
- Merge lineage: one source recipe, `TOGO_M2175_Capnocytophaga_Medium`, on fingerprint `ebfbeccbb6cb705c376b7ce03678dc251d31d858e7c2e03a884e2dc27450945f`.
- Maintained owner: `data/normalized_yaml/bacterial/TOGO_M2175_Capnocytophaga_Medium.yaml`.
- Claimed source identity: Togo Medium `M2175`, imported from DSMZ Medium 340.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The generated merge and normalized owner are materially identical: the merge only appends its `MERGED_RECIPES` event, `merge_fingerprint`, and `merged_from`.
- The record denotes Togo Medium M2175, `Capnocytophaga Medium`, which the Togo API identifies as an extraction from the DSMZ Medium 340 PDF.
- Togo M2175 and DSMZ Medium 340 describe the same formula: Trypticase 17 g, Yeast extract 3 g, Glucose 3 g, NaCl 3 g, KNO3 3 g, Haemin 3 mg, and Distilled water 1000 ml.
- `Distilled water`, `NaCl`, `KNO3`, `Haemin`, `Glucose`, and `CO2` have source-compatible primary groundings, but `CO2` belongs to the incubation atmosphere rather than to the ingredient list.
- `Trypticase (BBL)` is ungrounded because that parenthetical label was not present in the pinned MediaIngredientMech index. Its source label matches the Trypticase ingredient in DSMZ Medium 340, and the normalized DSMZ/MediaDive 340 records show an exact `Trypticase` mapping to `MICRO:0000175`.

## Evidence

- The Togo M2175 API reports `ph` 7.0 and lists `Distilled water` as 1000 ml, `Haemin` as 3 mg, the other five solutes with source-compatible gram quantities, and a `CO2` gas item parsed from the source text.
- The Togo M2175 API preserves two comments: `Adjust pH to 7.0.` and `Sterilize glucose separately. Incubate in oxygen-free, 5 - 10% CO2 containing atmosphere.`
- The DSMZ Medium 340 PDF linked by the Togo API agrees with those amounts and comments.
- MediaDive's Medium 340 JSON also preserves the same formula, the same two steps, and `Main sol. 340` as `mediadive.solution:653`.

## Completeness

- The generated record is missing `ph_value: 7.0` even though both the Togo metadata and DSMZ source declare the pH.
- The generated record is missing both Togo comments as structured `preparation_steps`.
- `Distilled water` is encoded as `1000 G_PER_L`, which is a solid mass concentration, not the source 1000 ml solvent volume.
- `Haemin` is encoded as `3 G_PER_L`, but the source says 3 mg; DSMZ/MediaDive 340 correctly normalize this row to `0.003 G_PER_L`.
- `CO2` is encoded as a variable ingredient, but the source mentions it only as a 5-10% incubation atmosphere component.
- KNO3 has a correct CHEBI primary `term`, but its `mediaingredientmech_term` is still a legacy `MediaIngredientMech:000170` object rather than the CHEBI-keyed mirror used on water, NaCl, Haemin, and Glucose.

## Findings

- Major: `Haemin` is off by a factor of 1000. Togo and DSMZ list 3 mg, but `data/normalized_yaml/bacterial/TOGO_M2175_Capnocytophaga_Medium.yaml` stores `3 G_PER_L` instead of `0.003 G_PER_L`.
- Major: the water row uses the wrong unit. The Togo source gives 1000 ml distilled water, while the normalized owner and generated merge store `1000 G_PER_L`.
- Major: DSMZ preparation text was imported by Togo but dropped from the CultureMech owner. The Togo API exposes the pH adjustment and the separate-glucose/oxygen-free incubation comment, but the generated record has no `preparation_steps` and no `ph_value`.
- Minor: `CO2` should be represented in the incubation preparation step, not as a variable recipe ingredient.
- Minor: KNO3 still carries a legacy `mediaingredientmech_term` even though its primary CHEBI grounding is correct.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M2175_Capnocytophaga_Medium.yaml`, not the generated merge.
- Change `Haemin` from `3 G_PER_L` to `0.003 G_PER_L`, preserving the source 3 mg addition.
- Change `Distilled water` to a volume-based 1000 ml addition compatible with other DSMZ/MediaDive Medium 340 imports.
- Move `CO2` out of `ingredients` and into a preparation/incubation step that preserves the source phrase `oxygen-free, 5 - 10% CO2 containing atmosphere`.
- Add `ph_value: 7.0` and the Togo/DSMZ preparation comments as structured `preparation_steps`.
- Normalize `Trypticase (BBL)` to the DSMZ/Togo label and ground it to `MICRO:0000175` if MICRO terms are accepted in ingredient rows.
- Replace KNO3's legacy `mediaingredientmech_term` with the CHEBI-keyed `mediaingredientmech_chebi_term` mirror.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against `data/normalized_yaml/bacterial/TOGO_M2175_Capnocytophaga_Medium.yaml`.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/capnocytophaga_medium__ebfbeccb.yaml`.
- Inspect the regenerated merge to confirm it has `Haemin` at `0.003 G_PER_L`, volume-based water, pH 7.0, no recipe-row `CO2`, no legacy KNO3 MIM field, and a structured oxygen-free CO2 incubation instruction.
- Re-check the Togo M2175 API and DSMZ Medium 340 PDF to confirm the maintained owner still matches the source formula and comments.

## Additional Notes

- `rg --no-ignore --hidden -l` for `CultureMech:008769`, `TOGO:M2175`, `TOGO_M2175_Capnocytophaga_Medium`, and `capnocytophaga_medium__ebfbeccb` included ignored and hidden files; it found one active normalized owner, one generated merge, generated indexes/catalogs, archived validation reports, ingredient audit output, and unrelated downstream app/report artifacts, but no second active owner for Togo M2175.
- `find . -iname '*capnocytophaga*'` also included ignored and hidden files and found expected active siblings for Togo M2175, Togo M459, JCM 459, DSMZ/MediaDive 340, KOMODO 340, KOMODO 340_7271, DSMZ/MediaDive 779, and KOMODO 779, plus their generated merges and existing review reports.
