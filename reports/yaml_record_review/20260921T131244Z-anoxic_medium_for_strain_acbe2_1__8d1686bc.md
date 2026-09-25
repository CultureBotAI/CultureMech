# YAML Record Review: ANOXIC MEDIUM FOR STRAIN AcBE2-1

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/anoxic_medium_for_strain_acbe2_1__8d1686bc.yaml
- Started UTC: 2026-09-21T13:12:14Z
- Finished UTC: 2026-09-21T13:12:44Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002801` / `anoxic_medium_for_strain_acbe2_1` in `data/merge_yaml/merged/anoxic_medium_for_strain_acbe2_1__8d1686bc.yaml`.

- The generated record was produced by `merge_recipes.py` from `anoxic_medium_for_strain_acbe2_1.yaml`.
- The maintained owner is `data/normalized_yaml/bacterial/anoxic_medium_for_strain_acbe2_1.yaml`.
- An ignored-inclusive exact search across `data`, `.claude`, and `reports` for `CultureMech:002801`, `mediadive.medium:J451`, `mediadive_4198_Main_sol_J451`, `anoxic_medium_for_strain_acbe2_1__8d1686bc`, `ANOXIC MEDIUM FOR STRAIN AcBE2-1`, and `GRMD=451` found this normalized JCM/MediaDive owner, the generated merge, the associated `mediadive_4198_Main_sol_J451` solution record, registry/catalog/index rows, and the parallel TOGO M451 record reviewed immediately before this one.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/anoxic_medium_for_strain_acbe2_1__8d1686bc.yaml` through the Python 3.11 no-project workaround | Pass; no issues found. |
| `python scripts/validate_strict.py data/merge_yaml/merged/anoxic_medium_for_strain_acbe2_1__8d1686bc.yaml --out /private/tmp/anoxic_j451.strict.tsv --workers 1 --quiet` through the Python 3.11 no-project workaround | Pass; 1 file scanned and 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/anoxic_medium_for_strain_acbe2_1__8d1686bc.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` through the Python 3.11 no-project workaround | Pass; 0 reference checks were discovered. |
| `linkml-term-validator validate-data data/merge_yaml/merged/anoxic_medium_for_strain_acbe2_1__8d1686bc.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` through the Python 3.11 no-project workaround | Pass; only the known `eutils` `pkg_resources` deprecation warning was emitted. |
| Embedded `MediaRecipe.curation_history` | Not checked: the documented `just validate-history` gate targets standalone files under `history/`, not embedded history on one generated merge record. |

The documented `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` wrappers were not rerun directly because project-level `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails before any target-specific validation begins. The equivalent LinkML/strict/reference/term checks above were run with `uv run --no-project --python /usr/local/bin/python3.11`.

## Identity and Grounding

The normalized owner and generated merge identify a JCM/MediaDive import of JCM medium 451, `ANOXIC MEDIUM FOR STRAIN AcBE2-1`. The live JCM `GRMD=451` URL now returns a `Nothing found` page, so the exact JCM source cited in this record could not be re-read. The live TOGO M451 API still carries the same old JCM M451 source identity, the same pH 7.2, and the same source comments, so it corroborates the medium identity even though it is a sibling import rather than this MediaDive import.

The base salts use the correct ChEBI terms for NaCl, MgCl2 hexahydrate, KH2PO4, KCl, NH4Cl, calcium chloride dihydrate, sodium sulfate, and sodium nitrate. Several stock-derived terms also use the right chemical identities, but `NiCl2 x 6 H2O` is grounded to `CHEBI:34887` / `nickel dichloride`, which omits the source hexahydrate. The `HCl` row denotes the 25 percent HCl component of M433 Trace element solution SL-10, not pure hydrogen chloride, so `CHEBI:17883` is too narrow for that stock solution row.

## Evidence

The first eight ingredient quantities are consistent with the MediaDive main-solution normalization in `data/normalized_yaml/bacterial/mediadive_4198_Main_sol_J451.yaml`: those salts were divided by the recorded `Original volume: 1032 mL`. The record also preserved pH 7.2 and the M451 sodium acetate / estradiol comments, which match the live TOGO M451 API.

The remaining direct ingredient rows are stock-solution formulas flattened into the final medium without the 1 ml/L or 0.5 ml/L dilution. JCM/TOGO M431 defines the selenite-tungstate stock, JCM/TOGO M433 defines Trace element solution SL-10, and JCM/TOGO M562 defines the 7 Vitamins stock. Those pages support the stock recipes, not the final-medium `G_PER_L` concentrations now present for FeCl2, ZnCl2, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, Na2MoO4, NaOH, Na2SeO3, Na2WO4, Vitamin B12, D-Biotin, D-Calcium pantothenate, thiamine, p-aminobenzoic acid, nicotinic acid, or pyridoxine.

## Completeness

The record is not complete as a stock-aware recipe. It lacks structured links to the three referenced external stock solutions and retains the 84 g/L NaHCO3 addition as an empty `Unknown solution` with `30 G_PER_L`, even though the source addition is 30 ml. It also moves the SL-10-specific preparation note, `Dissolve FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining salts.`, to a root-level `preparation_steps` entry.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml/merged`, the registries, and `reports/media_content_review_manifest.tsv` for `TOGO_M433`, `TOGO_M431`, `TOGO_M562`, `mediadive_4198_Main_sol_J451`, and `mediadive_4379_7_Vitamins_solution` found local records for the cross-referenced TOGO media, the MediaDive J451 main solution, and a MediaDive 7 Vitamins solution. These can seed future repairs without treating the generated merge as authoritative.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Stock-local trace metal, selenite-tungstate, and vitamin concentrations were flattened into final-medium ingredients at stock strength. | The J451 medium adds 1 ml/L SL-10, 1 ml/L selenite-tungstate, and 0.5 ml/L 7 Vitamins stocks, but rows such as FeCl2 1.5 `G_PER_L`, NaOH 0.4 `G_PER_L`, and Pyridoxine hydrochloride 0.5 `G_PER_L` are the stock recipes from M433/M431/M562, not final-medium concentrations. The repository's exact plausibility report also flags this record for one trace salt and four vitamin-scale slips. | `data/normalized_yaml/bacterial/anoxic_medium_for_strain_acbe2_1.yaml` and the MediaDive stock flattener. |
| major | The remaining NaHCO3 stock addition has the wrong unit and no composition. | Source M451 and the associated MediaDive `Main sol. J451` stock both treat `84 g/L NaHCO3 solution` as a 30 ml addition, but the generated record stores `value: '30'`, `unit: G_PER_L`, `composition: []`, and `name: Unknown solution`. | `data/normalized_yaml/bacterial/anoxic_medium_for_strain_acbe2_1.yaml` or the solution migrator that moved this row. |
| major | A stock-local preparation instruction is attached to the root recipe. | The generated `DISSOLVE` step describes preparing M433 Trace element solution SL-10 by dissolving FeCl2 in HCl, not preparation of M451's final medium; it should belong to that referenced stock solution or disappear behind a structured stock reference. | MediaDive stock import for `mediadive_4198_Main_sol_J451` and normalized J451. |
| major | The duplicate TOGO and MediaDive imports of JCM 451 remain separate generated media. | `CultureMech:002801` and `CultureMech:009838` cite the same JCM medium number and same human label but generate `anoxic_medium_for_strain_acbe2_1__8d1686bc.yaml` and `anoxic_medium_for_strain_acbe2_1.yaml` separately because their stock modeling diverged. | Merge fingerprint rules after both normalized source records are stock-aware. |
| major | `NiCl2 x 6 H2O` is grounded to an anhydrous ChEBI term. | The source row says nickel chloride hexahydrate, but the normalized row links `CHEBI:34887` / `nickel dichloride`, losing the hydrate. | `data/normalized_yaml/bacterial/anoxic_medium_for_strain_acbe2_1.yaml`. |

## Recommended Edits

1. In the MediaDive J451 owner or its import transform, replace flattened M433/M431/M562 stock ingredients with structured stock additions at 1 ml/L, 1 ml/L, and 0.5 ml/L.
2. Preserve `84 g/L NaHCO3 solution` as a 30 ml addition to final medium, not as `30 G_PER_L`, and populate or link its sodium bicarbonate composition.
3. Move the FeCl2-in-HCl preparation note from root M451 preparation to the SL-10 stock record.
4. Correct `NiCl2 x 6 H2O` to a hexahydrate ChEBI term or leave it unresolved if the exact ID cannot be verified during curation.
5. Reconcile this MediaDive/JCM J451 import with `data/normalized_yaml/bacterial/TOGO_M451_Anoxic_Medium_For_Strain_AcBE2-1.yaml`, then regenerate merges so one JCM 451 medium remains.

## Follow-up Checks

- Rerun focused open-schema, strict, reference, and term validation on `data/normalized_yaml/bacterial/anoxic_medium_for_strain_acbe2_1.yaml`.
- Rerun concentration plausibility on the repaired record and confirm the J451 rows no longer emit `TRACE_SALT_AS_STOCK` or `INDICATOR_UNIT_SLIP` findings.
- Rerun `just verify-merges` and `just audit-merge-freshness` after reconciling the TOGO and MediaDive J451 records.
- Re-run an ignored-inclusive exact search for `mediadive.medium:J451`, `TOGO_M451`, and `GRMD=451` to make sure only expected maintained inputs feed the final merged M451 page.

## Additional Notes

Optional `target_organisms` were left empty. The medium title names strain AcBE2-1, but neither the stale JCM URL nor the MediaDive-normalized record supplies a narrow taxon assertion.
