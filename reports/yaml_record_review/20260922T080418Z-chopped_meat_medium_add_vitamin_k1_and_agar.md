# YAML Record Review: Chopped Meat Medium (add Vitamin K1 and agar)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chopped_meat_medium_add_vitamin_k1_and_agar.yaml
- Started UTC: 2026-09-22T08:03:36Z
- Finished UTC: 2026-09-22T08:04:20Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009094 |
| Label | Chopped Meat Medium (add Vitamin K1 and agar) |
| Generated record | data/merge_yaml/merged/chopped_meat_medium_add_vitamin_k1_and_agar.yaml |
| Maintained owner | data/normalized_yaml/bacterial/chopped_meat_medium_add_vitamin_k1_and_agar.yaml |
| Source | TOGO Medium M2524, DSMZ Medium 78 |

The reviewed file is a generated one-source merge of the DSMZ Medium 78 agar
slant with Vitamin K1 additions through TOGO M2524. Future fixes belong in the
maintained normalized owner or in the TOGO/DSMZ importer and solution migration
logic rather than in the generated merge artifact.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chopped_meat_medium_add_vitamin_k1_and_agar.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The term validator emitted only the expected `eutils/pkg_resources is
deprecated` warning before passing.

## Identity and Grounding

The source identity is correct: `CultureMech:009094`, `TOGO:M2524`, the
maintained owner stem, and the generated merge fingerprint all denote Chopped
Meat Medium with the DSMZ Medium 78 agar, Haemin, and Vitamin K1 additions.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID,
TOGO M2524 source ID, maintained owner stem, and merge fingerprint found only
this generated record, its maintained owner, and normalized index entries.

## Evidence

TOGO M2524 and DSMZ Medium 78 support DSMZ Chopped Meat Medium with 15.0 g agar
per 1000.0 mL medium for agar slants, plus 10.00 mL Haemin solution and
10.00 mL Vitamin K1 solution added to 1000 mL medium after autoclaving. The
base medium uses 500.0 g fat-free meat, 1000.0 mL distilled water, 25.0 mL 1 N
NaOH, 30.0 g Casitone, 5.0 g yeast extract, 5.0 g `K2HPO4`, 1.0 mg resazurin,
0.5 g/L L-cysteine hydrochloride, pH 7.0, 100% N2 dispensing, and 121 C for
30 minutes autoclaving.

The Haemin solution is a separate stock made from 50 mg haemin dissolved in
1 mL 1 N NaOH and made up to 100 mL with distilled water. The Vitamin K1
solution is a separate stock made from 0.1 mL Vitamin K1 in 20 mL 95% ethanol.
Both stocks are filter sterilized and refrigerated.

The record correctly contains agar for this agar-slant variant, but it flattens
both stock recipes into final-medium ingredients. Haemin-stock water is merged
with base water into 1099 g/L, 1 mL Haemin-stock NaOH is a separate 1 g/L
parent ingredient, 50 mg haemin is recorded as 50 g/L, 20 mL ethanol as
20 g/L, and 0.1 mL Vitamin K1 as 0.1 g/L. The final 10 mL additions of Haemin
solution and Vitamin K1 solution are present only as empty `G_PER_L` solution
shells.

The source pH, 100% N2 condition, meat-filtrate preparation, 7 mL Hungate-tube
dispensing, post-autoclave stock addition, and stock filter-sterilization steps
are absent from the generated record.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this TOGO/DSMZ source record.

The recipe is incomplete until the base agar-slant medium, Haemin stock, and
Vitamin K1 stock are represented as separate stages or solutions with
source-faithful units and preparation steps.

## Findings

| Severity | Finding |
| --- | --- |
| Major | Haemin solution and Vitamin K1 solution internals are flattened into parent ingredients, while the two 10 mL stock additions remain as empty `G_PER_L` solution shells. **Owner:** `data/normalized_yaml/bacterial/chopped_meat_medium_add_vitamin_k1_and_agar.yaml` or solution migration. |
| Major | Source millilitre and milligram quantities are converted to `G_PER_L`, affecting base water, 1 N NaOH, resazurin, both stock additions, Haemin-stock water and NaOH, haemin, 95% ethanol, and Vitamin K1. **Owner:** the TOGO/DSMZ unit-conversion importer. |
| Major | pH 7.0 and the DSMZ preparation workflow are missing, including the meat-filtrate stage, 100% N2 dispensing, 121 C autoclaving, post-autoclave stock addition, and stock filter sterilization. **Owner:** the maintained normalized owner or the TOGO/DSMZ importer. |

## Recommended Edits

1. Keep Haemin solution and Vitamin K1 solution as separate stock solutions and
   add only 10.00 mL of each stock to the final agar-slant medium after
   autoclaving.
2. Preserve source volume and mass units for liquid and milligram quantities.
3. Add pH 7.0 and preparation steps for the base agar-slant medium, the
   post-autoclave Haemin and Vitamin K1 additions, and both filter-sterilized
   stocks.
4. Regenerate merged YAML after repairing the maintained owner or importer.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated record against TOGO M2524 and DSMZ Medium
78 to confirm the base agar-slant medium, Haemin stock, Vitamin K1 stock,
source units, pH, and post-autoclave addition sequence are source-faithful.

## Additional Notes

None found.
