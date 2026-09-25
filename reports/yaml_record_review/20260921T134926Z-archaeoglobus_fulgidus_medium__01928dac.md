# YAML Record Review: Archaeoglobus Fulgidus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/archaeoglobus_fulgidus_medium__01928dac.yaml
- Started UTC: 2026-09-21T13:46:57Z
- Finished UTC: 2026-09-21T13:49:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008658 |
| Name | archaeoglobus_fulgidus_medium |
| Original name | Archaeoglobus Fulgidus Medium |
| Category | archaea |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| Source | TOGO:M206 / JCM_M213 |
| Maintained owner | data/normalized_yaml/archaea/TOGO_M206_Archaeoglobus_Fulgidus_Medium.yaml |
| Generated record | data/merge_yaml/merged/archaeoglobus_fulgidus_medium__01928dac.yaml |
| Merge fingerprint | 01928dac9a81d8ecaae5f125079ea83cfec7cb0bb257bd5445dcf6244e615ac2 |

The target is a generated one-source merge whose maintained input is
`data/normalized_yaml/archaea/TOGO_M206_Archaeoglobus_Fulgidus_Medium.yaml`.
The generated file matches that owner plus the 2026-08-06 `merge_recipes.py`
curation event, `merge_fingerprint`, and `merged_from` metadata. Any fix should
be made in the normalized TOGO_M206 owner or in the TOGO import logic and then
propagated by regenerating the merge.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/archaeoglobus_fulgidus_medium__01928dac.yaml` | Passed, `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/archaeoglobus_fulgidus_medium__01928dac.yaml --out /private/tmp/archaeoglobus_fulgidus_medium__01928dac.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/archaeoglobus_fulgidus_medium__01928dac.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 active checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/archaeoglobus_fulgidus_medium__01928dac.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed with the known `eutils` / `pkg_resources` warning. |
| Embedded curation history | Not checked: the repository exposes `just validate-history` for standalone files under `history/`; no focused embedded `MediaRecipe.curation_history` validator is documented for a single generated merge record. |

## Identity and Grounding

The generated record identifies the expected source recipe. `media_term.id`
is `TOGO:M206`, `media_term.label` is `Archaeoglobus Fulgidus Medium`, and the
record notes name JCM `JCM_M213`, whose current page is medium 213
`ARCHAEOGLOBUS FULGIDUS MEDIUM`.

An ignored-file-inclusive bounded search for
`CultureMech:008658|TOGO:M206([^0-9]|$)|TOGO_M206_Archaeoglobus_Fulgidus_Medium|archaeoglobus_fulgidus_medium__01928dac`
across `data/normalized_yaml`, `data/merge_yaml`,
`data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`,
`reports/media_content_review_manifest.tsv`,
`data/import_tracking/reports/concentration_plausibility.tsv`, and
`data/import_tracking/reports/merged_duplicates.tsv` found one normalized owner,
the generated merge, the registry/catalog/manifest/index rows, and one
concentration-plausibility finding for the same record. It did not find a
second maintained normalized record for `TOGO:M206` in the searched corpus.

The grounded simple ingredients match the source chemical labels at recipe
scale. Examples include water as `CHEBI:15377`, magnesium sulfate heptahydrate
as `CHEBI:31795`, sodium chloride as `CHEBI:26710`, calcium chloride dihydrate
as `CHEBI:86158`, ammonium chloride as `CHEBI:31206`, dipotassium hydrogen
phosphate as `CHEBI:131527`, resazurin as `CHEBI:8806`, magnesium chloride
hexahydrate as `CHEBI:86345`, sodium sulfide nonahydrate as `CHEBI:76209`,
potassium chloride as `CHEBI:32588`, sodium hydrogencarbonate as
`CHEBI:32139`, ferrous ammonium sulfate hexahydrate as `CHEBI:76181`, ammonium
nickel sulfate hexahydrate as `CHEBI:86149`, sodium L-lactate as
`CHEBI:232798`, sulfuric acid as `CHEBI:26836`, carbon dioxide as
`CHEBI:16526`, and dinitrogen as `CHEBI:17997`.

## Evidence

The inspected TOGO SPARQLIST response for `M206` agrees with the record's
`meta.name`, `original_media_id`, source URL, and source pH. It lists the same
core salts, sodium L-lactate, yeast extract, resazurin, sodium sulfide, 1 N
`H2SO4`, `Carbon dioxide gas`, and `Nitrogen gas`.

The inspected JCM medium 213 page agrees with the same formula and resolves the
TOGO cross-reference: TOGO `Trace minerals (see Medium [M142])` is the JCM
`Trace minerals (see Medium No. 151)` row at 10.0 ml. The corpus maps
`TOGO:M142` to `data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml`,
whose notes identify the original source as `JCM_M151`.

The record loses several source units while preserving the source numeric
values:

| Component | Source quantity | Record quantity |
|---|---:|---:|
| Distilled water | 990 ml | 990 `G_PER_L` |
| Resazurin | 1 mg | 1 `G_PER_L` |
| Fe(NH4)2(SO4)2*6H2O | 2 mg | 2 `G_PER_L` |
| (NH4)2Ni(SO4)2*6H2O | 2 mg | 2 `G_PER_L` |
| Trace minerals | 10 ml | 10 `G_PER_L` |

The inspected JCM and TOGO sources also carry procedural evidence that is not
represented structurally in the record: mix everything except
`Na2S*9H2O`, adjust to pH 6.9 with 1 N `H2SO4`, filter-sterilize under an
`N2-CO2` 80:20 atmosphere, neutralize `Na2S*9H2O` as a 5% solution and
autoclave it under `N2`, add it aseptically and anaerobically under `N2-CO2`,
readjust to pH 6.9 if necessary, and pressurize inoculated bottles to
200 kPa `N2-CO2` 80:20.

## Completeness

The record is complete enough for source identity and the main grams-per-liter
chemical rows, but not for units, stock structure, or preparation:

- The `Trace minerals` stock is represented as an empty generated solution
  named `Unknown solution` with no structured relation to `TOGO:M142` /
  JCM medium 151.
- The milligram and milliliter rows were flattened to `G_PER_L`, creating
  1000x errors for three milligram ingredients and a dimensionally wrong trace
  stock dilution.
- The gas and acid handling instructions are collapsed to variable standalone
  ingredients, losing the 1 N acid strength, pH 6.9 target, 80:20 `N2-CO2`
  atmosphere, final 200 kPa pressure, and sodium sulfide sterilization boundary.
- The absent target organisms, variants, and primary growth references are not
  defects for this source recipe import; JCM medium pages describe a recipe and
  do not, by themselves, assert strain-level growth outcomes.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The source milligram and milliliter units were imported as `G_PER_L`, with numeric values left unchanged. | TOGO M206 and JCM medium 213 list `Resazurin` as 1 mg, `Fe(NH4)2(SO4)2*6H2O` as 2 mg, `(NH4)2Ni(SO4)2*6H2O` as 2 mg, `Trace minerals` as 10 ml, and `Distilled water` as 990 ml; the generated YAML stores all five as `G_PER_L`. `data/import_tracking/reports/concentration_plausibility.tsv` already flags the resazurin row as `INDICATOR_UNIT_SLIP`. | `data/normalized_yaml/archaea/TOGO_M206_Archaeoglobus_Fulgidus_Medium.yaml` or the TOGO importer. |
| Major | The trace-minerals stock reference remains an empty, ungrounded solution. | The generated `solutions` entry for `Trace minerals (see Medium [M142])` has `composition: []`, `name: Unknown solution`, and 10 `G_PER_L`. The inspected source row is a 10.0 ml addition of JCM Medium 151 trace minerals; the TOGO API names `reference_media_id: M142`, which resolves in this corpus to `TOGO_M142_Pyrococcus_Medium.yaml` / JCM_M151. | `data/normalized_yaml/archaea/TOGO_M206_Archaeoglobus_Fulgidus_Medium.yaml`, with stock content verified from TOGO M142 / JCM Medium 151. |
| Major | Anaerobic preparation, pH, filtration, and gas pressure constraints were dropped. | JCM medium 213 instructs pH 6.9 adjustment with 1 N `H2SO4`, filtration under `N2-CO2` 80:20, separate neutralization/autoclaving of `Na2S*9H2O`, anaerobic addition of that solution, optional pH readjustment, and 200 kPa bottle pressurization; the record retains only variable `H2SO4`, `Carbon dioxide gas`, and `Nitrogen gas` ingredient rows. | `data/normalized_yaml/archaea/TOGO_M206_Archaeoglobus_Fulgidus_Medium.yaml` or the TOGO importer. |

No blockers found. No minor findings found.

## Recommended Edits

1. In `data/normalized_yaml/archaea/TOGO_M206_Archaeoglobus_Fulgidus_Medium.yaml`
   or the TOGO import transform, preserve source mass/volume dimensions:
   `Distilled water` as 990 ml/L, `Resazurin` as 1 mg/L,
   `Fe(NH4)2(SO4)2*6H2O` as 2 mg/L,
   `(NH4)2Ni(SO4)2*6H2O` as 2 mg/L, and `Trace minerals` as a 10 ml/L stock
   addition rather than 10 g/L.
2. Replace the empty `Trace minerals (see Medium [M142])` solution with a
   structured, resolved stock representation backed by the TOGO M142 / JCM
   Medium 151 formula. Several curated bacterial records already document this
   as `TOGO M142 / JCM Medium 151`; use them only as patterns and re-check the
   source before copying formula rows.
3. Add source-backed preparation detail for pH 6.9, 1 N `H2SO4`, filtration
   under `N2-CO2` 80:20, separately neutralized and autoclaved 5% sodium
   sulfide, aseptic anaerobic addition, optional final pH readjustment, and
   200 kPa bottle pressurization.
4. Regenerate `data/merge_yaml/merged/archaeoglobus_fulgidus_medium__01928dac.yaml`
   and downstream pages/indexes from the maintained normalized record.

## Follow-up Checks

- Re-run open-schema, strict, term, and reference validation for the normalized
  owner after curation.
- Re-run the merge generator and verify the generated
  `archaeoglobus_fulgidus_medium__01928dac.yaml` no longer has `G_PER_L` for
  source milligram or milliliter rows.
- Inspect the regenerated merge to confirm the trace-minerals addition is no
  longer an empty `Unknown solution` and that its stock amount remains a
  10 ml/L addition to M206, not the final concentrations of the M142 stock
  multiplied into the base recipe.
- Verify any newly added pH, atmosphere, pressure, sterilization, and sodium
  sulfide handling notes against JCM medium 213 or TOGO M206 before treating
  the record as curated.

## Additional Notes

- The broad string `TOGO:M142` is ambiguous without a numeric boundary because
  it also matches adjacent TOGO IDs such as `TOGO:M1420` through
  `TOGO:M1429`; exact searches for that stock should use
  `TOGO:M142([^0-9]|$)` or the normalized owner filename.
- The generated record is not stale relative to its maintained owner; both have
  the same scientific payload, and the generated file adds only merge metadata.
