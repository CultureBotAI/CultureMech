# YAML Record Review: chopped_meat_medium_with_carbohydrates

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__8ad0d89d.yaml`
- Started UTC: 2026-09-22T08:36:31Z
- Finished UTC: 2026-09-22T08:39:00Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__8ad0d89d.yaml` |
| Stable ID | `CultureMech:009295` |
| Label | `chopped_meat_medium_with_carbohydrates` |
| Source term | `TOGO:M2744` |
| Source document | `DSMZ_Medium110.pdf` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M2744_Chopped_Meat_Medium_With_Carbohydrates.yaml` |
| Merge status | Generated from one source recipe, `TOGO_M2744_Chopped_Meat_Medium_With_Carbohydrates` |

The maintained owner carries the same scientific content as the generated
record before the generated merge footer, so future fixes belong in
`data/normalized_yaml/bacterial/TOGO_M2744_Chopped_Meat_Medium_With_Carbohydrates.yaml`
or in the TOGO importer that flattens stock components into parent media.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Pass; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__8ad0d89d.yaml` exited 0. |
| Strict schema | Pass; `scripts/validate_strict.py data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__8ad0d89d.yaml --out /private/tmp/chopped_meat_medium_with_carbohydrates__8ad0d89d.strict.tsv --workers 1 --quiet` scanned one file and emitted zero error rows. |
| Reference validation | Pass with no semantic coverage; `linkml-reference-validator validate data data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__8ad0d89d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported zero total checks because the record has no structured evidence references. |
| Term validation | Pass; `linkml-term-validator validate-data data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__8ad0d89d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` completed successfully, aside from the expected `eutils` `pkg_resources` deprecation warning. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries. |

`just` wrappers were not used because the project environment attempts to build
`llvmlite==0.46.0` under Python 3.13 and fails before the focused validators
can run. The checks above ran the same validator entry points in an offline
Python 3.11 `uv` environment.

## Identity and Grounding

The record is a TOGO rendering of DSMZ Medium 110 with the catalogue-dependent
Haemin and Vitamin K1 supplements. TOGO `M2744` and the inspected DSMZ Medium
110 PDF agree on the medium name, pH 7.0, the base Chopped Meat Medium With
Carbohydrates formulation, and a post-autoclave branch that adds 10 ml Haemin
solution plus 10 ml Vitamin K1 solution to 1000 ml of medium.

That branch is distinct from the Vitamin K3 branch and from the base DSMZ 110
recipe without Haemin or vitamin K. The identity therefore should remain a
variant of DSMZ 110, not a merge into a generic record that contains both K1
and K3 stock chemistries simultaneously.

## Evidence

Supported by the inspected TOGO `M2744` API payload and the DSMZ Medium 110 PDF:

- The basal recipe contains 500 g fat-free ground beef, 1000 ml distilled
  water, 25 ml of 1 N NaOH, 30 g Casitone, 5 g yeast extract, 5 g K2HPO4,
  0.5 ml Na-resazurin solution at 0.1% w/v, 4 g D-glucose, and 1 g each of
  cellobiose, maltose, and soluble starch.
- The recipe is made anoxic by boiling and cooling under 100% N2, then adding
  0.5 g/l L-cysteine hydrochloride and adjusting to pH 7.0 before dispensing
  under the same atmosphere and autoclaving at 121 C for 30 min.
- The K1 branch adds 10 ml Haemin solution and 10 ml Vitamin K1 solution after
  autoclaving.
- The Haemin stock is made from 50 mg haemin plus 1 ml of 1 N NaOH, brought to
  100 ml with distilled water, filter-sterilized, and stored refrigerated.
- The Vitamin K1 stock is made by dissolving 0.1 ml vitamin K1 in 20 ml
  95% ethanol, then filter-sterilizing and storing the stock refrigerated in a
  brown bottle.

Unsupported or under-scoped in the current record:

- The parent recipe lists Haemin-stock internals as parent ingredients:
  `1N NaOH` at `1 G_PER_L`, `haemin` at `50 G_PER_L`, and the Haemin-stock
  water merged into the base `Distilled water` amount.
- The parent recipe lists Vitamin-K1-stock internals as parent ingredients:
  `95% ethanol` at `20 G_PER_L` and `vitamin K1` at `0.1 G_PER_L`.
- `Haemin solution` and `Vitamin K1 solution` are represented as empty
  unknown solutions at `10 G_PER_L`; DSMZ specifies 10 ml additions of each
  stock to the autoclaved medium.
- The same base import issues from TOGO `M2743` remain: 1000 ml distilled water,
  25 ml 1 N NaOH, and 0.5 ml Na-resazurin stock are concentration-like
  ingredients; N2 is a variable ingredient; and every preparation step is
  absent.

## Completeness

The record has enough ingredient labels to reveal that it is the Haemin plus
Vitamin K1 branch, but it is not complete enough to execute safely. It erases
the stock boundaries, collapses the 100 ml Haemin stock water into the parent
medium, loses the 10 ml final stock addition units, and omits the source's
post-autoclave timing for both supplements.

The omission of the Vitamin K3 stock is correct for this record because M2744
is the Vitamin K1 branch. The omission of agar as a parent ingredient is also
acceptable because DSMZ lists agar only for agar slants.

An ignored-inclusive `rg --no-ignore --hidden` search over
`data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and
`reports` for exact `CultureMech:009295`, `TOGO:M2744`, `M2744`, the
`8ad0d89d7c96e593622dfd1bcadd73fad8db5ff22260418a5592d2f57f945062`
fingerprint, and the `TOGO_M2744_Chopped_Meat_Medium_With_Carbohydrates` stem
found this single owner plus its generated product, indexes, and review
manifests. It did not find a second owner for exact TOGO `M2744`.

Empty `target_organisms` and growth-evidence slots are acceptable here because
DSMZ Medium 110 is a source recipe, and the catalogue-dependent Haemin/K1
branch is not tied to a specific organism in this TOGO record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Haemin and Vitamin K1 stock internals are flattened into the parent medium. | DSMZ says to add 10 ml Haemin solution and 10 ml Vitamin K1 solution after autoclaving; the 50 mg haemin, 1 ml 1 N NaOH, 100 ml Haemin-stock water, 0.1 ml vitamin K1, and 20 ml ethanol are stock recipes, not parent-medium additions. | `data/normalized_yaml/bacterial/TOGO_M2744_Chopped_Meat_Medium_With_Carbohydrates.yaml` and, if systematic, the TOGO importer for subcomponents. |
| Major | Stock and preparation volumes are represented as `G_PER_L` concentrations. | DSMZ specifies 10 ml final Haemin stock, 10 ml final K1 stock, 25 ml base 1 N NaOH, and 0.5 ml Na-resazurin stock; the YAML records those volumes as gram-per-liter quantities or empty `solutions`. | `data/normalized_yaml/bacterial/TOGO_M2744_Chopped_Meat_Medium_With_Carbohydrates.yaml`. |
| Major | The source preparation workflow, pH, and post-autoclave supplement timing are missing. | DSMZ defines the meat infusion, 1000 ml final makeup, anoxic 100% N2 workflow, pH 7.0 adjustment, Hungate-tube dispensing, 121 C for 30 min autoclaving, and only then the Haemin/K1 additions. | `data/normalized_yaml/bacterial/TOGO_M2744_Chopped_Meat_Medium_With_Carbohydrates.yaml`. |
| Major | Nitrogen gas is modeled as a variable ingredient rather than the exact gas atmosphere. | DSMZ scopes nitrogen to cooling and dispensing under 100% N2; TOGO preserves that 100% value, but the YAML defaulted it to `VARIABLE`. | `data/normalized_yaml/bacterial/TOGO_M2744_Chopped_Meat_Medium_With_Carbohydrates.yaml`. |
| Minor | The L-cysteine ingredient still carries a legacy `mediaingredientmech_term` link and no CHEBI term. | The source ingredient is L-cysteine hydrochloride at 0.5 g/l; the ingredient label is retained, but the June 2026 MIM migration did not replace this legacy link. | `data/normalized_yaml/bacterial/TOGO_M2744_Chopped_Meat_Medium_With_Carbohydrates.yaml`. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M2744_Chopped_Meat_Medium_With_Carbohydrates.yaml`,
   separate the parent DSMZ 110 medium from the Haemin stock and Vitamin K1
   stock. Keep only 10 ml final additions of each stock in the parent branch.
2. Move 50 mg haemin, 1 ml 1 N NaOH, and the 100 ml final Haemin-stock volume
   into a Haemin solution recipe with filter sterilization and refrigerated
   storage.
3. Move 0.1 ml vitamin K1 and 20 ml 95% ethanol into a Vitamin K1 solution
   recipe with filter sterilization and brown-bottle refrigerated storage.
4. Correct the base DSMZ 110 quantities inherited by this branch: 1000 ml
   distilled water, 25 ml 1 N NaOH, 0.5 ml 0.1% w/v Na-resazurin solution, and
   100% N2 as an atmosphere rather than a variable ingredient.
5. Restore the DSMZ preparation sequence and explicitly place the 10 ml Haemin
   and 10 ml Vitamin K1 stock additions after autoclaving.
6. Re-resolve `L-cysteine hydrochloride` through the packaged
   MediaIngredientMech label index so the ingredient has a current exact
   CHEBI-backed link or an explicit unresolved note.

## Follow-up Checks

- Run focused open-schema, strict, reference, and term validation on the edited
  TOGO M2744 normalized record and any stock solution records used by it.
- Re-run `just verify-merges` and `just audit-merge-freshness` after
  regenerating merged YAML.
- Re-read the regenerated generated record against DSMZ Medium 110 and confirm
  that the M2744 K1 branch has no Vitamin K3 stock internals and no agar slant
  material in the base ingredient list.
- Compare the regenerated M2744 branch with the base M2743 and Vitamin K3
  branches to ensure only the intended post-autoclave stock differs.

## Additional Notes

- `data/import_tracking/reports/merged_duplicates.tsv` already flags the
  `Distilled water` value as a sum of two differing parts, `1000.0` and
  `100.0`. That 100 ml component is the Haemin stock final volume and should
  not be merged into the parent medium.
- The existing `mediadive.solution:1628` and `mediadive.solution:2227` terms on
  the two stock placeholders are useful leads, but their YAML nodes remain
  empty and still carry the wrong `G_PER_L` unit.
