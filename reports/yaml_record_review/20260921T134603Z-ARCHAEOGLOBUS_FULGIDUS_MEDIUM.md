# YAML Record Review: Archaeoglobus fulgidus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ARCHAEOGLOBUS_FULGIDUS_MEDIUM.yaml
- Started UTC: 2026-09-21T13:45:11Z
- Finished UTC: 2026-09-21T13:46:03Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| Stable ID | CultureMech:008362 |
| Name | archaeoglobus_fulgidus_medium |
| Original name | Archaeoglobus fulgidus Medium |
| Category | archaea |
| Source | TOGO:M1794, imported from NBRC_M1019 |
| Reviewed artifact | data/merge_yaml/merged/ARCHAEOGLOBUS_FULGIDUS_MEDIUM.yaml |
| Maintained owner | data/normalized_yaml/archaea/TOGO_M1794_Archaeoglobus_fulgidus_Medium.yaml |

This review targeted the generated canonical merge for TOGO M1794; `merged_from` contains only `TOGO_M1794_Archaeoglobus_fulgidus_Medium`.

An ignored-file-inclusive exact search for `CultureMech:008362`, `TOGO:M1794`, `M1794`, and `TOGO_M1794_Archaeoglobus_fulgidus_Medium` covered `data/normalized_yaml`, `data/merge_yaml`, `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, `reports/media_content_review_manifest.tsv`, `data/import_tracking/reports/concentration_plausibility.tsv`, and `data/import_tracking/reports/merged_duplicates.tsv`. It found this generated merge, the normalized owner, generated indexes, registry/catalog rows, and import-tracking diagnostics for the same CultureMech ID.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARCHAEOGLOBUS_FULGIDUS_MEDIUM.yaml`; no issues found. |
| Strict schema | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARCHAEOGLOBUS_FULGIDUS_MEDIUM.yaml --out /private/tmp/ARCHAEOGLOBUS_FULGIDUS_MEDIUM.strict.tsv --workers 1 --quiet`; 1 file scanned, 0 error rows. |
| Reference validator | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARCHAEOGLOBUS_FULGIDUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; 1 file validated, 0 total active checks. |
| Term validator | Passed with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARCHAEOGLOBUS_FULGIDUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`; only the upstream `eutils`/`pkg_resources` deprecation warning was emitted. |
| Embedded curation history | Not checked: this repository exposes `just validate-history` for standalone `history/` files, not a focused `MediaRecipe.curation_history` check for one merged recipe. |

Mechanical validators pass; the defects below are source-scope, unit, and regeneration issues.

## Identity and Grounding

The source identity is correct. Togo `M1794` names `Archaeoglobus fulgidus Medium` and carries `original_media_id: NBRC_M1019`; the live NBRC NO=1019 page also labels the recipe `Archaeoglobus fulgidus Medium`.

The generated merge is stale relative to its maintained owner. `data/normalized_yaml/archaea/TOGO_M1794_Archaeoglobus_fulgidus_Medium.yaml` has the 2026-09-02 `REPAIRED_SUMMED_DUPLICATE_MERGE` curation event and encodes `Distilled water` as `1.0 G_PER_L`; the generated merge still has `4.0 G_PER_L` and lacks that repair event.

Several exact chemical forms are wrong:

| Ingredient | Current grounding | Issue |
| --- | --- | --- |
| Fe(NH4)2(SO4)2.7H2O | CHEBI:131378, ferrous ammonium sulfate heptahydrate | NBRC and Togo use a 2 mg row; the mass unit is wrong in YAML even though the hydrate grounding is specific. |
| CoCl2.6H2O | CHEBI:35696, cobalt dichloride | Source is cobalt chloride hexahydrate; the record points to the anhydrous salt. |
| NiCl2.6H2O | CHEBI:34887, nickel dichloride | Source is nickel chloride hexahydrate; the record points to the anhydrous salt. |
| Ca-pantothenate | CHEBI:29032, (R)-pantothenate | Source is the calcium salt; the record points to the pantothenate anion. |

## Evidence

NBRC and Togo agree on the main medium:

| Main-medium component | Source amount | Generated amount |
| --- | ---: | ---: |
| KP buffer | 5 ml | `5 G_PER_L` in `solutions` |
| MgCl2.6H2O | 0.75 g | 0.75 G_PER_L |
| CaCl2.2H2O | 0.15 g | merged into 0.25 G_PER_L |
| NH4Cl | 0.54 g | 0.54 G_PER_L |
| NaCl | 30 g | merged into 31.0 G_PER_L |
| Na2SO4 | 2.4 g | 2.4 G_PER_L |
| Sodium lactate | 2.2 g | 2.2 G_PER_L |
| Bacto Yeast Extract (Difco) | 0.5 g | 0.5 G_PER_L |
| Fe(NH4)2(SO4)2.7H2O | 2 mg | 2 G_PER_L |
| Trace element solution | 2 ml | `2 G_PER_L` in `solutions` |
| Vitamin solution | 2 ml | `2 G_PER_L` in `solutions` |
| Resazurin | 1 mg | 1 G_PER_L |
| Na2CO3 | 1 g | 1 G_PER_L |
| Na2S.9H2O | 0.36 g | 0.36 G_PER_L |
| Distilled water | 1 L | 4.0 G_PER_L in the generated merge |

The source-local stock formulations are not represented as nested, M1794-local solutions:

| Source-local stock | Source contents | Generated representation |
| --- | --- | --- |
| KP buffer | KH2PO4 119 g, K2HPO4 21 g, Distilled water 1 L; autoclaved under N2 | Empty `KP buffer*` solution at `5 G_PER_L`; KH2PO4 and K2HPO4 are flattened into top-level final ingredients. |
| Trace element solution | NTA 12.8 g, FeCl3.6H2O 1.35 g, MnCl2.4H2O 0.1 g, CoCl2.6H2O 0.024 g, CaCl2.2H2O 0.1 g, ZnCl2 0.1 g, CuCl2.2H2O 0.025 g, H3BO3 0.01 g, Na2MoO4.2H2O 0.024 g, NaCl 1 g, NiCl2.6H2O 0.12 g, Na2SeO4 0.004 g, Na2WO4 0.004 g, Distilled water 1 L; NTA dissolved before pH adjustment with NaOH, final pH 7.0 | Linked to unrelated `mediadive.solution:6187`; trace components are flattened into top-level final ingredients and NaCl/CaCl2 are summed with final-medium rows. |
| Vitamin solution | Biotin 2 mg, Folic acid 2 mg, Pyridoxine-HCl 10 mg, Thiamine-HCl 5 mg, Riboflavin 5 mg, Nicotinic acid 5 mg, Ca-pantothenate 5 mg, p-Aminobenzoic acid 1 mg, Vitamin B12 0.01 mg, Distilled water 1 L | Linked to unrelated `mediadive.solution:6241`; vitamin components are flattened into top-level final ingredients and recorded in grams per liter instead of milligrams per liter stock amounts. |

The generated record drops source procedure that changes how the medium is made: NBRC leaves the starting pH unadjusted, excludes KP buffer, vitamin solution, Na2CO3, and Na2S.9H2O from the initial mix, dispenses under N2/CO2 80/20, separately autoclaves KP buffer and 5% Na2S.9H2O under N2, filter-sterilizes vitamin and 10% Na2CO3 stocks, and adds those pieces aseptically and anaerobically before inoculation.

## Completeness

Consequential gaps:

- The generated merge lags the normalized water repair.
- The three stock additions have wrong units and wrong or empty identities.
- KP buffer, trace, and vitamin stock rows are flattened into the final medium, erasing 5 ml and 2 ml dilution scope.
- The milligram Fe(NH4)2(SO4)2.7H2O and Resazurin main rows are recorded as grams per liter.
- NBRC preparation, gas, filtration, autoclaving, and post-autoclave addition details are absent.

Empty organism and growth-evidence fields are acceptable for this source-only NBRC formulation.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| major | The generated merge is stale and still over-sums water to `4.0 G_PER_L`. | The normalized owner has the 2026-09-02 duplicate-water repair and `Distilled water` at `1.0 G_PER_L`; the generated merge still has the older `4.0 G_PER_L` value. | Regenerate `data/merge_yaml/merged/ARCHAEOGLOBUS_FULGIDUS_MEDIUM.yaml` from the maintained owner after curation. |
| major | Stock solution additions are typed as mass concentrations and do not identify the NBRC-local stocks. | NBRC lists KP buffer 5 ml, trace element solution 2 ml, and vitamin solution 2 ml. The YAML records `5 G_PER_L`, `2 G_PER_L`, and `2 G_PER_L`, leaves KP buffer empty, and links trace/vitamin to unrelated MediaDive solutions 6187 and 6241. | Fix `data/normalized_yaml/archaea/TOGO_M1794_Archaeoglobus_fulgidus_Medium.yaml` or the TOGO/NBRC import path that creates those solution rows. |
| major | Stock components are flattened into final ingredients and duplicate salts are summed across scopes. | KH2PO4, K2HPO4, trace components, NaOH, and vitamins are source-local stock rows. The generated final ingredient list includes them top-level and sums final 30 g NaCl with trace 1 g NaCl and final 0.15 g CaCl2.2H2O with trace 0.1 g CaCl2.2H2O. | Restore stock boundaries and keep final rows separate from stock rows in the normalized owner. |
| major | Milligram rows are recorded as grams per liter. | NBRC lists Resazurin as 1 mg, Fe(NH4)2(SO4)2.7H2O as 2 mg, and all vitamin-stock quantities in mg; the YAML stores those numeric values under `G_PER_L`. | Correct source unit mapping before regenerating the merge. |
| major | Preparation semantics are dropped. | The source specifies unadjusted starting pH, anaerobic N2/CO2 dispensing, separate N2 autoclaving for KP buffer and sodium sulfide, filtration for vitamin and Na2CO3, and aseptic anaerobic post-autoclave additions. The YAML has no preparation steps. | Add the NBRC procedure to the normalized owner with final-assembly and stock-specific preparation notes. |
| major | Three exact chemical-form groundings are wrong. | CoCl2.6H2O, NiCl2.6H2O, and Ca-pantothenate are grounded to anhydrous cobalt dichloride, anhydrous nickel dichloride, and pantothenate. | Re-ground the hydrate salts and calcium pantothenate to exact terms, or leave them unresolved if exact terms are unavailable. |

No blocker findings: the record denotes the correct TOGO M1794 / NBRC_M1019 recipe.

## Recommended Edits

1. Regenerate the generated merge after fixing the normalized owner so the 2026-09-02 water repair propagates.
2. Replace the empty and unrelated solution rows with NBRC-local KP buffer, trace element solution, and vitamin solution stocks at 5 ml/L, 2 ml/L, and 2 ml/L.
3. Move KP buffer, trace, and vitamin stock components out of top-level final ingredients and stop summing stock NaCl/CaCl2 with final-medium NaCl/CaCl2.
4. Correct Fe(NH4)2(SO4)2.7H2O, Resazurin, and vitamin stock units from grams to milligrams in their proper scopes.
5. Preserve unadjusted pH, N2/CO2 dispensing, N2 autoclaving, filter sterilization, and anaerobic post-autoclave additions as preparation notes.
6. Re-ground CoCl2.6H2O, NiCl2.6H2O, and Ca-pantothenate exactly.

## Follow-up Checks

- Run focused schema, strict, reference, and term validators on the normalized owner after curation.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating the generated M1794 record.
- Recompare the regenerated record against the live NBRC NO=1019 page or Togo M1794 API payload, checking final rows, stock scopes, ml additions, mg units, gas handling, and preparation comments.
- Rebuild or recheck `data/import_tracking/reports/concentration_plausibility.tsv` and `data/import_tracking/reports/merged_duplicates.tsv`; the M1794 unit slips and final-vs-stock NaCl/CaCl2 sums should disappear.

## Additional Notes

- A broad Archaeoglobus search finds many distinct sibling recipes; this review did not treat those as duplicates of NBRC_M1019 without exact source support.
