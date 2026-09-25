# YAML Record Review: PY + X MEDIUM (N2/CO2)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/py_x_medium_n2_co2__ef8eb2fc.yaml
- Started UTC: 2026-09-24T22:19:12Z
- Finished UTC: 2026-09-24T22:19:12Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:000476 |
| Name | py_x_medium_n2_co2 |
| Original name | PY + X MEDIUM (N2/CO2) |
| Category | bacterial |
| Generated file | data/merge_yaml/merged/py_x_medium_n2_co2__ef8eb2fc.yaml |
| Maintained owner | data/normalized_yaml/bacterial/py_x_medium_n2_co2.yaml |
| Merge source | py_x_medium_n2_co2 |
| Source grounding | mediadive.medium:104c, DSMZ_Medium104c.pdf |

The reviewed file is a generated merge product with one direct DSMZ/MediaDive
source. Future corrections should be made in
`data/normalized_yaml/bacterial/py_x_medium_n2_co2.yaml` or in the MediaDive
import path that initially flattened the nested salt solution.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/py_x_medium_n2_co2__ef8eb2fc.yaml` | Passed with `No issues found`. |
| Strict CultureMech validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/py_x_medium_n2_co2__ef8eb2fc.yaml --out /private/tmp/py_x_medium_n2_co2__ef8eb2fc.strict.tsv --workers 1 --quiet` | Passed with 0 strict errors; `/private/tmp/py_x_medium_n2_co2__ef8eb2fc.strict.tsv` contained 1 line including the header. |
| LinkML references | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/py_x_medium_n2_co2__ef8eb2fc.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file was validated and no reference checks were emitted. |
| LinkML terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/py_x_medium_n2_co2__ef8eb2fc.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only the known `eutils`/`pkg_resources` deprecation warning was printed. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

- `data/merge_yaml/merged/py_x_medium_n2_co2__ef8eb2fc.yaml` is the generated
  direct DSMZ/MediaDive branch for CultureMech:000476 and source medium 104c.
- The DSMZ source PDF title is `104c: PY + X MEDIUM (N2/CO2)`, matching the
  record label and `mediadive.medium:104c` grounding.
- This record is the DSMZ 104c / N2-CO2 variant, not the DSMZ 104b / 100
  percent N2 `PY + X Medium` base recipe.
- Exact ignored-file search across `data/**/*.yaml` for
  `mediadive.medium:104c`, `DSMZ_Medium104c`, `Source: DSMZ, ID: 104c`, and
  `py_x_medium_n2_co2` found the reviewed direct DSMZ branch and the equivalent
  TOGO M2750 branch. It did not show any other direct DSMZ 104c owner.
- Primary CHEBI and MediaIngredientMech CHEBI links agree for the grounded
  small molecules.

## Evidence

- DSMZ 104c supports the record's identity, pH 7.0, 5 g Trypticase peptone,
  5 g meat peptone, 10 g yeast extract, 0.5 g L-Cysteine-HCl x H2O, 1 g
  Na2CO3, 5 g D-glucose, and the captured 80 percent N2 / 20 percent CO2
  preparation paragraph.
- DSMZ 104c adds `Salt solution` at 40 ml per final liter and defines that
  stock as 0.25 g CaCl2 x 2 H2O, 0.50 g MgSO4 x 7 H2O, 1.00 g K2HPO4, 1.00 g
  KH2PO4, 10.00 g NaHCO3, and 2.00 g NaCl in 1000 ml distilled water. The
  reviewed record stores those stock recipe strengths directly as final-medium
  `G_PER_L` ingredients, so each salt is 25-fold too concentrated for the
  final PY + X N2/CO2 medium.
- The 0.0005 `G_PER_L` sodium resazurin row is consistent with converting
  0.50 ml of a 0.1 percent w/v stock into a final mass per liter, but the
  source represents resazurin as a stock aliquot.
- The DSMZ preparation paragraph was captured and preserves the post-autoclave
  glucose and carbonate stock-addition requirement.

## Completeness

- Empty optional fields beyond the core recipe are not defects.
- The record captures pH 7.0 and the source preparation step.
- The primary completeness gap is the missing solution structure for the
  40 ml salt stock. That gap is consequential because the imported record
  cannot distinguish the final medium from the salt-stock recipe.
- The source's final-volume context and 960 ml main-medium water row are
  absent. Those water values are part of the stock/final boundary that a future
  correction needs to preserve.
- Exact ignored-file search included ignored files before assessing duplicate
  and sibling records.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Salt-stock composition was flattened into final-medium concentrations. | DSMZ 104c adds 40 ml salt solution to the final liter, but the YAML exposes CaCl2 x 2 H2O 0.25 g/L, MgSO4 x 7 H2O 0.5 g/L, K2HPO4 1 g/L, KH2PO4 1 g/L, NaHCO3 10 g/L, and NaCl 2 g/L as direct ingredients. Those are stock recipe values, not final concentrations. | data/normalized_yaml/bacterial/py_x_medium_n2_co2.yaml; MediaDive import |
| Minor | The resazurin stock aliquot was collapsed to final mass concentration. | DSMZ 104c lists 0.50 ml of `Sodium resazurin (0.1% w/v)`, while the record keeps only `Sodium resazurin` at 0.0005 g/L. The conversion is consistent, but the 0.1 percent stock boundary is no longer represented. | data/normalized_yaml/bacterial/py_x_medium_n2_co2.yaml |
| Minor | The equivalent TOGO branch remains a separate generated record. | Exact ignored-file search found TOGO M2750 / `data/merge_yaml/merged/py_x_medium_n2_co2.yaml` for the same DSMZ 104c source. The different fingerprints come from import-shape differences rather than a documented medium distinction. | data/normalized_yaml/bacterial/py_x_medium_n2_co2.yaml; data/normalized_yaml/bacterial/TOGO_M2750_PY_X_Medium_N2_CO2.yaml; merge_recipes.py |

## Recommended Edits

1. Recurate `data/normalized_yaml/bacterial/py_x_medium_n2_co2.yaml` to model
   `Salt solution` as a 40 ml/L stock aliquot and move CaCl2 x 2 H2O, MgSO4 x
   7 H2O, K2HPO4, KH2PO4, NaHCO3, and NaCl under that stock's composition.
2. Preserve the final-volume scope, including the 960 ml main-medium water and
   1000 ml salt-stock water, so the stock and final medium do not share a flat
   ingredient namespace.
3. Represent the sodium resazurin 0.1 percent w/v solution as a stock aliquot
   if the schema can express it; otherwise add a note documenting that
   0.0005 g/L is the final conversion from 0.50 ml of a 1 g/L stock.
4. Regenerate the merged YAML and compare the result with the TOGO M2750 branch
   so the two DSMZ 104c imports merge or differ only by documented source
   distinctions.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on
  `data/merge_yaml/merged/py_x_medium_n2_co2__ef8eb2fc.yaml`.
- Manually confirm the regenerated record no longer exposes salt-stock recipe
  values as direct final-medium ingredient concentrations.
- Manually compare `py_x_medium_n2_co2__ef8eb2fc.yaml` against the fixed TOGO
  M2750 branch to confirm duplicate DSMZ 104c imports no longer diverge by
  stock-modeling artifacts.

## Additional Notes

- DSMZ gives several organism-specific replacements and pH variants after the
  base 104c recipe. Those notes were not reviewed as part of this base-medium
  record.
