# YAML Record Review: Chopped Meat Carbohydrate Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Chopped_Meat_Carbohydrate_Medium.yaml
- Started UTC: 2026-09-22T07:45:09Z
- Finished UTC: 2026-09-22T07:46:56Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009264 |
| Label | Chopped Meat Carbohydrate Medium |
| Generated record | data/merge_yaml/merged/Chopped_Meat_Carbohydrate_Medium.yaml |
| Maintained owner | data/normalized_yaml/bacterial/chopped_meat_carbohydrate_medium.yaml |
| Source | TOGO Medium M2713, ATCC Medium 1016 |

The reviewed file is a generated one-source merge of ATCC Medium 1016 through
TOGO M2713. Future fixes belong in
`data/normalized_yaml/bacterial/chopped_meat_carbohydrate_medium.yaml` or the
TOGO/ATCC importer that handles nested media and millilitre units rather than
in `data/merge_yaml/merged/Chopped_Meat_Carbohydrate_Medium.yaml`.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/Chopped_Meat_Carbohydrate_Medium.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The first TOGO and ATCC requests failed on DNS resolution inside the sandbox and
then passed when retried directly. The term validator emitted only the expected
`eutils/pkg_resources is deprecated` warning before passing.

## Identity and Grounding

The source identity is correct: `CultureMech:009264`, `TOGO:M2713`, the ATCC
Medium 1016 PDF, and the generated merge fingerprint all denote Chopped Meat
Carbohydrate Medium.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID,
TOGO M2713 source ID, ATCC PDF token, normalized owner stem, and merge
fingerprint found this generated record, its maintained owner, two sibling ATCC
Chopped Meat Carbohydrate variants, and normalized index entries.

## Evidence

ATCC Medium 1016 and TOGO M2713 support a parent formula with 30.0 g peptone,
5.0 g yeast extract, 5.0 g `K2HPO4`, 4.0 g glucose, 1.0 g cellobiose, 1.0 g
maltose, 1.0 g starch, 150.0 mL rumen fluid, 4.0 mL 0.025% resazurin solution,
15.0 g optional agar, and 850 mL Chopped Meat Broth. They also support boiling,
cooling, adding 0.5 g cysteine, setting pH to 7.0, anaerobic dispensing under
nitrogen or nitrogen:hydrogen gas in 7 mL test-tube volumes, capping with
rubber stoppers, and autoclaving at 121 C.

The record flattens the Chopped Meat Broth subrecipe into parent ingredients.
The ATCC stock contains 500.0 g fat-free ground beef, 1000 mL DI water, and
25.0 mL 1 N NaOH and has its own boil, cooling, fat-skimming, cheesecloth
filtration, and volume-restoration instructions. Those three stock ingredients
should be nested under Chopped Meat Broth rather than asserted as additional
direct parent ingredients.

Every source millilitre quantity is imported as grams per litre. The parent
150 mL rumen fluid, 4 mL resazurin solution, and 850 mL Chopped Meat Broth rows
are all liquid volumes; the Chopped Meat Broth stock's 1000 mL DI water and
25 mL 1 N NaOH are also liquid volumes. The generated `solutions` entry for
0.025% resazurin has an empty composition and records `4 G_PER_L`, losing the
fact that 4 mL of that stock solution is added to the parent medium.

The source pH 7.0 and all parent and Chopped Meat Broth preparation
instructions are absent from the generated record.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this ATCC source record.

The formula is incomplete until Chopped Meat Broth is represented as a nested
stock, liquid volumes are kept as volumes, 0.025% resazurin is represented as a
4 mL stock addition, and the parent and broth preparation steps are restored.

## Findings

| Severity | Finding |
| --- | --- |
| Major | The Chopped Meat Broth stock recipe is flattened into direct parent ingredients. **Owner:** `data/normalized_yaml/bacterial/chopped_meat_carbohydrate_medium.yaml` or the TOGO/ATCC importer. |
| Major | Parent and nested millilitre additions are imported as `G_PER_L`, including rumen fluid, resazurin solution, Chopped Meat Broth, DI water, and 1 N NaOH. **Owner:** the TOGO/ATCC unit-conversion importer. |
| Major | The pH 7.0 assertion and all preparation instructions are missing. **Owner:** the TOGO/ATCC importer. |

## Recommended Edits

1. Nest the ATCC Chopped Meat Broth recipe under the 850 mL parent Chopped Meat
   Broth addition.
2. Convert all source mL amounts to source-faithful volume units and keep
   0.025% resazurin as a 4 mL stock-solution addition.
3. Add pH 7.0 and restore both parent and Chopped Meat Broth preparation
   workflows from the ATCC PDF.
4. Regenerate merged YAML after repairing the maintained owner or importer.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated record against TOGO M2713 and the ATCC
Medium 1016 PDF to confirm nested broth, resazurin, pH, and preparation
semantics.

## Additional Notes

None found.
