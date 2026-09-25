# YAML Record Review: capnocytophaga_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/capnocytophaga_medium__f2e19731.yaml
- Started UTC: 2026-09-22T03:37:10Z
- Finished UTC: 2026-09-22T03:37:10Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009846`, `capnocytophaga_medium`, class `MediaRecipe`.
- Merge lineage: one source recipe, `TOGO_M459_Capnocytophaga_Medium`, on fingerprint `f2e1973131c0c6966e069396d7d9aac24cbb3c0e63a310fe236b8cef007ca309`.
- Maintained owner: `data/normalized_yaml/bacterial/TOGO_M459_Capnocytophaga_Medium.yaml`.
- Claimed source identity: Togo Medium `M459`, imported from JCM Medium 459.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation exited successfully for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The generated merge and normalized owner are materially identical: the merge only appends its `MERGED_RECIPES` event, `merge_fingerprint`, and `merged_from`.
- The record denotes Togo Medium M459, `Capnocytophaga Medium`, which the Togo API identifies as an extraction from JCM Medium 459.
- Togo M459, JCM Medium 459, and MediaDive J459 describe the same formula: Trypticase peptone 17 g, Yeast extract 3 g, Glucose 3 g, NaCl 3 g, KNO3 3 g, Hemin 3 mg, and Distilled water 1 L.
- `Distilled water`, `NaCl`, `KNO3`, `Hemin`, `Glucose`, and `CO2` have source-compatible primary groundings, but `CO2` belongs to the incubation atmosphere rather than to the ingredient list.
- `Yeast extract (BD-Difco)` is a complex source ingredient and is reasonably left without a CHEBI grounding.
- `Trypticase peptone (BD-BBL)` is ungrounded despite a unique packaged MediaIngredientMech synonym mapping to `MICRO:0000175`.

## Evidence

- The JCM Medium 459 page lists Trypticase peptone 17 g, Yeast extract 3 g, Glucose 3 g, NaCl 3 g, KNO3 3 g, Hemin 3 mg, and Distilled water 1 L.
- The Togo M459 API reports `ph` 7.0 and preserves those same component amounts, plus source comments for pH adjustment, separate glucose autoclaving, and oxygen-free 5-10% CO2 incubation.
- MediaDive's J459 JSON preserves the same `Main sol. J459` recipe as `mediadive.solution:4206` with the same converted g/L values, the same 1000 ml main solution volume, and a structured `Distilled water` row.
- JCM's Medium 459 page states that, unless otherwise stated, media are sterilized by autoclaving at 121 C for 15 min.

## Completeness

- The generated record is missing `ph_value: 7.0` even though both the Togo metadata and JCM source declare the pH.
- The generated record is missing JCM's default autoclave condition and the medium-specific pH, separate-glucose, and oxygen-free incubation instructions.
- `Distilled water` is encoded as `1 G_PER_L`, which is a solid mass concentration, not the source 1 L solvent volume.
- `Hemin` is encoded as `3 G_PER_L`, but the source says 3 mg; MediaDive J459 correctly normalizes this row to `0.003 G_PER_L`.
- `CO2` is encoded as a variable ingredient, but the source mentions it only as a 5-10% incubation atmosphere component.
- KNO3 has a correct CHEBI primary `term`, but its `mediaingredientmech_term` is still a legacy `MediaIngredientMech:000170` object rather than the CHEBI-keyed mirror used on water, NaCl, Hemin, and Glucose.

## Findings

- Major: `Hemin` is off by a factor of 1000. JCM, Togo, and MediaDive all list 3 mg, but `data/normalized_yaml/bacterial/TOGO_M459_Capnocytophaga_Medium.yaml` stores `3 G_PER_L` instead of `0.003 G_PER_L`.
- Major: the water row uses the wrong unit. The source gives 1 L distilled water, while the normalized owner and generated merge store `1 G_PER_L`.
- Major: preparation metadata was imported by Togo but dropped from the CultureMech owner. The Togo API exposes pH adjustment, separate glucose autoclaving, and oxygen-free CO2 incubation; JCM also declares a 121 C, 15 min default autoclave rule, but the generated record has no `ph_value` and no `preparation_steps`.
- Minor: `CO2` should be represented in the incubation preparation step, not as a variable recipe ingredient.
- Minor: `Trypticase peptone (BD-BBL)` is ungrounded despite a unique packaged MediaIngredientMech synonym mapping to `MICRO:0000175`.
- Minor: KNO3 still carries a legacy `mediaingredientmech_term` even though its primary CHEBI grounding is correct.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M459_Capnocytophaga_Medium.yaml`, not the generated merge.
- Change `Hemin` from `3 G_PER_L` to `0.003 G_PER_L`, preserving the source 3 mg addition.
- Change `Distilled water` to a volume-based 1 L addition compatible with the source and other JCM/MediaDive J459 imports.
- Move `CO2` out of `ingredients` and into a preparation/incubation step that preserves the source phrase `oxygen-free atmosphere containing 5-10% CO2`.
- Add `ph_value: 7.0`, the Togo/JCM preparation comments, and the JCM default 121 C, 15 min autoclave condition as structured `preparation_steps`.
- Ground `Trypticase peptone (BD-BBL)` to `MICRO:0000175` if MICRO terms are accepted in ingredient rows; otherwise document why this exact packaged synonym mapping should remain unused.
- Replace KNO3's legacy `mediaingredientmech_term` with the CHEBI-keyed `mediaingredientmech_chebi_term` mirror.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against `data/normalized_yaml/bacterial/TOGO_M459_Capnocytophaga_Medium.yaml`.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/capnocytophaga_medium__f2e19731.yaml`.
- Inspect the regenerated merge to confirm it has `Hemin` at `0.003 G_PER_L`, volume-based water, pH 7.0, no recipe-row `CO2`, no legacy KNO3 MIM field, grounded Trypticase peptone, and the expected autoclave/incubation preparation steps.
- Re-check the Togo M459 API, JCM Medium 459 page, and MediaDive J459 JSON export to confirm the maintained owner still matches the source formula and comments.

## Additional Notes

- `rg --no-ignore --hidden -l` for `CultureMech:009846`, `TOGO:M459`, `TOGO_M459_Capnocytophaga_Medium`, and `capnocytophaga_medium__f2e19731` included ignored and hidden files; it found one active normalized owner, one generated merge, generated indexes/catalogs, archived validation reports, ingredient audit output, and unrelated downstream app/report artifacts, but no second active owner for Togo M459.
- `find . -iname '*capnocytophaga*'` also included ignored and hidden files and found expected active siblings for Togo M459, Togo M2175, JCM 459, DSMZ/MediaDive 340, KOMODO 340, KOMODO 340_7271, DSMZ/MediaDive 779, and KOMODO 779, plus their generated merges and existing review reports.
