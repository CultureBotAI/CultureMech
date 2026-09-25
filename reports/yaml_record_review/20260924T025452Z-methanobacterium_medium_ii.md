# YAML Record Review: Methanobacterium Medium (II)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_medium_ii.yaml
- Started UTC: 2026-09-24T02:53:08Z
- Finished UTC: 2026-09-24T02:54:53Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:010132 |
| Label | methanobacterium_medium_ii |
| Original label | Methanobacterium Medium (II) |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_medium_ii.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M724_Methanobacterium_Medium_II.yaml` |
| Merge lineage | `TOGO_M724_Methanobacterium_Medium_II` |
| Source identity | TOGO Medium M724 / JCM Medium 702 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_medium_ii.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_medium_ii.yaml --out /private/tmp/methanobacterium_medium_ii.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_medium_ii.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_medium_ii.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

The generated record identifies the intended source recipe. The TOGO API for M724 reports the name `Methanobacterium Medium (II)`, original source `JCM_M702`, source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=702`, and pH 7.0; the live JCM Medium 702 page has the same medium number and title. The generated merge contains one source owner, `TOGO_M724_Methanobacterium_Medium_II`.

A direct `find` lookup under `data/normalized_yaml`, which includes gitignored files, resolved the maintained TOGO M724 owner at `data/normalized_yaml/archaea/TOGO_M724_Methanobacterium_Medium_II.yaml`. An exact hidden- and ignored-inclusive search over `data/normalized_yaml` and `data/merge_yaml/merged` for `TOGO:M190`, `JCM_M197`, `TOGO_M142_Pyrococcus_Medium`, and the M190/M142 slugs confirmed that the referenced TOGO M142 and TOGO M190 source records are present in the normalized corpus.

## Evidence

JCM Medium 702 and TOGO M724 support the direct ingredient list stored in the record, but not all encoded units. The source formula uses 1 L distilled water, 0.5 mg resazurin, 10 ml trace minerals, 10 ml trace vitamins, 25 ml 8% NaHCO3 solution, and 10 ml 3% Na2S x 9 H2O solution per liter; the YAML stores those rows as `1`, `0.5`, `10`, `10`, `25`, and `10 G_PER_L`.

The stock-solution boundary was retained only as four empty `solutions` entries. The source explicitly refers the trace minerals to TOGO M142 / JCM Medium 151, refers the trace vitamins to TOGO M190 / JCM Medium 197, and gives separate post-autoclave bicarbonate and sulfide stock additions, but the YAML stores `composition: []`, `name: Unknown solution`, and no structured stock recipe, stock concentration, or internal source link for any of those four additions.

The hydrogen and carbon dioxide rows are unsupported as final ingredients. In the JCM page they describe the H2-CO2 gas phase used while cooling and dispensing the medium and the final 200 kPa H2-CO2 pressurization after inoculation.

The source preparation comments were not migrated. The JCM page says to bring the basal components to a boil, cool under H2-CO2 80:20, dispense under the same gas mix, seal with butyl rubber stoppers, autoclave, add sterile anaerobic stocks, check the finished medium at about pH 7.0, and pressurize inoculated bottles to 200 kPa H2-CO2 80:20. The YAML has no `preparation_steps`, `sterilization`, gas-atmosphere, pressure, or pH representation.

## Completeness

The empty optional slots for growth evidence and organism targets were not treated as defects. The inspected JCM page and TOGO API record are source formulations, not primary growth studies.

The trace-mineral and trace-vitamin cross-references are source-supported and TOGO-resolvable, but the M724 owner is incomplete because it leaves those rows as anonymous, empty solution stubs rather than exact stock additions copied from or linked to the referenced stock definitions.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Several non-gram quantities were imported as gram-per-liter concentrations. | The source gives 1 L water and 0.5 mg resazurin in the basal formula, plus 10 ml trace minerals, 10 ml trace vitamins, 25 ml bicarbonate stock, and 10 ml sulfide stock as additions. The YAML stores each of those values with `unit: G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M724_Methanobacterium_Medium_II.yaml`, or the TOGO unit parser. |
| major | Stock additions are empty anonymous solutions. | The four `solutions` entries have `composition: []` and `name: Unknown solution`; two of them point only to TOGO M142/M190 in free text, and the 8% NaHCO3 and 3% Na2S x 9 H2O stocks keep their stock percentages only inside `preferred_term` strings. | `data/normalized_yaml/archaea/TOGO_M724_Methanobacterium_Medium_II.yaml`, or the TOGO solution migrator. |
| major | H2-CO2 atmosphere requirements were modeled as variable final ingredients. | JCM Medium 702 uses H2-CO2 80:20 for cooling, dispensing, and final bottle pressurization; the generated record represents `Carbon dioxide gas` and `Hydrogen gas` as ordinary `ingredients`. | `data/normalized_yaml/archaea/TOGO_M724_Methanobacterium_Medium_II.yaml`, or the TOGO importer. |
| major | Preparation, sterilization, pH, and pressure details were dropped. | JCM Medium 702 contains explicit boiling, cooling, dispensing, sealing, autoclaving, sterile-stock addition, final pH, and 200 kPa pressurization instructions. The YAML has no structured fields for those claims. | `data/normalized_yaml/archaea/TOGO_M724_Methanobacterium_Medium_II.yaml`, or the TOGO comment importer. |

## Recommended Edits

1. Preserve source units for water, resazurin, and milliliter stock additions instead of coercing them to `G_PER_L`.
2. Replace the four empty `solutions` stubs with structured stock additions for trace minerals, trace vitamins, 8% NaHCO3, and 3% Na2S x 9 H2O.
3. Represent the TOGO M142/JCM 151 trace minerals and TOGO M190/JCM 197 trace vitamins as exact referenced stock compositions, not as anonymous name-only rows.
4. Move H2-CO2 out of final `ingredients` and into preparation or atmosphere fields that preserve the 80:20 gas mix and 200 kPa inoculated-bottle pressurization.
5. Add the JCM M702 preparation sequence, autoclave step, sterile anaerobic additions, and final pH check to the maintained TOGO M724 owner.
6. Regenerate `data/merge_yaml/merged/methanobacterium_medium_ii.yaml` from the corrected normalized input.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected TOGO M724 owner and regenerated merged file.
2. Compare the regenerated recipe against JCM Medium 702 and the TOGO M724 API to confirm that every gram, milligram, milliliter, stock percentage, pH, and gas-atmosphere claim remains source-supported.
3. Inspect the TOGO M142 and TOGO M190 stock definitions to confirm trace minerals and trace vitamins resolve to the exact JCM cross-reference rows required by Medium 702.
4. Render or inspect the generated page to confirm the bicarbonate and sulfide stock additions display as post-autoclave additions rather than gram-per-liter ingredients.

## Additional Notes

The M142 and M190 identifiers in the TOGO API are not typos: TOGO M142 maps to JCM Medium 151, and TOGO M190 maps to JCM Medium 197.
