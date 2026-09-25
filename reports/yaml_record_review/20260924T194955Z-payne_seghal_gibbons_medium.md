# YAML Record Review: payne_seghal_gibbons_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/payne_seghal_gibbons_medium.yaml
- Started UTC: 2026-09-24T19:49:55Z
- Finished UTC: 2026-09-24T19:49:55Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:003871 |
| Name | payne_seghal_gibbons_medium |
| Original name | PAYNE, SEGHAL & GIBBONS medium |
| Source identity | KOMODO 1160 merged with DSMZ/MediaDive 1160 |
| Source paths | data/normalized_yaml/bacterial/KOMODO_1160_PAYNE_SEGHAL_GIBBONS_medium.yaml; data/normalized_yaml/bacterial/medium_1160_modified_for_dsm_23178.yaml; data/normalized_yaml/bacterial/payne_seghal_gibbons_medium.yaml |
| Generated path | data/merge_yaml/merged/payne_seghal_gibbons_medium.yaml |
| Merge fingerprint | 876d49baf5cb82d3c250646d6a7c9d0fe2338da4ffe55cd87f4fb205a67aaf4d |

The target is a generated merged record. Future edits should be made in the
maintained normalized inputs or merge logic, not directly in
`data/merge_yaml/merged/payne_seghal_gibbons_medium.yaml`.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/payne_seghal_gibbons_medium.yaml` exited 0 and reported no issues. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/payne_seghal_gibbons_medium.yaml --out /private/tmp/payne_seghal_gibbons_medium.strict.tsv --workers 1 --quiet` exited 0 and wrote only the TSV header. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/payne_seghal_gibbons_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` exited 0 with 0 checks. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/payne_seghal_gibbons_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` embedded in merged YAML. |

## Identity and Grounding

The merged record correctly describes DSMZ Medium 1160, PAYNE, SEGHAL & GIBBONS
MEDIUM. The direct DSMZ/MediaDive source uses `mediadive.medium:1160`, and the
two KOMODO records explicitly identify DSMZ Medium 1160 as their source
formulation.

The generated ingredient concentrations match the DSMZ 1160 PDF and MediaDive
REST response for the eight chemical rows plus the 20 g agar row for solid
medium:

| DSMZ 1160 row | Generated representation |
| --- | --- |
| Casamino acids (Difco), 7.50 g | `Casamino acids`, 7.5 `G_PER_L` |
| Yeast extract, 10.00 g | `Yeast extract`, 10 `G_PER_L` |
| Trisodium citrate, 3.00 g | `Trisodium citrate`, 3 `G_PER_L` |
| KCl, 2.00 g | `KCl`, 2 `G_PER_L` |
| MgSO4 x 7 H2O, 20.00 g | `MgSO4 x 7 H2O`, 20 `G_PER_L` |
| FeCl2 x 4 H2O, 36.00 mg | `FeCl2 x 4 H2O`, 0.036 `G_PER_L` |
| MnCl2 x 4 H2O, 0.36 mg | `MnCl2 x 4 H2O`, 0.00036 `G_PER_L` |
| NaCl, 250.00 g | `NaCl`, 250 `G_PER_L` |
| Agar, 20.0 g for solid medium | `Agar`, 20 `G_PER_L` |

## Evidence

The DSMZ 1160 PDF and MediaDive 1160 REST payload support the record's pH 7.4,
solid agar state, ingredient amounts, and agar condition. They also include an
explicit `Distilled water`, 1000 ml row that is absent from the generated
target and from all three normalized inputs merged into it.

The direct DSMZ normalized record contains the preparation instruction, `Adjust
pH to 7.4. For solid medium add 20.0 g agar.` The generated merge selected the
KOMODO duplicate as canonical and kept the pH value and agar ingredient note,
but lost the `preparation_steps` entry.

An ignored-inclusive search for `mediadive.medium:1160`,
`KOMODO_1160_PAYNE_SEGHAL_GIBBONS`, `1160_23178`, `DSMZ, ID: 1160`, and
`PAYNE, SEGHAL` found exactly the three maintained normalized inputs already
listed in `merged_from`. No additional exact DSMZ 1160 source record was found.

## Completeness

The merged record has two completeness gaps:

- The DSMZ/MediaDive `Distilled water`, 1000 ml row is missing.
- The generated merge dropped the direct DSMZ `preparation_steps` text.

No citation object or `target_organisms` are expected on this provider recipe.
Those optional slots are correctly empty.

## Findings

### Major

- The normalized DSMZ 1160 and KOMODO 1160 inputs omit the provider's
  `Distilled water`, 1000 ml row, so the generated merge omits the final recipe
  volume.
- `merge_recipes.py` selected a KOMODO duplicate that lacks preparation text as
  canonical and did not preserve the direct DSMZ record's pH/agar preparation
  step in the generated merge.

## Recommended Edits

- Add the missing 1000 ml distilled-water row to
  `data/normalized_yaml/bacterial/payne_seghal_gibbons_medium.yaml` and to the
  KOMODO DSMZ-1160 projection, or fix the importer so all DSMZ 1160 projections
  preserve the water row before merging.
- Update merge behavior for source duplicates so preparation steps from a
  fuller direct provider record are retained when a KOMODO projection is chosen
  as the generated record's canonical value source.

## Follow-up Checks

- Rerun the open schema, strict, reference, and term validators on the
  regenerated DSMZ 1160 record.
- Compare the regenerated record against DSMZ Medium 1160 or MediaDive 1160 and
  confirm it includes the 1000 ml distilled-water row and the pH/solid-medium
  preparation instruction.
- Re-run an ignored-inclusive exact search for `mediadive.medium:1160`,
  `KOMODO_1160_PAYNE_SEGHAL_GIBBONS`, and `1160_23178` to confirm the same
  three projections still merge into one generated record.

## Additional Notes

None found.
