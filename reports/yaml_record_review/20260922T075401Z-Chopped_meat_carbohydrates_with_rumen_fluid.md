# YAML Record Review: Chopped meat carbohydrates with rumen fluid

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Chopped_meat_carbohydrates_with_rumen_fluid.yaml
- Started UTC: 2026-09-22T07:53:05Z
- Finished UTC: 2026-09-22T07:54:03Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009143 |
| Label | Chopped meat carbohydrates with rumen fluid |
| Generated record | data/merge_yaml/merged/Chopped_meat_carbohydrates_with_rumen_fluid.yaml |
| Maintained owner | data/normalized_yaml/bacterial/chopped_meat_carbohydrates_with_rumen_fluid.yaml |
| Source | TOGO Medium M2574, ATCC Medium 1703 |

The reviewed file is a generated one-source merge of ATCC Medium 1703 through
TOGO M2574. Future fixes belong in the maintained normalized owner or in the
TOGO/ATCC importer and solution migration logic rather than in the generated
merge artifact.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/Chopped_meat_carbohydrates_with_rumen_fluid.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The term validator emitted only the expected `eutils/pkg_resources is
deprecated` warning before passing.

## Identity and Grounding

The source identity is correct: `CultureMech:009143`, `TOGO:M2574`, the ATCC
PDF token in the source URL, and the generated merge fingerprint all denote
ATCC Medium 1703, Chopped meat carbohydrates with rumen fluid.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID,
TOGO M2574 source ID, normalized owner stem, source URL token, and merge
fingerprint found only this generated record, its maintained owner, and
normalized index entries.

## Evidence

ATCC Medium 1703 and TOGO M2574 support a medium made by supplementing ATCC
Medium 1490 with 0.4% glucose, 0.1% cellobiose, 0.1% maltose, 0.1% starch, and
15% filtered rumen fluid.

ATCC Medium 1490 is itself a staged chopped-meat medium. The source first boils
500.0 g fat-free ground beef, 1.0 L distilled water, and 25.0 mL N NaOH,
removes fat, filters while retaining meat particles and filtrate, and restores
the filtrate volume to 1 L. The source then adds 30.0 g Trypticase peptone,
5.0 g yeast extract, 5.0 g `K2HPO4`, 4.0 mL 0.025% resazurin, and 20.0 g
optional agar; boils and cools the medium under 80% N2, 10% H2, and 10% CO2;
adds 0.5 g L-cysteine HCl, 10.0 mL Hemin Solution, and 0.2 mL Vitamin K1
Solution; adjusts the final pH to 7.0; and anaerobically dispenses 7 mL into
tubes containing one part meat to five parts fluid under the same gas phase.

The ATCC Hemin solution is a separate stock of 50.0 mg hemin, 1.0 mL N NaOH,
and distilled water to 100.0 mL. The ATCC Vitamin K1 Solution is a separate
stock of 0.15 mL Vitamin K1 in 30.0 mL 95% ethanol.

The record flattens ATCC Medium 1490 and both solution stocks into the final
formula. It leaves `ATCC Medium 1490` as a 1 g/L ingredient, imports the 10 mL
and 0.2 mL stock additions as `G_PER_L`, migrates stock internals such as
95% ethanol, 50 mg hemin, and hemin-stock N NaOH into parent ingredients, and
then merges the parent and hemin-stock water and NaOH into 101 g/L distilled
water and 26 g/L N NaOH.

The 80:10:10 N2/H2/CO2 gas phase is reduced to three variable gas ingredients,
and the record lacks the pH, filtration, volume-restoration, anaerobic
dispensing, and autoclave workflow.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this ATCC source record.

The recipe is incomplete until ATCC Medium 1490 is represented as a structured
parent, the Hemin and Vitamin K1 stocks stay separate from final-medium
ingredients, source volume and mass units are preserved, pH 7.0 and the 80:10:10
gas phase are represented, and the ATCC preparation workflow is captured.

## Findings

| Severity | Finding |
| --- | --- |
| Major | `ATCC Medium 1490` is modeled as a 1 g/L ingredient while all of its internals are flattened into the final recipe. **Owner:** the TOGO M2574 normalized owner or the TOGO/ATCC parent-medium importer. |
| Major | Hemin Solution and Vitamin K1 Solution internals are flattened into parent ingredients, causing 95% ethanol, hemin, hemin-stock distilled water, and hemin-stock N NaOH to appear at the wrong level. **Owner:** solution migration and the maintained normalized owner. |
| Major | Source millilitre and milligram quantities are converted or merged into `G_PER_L`, including both stock additions, N NaOH, distilled water, 0.025% resazurin, 95% ethanol, Vitamin K1, and hemin. **Owner:** the TOGO/ATCC unit-conversion importer and solution migration. |
| Major | The pH 7.0, 80% N2 / 10% H2 / 10% CO2 gas phase, meat-filtrate staging, stock storage instruction, anaerobic dispensing, one-to-five meat-particle ratio, and 121 C autoclave instruction are missing. **Owner:** the maintained TOGO M2574 normalized owner or the TOGO/ATCC importer. |

## Recommended Edits

1. Represent the top-level medium as ATCC Medium 1490 plus the four
   carbohydrates and filtered rumen fluid.
2. Model ATCC Medium 1490 as the staged chopped-meat parent formula instead of
   flattening it into an ordinary ingredient list.
3. Keep Hemin Solution and Vitamin K1 Solution as stock solutions with
   source-faithful internals and add only 10.0 mL and 0.2 mL of those stocks to
   the final medium.
4. Convert liquid and mass quantities to source-faithful units, add pH 7.0,
   model the 80:10:10 gas phase, and capture the source preparation comments.
5. Regenerate merged YAML after repairing the maintained owner or importer.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated record against TOGO M2574 and the ATCC
Medium 1703 PDF to confirm that ATCC Medium 1490, the two stock solutions,
volume and mass units, pH, gas phase, and preparation instructions remain
source-faithful.

## Additional Notes

None found.
