# YAML Record Review: modified_sulfate_reducing_bacteria_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_sulfate_reducing_bacteria_medium__0c45301e.yaml
- Started UTC: 2026-09-24T13:20:03Z
- Finished UTC: 2026-09-24T13:21:01Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| CultureMech ID | CultureMech:002714 |
| Name | modified_sulfate_reducing_bacteria_medium |
| Original name | MODIFIED SULFATE REDUCING BACTERIA MEDIUM |
| Category | bacterial |
| Source identity | mediadive.medium:J354, JCM Medium 354 |
| Generated status | Generated canonical merge under `data/merge_yaml/merged/`; future fixes belong in `data/normalized_yaml/bacterial/modified_sulfate_reducing_bacteria_medium.yaml` or the JCM/MediaDive stock-solution importer. |

An ignored-file-inclusive exact search for `CultureMech:002714`, `mediadive.medium:J354`, `modified_sulfate_reducing_bacteria_medium`, `GRMD=354`, `JCM Medium J354`, and `0c45301e` under `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found this generated merge, its maintained JCM owner, a TOGO M348 branch from the same JCM source page, index/report rows, and aggregate QA rows. The reviewed generated record is a singleton merge from `modified_sulfate_reducing_bacteria_medium`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, Python 3.11 `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_sulfate_reducing_bacteria_medium__0c45301e.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator, Python 3.11 `scripts/validate_strict.py data/merge_yaml/merged/modified_sulfate_reducing_bacteria_medium__0c45301e.yaml --out /private/tmp/modified_sulfate_reducing_bacteria_medium__0c45301e.strict.tsv --workers 1 --quiet` | Passed. TSV contained only the header row, so there were 0 strict errors. |
| Reference validator, Python 3.11 `linkml-reference-validator validate data data/merge_yaml/merged/modified_sulfate_reducing_bacteria_medium__0c45301e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the checker reported 0 reference checks. |
| Term validator, Python 3.11 `linkml-term-validator validate-data data/merge_yaml/merged/modified_sulfate_reducing_bacteria_medium__0c45301e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone YAML under `history/`, not inline `MediaRecipe.curation_history` entries. |

## Identity and Grounding

The record identity is correct: JCM Medium 354 is `MODIFIED SULFATE REDUCING BACTERIA MEDIUM`, a pH 6.7 liquid medium prepared anaerobically under N2 and H2-CO2. The basal salts, PIPES, tryptone, acetate, selenate, tungstate, vitamin B12, resazurin, and sodium sulfide source rows all appear on the inspected JCM 354 page.

Most ChEBI groundings are exact for the displayed source labels. The sodium selenate row still uses a deprecated legacy `mediaingredientmech_term` even though its primary ChEBI term is correct.

## Evidence

The imported basal rows are recognizable but no longer exact source amounts because the importer appears to have normalized them across the 10 ml trace-vitamin addition. JCM 354 prints values such as 20.0 g NaCl, 3.0 g MgCl2 x 6 H2O, 4.0 g Na2SO4, and 3.46 g PIPES with 1 L water; the YAML stores 19.802, 2.9703, 3.9604, and 3.42574 `G_PER_L`.

The larger scientific error is the `Trace vitamins` stock. JCM 354 adds 10 ml of the Medium 197 trace-vitamin stock. The YAML instead flattens Medium 197's one-liter stock rows into the final ingredient list at stock concentration. For example, Medium 197 lists 2.0 mg/l biotin and 0.1 mg/l vitamin B12, but a 10 ml/l dose should contribute only 0.02 mg/l biotin and 0.001 mg/l vitamin B12 before any explicit B12 row is added.

The generated `Vitamin B12` row is a cross-scope sum: JCM 354 has a direct 0.05 mg/l Vitamin B12 row, and Medium 197 has Vitamin B12 inside the trace-vitamin stock. The YAML sums both as if they were final-medium duplicates.

## Completeness

The record is missing the trace-vitamin stock addition boundary. It also represents the 5% Na2S x 9H2O solution as only a final ingredient row; the preparation text describes its neutralization and separate autoclaving, but a future curation pass should make the stock addition explicit.

Empty `target_organisms`, `growth_evidence`, and `discussion` slots are acceptable for this JCM recipe import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Medium 197 trace vitamins are flattened into final-medium rows. | JCM 354 calls for 10 ml/l `Trace vitamins (see Medium No. 197)`. The YAML stores every vitamin as a top-level final-medium ingredient at the Medium 197 stock concentration. | `data/normalized_yaml/bacterial/modified_sulfate_reducing_bacteria_medium.yaml`; JCM stock-solution extraction. |
| major | `Vitamin B12` was summed across the final medium and trace-vitamin stock. | The final medium has its own 0.05 mg/l Vitamin B12 row; Medium 197 also contains Vitamin B12 at 0.1 mg/l stock. The YAML has one merged `Vitamin B12` row with `Merged 2 duplicates: 4.95049e-05, 0.0001`. | `data/normalized_yaml/bacterial/modified_sulfate_reducing_bacteria_medium.yaml`; duplicate-row cleanup should respect solution scope. |
| minor | Basal row concentrations no longer exactly preserve the JCM table. | Source rows such as 20.0 g NaCl, 3.0 g MgCl2 x 6 H2O, 4.0 g Na2SO4, and 3.46 g PIPES are normalized to 19.802, 2.9703, 3.9604, and 3.42574 `G_PER_L`. | `data/normalized_yaml/bacterial/modified_sulfate_reducing_bacteria_medium.yaml`; JCM final-volume normalization. |
| minor | `Na2SeO4` still uses a deprecated legacy MediaIngredientMech identifier field. | The row has correct primary grounding to `CHEBI:77775` but keeps `mediaingredientmech_term: MediaIngredientMech:000198` after the 2026-06-05 migration replaced 22 other legacy links. | `data/normalized_yaml/bacterial/modified_sulfate_reducing_bacteria_medium.yaml`; MediaIngredientMech-to-ChEBI migration. |
| minor | The MediaDive/JCM branch has a same-page TOGO duplicate to reconcile. | Exact ignored-file-inclusive search found `data/normalized_yaml/bacterial/TOGO_M348_Modified_Sulfate_Reducing_Bacteria_Medium.yaml`, which cites the same JCM `GRMD=354` page but is generated separately as `data/merge_yaml/merged/MODIFIED_SULFATE_REDUCING_BACTERIA_MEDIUM.yaml`. | Merge/source-duplicate curation for JCM GRMD 354. |

No blocker findings.

## Recommended Edits

1. Represent Medium 197 trace vitamins as a stock addition dosed at 10 ml/l instead of flattening its contents into the final medium.
2. Split `Vitamin B12` into the source-supported direct B12 row plus the B12 contained inside the Medium 197 stock; do not sum the two across scopes.
3. Make the neutralized 5% Na2S x 9H2O solution an explicit stock/addition while preserving the source final amount.
4. Preserve or explicitly justify any final-volume normalization that converts the printed JCM amounts into lower `G_PER_L` values.
5. Migrate the `Na2SeO4` MediaIngredientMech link to `mediaingredientmech_chebi_term` keyed to `CHEBI:77775`.
6. Compare the corrected MediaDive/JCM 354 branch with TOGO M348 and reconcile them as source duplicates if their corrected formulations match.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the corrected normalized branch and regenerated `data/merge_yaml/merged/modified_sulfate_reducing_bacteria_medium__0c45301e.yaml`.
- Re-run duplicate-ingredient QA and confirm `CultureMech:002714` no longer has a `DIFFERING_PARTS` row for `Vitamin B12`.
- Re-inspect the regenerated record against JCM 354 and Medium 197 to confirm all vitamins remain inside a trace-vitamin stock dosed at 10 ml/l.
- Re-run merge freshness and confirm the JCM/MediaDive and TOGO M348 records from `GRMD=354` are not left as independent generated outputs when their source support is equivalent.

## Additional Notes

I reused the inspected Medium 197 page from the preceding `modified_sporomusa_medium` review to verify the trace-vitamin stock composition; JCM 354 links to the same Medium 197 source.
