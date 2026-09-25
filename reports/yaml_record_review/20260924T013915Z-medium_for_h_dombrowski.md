# YAML Record Review: medium_for_h_dombrowski

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_h_dombrowski.yaml
- Started UTC: 2026-09-24T01:38:38Z
- Finished UTC: 2026-09-24T01:39:15Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:008963 |
| Name | medium_for_h_dombrowski |
| Generated record | data/merge_yaml/merged/medium_for_h_dombrowski.yaml |
| Maintained owner | data/normalized_yaml/bacterial/medium_for_h_dombrowski.yaml |
| Source identity | TOGO:M2379 importing DSMZ Medium 954 |

This generated record is the TOGO M2379 import of DSMZ Medium 954, a solid agar
medium for halophilic H. dombrowskii. It is a single-source generated artifact;
future fixes belong in the normalized TOGO owner and the merge/reconciliation
logic that should fold it into the existing DSMZ Medium 954 record family.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_h_dombrowski.yaml` | Passed with no issues found. |
| Strict validation, `scripts/validate_strict.py data/merge_yaml/merged/medium_for_h_dombrowski.yaml --workers 1` | Passed; the TSV contained only its header and 0 error rows. |
| Reference validation, `linkml-reference-validator validate data ... --target-class MediaRecipe` | Passed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data ... -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented history validator targets standalone `history/` files, not embedded generated-record events. |

The focused validators were run with Python 3.11 through `uv --no-project
--offline` to avoid the project-level Python 3.13 `llvmlite` build failure.

## Identity and Grounding

TOGO M2379, the TOGO owner, and the reviewed generated record all point at DSMZ
Medium 954. The ingredients, quantities, category, complex/undefined medium
class, and solid-agar physical state agree with the MediaDive 954 record.

The source label in the generated record is misspelled relative to DSMZ and
MediaDive: TOGO uses `Medium For H. Dombrowski`, while DSMZ/MediaDive use
`MEDIUM FOR H. DOMBROWSKII`. That lost final `i` propagates into the normalized
name `medium_for_h_dombrowski` and prevents source-duplicate matching with
`data/normalized_yaml/bacterial/medium_for_h_dombrowskii.yaml`, which is the
direct MediaDive owner for the same DSMZ Medium 954 source.

A gitignore-independent exact scan for `TOGO:M2379`,
`mediadive.medium:954`, `DSMZ_Medium954`, `medium_for_h_dombrowski`, and
`medium_for_h_dombrowskii` found the TOGO owner and generated artifact split
from the direct MediaDive/KOMODO source-duplicate pair under the corrected
`medium_for_h_dombrowskii` spelling. Ignored files were included.

## Evidence

TOGO M2379 and MediaDive 954 agree that DSMZ Medium 954 contains, per liter,
5 g Casamino acids, 5 g yeast extract, 12.1 g Tris, 2 g KCl, 20 g
MgCl2 x 6 H2O, 0.2 g CaCl2 x 2 H2O, 200 g NaCl, 20 g agar, and distilled water.
Those component amounts are preserved in the generated target.

The pH and preparation detail are not preserved. TOGO exposes pH 7.4 in its
metadata, and the MediaDive 954 step says to adjust to pH 7.4 and add agar only
after dissolving all other ingredients and adjusting pH. The generated TOGO
record has no `ph_value` and no `preparation_steps`.

No target-organism claims are asserted. That is acceptable here because the
inspected TOGO and MediaDive records define the recipe but do not list a growth
experiment or a strain-specific target organism.

## Completeness

The generated record is complete enough for the ingredient list, but it is
missing final pH, preparation order, corrected DSMZ source spelling, and the
source-duplicate relationship to direct DSMZ Medium 954 records. Those gaps are
consequential because they leave this TOGO import outside the already-merged
MediaDive/KOMODO generated record for the same DSMZ source.

## Findings

| Severity | Finding | Evidence | Maintained owner for future fix |
|---|---|---|---|
| major | The TOGO import carries a misspelled source label that splits a DSMZ Medium 954 duplicate. | TOGO M2379 links to DSMZ Medium 954 but says `Medium For H. Dombrowski`; MediaDive 954 and the direct owner use `MEDIUM FOR H. DOMBROWSKII`. The generated layer has `medium_for_h_dombrowski.yaml` beside `medium_for_h_dombrowskii.yaml`, which already merges the direct MediaDive and KOMODO DSMZ 954 imports. | `data/normalized_yaml/bacterial/medium_for_h_dombrowski.yaml`; source-duplicate reconciliation for DSMZ Medium 954. |
| major | Final pH and agar-order preparation are missing. | TOGO M2379 stores pH 7.4; MediaDive 954 additionally preserves the instruction to adjust pH before adding agar. The TOGO owner and generated record carry neither field. | `data/normalized_yaml/bacterial/medium_for_h_dombrowski.yaml`. |

## Recommended Edits

1. Normalize the TOGO M2379 label and filename lineage to the DSMZ/MediaDive
   spelling `H. dombrowskii`, or otherwise add source-equivalence metadata that
   unambiguously maps the misspelled TOGO source to DSMZ Medium 954.
2. Link the TOGO owner as a `SOURCE_DUPLICATE` of
   `data/normalized_yaml/bacterial/medium_for_h_dombrowskii.yaml` and re-run the
   merge so only one generated DSMZ Medium 954 record remains.
3. Add `ph_value: 7.4` and the agar-after-pH adjustment preparation step from
   MediaDive/DSMZ to the maintained TOGO owner before regenerating.

## Follow-up Checks

- Run the focused open schema, strict, reference, and term validators on the
  repaired TOGO owner and regenerated DSMZ 954 merge.
- Run `just verify-merges` to confirm the misspelled TOGO record no longer
  emits a standalone `medium_for_h_dombrowski.yaml` generated artifact.
- Repeat a gitignore-independent exact scan for `TOGO:M2379`,
  `mediadive.medium:954`, and `DSMZ_Medium954` to ensure the source family
  appears only on the reconciled normalized owners, the single generated merge,
  and expected indexes.
- Manually compare the regenerated DSMZ 954 record against MediaDive 954 and
  TOGO M2379 to confirm every ingredient amount, pH 7.4, and agar preparation
  survived source reconciliation.

## Additional Notes

None found.
