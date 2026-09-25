# YAML Record Review: ANCALOMICROBIUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANCALOMICROBIUM_MEDIUM.yaml
- Started UTC: 2026-09-21T12:59:10Z
- Finished UTC: 2026-09-21T13:01:09Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ANCALOMICROBIUM_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:002949` |
| Name | `ancalomicrobium_medium` |
| Source accession | `mediadive.medium:J601` |
| Source label | `ANCALOMICROBIUM MEDIUM` |
| Generated status | Generated merge from `JCM_J601_ANCALOMICROBIUM_MEDIUM` |

The reviewed file is a generated merge of one maintained JCM / MediaDive input:
`data/normalized_yaml/bacterial/JCM_J601_ANCALOMICROBIUM_MEDIUM.yaml`.

The exact, gitignore-independent identity search used `rg --no-ignore --hidden`
across `data/normalized_yaml`, `data/merge_yaml/merged`, `scripts`, `tests`,
and `history` for `ANCALOMICROBIUM_MEDIUM`, `ANCALOMICROBIUM MEDIUM`,
`ancalomicrobium_medium`, `CultureMech:002949`, `mediadive.medium:J601`,
`JCM_J601_ANCALOMICROBIUM_MEDIUM`, and `jcm_grmd?GRMD=601`. It found the
maintained JCM input, this generated merge, generated indexes, and related TOGO
and KOMODO Ancalomicrobium records that are reviewed separately.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANCALOMICROBIUM_MEDIUM.yaml` | Passed with no issues reported |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANCALOMICROBIUM_MEDIUM.yaml --out /private/tmp/ANCALOMICROBIUM_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANCALOMICROBIUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were available |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANCALOMICROBIUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` inside one generated merge |

The documented `just` wrappers still fail before focused validation in this
checkout because project `uv` resolves with Python 3.13 and attempts to build
`llvmlite==0.46.0`, whose setuptools build aborts with `TypeError:
Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project
Python 3.11 commands above validate the generated record without building the
project.

## Identity and Grounding

The record correctly identifies JCM Medium 601 / MediaDive `J601`; the current
JCM page is headed `601  ANCALOMICROBIUM MEDIUM`, matches the stored source URL,
and lists a final pH adjustment to 7.0.

The source identity is narrower than the generated ingredient list. JCM Medium
601 contains `(NH4)2SO4`, glucose, `Na2HPO4`, 980 ml distilled water, 10 ml of
Vitamin solution from JCM Medium 979, and 20 ml of Modified Hutner's basal salts
from JCM Medium 900. The generated record omits the two solution additions and
instead emits Medium 979 vitamin rows and the Medium 900 Modified Hutner's basal
salts rows as direct Medium 601 ingredients.

The grounding of supplied hydrates is mostly exact, but `(NH4)6Mo7O24 x 4 H2O`
is grounded to generic ammonium molybdate rather than an ammonium molybdate
tetrahydrate, and `MnSO4 x n H2O` is grounded only to generic manganese sulfate.

## Evidence

JCM Medium 601 supports the three main dry components, the `980.0 ml` distilled
water row, the final pH 7.0 adjustment, a 10 ml Vitamin solution addition, a 20
ml Modified Hutner's basal salts addition, and the note that the Vitamin
solution should be filter-sterilized and added aseptically.

JCM Medium 979 supports the undiluted Vitamin solution stock composition:
Vitamin B12, biotin, thiamine hydrochloride dihydrate, calcium pantothenate,
folic acid, riboflavin, nicotinamide, and 1 L distilled water. These are not
direct Medium 601 rows unless they are represented with the 10 ml/L dilution
from Medium 601.

JCM Medium 900 supports the undiluted Modified Hutner's basal salts stock
composition: nitrilotriacetic acid, magnesium sulfate heptahydrate, calcium
chloride dihydrate, ammonium molybdate, 99 mg/L ferrous sulfate heptahydrate,
50 ml/L Metals "44", and 950 ml/L water. Metals "44" from JCM Medium 149
contains disodium EDTA, zinc sulfate heptahydrate, 500 mg/L ferrous sulfate
heptahydrate, manganese sulfate hydrate, copper sulfate pentahydrate, cobalt
nitrate hexahydrate, sodium borate decahydrate, and 1 L distilled water.

The generated `FeSO4 x 7 H2O` row combines the 99 mg/L Modified Hutner's basal
salts stock row with the 500 mg/L Metals "44" stock row as `0.599 G_PER_L`.
That loses both solution boundaries and both dilution steps.

## Completeness

The top-level JCM Medium 601 identity, pH, dry salts, and filter-sterilized
vitamin-preparation note are present.

The consequential gaps are:

- no `solutions` entry for the 10 ml Vitamin solution addition from Medium 979;
- no `solutions` entry for the 20 ml Modified Hutner's basal salts addition
  from Medium 900;
- no nested Metals "44" addition inside the Modified Hutner's basal salts
  solution;
- no distilled-water row from Medium 601 or from any referenced stock;
- no solution-local scope for the Vitamin solution filtration note or Hutner
  pH 6.8 adjustment.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The Vitamin solution from JCM Medium 979 is flattened into direct final-medium rows. | JCM Medium 601 adds 10 ml Vitamin solution, while the generated record emits Vitamin B12 through nicotinamide at the undiluted 1 L stock concentrations from Medium 979. | `data/normalized_yaml/bacterial/JCM_J601_ANCALOMICROBIUM_MEDIUM.yaml` |
| Major | Modified Hutner's basal salts from JCM Medium 900 are flattened into direct final-medium rows. | JCM Medium 601 adds 20 ml Modified Hutner's basal salts, while the generated record emits NTA, magnesium sulfate heptahydrate, calcium chloride dihydrate, ammonium molybdate, and ferrous sulfate at Medium 900 stock concentrations. | Same normalized owner |
| Major | Metals "44" from JCM Medium 149 are flattened two solution levels away from Medium 601. | Medium 900 adds 50 ml Metals "44"; Medium 601 adds 20 ml of Medium 900. The generated record emits the Metals "44" EDTA, zinc, iron, manganese, copper, cobalt, and borate rows as direct Medium 601 ingredients, and merges the Metals ferrous sulfate with the Hutner ferrous sulfate. | Same normalized owner |
| Minor | Two stock-preparation steps are scoped to the main Medium 601 record. | The filter-sterilization step belongs to the Vitamin solution, and the NTA/KOH/pH 6.8 step belongs to Modified Hutner's basal salts, but both appear as root `preparation_steps`. | Same normalized owner after stock repair |
| Minor | Two hydrate-sensitive trace salts have only generic groundings. | The source states `(NH4)6Mo7O24 x 4 H2O` and `MnSO4 x n H2O`; the generated rows store generic ammonium molybdate and generic manganese sulfate terms. | Same normalized owner or ingredient grounding enrichment |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/JCM_J601_ANCALOMICROBIUM_MEDIUM.yaml`,
   restore the two Medium 601 solution additions and replace the flattened
   stock ingredients with 10 ml/L Vitamin solution and 20 ml/L Modified
   Hutner's basal salts.
2. Represent the JCM Medium 979 Vitamin solution and JCM Medium 900 Modified
   Hutner's basal salts as structured stock solutions, with Metals "44" from
   JCM Medium 149 nested under the Hutner stock.
3. Restore distilled-water rows for the main JCM Medium 601 recipe and the
   nested solution recipes.
4. Move the filter-sterilization step under the Vitamin solution and the
   NTA/KOH/pH 6.8 adjustment under the Modified Hutner's basal salts solution.
5. Clear the generic ammonium molybdate and manganese sulfate terms unless exact
   hydrate-aware groundings are available in the packaged MediaIngredientMech
   index.

## Follow-up Checks

1. Run `just validate-schema`, `just validate-strict`, `just validate-terms`,
   and `just validate-references` on
   `data/normalized_yaml/bacterial/JCM_J601_ANCALOMICROBIUM_MEDIUM.yaml`.
2. Regenerate `data/merge_yaml/merged/ANCALOMICROBIUM_MEDIUM.yaml`.
3. Re-open the regenerated merge and verify that vitamin ingredients, Hutner
   salts, and Metals "44" no longer appear as direct final-medium rows.

## Additional Notes

The exact identity search included ignored files. It found an adjacent TOGO
M608 snapshot of the same JCM Medium 601 source and two adjacent DSMZ / KOMODO
603 Ancalomicrobium records, but none are merged into this JCM/MediaDive
generated record.
