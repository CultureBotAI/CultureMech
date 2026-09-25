# YAML Record Review: Artficial Freshwater Medium II

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_II.yaml`
- Started UTC: 2026-09-21T14:45:41Z
- Finished UTC: 2026-09-21T14:47:27Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:007730` |
| Label | `artficial_freshwater_medium_ii` |
| Source identity | TOGO `M1203`, original `JCM_M1125`, JCM Medium 1125 |
| Generated status | Generated merge under `data/merge_yaml/merged/`; do not edit in place |
| Maintained owners | `data/normalized_yaml/bacterial/TOGO_M1203_Artficial_Freshwater_Medium_II.yaml`; `data/normalized_yaml/bacterial/TOGO_M1204_Artficial_Freshwater_Medium_II.yaml`; the merge recipe that writes `data/merge_yaml/merged/` |
| Merge provenance | `merged_from` lists `TOGO_M1203_Artficial_Freshwater_Medium_II` and `TOGO_M1204_Artficial_Freshwater_Medium_II` |

This review covers exactly `data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_II.yaml`. `find reports/yaml_record_review -name '*ARTFICIAL_FRESHWATER_MEDIUM_II.md' -print` searched the ignored `reports/yaml_record_review/` tree and found no prior report named for this target.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_II.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_II.yaml --out /private/tmp/ARTFICIAL_FRESHWATER_MEDIUM_II.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_II.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARTFICIAL_FRESHWATER_MEDIUM_II.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The only emitted message was the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | `just validate-history` | Not checked: the repository exposes this validator for standalone `history/*.yaml` records, not for embedded `MediaRecipe.curation_history` blocks in one merged recipe. |

The project `just` wrappers were not rerun in this pass because this checkout currently resolves through Python 3.13 and attempts to build `llvmlite==0.46.0`, which fails before any target-specific YAML validation. The no-project commands above exercise the narrow validators against this one generated record.

## Identity and Grounding

The canonical record identifies TOGO `M1203`, which TOGO reports as `original_media_id` `JCM_M1125` with `src_url` `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1125`. JCM Medium 1125 is titled `ARTFICIAL FRESHWATER MEDIUM II`, matching the TOGO spelling and the generated `original_name`.

The generated merge identity is not coherent, because it also absorbed TOGO `M1204`. TOGO `M1204` reports `original_media_id` `JCM_M1125-2`, and its source component list uses `sodium lactate solution` where TOGO `M1203` uses `1 M Glycerin solution*`. JCM 1125 makes the same variant explicit in its cultivation comment: the JCM 31104 variant uses 1 M sodium lactate instead of 1 M glycerin, with a final 10 mM lactate concentration. A generated record whose `media_term` is only `TOGO:M1203` must therefore not claim `TOGO_M1204` as an equivalent duplicate in `merged_from`.

The simple base salts are grounded plausibly: KH2PO4 to `CHEBI:63036`, NH4Cl to `CHEBI:31206`, KCl to `CHEBI:32588`, Na2SO4 to `CHEBI:32149`, water to `CHEBI:15377`, carbon dioxide to `CHEBI:16526`, and nitrogen to `CHEBI:17997` all match the corresponding source ingredient identities.

## Evidence

JCM Medium 1125 supports the direct base recipe rows for KH2PO4 0.2 g, NH4Cl 0.25 g, KCl 0.3 g, Na2SO4 1.4 g, FeCl2 solution 1.0 ml, Trace element solution 1.0 ml, Selenite-tungstate solution 1.0 ml, Resazurin 1.0 mg, and Distilled water 960.0 ml. The generated record retains the direct salts, but imports the 960 ml water amount as `960 G_PER_L` and the 1.0 mg resazurin amount as `1 G_PER_L`.

JCM Medium 1125 supports the stock additions after cooling: 8% NaHCO3 solution at 30.0 ml, 1 M MgCl2 x 6H2O solution at 2.5 ml, 1 M CaCl2 x 2H2O solution at 1.0 ml, the vitamin, thiamine, and vitamin B12 stocks from JCM 403 at 1.0 ml each, 10% yeast extract solution at 1.0 ml, and 1 M glycerin solution at 10.0 ml for the M1203 variant. The generated `solutions` block lists these entries with the same numeric amounts but changes every `ml` addition to `G_PER_L` and leaves every stock as `name: Unknown solution` with `composition: []`.

JCM Media 187, 403, and 431 provide the stock compositions that JCM 1125 references:

| Referenced source | Stock composition that should be represented |
|---|---|
| JCM 187 | FeCl2 stock: 25% HCl, FeCl2 x 4H2O, distilled water; Trace element stock: ZnCl2, MnCl2 x 4H2O, H3BO3, CoCl2 x 6H2O, CuCl2 x 2H2O, NiCl2 x 6H2O, Na2MoO4 x 2H2O, distilled water |
| JCM 403 | Vitamin stock, thiamine stock, and vitamin B12 stock subrecipes |
| JCM 431 | Selenite-tungstate stock: NaOH, Na2SeO3 x 5H2O, Na2WO4 x 2H2O, distilled water |

Those referenced stock recipes are missing from the generated record even though the normalized TOGO M1203 and M1204 owners now contain curated compositions and formal `references` for the JCM and TOGO source records.

## Completeness

The generated merge is materially incomplete for a procedural medium:

- It has no `preparation_steps`, but JCM 1125 tells the curator to autoclave the base under N2-CO2 (4:1), add autoclaved or filter-sterilized stocks after cooling, distribute aseptically and anaerobically under the same gas mixture, seal with butyl rubber stoppers, and reduce immediately before use with a 5% Na2S x 9H2O solution.
- It has no formal `references` list, even though its maintained owners now cite TOGO M1203 or M1204, JCM 1125, MediaDive J1125, TOGO M180, TOGO M401, TOGO M431, JCM 187, JCM 403, and JCM 431.
- It has no `target_organisms`. That is acceptable here because this TOGO/JCM source recipe does not claim that every intended strain has been curated as growth evidence.
- It has no discussions or quality flags naming the stale merge. That should be unnecessary after merge regeneration; the generated artifact should simply stop collapsing M1203 and M1204.

## Findings

| Severity | Finding | Evidence | Maintained owner for a fix |
|---|---|---|---|
| Blocker | The generated M1203 canonical incorrectly merged the M1204 sodium-lactate variant as an equivalent duplicate. | `media_term` is `TOGO:M1203`, while `merged_from` lists both M1203 and M1204. TOGO M1203 is JCM_M1125 and uses 1 M glycerin; TOGO M1204 is JCM_M1125-2 and uses sodium lactate for the JCM 31104 substitution that JCM 1125 describes. | Regenerate `data/merge_yaml/merged/` from the repaired normalized owners and make the merge fingerprint distinguish stock identity and composition so `TOGO_M1204_Artficial_Freshwater_Medium_II.yaml` remains a variant, not a duplicate of M1203. |
| Major | All 12 stock solutions in the generated record are empty `Unknown solution` stubs and have final-addition milliliter amounts mislabeled as `G_PER_L`. | Lines 180-267 list FeCl2, trace elements, selenite-tungstate, NaHCO3, MgCl2, CaCl2, yeast extract, glycerin, vitamin, thiamine, vitamin B12, and Na2S stocks as `composition: []` with `unit: G_PER_L`. JCM 1125, 187, 403, and 431 provide ml additions and stock subrecipes. | Keep the curated nested `solutions` in the two normalized TOGO owner files and regenerate the merge after fixing the stale/overbroad merge. |
| Major | Preparation was dropped from the generated merge. | JCM 1125 includes autoclaving under N2-CO2, post-cooling stock addition, anaerobic dispensing and butyl-rubber stopper sealing, and reduce-before-use instructions. The generated YAML has no `preparation_steps`. | Preserve `preparation_steps` from `data/normalized_yaml/bacterial/TOGO_M1203_Artficial_Freshwater_Medium_II.yaml` and the sodium-lactate wording from the M1204 owner when regenerating generated outputs. |
| Major | Two direct ingredient units are dimensionally wrong. | The generated record imports `Distilled water` as `960 G_PER_L` and `Resazurin` as `1 G_PER_L`; JCM 1125 and the TOGO M1203/M1204 API data list those source rows as 960 ml and 1 mg. | The normalized M1203 and M1204 owners now carry `960.0 ML_PER_L` water and `0.984252 MG_PER_L` resazurin values; regenerated merges should carry those corrected units forward. |
| Minor | Nitrogen gas is duplicated. | Lines 89-104 contain both `Nitrogen gas` and `N2`, and both resolve to `CHEBI:17997` dinitrogen. TOGO repeats the same gas row in separate parsed paragraphs, but this generated record does not need two dinitrogen ingredients. | Keep only one dinitrogen row in the normalized/generated representation or teach the TOGO importer/normalizer to coalesce repeated gas markers from one recipe. |

## Recommended Edits

1. Regenerate the M1203 and M1204 merge outputs from the repaired normalized YAML so the generated canonical records stop reflecting the pre-repair August 2026 merge.
2. Audit `scripts/merge_recipes.py` fingerprinting for solution identity and stock composition. M1203 and M1204 differ only in the 10 ml/L carbon-source stock, so any fingerprint that still merges them is too coarse.
3. Preserve the curated `solutions`, `preparation_steps`, and `references` blocks from `data/normalized_yaml/bacterial/TOGO_M1203_Artficial_Freshwater_Medium_II.yaml` and `data/normalized_yaml/bacterial/TOGO_M1204_Artficial_Freshwater_Medium_II.yaml` into regenerated derived records and pages.
4. Ensure the TOGO importer or normalizer maps one-off recipe additions expressed as `ml` and `mg` to volume or mass units instead of converting all numeric rows to `G_PER_L`.
5. Add a focused regression fixture for the M1203/M1204 pair so the glycerin and sodium-lactate stocks cannot be collapsed into the same merge fingerprint.

## Follow-up Checks

- Run `just verify-merges` after regenerating `data/merge_yaml/merged/` and confirm `TOGO_M1203_Artficial_Freshwater_Medium_II.yaml` and `TOGO_M1204_Artficial_Freshwater_Medium_II.yaml` no longer merge into one `CultureMech:007730` output.
- Run `just audit-merge-freshness` to prove no generated merge is older than the maintained normalized owners.
- Run `just validate data/normalized_yaml/bacterial/TOGO_M1203_Artficial_Freshwater_Medium_II.yaml` and the same command for `TOGO_M1204_Artficial_Freshwater_Medium_II.yaml`.
- Run the same open-schema, strict, reference, and term validators against the regenerated M1203 and M1204 merge records.
- Manually compare the regenerated stock solutions against JCM 1125, JCM 187, JCM 403, and JCM 431, checking especially the 10 ml/L glycerin versus sodium-lactate distinction.

## Additional Notes

- The generated record under review is stale relative to the two maintained owners: both normalized TOGO records have a 2026-09-11 `RESOLVED_TOGO_M1200_M1204_SCORE15` curation event, while this merged record's newest events are the 2026-08-06 duplicate merge events.
- The normalized M1203 and M1204 owner files were inspected in full for this review; `data/normalized_yaml/bacterial/artficial_freshwater_medium_ii.yaml` is a sibling CultureMech `002298` / MediaDive JCM J1125 record and was not treated as an owner of this generated merge.
