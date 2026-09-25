# YAML Record Review: artificial_pilot_plant_water_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ARTIFICIAL_PILOT_PLANT_WATER_MEDIUM.yaml
- Started UTC: 2026-09-21T15:07:55Z
- Finished UTC: 2026-09-21T15:10:35Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/ARTIFICIAL_PILOT_PLANT_WATER_MEDIUM.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/artificial_pilot_plant_water_medium.yaml` |
| Stable ID | `CultureMech:002487` |
| Name | `artificial_pilot_plant_water_medium` |
| Original name | `ARTIFICIAL PILOT PLANT WATER MEDIUM` |
| Category | `bacterial` |
| Merge state | Single-source merge from `artificial_pilot_plant_water_medium` with fingerprint `0eed86a9fb470742a852981b5bf78a40a231c5ba425f1a7f087320bbfd002928` |

The target is the generated merge for MediaDive `J1323`; future fixes belong in `data/normalized_yaml/bacterial/artificial_pilot_plant_water_medium.yaml` and then should be regenerated into `data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARTIFICIAL_PILOT_PLANT_WATER_MEDIUM.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARTIFICIAL_PILOT_PLANT_WATER_MEDIUM.yaml --out /private/tmp/ARTIFICIAL_PILOT_PLANT_WATER_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARTIFICIAL_PILOT_PLANT_WATER_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARTIFICIAL_PILOT_PLANT_WATER_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, and no focused validator for embedded `MediaRecipe.curation_history` arrays is exposed. |

The documented `just validate-*` wrappers remain blocked for this environment by project dependency resolution under Python 3.13, so this review used the equivalent no-project Python 3.11 validators already cached under `/private/tmp/uv-cache-culturemech-review`.

## Identity and Grounding

- **Medium identity is correct.** MediaDive `J1323` is `ARTIFICIAL PILOT PLANT WATER MEDIUM`, matching the `mediadive.medium:J1323` grounding and `CultureMech:002487` in the normalized owner and generated merge.
- **The formulation is a defined liquid filter-sterilized medium.** MediaDive marks the medium as non-complex, contains only salts plus water, and lists filter equipment; the local `DEFINED`, `LIQUID`, and `FILTER_STERILIZE` values agree.
- **The ten nonwater ingredient rows match MediaDive.** The local record preserves the MediaDive gram-per-liter values for `Na2SO4`, `K2SO4`, `MgSO4 x 7 H2O`, `CaSO4 x 2 H2O`, `NaHCO3`, `NH4Cl`, `Al2(SO4)3 x 18 H2O`, `FeSO4 x 7 H2O`, `MnCl4 x 6 H2O`, and `ZnCl2`.
- **The solvent row is missing.** MediaDive `J1323` has an eleventh recipe row for 1000 ml `Distilled water`; the generated and normalized CultureMech records have no water ingredient or preparation text giving the final volume.

## Evidence

- The original JCM URL in the source note currently returns a JCM `Nothing found` page for medium 1323, but the MediaDive page and `/download/medium/J1323/json` export are live and identify J1323 as `ARTIFICIAL PILOT PLANT WATER MEDIUM` from JCM.
- The MediaDive medium JSON export lists one `Main sol. J1323` at 1000 ml and 11 recipe rows. Rows 1-10 correspond to the 10 CultureMech ingredients, and row 11 is `Distilled water`, 1000 ml.
- The source also gives the preparation step already in CultureMech: mix components thoroughly, adjust to pH 3.0 with sulfuric acid, and filter-sterilize.
- `MnCl4 x 6 H2O` is source-supported despite lacking a local CHEBI term. MediaDive itself leaves that row's mM value blank, so preserving the unresolved label is better than forcing a plausible manganese chloride grounding without additional evidence.

## Completeness

- The explicit `Distilled water` row from MediaDive is missing from CultureMech.
- No `target_organisms`, `growth_metrics`, or incubation conditions are present. That is acceptable because the inspected MediaDive page has no associated strains and only supplies a recipe.
- The missing `ph_value` slot is non-blocking because pH 3.0 is preserved in the preparation step. Adding it would improve structured search, but the pH claim is not lost.
- The dead JCM source link is a provenance weakness, but the MediaDive grounding and live MediaDive page still recover the formulation.
- A gitignore-independent `find` search under `reports/yaml_record_review` found no pre-existing `*ARTIFICIAL_PILOT_PLANT_WATER_MEDIUM.md` report before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record omits the required 1000 ml `Distilled water` row from the source recipe. | The live MediaDive medium JSON export for `J1323` lists `Distilled water`, amount `1000`, unit `ml`, optional `no`; neither the normalized owner nor the generated merge has a water ingredient or an equivalent final-volume statement. | `data/normalized_yaml/bacterial/artificial_pilot_plant_water_medium.yaml`. |

No blockers found: the YAML validates, the MediaDive `J1323` identity is correct, and every present ingredient amount is source-supported.

## Recommended Edits

1. Add the MediaDive `Distilled water` 1000 ml row to `data/normalized_yaml/bacterial/artificial_pilot_plant_water_medium.yaml` or otherwise represent the 1000 ml final volume in a source-scoped preparation field.
2. Preserve `MnCl4 x 6 H2O` as an unresolved source label unless a curator verifies its intended manganese chloride hydrate identity from MediaDive, JCM, or another primary source.
3. Regenerate `data/merge_yaml/merged/ARTIFICIAL_PILOT_PLANT_WATER_MEDIUM.yaml`.

## Follow-up Checks

- Re-run `just validate-schema data/normalized_yaml/bacterial/artificial_pilot_plant_water_medium.yaml` and `just validate-strict data/normalized_yaml/bacterial/artificial_pilot_plant_water_medium.yaml` after the normalized edit.
- Regenerate the merge layer and confirm that `ARTIFICIAL_PILOT_PLANT_WATER_MEDIUM.yaml` includes the source water/final-volume representation.
- Manually compare the regenerated merge against the MediaDive `J1323` medium JSON export and confirm there are 11 recipe rows plus the filter-sterilization step.

## Additional Notes

- `find data/normalized_yaml -iname '*artificial*pilot*plant*water*medium*.yaml' -print` located the single normalized owner at `data/normalized_yaml/bacterial/artificial_pilot_plant_water_medium.yaml`.
- Exact gitignore-independent searches for `CultureMech:002487`, `mediadive.medium:J1323`, and `MnCl4 x 6 H2O` in the normalized owner and generated record found the same MediaDive identity and unresolved manganese ingredient in both files.
