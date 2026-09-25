# YAML Record Review: basal_salts_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/basal_salts_medium.yaml
- Started UTC: 2026-09-21T18:42:14Z
- Finished UTC: 2026-09-21T18:45:02Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path reviewed | `data/merge_yaml/merged/basal_salts_medium.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/basal_salts_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:009411` |
| Name | `basal_salts_medium` |
| Original name | `basal salts medium` |
| Source | TOGO Medium `M2877` |
| Merge status | Generated one-source merge from `basal_salts_medium` |

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with the no-project LinkML invocation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`, and `data/merge_yaml/merged/basal_salts_medium.yaml`. |
| Strict schema | Passed with the no-project invocation of `scripts/validate_strict.py data/merge_yaml/merged/basal_salts_medium.yaml --out /private/tmp/basal_salts_medium.strict.tsv --workers 1 --quiet`: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | Passed with 0 reference checks: the record has no populated `references` list or other reference-bearing evidence for the focused validator to inspect. |
| Term validator | Passed with `linkml-term-validator validate-data data/merge_yaml/merged/basal_salts_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for the standalone `history/` tree, not a focused one-record `MediaRecipe.curation_history` check. |
| Project `just` wrappers | Not rerun here: direct `just validate-schema`, `just validate-strict`, and `just validate-terms` fail before target-specific validation in this checkout while the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13. The equivalent no-project Python 3.11 validators above exercised the target record. |

## Identity and Grounding

- The generated record denotes a single TOGO import, `TOGO:M2877`, named `basal salts medium`; `CultureMech:009411` is registered to `data/normalized_yaml/bacterial/basal_salts_medium.yaml`.
- The maintained normalized record and generated merge currently have the same ingredient content; curation should therefore start in `data/normalized_yaml/bacterial/basal_salts_medium.yaml`, then regenerate merge output.
- Exact gitignore-independent searches for `CultureMech:009411`, `M2877`, and `basal_salts_medium` covered `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`. They found the normalized owner, generated merge, generated indexes, registry rows, and import reports; they did not find a maintained raw M2877 payload in this checkout.
- The hydrated salts with exact CHEBI terms are mostly grounded to the correct ingredient identities. `NaMoO4 . 2H2O` is mapped by the packaged MediaIngredientMech label index to `CHEBI:75213`, whose publication label is `Na2MoO4 x 2 H2O`, but the source and generated preferred term preserve the one-sodium shorthand `NaMoO4`; preserve the source string or document any future normalization explicitly.
- `distilled or deionized water` remains intentionally ungrounded.

## Evidence

- The inspected TOGO M2877 API response supports the record identity, the medium name, the one-liter formulation, all salts, and the role/property annotations imported from GMO.
- The source comment lists these gram-level amounts for a one-liter medium: `(NH4)2SO4, 1.3 g`; `KH2PO4, 0.28 g`; `MgSO4 . 7H2O, 0.25 g`; `CaCl2 . 2H2O, 0.07 g`; and `FeCl3 . 6H2O, 0.02 g`. The generated `G_PER_L` values for those five rows are therefore arithmetically consistent with the one-liter source.
- The source comment and component rows list seven trace additions in milligrams, but the generated record stores each numeric value as grams per liter: `NaMoO4 . 2H2O` 0.03 mg, `MnCl2 . 4H2O` 1.8 mg, `ZnSO4 . 7H2O` 0.22 mg, `CuCl2 . 2H2O` 0.05 mg, `VOSO4 . 2 H2O` 0.03 mg, `Na2B4O7 . 10 H2O` 4.5 mg, and `CoSO4` 0.01 mg.
- The source gives the solvent as `distilled or deionized water, 1 l`; the record keeps numeric value `1` but imports it as `G_PER_L`.
- The source says the pH is adjusted with `10N H2SO4`, and the H2SO4 component has `conc_value: 10` plus `conc_unit: N` in the TOGO API response. The record instead has only a default `variable`/`VARIABLE` concentration and treats H2SO4 as a generic mineral-source ingredient.
- The record has no direct primary citation, DOI, PMID, target-organism evidence, or preparation evidence beyond TOGO's source comment.

## Completeness

- Consequential gaps:
  - Seven milligram additions require correction to mg/L or an equivalent `0.001` conversion to g/L.
  - `distilled or deionized water` needs a volume representation instead of `1 G_PER_L`.
  - The `10 N` H2SO4 concentration and "adjusted with" semantics need to be retained.
  - `medium_type` and `composition_type` need curator review because the all-salt formulation is represented as `COMPLEX`/`UNDEFINED`.
- Correctly empty optional slots:
  - `solutions` is absent because the inspected TOGO record lists all components directly.
  - `target_organisms`, `references`, `variants`, and organism-growth evidence are empty; TOGO M2877 does not name a strain, organism, or publication identifier in the inspected payload.
- Bounded negative searches:
  - An exact gitignore-independent search for the M2877 source sentence, `For most studies a basal salts medium`, across `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found no local raw source capture.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Seven trace salts are imported 1000x too high because TOGO `mg` rows became `G_PER_L` rows without scaling. | TOGO M2877 lists `NaMoO4 . 2H2O`, `MnCl2 . 4H2O`, `ZnSO4 . 7H2O`, `CuCl2 . 2H2O`, `VOSO4 . 2 H2O`, `Na2B4O7 . 10 H2O`, and `CoSO4` in `mg`; the generated record stores the same numeric values in `G_PER_L`. | `data/normalized_yaml/bacterial/basal_salts_medium.yaml`; broad repeats should be fixed in the TOGO import unit conversion. |
| Major | The one-liter water row is dimensionally wrong. | TOGO M2877 lists `distilled or deionized water` as `1 L`; the record stores `value: '1'`, `unit: G_PER_L`. | `data/normalized_yaml/bacterial/basal_salts_medium.yaml`; broad repeats should be fixed in the TOGO import volume conversion. |
| Major | The acid adjustment lost the source concentration and procedural role. | TOGO M2877 carries `H2SO4` with `conc_value: 10`, `conc_unit: N`, and the comment states the pH was adjusted with 10 N H2SO4; schema defaulter history shows the imported row was defaulted to `variable`/`VARIABLE`. | `data/normalized_yaml/bacterial/basal_salts_medium.yaml`; the TOGO importer should retain normality and pH-adjustment context where present. |
| Major | The chemically defined salts recipe is classified as complex and undefined. | Every TOGO M2877 component is a defined water, salt, or acid solution; the record says `medium_type: COMPLEX` and `composition_type: UNDEFINED`, which downstream KGX export treats as load-bearing. | `data/normalized_yaml/bacterial/basal_salts_medium.yaml`. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/basal_salts_medium.yaml`, convert the seven TOGO milligram components to `0.00003`, `0.0018`, `0.00022`, `0.00005`, `0.00003`, `0.0045`, and `0.00001 G_PER_L`, or to an equivalent mg/L representation if the schema supports it.
2. Represent the solvent as `1 L` or a schema-supported one-liter final-volume row; do not leave it as `1 G_PER_L`.
3. Preserve the `10 N` H2SO4 adjustment as an acid-adjustment ingredient or preparation note rather than a default variable mineral source.
4. Reclassify this medium to `composition_type: DEFINED` and keep `medium_type` derived consistently as `DEFINED`.
5. If other TOGO imports repeat the same unit pattern, fix the TOGO import normalization that converts source `mg`, `L`, and concentrated acid rows before regenerating normalized and merged products.

## Follow-up Checks

- Rerun open-schema LinkML validation, `scripts/validate_strict.py`, `linkml-term-validator`, and the reference validator on `data/normalized_yaml/bacterial/basal_salts_medium.yaml` after the normalized fix.
- Regenerate `data/merge_yaml/merged/basal_salts_medium.yaml`, rerun `just verify-merges` and `just audit-merge-freshness`, and confirm no derived record still has the seven 1000x trace-salt values.
- Re-run `data/import_tracking/reports/concentration_plausibility.tsv` generation or an equivalent focused check and confirm `CultureMech:009411` no longer emits the `TRACE_SALT_AS_STOCK` rows that currently flag `MnCl2 . 4H2O` and borax.
- Manually re-fetch TOGO M2877 and diff the source component amounts against the normalized rows, including the `10 N` H2SO4 component.

## Additional Notes

- The exact `CultureMech:009411` search already surfaces `data/import_tracking/reports/concentration_plausibility.tsv`, which independently flags `MnCl2 . 4H2O` and `Na2B4O7 .  10 H2O` as trace-salt magnitudes that look like stock-solution or unit-conversion errors.
- Exact gitignore-independent searches included ignored files where present. The local search for `GMO_001011` found no rows, so the source GMO component identifiers from the live TOGO API are not persisted in tracked or ignored local data under the searched paths.
