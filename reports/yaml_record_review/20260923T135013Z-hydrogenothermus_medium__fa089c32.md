# YAML Record Review: Hydrogenothermus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hydrogenothermus_medium__fa089c32.yaml
- Started UTC: 2026-09-23T13:47:00Z
- Finished UTC: 2026-09-23T13:50:13Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:002643 |
| Name | hydrogenothermus_medium |
| Original name | HYDROGENOTHERMUS MEDIUM |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| pH | 7.0 |
| Source identity | MediaDive/JCM Medium J286, HYDROGENOTHERMUS MEDIUM |
| Generated path reviewed | data/merge_yaml/merged/hydrogenothermus_medium__fa089c32.yaml |
| Maintained owner | data/normalized_yaml/bacterial/hydrogenothermus_medium.yaml |

The reviewed file is generated from the maintained JCM 286 record after
`resolve_option_c_references` copied `aquifex_medium` and the merge step
collapsed the two sources into one fingerprint. Future fixes should update the
JCM 286 normalized record, the Aquifex reference-expansion path, and the shared
stock-solution handling before regenerating `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hydrogenothermus_medium__fa089c32.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hydrogenothermus_medium__fa089c32.yaml --out /private/tmp/hydrogenothermus_medium__fa089c32.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hydrogenothermus_medium__fa089c32.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hydrogenothermus_medium__fa089c32.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The primary source identity is coherent: `CultureMech:002643`,
  `mediadive.medium:J286`, and the live JCM 286 page all identify
  HYDROGENOTHERMUS MEDIUM.
- JCM 286 is a child recipe of JCM 255 Aquifex Medium, not a source duplicate:
  it uses Aquifex Medium without Trace vitamins, supplements yeast extract and
  sulfur, adjusts to pH 7.0, and changes the sterilization and gassing
  procedure.
- A gitignore-independent exact search for `CultureMech:002643` over
  `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports` found the
  maintained JCM 286 file, generated indexes, generated merged YAML, archival
  reports, and one Aquifex `variant_children` backlink.
- A gitignore-independent exact search for `mediadive.medium:J286` over
  `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports` found only
  this JCM 286 record plus generated indexes and the review manifest.
- The generated synonym for `aquifex_medium` with source
  `mediadive.medium:J255`, `merged_from` list, `SOURCE_DUPLICATE` parent, and
  duplicate merge fingerprint conflict with the inspected JCM source
  relationship.
- The copied Aquifex mineral salts and vitamin ingredients are individually
  grounded where the inherited row should exist, but their presence and
  placement in JCM 286 are not source-faithful.

## Evidence

- JCM 286 and MediaDive J286 do not provide a stand-alone ingredient table;
  both say to use Aquifex Medium, omit Trace vitamins, and add 0.2 g/L yeast
  extract plus 0.5 g/L sulfur powder.
- JCM 255 / MediaDive J255 contains the Aquifex base direct salts, 10 ml Trace
  minerals, 20 mg (NH4)2Ni(SO4)2 x 6H2O, 0.1 mg Na2WO4 x 2H2O, 0.1 mg Na2SeO4,
  10 ml Trace vitamins, and 1 L distilled water.
- The reviewed JCM 286 YAML still contains all 10 Trace vitamins members from
  MediaDive solution 3861 even though the JCM 286 instruction explicitly omits
  that stock.
- A gitignore-independent, two-file search for yeast or sulfur ingredient
  `preferred_term` entries in the maintained and generated JCM 286 YAML found
  no matches; yeast extract and sulfur only appear in the preparation prose.
- The 10 ml Trace minerals stock from JCM 255 is flattened at undiluted stock
  strength, and stock members are merged into final-medium NaCl, MgSO4 x 7H2O,
  and CaCl2 x 2H2O rows.
- The JCM 255 1 L distilled-water row and the 1 L water rows in the Trace
  minerals and Trace vitamins stocks are omitted from the copied composition.

## Completeness

- The recipe is missing the two JCM 286 supplement ingredients: yeast extract
  at 0.2 g/L and sulfur powder at 0.5 g/L.
- The inherited Aquifex base needs to exclude the Trace vitamins stock and keep
  the 10 ml Trace minerals stock nested instead of flattening it into the final
  medium.
- The relationship to `aquifex_medium` should describe a variant or derived
  parent recipe, not a duplicate source recipe.
- pH 7.0 and the JCM 286 preparation description are present.
- Empty optional fields for target organisms, direct publication references,
  discussions, and quality flags are acceptable for this provider import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The two JCM 286 supplement ingredients are missing. | JCM 286 supplements Aquifex Medium with 0.2 g/L yeast extract and 0.5 g/L sulfur powder; the YAML has neither as an ingredient row. | `data/normalized_yaml/bacterial/hydrogenothermus_medium.yaml`; reference-expansion logic for modified parent media. |
| Major | Trace vitamins were copied into a medium that explicitly omits them. | JCM 286 says to use Aquifex Medium without Trace vitamins, but the YAML contains Biotin, Folic acid, Pyridoxine hydrochloride, Thiamine HCl, Riboflavin, Nicotinic acid, Calcium pantothenate, Vitamin B12, p-Aminobenzoic acid, and Lipoic acid from MediaDive solution 3861. | `data/normalized_yaml/bacterial/hydrogenothermus_medium.yaml`; copied parent rows need deletion-aware filtering. |
| Major | The Trace minerals stock from Aquifex Medium is flattened and merged into final-medium concentrations. | Aquifex Medium has a 10 ml Trace minerals row; the YAML has the stock's NTA and mineral rows as top-level ingredients and sums stock NaCl, MgSO4 x 7H2O, and CaCl2 x 2H2O with the direct Aquifex rows. | `data/normalized_yaml/bacterial/aquifex_medium.yaml`, `data/normalized_yaml/bacterial/hydrogenothermus_medium.yaml`, and MediaDive stock-solution import logic. |
| Major | JCM 286 was misclassified and merged as a duplicate of JCM 255. | The source modifies Aquifex Medium by removing Trace vitamins and adding yeast extract and sulfur, but the maintained JCM 286 record has `variant_relationship: SOURCE_DUPLICATE` and the generated record merges `aquifex_medium` and `hydrogenothermus_medium` under one fingerprint. | `data/normalized_yaml/bacterial/hydrogenothermus_medium.yaml`; duplicate detection should compare modified resolved compositions. |
| Major | Water volumes from the parent and copied stocks are omitted. | JCM 255 has 1 L distilled water in the main Aquifex base, and MediaDive solutions 3804 and 3861 each include 1 L distilled water; the copied ingredient list has no water rows. | `data/normalized_yaml/bacterial/aquifex_medium.yaml`; MediaDive volume import. |

## Recommended Edits

1. Add yeast extract at 0.2 g/L and sulfur powder at 0.5 g/L to the JCM 286
   maintained record.
2. Remove all Trace vitamins members from JCM 286 and ensure the copied Aquifex
   base excludes MediaDive solution 3861.
3. Represent Aquifex's 10 ml Trace minerals row as a nested stock addition, not
   as undiluted final-medium ingredients.
4. Repair duplicate merging so JCM 286 is retained as a child or variant of
   Aquifex Medium rather than a `SOURCE_DUPLICATE` of the parent.
5. Restore distilled-water volume rows for Aquifex Medium and its nested stock
   solutions where the source states them.
6. Regenerate `data/merge_yaml/merged/` from the corrected normalized record.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  JCM 286 merged record.
- Manually verify the regenerated JCM 286 composition against JCM 286, JCM 255,
  and MediaDive J255: Aquifex base minus Trace vitamins, plus yeast extract and
  sulfur.
- Confirm the regenerated JCM 286 record no longer shares Aquifex Medium's
  exact ingredient fingerprint and is not collapsed into JCM 255.

## Additional Notes

- The JCM 286 MediaDive REST record contains the preparation text but no
  materialized recipe array, so reconstructing JCM 286 requires applying the
  prose edit to JCM 255 rather than copying JCM 255 wholesale.
