# YAML Record Review: payne_seghal_gibbons_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/payne_seghal_gibbons_medium__d891051e.yaml
- Started UTC: 2026-09-24T19:50:56Z
- Finished UTC: 2026-09-24T19:50:56Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:008965 |
| Name | payne_seghal_gibbons_medium |
| Original name | Payne, Seghal & Gibbons Medium |
| Source identity | TOGO Medium M2380 |
| Source path | data/normalized_yaml/bacterial/TOGO_M2380_Payne_Seghal_Gibbons_Medium.yaml |
| Generated path | data/merge_yaml/merged/payne_seghal_gibbons_medium__d891051e.yaml |
| Merge fingerprint | d891051e2a4a13c958ed58889aa6fe9c40567aa628b7f24f36e7a223923e96ed |

The target is a generated merged record. Future edits should be made in the
maintained TOGO input or TOGO import logic, not directly in
`data/merge_yaml/merged/payne_seghal_gibbons_medium__d891051e.yaml`.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/payne_seghal_gibbons_medium__d891051e.yaml` exited 0 and reported no issues. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/payne_seghal_gibbons_medium__d891051e.yaml --out /private/tmp/payne_seghal_gibbons_medium__d891051e.strict.tsv --workers 1 --quiet` exited 0 and wrote only the TSV header. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/payne_seghal_gibbons_medium__d891051e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` exited 0 with 0 checks. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/payne_seghal_gibbons_medium__d891051e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` embedded in merged YAML. |

## Identity and Grounding

The `TOGO:M2380` medium grounding resolves to Payne, Seghal & Gibbons Medium
and points back to DSMZ Medium 1160. Its M2380 identity is the liquid-base TOGO
projection of the DSMZ recipe; the add-agar companion is TOGO M2381.

Several ingredient amounts match TOGO M2380 and DSMZ 1160 after gram-per-liter
normalization: 20 g/L MgSO4 x 7 H2O, 10 g/L yeast extract, 250 g/L NaCl, 2 g/L
KCl, 3 g/L trisodium citrate, and 7.5 g/L Casamino acids.

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

The TOGO M2380 API and the DSMZ 1160 PDF both support the Payne, Seghal &
Gibbons identity, pH 7.4, 1000 ml distilled water, 36 mg FeCl2 x 4 H2O, 0.36 mg
MnCl2 x 4 H2O, and the comment to adjust pH to 7.4 and add 20 g agar for solid
medium. The generated target lost the pH and comment and mis-converted the two
milligram amounts as grams per liter.

The generated `payne_seghal_gibbons_medium_add_agar.yaml` sibling is TOGO
M2381, another TOGO projection from the same DSMZ Medium 1160 PDF that includes
the optional 20 g agar row. That is a related add-agar variant of M2380, not an
unrelated recipe.

An ignored-inclusive PCRE2 search for `TOGO:M2380`, `M2380`, `Payne, Seghal &
Gibbons`, and `DSMZ_Medium1160.pdf` found the current TOGO M2380 input, the
current generated target, the TOGO M2381 add-agar sibling, and the direct
DSMZ/MediaDive DSMZ 1160 normalized input. A separate ignored-inclusive search
for `mediadive.medium:1160`, `KOMODO_1160_PAYNE_SEGHAL_GIBBONS`, and
`1160_23178` found the KOMODO/DSMZ source-duplicate group for the same DSMZ
source formulation.

## Completeness

The generated target is materially incomplete because it omits TOGO's pH 7.4
metadata and the DSMZ preparation comment. It also has no variant relationship
to the TOGO M2381 add-agar recipe generated from the same DSMZ source.

No citation object or `target_organisms` are expected on this provider recipe.
Those optional slots are correctly empty.

## Findings

### Major

- `data/normalized_yaml/bacterial/TOGO_M2380_Payne_Seghal_Gibbons_Medium.yaml`
  imports 36 mg FeCl2 x 4 H2O as 36 `G_PER_L` and 0.36 mg MnCl2 x 4 H2O as
  0.36 `G_PER_L`, inflating both trace salts by 1000x.
- The same TOGO import stores `Distilled water`, 1000 ml as 1000 `G_PER_L`
  rather than preserving it as a volume.
- The TOGO M2380 input drops pH 7.4 and the DSMZ/TOGO preparation comment.
- TOGO M2380 and TOGO M2381 are generated as unrelated singleton records even
  though they are the liquid-base and add-agar variants of DSMZ Medium 1160.

### Minor

- The MgSO4 x 7 H2O primary `term` is `CHEBI:31795`, but
  `mediaingredientmech_chebi_term` still points to `CHEBI:32599`.

## Recommended Edits

- Fix the TOGO import or maintained M2380 input so milligram rows are converted
  to 0.036 `G_PER_L` for FeCl2 x 4 H2O and 0.00036 `G_PER_L` for MnCl2 x 4 H2O.
- Preserve TOGO volume rows as volumes or solution rows instead of encoding
  1000 ml distilled water as 1000 `G_PER_L`.
- Add pH 7.4 and the DSMZ/TOGO preparation comment to the maintained M2380
  representation.
- Add an explicit M2380/M2381 variant relationship so the liquid base and
  add-agar records remain connected after generation.
- Refresh the MgSO4 x 7 H2O MediaIngredientMech CHEBI link so it matches the
  corrected primary `CHEBI:31795` term.

## Follow-up Checks

- Rerun the open schema, strict, reference, and term validators on the
  regenerated TOGO M2380 record.
- Compare the regenerated record against TOGO M2380 and DSMZ 1160 to confirm
  that the two milligram rows are scaled correctly and that pH 7.4 is present.
- Re-run ignored-inclusive exact searches for `TOGO:M2380`, `TOGO:M2381`, and
  `mediadive.medium:1160` to confirm the regenerated M2380 record is linked to
  its add-agar sibling and still traceable to DSMZ Medium 1160.

## Additional Notes

None found.
