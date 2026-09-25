# YAML Record Review: paracoccus_alcaliphilus_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/paracoccus_alcaliphilus_medium__0f81fc1f.yaml
- Started UTC: 2026-09-24T19:46:18Z
- Finished UTC: 2026-09-24T19:46:18Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:001906 |
| Name | paracoccus_alcaliphilus_medium |
| Original name | PARACOCCUS ALCALIPHILUS MEDIUM |
| Source identity | DSMZ Medium 772 / MediaDive 772 |
| Source path | data/normalized_yaml/bacterial/paracoccus_alcaliphilus_medium.yaml |
| Generated path | data/merge_yaml/merged/paracoccus_alcaliphilus_medium__0f81fc1f.yaml |
| Merge fingerprint | 0f81fc1fb75432dcab7957853b23d8bfb60d28ef4d6157083c00d39a1ed0901d |

The target is a generated merged record. Future edits should be made in the
maintained normalized input and merge/import logic, not directly in
`data/merge_yaml/merged/paracoccus_alcaliphilus_medium__0f81fc1f.yaml`.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/paracoccus_alcaliphilus_medium__0f81fc1f.yaml` exited 0 with no diagnostics. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/paracoccus_alcaliphilus_medium__0f81fc1f.yaml --out /private/tmp/paracoccus_alcaliphilus_medium__0f81fc1f.strict.tsv --workers 1 --quiet` exited 0 and wrote only the TSV header. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/paracoccus_alcaliphilus_medium__0f81fc1f.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` exited 0. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/paracoccus_alcaliphilus_medium__0f81fc1f.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` embedded in merged YAML. |

## Identity and Grounding

The generated record correctly denotes DSMZ Medium 772, PARACOCCUS
ALCALIPHILUS MEDIUM. Its medium grounding uses `mediadive.medium:772`, which
matches the DSMZ PDF and MediaDive REST identity.

The ingredient groundings are syntactically valid and term validation passed.
Most source rows are represented at the right gram-per-liter scale:

| DSMZ 772 row | Generated representation |
| --- | --- |
| (NH4)2SO4, 3.0 g | `(NH4)2SO4`, 3 `G_PER_L` |
| KH2PO4, 1.4 g | `KH2PO4`, 1.4 `G_PER_L` |
| Na2HPO4, 3.0 g | `Na2HPO4`, 3 `G_PER_L` |
| MgSO4 x 7 H2O, 0.2 g | `MgSO4 x 7 H2O`, 0.2 `G_PER_L` |
| Fe-citrate, 30.0 mg | `Fe(III) citrate`, 0.03 `G_PER_L` |
| CaCl2 x 2 H2O, 30.0 mg | `CaCl2 x 2 H2O`, 0.03 `G_PER_L` |
| MnCl2 x 4 H2O, 5.0 mg | `MnCl2 x 4 H2O`, 0.005 `G_PER_L` |
| ZnSO4 x 7 H2O, 5.0 mg | `ZnSO4 x 7 H2O`, 0.005 `G_PER_L` |
| CuSO4 x 2 H2O, 0.5 mg | `CuSO4 x 2 H2O`, 0.0005 `G_PER_L` |
| Thiamine-HCl x 2 H2O, 0.4 mg | `Thiamine-HCl x 2 H2O`, 0.0004 `G_PER_L` |
| 10 ml sterile methanol added after sterilization | `Methanol`, 7.92 `G_PER_L` |

## Evidence

The DSMZ Medium 772 PDF supports the recipe name, pH 9.0, the ten salts and
thiamine rows, the 10 ml methanol addition, and the preparation note stating
that thiamine hydrochloride may be replaced by 2 g/l yeast extract and that the
pH is adjusted with filter-sterilised 10% Na2CO3.

The MediaDive 772 REST source likewise resolves to the same DSMZ recipe and
includes an explicit `Distilled water`, 1000 ml row. The generated target does
not carry that water row.

An ignored-inclusive search for `PARACOCCUS_ALCALIPHILUS_MEDIUM`,
`KOMODO_772`, `paracoccus_alcaliphilus_medium`, and exact DSMZ 772 source
strings found:

- `data/normalized_yaml/bacterial/paracoccus_alcaliphilus_medium.yaml`
- `data/normalized_yaml/bacterial/KOMODO_772_PARACOCCUS_ALCALIPHILUS_MEDIUM.yaml`
- `data/merge_yaml/merged/paracoccus_alcaliphilus_medium__0f81fc1f.yaml`
- `data/merge_yaml/merged/PARACOCCUS_ALCALIPHILUS_MEDIUM.yaml`

The KOMODO normalized record is another import of DSMZ 772. Its generated
record has the same core DSMZ ingredient list plus an extra variable `Na2CO3`
entry extracted from the pH-adjustment note, and it is emitted under a
different merge fingerprint.

## Completeness

The record is materially incomplete: DSMZ Medium 772 includes `Distilled water`
at 1000 ml, but neither the generated target nor its maintained normalized
input includes a water ingredient.

The generated merge is also incomplete across source duplicates. The KOMODO 772
input declares the same DSMZ Medium 772 identity, but the current merge split
emits it as `data/merge_yaml/merged/PARACOCCUS_ALCALIPHILUS_MEDIUM.yaml`.

No citation object or `target_organisms` are expected on this provider recipe.
Those optional slots are correctly empty.

## Findings

### Major

- `data/normalized_yaml/bacterial/paracoccus_alcaliphilus_medium.yaml` and the
  generated target omit the DSMZ/MediaDive `Distilled water`, 1000 ml row. The
  source medium is a one-liter recipe, so the absence of water loses the final
  dilution context for all solutes.
- DSMZ Medium 772 is split into two generated records:
  `paracoccus_alcaliphilus_medium__0f81fc1f.yaml` from the direct MediaDive
  import and `PARACOCCUS_ALCALIPHILUS_MEDIUM.yaml` from KOMODO 772. The sibling
  is the same source recipe, not a concentration variant.

## Recommended Edits

- Restore a `Distilled water`, 1000 ml ingredient in
  `data/normalized_yaml/bacterial/paracoccus_alcaliphilus_medium.yaml`, then
  regenerate the merged YAML.
- Reconcile KOMODO 772 with the direct DSMZ/MediaDive 772 record in the
  maintained input or merge logic so the DSMZ recipe has one generated
  representation. The fix should avoid using a note-derived variable `Na2CO3`
  row to force a second fingerprint for the same source formulation.

## Follow-up Checks

- Rerun the open schema, strict, reference, and term validators on the
  regenerated DSMZ 772 record.
- Re-run an ignored-inclusive exact search for `DSMZ Medium: 772`, `ID: 772`,
  `mediadive.medium:772`, and `KOMODO_772_PARACOCCUS_ALCALIPHILUS_MEDIUM` to
  confirm that the KOMODO duplicate now merges or is explicitly deduplicated.
- Compare the regenerated ingredient list against the DSMZ Medium 772 PDF or
  MediaDive REST response and confirm the 1000 ml water row is represented.

## Additional Notes

None found.
