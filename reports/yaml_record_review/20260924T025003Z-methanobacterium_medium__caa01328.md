# YAML Record Review: Methanobacterium Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_medium__caa01328.yaml
- Started UTC: 2026-09-24T02:50:02Z
- Finished UTC: 2026-09-24T02:50:34Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:008337 |
| Label | methanobacterium_medium |
| Original label | Methanobacterium Medium |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_medium__caa01328.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M1771_Methanobacterium_Medium.yaml` |
| Merge lineage | `TOGO_M1771_Methanobacterium_Medium` |
| Source identity | TOGO `M1771`, original source `NBRC_M986` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_medium__caa01328.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_medium__caa01328.yaml --out /private/tmp/methanobacterium_medium__caa01328.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows; the TSV contained only its header. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_medium__caa01328.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_medium__caa01328.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

The generated record identifies the intended NBRC/TOGO source: TOGO M1771 reports `Methanobacterium Medium`, original medium ID `NBRC_M986`, and the NBRC medium 986 URL. NBRC medium 986 has the same formulation. The generated file was last merged from the single maintained owner `data/normalized_yaml/archaea/TOGO_M1771_Methanobacterium_Medium.yaml`.

An accession-focused gitignore-independent search over `data/normalized_yaml` and `data/merge_yaml/merged` for `TOGO:M1771|M1771|NBRC_M986|NBRCMediumDetailServlet?NO=986` found this normalized owner, the reviewed generated record, and index references to this same owner. The search included ignored and hidden files.

## Evidence

TOGO and NBRC support the final medium as 1 L distilled water, 1 g NaCl, 0.15 g CaCl2 x 2 H2O, 0.2 g KH2PO4, 0.25 g NH4Cl, 1 mg resazurin, 0.4 g MgCl2 x 6 H2O, 0.5 g Na2S x 9 H2O, 0.5 g KCl, 4.8 g NaHCO3, 0.16 g sodium acetate, 0.5 g cysteine-HCl, 2 ml trace-element solution, and 2 ml vitamin solution.

The inspected sources put the trace recipe and vitamin recipe in nested stocks. The trace stock is a one-liter mineral stock with KOH pH adjustment; the vitamin stock is a one-liter stock with milligram quantities of vitamins. The source spelling `Distiled water` inside the trace stock is a typo for water, not a new final-medium ingredient.

NBRC supplies preparation text that omits vitamin solution, NaHCO3, Na2S x 9 H2O, and cysteine-HCl before autoclaving under H2/CO2 at 80/20; separately autoclaves cysteine-HCl and Na2S x 9 H2O as 5% solutions under N2; filter-sterilizes vitamin and 8% NaHCO3 solutions; then aseptically adds those solutions and pressurizes inoculated bottles to 150 kPa with H2/CO2.

## Completeness

The generated record is stale relative to the owner: the reviewed merge still has 2.0 g/L distilled water and 2.0 g/L NaCl from identical duplicate rows, while `data/normalized_yaml/archaea/TOGO_M1771_Methanobacterium_Medium.yaml` has a 2026-09-02 repair event and stores both rows as 1.0 g/L.

The owner still needs curation because the `Distiled water` typo survives as a separate top-level water row, the trace and vitamin stock members are flattened into top-level ingredients, the two stock additions are stored as empty `2 G_PER_L` solution stubs, and all source preparation instructions are absent.

The empty optional slots for growth evidence and organism targets were not treated as defects. This source is a medium recipe page rather than a primary growth experiment.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated record is stale relative to the normalized owner. | The reviewed merge has 2.0 g/L for both distilled water and NaCl from identical duplicate rows. The maintained owner has a later `repair_merged_duplicates.py` event and stores both rows as 1.0 g/L. | Regenerate `data/merge_yaml/merged/methanobacterium_medium__caa01328.yaml` from `data/normalized_yaml/archaea/TOGO_M1771_Methanobacterium_Medium.yaml`. |
| major | Trace and vitamin stock additions were converted to empty gram-per-liter solution stubs. | TOGO/NBRC specify 2 ml trace-element solution and 2 ml vitamin solution. The YAML stores both under `solutions` with empty composition, `Unknown solution` names, and `2 G_PER_L` concentrations. | `data/normalized_yaml/archaea/TOGO_M1771_Methanobacterium_Medium.yaml`, or the TOGO import and solution-migration code. |
| major | Trace and vitamin stock contents were flattened into final ingredients. | The YAML lists the trace mineral salts, NTA, KOH, trace-stock water, and every vitamin row as top-level final-medium ingredients, while TOGO/NBRC place them in nested one-liter stocks. | `data/normalized_yaml/archaea/TOGO_M1771_Methanobacterium_Medium.yaml`, or the TOGO stock parser. |
| major | Source typos and units were preserved in ways that changed semantics. | NBRC's trace-stock `Distiled water` typo became a separate top-level water row instead of a normalized stock water row, and the source's milligram vitamin-stock quantities were stored as top-level `G_PER_L` values. | `data/normalized_yaml/archaea/TOGO_M1771_Methanobacterium_Medium.yaml`, or the TOGO ingredient normalizer and unit parser. |
| major | Preparation instructions are missing. | NBRC describes H2/CO2 autoclaving, 5% cysteine and sulfide stocks, filter-sterile vitamin and 8% NaHCO3 stocks, aseptic anaerobic additions, and 150 kPa H2/CO2 pressurization. The YAML has no preparation steps and carries the gases and KOH only as variable ingredients. | `data/normalized_yaml/archaea/TOGO_M1771_Methanobacterium_Medium.yaml`, or the TOGO preparation importer. |

## Recommended Edits

1. Rebuild the TOGO M1771 owner from TOGO/NBRC with direct final-medium ingredients and two 2 ml stock additions.
2. Normalize `Distiled water` to trace-stock water and move all trace and vitamin members out of top-level `ingredients` into structured stocks.
3. Preserve source milligram units in the vitamin stock, and prevent stock-local NaCl and CaCl2 from being merged with final-medium salts.
4. Add preparation steps for the anaerobic H2/CO2 autoclave, 5% cysteine/sulfide stocks under N2, filter-sterile vitamin and bicarbonate solutions, and post-inoculation H2/CO2 pressurization.
5. Regenerate `data/merge_yaml/merged/methanobacterium_medium__caa01328.yaml` from the corrected normalized owner instead of editing the generated merge directly.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected normalized owner and regenerated merged file.
2. Compare the regenerated record to TOGO M1771 and NBRC medium 986 to verify the two 2 ml stock additions and all final-medium ingredients remain in the right compartments.
3. Re-run an accession-focused duplicate search for TOGO M1771 and NBRC 986 across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.
4. Render or inspect the generated medium page to confirm `Distiled water` no longer appears and the trace and vitamin stocks render as stocks.

## Additional Notes

None found.
