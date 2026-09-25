# YAML Record Review: bacillus_tusciae_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml
- Started UTC: 2026-09-21T18:07:45Z
- Finished UTC: 2026-09-21T18:09:56Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml` |
| Generated ID | `CultureMech:008975` |
| Label | `bacillus_tusciae_medium` |
| Source | TOGO Medium M2392 |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml` |
| Merge fingerprint | `fe7a176e073dddcaa459dbdcdeff7af46b5c60e8a69b72c4e0352db3f2c0c81d` |

The target is a generated single-source merge from `TOGO_M2392_Bacillus_Tusciae_Medium.yaml`. Future repairs belong in that normalized TOGO owner, the TOGO importer/unit transform, or merge regeneration; the generated merge itself must not be edited directly.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml` | Passed |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml --out /private/tmp/Bacillus_Tusciae_Medium.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 0 checks, all validations passed |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone `history/` files |

## Identity and Grounding

The generated record has the intended TOGO M2392 / Bacillus Tusciae Medium source identity, but its scientific state is closer to an incompletely flattened Medium 260/261 body than to DSMZ Medium 369. DSMZ Medium 369 defines Bacillus Tusciae Medium by applying a pH 4.0 and 50 C gas-incubation overlay to Medium 261. DSMZ Medium 261 in turn says to use Medium 260 without pyruvate, and DSMZ Medium 260 is the source of the mineral-salt and SL-6 trace-element formulation.

The ingredient groundings are mostly correct at the primary `term` level. Two grounding defects remain: `MgSO4 x 7 H2O` has a heptahydrate primary `term` but a generic `mediaingredientmech_chebi_term`, and `NiCl2 x 6 H2O` is grounded as anhydrous `CHEBI:34887` / nickel dichloride instead of hydrate-specific nickel chloride hexahydrate.

## Evidence

The TOGO M2392 API payload points back to DSMZ Medium 369 and carries the Medium 260/261 basal recipe with 1000 ml distilled water, 4.5 g `Na2HPO4 x 2 H2O`, 1.5 g `KH2PO4`, 1 g `NH4Cl`, 0.01 g `MnSO4 x H2O`, 0.2 g `MgSO4 x 7 H2O`, 0.01 g `CaCl2 x 2 H2O`, 5 mg ferric ammonium citrate, and 3 ml `Trace element solution SL-6`.

DSMZ Medium 27 supports the SL-6 stock recipe that Medium 260 uses: the seven trace salts plus 1000 ml distilled water are a separate stock, and Medium 260 adds 3 ml/L of that stock. The TOGO owner already has a `solutions` row for `Trace element solution SL-6`, but it records `3 G_PER_L` instead of 3 ml/L and leaves the stock salts duplicated as top-level final-medium ingredients.

DSMZ Medium 369 supplies the Bacillus tusciae-specific conditions: pH 4.0 and incubation at 50 C without agitation under 5% O2, 10% CO2, and 45% H2. The generated TOGO record has no `ph_value`, no adjustment to pH 4.0, and no incubation-atmosphere step.

## Completeness

Consequential gaps:

- Missing Bacillus tusciae pH 4.0.
- Missing Bacillus tusciae incubation temperature and gas atmosphere.
- Missing the correct 3 ml/L `Trace element solution SL-6` stock amount.
- Duplicating the SL-6 stock salts as top-level medium ingredients at stock strength.
- Importing DSMZ 5 mg ferric ammonium citrate as 5 g/L.
- Importing water as g/L, with generated water additionally stale at 2000 g/L after the normalized source was repaired to 1000.

Optional explicit organism and growth-evidence fields are not required for this source recipe. This review verified TOGO M2392 and the DSMZ Medium 369, 261, 260, and 27 source chain.

An ignored-file-inclusive prior-report search covered `reports/yaml_record_review` for `Bacillus_Tusciae_Medium`, `bacillus_tusciae_medium`, `TOGO_M2392_Bacillus_Tusciae_Medium`, and `CultureMech:008975`; it found no prior report for this generated record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The Bacillus tusciae pH and incubation overlay is missing. | DSMZ Medium 369 says to adjust Medium 261 to pH 4.0 and incubate at 50 C without agitation under 5% O2, 10% CO2, 45% H2. TOGO M2392 has no pH field or preparation steps. | `data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml` and the TOGO DSMZ-reference importer |
| Major | SL-6 is represented both as a malformed solution and as top-level stock salts. | TOGO and DSMZ add 3 ml of `Trace element solution SL-6`; the normalized record has `solutions[0].concentration.unit: G_PER_L` and also keeps the SL-6 stock components as final-medium ingredients at stock g/L concentrations. | `data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml`; TOGO stock-solution migration |
| Major | Ferric ammonium citrate is 1000-fold too high. | TOGO imports `Ferric ammonium citrate` as 5 mg, but the normalized and generated row is `5 G_PER_L` instead of 0.005 g/L. | `data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml`; TOGO mg-to-g conversion |
| Major | Main water has the wrong unit and stale generated value. | TOGO lists 1000 ml distilled water. The normalized row is `1000 G_PER_L`; the generated row has `[Merged 2 duplicates: 1000.0, 1000.0]` and `2000.0 G_PER_L`, which predates the September 2026 duplicate-merge repair. | `data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml`; merge regeneration |
| Major | Two hydrated salts have inconsistent or overly broad MIM links. | `MgSO4 x 7 H2O` has primary `CHEBI:31795` but `mediaingredientmech_chebi_term: CHEBI:32599`; `NiCl2 x 6 H2O` is mapped to anhydrous nickel dichloride. | `data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml`; the MIM label-index rule for `NiCl2 x 6 H2O` |

## Recommended Edits

1. Add `ph_value: 4.0` and preparation steps for the DSMZ Medium 369 pH adjustment and 50 C, 5% O2 / 10% CO2 / 45% H2, no-agitation incubation.
2. Convert main water to a volume unit, keeping 1000 ml/L, and preserve only one main water row.
3. Convert ferric ammonium citrate from 5 mg/L to 0.005 g/L.
4. Replace the top-level SL-6 trace-salt rows with a correctly typed `solutions` entry for `Trace element solution SL-6` at 3 ml/L; keep stock composition only nested under that solution or in a corrected reusable SL-6 solution record.
5. Fix `MgSO4 x 7 H2O` so both term slots use the heptahydrate-specific `CHEBI:31795`.
6. Re-ground `NiCl2 x 6 H2O` to a hydrate-specific term or leave it explicitly unresolved; do not publish it as anhydrous nickel dichloride.
7. Regenerate `data/merge_yaml/merged/` and verify the repaired TOGO M2392 source deduplicates with the existing DSMZ/KOMODO Medium 369 records, not with Medium 261 alone.

## Follow-up Checks

- Run `just validate data/normalized_yaml/bacterial/TOGO_M2392_Bacillus_Tusciae_Medium.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Re-run the no-project open-schema, strict, reference, and term validators against `data/merge_yaml/merged/Bacillus_Tusciae_Medium.yaml`.
- Recompare regenerated output with TOGO M2392, DSMZ Medium 369, DSMZ Medium 261, DSMZ Medium 260, and DSMZ Medium 27.
- Check that regenerated `Bacillus_Tusciae_Medium.yaml` no longer has `2000.0` water, `3 G_PER_L` for SL-6, `5 G_PER_L` ferric ammonium citrate, or top-level SL-6 stock salt rows.

## Additional Notes

The existing generated `MEDIUM_FOR_CHEMOLITHOTROPHIC_GROWTH_OF_BACILLUS_SCHLEGELII.yaml` has already collapsed DSMZ Medium 369 and Bacillus tusciae into Medium 261 because those records share the same no-pyruvate ingredient signature when pH and atmosphere are ignored. The TOGO M2392 repair should preserve the pH 4.0 and 50 C gas overlay before deduplication so Medium 369 remains distinguishable from its Medium 261 parent.
