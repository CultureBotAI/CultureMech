# YAML Record Review: msv_thiotrix_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/msv_thiotrix_medium.yaml
- Started UTC: 2026-09-24T15:35:40Z
- Finished UTC: 2026-09-24T15:37:21Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/msv_thiotrix_medium.yaml`.

The generated record is `CultureMech:006644` and keeps the KOMODO source copy as
canonical:

- `media_term`: `komodo.medium:841`
- `name`: `msv_thiotrix_medium`
- `original_name`: `MSV-THIOTRIX-MEDIUM`
- `physical_state`: `SOLID_AGAR`
- `ph_value`: 7.4
- `ingredients`: 20
- `merged_from`: `KOMODO_841_MSV-THIOTRIX-MEDIUM` and
  `msv_thiotrix_medium`

The maintained owners involved in the merge are:

- `data/normalized_yaml/bacterial/KOMODO_841_MSV-THIOTRIX-MEDIUM.yaml`
  with `id: CultureMech:006644` and `media_term: komodo.medium:841`.
- `data/normalized_yaml/bacterial/msv_thiotrix_medium.yaml` with
  `id: CultureMech:001997` and `media_term: mediadive.medium:841`.

## Validation

- Open schema validation: Passed; exited 0 with no diagnostics.
- Strict schema validation: Passed with 0 errors; the TSV contained only the
  header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked; `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The record has the right MSV-THIOTRIX-MEDIUM name, agar plate state, pH 7.4,
DSMZ 841 provenance, and exact KOMODO-to-MediaDive source-duplicate
relationship. The generated canonical owner is nevertheless the KOMODO copy;
the direct DSMZ/MediaDive owner is `CultureMech:001997`, carries
`mediadive.medium:841`, and now contains a nested `Standard vitamin solution`
that the generated YAML does not.

An exact ignored-file-inclusive search for `CultureMech:006644`,
`CultureMech:001997`, `komodo.medium:841`, and `mediadive.medium:841` found
only the two active normalized owners, their generated merge, and
registry/catalog entries in current `data/` scope.

Most ingredient strings are grounded to terms that match the imported chemical
labels. No over-broadened or legacy `mediaingredientmech_term` grounding was
found in this generated record.

## Evidence

MediaDive REST and HTML for medium 841 currently describe DSMZ
`MSV-THIOTRIX-MEDIUM` as pH 7.4. Its 1000 ml main solution contains 991 ml
`Solution I`, 8 ml `Solution II`, 1 ml `Solution III`, 0.1 ml `Solution IV`,
and 15 g/L agar.

The named solutions are stock or subsolution recipes:

- `Solution I`: 991 ml containing 0.5 g `(NH4)2SO4`, 0.1 g
  `MgSO4 x 7 H2O`, 0.05 g `CaCl2 x 2 H2O`, 0.11 g `K2HPO4`, 0.085 g
  `KH2PO4`, 2 mg `FeCl3 x 6 H2O`, 3 mg `Na2-EDTA`, 0.546 g
  `Na-acetate`, 0.4 g `Na2S2O3 x 5 H2O`, and 991 ml distilled water.
- `Solution II`: 50 ml containing 2.625 g `NaHCO3` and 50 ml distilled water,
  with 8 ml/L added to the main medium.
- `Solution III`: 1 ml `Standard vitamin solution`, with 1 ml/L added to the
  main medium.
- `Solution IV`: 10 ml containing 1 g `Inositol` and 10 ml distilled water,
  with 0.1 ml/L added to the main medium.
- `Standard vitamin solution`: a 100 ml vitamin stock with `Riboflavin`,
  `Thiamine-HCl x 2 H2O`, `Nicotinic acid`, `Pyridoxine hydrochloride`,
  `Calcium pantothenate`, `Biotin`, `Folic acid`, `Vitamin B12`, and
  distilled water.

The generated YAML predates the August 7 `apply_cocktail_nesting.py` repair in
both normalized owners, so it still places `Riboflavin`,
`Thiamine-HCl x 2 H2O`, `Nicotinic acid`, and `Pyridoxine hydrochloride` in
top-level final ingredients instead of inside a 1 ml/L `Standard vitamin
solution`. Even the newer normalized owners remain only partially repaired:
`Calcium pantothenate`, `Biotin`, `Folic acid`, and `Vitamin B12` are still
top-level stock-strength ingredients, and `NaHCO3` and `Inositol` still carry
their stock g/L values.

## Completeness

The generated record lists all non-water compounds from the DSMZ source, but it
is not complete enough to reproduce the medium because all four main
subsolution additions are flattened. It also drops the preparation steps that
survive on the DSMZ/MediaDive owner, including these source-level steps:

- Final pH approximately 7.4 should be controlled sterile.
- Autoclave Solution I for 20 min at 121 C.
- Add sterile Solution II shortly before inoculation.
- Filter sterilize the vitamin solution and add 1 ml/L medium.
- Filter sterilize Solution IV and add 0.1 ml/L medium.
- Filter sterilize Standard vitamin solution with a 0.2 um pore-size filter
  and store it at 4 C.

`target_organisms` and structured `references` are absent. They were not
treated as defects for this generated record because the source duplicate
merge and the imported MediaDive payload already encode the medium identity
and source URL.

## Findings

- The generated record is stale. It was merged on 2026-08-06, but both
  maintained owners were partially repaired on 2026-08-07 to move four
  Standard vitamin solution components under `solutions`.
- The merge chose `CultureMech:006644` / `komodo.medium:841` as canonical even
  though that record is a KOMODO source duplicate of DSMZ Medium 841. The
  direct DSMZ/MediaDive owner, `CultureMech:001997`, should carry the
  canonical `mediadive.medium:841` identity.
- The generated record flattens `Solution I` at stock g/L instead of preserving
  991 ml/L as the amount added to the 1000 ml final recipe. Each Solution I
  salt is therefore about 1.009x too concentrated; for example, `(NH4)2SO4`
  should be 0.5 g/L final, not 0.504541 g/L.
- `NaHCO3` is imported from the 52.5 g/L Solution II stock even though only
  8 ml/L is added to the final medium; the final concentration should be
  0.42 g/L, not 52.5 g/L.
- `Inositol` is imported from the 100 g/L Solution IV stock even though only
  0.1 ml/L is added to the final medium; the final concentration should be
  0.01 g/L, not 100 g/L.
- All eight Standard vitamin solution components are represented at stock
  strength in the generated record, 1000x above their final concentrations.
  The generated record has no 1 ml/L `Standard vitamin solution` edge.
- The `komodo-web-import` timestamp is malformed as
  `2026-01-27T01:15:03.fZ`, and the merged record inherits it.

## Recommended Edits

- Repair the maintained MediaDive owner and its KOMODO source duplicate, then
  regenerate `data/merge_yaml/merged/msv_thiotrix_medium.yaml`.
- Prefer `data/normalized_yaml/bacterial/msv_thiotrix_medium.yaml` as the
  canonical owner for DSMZ/MediaDive Medium 841 so the generated record keeps
  `CultureMech:001997`, `mediadive.medium:841`, and the DSMZ preparation
  steps.
- Preserve `Solution I`, `Solution II`, `Solution III`, `Solution IV`, and
  `Standard vitamin solution` as nested solutions if the schema can carry that
  hierarchy. If it cannot, scale their solutes into final g/L before
  generation.
- Extend the Standard vitamin solution repair to include `Calcium
  pantothenate`, `Biotin`, `Folic acid`, and `Vitamin B12`.
- Normalize the malformed KOMODO import timestamp to a valid UTC datetime.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the
  regenerated YAML.
- Confirm the regenerated record keeps `SOLID_AGAR`, 15 g/L agar, pH 7.4, and
  the DSMZ/MediaDive preparation steps.
- Confirm the regenerated final values are 0.5 g/L `(NH4)2SO4`, 0.1 g/L
  `MgSO4 x 7 H2O`, 0.05 g/L `CaCl2 x 2 H2O`, 0.11 g/L `K2HPO4`,
  0.085 g/L `KH2PO4`, 0.002 g/L `FeCl3 x 6 H2O`, 0.003 g/L `Na2-EDTA`,
  0.546 g/L `Na-acetate`, 0.4 g/L `Na2S2O3 x 5 H2O`, 0.42 g/L `NaHCO3`,
  and 0.01 g/L `Inositol`.
- Confirm the Standard vitamin solution is either present as a 1 ml/L nested
  solution or scaled by 0.001 into the final recipe.

## Additional Notes

The generated YAML and both source owners agree on the same local ingredient
signature before nesting repairs, so the KOMODO record appears to be a source
duplicate rather than an intentional DSMZ 841 variant.
