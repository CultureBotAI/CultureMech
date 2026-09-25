# YAML Record Review: Methanothermus Fervidus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanothermus_fervidus_medium__3a7f4143.yaml
- Started UTC: 2026-09-24T05:21:51Z
- Finished UTC: 2026-09-24T05:22:52Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methanothermus_fervidus_medium__3a7f4143.yaml`, a generated `MediaRecipe` for `CultureMech:009019` with `name: methanothermus_fervidus_medium`, `original_name: Methanothermus Fervidus Medium`, and source grounding `TOGO:M243`.

The merged record was generated from `TOGO_M243_Methanothermus_Fervidus_Medium`; the maintained owner is `data/normalized_yaml/archaea/TOGO_M243_Methanothermus_Fervidus_Medium.yaml`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanothermus_fervidus_medium__3a7f4143.yaml` | Passed; `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methanothermus_fervidus_medium__3a7f4143.yaml --out /private/tmp/methanothermus_fervidus_medium__3a7f4143.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methanothermus_fervidus_medium__3a7f4143.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methanothermus_fervidus_medium__3a7f4143.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The source identity is correct: TOGO `M243` is derived from JCM `JCM_M251`, and JCM medium 251 is `METHANOTHERMUS FERVIDUS MEDIUM`.

The recipe is not faithfully grounded. JCM 251 has 37.5 ml Mineral solution I, 37.5 ml Mineral solution II, 10 ml Trace vitamins from JCM 197, 10 ml Trace minerals from JCM 151, direct milligram rows for resazurin, nickel salt, and FeSO4 x 7 H2O, pH 6.5, and a long anaerobic H2/CO2/N2 preparation. The generated record flattens mineral stock contents, stores stock additions as grams per liter, and omits all pH and preparation detail.

## Evidence

Supported source claims:

- TOGO `M243` supports the record label, the JCM 251 original URL, complex/undefined classification, and the direct 2 g/L yeast extract, 2 g/L Trypticase peptone, 3.4 g/L sodium sulfate, 2 g/L bicarbonate, 0.5 g/L sulfide, and 0.5 g/L cysteine amounts.
- TOGO `M243` preserves the JCM stock additions for Mineral solution I, Mineral solution II, Trace vitamins, and Trace minerals as separate referenced components.

Unsupported or over-scoped generated claims:

- `Resazurin: 1 G_PER_L`, `(NH4)2Ni(SO4)2 x 6 H2O: 3 G_PER_L`, and `FeSO4 x 7 H2O: 2 G_PER_L` are unit slips. JCM and TOGO give those rows as 1 mg, 3 mg, and 2 mg, respectively.
- `Mineral solution I`, `Mineral solution II`, `Trace vitamins`, and `Trace minerals` are milliliter additions, not 37.5 or 10 g/L solutes.
- K2HPO4, KH2PO4, (NH4)2SO4, NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O belong inside Mineral solution I or II, not as final top-level ingredients at stock concentration.
- The `Distilled water` row merges 920 ml main water and 1 L water rows from two mineral stocks into `922.0 G_PER_L`.

## Completeness

The schema-optional evidence, discussions, growth, and target organism fields are empty; those empty slots are not defects by themselves.

Consequential gaps:

- Mineral solution I and II have empty composition arrays even though TOGO and JCM include their formulas inline.
- Trace vitamins and Trace minerals are not resolved to the referenced JCM 197 and JCM 151 formulas, and the imported cross references remain prose-only `notes`.
- The TOGO/JCM pH 6.5 is absent from `ph_value`.
- The H2/CO2 boil-and-dispense handling, separate N2 autoclaving of 5% cysteine and sulfide stocks, overnight stand, anaerobic additions, and 200 kPa H2/CO2 post-inoculation pressure were dropped.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Source milligram and milliliter rows were serialized as `G_PER_L`. | Resazurin, nickel salt, and FeSO4 are mg rows in JCM/TOGO, and the four stock additions are ml rows. The YAML stores their raw amounts under `G_PER_L`, making a thousand-fold or dimensionally invalid assertion. | `data/normalized_yaml/archaea/TOGO_M243_Methanothermus_Fervidus_Medium.yaml`; TOGO importer. |
| Major | Mineral solution I and II were flattened and partially emptied. | TOGO M243 imports both inline mineral stock formulas, but the generated record stores their salts as top-level ingredients and leaves the `Mineral solution I` and `Mineral solution II` solution objects with empty `composition`. | `data/normalized_yaml/archaea/TOGO_M243_Methanothermus_Fervidus_Medium.yaml`; solution migrator. |
| Major | Water rows were merged across unrelated scopes. | The single `Distilled water` row says it merged 920, 1, and 1 from the main medium and two 1 L mineral-stock solvents. | `data/normalized_yaml/archaea/TOGO_M243_Methanothermus_Fervidus_Medium.yaml`; duplicate ingredient cleanup. |
| Major | Essential pH and anaerobic preparation text is absent. | JCM 251 and TOGO M243 specify pH 6.5, H2/CO2 boiling and dispensing, N2 handling for 5% cysteine and sulfide solutions, an overnight stand, and final pressurization. The YAML has no `ph_value` and no preparation steps. | `data/normalized_yaml/archaea/TOGO_M243_Methanothermus_Fervidus_Medium.yaml`; TOGO comment importer. |
| Minor | JCM stock cross references are not structured. | Trace vitamins and Trace minerals cite JCM 197 and JCM 151 in the source. The YAML keeps TOGO `M190` and `M142` only as free-text notes on empty solution records. | `data/normalized_yaml/archaea/TOGO_M243_Methanothermus_Fervidus_Medium.yaml`. |

## Recommended Edits

1. Recurate the TOGO M243 normalized record to keep milligram, milliliter, and stock-scope quantities in their original dimensions.
2. Populate Mineral solution I and II as scoped stocks and link Trace vitamins and Trace minerals to their referenced JCM/TOGO stock records instead of flattening or leaving empty stubs.
3. Restore the distinct main and mineral-stock water rows in their owning scopes.
4. Import pH 6.5 and the full anaerobic preparation paragraph.
5. Regenerate `data/merge_yaml/merged/methanothermus_fervidus_medium__3a7f4143.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on the regenerated record.
- Diff the regenerated YAML against JCM 251 and TOGO M243 to confirm mg and ml rows no longer appear as `G_PER_L`.
- Verify that Mineral solution I and II are nested and that the JCM 197/151 cross references are structured.

## Additional Notes

- Empty optional evidence and discussion fields were not treated as defects.
- The exact owner search used `rg --no-ignore --hidden`, so ignored files were included when resolving `CultureMech:009019`, `TOGO_M243_Methanothermus_Fervidus_Medium`, and `methanothermus_fervidus_medium`.
