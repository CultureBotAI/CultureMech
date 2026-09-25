# YAML Record Review: Iodide-Oxidizing Bacterium Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/iodide_oxidizing_bacterium_medium.yaml
- Started UTC: 2026-09-23T15:14:05Z
- Finished UTC: 2026-09-23T15:18:50Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:010390 |
| Name | iodide_oxidizing_bacterium_medium |
| Original name | Iodide-Oxidizing Bacterium Medium |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | SOLID_AGAR |
| pH | Not represented |
| Source identity | TOGO Medium M965, derived from JCM Medium 919 |
| Generated path reviewed | data/merge_yaml/merged/iodide_oxidizing_bacterium_medium.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M965_Iodide-Oxidizing_Bacterium_Medium.yaml |

The reviewed file is generated from the maintained TOGO/JCM owner above.
Future fixes should update that normalized record, deduplicate it with the
MediaDive J919 owner, and regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/iodide_oxidizing_bacterium_medium.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/iodide_oxidizing_bacterium_medium.yaml --out /private/tmp/iodide_oxidizing_bacterium_medium.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/iodide_oxidizing_bacterium_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; zero reference checks were applicable. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/iodide_oxidizing_bacterium_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The stable ID, slug, `TOGO:M965` media term, and source URL identify TOGO's
  JCM Medium 919 import.
- A gitignore-independent exact search for `CultureMech:010390` over bacterial
  normalized records, normalized indexes, and merged records found only this
  owner, this generated copy, and index entries.
- A gitignore-independent exact anchored search for `TOGO:M965` over the same
  paths found only this owner, this generated copy, and index entries.
- A gitignore-independent exact search for `mediadive.medium:J919` found a
  separate direct MediaDive import of the same JCM medium.

## Evidence

- TOGO M965 and MediaDive J919 both expose Marine agar 2216, potassium iodide,
  soluble starch or starch, and distilled water at the same amounts.
- The live JCM GRMD=919 page now returns `Nothing found`, so TOGO and MediaDive
  are the recoverable upstream formula views for this JCM identifier.
- The generated TOGO record preserves the four source rows, but it records
  1 L distilled water as `1 G_PER_L`.
- The direct MediaDive J919 record records the three solute or agar rows but is
  emitted as a separate merged record instead of being linked to TOGO M965 as a
  source duplicate.

## Completeness

- The marine agar, potassium iodide, and soluble starch masses are represented.
- The distilled-water unit is wrong in the TOGO branch.
- The duplicate MediaDive/JCM branch should be linked or merged with this
  TOGO/JCM branch after preserving the TOGO water row.
- Empty optional fields for synonyms, direct publication references,
  preparation steps, organism targets, discussions, variants, and quality flags
  are acceptable after the water unit and duplicate branch are fixed.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The 1 L distilled-water row is represented with a mass-concentration unit. | TOGO M965 and MediaDive J919 list 1 L / 1000 ml distilled water; the YAML has `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M965_Iodide-Oxidizing_Bacterium_Medium.yaml`; TOGO unit import. |
| Minor | The direct MediaDive duplicate is not merged. | This record is `TOGO:M965`; `data/normalized_yaml/bacterial/iodide_oxidizing_bacterium_medium.yaml` is `mediadive.medium:J919` with the same non-water formulation. | Duplicate detection across TOGO M965 and MediaDive J919. |

## Recommended Edits

1. Correct the TOGO M965 distilled-water row to `1 L`.
2. Link the TOGO M965 and MediaDive J919 records as source duplicates and keep
   the water carrier in the canonical merged output.
3. Regenerate `data/merge_yaml/merged/` from the corrected normalized sources.

## Follow-up Checks

1. Rerun open LinkML, strict, reference, and term validation after correcting
   the TOGO owner and duplicate links.
2. Recompare the canonical generated record to TOGO M965 and MediaDive J919,
   checking the 55.1 g Marine agar 2216, 1 g potassium iodide, 1.2 g starch,
   and 1 L water rows.
3. Confirm only one canonical merged record is emitted for TOGO M965 /
   MediaDive J919 after duplicate linking.

## Additional Notes

- This record has no target-organism or literature evidence entries, so no
  organism-grounding, snippet, or DOI checks were applicable.
