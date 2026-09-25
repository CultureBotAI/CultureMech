# YAML Record Review: Clostridium thermocellum Medium (D58 Medium)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/clostridium_thermocellum_medium_d58_medium.yaml`
- Started UTC: `2026-09-22T09:53:26Z`
- Finished UTC: `2026-09-22T09:55:07Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:008330` for TOGO Medium `M1765`, generated from `data/normalized_yaml/bacterial/clostridium_thermocellum_medium_d58_medium.yaml` on merge fingerprint `0a6dcf8ff94c00878e0e1958655b0cbeca2d48cde0c972b8d40b9a97adb8a900`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/clostridium_thermocellum_medium_d58.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The source identity is correct: TOGO `M1765` and the generated record both point to NBRC Medium 979, Clostridium thermocellum Medium (D58 Medium), and this branch selects the 10 g cellulose alternative rather than the 5 g cellobiose alternative.

The grounding is incomplete. `Cellulose (Avicel or MN 300)` and `Sodium glycerophosphate` are ungrounded, and `K2HPO4 x 3H2O` is grounded to generic dipotassium hydrogen phosphate rather than to a trihydrate-specific term if one exists.

An ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found a sibling TOGO input, `TOGO_M1766_Clostridium_thermocellum_Medium_D58_Medium.yaml`, for the same NBRC URL and the source tag `NBRC_M979-2`. That cellobiose branch was merged into generated `Modified_D58_medium.yaml` rather than this cellulose branch. Ignored files were included.

## Evidence

NBRC Medium 979 supports the major gram-level rows: 1.3 g `(NH4)2SO4`, 2.6 g `MgCl2 x 6H2O`, 1.43 g `KH2PO4`, 7.2 g `K2HPO4 x 3H2O`, 0.13 g `CaCl2 x 2H2O`, 6 g sodium glycerophosphate, 0.25 g glutathione, 4.5 g yeast extract, 10 g cellulose, and distilled water 1 L.

The same NBRC source gives `FeSO4 x 7H2O` as 1.1 mg and resazurin as 1 mg. TOGO `M1765` also carries those units as `mg`, but the generated record stores both source values as `G_PER_L`, producing 1000x concentration errors.

NBRC Medium 979 also gives an alternative 5 g cellobiose row, pH 7.0-7.2, and this preparation instruction: mix all ingredients except cellobiose, autoclave under N2/CO2 at 80/20, then aseptically and anaerobically add filter-sterile 10% cellobiose solution before inoculation.

## Completeness

The cellulose formula is otherwise complete for the branch imported as TOGO `M1765`.

The generated record omits source pH 7.0-7.2, the N2/CO2 80/20 autoclaving condition, and the filter-sterile cellobiose-addition step. The 5 g cellobiose option from the same NBRC page is not represented as a variant here; it instead exists in the sibling TOGO `M1766` input that merged with NBRC Medium 1287 under `Modified_D58_medium.yaml`.

No target organism or growth evidence is present.

## Findings

- Severe: `FeSO4 x 7H2O` is 1.1 mg in NBRC and TOGO but `1.1 G_PER_L` in the generated record.
- Severe: `Resazurin` is 1 mg in NBRC and TOGO but `1 G_PER_L` in the generated record.
- Major: the pH 7.0-7.2 source range is missing from the generated record.
- Major: NBRC's N2/CO2 80/20 autoclave condition and aseptic anaerobic addition of filter-sterile cellobiose are absent from `preparation_steps`.
- Major: the cellobiose branch from the same NBRC page is split into normalized `CultureMech:008331` and then merged into `Modified_D58_medium.yaml`, making the D58 relationship hard to curate from either generated record.
- Minor: `Cellulose (Avicel or MN 300)`, `Sodium glycerophosphate`, and possibly `K2HPO4 x 3H2O` need more specific grounding.

## Recommended Edits

- Convert `FeSO4 x 7H2O` to `0.0011 G_PER_L` and `Resazurin` to `0.001 G_PER_L`.
- Preserve NBRC pH 7.0-7.2 as a pH range.
- Add preparation steps for autoclaving under N2/CO2 80/20 and aseptic anaerobic addition of a filter-sterilized 10% cellobiose solution.
- Reconcile TOGO `M1765` and `M1766` so the cellulose and cellobiose rows are represented as source variants of NBRC Medium 979 instead of unrelated generated recipes.
- Ground cellulose, sodium glycerophosphate, and the K2HPO4 trihydrate row more specifically where an exact ontology term exists.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm FeSO4 and resazurin remain at 0.0011 and 0.001 g/L.
- Confirm the pH range and N2/CO2 80/20 handling are present.
- Confirm the NBRC Medium 979 cellobiose branch is no longer merged only into `Modified_D58_medium.yaml`.

## Additional Notes

Empty optional fields are not defects. The sibling and duplicate search used ignored-inclusive `rg --no-ignore --hidden` so reports and generated inputs hidden by ignore rules were included.
