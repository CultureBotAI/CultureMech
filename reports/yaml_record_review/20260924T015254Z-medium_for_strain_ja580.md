# YAML Record Review: medium_for_strain_ja580

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_strain_ja580.yaml
- Started UTC: 2026-09-24T01:52:12Z
- Finished UTC: 2026-09-24T01:52:54Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/medium_for_strain_ja580.yaml` |
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:008492` |
| Label | `medium_for_strain_ja580` |
| Original name | `Medium for Strain JA580` |
| Category | `bacterial` |
| Source accession | `TOGO:M1914` |
| Maintained owners | `data/normalized_yaml/bacterial/medium_for_strain_ja580.yaml`, `data/normalized_yaml/bacterial/medium_for_strain_ja480.yaml` |
| Generated status | Generated merge from two TOGO/NBRC imports, with `merge_fingerprint` `b5139ec43f52ad882f1e769b0cda4bd18377ec424dc6a1d9762ac18d94bef076` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_strain_ja580.yaml` | Passed: no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/medium_for_strain_ja580.yaml --out /private/tmp/medium_for_strain_ja580.strict.tsv --workers 1 --quiet` | Passed. The TSV had 1 line, so it contained only the header and 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/medium_for_strain_ja580.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/medium_for_strain_ja580.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

- The generated record resolves to TOGO M1914 / NBRC Medium 1176, `Medium for Strain JA580`, but its visible formula is a hybrid that has JA480 values for at least MgSO4 x 7 H2O, NaCl, and CaCl2 x 2 H2O.
- NBRC Medium 1176 and TOGO M1914 support the JA580 identity and list MgSO4 x 7 H2O 2 g/l, NaCl 10 g/l, and CaCl2 x 2 H2O 0.15 g/l.
- NBRC Medium 1117 and TOGO M1872 support JA480 and list MgSO4 x 7 H2O 0.5 g/l, NaCl 0.4 g/l, and CaCl2 x 2 H2O 0.25 g/l.
- `data/normalized_yaml/bacterial/NBRC_1118.yaml` is a more curated direct NBRC Medium 1117 record for the JA480 side, with pH 6.6 to 7.4 and a nested SL7 trace-element solution.
- An exact, gitignore-independent search that included ignored and hidden files for `TOGO:M1914`, `TOGO:M1872`, `NBRC_M1176`, `NBRC_M1117`, `NO=1176`, `NO=1117`, the two strain slugs, and the JA480/JA580 source labels found the generated merge, the two TOGO normalized owners, and the direct NBRC 1117 owner.

## Evidence

Supported claims:

- Both JA480 and JA580 NBRC/TOGO tables support KH2PO4 0.5 g/l, NH4Cl 0.68 g/l, sodium pyruvate 0.5 g/l, sodium succinate 0.5 g/l, sodium acetate 0.5 g/l, yeast extract 0.5 g/l, Na2S x 9 H2O 0.24 g/l, 1 mg/l resazurin, 15 ml/l 10% NaHCO3, 1 ml/l Vitamin B12, 5 ml/l 0.1% ferric citrate, and 1 ml/l Trace element solution SL7.

Unsupported or over-scoped claims:

- JA480 and JA580 are not the same formula. Merging them under the JA580 identity erases the JA580 MgSO4, NaCl, and CaCl2 concentrations.
- 15 ml/l NaHCO3, 1 ml/l Vitamin B12, 5 ml/l ferric citrate, and 1 ml/l SL7 are stored as `G_PER_L` quantities or empty solution entries instead of `ML_PER_L` additions.
- The SL7 stock recipe is flattened into final-medium ingredients with milligram stock amounts imported as grams per liter.
- Water from the final recipe and SL7 stock is collapsed into one 991 `G_PER_L` ingredient.
- Final pH 6.6 to 7.4 and the N2 anaerobic, Na2S autoclaving, vitamin B12/NaHCO3 filter-sterilization, and aseptic anaerobic addition steps are absent.

## Completeness

- The generated record is not complete enough to publish as a canonical JA580 merge because it carries a JA480 formula and JA480 synonym under a JA580 source accession.
- The existing TOGO JA480 and JA580 owners are both incomplete because both still flatten the same SL7 stock and post-autoclave additions.
- `target_organisms` and strain-level growth evidence are empty. That is acceptable for this pass because the inspected NBRC and TOGO sources provide formulation data and do not report growth measurements for JA480 or JA580.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | JA480 was merged into JA580 even though the recipes differ. | NBRC 1176 / TOGO M1914 uses 2 g/l MgSO4 x 7 H2O, 10 g/l NaCl, and 0.15 g/l CaCl2 x 2 H2O; NBRC 1117 / TOGO M1872 uses 0.5 g/l, 0.4 g/l, and 0.25 g/l respectively. The generated JA580 record carries the JA480 values. | Merge grouping for `data/normalized_yaml/bacterial/medium_for_strain_ja480.yaml` and `data/normalized_yaml/bacterial/medium_for_strain_ja580.yaml`. |
| Major | Volume additions were migrated as grams per liter. | NBRC lists 15 ml/l 10% NaHCO3, 1 ml/l 0.002% Vitamin B12, 5 ml/l 0.1% ferric citrate, and 1 ml/l SL7; the YAML stores them as `G_PER_L` entries or `G_PER_L` solutions. | Both normalized TOGO owners; TOGO importer stock handling if source-owned. |
| Major | SL7 was flattened into stock-strength top-level ingredients. | The NBRC-local SL7 recipe has HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and 990 ml water; the generated YAML stores the chemical rows directly. | Both normalized TOGO owners. |
| Major | pH and anaerobic preparation are missing. | The source gives final pH 6.6 to 7.4, N2 autoclaving, separate Na2S x 9 H2O autoclaving under N2, vitamin B12 and NaHCO3 filtration, and aseptic anaerobic additions before inoculation; none are represented as pH or preparation steps. | Both normalized TOGO owners. |
| Minor | Two hydrated chloride salts are not grounded to exact hydrated CHEBI terms. | CoCl2 x 6 H2O is linked to cobalt dichloride and NiCl2 x 6 H2O is linked to nickel dichloride. | Both normalized TOGO owners, followed by MediaIngredientMech enrichment. |

## Recommended Edits

1. Split `medium_for_strain_ja480` out of the JA580 merge and regenerate `data/merge_yaml/merged/medium_for_strain_ja580.yaml` with only the TOGO M1914 / NBRC 1176 source formula.
2. Link or merge the JA480 TOGO source with the curated direct `data/normalized_yaml/bacterial/NBRC_1118.yaml` representation of NBRC Medium 1117 rather than with JA580.
3. Repair both TOGO owners so Vitamin B12, NaHCO3, ferric citrate, and SL7 are volume additions with `ML_PER_L` units.
4. Move all SL7 chemicals into a local `Trace element solution SL7` composition, preserving mg versus g quantities and the 990 ml water basis.
5. Add pH 6.6 to 7.4 and the source anaerobic autoclaving, filtration, and post-autoclave addition instructions.
6. Regenerate merged YAML and derived pages after the normalized duplicate and stock repairs.

## Follow-up Checks

- Re-run the focused open-schema, strict, reference, and term validators on the repaired normalized owners and regenerated merges.
- Verify the regenerated JA580 top-level formula has 2 g/l MgSO4 x 7 H2O, 10 g/l NaCl, and 0.15 g/l CaCl2 x 2 H2O.
- Verify `medium_for_strain_ja480` and `TOGO:M1872` no longer appear in the JA580 generated record.
- Compare TOGO M1914 / NBRC 1176 and TOGO M1872 / NBRC 1117 row by row before accepting any future duplicate merge.

## Additional Notes

- The same TOGO stock-flattening defect is present in both normalized source records; the blocker is specifically the false duplicate relation between those records.
- The direct NBRC 1117 record shows the shape the JA480 side should eventually follow: corrected volume additions, a nested SL7 composition, final pH, and preparation steps.
