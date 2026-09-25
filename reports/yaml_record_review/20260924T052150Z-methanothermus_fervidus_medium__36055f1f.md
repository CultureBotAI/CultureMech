# YAML Record Review: METHANOTHERMUS FERVIDUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanothermus_fervidus_medium__36055f1f.yaml
- Started UTC: 2026-09-24T05:20:43Z
- Finished UTC: 2026-09-24T05:21:50Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methanothermus_fervidus_medium__36055f1f.yaml`, a generated `MediaRecipe` for `CultureMech:002611` with `name: methanothermus_fervidus_medium`, `original_name: METHANOTHERMUS FERVIDUS MEDIUM`, and source grounding `mediadive.medium:J251`.

The merged record was generated from `methanothermus_fervidus_medium`; the maintained owner is `data/normalized_yaml/archaea/methanothermus_fervidus_medium.yaml`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanothermus_fervidus_medium__36055f1f.yaml` | Passed; exited 0 with no diagnostics. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methanothermus_fervidus_medium__36055f1f.yaml --out /private/tmp/methanothermus_fervidus_medium__36055f1f.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methanothermus_fervidus_medium__36055f1f.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methanothermus_fervidus_medium__36055f1f.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The record identity is correct: JCM medium 251 and MediaDive `J251` are `METHANOTHERMUS FERVIDUS MEDIUM`, and both carry final pH 6.5. The `COMPLEX` and `UNDEFINED` classifications are also source-compatible because JCM 251 contains yeast extract and Trypticase peptone.

The ingredient graph is not correctly grounded because JCM 251 is a stock-based medium. It uses 37.5 ml Mineral solution I, 37.5 ml Mineral solution II, 10 ml JCM 197 Trace vitamins, and 10 ml JCM 151 Trace minerals, and those stock recipes need to remain scoped.

## Evidence

Supported source claims:

- The JCM 251 identity, pH 6.5, direct main-medium salts, nickel, ferrous sulfate, yeast extract, Trypticase peptone, sodium sulfate, bicarbonate, resazurin, sulfide, and cysteine amounts match MediaDive J251's normalized `g_l` values for a 1015 ml final recipe.
- The main preparation step is from JCM 251 and preserves H2/CO2 handling, separate 5% cysteine and sulfide stocks under N2, overnight standing, pH adjustment, anaerobic stock addition, and 200 kPa post-inoculation pressure.
- The trace-mineral preparation step comes from the nested MediaDive `Trace minerals` solution.

Unsupported or over-scoped generated claims:

- Mineral solution I and II constituents are stock constituents, not top-level final-medium ingredients at 6, 12, 2.4, or 1.6 g/L.
- Trace vitamins from JCM 197 and Trace minerals from JCM 151 were expanded into top-level rows at stock concentration.
- Chemically repeated rows were merged across scopes: FeSO4 x 7 H2O sums the main-medium 2 mg row with 0.1 g/L trace-stock FeSO4; MgSO4 x 7 H2O, CaCl2 x 2 H2O, and NaCl similarly add Mineral solution II concentrations to Trace minerals concentrations.
- JCM 251 specifies 920 ml water in the main solution and 1 L water in Mineral solution I, Mineral solution II, Trace vitamins, and Trace minerals; none of those water rows survive.

## Completeness

The schema-optional evidence, discussions, growth, target organism, and solution arrays are empty; evidence, discussion, and growth omissions are not defects by themselves.

Consequential gaps:

- Solution additions for Mineral solution I, Mineral solution II, Trace vitamins, and Trace minerals are absent.
- Cross references to JCM 197 and JCM 151 are absent.
- All stock water rows are absent.
- The trace-mineral pH instructions are present but attached as a generic second preparation step rather than scoped to the Trace minerals stock.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Four stock additions were flattened into final ingredients. | JCM 251 uses Mineral solution I, Mineral solution II, Trace vitamins from JCM 197, and Trace minerals from JCM 151 as milliliter stock additions. The YAML has no `solutions` entries and stores all stock children as final ingredients. | `data/normalized_yaml/archaea/methanothermus_fervidus_medium.yaml`; JCM/MediaDive solution import. |
| Major | Duplicate cleanup summed ingredients across unrelated scopes. | `FeSO4 x 7 H2O`, `NaCl`, `MgSO4 x 7 H2O`, and `CaCl2 x 2 H2O` have notes showing merged values from main, Mineral solution II, or Trace minerals scopes. These are not duplicate final-medium rows. | `data/normalized_yaml/archaea/methanothermus_fervidus_medium.yaml`; duplicate ingredient cleanup. |
| Major | Source water rows were dropped. | JCM and MediaDive expose main water plus water in Mineral solution I, Mineral solution II, Trace vitamins, and Trace minerals. The YAML has no water ingredient and no stock solution composition carrying those waters. | `data/normalized_yaml/archaea/methanothermus_fervidus_medium.yaml`; JCM/MediaDive importer. |
| Minor | Trace-mineral preparation lost its solution scope. | MediaDive nests the nitrilotriacetic-acid pH steps under `Trace minerals`; the YAML appends them after the main medium H2/CO2 and pressure step. | `data/normalized_yaml/archaea/methanothermus_fervidus_medium.yaml`. |

## Recommended Edits

1. Restore Mineral solution I, Mineral solution II, Trace vitamins, and Trace minerals as scoped stock additions with MediaDive solution IDs 432, 433, 3861, and 3804 and JCM 197/151 provenance where present in JCM.
2. Keep repeated chemical names separate when they come from different stock scopes; do not sum Mineral solution II or Trace minerals salts into final top-level ingredients.
3. Restore the 920 ml main water row and 1 L stock water rows inside their owning solutions.
4. Scope the nitrilotriacetic-acid and pH 7.0 preparation text to the Trace minerals stock.
5. Regenerate `data/merge_yaml/merged/methanothermus_fervidus_medium__36055f1f.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on the regenerated record.
- Diff the regenerated record against JCM 251 and MediaDive J251, verifying that Mineral solution I/II, Trace vitamins, and Trace minerals remain nested.
- Confirm that no stock concentration row is present in top-level `ingredients` unless it is also a direct JCM 251 main-medium ingredient.

## Additional Notes

- Empty optional evidence and discussion fields were not treated as defects.
- A narrow exact search with `rg --no-ignore --hidden` resolved `CultureMech:002611`, `J251`, and `methanothermus_fervidus_medium` in the maintained normalized file and generated merge file; ignored files were included.
