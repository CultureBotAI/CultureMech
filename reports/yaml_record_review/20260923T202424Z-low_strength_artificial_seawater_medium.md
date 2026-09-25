# YAML Record Review: Low-Strength Artificial Seawater Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/low_strength_artificial_seawater_medium.yaml`
- Started UTC: `2026-09-23T20:23:05Z`
- Finished UTC: `2026-09-23T20:24:24Z`
- Verdict: needs curation

## Target

- `id`: `CultureMech:010131`
- `name`: `low_strength_artificial_seawater_medium`
- `original_name`: `Low-Strength Artificial Seawater Medium`
- `category`: `bacterial`
- `medium_type`: `COMPLEX`
- `composition_type`: `UNDEFINED`
- `physical_state`: `LIQUID`
- `media_term`: `TOGO:M723`
- `merge_fingerprint`: `32da60ad1abd01c28e97f5cc90c8b3a1f175248bab75385b1aa8fe9177d908fc`
- `merged_from`: `TOGO_M1022_Artificial_Seawater_Medium`, `TOGO_M723_Low-Strength_Artificial_Seawater_Medium`

## Validation

- Open schema validation passed with `linkml-validate`.
- Strict schema validation passed with 0 error rows written to `/private/tmp/low_strength_artificial_seawater_medium.strict.tsv`.
- LinkML reference validation passed with 0 checks.
- LinkML term validation passed.
- Embedded `curation_history` objects were not checked: the available history validator checks standalone `history/` files, not merged `MediaRecipe.curation_history` entries.

## Identity and Grounding

- An ignored-inclusive exact search for `CultureMech:010131`, `TOGO:M723`, `TOGO_M723_Low-Strength_Artificial_Seawater_Medium`, `TOGO_M1022_Artificial_Seawater_Medium`, `low_strength_artificial_seawater_medium`, and the merge fingerprint found the maintained low-strength owner, `data/normalized_yaml/bacterial/TOGO_M723_Low-Strength_Artificial_Seawater_Medium.yaml`, the maintained parent owner, `data/normalized_yaml/bacterial/TOGO_M1022_Artificial_Seawater_Medium.yaml`, this generated record, and a same-name `CultureMech:003047` / `mediadive.medium:J701` sibling.
- The generated record merged the TOGO M1022 parent and the TOGO M723 low-strength child on one fingerprint even though the maintained owners explicitly describe them as `CONCENTRATION_VARIANT` records.
- TOGO M723 identifies the reviewed source as `Low-Strength Artificial Seawater Medium`, original media ID `JCM_M701`, and JCM GRMD 701.
- TOGO M1022 identifies the parent as `Artificial Seawater Medium`, original media ID `JCM_M972`, and pH 7.5.
- MediaDive REST resolves JCM J701 as `LOW-STRENGTH ARTIFICIAL SEAWATER MEDIUM` with the same low-strength organic concentrations as TOGO M723.

## Evidence

- TOGO M723 lists 1 L distilled water, 0.1 g yeast extract, 24 g NaCl, 7 g `MgCl2 x 6 H2O`, 0.7 g KCl, and 0.5 g peptone.
- MediaDive J701 lists the same low-strength signature: 24 g NaCl, 0.7 g KCl, 7 g `MgCl2 x 6 H2O`, 0.1 g yeast extract, 0.5 g peptone, and 1000 ml distilled water in a 1000 ml main solution.
- TOGO M1022 lists the same salt base but 3 g yeast extract and 2.5 g peptone; its comment says to use Medium 701 with 3.0 g/L final yeast extract and 2.5 g/L final peptone, then adjust pH to 7.5.
- The generated record is identified as TOGO M723 but stores 3 g/L yeast extract and 2.5 g/L peptone from TOGO M1022.
- The generated `variant_modifications` entry correctly states that the low-strength child should decrease yeast extract from 3 g/L to 0.1 g/L and peptone from 2.5 g/L to 0.5 g/L, contradicting the merged ingredient list.

## Completeness

- The three seawater salt amounts match both M723 and M1022.
- The two organic nutrient amounts match the parent M1022, not the reviewed M723 child.
- The generated record's `media_term` and `original_name` point to the child M723 while `merged_from`, `synonyms`, and the ingredient concentrations combine the child with parent M1022.
- The source 1 L / 1000 ml distilled-water row is represented as 1 `G_PER_L`, which has the wrong dimension.
- A same-name JCM/MediaDive J701 active sibling exists for the same low-strength formulation and should be reconciled with the TOGO M723 record.

## Findings

1. The generated Low-Strength record uses parent organic nutrient concentrations.
   - Evidence: TOGO M723 and MediaDive J701 both list 0.1 g yeast extract and 0.5 g peptone; the generated TOGO M723 record stores 3 `G_PER_L` yeast extract and 2.5 `G_PER_L` peptone from TOGO M1022.
   - Impact: the generated record denotes the low-strength medium but would make the full-strength parent formulation.

2. The merge collapsed a parent and its concentration variant into one canonical recipe.
   - Evidence: the maintained TOGO owners relate M1022 and M723 as `CONCENTRATION_VARIANT`, while the generated record has `merged_from` entries for both owners and a synonym that makes `artificial_seawater_medium` an alias of the low-strength record.
   - Impact: users cannot retrieve the parent and child as separate formulations even though the source values differ materially.

3. The source solvent row has the wrong unit.
   - Evidence: TOGO M723 lists 1 L distilled water and MediaDive J701 lists 1000 ml distilled water; the generated row stores `Distilled water` as 1 `G_PER_L`.
   - Impact: water is represented as a mass concentration instead of the final solvent volume.

4. A second same-name low-strength JCM record is active.
   - Evidence: MediaDive J701 resolves the same JCM 701 low-strength formula, and `data/merge_yaml/merged/low_strength_artificial_seawater_medium__5cd782ae.yaml` is another generated record named `low_strength_artificial_seawater_medium`.
   - Impact: the generated corpus contains duplicate pages and IDs for the same JCM 701 formula.

## Recommended Edits

1. Fix merge logic so `TOGO_M1022_Artificial_Seawater_Medium.yaml` and `TOGO_M723_Low-Strength_Artificial_Seawater_Medium.yaml` stay separate generated records linked only by `CONCENTRATION_VARIANT`.
2. Rebuild `data/merge_yaml/merged/low_strength_artificial_seawater_medium.yaml` so it uses TOGO M723's 0.1 g/L yeast extract and 0.5 g/L peptone values.
3. Represent M723's 1 L distilled water as volume rather than 1 `G_PER_L`.
4. Reconcile the TOGO M723 `CultureMech:010131` record with the MediaDive J701 `CultureMech:003047` sibling before publishing regenerated outputs.

## Follow-up Checks

- Re-fetch TOGO M723, TOGO M1022, and MediaDive J701, then confirm the rebuilt M723 and M1022 generated records retain their distinct yeast extract, peptone, and pH values.
- Re-run open schema, strict schema, reference, and term validation on the rebuilt record.
- Run an ignored-inclusive exact search for `low_strength_artificial_seawater_medium`, `J701`, `JCM_M701`, and `TOGO:M723` after de-duplication to confirm the target is no longer represented by two active CultureMech records.

## Additional Notes

- Exact duplicate checks included ignored and hidden files via `rg --no-ignore --hidden` and were scoped to `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive`.
