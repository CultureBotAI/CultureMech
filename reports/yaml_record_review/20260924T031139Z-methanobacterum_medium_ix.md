# YAML Record Review: Methanobacterum Medium (IX)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterum_medium_ix.yaml
- Started UTC: 2026-09-24T03:10:55Z
- Finished UTC: 2026-09-24T03:11:38Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:007757 |
| Label | methanobacterum_medium_ix |
| Original label | Methanobacterum Medium (IX) |
| Category | bacterial |
| Generated path | `data/merge_yaml/merged/methanobacterum_medium_ix.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M1229_Methanobacterum_Medium_IX.yaml` |
| Merge lineage | `TOGO_M1229_Methanobacterum_Medium_IX` |
| Source identity | TOGO `M1229`; JCM Medium 1147 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterum_medium_ix.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterum_medium_ix.yaml --out /private/tmp/methanobacterum_medium_ix.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterum_medium_ix.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterum_medium_ix.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

This generated record is the TOGO import of JCM Medium 1147. TOGO M1229 preserves JCM's misspelled `Methanobacterum Medium (IX)` label and points at the live JCM `GRMD=1147` page.

An exact hidden- and ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, and `scripts` for `TOGO:M1229`, `JCM_M1147`, `GRMD=1147`, `TOGO_M1229_Methanobacterum_Medium_IX`, `methanobacterum_medium_ix`, and `CultureMech:007757` found this TOGO owner and generated file plus a separate MediaDive/JCM duplicate, `data/normalized_yaml/bacterial/methanobacterum_medium_ix.yaml` and `data/merge_yaml/merged/methanobacterum_medium_ix__66b5a244.yaml`.

## Evidence

JCM 1147 lists a 922 ml distilled-water base with seven milliliter-scale stock additions: 1 ml FeCl2 solution, 1 ml trace element solution, 20 ml fatty acid mixture, 0.5 ml selenite-tungstate solution, 50 ml 8% NaHCO3 solution, 6.3 ml 50% methanol, and two 10 ml 5% reductant additions.

The generated record stores the 922 ml water row as `922 G_PER_L` and the 0.5 mg resazurin row as `0.5 G_PER_L`. All seven milliliter stock additions are present as either top-level ingredients or empty `solutions`, but every stock amount is recorded as `G_PER_L`, including 20 ml fatty acid mixture, 50 ml 8% NaHCO3, 6.3 ml 50% methanol, 0.5 ml selenite-tungstate, and the two 10 ml reductant additions.

No preparation text survived the TOGO import. The live JCM page says to autoclave under N2-CO2, add selenite-tungstate, bicarbonate, and methanol stocks after cooling, distribute the medium under H2-CO2, add sulfide and cysteine stocks before inoculation, readjust pH to 7.5 if necessary, and pressurize the inoculated culture vessels to 100 kPa H2-CO2.

Gas-handling hints became ingredients. The generated record publishes `Carbon dioxide gas`, `Nitrogen gas`, `N2`, and `Hydrogen gas` as variable ingredients even though the gases occur only in the N2-CO2 autoclaving atmosphere, H2-CO2 distribution and pressure atmosphere, and N2 stock-storage condition.

The category is also suspicious. The record lives under `data/normalized_yaml/bacterial`, but this JCM 1147 source is part of the Methanobacterium medium series reviewed with archaeal methanogen recipes.

## Completeness

The empty optional organism-target and growth-evidence slots were not treated as defects. JCM 1147, TOGO M1229, and the MediaDive J1147 duplicate are formulation sources, not primary growth studies.

The record needs a full stock-boundary repair before it is a usable M1229 representation. Unlike a simple missing annotation, the current row units change the measured amounts of water, resazurin, methanol, bicarbonate stock, and every anaerobic stock addition.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | Milliliter and milligram source amounts are stored as grams per liter. | JCM 1147 lists 922 ml water, 0.5 mg resazurin, 20 ml fatty acid mixture, 50 ml 8% NaHCO3, 6.3 ml 50% methanol, 0.5 ml selenite-tungstate, and two 10 ml reductant additions; the generated record stores those as `G_PER_L` values. | `data/normalized_yaml/bacterial/TOGO_M1229_Methanobacterum_Medium_IX.yaml` |
| blocker | Seven stock additions are empty solution stubs or final ingredients instead of structured post-autoclave additions. | FeCl2, trace element, fatty-acid, bicarbonate, selenite-tungstate, sulfide, and cysteine stocks all have empty `composition` arrays or final-ingredient rows, even though the source places them in two post-autoclave addition tables. | `data/normalized_yaml/bacterial/TOGO_M1229_Methanobacterum_Medium_IX.yaml` |
| blocker | All source preparation instructions are missing. | The generated record has no `preparation_steps`, while JCM 1147 distinguishes autoclaving under N2-CO2, adding three anaerobic stocks after cooling, distributing under H2-CO2, adding two reductant stocks before inoculation, readjusting pH to 7.5, and pressurizing to 100 kPa. | `data/normalized_yaml/bacterial/TOGO_M1229_Methanobacterum_Medium_IX.yaml` |
| major | Anaerobic gases were promoted to recipe ingredients. | `Carbon dioxide gas`, `Nitrogen gas`, `N2`, and `Hydrogen gas` appear as variable ingredients, but the JCM source only uses gases for anaerobic handling and stock storage. | TOGO import handling for `data/normalized_yaml/bacterial/TOGO_M1229_Methanobacterum_Medium_IX.yaml` |
| minor | The same JCM 1147 source has a separate MediaDive duplicate. | An exact hidden/ignored search found the MediaDive owner and generated file `methanobacterum_medium_ix__66b5a244.yaml` with the same `GRMD=1147` source URL. | De-duplication between TOGO and MediaDive JCM imports. |
| minor | The normalized owner is filed under `bacterial`, even though it is a methanogen medium from the Methanobacterium series. | The TOGO owner path is `data/normalized_yaml/bacterial/...`, while the neighboring Methanobacterium medium records are archaeal methanogen recipes. | `data/normalized_yaml/bacterial/TOGO_M1229_Methanobacterum_Medium_IX.yaml` |

## Recommended Edits

1. Restore the JCM volume and mass units for water, resazurin, 50% methanol, and every stock addition.
2. Model FeCl2, trace element, fatty-acid, 8% NaHCO3, selenite-tungstate, 5% Na2S x 9 H2O, and 5% L-Cysteine HCl x H2O as stock additions, not `G_PER_L` final rows.
3. Add the missing JCM preparation sequence, including N2-CO2 autoclaving, H2-CO2 distribution, pre-inoculation reductant additions, pH 7.5 readjustment, and 100 kPa H2-CO2 pressurization.
4. Move gas requirements to preparation or anaerobic handling metadata and remove them from `ingredients`.
5. Review the category and normalized path; this record likely belongs under `archaea`, not `bacterial`.
6. Merge the corrected TOGO M1229 and MediaDive J1147 owners as true source duplicates, then regenerate `data/merge_yaml/merged/methanobacterum_medium_ix.yaml`.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against both corrected normalized owners and regenerated merged files.
2. Compare the regenerated record against JCM 1147 to confirm all stock additions retain milliliter units and resazurin remains 0.5 mg/L.
3. Re-run exact duplicate searches for `TOGO:M1229`, `JCM_M1147`, and `GRMD=1147` across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.
4. Inspect the generated page to confirm the medium is filed and rendered with the intended archaeal context.

## Additional Notes

None found.
