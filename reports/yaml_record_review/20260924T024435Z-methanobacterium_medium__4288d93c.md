# YAML Record Review: Methanobacterium Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacterium_medium__4288d93c.yaml
- Started UTC: 2026-09-24T02:44:35Z
- Finished UTC: 2026-09-24T02:45:09Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:008407 |
| Label | methanobacterium_medium |
| Original label | Methanobacterium Medium |
| Category | archaea |
| Generated path | `data/merge_yaml/merged/methanobacterium_medium__4288d93c.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M1834_Methanobacterium_Medium.yaml` |
| Merge lineage | `TOGO_M1834_Methanobacterium_Medium` |
| Source identity | TOGO `M1834`, original source `NBRC_M1067` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacterium_medium__4288d93c.yaml` | Passed with no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacterium_medium__4288d93c.yaml --out /private/tmp/methanobacterium_medium__4288d93c.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and 0 error rows; the TSV contained only its header. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacterium_medium__4288d93c.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacterium_medium__4288d93c.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known eutils/pkg_resources warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in a merged recipe. |

The repository's documented `just` validators were not used because this checkout's uv resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. The equivalent focused validators above ran with Python 3.11 against the generated record.

## Identity and Grounding

The generated record identifies the intended TOGO/NBRC source: TOGO M1834 reports `Methanobacterium Medium`, original medium ID `NBRC_M1067`, and the NBRC medium 1067 URL. NBRC medium 1067 is the same formulation. The generated file was last merged from the single maintained owner `data/normalized_yaml/archaea/TOGO_M1834_Methanobacterium_Medium.yaml`.

An accession-focused gitignore-independent search over `data/normalized_yaml/archaea` and the reviewed merged file for `TOGO:M1834|M1834|NBRC_M1067|NBRCMediumDetailServlet?NO=1067|Methanobacterium Medium` found this owner and several other TOGO Methanobacterium media with the same display label or Roman-numeral variants. The reviewed record is specifically TOGO M1834 / NBRC 1067 and should not be conflated with those sibling TOGO accessions.

## Evidence

The TOGO API and NBRC source both support the top-level NBRC recipe as 1 L distilled water, 0.147 g CaCl2 x 2 H2O, 0.136 g KH2PO4, 0.54 g NH4Cl, 1 mg resazurin, 0.2 g MgCl2 x 6 H2O, 0.5 g Na2S x 9 H2O, 2.5 g NaHCO3, 0.8 g sodium acetate, 0.2 g Bacto Yeast Extract, 0.5 g cysteine-HCl, 10 ml vitamin solution, and 10 ml trace-element solution.

The source also supports a one-liter vitamin stock made from milligram-scale vitamins and a one-liter trace-element stock made from mineral salts plus NaOH pH adjustment. Those are nested stocks, not final-medium gram-per-liter ingredients.

NBRC additionally supplies preparation text: omit vitamin solution, cysteine-HCl, and Na2S x 9 H2O during the main autoclave; autoclave the main mixture under H2/CO2 at 80/20; sterilize concentrated cysteine-HCl and sodium sulfide separately under N2; add filter-sterile vitamin solution, cysteine-HCl, and Na2S x 9 H2O before inoculation; and pressurize inoculated vessels to 150 kPa with H2/CO2 at 80/20.

## Completeness

The merged record is stale relative to its owner: `data/normalized_yaml/archaea/TOGO_M1834_Methanobacterium_Medium.yaml` has a 2026-09-02 `repair_merged_duplicates.py` event that collapsed the three identical water rows back to one `1.0 G_PER_L` row, while the generated record still has `3.0 G_PER_L` and only the older 2026-08-06 merge event.

The current owner still needs curation because it retains 10 ml vitamin solution and 10 ml trace-element solution as `10 G_PER_L` empty solution stubs, keeps vitamin and trace-stock members as top-level ingredients, and has no source-supported preparation steps.

The empty optional slots for growth evidence and organism targets were not treated as defects. This source is a medium recipe page rather than a primary growth experiment, and no inspected source in this review would support a narrower strain-level growth claim.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated record is stale relative to the normalized owner. | The reviewed merge has 3.0 g/L distilled water from three collapsed rows. The maintained TOGO owner has a later 2026-09-02 repair event and stores that water row as 1.0 g/L. | Regenerate `data/merge_yaml/merged/methanobacterium_medium__4288d93c.yaml` from `data/normalized_yaml/archaea/TOGO_M1834_Methanobacterium_Medium.yaml`. |
| major | Vitamin and trace-element stock additions were converted to empty gram-per-liter solution stubs. | TOGO/NBRC specify 10 ml vitamin solution and 10 ml trace-element solution. The YAML stores both under `solutions` with empty composition, `Unknown solution` names, and `10 G_PER_L` concentrations. | `data/normalized_yaml/archaea/TOGO_M1834_Methanobacterium_Medium.yaml`, or the TOGO import and solution-migration code. |
| major | Stock contents were flattened into the final ingredient list. | TOGO/NBRC put biotin, p-aminobenzoic acid, thiamine-HCl, Ca-pantothenate, pyridoxine-HCl, folic acid, vitamin B12, riboflavin, and nicotinic acid inside the vitamin stock, and mineral salts plus NaOH inside the trace stock. The YAML lists those rows as top-level final-medium ingredients. | `data/normalized_yaml/archaea/TOGO_M1834_Methanobacterium_Medium.yaml`, or the TOGO stock parser. |
| major | Units and preparation context are unsupported or missing. | The source has 1 mg resazurin in the final medium and milligram quantities in the one-liter vitamin stock, while the YAML represents those source numbers as `G_PER_L`. NBRC also provides anaerobic H2/CO2 and N2 sterilization, filter-sterile vitamin addition, and 150 kPa H2/CO2 pressurization steps that the YAML omits. | `data/normalized_yaml/archaea/TOGO_M1834_Methanobacterium_Medium.yaml`, or the TOGO unit and preparation importers. |

## Recommended Edits

1. Rebuild the TOGO M1834 normalized owner from the NBRC/TOGO source so the final recipe has the direct medium ingredients and two stock additions with milliliter volumes.
2. Represent the vitamin and trace-element stocks as nested solution records or inline compositions rather than top-level final-medium ingredients.
3. Remove the flattened vitamin and trace-stock members from the final ingredient list, undo the cross-level CaCl2 x 2 H2O merge, and preserve milligram units from resazurin and the vitamin stock.
4. Add structured preparation steps for H2/CO2 autoclaving, separate N2 sterilization of cysteine-HCl and sodium sulfide, filter-sterile vitamin addition, and 150 kPa H2/CO2 pressurization.
5. Regenerate `data/merge_yaml/merged/methanobacterium_medium__4288d93c.yaml` from the corrected normalized owner instead of editing the generated merge directly.

## Follow-up Checks

1. Rerun open-schema, strict, term, and reference validation against the corrected normalized owner and regenerated merged file.
2. Compare the regenerated record to TOGO M1834 and NBRC medium 1067 to verify all vitamin and trace-stock ingredients remain in their source-supported stock contexts.
3. Re-run an accession-focused duplicate search for TOGO M1834, NBRC 1067, the exact label, and the slug across `data/normalized_yaml` and `data/merge_yaml/merged`, including ignored and hidden files.
4. Render or inspect the generated medium page to confirm that the vitamin and trace-element stocks display as 10 ml additions rather than final gram-per-liter rows.

## Additional Notes

None found.
