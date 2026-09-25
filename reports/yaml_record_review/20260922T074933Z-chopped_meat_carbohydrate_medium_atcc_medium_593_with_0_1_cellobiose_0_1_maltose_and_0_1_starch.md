# YAML Record Review: Chopped meat carbohydrate medium with cellobiose, maltose, and starch

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chopped_meat_carbohydrate_medium_atcc_medium_593_with_0_1_cellobiose_0_1_maltose_and_0_1_starch.yaml
- Started UTC: 2026-09-22T07:47:57Z
- Finished UTC: 2026-09-22T07:49:35Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009257 |
| Label | Chopped meat carbohydrate medium (ATCC Medium 593) with 0.1% cellobiose, 0.1% maltose and 0.1% starch |
| Generated record | data/merge_yaml/merged/chopped_meat_carbohydrate_medium_atcc_medium_593_with_0_1_cellobiose_0_1_maltose_and_0_1_starch.yaml |
| Maintained owner | data/normalized_yaml/bacterial/chopped_meat_carbohydrate_medium_atcc_medium_593_with_0_1_cellobiose_0_1_maltose_and_0_1_starch.yaml |
| Source | TOGO Medium M2705, ATCC Medium 1015 / ATCC Medium 593 |

The reviewed file is a generated one-source merge of ATCC Medium 1015 through
TOGO M2705. Future fixes belong in the maintained normalized owner or in the
TOGO/ATCC importer that handles staged meat-broth construction and millilitre
units rather than in the generated merge artifact.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chopped_meat_carbohydrate_medium_atcc_medium_593_with_0_1_cellobiose_0_1_maltose_and_0_1_starch.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The first TOGO and ATCC requests failed on DNS resolution inside the sandbox and
then passed when retried directly. The term validator emitted only the expected
`eutils/pkg_resources is deprecated` warning before passing.

## Identity and Grounding

The source identity is correct: `CultureMech:009257`, `TOGO:M2705`, the ATCC
Medium 1015 PDF, and the generated merge fingerprint all denote Chopped meat
carbohydrate medium based on ATCC Medium 593 with 0.1% cellobiose, 0.1% maltose,
and 0.1% starch.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID,
TOGO M2705 source ID, ATCC PDF token, normalized owner stem, and merge
fingerprint found this generated record, its maintained owner, and normalized
index entries.

## Evidence

ATCC Medium 1015 and TOGO M2705 support ATCC Medium 593 with 0.1% cellobiose,
0.1% maltose, and 0.1% starch. ATCC Medium 593 first builds a meat filtrate
from 500.0 g fat-free ground beef, 1.0 L distilled water, and 25.0 mL N NaOH.
The source then adds 30.0 g peptone, 5.0 g yeast extract, 5.0 g `K2HPO4`, and
4.0 mL 0.025% resazurin solution to the filtrate, followed by boiling, cooling,
adding 0.5 g L-cysteine HCl, adjusting to pH 7.0, dispensing 7 mL under 97%
nitrogen / 3% hydrogen over one part meat particles to 4-5 parts fluid, capping
with butyl rubber stoppers, and autoclaving under fast exhaust for 15 minutes.

The record flattens the meat-filtrate stage into direct parent ingredients.
The ground beef, 1 L distilled water, and 25 mL N NaOH rows should form the
ATCC Medium 593 meat broth stage and should not be represented as simple direct
ingredients in the final supplemented parent medium.

The importer also converts liquid volumes to grams per litre. Distilled water
is recorded as 1 g/L instead of 1 L, N NaOH is 25 g/L instead of 25 mL, and
4 mL 0.025% resazurin solution is migrated to an empty solution shell at
4 g/L. The 97% nitrogen / 3% hydrogen atmosphere is defaulted to two variable
gas ingredients.

The source pH 7.0 and all preparation steps are absent from the generated
record.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this ATCC source record.

The recipe is incomplete until the meat-filtrate stage, source liquid volumes,
0.025% resazurin stock addition, pH, 97:3 gas ratio, 7 mL dispensing volume, and
autoclave workflow are represented.

## Findings

| Severity | Finding |
| --- | --- |
| Major | The ATCC Medium 593 meat-filtrate stage is flattened into direct parent ingredients. **Owner:** the maintained TOGO M2705 normalized owner or the TOGO/ATCC importer. |
| Major | Distilled water, N NaOH, and resazurin solution are imported as `G_PER_L` instead of source liquid volumes. **Owner:** the TOGO/ATCC unit-conversion importer. |
| Major | The pH 7.0, 97% nitrogen / 3% hydrogen atmosphere, dispensing, stopper, autoclave, and meat-broth preparation instructions are missing. **Owner:** the TOGO/ATCC importer. |

## Recommended Edits

1. Model ATCC Medium 593 as a staged meat-filtrate preparation and keep the
   0.1% cellobiose, 0.1% maltose, and 0.1% starch as final supplements.
2. Convert all source liquid amounts to source-faithful volume units, including
   the 1.0 L distilled water, 25 mL N NaOH, and 4 mL 0.025% resazurin solution.
3. Add pH 7.0 and the complete source preparation workflow, including the 97:3
   nitrogen:hydrogen atmosphere.
4. Regenerate merged YAML after repairing the maintained owner or importer.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated record against TOGO M2705 and the ATCC
Medium 1015 PDF to confirm the staged broth construction and final carbohydrate
supplements are source-faithful.

## Additional Notes

None found.
