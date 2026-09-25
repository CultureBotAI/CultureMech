# YAML Record Review: hydrogen_oxydizing_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hydrogen_oxydizing_medium.yaml
- Started UTC: 2026-09-23T13:03:15Z
- Finished UTC: 2026-09-23T13:06:53Z
- Verdict: needs curation

## Target

- Reviewed generated record: `data/merge_yaml/merged/hydrogen_oxydizing_medium.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:003500`
- Name: `hydrogen_oxydizing_medium`
- Source identity in the generated record: KOMODO Medium 1003, `HYDROGEN-OXYDIZING MEDIUM`, `komodo.medium:1003`
- Maintained inputs:
  - `data/normalized_yaml/bacterial/KOMODO_1003_HYDROGEN-OXYDIZING_MEDIUM.yaml`, `CultureMech:003500`
  - `data/normalized_yaml/bacterial/hydrogen_oxydizing_medium.yaml`, `CultureMech:000419`
- Merge state: generated `SOURCE_DUPLICATE` merge from `KOMODO_1003_HYDROGEN-OXYDIZING_MEDIUM` and `hydrogen_oxydizing_medium`

## Validation

- `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hydrogen_oxydizing_medium.yaml`: passed.
- `python scripts/validate_strict.py data/merge_yaml/merged/hydrogen_oxydizing_medium.yaml --out /private/tmp/hydrogen_oxydizing_medium.strict.tsv --workers 1 --quiet`: passed with 0 error rows.
- `linkml-reference-validator validate data data/merge_yaml/merged/hydrogen_oxydizing_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`: passed; 0 reference checks.
- `linkml-term-validator validate-data data/merge_yaml/merged/hydrogen_oxydizing_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`: passed after the expected `eutils` deprecation warning.
- Embedded history: Not checked; the repository exposes `just validate-history` for standalone `history/` entries, not for `MediaRecipe.curation_history` embedded in a merged YAML file.

## Identity and Grounding

- The stable ID, generated filename, and `media_term` consistently identify KOMODO Medium 1003, `HYDROGEN-OXYDIZING MEDIUM`.
- The `hydrogen_oxydizing` spelling is inherited from the upstream `HYDROGEN-OXYDIZING` source label rather than introduced only by the local slug.
- The DSMZ duplicate input also resolves to DSMZ/MediaDive Medium 1003, the same named medium, and the live MediaDive REST record links it to `DSMZ_Medium1003.pdf`.
- The generated record keeps the KOMODO `media_term` but the KOMODO normalized input says its ingredients were copied from DSMZ Medium 1003. Live KOMODO 1003 exposes final, diluted gram amounts, while the normalized KOMODO file currently contains undiluted DSMZ stock-solution strengths.
- Grounding is incomplete or stale for the nested trace solution after flattening:
  - `Na-tungstate x 2 H2O`, `Se-acid`, and `HBO3` are ungrounded in the generated record.
  - `NiSO4 x 6 H2O` is grounded to `CHEBI:53001`, generic nickel sulfate, although the source label is a hexahydrate.

## Evidence

- DSMZ Medium 1003 and the MediaDive 1003 REST record support the main solution with 1000 ml anaerobic water, 7 g `MgSO4 x 7 H2O`, 2 g `NaS2O3`, 0.40 g `CaCl2 x 2 H2O`, 0.48 g `KCl`, 0.78 g `MgCl2`, and 1.95 g `MES`.
- Those same DSMZ/MediaDive sources add three stock solutions to the main solution: 2.00 ml Solution A, 1.50 ml Solution B, and 10.00 ml trace mineral solution.
- Solution A is a 100x stock containing, per 1000 ml stock, 100 g `NH4Cl`, 100 g `MgCl2 x H2O`, and 40 g `CaCl2 x 2 H2O`, adjusted to pH 4 with HCl.
- Solution B is a 500x stock containing, per 1000 ml stock, 200 g `K2HPO4 x 3 H2O`.
- The trace mineral solution is a 100x stock containing mg-scale EDTA, cobalt, manganese, iron, zinc, aluminum, tungstate, copper, nickel, selenium, borate, and molybdate components per 1000 ml stock, adjusted to pH 3.0 with HCl.
- The generated record does not cite an inspected reference under `references`; its source identity is recoverable only from `media_term`, `notes`, and source import history.

## Completeness

- Consequentially incomplete: the generated canonical record has no `preparation_steps`, although the DSMZ normalized duplicate has the CO2 gassing, tube loading, autoclaving, O2 addition, and H2 pressurization instructions.
- Consequentially incomplete: stock solution references and stock solvents were lost in the main medium. The generated record should either reference Solution A, Solution B, and the trace mineral solution with their addition volumes or carry final diluted amounts with explicit derivation.
- Consequentially incomplete: the main 1000 ml anaerobic water row and the 1000 ml distilled-water rows inside the three stocks are not represented.
- Consequentially incomplete: the HCl pH adjusters for Solution A and the trace mineral stock are not represented.
- Empty optional slots for target organisms, growth evidence, and literature citations are not defects in this import-only recipe record.
- Bounded searches:
  - `find data/normalized_yaml -name '*solution*b*1003*' -print`, which includes ignored files, found no curated KOMODO/DSMZ `Solution B` file named for medium 1003.
  - `rg --no-ignore --hidden -n -F 'Solution B (500x solution)' data data/import_tracking src scripts` found the generic MediaDive solution record `data/normalized_yaml/bacterial/mediadive_2048_Solution_B_500x_solution.yaml`.
  - `find data/raw/komodo data/raw/komodo_web -maxdepth 3 -type f -print` found only the two README files, and `rg --no-ignore --hidden -n -F 'HYDROGEN-OXYDIZING' data/raw/komodo data/raw/komodo_web` found no raw KOMODO payload in this checkout.

## Findings

### Blockers

None found.

### Major

| Finding | Evidence | Maintained owner |
|---|---|---|
| Stock strengths are flattened as final `G_PER_L` ingredients. | DSMZ and MediaDive add 2 ml Solution A, 1.5 ml Solution B, and 10 ml trace solution to the main solution; the generated record instead carries 100 g/L `NH4Cl`, 100 g/L `MgCl2 x H2O`, 200 g/L `K2HPO4 x 3 H2O`, and full trace-stock concentrations as direct medium ingredients. | `data/normalized_yaml/bacterial/KOMODO_1003_HYDROGEN-OXYDIZING_MEDIUM.yaml`; the DSMZ enrichment that copied nested stock recipes into the KOMODO main recipe. |
| `CaCl2 x 2 H2O` is an unsupported synthetic 40.4 g/L value. | The source main solution has 0.40 g calcium chloride dihydrate and Solution A has 40 g/L calcium chloride dihydrate stock added at 2 ml. The record sums 0.4 and 40.0 across solution boundaries. `data/import_tracking/reports/merged_duplicates.tsv` also flags this exact `DIFFERING_PARTS` merge for both normalized inputs. | `data/normalized_yaml/bacterial/KOMODO_1003_HYDROGEN-OXYDIZING_MEDIUM.yaml`, `data/normalized_yaml/bacterial/hydrogen_oxydizing_medium.yaml`, and the duplicate-ingredient cleanup rule. |
| The merge drops supported DSMZ preparation detail. | DSMZ and MediaDive specify CO2 gassing before dispensing, stoppered culture tubes, autoclaving for 20 min at 121 C, O2 before inoculation, and H2 pressurization after inoculation. The DSMZ normalized input preserved those steps, but the generated canonical KOMODO merge has no `preparation_steps`. | Merge selection for `KOMODO_1003_HYDROGEN-OXYDIZING_MEDIUM.yaml` and `data/normalized_yaml/bacterial/hydrogen_oxydizing_medium.yaml`. |
| Trace-solution ingredient grounding is stale or unresolved after flattening. | The generated record leaves `Na-tungstate x 2 H2O`, `Se-acid`, and `HBO3` without terms and maps hydrated `NiSO4 x 6 H2O` to generic nickel sulfate. The maintained KOMODO 2075 trace-solution record has already resolved sodium tungstate dihydrate, selenic acid, boric acid, and nickel sulfate hexahydrate more specifically. | Import/enrichment for `data/normalized_yaml/bacterial/KOMODO_1003_HYDROGEN-OXYDIZING_MEDIUM.yaml`; solution provenance in `data/normalized_yaml/bacterial/trace_mineral_solution_medium_1003.yaml`. |

### Minor

| Finding | Evidence | Maintained owner |
|---|---|---|
| The generated record lacks direct `references`. | Neither normalized main-medium input contributes a `references` list to the generated record, even though the DSMZ PDF, MediaDive medium URL, and KOMODO medium URL were sufficient to verify the formulation. | Normalized KOMODO and DSMZ Medium 1003 records. |

## Recommended Edits

1. Rebuild `data/normalized_yaml/bacterial/KOMODO_1003_HYDROGEN-OXYDIZING_MEDIUM.yaml` from live KOMODO Medium 1003 final concentrations or from DSMZ/MediaDive nested stocks with explicit stock-solution references; do not carry undiluted Solution A, Solution B, or trace-stock amounts as direct final-medium grams per liter.
2. Correct the DSMZ-owned `data/normalized_yaml/bacterial/hydrogen_oxydizing_medium.yaml` to preserve the main formula, the 2 ml Solution A addition, the 1.5 ml Solution B addition, the 10 ml trace-solution addition, and the stock solution boundaries instead of the summed flat ingredient list.
3. Add or curate a maintained medium-1003 Solution B record from the DSMZ/MediaDive 2048 source, analogous to `solution_a_medium_1003.yaml` and `trace_mineral_solution_medium_1003.yaml`.
4. Keep the DSMZ gassing, tube-loading, autoclaving, O2, H2, and stock pH-adjustment steps attached to the DSMZ-derived representation so merge generation cannot discard them.
5. Refresh trace-solution grounding in the generated main record by referencing the curated trace solution rather than copying stale ungrounded trace labels.
6. Add inspected source URLs to both normalized main-medium records and regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation on both normalized inputs and the regenerated `data/merge_yaml/merged/hydrogen_oxydizing_medium.yaml`.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration to confirm the source duplicate still collapses intentionally and no stale merged record remains.
- Manually refetch KOMODO Medium 1003 and MediaDive/DSMZ Medium 1003 and verify that the generated main medium no longer contains `40.4` g/L calcium chloride, undiluted `100` g/L ammonium chloride, or undiluted `200` g/L phosphate as direct final-medium rows.
- Verify `linkml-term-validator` after the trace solution is linked or refreshed; `Na-tungstate x 2 H2O`, `Se-acid`, `HBO3`, and `NiSO4 x 6 H2O` should not remain ungrounded or mapped to an anhydrous salt when a hydrated source form is known.

## Additional Notes

- The raw KOMODO directories in this checkout are empty apart from READMEs, so this review used the live KOMODO servlet pages for media 1003, 2025, and 2075 plus the MediaDive REST record and extracted DSMZ PDF text.
- Live KOMODO Medium 1003 already reports final diluted amounts for the 100x and 500x stock components. The incorrect large stock strengths in `CultureMech:003500` appear to come from the `dsmz-resolver-v1.0` enrichment step, not from the original KOMODO 1003 table.
- The source spelling `HYDROGEN-OXYDIZING` is unusual but present in KOMODO, DSMZ, and MediaDive, so the local `hydrogen_oxydizing_medium` stem is source-derived.
