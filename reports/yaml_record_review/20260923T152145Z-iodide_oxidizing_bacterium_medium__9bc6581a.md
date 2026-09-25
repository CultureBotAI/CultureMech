# YAML Record Review: IODIDE-OXIDIZING BACTERIUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/iodide_oxidizing_bacterium_medium__9bc6581a.yaml
- Started UTC: 2026-09-23T15:19:00Z
- Finished UTC: 2026-09-23T15:21:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:003266 |
| Name | iodide_oxidizing_bacterium_medium |
| Original name | IODIDE-OXIDIZING BACTERIUM MEDIUM |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | SOLID_AGAR |
| pH | Not represented |
| Source identity | MediaDive JCM Medium J919 |
| Generated path reviewed | data/merge_yaml/merged/iodide_oxidizing_bacterium_medium__9bc6581a.yaml |
| Maintained owner | data/normalized_yaml/bacterial/iodide_oxidizing_bacterium_medium.yaml |

The reviewed file is generated from the maintained MediaDive/JCM owner above.
Future fixes should update that normalized record, deduplicate it with the TOGO
M965 owner, and regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/iodide_oxidizing_bacterium_medium__9bc6581a.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/iodide_oxidizing_bacterium_medium__9bc6581a.yaml --out /private/tmp/iodide_oxidizing_bacterium_medium__9bc6581a.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/iodide_oxidizing_bacterium_medium__9bc6581a.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; zero reference checks were applicable. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/iodide_oxidizing_bacterium_medium__9bc6581a.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The stable ID, slug, `mediadive.medium:J919` source term, and source URL
  identify the MediaDive import of JCM Medium 919.
- A gitignore-independent exact search for `CultureMech:003266` over bacterial
  normalized records, normalized indexes, and merged records found only this
  owner, this generated copy, and index entries.
- A gitignore-independent exact search for `mediadive.medium:J919` over the
  same paths found only this owner, this generated copy, and index entries.
- A gitignore-independent exact anchored search for `TOGO:M965` found a
  separate TOGO import of the same JCM medium.

## Evidence

- MediaDive J919 exposes Marine agar 2216, potassium iodide, soluble starch,
  and 1000 ml distilled water in one main solution.
- TOGO M965 preserves the same formula with the same 55.1 g Marine agar 2216,
  1 g potassium iodide, 1.2 g soluble starch, and 1 L distilled water rows.
- The live JCM GRMD=919 page now returns `Nothing found`, so MediaDive and TOGO
  are the recoverable upstream formula views for this JCM identifier.
- The generated MediaDive record drops the 1000 ml distilled-water row.
- The MediaDive J919 and TOGO M965 branches are still emitted as separate
  generated records.

## Completeness

- The marine agar, potassium iodide, and soluble starch rows are present.
- The source water carrier is absent.
- The duplicate TOGO/JCM branch should be linked or merged with this
  MediaDive/JCM branch after preserving the water row.
- Empty optional fields for synonyms, direct publication references,
  preparation steps, organism targets, discussions, variants, and quality flags
  are acceptable after the water carrier and duplicate branch are fixed.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The 1000 ml distilled-water row is missing. | MediaDive J919 and TOGO M965 both list distilled water; the MediaDive YAML has only Marine agar 2216, potassium iodide, and starch. | `data/normalized_yaml/bacterial/iodide_oxidizing_bacterium_medium.yaml`; MediaDive import. |
| Minor | The TOGO duplicate is not merged. | This record is `mediadive.medium:J919`; `data/normalized_yaml/bacterial/TOGO_M965_Iodide-Oxidizing_Bacterium_Medium.yaml` is `TOGO:M965` with the same JCM formula. | Duplicate detection across MediaDive J919 and TOGO M965. |

## Recommended Edits

1. Restore the 1000 ml distilled-water row from MediaDive J919.
2. Link the MediaDive J919 and TOGO M965 records as source duplicates and keep
   the water carrier in the canonical merged output.
3. Regenerate `data/merge_yaml/merged/` from the corrected normalized sources.

## Follow-up Checks

1. Rerun open LinkML, strict, reference, and term validation after correcting
   the MediaDive owner and duplicate links.
2. Recompare the canonical generated record to MediaDive J919 and TOGO M965,
   checking the 55.1 g Marine agar 2216, 1 g potassium iodide, 1.2 g starch,
   and 1 L water rows.
3. Confirm only one canonical merged record is emitted for MediaDive J919 /
   TOGO M965 after duplicate linking.

## Additional Notes

- This record has no target-organism or literature evidence entries, so no
  organism-grounding, snippet, or DOI checks were applicable.
