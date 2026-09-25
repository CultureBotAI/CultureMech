# YAML Record Review: Chopped Meat Medium With Carbohydrates

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__05390fed.yaml
- Started UTC: 2026-09-22T08:24:15Z
- Finished UTC: 2026-09-22T08:25:29Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009107 |
| Label | Chopped Meat Medium With Carbohydrates |
| Generated record | data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__05390fed.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M2537_Chopped_Meat_Medium_With_Carbohydrates.yaml |
| Source | TOGO Medium M2537, DSMZ Medium 110 |

The reviewed file is a generated one-source merge of TOGO M2537, which imports
DSMZ Medium 110. The generated merge differs from the maintained normalized
owner only by the merge-history event and the `merge_fingerprint` /
`merged_from` footer, so future fixes belong in the normalized owner or in the
TOGO/DSMZ importer and solution-migration logic rather than in the generated
merge artifact.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed; reported `No issues found` |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chopped_meat_medium_with_carbohydrates__05390fed.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The term validator emitted only the expected `eutils/pkg_resources is
deprecated` warning before passing.

## Identity and Grounding

The source identity is coherent: `CultureMech:009107`, `TOGO:M2537`, the DSMZ
Medium 110 PDF token, the maintained owner, and the generated merge
fingerprint all denote one TOGO import of DSMZ Chopped Meat Medium with
Carbohydrates.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml`, `data/merge_yaml/merged`, the registry and catalog
TSVs, and `data/import_tracking/reports` for the CultureMech ID, TOGO M2537
ID, DSMZ Medium 110 PDF token, maintained owner stem, and merge fingerprint
found this generated record, its maintained owner, same-family DSMZ Medium 110
variants, normalized indexes, and diagnostic registry or import-tracking rows.

The record represents DSMZ Medium 110's optional agar-slant and Haemin/Vitamin
K branches as unconditional parts of this parent medium.

## Evidence

The inspected DSMZ Medium 110 PDF and TOGO M2537 JSON support a base
chopped-meat medium made with 500 g fat-free ground beef, 1000 mL distilled
water, 25 mL 1 N NaOH, 30 g Casitone, 5 g yeast extract, 5 g `K2HPO4`,
0.5 mL 0.1% Na-resazurin solution, 4 g D-glucose, 1 g cellobiose, 1 g
maltose, 1 g soluble starch, 0.5 g/L L-cysteine hydrochloride, pH 7.0, and
100% N2 handling.

The source preparation boils the meat, water, and NaOH, cools and skims the
extract, filters while retaining meat particles and filtrate, restores the
filtrate to 1000 mL, adds the salts, peptides, sugars, and Na-resazurin
solution, boils and cools under 100% N2, then dispenses 7 mL medium into
Hungate tubes with optional meat particles and autoclaves at 121 C for 30
minutes. The source says to use 15 g agar per 1000 mL only for agar slants.

DSMZ Medium 110 further states that Haemin and either Vitamin K1 or Vitamin K3
are needed only in catalogue-indicated cases, with 10 mL stock solution added
to 1000 mL of medium after autoclaving. The record instead models the Haemin
solution, Vitamin K3 solution, 15 g agar, and all of the stock internals as
unconditional parent ingredients.

The nested stock scopes are also flattened. Base water, Haemin-stock water,
and Vitamin K3-stock water are merged into a 1198 g/L parent water ingredient;
the 10 mL Haemin and Vitamin K3 stock additions are empty `G_PER_L` solution
shells; 25 mL 1 N NaOH, 1 mL Haemin-stock NaOH, 50 mg haemin, 1 mL 95%
ethanol, and 5 mg Vitamin K3 are all asserted as parent `G_PER_L`
ingredients.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this TOGO/DSMZ source record.

The record is incomplete until DSMZ Medium 110's base medium, optional
agar-slant branch, Haemin stock, and Vitamin K3 stock are modeled as separate
recipe scopes with source-faithful millilitre and milligram units, pH, 100% N2
handling, and the meat-filtrate preparation sequence.

## Findings

| Severity | Finding |
| --- | --- |
| Major | The conditional agar-slant branch and the conditional Haemin/Vitamin K branch are represented as unconditional parent-medium ingredients and stock additions. **Owner:** `data/normalized_yaml/bacterial/TOGO_M2537_Chopped_Meat_Medium_With_Carbohydrates.yaml` or the TOGO/DSMZ importer. |
| Major | Haemin solution and Vitamin K3 solution are flattened into parent ingredients while their 10 mL post-autoclave additions remain as empty `G_PER_L` solution shells. **Owner:** the maintained normalized owner or solution migration. |
| Major | Source volumes and milligram quantities are converted to parent `G_PER_L`, affecting 25 mL 1 N NaOH, 0.5 mL Na-resazurin, 50 mg haemin, 1 mL 95% ethanol, and 5 mg Vitamin K3. **Owner:** the TOGO/DSMZ unit-conversion importer. |
| Major | Water from three scopes is merged into one 1198 g/L parent ingredient, erasing the 1000 mL base medium volume and the 99 mL water quantities in the two stocks. **Owner:** duplicate merging plus solution migration. |
| Major | The source pH, 100% N2 handling, meat-filtrate workflow, Hungate-tube dispensing, 121 C autoclaving, post-autoclave stock additions, and stock filter-sterilization steps are not represented as preparation steps. **Owner:** the maintained normalized owner or TOGO/DSMZ importer. |

## Recommended Edits

1. Keep DSMZ 110 base medium, agar-slant agar, Haemin solution, and Vitamin K3
   solution in separate scopes; do not treat optional agar or optional
   Haemin/Vitamin K as unconditional final ingredients.
2. Restore source volume and mass units for water, 1 N NaOH, Na-resazurin
   solution, Haemin stock, and Vitamin K3 stock.
3. Add pH 7.0 and preparation steps for the meat-filtrate base medium, 100% N2
   handling, 121 C autoclaving, optional post-autoclave stock additions, and
   filter-sterilized stocks.
4. Regenerate merged YAML after repairing the maintained owner or importer.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated record against TOGO M2537 and DSMZ
Medium 110 to confirm that base-medium units, optional branches, solution
boundaries, pH, N2 handling, and preparation order are source-faithful.

## Additional Notes

None found.
