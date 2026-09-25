# YAML Record Review: chopped_meat_medium_with_carbohydrates

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__960dd33a.yaml`
- Started UTC: 2026-09-22T08:39:01Z
- Finished UTC: 2026-09-22T08:41:10Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__960dd33a.yaml` |
| Stable ID | `CultureMech:009105` |
| Label | `chopped_meat_medium_with_carbohydrates` |
| Source term | `TOGO:M2535` |
| Source document | `DSMZ_Medium110.pdf` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M2535_Chopped_Meat_Medium_With_Carbohydrates.yaml` |
| Merge status | Generated from one source recipe, `TOGO_M2535_Chopped_Meat_Medium_With_Carbohydrates` |

The maintained owner carries the same scientific content as the generated
record before the generated merge footer, so future fixes belong in
`data/normalized_yaml/bacterial/TOGO_M2535_Chopped_Meat_Medium_With_Carbohydrates.yaml`
or in the TOGO importer that currently flattens stock components into parent
media.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Pass; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__960dd33a.yaml` reported `No issues found`. |
| Strict schema | Pass; `scripts/validate_strict.py data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__960dd33a.yaml --out /private/tmp/chopped_meat_medium_with_carbohydrates__960dd33a.strict.tsv --workers 1 --quiet` scanned one file and emitted zero error rows. |
| Reference validation | Pass with no semantic coverage; `linkml-reference-validator validate data data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__960dd33a.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported zero total checks because the record has no structured evidence references. |
| Term validation | Pass; `linkml-term-validator validate-data data/merge_yaml/merged/chopped_meat_medium_with_carbohydrates__960dd33a.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` completed successfully, aside from the expected `eutils` `pkg_resources` deprecation warning. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries. |

`just` wrappers were not used because the project environment attempts to build
`llvmlite==0.46.0` under Python 3.13 and fails before the focused validators
can run. The checks above ran the same validator entry points in an offline
Python 3.11 `uv` environment.

## Identity and Grounding

The record is a TOGO rendering of the DSMZ Medium 110 Vitamin K3 branch. TOGO
`M2535` and the inspected DSMZ Medium 110 PDF agree on the medium name, the
base Chopped Meat Medium With Carbohydrates recipe, and a post-autoclave branch
that adds 10 ml Haemin solution plus 10 ml Vitamin K3 solution to 1000 ml of
medium.

This identity is distinct from the base DSMZ 110 recipe, the Vitamin K1 branch,
and strain-specific pH or horse-serum variants. The record should remain a
variant of DSMZ 110 with only the Haemin plus Vitamin K3 additions.

## Evidence

Supported by the inspected TOGO `M2535` API payload and the DSMZ Medium 110 PDF:

- The basal recipe contains 500 g fat-free ground beef, 1000 ml distilled
  water, 25 ml of 1 N NaOH, 30 g Casitone, 5 g yeast extract, 5 g K2HPO4,
  0.5 ml Na-resazurin solution at 0.1% w/v, 4 g D-glucose, and 1 g each of
  cellobiose, maltose, and soluble starch.
- The recipe is made anoxic with 100% N2, 0.5 g/l L-cysteine hydrochloride,
  pH 7.0 adjustment, 7 ml Hungate-tube portions dispensed under the same gas,
  and 121 C for 30 min autoclaving.
- The K3 branch adds 10 ml Haemin solution and 10 ml Vitamin K3 solution after
  autoclaving.
- The Haemin stock is made from 50 mg haemin plus 1 ml of 1 N NaOH, brought to
  100 ml with distilled water, filter-sterilized, and stored refrigerated.
- The Vitamin K3 stock is first made at 5 mg/ml in 95% ethanol, diluted to
  0.05 mg/ml in water, filter-sterilized, and stored refrigerated in a brown
  bottle. TOGO represents that as 5 mg vitamin K3, 1 ml 95% ethanol, and
  99 ml water.

Unsupported or under-scoped in the current record:

- The parent recipe lists Haemin-stock internals as parent ingredients:
  `NaOH` at `1 G_PER_L`, `haemin` at `50 G_PER_L`, and 99 ml of Haemin-stock
  dilution water merged into the parent `Distilled water` amount.
- The parent recipe lists Vitamin-K3-stock internals as parent ingredients:
  99 ml water, 1 ml 95% ethanol, and 5 mg vitamin K3. The 99 ml K3 water is
  also merged into parent `Distilled water`.
- `Haemin solution` and `Vitamin K3 solution` are represented as empty unknown
  solutions at `10 G_PER_L`; DSMZ specifies 10 ml additions of each stock to
  the autoclaved medium.
- The same base import issues from TOGO `M2743` remain: 1000 ml distilled water,
  25 ml 1 N NaOH, and 0.5 ml Na-resazurin stock are concentration-like
  ingredients; N2 is a variable ingredient; pH 7.0 is absent; and every
  preparation step is absent.

## Completeness

The record has enough labels to identify the Haemin plus Vitamin K3 branch, but
not enough structure to reconstruct it. The final recipe, Haemin stock, and
Vitamin K3 stock are mixed into one parent ingredient list, source volumes are
stored as gram-per-liter concentrations, stock water is summed into parent
water, and the post-autoclave supplement timing is missing.

The omission of Vitamin K1 is correct for this K3-specific branch. The omission
of agar as a parent ingredient is also acceptable because DSMZ lists agar only
for agar slants.

An ignored-inclusive `rg --no-ignore --hidden` search over
`data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and
`reports` for exact `CultureMech:009105`, `TOGO:M2535`, `M2535`, the
`960dd33aeff233367271885f37bb6e8f3425f7f29c1f4f063246e4bc313f697d`
fingerprint, and the `TOGO_M2535_Chopped_Meat_Medium_With_Carbohydrates` stem
found this single owner plus its generated product, indexes, and review
manifests. It did not find a second owner for exact TOGO `M2535`.

Empty `target_organisms` and growth-evidence slots are acceptable here because
DSMZ Medium 110 is a source recipe, and this TOGO record does not tie the K3
branch to a tested strain.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Haemin and Vitamin K3 stock internals are flattened into the parent medium. | DSMZ says to add 10 ml Haemin solution and 10 ml Vitamin K3 solution after autoclaving; the 50 mg haemin, 1 ml 1 N NaOH, 99 ml Haemin-stock water, 5 mg K3, 1 ml ethanol, and 99 ml K3 dilution water are stock-internal materials. | `data/normalized_yaml/bacterial/TOGO_M2535_Chopped_Meat_Medium_With_Carbohydrates.yaml` and, if systematic, the TOGO importer for subcomponents. |
| Major | Stock and preparation volumes are represented as `G_PER_L` concentrations. | DSMZ specifies 10 ml final Haemin stock, 10 ml final K3 stock, 25 ml base 1 N NaOH, and 0.5 ml Na-resazurin stock; the YAML records those volumes as gram-per-liter quantities or empty `solutions`. | `data/normalized_yaml/bacterial/TOGO_M2535_Chopped_Meat_Medium_With_Carbohydrates.yaml`. |
| Major | The source preparation workflow, pH, and post-autoclave supplement timing are missing. | DSMZ defines the meat infusion, 1000 ml final makeup, anoxic 100% N2 workflow, pH 7.0 adjustment, Hungate-tube dispensing, 121 C for 30 min autoclaving, and only then the Haemin/K3 additions. | `data/normalized_yaml/bacterial/TOGO_M2535_Chopped_Meat_Medium_With_Carbohydrates.yaml`. |
| Major | Nitrogen gas is modeled as a variable ingredient rather than the exact gas atmosphere. | DSMZ scopes nitrogen to cooling and dispensing under 100% N2; TOGO preserves that 100% value, but the YAML defaulted it to `VARIABLE`. | `data/normalized_yaml/bacterial/TOGO_M2535_Chopped_Meat_Medium_With_Carbohydrates.yaml`. |
| Minor | The L-cysteine ingredient still carries a legacy `mediaingredientmech_term` link and no CHEBI term. | The source ingredient is L-cysteine hydrochloride at 0.5 g/l; the ingredient label is retained, but the June 2026 MIM migration did not replace this legacy link. | `data/normalized_yaml/bacterial/TOGO_M2535_Chopped_Meat_Medium_With_Carbohydrates.yaml`. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M2535_Chopped_Meat_Medium_With_Carbohydrates.yaml`,
   separate the parent DSMZ 110 medium from the Haemin stock and Vitamin K3
   stock. Keep only 10 ml final additions of each stock in the parent branch.
2. Move 50 mg haemin, 1 ml 1 N NaOH, and the 100 ml final Haemin-stock volume
   into a Haemin solution recipe with filter sterilization and refrigerated
   storage.
3. Move 5 mg vitamin K3, 1 ml 95% ethanol, and the 100 ml final diluted K3
   stock volume into a Vitamin K3 solution recipe with filter sterilization
   and brown-bottle refrigerated storage.
4. Correct the base DSMZ 110 quantities inherited by this branch: 1000 ml
   distilled water, 25 ml 1 N NaOH, 0.5 ml 0.1% w/v Na-resazurin solution, and
   100% N2 as an atmosphere rather than a variable ingredient.
5. Restore the DSMZ preparation sequence and explicitly place the 10 ml Haemin
   and 10 ml Vitamin K3 stock additions after autoclaving.
6. Re-resolve `L-cysteine hydrochloride` through the packaged
   MediaIngredientMech label index so the ingredient has a current exact
   CHEBI-backed link or an explicit unresolved note.

## Follow-up Checks

- Run focused open-schema, strict, reference, and term validation on the edited
  TOGO M2535 normalized record and any stock solution records used by it.
- Re-run `just verify-merges` and `just audit-merge-freshness` after
  regenerating merged YAML.
- Re-read the regenerated generated record against DSMZ Medium 110 and confirm
  that the M2535 K3 branch has no Vitamin K1 stock internals and no agar slant
  material in the base ingredient list.
- Compare the regenerated M2535 branch with the base, Vitamin K1, and other
  Vitamin K3 TOGO Medium 110 variants before deciding whether any exact
  duplicates should merge.

## Additional Notes

- `data/import_tracking/reports/merged_duplicates.tsv` already flags
  `Distilled water` as a sum of three differing parts, `1000.0`, `99.0`, and
  `99.0`. The two 99 ml components are stock dilution water amounts, not
  parent medium water.
- The TOGO source omits an explicit `ph` field for `M2535`, but the shared
  DSMZ Medium 110 source gives pH 7.0 for the completed base before the
  post-autoclave branch additions.
