# YAML Record Review: ARTFICIAL FRESHWATER MEDIUM I

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml
- Started UTC: 2026-09-21T14:41:50Z
- Finished UTC: 2026-09-21T14:43:31Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:002297` |
| Generated record | `data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml` |
| Merge input | `artficial_freshwater_medium_i` |
| Name | `artficial_freshwater_medium_i` |
| Original/source label | `ARTFICIAL FRESHWATER MEDIUM I` |
| Source grounding | JCM Medium J1124, `mediadive.medium:J1124` |

The generated merge has one normalized source recipe. Future curation belongs
in `data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml`; the
misspellings `ARTFICIAL` and `artficial` are inherited from the JCM source.

## Validation

| Check | Result |
|---|---|
| Open-schema LinkML validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml` returned `No issues found`. |
| Strict validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml --out /private/tmp/artficial_freshwater_medium_i.strict.tsv --workers 1 --quiet` scanned one file and reported `total ERROR rows: 0`. |
| Reference validation | Pass with no reference checks. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported one file validated, zero checks, and all validations passed. |
| Term validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_I.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` reported `Validation passed` after the known `eutils/pkg_resources` warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/*.yaml` records, not a focused validator for `MediaRecipe.curation_history` arrays embedded in one generated merge. |
| JCM source retrieval | Pass. JCM Medium 1124 and linked JCM Medium 187, 403, and 431 HTML pages were fetched and inspected. |

The documented `just` entrypoints are currently blocked by the project
environment's Python 3.13 / `llvmlite==0.46.0` build failure, so the review used
the same focused validators through the Python 3.11 no-project workaround.

## Identity and Grounding

The record points to the intended source. The generated YAML declares
`CultureMech:002297`, `mediadive.medium:J1124`, and
`ARTFICIAL FRESHWATER MEDIUM I`; the inspected JCM page is medium 1124 with the
same misspelled title. An ignored-inclusive exact search found the ID, owner
path, catalog row, and normalized indexes for this exact record, while also
showing adjacent sibling records for `artficial_freshwater_medium_ii` that are
not part of this review.

Most base-salt identities are exact, but `NiCl2 x 6 H2O` is grounded to
anhydrous nickel dichloride (`CHEBI:34887`). The JCM 187 Trace element solution
uses the hexahydrate, and the packaged MIM label index includes a
hydrate-specific mapping to `CHEBI:53542`.

## Evidence

Supported by the inspected JCM 1124 page:

- JCM Medium 1124 is `ARTFICIAL FRESHWATER MEDIUM I`.
- The base mix lists `KH2PO4`, `NH4Cl`, `KCl`, `NaCl`, `Na2SO4`, `Resazurin`,
  three stock additions by reference, and `Distilled water 960.0 ml`.
- After autoclaving under `N2-CO2 (4:1, v/v)`, JCM adds `8% NaHCO3`,
  `1 M MgCl2 x 6H2O`, `1 M CaCl2 x 2H2O`, Vitamin solution, Thiamine
  solution, Vitamin B12 solution, and `1 M Fructose` as milliliter aliquots.
- Before use, JCM adds `5% Na2S x 9H2O` as a 5 ml reducing-solution aliquot.

Supported by linked JCM stock pages:

- JCM 187 defines the FeCl2 and Trace element solution recipes referenced by
  JCM 1124.
- JCM 431 defines a Selenite-tungstate solution recipe matching the selenium
  and tungsten rows imported here.
- JCM 403 defines the Vitamin, Thiamine, and Vitamin B12 solutions referenced
  by JCM 1124.

Unsupported in the YAML:

- The five base grams and resazurin were scaled by the final sum of source
  volumes instead of being retained as source-stated recipe amounts.
- `NaHCO3`, `MgCl2 x 6 H2O`, `CaCl2 x 2 H2O`, `Fructose`, and
  `Na2S x 9 H2O` are stored as direct `G_PER_L` rows even though JCM gives
  milliliter aliquots of named stock solutions.
- The FeCl2, Trace element, and Selenite-tungstate stock recipes are flattened
  into direct final-medium ingredients.
- The Vitamin, Thiamine, and Vitamin B12 solutions are present only as empty
  `solutions` entries named `Unknown solution`, each with `1 G_PER_L` instead
  of the source's `1.0 ml` amount.

## Completeness

The record is structurally valid but is not complete enough to reproduce the
JCM recipe. The source's stock-solution topology is lost: three linked stocks
were flattened into direct ingredients, three linked vitamin stocks were
migrated to empty stubs, and five target-page solution additions were converted
from `ml` aliquots to unsupported `G_PER_L` ingredients.

An ignored-inclusive exact search found this record in
`data/import_tracking/reports/concentration_plausibility.tsv` for
`FeCl2 x 4 H2O` at stock magnitude. `find` over the ignored report directory
found no prior `*ARTFICIAL_FRESHWATER_MEDIUM_I.md` report before this one was
written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The import flattened multiple stock additions and linked stock definitions into direct final-medium ingredients. | JCM 1124 uses milliliter additions of FeCl2 solution, Trace element solution, Selenite-tungstate solution, `8% NaHCO3`, `1 M MgCl2 x 6H2O`, `1 M CaCl2 x 2H2O`, `1 M Fructose`, and `5% Na2S x 9H2O`; the YAML stores stock contents and aliquots as `G_PER_L` ingredient rows. | `data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml` |
| Major | Three JCM 403 vitamin stocks are empty `Unknown solution` stubs with the wrong unit. | JCM 1124 lists Vitamin solution, Thiamine solution, and Vitamin B12 solution at `1.0 ml` each and links them to JCM 403; the YAML has three empty `solutions` with `name: Unknown solution` and `unit: G_PER_L`. | `data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml` |
| Major | The base-medium amounts were rescaled from the source recipe instead of preserved. | JCM lists `0.2 g` `KH2PO4`, `0.25 g` `NH4Cl`, `0.3 g` `KCl`, `5.0 g` `NaCl`, `1.4 g` `Na2SO4`, and `1.0 mg` resazurin before the stock additions; the YAML stores each divided by the summed stock-volume denominator. | `data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml` |
| Major | `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride. | JCM 187 uses `NiCl2 x 6H2O`; the YAML row points to `CHEBI:34887` / nickel dichloride, while the packaged MIM label index includes `CHEBI:53542` for nickel chloride hexahydrate. | `data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml` |

No blockers: the YAML is valid and denotes the intended JCM 1124 medium.

No minor findings beyond the material stock-topology, arithmetic, and chemical
identity issues above.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/artficial_freshwater_medium_i.yaml`,
   restore JCM 1124's base medium amounts and keep `Distilled water 960 ml`
   separate from stock volumes.
2. Model FeCl2, Trace element, Selenite-tungstate, bicarbonate, magnesium
   chloride, calcium chloride, Vitamin, Thiamine, Vitamin B12, Fructose, and
   sulfide as stock additions with source-stated milliliter amounts.
3. Inline or link the JCM 187, 431, and 403 stock compositions under the
   appropriate solution records instead of storing their components as direct
   final-medium ingredients.
4. Re-ground `NiCl2 x 6 H2O` to the hexahydrate-specific CHEBI identity.
5. Attach a curation event and regenerate `data/merge_yaml/merged/` after the
   normalized owner is repaired.

## Follow-up Checks

- Re-run the focused schema, strict, term, and reference validators on the
  normalized owner and regenerated merged record.
- Run `just verify-merges` after regenerating merge outputs.
- Re-run the concentration-plausibility report or an exact ignored-inclusive
  `rg` over `data/import_tracking/reports/concentration_plausibility.tsv` to
  confirm `CultureMech:002297` no longer appears for stock-magnitude
  concentration rows.
- Manually inspect the regenerated `solutions` array to ensure all JCM 1124
  stock additions have `ML_PER_L`-style volumes and no `Unknown solution`
  placeholders.

## Additional Notes

The generated record is number 519 of 6286 in the case-folded
`data/merge_yaml/merged/*.yaml` review order used by this bulk pass.
