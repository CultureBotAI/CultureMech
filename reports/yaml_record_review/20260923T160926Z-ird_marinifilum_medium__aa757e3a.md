# YAML Record Review: ird_marinifilum_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ird_marinifilum_medium__aa757e3a.yaml`
- Started UTC: 2026-09-23T16:08:00Z
- Finished UTC: 2026-09-23T16:09:28Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:002210` |
| Label | `ird_marinifilum_medium` |
| Source term | `mediadive.medium:J1026`, `IRD MARINIFILUM MEDIUM` |
| Maintained owner | `data/normalized_yaml/bacterial/ird_marinifilum_medium.yaml` |
| Generated target | `data/merge_yaml/merged/ird_marinifilum_medium__aa757e3a.yaml` |
| Merge | Single source, `merged_from: [ird_marinifilum_medium]` |

This is the generated MediaDive import of JCM Medium 1026, IRD MARINIFILUM
MEDIUM. Future formulation fixes belong in the maintained MediaDive owner or
its importer, then `data/merge_yaml/merged/` should be regenerated.

## Validation

| Check | Result |
|---|---|
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ird_marinifilum_medium__aa757e3a.yaml` | Passed. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ird_marinifilum_medium__aa757e3a.yaml --out /private/tmp/ird_marinifilum_medium__aa757e3a.strict.tsv --workers 1 --quiet` | Passed with 0 error rows; the TSV had only its header. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ird_marinifilum_medium__aa757e3a.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the configured reference pass performed 0 checks. |
| `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ird_marinifilum_medium__aa757e3a.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed with the known `pkg_resources` warning from `eutils`. |
| Embedded `curation_history` validator | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not the embedded `MediaRecipe.curation_history` block in generated YAML. |

## Identity and Grounding

JCM, MediaDive, and TOGO agree on the target identity: JCM GRMD 1026 is IRD
MARINIFILUM MEDIUM; MediaDive exposes it as `J1026`; TOGO exposes the same
JCM source as `M1088` with `original_media_id: JCM_M1026`.

The record is not a wrong medium: `media_term.id` is `mediadive.medium:J1026`,
the name is the JCM name normalized to snake case, `ph_value` is 7.2 as in
JCM/MediaDive/TOGO, and `category: bacterial`, `medium_type: COMPLEX`,
`composition_type: UNDEFINED`, and `physical_state: LIQUID` are coherent for
the imported medium.

It is, however, a duplicate view of the same source medium. An
ignored-file-inclusive `rg` for exact JCM/MediaDive/TOGO identifiers under
`data/normalized_yaml` and `data/merge_yaml/merged` found this MediaDive owner
and generated file plus `TOGO_M1088_IRD_Marinifilum_Medium.yaml` and its
generated sibling, `IRD_MARINIFILUM_MEDIUM.yaml`.

## Evidence

The directly weighed basal ingredients are source-aligned. JCM 1026 lists
1.0 g NH4Cl, 0.3 g KH2PO4, 0.3 g K2HPO4, 25.0 g NaCl, 0.1 g KCl,
0.1 g CaCl2 x 2 H2O, 1.0 g yeast extract, 0.5 g L-cysteine HCl x H2O,
and 1.0 mg resazurin. MediaDive represents those rows with a 1001 ml solution
volume, so the generated `G_PER_L` values around `0.999001`, `0.2997`,
`24.975`, `0.0999001`, and `0.000999001` match the MediaDive conversion.

The preparation prose is traceable to JCM 1026: mix the basal components,
adjust to pH 7.2, boil, cool under N2-CO2 at 4:1, seal with butyl rubber
stoppers, autoclave, add the stock solutions aseptically and anaerobically,
and readjust to pH 7.2 if needed.

The post-autoclave stock additions are not represented correctly. JCM 1026 and
MediaDive J1026 add 20 ml of 15% MgCl2 x 6 H2O solution, 25 ml of 8% NaHCO3
solution, 20 ml of 1 M glucose solution, and 10 ml of 5% Na2S x 9 H2O
solution. The generated record instead stores `MgCl2 x 6 H2O`, `NaHCO3`,
`Glucose`, and `Na2S x 9 H2O` as final-medium ingredients with `20`, `25`,
`20`, and `10 G_PER_L`.

The trace stock was flattened as if its one-liter stock recipe were final
medium. JCM 1026 says to add 1.0 ml of "Trace element solution (see Medium No.
439)". JCM 439 and MediaDive solution `4186` define that stock as 12.5 ml 25%
HCl, 2.1 g FeSO4 x 7 H2O, 30 mg H3BO3, 100 mg MnCl2 x 4 H2O, 190 mg
CoCl2 x 6 H2O, 24 mg NiCl2 x 6 H2O, 2 mg CuCl2 x 2 H2O, 144 mg
ZnSO4 x 7 H2O, 36 mg Na2MoO4 x 2 H2O, and 987 ml distilled water. The
generated record promotes the non-water stock components to top-level
ingredients with the stock g/L values and turns `12.5 ml HCl (25%)` into
`12.5 G_PER_L`.

## Completeness

The main-medium and trace-stock water rows are missing. JCM and MediaDive
state 925 ml distilled water in the J1026 basal solution and 987 ml distilled
water in the M439 trace stock; neither appears in the generated record.

The sibling TOGO import is also incomplete. It leaves the M439 trace stock and
the four JCM stock additions as `Unknown solution` entries with empty
`composition` arrays, so the two generated records for the same JCM source
cannot currently merge into a single complete representation.

`target_organisms`, `growth_metrics`, and strain-level growth evidence can
remain empty in this generated source import: JCM 1026 is a formulation record,
and the inspected JCM, MediaDive, and TOGO source records do not assert a
specific organism or growth outcome for this medium.

An ignored-file-inclusive `find` under `reports/yaml_record_review` found no
pre-existing review report for the exact
`ird_marinifilum_medium__aa757e3a` generated stem before this report was
created.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The M439 trace stock has been flattened into final-medium ingredients. The reviewed record represents HCl, FeSO4 x 7 H2O, H3BO3, MnCl2 x 4 H2O, CoCl2 x 6 H2O, NiCl2 x 6 H2O, CuCl2 x 2 H2O, ZnSO4 x 7 H2O, and Na2MoO4 x 2 H2O as if their stock concentrations were final concentrations. | JCM 1026 lists a 1.0 ml trace-stock addition; JCM 439 and MediaDive solution `4186` list these as ingredients of the one-liter trace stock. | `data/normalized_yaml/bacterial/ird_marinifilum_medium.yaml`, its linked MediaDive solution import, or the MediaDive importer. |
| Major | Four post-autoclave solution additions were converted to top-level `G_PER_L` ingredient rows. | JCM 1026 and MediaDive J1026 list 20 ml 15% MgCl2 x 6 H2O, 25 ml 8% NaHCO3, 20 ml 1 M glucose, and 10 ml 5% Na2S x 9 H2O; the generated YAML stores them as `20`, `25`, `20`, and `10 G_PER_L`. | `data/normalized_yaml/bacterial/ird_marinifilum_medium.yaml` or the MediaDive importer. |
| Major | The generated record drops water from both the final basal medium and the trace stock. | JCM/MediaDive J1026 state 925 ml distilled water for the basal medium; JCM 439 and MediaDive solution `4186` state 987 ml distilled water for the trace stock. | `data/normalized_yaml/bacterial/ird_marinifilum_medium.yaml`, the MediaDive solution import, or the MediaDive importer. |
| Major | The duplicate TOGO M1088 record for the same JCM source cannot merge with this MediaDive J1026 record because each importer loses a different part of the same stock structure. | The TOGO owner for `TOGO:M1088` points at the same JCM `GRMD=1026` URL and keeps the M439, bicarbonate, magnesium chloride, glucose, and sulfide additions as five empty `Unknown solution` objects. | `data/normalized_yaml/bacterial/TOGO_M1088_IRD_Marinifilum_Medium.yaml`, `data/normalized_yaml/bacterial/ird_marinifilum_medium.yaml`, and their import/merge rules. |
| Minor | Preparation is stored as one broad `AUTOCLAVE` step plus a pH readjustment, so the boil, cool under N2-CO2, seal, anaerobic stock addition, stock atmosphere, and filtered 8% NaHCO3 solution details are not structured. | JCM 1026 scopes the anaerobic handling and post-autoclave stock addition instructions around the second table; the generated text preserves them only as one string. | `data/normalized_yaml/bacterial/ird_marinifilum_medium.yaml` or the MediaDive importer. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/ird_marinifilum_medium.yaml`, replace the
   flattened trace constituents with a 1 ml addition of the M439/MediaDive
   `4186` trace stock, represented either as a resolvable `SolutionRecipe` or
   as a nested solution with the JCM 439 formulation.
2. Preserve the post-autoclave 20 ml 15% MgCl2 x 6 H2O, 25 ml 8% NaHCO3,
   20 ml 1 M glucose, and 10 ml 5% Na2S x 9 H2O solution additions instead of
   treating their volumes as grams per liter.
3. Restore the 925 ml J1026 distilled-water row and the 987 ml M439
   trace-stock water row in their correct scopes.
4. Split the JCM 1026 preparation text into distinct ordered actions for pH
   adjustment, boiling, cooling under N2-CO2, butyl-stopper sealing,
   autoclaving, anaerobic stock addition, and final pH readjustment.
5. Apply the same source-boundary repair to
   `data/normalized_yaml/bacterial/TOGO_M1088_IRD_Marinifilum_Medium.yaml` so
   the TOGO M1088 and MediaDive J1026 views can regenerate to one complete
   merged recipe.
6. Regenerate `data/merge_yaml/merged/` after the maintained owners or importers
   are fixed.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/bacterial/ird_marinifilum_medium.yaml`.
- Run `just validate-strict data/normalized_yaml/bacterial/ird_marinifilum_medium.yaml`.
- Run `just validate-terms data/normalized_yaml/bacterial/ird_marinifilum_medium.yaml` after linking the repaired solution records.
- Run `just validate-references data/normalized_yaml/bacterial/ird_marinifilum_medium.yaml` after adding structured JCM, MediaDive, and TOGO source references.
- Regenerate the merged YAML, then rerun the schema, strict, term, and
  reference validators on the regenerated `ird_marinifilum_medium` target.
- Manually compare the regenerated target against JCM 1026, JCM 439, MediaDive
  J1026, MediaDive solution `4186`, and TOGO M1088 for solution boundaries,
  stock volumes, water rows, pH 7.2, and anaerobic preparation order.

## Additional Notes

- Empty `target_organisms`, `growth_metrics`, `variants`, and discussion fields
  are not defects for this imported formulation.
- The source fetches used MediaDive REST `/rest/medium/J1026`, MediaDive REST
  `/rest/solution/4186`, TOGO
  `/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1088`, JCM `GRMD=1026`, and JCM
  `GRMD=439`.
- The exact source-ID and report-existence searches used ignored-file-inclusive
  `rg --no-ignore --hidden` and `find`, respectively.
