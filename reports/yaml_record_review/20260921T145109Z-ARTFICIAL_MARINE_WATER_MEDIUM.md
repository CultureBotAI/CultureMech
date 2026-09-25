# YAML Record Review: Artficial Marine Water Medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ARTFICIAL_MARINE_WATER_MEDIUM.yaml`
- Started UTC: 2026-09-21T14:51:09Z
- Finished UTC: 2026-09-21T14:53:12Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:007728` |
| Label | `artficial_marine_water_medium` |
| Source identity | TOGO `M1201`, JCM Medium 1123 |
| Generated status | Generated merge under `data/merge_yaml/merged/`; do not edit in place |
| Maintained owners | `data/normalized_yaml/bacterial/artficial_marine_water_medium.yaml`; `data/normalized_yaml/bacterial/TOGO_M1200_Artficial_Brackish_Water_Medium.yaml`; `data/normalized_yaml/bacterial/TOGO_M1202_Artficial_Freshwater_Medium_I.yaml`; the merge recipe that writes `data/merge_yaml/merged/` |
| Merge provenance | `merged_from` lists M1200 brackish water, M1202 freshwater I, and MediaDive `artficial_marine_water_medium`; the generated record itself carries the M1201 marine identity |

This review covers exactly `data/merge_yaml/merged/ARTFICIAL_MARINE_WATER_MEDIUM.yaml`. `find reports/yaml_record_review -name '*ARTFICIAL_MARINE_WATER_MEDIUM.md' -print` searched the ignored `reports/yaml_record_review/` tree and found no prior report named for this target.

The maintained M1201 owner is `data/normalized_yaml/bacterial/artficial_marine_water_medium.yaml`, not a `TOGO_M1201...` filename. `rg --no-ignore --hidden -n 'TOGO_M1201_Artficial_Marine_Water_Medium|TOGO:M1201|M1201' data/normalized_yaml data/merge_yaml` searched generated and normalized data, including ignored paths, before that owner was resolved.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARTFICIAL_MARINE_WATER_MEDIUM.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARTFICIAL_MARINE_WATER_MEDIUM.yaml --out /private/tmp/ARTFICIAL_MARINE_WATER_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARTFICIAL_MARINE_WATER_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARTFICIAL_MARINE_WATER_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The only emitted message was the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | `just validate-history` | Not checked: the repository exposes this validator for standalone `history/*.yaml` records, not for embedded `MediaRecipe.curation_history` blocks in one merged recipe. |

The project `just` wrappers were not rerun in this pass because this checkout currently resolves through Python 3.13 and attempts to build `llvmlite==0.46.0`, which fails before any target-specific YAML validation. The no-project commands above exercise the narrow validators against this one generated record.

## Identity and Grounding

The top-level identity is TOGO `M1201`, whose API payload reports `original_media_id: JCM_M1123` and `name: Artficial Marine Water Medium`. JCM Medium 1123 is titled `ARTFICIAL MARINE WATER MEDIUM`, so the source identity itself is valid.

The generated merge is not valid. It merges the M1201 marine-water identity with TOGO M1200 / JCM 1122 `ARTFICIAL BRACKISH WATER MEDIUM`, TOGO M1202 / JCM 1124 `ARTFICIAL FRESHWATER MEDIUM I`, and the MediaDive J1123 record. JCM 1122, 1123, and 1124 have distinct salt concentrations and distinct carbon-source stocks, so they are related variants, not equivalent duplicates.

The repaired M1201 normalized owner now has the expected exact source amounts for JCM 1123, including NaCl 26.0 g, KCl 0.72 g, Na2SO4 4.0 g, 40.0 ml 1 M MgCl2 x 6H2O, 10.0 ml 1 M CaCl2 x 2H2O, and 10.0 ml 1 M glucose. The generated M1201 canonical still combines brackish base values such as 940 ml water, NaCl 13 g/L, KCl 0.36 g/L, and Na2SO4 1.42 g/L with marine stock amounts such as 40 and 10 for MgCl2 and CaCl2.

## Evidence

JCM Medium 1123 supports a 960 ml distilled-water base with KH2PO4, NH4Cl, KCl, NaCl, Na2SO4, FeCl2 solution, Trace element solution, Selenite-tungstate solution, and 1.0 mg resazurin. Its post-cooling stocks are 30.0 ml 8% NaHCO3, 40.0 ml 1 M MgCl2 x 6H2O, 10.0 ml 1 M CaCl2 x 2H2O, 1.0 ml each of the JCM 403 vitamin-family stocks, and 10.0 ml 1 M glucose, followed by 5.0 ml 5% Na2S x 9H2O before use.

The generated record preserves the M1201 `media_term`, but not that formulation. Its direct ingredients list 940 water in `G_PER_L`, NaCl 13 `G_PER_L`, KCl 0.36 `G_PER_L`, and Na2SO4 1.42 `G_PER_L`, values that match JCM 1122 brackish water rather than JCM 1123 marine water. It also imports JCM 1123's 40 ml MgCl2 and 10 ml CaCl2 stock additions as `40 G_PER_L` and `10 G_PER_L` empty solution stubs.

JCM 187, JCM 403, and JCM 431 provide the referenced FeCl2, trace-element, vitamin, thiamine, vitamin B12, and selenite-tungstate stock recipes. None of those nested stock compositions are represented in the generated `solutions` list.

## Completeness

The generated record has no `preparation_steps`, although JCM 1123 specifies base mixing, autoclaving under N2-CO2 (4:1), post-cooling stock additions, anaerobic dispensing under the same gas mixture, butyl-rubber stopper sealing, and reduction before use with 5% Na2S x 9H2O.

The generated record has no formal `references` list. Its maintained M1201 owner now cites TOGO M1201 and JCM Media 1123, 187, 403, and 431.

Optional `target_organisms` are absent; this is acceptable for the inspected source records because this recipe-only source does not itself curate a strain-level growth evidence claim.

## Findings

| Severity | Finding | Evidence | Maintained owner for a fix |
|---|---|---|---|
| Blocker | The generated canonical collapses three distinct JCM media and a separate MediaDive record into one TOGO M1201 recipe. | `merged_from` lists M1200 brackish, M1202 freshwater I, and MediaDive J1123 records under `TOGO:M1201`. JCM 1122, 1123, and 1124 differ in NaCl, KCl, Na2SO4, MgCl2, CaCl2, and glucose versus fructose stock identity. | Regenerate `data/merge_yaml/merged/` from the repaired September 11 normalized owners and make `scripts/merge_recipes.py` distinguish base salts, stock identity, and stock volumes in its fingerprint. |
| Major | The generated M1201 formulation is a synthetic mixture of brackish and marine values. | JCM 1123 lists 960 ml water, 26 g NaCl, 0.72 g KCl, and 4.0 g Na2SO4. The generated M1201 record lists 940 `G_PER_L` water, 13 `G_PER_L` NaCl, 0.36 `G_PER_L` KCl, and 1.42 `G_PER_L` Na2SO4. | Keep the curated marine-water quantities in `data/normalized_yaml/bacterial/artficial_marine_water_medium.yaml` and regenerate the merge. |
| Major | All 11 stock solutions are empty `Unknown solution` stubs and use milliliter amounts as `G_PER_L`. | Lines 193-273 list FeCl2, Trace element, Selenite-tungstate, NaHCO3, CaCl2, MgCl2, Glucose, Vitamin, Thiamine, Vitamin B12, and Na2S as `composition: []` with `unit: G_PER_L`. JCM 1123 and the repaired normalized owner represent these as `ML_PER_L` stocks. | Preserve the nested `solutions` from the normalized M1201 owner into regenerated merged records. |
| Major | Preparation was dropped from the generated merge. | JCM 1123 contains anaerobic autoclaving, filter-sterilized additions, anaerobic distribution, stopper sealing, and reduce-before-use instructions; the generated record has no `preparation_steps`. | Preserve the repaired `preparation_steps` from `data/normalized_yaml/bacterial/artficial_marine_water_medium.yaml` during merge regeneration. |
| Minor | Nitrogen gas is duplicated. | Lines 101-116 list both `Nitrogen gas` and `N2`, both grounded to `CHEBI:17997` dinitrogen. | Coalesce duplicate gas markers from TOGO's parsed paragraphs in the importer or normalizer. |
| Minor | The generated classification is stale. | The generated record still says `medium_type: COMPLEX` and `composition_type: UNDEFINED`, while the repaired M1201 normalized owner is `DEFINED` / `DEFINED`. | Regeneration should carry the normalized classification forward. |

## Recommended Edits

1. Regenerate the merge layer so TOGO M1200, M1201, M1202, and MediaDive J1123 are no longer collapsed into `ARTFICIAL_MARINE_WATER_MEDIUM.yaml`.
2. Add a merge regression test around the JCM 1122, 1123, and 1124 family: shared FeCl2/trace/vitamin stock references are not enough to make brackish, marine, and freshwater media equivalent.
3. Preserve the M1201 owner's repaired `ingredients`, nested `solutions`, `preparation_steps`, `references`, and `composition_type` when generating the new M1201 output.
4. Ensure regenerated TOGO outputs coalesce `Nitrogen gas` and `N2` to one dinitrogen ingredient when both parsed rows denote the same gas condition.

## Follow-up Checks

- Run `just verify-merges` after regeneration and confirm M1200, M1201, M1202, and MediaDive J1123 do not share one merge fingerprint.
- Run `just audit-merge-freshness` to ensure no generated YAML is older than the September 11 normalized curation events.
- Run `just validate data/normalized_yaml/bacterial/artficial_marine_water_medium.yaml`.
- Run the same open-schema, strict, reference, and term validators against the regenerated M1201 merged record.
- Manually compare the regenerated M1201 record against JCM 1123 and verify 26 g NaCl, 40 ml MgCl2, 10 ml CaCl2, and glucose rather than the M1200 or M1202 variant values.

## Additional Notes

- `data/normalized_yaml/specialized/artficial_marine_water_medium.yaml` is the separate MediaDive J1123 owner and is not the owner of this TOGO M1201 generated canonical.
- The current generated file predates the repair event `repair_togo_m1201_artificial_marine_water_score15.py`, which is present in the maintained M1201 owner but absent from this stale merge output.
