# YAML Record Review: ghiorsea_bivora_medium__ce993dbd

- Repository: CultureMech
- Record: data/merge_yaml/merged/ghiorsea_bivora_medium__ce993dbd.yaml
- Started UTC: 2026-09-23T06:13:19Z
- Finished UTC: 2026-09-23T06:16:11Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:002330` is the direct MediaDive/JCM import for JCM 1158, `GHIORSEA BIVORA MEDIUM`.

The generated record derives from `data/normalized_yaml/bacterial/ghiorsea_bivora_medium.yaml`. An ignored-file-inclusive exact search for `mediadive.medium:J1158`, `JCM_M1158`, and `GRMD=1158'` also found the equivalent Togo M1240 import in `data/normalized_yaml/bacterial/TOGO_M1240_Ghiorsea_Bivora_Medium.yaml` and `data/merge_yaml/merged/GHIORSEA_BIVORA_MEDIUM.yaml`.

## Validation

`linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ghiorsea_bivora_medium__ce993dbd.yaml` passed.

`scripts/validate_strict.py data/merge_yaml/merged/ghiorsea_bivora_medium__ce993dbd.yaml --workers 1 --quiet` exited 0; `/private/tmp/ghiorsea_bivora_medium_ce993dbd.strict.tsv` contained only the header row.

`linkml-reference-validator validate data data/merge_yaml/merged/ghiorsea_bivora_medium__ce993dbd.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` passed with 0 checks.

`linkml-term-validator validate-data data/merge_yaml/merged/ghiorsea_bivora_medium__ce993dbd.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `mediadive.medium:J1158` identity, label, category, defined-medium classification, and liquid state agree with the live JCM 1158 source and the MediaDive REST payload.

The same JCM recipe is split into a separate Togo M1240 generated record.

Most source strings are grounded plausibly. `NiCl2 x 6 H2O` from Wolfe's mineral solution is grounded to `CHEBI:34887`, `nickel dichloride`, which does not preserve the source hexahydrate form.

## Evidence

JCM 1158 defines the main medium as 1 L Artificial saltwater from JCM 629, 1 ml Wolfe's mineral solution from JCM 265, and 1.68 g NaHCO3. After cooling, JCM adds 1 ml filter-sterilized Modified trace vitamins per liter and later adds filter-sterilized 5% H2 and 5% air to the gas phase.

The live JCM 1158 page defines Modified trace vitamins as a 1 L stock with vitamin milligram rows and 0.9 g KH2PO4. The live JCM 629 and JCM 265 pages define the referenced Artificial saltwater and Wolfe's mineral solution stocks.

MediaDive preserves the JCM hierarchy as `Main sol. J1158`, separate `Artificial saltwater`, `Wolfe's mineral solution`, and nested `Trace minerals` solutions, but its J1158 payload also places the Modified trace vitamins rows inside `Main sol. J1158` and gives the main solution a 2002 ml volume.

## Completeness

Artificial saltwater, Wolfe's mineral solution, Trace minerals, and Modified trace vitamins are absent as stock or subrecipe structures in the generated record.

The 1 L water rows from Artificial saltwater, Modified trace vitamins, and Trace minerals are absent.

The N2-CO2 sparging, serum-bottle volume, filter-sterilized post-cooling vitamin addition, H2/air gas-phase supplementation, incubation mode, and every-two-days gas replenishment instructions are retained as text.

Empty growth-evidence, variant, discussion, and publication slots are acceptable for this imported JCM recipe.

## Findings

- Major: The 1 ml Modified trace vitamins addition is represented both as an empty `Modified trace vitamins` 1 g/L ingredient and as direct vitamin/KH2PO4 rows calculated from the stock table against an unsupported 2002 ml main volume.
- Major: Wolfe's mineral solution and nested Trace minerals are flattened at stock strength instead of being scoped to a 1 ml addition; NiCl2 x 6H2O, Na2SeO3, Na2WO4 x 2H2O, nitrilotriacetic acid, MnSO4, FeSO4, CoSO4, ZnSO4, CuSO4, AlK(SO4)2, H3BO3, and Na2MoO4 x 2H2O are all stock-internal rows.
- Major: Duplicate cleanup summed salts from incompatible scopes, including main NaHCO3 with Artificial saltwater NaHCO3, Artificial saltwater KH2PO4 with Modified trace vitamins KH2PO4, and Artificial saltwater salts with Trace minerals salts.
- Major: The MediaDive/JCM J1158 record is split from the equivalent Togo M1240 import.
- Major: Source water rows for the nested 1 L stocks are absent.
- Minor: `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride.

## Recommended Edits

- Preserve Artificial saltwater as a 1 L addition, Wolfe's mineral solution as a 1 ml addition, and Modified trace vitamins as a 1 ml filter-sterilized post-cooling addition in `data/normalized_yaml/bacterial/ghiorsea_bivora_medium.yaml`.
- Keep the Artificial saltwater, Wolfe's mineral solution, Trace minerals, and Modified trace vitamins subrecipes separate, or compute final values only from documented dilution factors while retaining the source boundaries.
- Remove duplicate-merge sums that combine main-medium salts with stock-internal salts.
- Preserve the 1 L water rows in the stock subrecipes as formulation context.
- Re-ground hydrated nickel chloride if an exact term is available.
- Align the MediaDive J1158 and Togo M1240 normalized rows so regeneration merges or explicitly cross-links both archives of `JCM_M1158`.

## Follow-up Checks

- Regenerate the J1158 output and confirm there are no direct final Trace minerals or Modified trace vitamins internal rows at stock strength.
- Confirm there is only one scoped main-medium NaHCO3 row plus separate Artificial saltwater and Wolfe's mineral solution additions.
- Re-run LinkML, strict, reference, and term validation on the regenerated generated YAML.
- Re-run an ignored-file-inclusive exact search for `mediadive.medium:J1158`, `JCM_M1158`, and `TOGO:M1240` to confirm the MediaDive and Togo branches no longer produce split equivalent generated records.

## Additional Notes

The exact source search used `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged`, so ignored generated records and index files were included.
