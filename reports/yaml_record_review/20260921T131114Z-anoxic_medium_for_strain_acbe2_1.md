# YAML Record Review: Anoxic Medium For Strain AcBE2-1

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/anoxic_medium_for_strain_acbe2_1.yaml
- Started UTC: 2026-09-21T13:08:28Z
- Finished UTC: 2026-09-21T13:11:14Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:009838` / `anoxic_medium_for_strain_acbe2_1` in `data/merge_yaml/merged/anoxic_medium_for_strain_acbe2_1.yaml`.

- The generated record was produced by `merge_recipes.py` from `TOGO_M451_Anoxic_Medium_For_Strain_AcBE2-1.yaml`.
- The maintained owner is `data/normalized_yaml/bacterial/TOGO_M451_Anoxic_Medium_For_Strain_AcBE2-1.yaml`.
- An ignored-inclusive exact search across `data`, `.claude`, and `reports` for `CultureMech:009838`, `TOGO_M451_Anoxic_Medium_For_Strain_AcBE2-1`, `GRMD=451`, the TOGO M451 URL, and `JCM_M451` found the normalized TOGO owner, this generated merge, registry/catalog/index entries, and a separate JCM/MediaDive record at `data/normalized_yaml/bacterial/anoxic_medium_for_strain_acbe2_1.yaml`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/anoxic_medium_for_strain_acbe2_1.yaml` through the Python 3.11 no-project workaround | Pass; no issues found. |
| `python scripts/validate_strict.py data/merge_yaml/merged/anoxic_medium_for_strain_acbe2_1.yaml --out /private/tmp/anoxic_m451.strict.tsv --workers 1 --quiet` through the Python 3.11 no-project workaround | Pass; 1 file scanned and 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/anoxic_medium_for_strain_acbe2_1.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` through the Python 3.11 no-project workaround | Pass; 0 reference checks were discovered. |
| `linkml-term-validator validate-data data/merge_yaml/merged/anoxic_medium_for_strain_acbe2_1.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` through the Python 3.11 no-project workaround | Pass; only the known `eutils` `pkg_resources` deprecation warning was emitted. |
| Embedded `MediaRecipe.curation_history` | Not checked: the documented `just validate-history` gate targets standalone files under `history/`, not embedded history on one generated merge record. |

The documented `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` wrappers were not rerun directly because project-level `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails before any target-specific validation begins. The equivalent LinkML/strict/reference/term checks above were run with `uv run --no-project --python /usr/local/bin/python3.11`.

## Identity and Grounding

The TOGO identity is internally correct: the record points at `TOGO:M451`, labels it `Anoxic Medium For Strain AcBE2-1`, records original source `JCM_M451`, and the live TOGO API for `gm_id=M451` returns the same medium name, same original source accession, original URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=451`, and pH `7.2`.

The current JCM `GRMD=451` URL is source-rotted: it still responds but returns a page body saying `Nothing found` for medium number 451. The Internet Archive CDX query for exact `www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=451` captures with 200 status between 2020 and 2026 returned an empty 3-byte JSON response, so no JCM capture in that bounded query was available to inspect.

The base formulation is grounded to appropriate ChEBI classes for water, NaCl, calcium chloride dihydrate, KH2PO4, NH4Cl, magnesium chloride hexahydrate, KCl, NaNO3, Na2SO4, carbon dioxide, and dinitrogen. The cross-referenced M433, M431, and M562 stock solution names are also real source references: TOGO M433/JCM 433 contains `Trace element solution SL-10`, TOGO M431/JCM 431 contains `Selenite-tungstate solution`, and TOGO M562/JCM 558 contains `7 Vitamins solution`.

## Evidence

Supported by the inspected TOGO M451 API payload:

- Medium identity: M451 is `Anoxic Medium For Strain AcBE2-1`, original source `JCM_M451`.
- Base solution ingredients: `Distilled water` 1 L; `NaCl` 1 g; `CaCl2.2H2O` 0.15 g; `KH2PO4` 0.2 g; `NH4Cl` 0.25 g; `MgCl2.6H2O` 0.4 g; `KCl` 0.5 g; `NaNO3` 0.425 g; `Na2SO4` 0.07 g; carbon dioxide gas; nitrogen gas.
- Follow-on additions: 30 ml `84 g/L NaHCO3 solution`, 1 ml `Trace element solution SL--10 (see Medium [M433])`, 1 ml `Selenite--tungstate solution (see Medium [M431])`, and 0.5 ml `7 Vitamins solution (see Medium [M562])`.
- Conditions/preparation comments: pH 7.2, a sodium acetate vs. `17 beta-estradiol` note, autoclaving/cooling under `N2--CO2 (80:20, v/v)`, and the 28 C dark incubation comment for estradiol substrate vessels.

The final-medium row values copied from TOGO M451 are supported, but the generated representation is incomplete at the preparation and stock boundaries.

## Completeness

The record is incomplete as a runnable recipe. It omits TOGO M451's `ph` value and both source comments, and it keeps every stock addition as `Unknown solution` with empty `composition`. Three of those empty entries have enough cross-reference information to recover their component lists from local normalized TOGO records or live JCM pages:

- `data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml` owns TOGO M433 and includes `Trace element solution SL--10`.
- `data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml` owns TOGO M431 and includes `Selenite--tungstate solution`.
- `data/normalized_yaml/bacterial/TOGO_M562_Magnetospirillum_Medium_A.yaml` owns TOGO M562 and includes `7 Vitamins solution`.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml/merged`, the CultureMech registries, and `reports/media_content_review_manifest.tsv` for `TOGO_M433`, `TOGO_M431`, `TOGO_M562`, `mediadive_4198_Main_sol_J451`, and `mediadive_4379_7_Vitamins_solution` found the three TOGO cross-reference owners plus MediaDive solution records for the J451 main solution and 7 Vitamins solution.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The four stock additions are encoded with mass concentration units instead of source volume additions. | TOGO M451 has 30 ml NaHCO3 stock, 1 ml SL--10, 1 ml selenite-tungstate, and 0.5 ml 7 Vitamins. The generated `solutions` entries keep those numeric values but store each as `G_PER_L`, which makes volume additions dimensionally wrong. | `data/normalized_yaml/bacterial/TOGO_M451_Anoxic_Medium_For_Strain_AcBE2-1.yaml`, or the TOGO solution migrator if this is an importer-wide unit coercion. |
| major | The stock solution rows are placeholders even though the referenced formulations are resolvable. | All four `solutions` have `composition: []` and `name: Unknown solution`; three point to M433, M431, and M562 records whose TOGO/JCM pages contain the stock recipes. The NaHCO3 stock is named explicitly enough to become an 84 g/L sodium bicarbonate solution prepared under CO2. | TOGO normalized M451 plus the cross-reference resolver that should connect M433/M431/M562 stock subcomponents. |
| major | TOGO M451 pH and preparation comments were dropped. | The generated record has no `ph_value` or `preparation_steps`; the live TOGO M451 payload has `ph: "7.2"` and comments for sodium acetate/estradiol handling, autoclaving and cooling under N2-CO2, and estradiol incubation. | `data/normalized_yaml/bacterial/TOGO_M451_Anoxic_Medium_For_Strain_AcBE2-1.yaml` or the TOGO comments importer. |
| major | The same JCM M451 recipe has a parallel MediaDive/JCM record that did not merge with this TOGO record. | Ignored-inclusive exact search found `CultureMech:002801` in `data/normalized_yaml/bacterial/anoxic_medium_for_strain_acbe2_1.yaml`; it has the same JCM URL, the same `J451` source identity, pH 7.2, and a generated sibling `data/merge_yaml/merged/anoxic_medium_for_strain_acbe2_1__8d1686bc.yaml`. | Merge fingerprint rules after correcting the TOGO stock boundary, and the MediaDive normalized J451 record if its flattened stock rows remain incompatible with TOGO. |
| minor | The medium is classified as `COMPLEX` / `UNDEFINED` despite the inspected M451 payload listing defined salts, gases, and defined stock solutions. | The TOGO payload and referenced M433/M431/M562 stocks are chemically defined; no yeast, peptone, extract, or other undefined ingredient is present in M451. | `data/normalized_yaml/bacterial/TOGO_M451_Anoxic_Medium_For_Strain_AcBE2-1.yaml`. |

## Recommended Edits

1. In the maintained TOGO M451 record or importer output, preserve the source units on the four post-base additions as ml additions rather than `G_PER_L`.
2. Resolve the M433, M431, and M562 cross-references to structured stock compositions, and convert the inline NaHCO3 stock into a sodium bicarbonate solution with 84 g/L strength and CO2 autoclaving context.
3. Import `ph_value: 7.2` and translate both TOGO M451 comments into ordered `preparation_steps` without inventing extra details.
4. Reconcile the TOGO M451 and MediaDive/JCM J451 records so the final merge has one source identity for JCM 451, one pH, one stock-boundary model, and one generated page.
5. Reclassify `medium_type` / `composition_type` after the stock solutions are represented; the corrected M451 recipe appears defined.
6. Regenerate `data/merge_yaml/merged/anoxic_medium_for_strain_acbe2_1.yaml` from normalized data instead of hand-editing the generated merge.

## Follow-up Checks

- Rerun focused open-schema, strict, reference, and term validation on `data/normalized_yaml/bacterial/TOGO_M451_Anoxic_Medium_For_Strain_AcBE2-1.yaml`.
- Rerun `just verify-merges` and `just audit-merge-freshness` after any M451/J451 normalized repairs.
- Render the regenerated media page and confirm it shows pH 7.2, source preparation text, ml stock additions, and non-empty stock compositions.
- Re-run an ignored-inclusive exact search for `GRMD=451` and `Anoxic Medium For Strain AcBE2-1` to confirm no duplicate normalized source record remains outside the expected merged group.

## Additional Notes

Optional `target_organisms` were left empty in the generated record. The medium title names strain AcBE2-1, but TOGO M451 itself does not attach a taxon, and resolving that strain to a CultureMech target organism should be done with a primary growth citation rather than inferred from the medium title alone.
