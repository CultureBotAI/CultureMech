# YAML Record Review: Methanobacterium Medium (III)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_medium_iii.yaml
- Started UTC: 2026-09-24T02:58:23Z
- Finished UTC: 2026-09-24T02:58:58Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:010240 |
| Label | methanobacterium_medium_iii |
| Original label | Methanobacterium Medium (III) |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_medium_iii.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M827_Methanobacterium_Medium_III.yaml` |
| Merge lineage | `TOGO_M827_Methanobacterium_Medium_III` |
| Source identity | TOGO Medium M827 / JCM Medium 794 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_medium_iii.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_medium_iii.yaml --out /private/tmp/methanobacterium_medium_iii.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_medium_iii.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_medium_iii.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

The generated record identifies TOGO M827, the TOGO import of JCM Medium 794, `METHANOBACTERIUM MEDIUM (III)`. The live JCM Medium 794 page, the TOGO M827 API, and the MediaDive J794 REST record all agree on the JCM 794 source identity and on the core formula. The generated merge contains one TOGO source owner, `TOGO_M827_Methanobacterium_Medium_III`.

An exact hidden- and ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, and `scripts` for `TOGO:M827`, `JCM_M794`, `GRMD=794`, and `mediadive.medium:J794` found this TOGO owner plus a separate normalized MediaDive J794 owner at `data/normalized_yaml/archaea/methanobacterium_medium_iii.yaml`.

## Evidence

JCM 794 and TOGO M827 support the basal salts, 2.5 g NaHCO3, 0.2 g yeast extract, 0.8 g sodium acetate, 10 ml trace vitamins, 10 ml trace minerals, 1 mg resazurin, and 1 L distilled water. The YAML preserves the gram-valued basal rows but stores 1 L water, 1 mg resazurin, 10 ml trace vitamins, 10 ml trace minerals, and 10 ml 5% Na2S x 9 H2O as `G_PER_L` concentrations.

The source lists both post-autoclave reducing stocks under the same sterile anaerobic stock-addition paragraph: 10 ml 5% L-cysteine HCl H2O and 10 ml 5% Na2S x 9 H2O per liter. The YAML handles them inconsistently: sulfide is an empty anonymous `solutions` row, while cysteine remains a top-level `ingredients` row with value `10 G_PER_L`.

The source preparation text requires boiling the basal components, cooling and dispensing under H2-CO2 80:20, sealing and autoclaving, adding anaerobic stocks autoclaved under N2, and pressurizing inoculated vessels to 150 kPa H2-CO2 80:20. None of those steps are present in structured `preparation_steps`; H2, CO2, and N2 have instead been parsed as variable final-medium ingredients.

## Completeness

The empty optional slots for growth evidence and organism targets were not treated as defects. The inspected JCM, TOGO, and MediaDive records are source formulations, not primary growth studies.

The generated TOGO/JCM record also duplicates a normalized MediaDive J794 owner and the generated `data/merge_yaml/merged/methanobacterium_medium_iii__4905ae80.yaml` record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Several non-gram quantities were imported as gram-per-liter concentrations. | JCM 794 gives 1 L water, 1 mg resazurin, 10 ml trace vitamins, 10 ml trace minerals, and 10 ml 5% Na2S x 9 H2O; the YAML stores all five with `unit: G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M827_Methanobacterium_Medium_III.yaml`, or the TOGO unit parser. |
| major | Post-autoclave stock additions are incomplete and inconsistently scoped. | The source adds both 5% L-cysteine HCl H2O and 5% Na2S x 9 H2O as 10 ml sterile anaerobic stock additions; the YAML leaves sulfide as an empty `solutions` stub and promotes cysteine to a final ingredient. | `data/normalized_yaml/archaea/TOGO_M827_Methanobacterium_Medium_III.yaml`, or the TOGO solution migrator. |
| major | Trace stock references are empty anonymous solutions. | The trace-vitamin and trace-mineral rows reference TOGO M190 and M142 / JCM Medium 197 and 151, but the YAML has `composition: []`, `name: Unknown solution`, no stock composition, and no internal link for either row. | `data/normalized_yaml/archaea/TOGO_M827_Methanobacterium_Medium_III.yaml`, or the TOGO solution migrator. |
| major | Gas-atmosphere requirements were modeled as variable final ingredients. | JCM 794 uses H2-CO2 80:20 for cooling, dispensing, and final pressurization, and N2 only as the atmosphere for autoclaving anaerobic stock solutions; the generated record lists H2, CO2, and N2 as ordinary `ingredients`. | `data/normalized_yaml/archaea/TOGO_M827_Methanobacterium_Medium_III.yaml`, or the TOGO importer. |
| major | Preparation and pressure details were dropped. | JCM 794 contains explicit boiling, cooling, dispensing, sealing, autoclaving, sterile-stock addition, and 150 kPa pressurization instructions. The YAML has no structured fields for those claims. | `data/normalized_yaml/archaea/TOGO_M827_Methanobacterium_Medium_III.yaml`, or the TOGO comment importer. |
| major | The same JCM recipe is represented by a duplicate MediaDive owner. | `data/normalized_yaml/archaea/methanobacterium_medium_iii.yaml` also imports JCM Medium 794 through MediaDive J794 and renders as `data/merge_yaml/merged/methanobacterium_medium_iii__4905ae80.yaml`. | Merge/de-duplication logic for JCM media imported through both MediaDive and TOGO. |

## Recommended Edits

1. Preserve trace vitamins, trace minerals, 5% L-cysteine HCl H2O, and 5% Na2S x 9 H2O as structured stock additions with 10 ml addition volumes.
2. Preserve the 5% stock concentrations for the cysteine and sulfide stocks instead of promoting their 10 ml addition volumes to `G_PER_L`.
3. Preserve 1 L water and 1 mg resazurin without converting them to `G_PER_L`.
4. Move H2-CO2 and N2 out of final `ingredients` and into preparation or atmosphere fields scoped to cooling, dispensing, final pressurization, and stock autoclaving.
5. Add the JCM 794 preparation sequence and 150 kPa final pressurization to the maintained TOGO M827 owner.
6. Reconcile this TOGO M827 owner with the MediaDive J794 owner so JCM Medium 794 has one canonical merged output.
7. Regenerate `data/merge_yaml/merged/methanobacterium_medium_iii.yaml` from corrected normalized inputs.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected TOGO M827 owner and regenerated merged file.
2. Compare the regenerated recipe against JCM Medium 794, TOGO M827, and MediaDive J794 to confirm that all four stock additions remain stocks and that all gas atmospheres are scoped to preparation.
3. Re-run an exact duplicate search for `TOGO:M827`, `mediadive.medium:J794`, and `GRMD=794` across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.
4. Render or inspect the generated page to confirm the sterile cysteine and sulfide additions display together as post-autoclave stock additions.

## Additional Notes

None found.
