# YAML Record Review: medium_for_h_dombrowskii

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_h_dombrowskii.yaml
- Started UTC: 2026-09-24T01:39:58Z
- Finished UTC: 2026-09-24T01:40:15Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:006897 |
| Name | medium_for_h_dombrowskii |
| Generated record | data/merge_yaml/merged/medium_for_h_dombrowskii.yaml |
| Source identities merged | KOMODO medium 954; MediaDive/DSMZ medium 954 |

This generated record merges the KOMODO and direct MediaDive representations of
DSMZ Medium 954, "MEDIUM FOR H. DOMBROWSKII." The formula is a high-salt solid
agar medium with pH 7.4.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_h_dombrowskii.yaml` | Passed with no issues found. |
| Strict validation, `scripts/validate_strict.py data/merge_yaml/merged/medium_for_h_dombrowskii.yaml --workers 1` | Passed; the TSV contained only its header and 0 error rows. |
| Reference validation, `linkml-reference-validator validate data ... --target-class MediaRecipe` | Passed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data ... -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented history validator targets standalone `history/` files, not embedded generated-record events. |

The focused validators were run with Python 3.11 through `uv --no-project
--offline` to avoid the project-level Python 3.13 `llvmlite` build failure.

## Identity and Grounding

The generated ID, name, original name, bacterial category, solid-agar physical
state, pH 7.4, `komodo.medium:954` media term, and `SOURCE_DUPLICATE` link to
`data/normalized_yaml/bacterial/medium_for_h_dombrowskii.yaml` all point to DSMZ
Medium 954. MediaDive 954 confirms the same source name, pH, and ingredient list.

A gitignore-independent exact scan for `mediadive.medium:954`,
`DSMZ_Medium954`, `medium_for_h_dombrowskii`, and `TOGO:M2379` found this
MediaDive/KOMODO generated merge and a separate TOGO generated record,
`data/merge_yaml/merged/medium_for_h_dombrowski.yaml`, for the same DSMZ Medium
954 source through TOGO M2379. Ignored files were included.

## Evidence

MediaDive 954 supports all eight non-water ingredients, their G_PER_L values,
pH 7.4, and the note that agar should be added after dissolving all ingredients
in water and adjusting pH. KOMODO copied the same DSMZ Medium 954 ingredient
signature, and its normalized owner is correctly marked as a source duplicate of
the direct MediaDive owner.

The generated record preserves the ingredient values and pH, but not the
MediaDive preparation step. Its ingredients are otherwise source-consistent:
Casamino acids 5 g/L, yeast extract 5 g/L, Tris 12.1 g/L, KCl 2 g/L,
MgCl2 x 6 H2O 20 g/L, CaCl2 x 2 H2O 0.2 g/L, NaCl 200 g/L, and agar 20 g/L.

No target-organism claims are asserted. That is acceptable for an imported DSMZ
recipe that carries no inspected strain-growth evidence.

## Completeness

The missing `preparation_steps` row is consequential because adding agar after
pH adjustment is explicit source procedure, not generic solid-medium boilerplate.
The generated record is also incomplete at the source-family level because the
TOGO M2379 import of the same DSMZ Medium 954 source has not been merged into
this canonical spelling.

## Findings

| Severity | Finding | Evidence | Maintained owner for future fix |
|---|---|---|---|
| major | The KOMODO/MediaDive merge loses MediaDive-only preparation. | `data/normalized_yaml/bacterial/medium_for_h_dombrowskii.yaml` retains the pH-adjust-then-add-agar instruction from MediaDive 954. The generated merge based on the KOMODO child has pH 7.4 but no `preparation_steps`. | Merge logic for source duplicates; direct MediaDive owner `data/normalized_yaml/bacterial/medium_for_h_dombrowskii.yaml`. |
| major | DSMZ Medium 954 is still split across a misspelled TOGO M2379 generated record. | The exact source-family scan found TOGO M2379 in `medium_for_h_dombrowski.yaml`, while this generated record merges only KOMODO 954 and MediaDive 954. Both point at DSMZ Medium 954. | Source-equivalence reconciliation between `data/normalized_yaml/bacterial/medium_for_h_dombrowskii.yaml` and `data/normalized_yaml/bacterial/medium_for_h_dombrowski.yaml`. |

## Recommended Edits

1. Preserve direct-parent `preparation_steps` when KOMODO and MediaDive source
   duplicates merge, then regenerate DSMZ Medium 954.
2. Map the misspelled TOGO M2379 owner to DSMZ Medium 954 and merge it into this
   source family.

## Follow-up Checks

- Run focused open schema, strict, reference, and term validators on the
  regenerated DSMZ Medium 954 record.
- Run `just verify-merges` to confirm `preparation_steps` survive the
  source-duplicate merge and the misspelled TOGO record no longer emits a
  standalone generated artifact.
- Repeat a gitignore-independent scan for `mediadive.medium:954`,
  `TOGO:M2379`, and `DSMZ_Medium954` to confirm only the reconciled owners, one
  generated merge, and expected indexes reference the source family.

## Additional Notes

None found.
