# YAML Record Review: medium_for_strain_ja363_ja395_and_ja418

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_strain_ja363_ja395_and_ja418.yaml
- Started UTC: 2026-09-24T01:50:58Z
- Finished UTC: 2026-09-24T01:51:30Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/medium_for_strain_ja363_ja395_and_ja418.yaml` |
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:008405` |
| Label | `medium_for_strain_ja363_ja395_and_ja418` |
| Original name | `Medium for strain JA363, JA395 and JA418` |
| Category | `bacterial` |
| Source accession | `TOGO:M1832` |
| Maintained owner | `data/normalized_yaml/bacterial/medium_for_strain_ja363_ja395_and_ja418.yaml` |
| Generated status | Generated merge from one TOGO/NBRC import, with `merge_fingerprint` `25918b0c04fe2312b4c9239fa33d9d20ee39e5d1723385500ea53be4b277db7c` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_strain_ja363_ja395_and_ja418.yaml` | Passed: exited 0 with no diagnostics after printing `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/medium_for_strain_ja363_ja395_and_ja418.yaml --out /private/tmp/medium_for_strain_ja363_ja395_and_ja418.strict.tsv --workers 1 --quiet` | Passed. The TSV had 1 line, so it contained only the header and 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/medium_for_strain_ja363_ja395_and_ja418.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/medium_for_strain_ja363_ja395_and_ja418.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

- The record identity agrees with TOGO M1832 and NBRC Medium 1065: both inspected sources name `Medium for strain JA363, JA395 and JA418`, and the normalized record preserves the NBRC URL and `NBRC_M1065` pointer.
- The generated record is a direct copy of `data/normalized_yaml/bacterial/medium_for_strain_ja363_ja395_and_ja418.yaml` plus the generated merge event, `merge_fingerprint`, and `merged_from` fields.
- An exact, gitignore-independent search that included ignored and hidden files for `TOGO:M1832`, `M1832`, `NBRC_M1065`, the NBRC URL marker `NO=1065`, the label, and the slug found only the generated record and its direct normalized owner.

## Evidence

Supported claims:

- The simple final-medium solutes match NBRC and TOGO: KH2PO4 0.5 g/l, MgSO4 x 7 H2O 2 g/l, NaCl 20 g/l, NH4Cl 0.6 g/l, CaCl2 x 2 H2O 0.15 g/l, sodium pyruvate 3 g/l, yeast extract 0.3 g/l, peptone 0.3 g/l, and Na2S x 9 H2O 0.24 g/l.
- The source supports a complex/undefined liquid medium because yeast extract and peptone are direct ingredients.

Unsupported or over-scoped claims:

- `NaHCO3 (10% (w/v))` is a 10 ml/l addition in NBRC, but it is modeled as a 10 `G_PER_L` ingredient.
- `Ferric citrate solution* (0.1%)` and `Trace element solution SL7**` are 5 ml/l and 1 ml/l additions in NBRC, but the `solutions` entries store 5 and 1 `G_PER_L` with `Unknown solution` names and empty compositions.
- The SL7 stock recipe is flattened into final-medium ingredients. NBRC defines HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and 990 ml water as a local trace-element solution.
- Several SL7 milligram quantities were imported as grams per liter: ZnCl2 70 mg became 70 `G_PER_L`, MnCl2 x 4 H2O 100 mg became 100 `G_PER_L`, and Na2MoO4 x 2 H2O 40 mg became 40 `G_PER_L`.
- Source pH 8, N2-atmosphere autoclaving, separate Na2S x 9 H2O autoclaving, NaHCO3 filter sterilization, and aseptic anaerobic post-autoclave additions are absent. The N2 atmosphere is represented only as a variable ingredient.

## Completeness

- The direct main recipe is incomplete until the bicarbonate and ferric citrate additions are expressed with `ML_PER_L` units.
- The trace-element recipe is incomplete until SL7 has a local composition and no SL7 constituents remain as top-level final-medium ingredients.
- The derived `high_metal: true` flag should be re-evaluated after stock rows are nested; it appears to be driven by SL7 stock components being treated as final-medium masses.
- `target_organisms` and strain-level growth evidence are empty. That is acceptable for this pass because the inspected NBRC and TOGO sources provide formulation data and do not report growth measurements for the named strains.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Volume additions were migrated as grams per liter. | NBRC M1065 lists 10 ml/l 10% NaHCO3, 5 ml/l ferric citrate, and 1 ml/l SL7; the YAML represents the first as a 10 `G_PER_L` ingredient and the latter two as `G_PER_L` solution entries. | `data/normalized_yaml/bacterial/medium_for_strain_ja363_ja395_and_ja418.yaml`; TOGO importer stock handling if source-owned. |
| Major | SL7 was flattened into stock-strength top-level ingredients. | The NBRC-local SL7 recipe has HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and 990 ml water; the YAML stores the chemical rows as final `G_PER_L` ingredients. | `data/normalized_yaml/bacterial/medium_for_strain_ja363_ja395_and_ja418.yaml`. |
| Major | pH and anaerobic preparation are missing. | NBRC gives final pH 8, autoclaving under N2, separate Na2S x 9 H2O autoclaving under N2, NaHCO3 filter sterilization, and aseptic anaerobic post-autoclave additions; the YAML has no pH or preparation steps. | `data/normalized_yaml/bacterial/medium_for_strain_ja363_ja395_and_ja418.yaml`. |
| Minor | Two hydrated chloride salts are not grounded to exact hydrated CHEBI terms. | CoCl2 x 6 H2O is linked to cobalt dichloride and NiCl2 x 6 H2O is linked to nickel dichloride. | `data/normalized_yaml/bacterial/medium_for_strain_ja363_ja395_and_ja418.yaml`, followed by MediaIngredientMech enrichment. |

## Recommended Edits

1. Rebuild `data/normalized_yaml/bacterial/medium_for_strain_ja363_ja395_and_ja418.yaml` so 10% NaHCO3, 0.1% ferric citrate, and SL7 are represented as volume additions with `ML_PER_L`.
2. Move all SL7 chemicals into an inline `Trace element solution SL7` composition or an equivalent local `SolutionRecipe`, preserving mg versus g quantities and the 990 ml water basis.
3. Add pH 8 and preparation steps for N2 autoclaving, separate Na2S autoclaving, NaHCO3 filtration, and anaerobic aseptic additions before inoculation.
4. Reground CoCl2 x 6 H2O and NiCl2 x 6 H2O to exact hydrated classes where available.
5. Regenerate the merged YAML and derived pages after normalized curation.

## Follow-up Checks

- Re-run the focused open-schema, strict, reference, and term validators on the normalized owner and regenerated merge.
- Confirm the regenerated top-level ingredient list no longer contains HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, or Na2MoO4 x 2 H2O.
- Verify the final solution additions are exactly 10 ml/l NaHCO3, 5 ml/l Ferric citrate solution, and 1 ml/l Trace element solution SL7.
- Compare the regenerated record against NBRC Medium 1065 for final pH and anaerobic preparation instructions.

## Additional Notes

- The generated and normalized records have the same formulation defects; the merge itself is not stale.
- The source-specific `Soluble in hot water` note belongs to ferric citrate handling, not to the final medium as a whole.
