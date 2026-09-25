# YAML Record Review: payne_seghal_gibbons_medium_add_agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/payne_seghal_gibbons_medium_add_agar.yaml
- Started UTC: 2026-09-24T19:51:47Z
- Finished UTC: 2026-09-24T19:51:47Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:008966 |
| Name | payne_seghal_gibbons_medium_add_agar |
| Original name | Payne, Seghal & Gibbons Medium (add agar) |
| Source identity | TOGO Medium M2381 |
| Source path | data/normalized_yaml/bacterial/payne_seghal_gibbons_medium_add_agar.yaml |
| Generated path | data/merge_yaml/merged/payne_seghal_gibbons_medium_add_agar.yaml |
| Merge fingerprint | 6c7d4a63e6917befd2d7c7ca8323d84b190ae2323f8fb63c6792f83a5a08cc05 |

The target is a generated merged record. Future edits should be made in the
maintained TOGO input or TOGO import logic, not directly in
`data/merge_yaml/merged/payne_seghal_gibbons_medium_add_agar.yaml`.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/payne_seghal_gibbons_medium_add_agar.yaml` exited 0 and reported no issues. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/payne_seghal_gibbons_medium_add_agar.yaml --out /private/tmp/payne_seghal_gibbons_medium_add_agar.strict.tsv --workers 1 --quiet` exited 0 and wrote only the TSV header. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/payne_seghal_gibbons_medium_add_agar.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` exited 0 with 0 checks. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/payne_seghal_gibbons_medium_add_agar.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` embedded in merged YAML. |

## Identity and Grounding

The `TOGO:M2381` medium grounding resolves to Payne, Seghal & Gibbons Medium
(add agar), which is the TOGO solid-agar projection from DSMZ Medium 1160.

Seven represented ingredients match TOGO M2381 and DSMZ 1160 at the right
gram-per-liter scale: 20 g/L MgSO4 x 7 H2O, 10 g/L yeast extract, 250 g/L NaCl,
2 g/L KCl, 3 g/L trisodium citrate, 20 g/L agar, and 7.5 g/L Casamino acids.

Three represented concentrations are unsupported:

| Ingredient | Source amount | Generated value |
| --- | --- | --- |
| Distilled water | 1000 ml | 1000 `G_PER_L` |
| MnCl2 x 4 H2O | 0.36 mg | 0.36 `G_PER_L` |
| FeCl2 x 4 H2O | 36 mg | 36 `G_PER_L` |

The primary MgSO4 x 7 H2O term is correctly `CHEBI:31795`, but its
`mediaingredientmech_chebi_term` still points at generic `CHEBI:32599`
magnesium sulfate.

## Evidence

The TOGO M2381 API and DSMZ 1160 PDF both support the add-agar identity, the 20
g agar row, 1000 ml distilled water, 36 mg FeCl2 x 4 H2O, 0.36 mg MnCl2 x 4
H2O, and the comment to adjust pH to 7.4 and add 20 g agar for solid medium.
The generated target lost the pH comment and mis-converted the two milligram
amounts as grams per liter.

The generated `payne_seghal_gibbons_medium__d891051e.yaml` sibling is TOGO
M2380, the liquid-base projection from the same DSMZ Medium 1160 PDF. M2380 and
M2381 are related liquid and add-agar variants, but this generated record has
no variant edge to M2380.

An ignored-inclusive PCRE2 search for `TOGO:M2381`, `M2381`, `Payne, Seghal &
Gibbons Medium (add agar)`, and `DSMZ_Medium1160.pdf` found exactly one
maintained TOGO M2381 input, this generated record, the related TOGO M2380
record, and the direct DSMZ/MediaDive DSMZ 1160 input. No second TOGO M2381
input was found.

## Completeness

The generated target is materially incomplete because it omits the DSMZ/TOGO
pH 7.4 preparation comment. It also lacks a variant relationship to the TOGO
M2380 liquid-base record generated from the same DSMZ source.

No citation object or `target_organisms` are expected on this provider recipe.
Those optional slots are correctly empty.

## Findings

### Major

- `data/normalized_yaml/bacterial/payne_seghal_gibbons_medium_add_agar.yaml`
  imports 36 mg FeCl2 x 4 H2O as 36 `G_PER_L` and 0.36 mg MnCl2 x 4 H2O as
  0.36 `G_PER_L`, inflating both trace salts by 1000x.
- The same TOGO import stores `Distilled water`, 1000 ml as 1000 `G_PER_L`
  rather than preserving it as a volume.
- The TOGO M2381 input drops the DSMZ/TOGO pH 7.4 preparation comment.
- TOGO M2381 and TOGO M2380 are generated as unrelated singleton records even
  though they are the add-agar and liquid-base variants of DSMZ Medium 1160.

### Minor

- The MgSO4 x 7 H2O primary `term` is `CHEBI:31795`, but
  `mediaingredientmech_chebi_term` still points to `CHEBI:32599`.

## Recommended Edits

- Fix the TOGO import or maintained M2381 input so milligram rows are converted
  to 0.036 `G_PER_L` for FeCl2 x 4 H2O and 0.00036 `G_PER_L` for MnCl2 x 4 H2O.
- Preserve TOGO volume rows as volumes or solution rows instead of encoding
  1000 ml distilled water as 1000 `G_PER_L`.
- Add the DSMZ/TOGO pH 7.4 preparation comment to the maintained M2381
  representation.
- Add an explicit M2380/M2381 variant relationship so the liquid base and
  add-agar records remain connected after generation.
- Refresh the MgSO4 x 7 H2O MediaIngredientMech CHEBI link so it matches the
  corrected primary `CHEBI:31795` term.

## Follow-up Checks

- Rerun the open schema, strict, reference, and term validators on the
  regenerated TOGO M2381 record.
- Compare the regenerated record against TOGO M2381 and DSMZ 1160 to confirm
  that the two milligram rows are scaled correctly and that the pH 7.4
  preparation comment is present.
- Re-run ignored-inclusive exact searches for `TOGO:M2380`, `TOGO:M2381`, and
  `DSMZ_Medium1160.pdf` to confirm the regenerated add-agar record is linked to
  its liquid-base sibling and still traceable to DSMZ Medium 1160.

## Additional Notes

None found.
