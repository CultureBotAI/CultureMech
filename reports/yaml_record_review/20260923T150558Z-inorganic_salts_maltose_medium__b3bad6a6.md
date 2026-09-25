# YAML Record Review: INORGANIC SALTS-MALTOSE MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/inorganic_salts_maltose_medium__b3bad6a6.yaml
- Started UTC: 2026-09-23T15:03:45Z
- Finished UTC: 2026-09-23T15:06:04Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:010476 |
| Name | inorganic_salts_maltose_medium |
| Original name | INORGANIC SALTS-MALTOSE MEDIUM |
| Class | MediaRecipe |
| Category | fungal |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| pH | 7.5 |
| Source identity | DSMZ/MediaDive Medium 754 |
| Generated path reviewed | data/merge_yaml/merged/inorganic_salts_maltose_medium__b3bad6a6.yaml |
| Maintained owner | data/normalized_yaml/fungal/inorganic_salts_maltose_medium.yaml |

The reviewed file is generated from the maintained DSMZ/MediaDive owner above.
Future fixes should update that normalized record, source-duplicate links to
the KOMODO owner, and MediaDive stock-solution import logic before regenerating
`data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/inorganic_salts_maltose_medium__b3bad6a6.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/inorganic_salts_maltose_medium__b3bad6a6.yaml --out /private/tmp/inorganic_salts_maltose_medium__b3bad6a6.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/inorganic_salts_maltose_medium__b3bad6a6.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; zero reference checks were applicable. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/inorganic_salts_maltose_medium__b3bad6a6.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The stable ID, slug, `mediadive.medium:754` source term, and source URL
  identify the direct DSMZ Medium 754 import.
- A gitignore-independent exact search for `CultureMech:010476` over normalized
  records, normalized indexes, and merged records found only this MediaDive
  owner, its generated merged copy, and index entries.
- A gitignore-independent exact search for `mediadive.medium:754` found this
  owner plus a KOMODO Medium 754 record that names the same DSMZ source in its
  notes.
- A gitignore-independent exact search for `komodo.medium:754` found the
  separate KOMODO record for the same DSMZ formula.

## Evidence

- DSMZ and MediaDive define the recipe as 2 g peptone, 4 g yeast extract,
  980 ml inorganic salt solution, and 20 ml of a filter-sterilized 25% maltose
  solution after autoclaving.
- The YAML keeps the final 5 g/L maltose amount and both DSMZ preparation
  steps, including post-autoclave maltose addition, ordered salt dissolution,
  and optional 0.75% agar.
- The YAML flattens the inorganic salt stock by recording CaCl2 x 2 H2O, NaCl,
  and MgSO4 x 7 H2O as top-level ingredients at the stock recipe's 1 L
  concentrations.
- The source 980 ml inorganic salt solution row and its 1000 ml stock water row
  are both absent.
- The direct MediaDive import and the KOMODO import are still emitted as two
  separate merged records despite representing DSMZ Medium 754.

## Completeness

- The principal organic components, pH 7.5, maltose timing, salt-order note,
  autoclave condition, and optional agar concentration are represented.
- The inorganic salt stock boundary is missing, so the exact 980 ml stock
  addition is not recoverable from the generated YAML.
- Empty optional fields for synonyms, direct publication references, organism
  targets, discussions, variants, and quality flags are acceptable only after
  the inorganic salt solution and source-duplicate relationship are represented
  explicitly.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The 980 ml inorganic salt solution is flattened as stock-strength final salts. | DSMZ/MediaDive list 980 ml of an inorganic salt solution containing CaCl2, NaCl, MgSO4, and 1000 ml water; the YAML records the three stock salts directly at the stock's G_PER_L concentrations. | `data/normalized_yaml/fungal/inorganic_salts_maltose_medium.yaml`; MediaDive stock import. |
| Major | The DSMZ Medium 754 source duplicate is not merged. | This record is `mediadive.medium:754`; `data/normalized_yaml/bacterial/inorganic_salts_maltose_medium.yaml` is `komodo.medium:754` with the same DSMZ formula and no direct source-duplicate link. | Duplicate detection across MediaDive 754 and KOMODO 754. |
| Minor | The 25% maltose stock addition is only implicit. | The preparation step says to add 20 ml of a 25% filter-sterilized maltose solution, but `ingredients` contains only final 5 g/L maltose. | `data/normalized_yaml/fungal/inorganic_salts_maltose_medium.yaml`; MediaDive stock import. |

## Recommended Edits

1. Represent Inorganic salt solution as a 980 ml stock addition with the source
   CaCl2, NaCl, MgSO4, and 1000 ml water subrecipe.
2. Preserve the 20 ml 25% filter-sterilized maltose addition as source stock
   structure alongside the final maltose amount.
3. Link the KOMODO 754 record to the direct DSMZ/MediaDive 754 record as a
   source duplicate and keep the DSMZ preparation steps in the canonical merged
   output.
4. Regenerate `data/merge_yaml/merged/` after the normalized sources are
   corrected.

## Follow-up Checks

1. Rerun open LinkML, strict, reference, and term validation after correcting
   the MediaDive 754 owner and source-duplicate links.
2. Diff the regenerated canonical Medium 754 record against the DSMZ PDF and
   MediaDive 754 payload to confirm the 980 ml inorganic salt solution, 20 ml
   maltose stock, and two DSMZ preparation steps are retained.
3. Confirm only one canonical merged record is emitted for DSMZ/KOMODO Medium
   754 after duplicate linking.

## Additional Notes

- This record has no target-organism or literature evidence entries, so no
  organism-grounding, snippet, or DOI checks were applicable.
