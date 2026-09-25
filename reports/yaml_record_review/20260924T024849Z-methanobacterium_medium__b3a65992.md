# YAML Record Review: Methanobacterium Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_medium__b3a65992.yaml
- Started UTC: 2026-09-24T02:48:49Z
- Finished UTC: 2026-09-24T02:49:27Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:008231 |
| Label | methanobacterium_medium |
| Original label | Methanobacterium Medium |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_medium__b3a65992.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M1673_Methanobacterium_Medium.yaml` |
| Merge lineage | `TOGO_M1673_Methanobacterium_Medium` |
| Source identity | TOGO `M1673`, original source `NBRC_M878` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_medium__b3a65992.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_medium__b3a65992.yaml --out /private/tmp/methanobacterium_medium__b3a65992.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows; the TSV contained only its header. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_medium__b3a65992.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_medium__b3a65992.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

The generated record identifies the intended NBRC/TOGO source: TOGO M1673 reports `Methanobacterium Medium`, original medium ID `NBRC_M878`, and the NBRC medium 878 URL. NBRC medium 878 has the same formulation. The generated file was last merged from the single maintained owner `data/normalized_yaml/archaea/TOGO_M1673_Methanobacterium_Medium.yaml`.

An accession-focused gitignore-independent search over `data/normalized_yaml` and `data/merge_yaml/merged` for `TOGO:M1673|M1673|NBRC_M878|NBRCMediumDetailServlet?NO=878` found this normalized owner, the reviewed generated record, and index references to this same owner. The search included ignored and hidden files.

## Evidence

TOGO and NBRC support the top-level medium as 1 L distilled water, 0.75 g KH2PO4, 1 g NH4Cl, 0.75 g K2HPO4, 1 mg resazurin, 0.36 g MgCl2 x 6 H2O, 0.5 g Na2S x 9 H2O, 4 g NaHCO3, 0.1 g Bacto Yeast Extract, 0.5 g cysteine-HCl, 0.1 g Polypeptone, 10 ml trace-elements solution, and 10 ml vitamin solution.

The source keeps trace-elements and vitamin stocks separate. The trace stock contains its own 1 L water, CaCl2 x 2 H2O, Na2MoO4 x 2 H2O, H3BO3, MnCl2 x 4 H2O, CoCl2 x 6 H2O, NiCl2 x 6 H2O, ZnCl2, FeCl3 x 6 H2O, NTA, and NaOH adjustment; the vitamin stock contains milligram quantities of B vitamins in 1 L water.

NBRC supplies anaerobic preparation instructions: autoclave the main medium without vitamin solution, cysteine-HCl, or Na2S x 9 H2O under H2/CO2 at 80/20; separately autoclave cysteine-HCl and Na2S x 9 H2O as 5% solutions under N2; then add the filter-sterile vitamin solution plus cysteine and sulfide solutions and pressurize inoculated bottles to 150 kPa with H2/CO2.

## Completeness

The generated record is stale relative to the owner: the reviewed merge still has 3.0 g/L distilled water from three identical rows, while `data/normalized_yaml/archaea/TOGO_M1673_Methanobacterium_Medium.yaml` has a 2026-09-02 repair event and stores that row as 1.0 g/L.

The owner still needs source-level repair because trace-stock and vitamin-stock rows are flattened into the final ingredient list and the 10 ml addition volumes are encoded as `10 G_PER_L` empty solution stubs.

The empty optional slots for growth evidence and organism targets were not treated as defects. This source is a medium recipe page rather than a primary growth experiment.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated record is stale relative to the normalized owner. | The reviewed merge has 3.0 g/L distilled water from three source waters. The maintained owner has a later `repair_merged_duplicates.py` event and stores that row as 1.0 g/L. | Regenerate `data/merge_yaml/merged/methanobacterium_medium__b3a65992.yaml` from `data/normalized_yaml/archaea/TOGO_M1673_Methanobacterium_Medium.yaml`. |
| major | Trace and vitamin stock additions were converted to empty gram-per-liter solution stubs. | TOGO/NBRC specify 10 ml trace-elements solution and 10 ml vitamin solution. The YAML stores both under `solutions` with empty composition, `Unknown solution` names, and `10 G_PER_L` concentrations. | `data/normalized_yaml/archaea/TOGO_M1673_Methanobacterium_Medium.yaml`, or the TOGO import and solution-migration code. |
| major | Trace and vitamin stock contents were flattened into final ingredients. | All trace salts, NTA, NaOH, and all vitamin-stock rows appear as top-level ingredients even though the source puts them in nested one-liter stock solutions. | `data/normalized_yaml/archaea/TOGO_M1673_Methanobacterium_Medium.yaml`, or the TOGO stock parser. |
| major | Source units and preparation context are missing or unsupported. | The source lists 1 mg resazurin and milligram vitamin-stock quantities, while the YAML stores the same numbers as `G_PER_L`. NBRC preparation for H2/CO2 autoclaving, 5% cysteine and sulfide stocks, filter-sterile vitamins, and 150 kPa H2/CO2 pressurization is absent. | `data/normalized_yaml/archaea/TOGO_M1673_Methanobacterium_Medium.yaml`, or the TOGO unit and preparation importers. |

## Recommended Edits

1. Rebuild the TOGO M1673 owner from TOGO/NBRC with the direct final-medium ingredients and the two supported 10 ml stock additions.
2. Move trace and vitamin members out of top-level `ingredients` into stock-solution records or inline stock compositions.
3. Restore source units, keeping resazurin and vitamin-stock rows as milligram quantities in their source-supported contexts.
4. Add structured preparation steps for H2/CO2 autoclaving, 5% cysteine-HCl and Na2S x 9 H2O stocks under N2, filter-sterile vitamin addition, and 150 kPa H2/CO2 pressurization.
5. Regenerate `data/merge_yaml/merged/methanobacterium_medium__b3a65992.yaml` from the corrected normalized owner instead of editing the generated merge directly.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected normalized owner and regenerated merged file.
2. Compare the regenerated record to TOGO M1673 and NBRC medium 878 to verify the two stocks are represented as 10 ml additions and not final gram-per-liter rows.
3. Re-run an accession-focused duplicate search for TOGO M1673 and NBRC 878 across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.
4. Render or inspect the generated medium page to confirm gases and NaOH appear only in source-supported preparation or stock context.

## Additional Notes

None found.
