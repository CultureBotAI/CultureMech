# YAML Record Review: Hyphomicrobium Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hyphomicrobium_medium__41859ce8.yaml
- Started UTC: 2026-09-23T14:02:30Z
- Finished UTC: 2026-09-23T14:04:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:000813 |
| Name | hyphomicrobium_medium |
| Original name | HYPHOMICROBIUM MEDIUM |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | DEFINED |
| Composition type | DEFINED |
| Physical state | SOLID_AGAR |
| pH | 6.0 |
| Source identity | MediaDive/DSMZ Medium 1355, HYPHOMICROBIUM MEDIUM |
| Generated path reviewed | data/merge_yaml/merged/hyphomicrobium_medium__41859ce8.yaml |
| Maintained owner | data/normalized_yaml/bacterial/hyphomicrobium_medium.yaml |

The reviewed file is generated from the maintained MediaDive/DSMZ import above.
Future fixes should update the normalized record or MediaDive stock-solution
import for DSMZ 1355, then regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hyphomicrobium_medium__41859ce8.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hyphomicrobium_medium__41859ce8.yaml --out /private/tmp/hyphomicrobium_medium__41859ce8.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hyphomicrobium_medium__41859ce8.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hyphomicrobium_medium__41859ce8.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The record identity is coherent: `CultureMech:000813` is the MediaDive import
  of DSMZ Medium 1355, and the inspected DSMZ PDF and MediaDive REST record
  both identify HYPHOMICROBIUM MEDIUM.
- A gitignore-independent exact search for `CultureMech:000813` over
  `data/normalized_yaml/bacterial`, `data/merge_yaml/merged`, MediaDive
  indexes, and the review manifest found only this maintained DSMZ 1355 record
  and its generated merged copy.
- A gitignore-independent exact search for `mediadive.medium:1355` over
  `data/normalized_yaml/bacterial`, `data/merge_yaml/merged`, and MediaDive
  indexes found only this DSMZ 1355 record.
- `hyphomicrobium_medium_saf` is a separate DSMZ 1386 SAF medium, not an
  alternate owner for this record.
- K2HPO4, NaH2PO4, ammonium sulfate, MgSO4 x 7H2O, agar, methylamine, EDTA,
  ZnSO4 x 7H2O, CaCl2 x 2H2O, MnCl2 x 4H2O, FeSO4 x 7H2O, CuSO4 x 5H2O, and
  CoCl2 x 6H2O are grounded exactly enough. Ammonium molybdate is hydrated in
  the source but grounded generically.

## Evidence

- The four direct Mineral Salts Solution rows and their pH 6.0 value match DSMZ
  1355 and MediaDive 1355.
- The source adds 1 ml Visniac Trace Elements (1000x) to the final medium and
  defines that stock in 500 ml water; the YAML flattens all eight trace rows
  into top-level final-medium ingredients at the stock's g/L concentrations.
- DSMZ lists 1000 ml distilled water in the main Mineral Salts Solution and
  500 ml distilled water in the Visniac stock; neither water row is present.
- The source adds sterile 0.2% v/v methylamine after autoclaving; MediaDive
  preserves it as a 2 ml row, but the YAML records Methylamine as `2 G_PER_L`.
- The source says the medium may be solidified by adding 12 g/L agar; the YAML
  records agar as a required ingredient and sets the whole recipe to
  `SOLID_AGAR`.
- The Visniac Trace Elements pH adjustment belongs to the stock, but the YAML
  imports it as top-level preparation step 2.

## Completeness

- The 1 ml Visniac Trace Elements addition needs to be nested with its
  component rows and its 500 ml water row.
- The sterile methylamine addition needs to retain the source stock
  concentration, volume, and post-autoclave scope.
- Agar optionality needs to be modeled as an optional solidifying addition or
  a variant rather than a required final row.
- Empty optional fields for target organisms, synonyms, variants, direct
  publication references, discussions, and quality flags are acceptable for
  this provider import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Visniac Trace Elements (1000x) is flattened into the final medium at stock concentration. | DSMZ 1355 adds 1 ml Visniac Trace Elements to the Mineral Salts Solution; the YAML lists EDTA, ZnSO4 x 7H2O, CaCl2 x 2H2O, MnCl2 x 4H2O, FeSO4 x 7H2O, ammonium molybdate, CuSO4 x 5H2O, and CoCl2 x 6H2O as top-level ingredients. | `data/normalized_yaml/bacterial/hyphomicrobium_medium.yaml`; MediaDive stock-solution import logic. |
| Major | Methylamine volume was converted into a mass concentration. | DSMZ adds 2 ml sterile 0.2% v/v methylamine after autoclaving; the YAML records `2 G_PER_L` Methylamine. | `data/normalized_yaml/bacterial/hyphomicrobium_medium.yaml`; post-autoclave stock addition handling. |
| Major | Source water volumes are omitted. | DSMZ has 1000 ml distilled water in the main solution and 500 ml in Visniac Trace Elements; no water row appears in the YAML. | `data/normalized_yaml/bacterial/hyphomicrobium_medium.yaml`; MediaDive volume import. |
| Major | Agar optionality and broth state are lost. | The source states that the medium may be solidified by 12 g/L agar, but the YAML makes agar mandatory and sets `physical_state: SOLID_AGAR`. | `data/normalized_yaml/bacterial/hyphomicrobium_medium.yaml`; optional agar handling. |
| Major | Visniac stock preparation is scoped to the final medium. | The NaOH pH adjustment belongs to the trace stock, but the YAML records it as top-level step 2. | `data/normalized_yaml/bacterial/hyphomicrobium_medium.yaml`; preparation import should keep stock steps nested. |

## Recommended Edits

1. Restore Visniac Trace Elements as a 1 ml nested stock addition with the eight
   source trace rows and 500 ml water.
2. Represent methylamine as a 2 ml post-autoclave addition of sterile 0.2% v/v
   stock.
3. Represent the 1000 ml main distilled-water row.
4. Model 12 g/L agar as optional or as a solid-medium variant.
5. Move the Visniac NaOH pH-adjustment step under the stock.
6. Regenerate `data/merge_yaml/merged/` from the corrected normalized record.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  DSMZ 1355 merged record.
- Manually compare the regenerated record against the DSMZ 1355 PDF and
  MediaDive 1355 REST record.
- Verify the final-medium ingredients contain only the Mineral Salts Solution
  rows, optional agar if chosen, and a nested 1 ml Visniac addition.

## Additional Notes

- The MediaDive REST record already exposes Visniac Trace Elements as solution
  2729; the loss happens when that stock is expanded into the normalized
  recipe.
