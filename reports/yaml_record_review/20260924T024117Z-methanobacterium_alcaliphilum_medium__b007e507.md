# YAML Record Review: Methanobacterium alcaliphilum medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_alcaliphilum_medium__b007e507.yaml
- Started UTC: 2026-09-24T02:41:02Z
- Finished UTC: 2026-09-24T02:42:23Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:008422 |
| Label | methanobacterium_alcaliphilum_medium |
| Original label | Methanobacterium alcaliphilum medium |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_alcaliphilum_medium__b007e507.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M1848_Methanobacterium_alcaliphilum_medium.yaml` |
| Merge lineage | `TOGO_M1848_Methanobacterium_alcaliphilum_medium` |
| Source identity | TOGO `M1848`, original source `NBRC_M1083` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_alcaliphilum_medium__b007e507.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_alcaliphilum_medium__b007e507.yaml --out /private/tmp/methanobacterium_alcaliphilum_medium__b007e507.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows; the TSV contained only its header. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_alcaliphilum_medium__b007e507.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_alcaliphilum_medium__b007e507.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

The generated record identifies the intended NBRC/TOGO source: TOGO M1848 reports the name `Methanobacterium alcaliphilum medium`, original medium ID `NBRC_M1083`, and source URL for NBRC medium 1083. NBRC medium 1083 is the same formulation. The generated record comes from exactly one maintained normalized owner, `data/normalized_yaml/archaea/TOGO_M1848_Methanobacterium_alcaliphilum_medium.yaml`.

An exact gitignore-independent search over `data/normalized_yaml` and `data/merge_yaml/merged` for `Methanobacterium alcaliphilum medium|methanobacterium_alcaliphilum_medium` found this TOGO/NBRC owner and a distinct DSMZ/KOMODO medium-342 owner group. That second group renders to `data/merge_yaml/merged/METHANOBACTERIUM_ALCALIPHILUM_MEDIUM.yaml`; it is a related source variant, not an extra owner for this `b007e507` generated record.

## Evidence

The TOGO API and NBRC source both support the top-level NBRC recipe as 760 ml distilled water, 0.1 g CaCl2 x 2 H2O, 1 g NH4Cl, 0.4 g K2HPO4, 1 mg resazurin, 0.1 g MgCl2 x 6 H2O, 2 g Bacto Yeast Extract, 2 g Polypeptone, 210 ml carbonate mixture, 10 ml Tris-HCl buffer, 10 ml vitamin solution, 10 ml trace-elements solution, 0.3 g cysteine-HCl, and 0.3 g Na2S x 9 H2O.

The inspected sources support four nested solution boundaries that the YAML no longer preserves:

| Source component | Source amount | YAML representation |
|---|---:|---|
| Carbonate mixture | 210 ml added to the final medium; made from 10 g NaHCO3 and 0.5 g Na2CO3 in 210 ml water | Empty solution with `210 G_PER_L`; NaHCO3 and Na2CO3 also appear as top-level final-medium ingredients. |
| Tris-HCl buffer | 10 ml added to the final medium; 2 M Tris adjusted to pH 8.4 with HCl and autoclaved under N2 | Empty solution with `10 G_PER_L`; Tris, HCl, and N2 also appear as variable top-level ingredients. |
| Vitamin solution | 10 ml added to the final medium from a one-liter stock containing milligram vitamin quantities | Empty solution with `10 G_PER_L`; each milligram stock ingredient also appears as a gram-per-liter final-medium ingredient. |
| Trace elements solution | 10 ml added to the final medium from a one-liter stock containing gram and milligram mineral quantities | Empty solution with `10 G_PER_L`; every trace-stock salt appears as a gram-per-liter final-medium ingredient. |

The record omits the NBRC procedure: the main solution should be autoclaved under H2 except for carbonate mixture, Tris-HCl buffer, vitamin solution, cysteine-HCl, and Na2S x 9 H2O; carbonate mixture, Tris-HCl buffer, 3% cysteine-HCl, and 3% Na2S x 9 H2O should be autoclaved separately under N2; the vitamin solution should be filter sterile; and inoculated vessels should be pressurized to 150 kPa with H2.

## Completeness

The source formulation is materially incomplete in the YAML because the preparation text, gas-atmosphere context, separate 3% cysteine and sulfide additions, Tris-HCl pH adjustment, carbonate stock, vitamin stock, and trace-element stock boundaries are missing or encoded as final ingredients.

The empty optional slots for growth evidence and organism targets were not treated as defects. This source is a medium recipe page rather than a primary growth experiment, and no inspected source in this review would support a narrower strain-level growth claim.

The exact duplicate search included ignored and hidden files under `data/normalized_yaml` and `data/merge_yaml/merged`; it found no additional exact `Methanobacterium alcaliphilum medium` owners beyond the TOGO/NBRC owner and the separate DSMZ/KOMODO 342 group described above.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Stock solution additions were converted to empty solutions with gram-per-liter addition amounts. | TOGO/NBRC specify 210 ml carbonate mixture plus 10 ml each of Tris-HCl buffer, vitamin solution, and trace-elements solution. The YAML stores those as `210`, `10`, `10`, and `10 G_PER_L` under `solutions`, with empty `composition` arrays. | `data/normalized_yaml/archaea/TOGO_M1848_Methanobacterium_alcaliphilum_medium.yaml`, or the TOGO import and solution-migration code that produced the normalized structure. |
| major | Stock contents were flattened into the final medium, and duplicate water and CaCl2 were summed across unrelated formulation levels. | TOGO/NBRC put NaHCO3 and Na2CO3 inside the carbonate mixture, Tris and HCl inside the Tris-HCl buffer protocol, vitamins inside a one-liter stock, and trace salts inside a one-liter stock. The YAML lists all of them as top-level final-medium ingredients; it also reports 972 g/L distilled water from `760.0, 210.0, 1.0, 1.0` and 0.23 g/L CaCl2 x 2 H2O from `0.1, 0.13`. | `data/normalized_yaml/archaea/TOGO_M1848_Methanobacterium_alcaliphilum_medium.yaml`, plus duplicate-merging logic before regeneration. |
| major | Several units and dimensions are unsupported by the source. | The source has resazurin as 1 mg in the final medium and vitamin-stock rows such as 2 mg biotin and 0.01 mg vitamin B12 in 1 L of stock, but the YAML stores them as `G_PER_L`. It also stores source solution volumes in milliliters as `G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M1848_Methanobacterium_alcaliphilum_medium.yaml`, or the TOGO unit parser. |
| major | Preparation, sterilization, gas, and pH instructions are missing from structured recipe fields. | NBRC supplies H2 and N2 autoclave atmospheres, separate 3% cysteine-HCl and sulfide solutions, filter-sterile vitamin addition, 150 kPa H2 pressurization, and Tris-HCl adjustment to pH 8.4. The YAML has no `preparation_steps`, and N2/H2 appear only as variable ingredients. | `data/normalized_yaml/archaea/TOGO_M1848_Methanobacterium_alcaliphilum_medium.yaml`, or the TOGO preparation importer. |

## Recommended Edits

1. Rebuild the TOGO M1848 normalized owner from the NBRC/TOGO source as a top-level medium with 760 ml water, the supported gram and milligram direct ingredients, and four solution additions with milliliter volumes instead of gram-per-liter concentrations.
2. Represent the carbonate, Tris-HCl, vitamin, and trace-element stocks as nested solution records or inline compositions so their members remain separate from final-medium ingredients.
3. Remove flattened stock members from the final ingredient list, undo cross-level duplicate merges for water and CaCl2 x 2 H2O, and preserve source units before converting only dimensionally valid amounts.
4. Add structured preparation steps for the H2/N2 atmospheres, separate autoclaving, filter-sterile vitamin addition, Tris-HCl pH 8.4 adjustment, 3% cysteine/sulfide stocks, and 150 kPa H2 pressurization.
5. Regenerate `data/merge_yaml/merged/methanobacterium_alcaliphilum_medium__b007e507.yaml` from the corrected normalized owner instead of editing the generated merge directly.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected normalized owner and regenerated merged file.
2. Manually compare the regenerated YAML to NBRC medium 1083 and TOGO M1848 to ensure every final-medium ingredient and every stock ingredient remains in the source-supported compartment with a source-supported unit.
3. Re-run a duplicate search for the exact medium name and slug across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files, before linking this TOGO/NBRC recipe to the separate DSMZ/KOMODO 342 variant group.
4. Render or inspect the generated medium page to verify the carbonate, Tris-HCl, vitamin, and trace-element stocks display as stock additions rather than final gram-per-liter rows.

## Additional Notes

None found.
