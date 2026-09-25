# YAML Record Review: METHANOBACTERIUM VT MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_vt_medium.yaml
- Started UTC: 2026-09-24T03:09:42Z
- Finished UTC: 2026-09-24T03:10:25Z
- Verdict: pass with minor issues

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:015840 |
| Label | methanobacterium_vt_medium |
| Original label | METHANOBACTERIUM VT MEDIUM |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_vt_medium.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/JCM_J1362_METHANOBACTERIUM_VT_MEDIUM.yaml` |
| Merge lineage | `JCM_J1362_METHANOBACTERIUM_VT_MEDIUM` |
| Source identity | `jcm.grmd:1362`; JCM Medium 1362 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_vt_medium.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_vt_medium.yaml --out /private/tmp/methanobacterium_vt_medium.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_vt_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_vt_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

This generated record is a direct JCM scrape of JCM Medium 1362. The generated `jcm.grmd:1362` identifier, stable ID, normalized owner, and live JCM `GRMD=1362` page all point to `METHANOBACTERIUM VT MEDIUM`.

An exact hidden- and ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, and `scripts` for `jcm.grmd:1362`, `GRMD=1362`, `JCM_J1362_METHANOBACTERIUM_VT_MEDIUM`, `methanobacterium_vt_medium`, and `CultureMech:015840` found only the expected normalized owner and this generated file.

## Evidence

The generated ingredient amounts match the live JCM table: 0.14 g K2HPO4, 0.34 g KCl, 0.4 g MgCl2 x 6 H2O, 0.35 g MgSO4 x 7 H2O, 0.25 g NH4Cl, 0.14 g CaCl2 x 2 H2O, 4.4 g NaCl, 10 ml Wolfe's mineral solution from Medium 265, 10 ml trace vitamins from Medium 197, 2.5 g NaHCO3, 1 g yeast extract, 1 g Trypticase peptone, 0.5 mg resazurin, 980 ml distilled water, and two 10 ml 5% reductant additions.

The milliliter and milligram rows retain their source units as `ML_PER_L` or `MG_PER_L`, so this direct JCM import avoided the older TOGO importer problems that converted water, stock volumes, and resazurin to grams per liter.

The preparation text also matches the source sequence: pH 6.5 before NaHCO3, cooling and dispensing under H2-CO2 at 80:20, overnight standing after autoclaving, anaerobic addition of autoclaved cysteine and Na2S stocks stored under N2, optional adjustment to pH 6.7-7.0, and final pressurization to 200 kPa H2-CO2.

The remaining issue is only structural. The Wolfe's mineral solution and trace-vitamins rows preserve the JCM cross-reference text, but they are not linked to structured JCM Medium 265 or JCM Medium 197 solution records.

## Completeness

The empty optional organism-target and growth-evidence slots were not treated as defects. JCM 1362 is a formulation source, not a primary growth study.

The final medium is usable as a JCM source recipe. It would be easier to audit and render if the two cross-referenced stocks were represented as structured links instead of name-only `ML_PER_L` ingredients.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| minor | Cross-referenced stock solutions are text rows rather than structured linked stocks. | The source references Wolfe's mineral solution in Medium 265 and trace vitamins in Medium 197; the generated record stores both as name-only 10 ml/L ingredients and does not link or expand those stock recipes. | `data/normalized_yaml/archaea/JCM_J1362_METHANOBACTERIUM_VT_MEDIUM.yaml` |

## Recommended Edits

1. Link the Wolfe's mineral solution and trace-vitamins rows to structured JCM Medium 265 and JCM Medium 197 stock records, if those stocks are available in normalized data.
2. Regenerate `data/merge_yaml/merged/methanobacterium_vt_medium.yaml` from the linked normalized owner.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the regenerated file.
2. Compare the regenerated ingredient table against JCM 1362 to confirm the two stock additions remain 10 ml/L and the reductant rows remain 5% 10 ml/L additions.
3. Re-run an exact search for `jcm.grmd:1362`, `GRMD=1362`, and `JCM_J1362_METHANOBACTERIUM_VT_MEDIUM` across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.

## Additional Notes

None found.
