# YAML Record Review: Methanobacterium Medium (IV)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_medium_iv.yaml
- Started UTC: 2026-09-24T03:00:49Z
- Finished UTC: 2026-09-24T03:01:16Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:010331 |
| Label | methanobacterium_medium_iv |
| Original label | Methanobacterium Medium (IV) |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_medium_iv.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M911_Methanobacterium_Medium_IV.yaml` |
| Merge lineage | `TOGO_M911_Methanobacterium_Medium_IV` |
| Source identity | TOGO Medium M911 / JCM Medium 872 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_medium_iv.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_medium_iv.yaml --out /private/tmp/methanobacterium_medium_iv.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_medium_iv.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_medium_iv.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

The generated record identifies TOGO M911, the TOGO import of JCM Medium 872, `METHANOBACTERIUM MEDIUM (IV)`. The live JCM Medium 872 page, the TOGO M911 API, and the MediaDive J872 REST record all agree on the JCM 872 source identity. The generated merge contains one TOGO source owner, `TOGO_M911_Methanobacterium_Medium_IV`.

An exact hidden- and ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, and `scripts` for `TOGO:M911`, `JCM_M872`, `GRMD=872`, and `mediadive.medium:J872` found this TOGO owner plus a separate normalized MediaDive J872 owner at `data/normalized_yaml/archaea/methanobacterium_medium_iv.yaml`.

## Evidence

JCM 872 and TOGO M911 support the gram-valued basal salts, sodium acetate, sodium formate, NaHCO3, 1 mg resazurin, 930 ml water, and six additions with their own preparation boundaries: 1 ml FeCl2 solution, 1 ml trace element solution, 50 ml sludge fluid, 20 ml fatty acid mixture, 10 ml 5% Na2S x 9 H2O, and 10 ml 5% L-cysteine HCl H2O.

The YAML stores all six milliliter additions as gram-per-liter values. FeCl2, trace elements, fatty acids, sulfide, and cysteine are empty anonymous `solutions` entries with values of `1`, `1`, `20`, `10`, and `10 G_PER_L`; sludge fluid remains a top-level `ingredients` row with `50 G_PER_L`.

The sludge-fluid stock recipe was flattened incorrectly. The source makes sludge fluid from anaerobic-digester sludge plus 0.4% yeast extract under N2, with incubation, centrifugation, autoclaving, and dark storage; the YAML preserves only a top-level variable `sludge` ingredient and no sludge-fluid stock composition or preparation.

The source preparation requires adding NaHCO3 after boiling and cooling under H2-CO2 80:20, dispensing under the same gas, autoclaving, adding the five sterile solutions before inoculation, and pressurizing inoculated vessels to 200 kPa H2-CO2 80:20. The generated record has no `preparation_steps`, and H2, CO2, and N2 are represented as variable final-medium ingredients rather than gas atmospheres.

## Completeness

The empty optional slots for growth evidence and organism targets were not treated as defects. The inspected JCM, TOGO, and MediaDive records are source formulations, not primary growth studies.

This generated TOGO/JCM record duplicates a normalized MediaDive J872 owner that imports the same JCM Medium 872 formulation through MediaDive.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Six stock additions were encoded as gram-per-liter concentrations. | JCM 872 gives milliliter additions for FeCl2 solution, trace element solution, sludge fluid, fatty acid mixture, 5% Na2S x 9 H2O, and 5% L-cysteine HCl H2O; the YAML stores their addition volumes as `G_PER_L` values or a `50 G_PER_L` sludge-fluid ingredient. | `data/normalized_yaml/archaea/TOGO_M911_Methanobacterium_Medium_IV.yaml`, or the TOGO unit parser. |
| major | Referenced FeCl2, trace-element, fatty-acid, sulfide, and cysteine stocks are empty anonymous solutions. | Five `solutions` entries have `composition: []` and `name: Unknown solution`, so the M180, M258, sulfide, and cysteine stock definitions are not represented. | `data/normalized_yaml/archaea/TOGO_M911_Methanobacterium_Medium_IV.yaml`, or the TOGO solution migrator. |
| major | Sludge fluid lost its stock composition and preparation boundary. | The source defines a sludge-fluid subrecipe using sludge, 0.4% yeast extract, N2 gassing, 37 C incubation, centrifugation, autoclaving, and dark storage; the YAML has only top-level `Sludge fluid (see below)` and `sludge` ingredient rows. | `data/normalized_yaml/archaea/TOGO_M911_Methanobacterium_Medium_IV.yaml`, or the TOGO subcomponent importer. |
| major | Resazurin and distilled water were imported with mass units. | JCM 872 gives 1 mg resazurin and 930 ml distilled water; the YAML stores `1 G_PER_L` and `930 G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M911_Methanobacterium_Medium_IV.yaml`, or the TOGO unit parser. |
| major | Gas-atmosphere and preparation details were dropped. | JCM 872 specifies H2-CO2 80:20 for cooling, dispensing, and 200 kPa final pressurization, and N2 for stock storage and sludge-fluid preparation; the YAML lists H2, CO2, and N2 as ordinary `ingredients` and has no structured preparation. | `data/normalized_yaml/archaea/TOGO_M911_Methanobacterium_Medium_IV.yaml`, or the TOGO comment importer. |
| major | The same JCM recipe is represented by a duplicate MediaDive owner. | `data/normalized_yaml/archaea/methanobacterium_medium_iv.yaml` also imports JCM Medium 872 through MediaDive J872. | Merge/de-duplication logic for JCM media imported through both MediaDive and TOGO. |

## Recommended Edits

1. Preserve FeCl2 solution, trace element solution, sludge fluid, fatty acid mixture, 5% Na2S x 9 H2O, and 5% L-cysteine HCl H2O as structured additions with their source milliliter addition volumes.
2. Populate or link exact stock definitions for the M180 FeCl2 and trace-element stocks, the M258 fatty acid mixture, the sulfide and cysteine stocks, and the local sludge-fluid stock.
3. Move sludge and 0.4% yeast extract into the sludge-fluid stock composition, with the N2, incubation, centrifugation, autoclave, and storage instructions scoped to sludge fluid.
4. Preserve the 930 ml water and 1 mg resazurin source units instead of coercing them to `G_PER_L`.
5. Move H2, CO2, and N2 out of final `ingredients` and into preparation or atmosphere fields scoped to cooling, dispensing, final pressurization, stock storage, and sludge-fluid preparation.
6. Reconcile this TOGO M911 owner with the MediaDive J872 owner so JCM Medium 872 has one canonical merged output.
7. Regenerate `data/merge_yaml/merged/methanobacterium_medium_iv.yaml` from corrected normalized inputs.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected TOGO M911 owner and regenerated merged file.
2. Compare the regenerated recipe against JCM Medium 872, TOGO M911, and MediaDive J872 to confirm that all stock and sludge-fluid additions remain scoped stocks.
3. Re-run an exact duplicate search for `TOGO:M911`, `mediadive.medium:J872`, and `GRMD=872` across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.
4. Render or inspect the generated page to confirm FeCl2, trace elements, sludge fluid, fatty acids, sulfide, and cysteine display as stock additions rather than gram-per-liter ingredients.

## Additional Notes

None found.
