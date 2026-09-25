# YAML Record Review: CYCLONATRONUM PROTEIVORANS MEDIUM (OMEGA)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/cyclonatronum_proteivorans_medium_omega.yaml
- Started UTC: 2026-09-22T12:48:31Z
- Finished UTC: 2026-09-22T12:50:50Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:000959 |
| Name | cyclonatronum_proteivorans_medium_omega |
| Source | DSMZ / MediaDive medium 1491 |
| Media term | mediadive.medium:1491, DSMZ Medium 1491 |
| Generated record | data/merge_yaml/merged/cyclonatronum_proteivorans_medium_omega.yaml |
| Maintained input | data/normalized_yaml/bacterial/cyclonatronum_proteivorans_medium_omega.yaml |

The merged record is a single-source generated copy of the normalized
DSMZ / MediaDive import. Future repairs belong in the normalized input or in
the MediaDive solution import and merge logic that flattened nested stock
solutions into final-medium ingredient rows.

## Validation

| Check | Result |
|---|---|
| LinkML open-schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/cyclonatronum_proteivorans_medium_omega.yaml` | Passed |
| Closed-schema validation, `python scripts/validate_strict.py data/merge_yaml/merged/cyclonatronum_proteivorans_medium_omega.yaml --out /private/tmp/cyclonatronum_proteivorans_medium_omega.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/cyclonatronum_proteivorans_medium_omega.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/cyclonatronum_proteivorans_medium_omega.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history validation | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML |

The passing validators prove that the generated YAML is schema-shaped. They do
not prove that the stock-solution graph and final-medium arithmetic match DSMZ
Medium 1491.

## Identity and Grounding

The record identity is correct. `CultureMech:000959` denotes DSMZ / MediaDive
medium `1491`, "CYCLONATRONUM PROTEIVORANS MEDIUM (OMEGA)", and the live
MediaDive REST endpoint gives the same ID, title, DSMZ PDF link, and pH range
10.0-10.1.

A gitignore-independent search with `rg --no-ignore --hidden` over
`data/normalized_yaml`, `data/raw`, and the generated target found one
normalized MediaRecipe with `mediadive.medium:1491`, this generated record, and
no exact raw capture for `mediadive.medium:1491` or `DSMZ_Medium1491` under
`data/raw`.

Most small-molecule groundings are plausible. One grounding should be reviewed:
`NiCl2 x 6 H2O` is grounded to `CHEBI:34887` with label `nickel dichloride`,
but the source chemical is the hexahydrate, not anhydrous nickel chloride.

## Evidence

DSMZ and the live MediaDive REST export support a three-part formulation:

| Source component | Source amount | Record amount |
|---|---:|---:|
| Na2CO3 | 5 g/L | 5 g/L |
| NaCl | 10 g/L | 10 g/L |
| K2HPO4 | 1 g/L | 1 g/L |
| Trace element solution | 1 ml/L | flattened as stock constituents |
| Distilled water, main solution | 1000 ml/L | missing |
| Yeast extract | 20 mg/L | 0.02 g/L |
| Peptone | 2 g/L | 2 g/L |
| Vitamin mix | 1 ml/L | flattened as stock constituents |

The generated record is correct for the direct final-medium salts, yeast
extract, and peptone. It is not correct for the two nested stock solutions.
MediaDive solution `3027` is a one-liter trace element stock added to the final
medium at 1 ml/L. The generated record instead lists that stock's EDTA,
FeSO4 x 7 H2O, ZnSO4, MnCl2, H3BO3, CoCl2 x 6 H2O, CuCl2 x 5 H2O,
NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O rows directly in the final medium at raw
stock concentrations.

The vitamin solution has the same structural defect. DSMZ defines four
100 ml vitamin stocks and says to mix them 1:1:1:1 immediately before addition
or add each at 1 ml/L. The generated record flattens the thiamin, calcium
pantothenate, biotin, PABA, nicotinic acid, pyridoxine, folic acid, riboflavin,
and B12 stock concentrations into final-medium `G_PER_L` rows.

## Completeness

- The record has no structured `references`, `source_data`,
  `target_organisms`, or `growth_metrics`. Empty target-organism and
  growth-metric slots are acceptable because DSMZ Medium 1491 is a recipe
  record, not a primary growth assay.
- The missing structured Trace element solution and Vitamin mix references are
  consequential because the current top-level rows erase the difference between
  final-medium salts and stock-solution ingredients.
- The generated output omits the distilled-water rows from both the main
  solution and the trace-element stock.
- The generated preparation steps are copied from the final medium, trace
  stock, and vitamin stock as one flat list, so a reader cannot tell which pH,
  autoclave, filtration, and mixing instructions belong to which stock.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Trace element solution `3027` was flattened into final-medium top-level ingredients. | The parent medium uses 1 ml/L of the trace stock; the generated YAML records the trace stock's raw g/L rows directly under the final medium. | `data/normalized_yaml/bacterial/cyclonatronum_proteivorans_medium_omega.yaml` and MediaDive solution import/merge logic |
| major | Vitamin mix `3031` was flattened into final-medium top-level ingredients. | DSMZ uses four 100 ml vitamin stocks added as a mixed or separate 1 ml/L supplement; the generated YAML records the vitamin stock strengths as final g/L values. | `data/normalized_yaml/bacterial/cyclonatronum_proteivorans_medium_omega.yaml` and MediaDive solution import/merge logic |
| major | Required distilled-water rows are missing. | DSMZ and MediaDive include 1000 ml distilled water in the main solution and the trace element stock; neither row appears in the generated record. | MediaDive importer and normalized solution handling |
| minor | The nickel salt grounding is underspecified. | The source row is `NiCl2 x 6 H2O`, but the record grounds it to `CHEBI:34887`, nickel dichloride, without the hexahydrate scope. | Ingredient grounding for DSMZ/MediaDive medium 1491 |
| minor | The generated recipe has only generic source provenance. | The DSMZ PDF URL is present in `notes`, but there is no structured `references` or `source_data` entry for the MediaDive REST endpoint or DSMZ PDF. | `data/normalized_yaml/bacterial/cyclonatronum_proteivorans_medium_omega.yaml` |

## Recommended Edits

1. Repair the MediaDive solution importer or this normalized input so DSMZ
   trace element solution `3027` remains a nested one-liter stock added at
   1 ml/L, including its 1000 ml distilled-water row.
2. Preserve the Pfennig and Lippert vitamin mix as four 100 ml stock solutions
   plus the source instruction to mix them or add each at 1 ml/L; do not flatten
   their stock strengths into final-medium ingredient rows.
3. Restore the main 1000 ml distilled-water row and keep the final-medium pH
   range at 10.0-10.1.
4. Review and, if needed, replace the `NiCl2 x 6 H2O` ChEBI grounding with a
   hexahydrate-specific term.
5. Add structured source provenance for the DSMZ Medium 1491 PDF and MediaDive
   medium 1491 REST endpoint.
6. Regenerate `data/merge_yaml/merged/cyclonatronum_proteivorans_medium_omega.yaml`
   after repairing the maintained input.

## Follow-up Checks

- Re-run open-schema, closed-schema, reference, and term validation on the
  repaired normalized input and regenerated merged record.
- Diff the regenerated record against DSMZ Medium 1491 and the live MediaDive
  medium 1491 response, checking main-solution ingredients, nested stock
  volumes, pH, and all preparation steps.
- Verify that trace and vitamin stock rows are not interpreted as final g/L
  concentrations unless they are dimensionally back-calculated from the source
  stock and addition volumes.
- Re-run `rg --no-ignore --hidden` for `mediadive.medium:1491` and
  `DSMZ_Medium1491` across `data/normalized_yaml` and `data/raw` to confirm
  that no stale flattened copy remains.

## Additional Notes

- The spelling `Pepton` in the DSMZ PDF and `Peptone` in MediaDive appear to
  refer to the same 2 g final-medium row.
- The flattened vitamin rows look like the concentrations inside the combined
  400 ml vitamin mix, not final-medium concentrations after a 1 ml/L addition.
