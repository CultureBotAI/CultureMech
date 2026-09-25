# YAML Record Review: artificial_deep_lake_vitamin_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/artificial_deep_lake_vitamin_medium__83e173f7.yaml
- Started UTC: 2026-09-21T15:05:03Z
- Finished UTC: 2026-09-21T15:06:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/artificial_deep_lake_vitamin_medium__83e173f7.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/artificial_deep_lake_vitamin_medium.yaml` |
| Stable ID | `CultureMech:002530` |
| Name | `artificial_deep_lake_vitamin_medium` |
| Original name | `ARTIFICIAL DEEP LAKE VITAMIN MEDIUM` |
| Category | `bacterial` |
| Merge state | Single-source merge from `artificial_deep_lake_vitamin_medium` with fingerprint `83e173f719ac11b6d6d595a09638b2d14c8cd28498655edf0e8fdf54a863e543` |

The target is a generated merge product for the MediaDive/JCM `J170` Artificial Deep Lake Vitamin Medium record. The authoritative normalized owner has changed after this generated file was written, so the immediate owner is the stale merge layer rather than a new source correction.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/artificial_deep_lake_vitamin_medium__83e173f7.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/artificial_deep_lake_vitamin_medium__83e173f7.yaml --out /private/tmp/artificial_deep_lake_vitamin_medium__83e173f7.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/artificial_deep_lake_vitamin_medium__83e173f7.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/artificial_deep_lake_vitamin_medium__83e173f7.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, and no focused validator for embedded `MediaRecipe.curation_history` arrays is exposed. |

The documented `just validate-*` wrappers remain blocked for this environment by project dependency resolution under Python 3.13, so this review used the equivalent no-project Python 3.11 validators already cached under `/private/tmp/uv-cache-culturemech-review`.

## Identity and Grounding

- **Medium identity is correct.** The record denotes JCM/MediaDive `J170` `ARTIFICIAL DEEP LAKE VITAMIN MEDIUM`, and its `mediadive.medium:J170` grounding agrees with `CultureMech:002530` in both the generated record and current normalized owner.
- **The liquid formulation and pH are source-supported.** The inspected JCM medium 170 page lists the same basal liquid formulation, pH 7.4, and optional 20.0 g/L Noble Agar addition for solid medium.
- **The generated merge is stale.** The current normalized owner contains an `apply_cocktail_nesting.py` event on 2026-08-13 that moved the three stock-strength vitamins under `Vitamin solution` at `10 ML_PER_L`; this generated record was merged on 2026-08-06 and still has `Biotin`, `Vitamin B12`, and `Thiamine HCl` as direct final-medium ingredients.

## Evidence

- The inspected JCM medium 170 page supports the basal NaCl, magnesium chloride hexahydrate, magnesium sulfate heptahydrate, KCl, calcium chloride dihydrate, sodium succinate, and yeast extract amounts present in the record.
- JCM also supports the normalized owner's nested stock representation: the final medium receives 10.0 ml of `Vitamin solution`, and that stock contains 0.1 g each of biotin, Vitamin B12, and thiamine HCl in 1.0 L distilled water.
- `data/normalized_yaml/bacterial/artificial_deep_lake_vitamin_medium.yaml` now has a `solutions` entry with those three vitamin components and `concentration.unit: ML_PER_L`; the generated file lacks a `solutions` entry and still exposes all three vitamin rows under `ingredients`.

## Completeness

- The source note identifies JCM and links to medium 170; no structured `references` block is present, but the formulation can be recovered.
- Preparation detail is present in both the stale generated merge and the current normalized owner: the recipe says to adjust to pH 7.4, autoclave, cool to 50 C, and add the filter-sterilized vitamin solution aseptically.
- No `target_organisms`, `growth_metrics`, or incubation conditions are present. That is acceptable because the inspected JCM medium page is a formulation, not a growth assay for a named strain.
- A gitignore-independent `find` search under `reports/yaml_record_review` found no pre-existing `*artificial_deep_lake_vitamin_medium__83e173f7.md` report before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The merge artifact is stale relative to the normalized owner and still publishes the pre-nesting vitamin-stock representation. | The generated record's last merge event is from 2026-08-06 and lists `Biotin`, `Vitamin B12`, and `Thiamine HCl` as direct ingredients. The normalized owner has a 2026-08-13 `NESTED_FLATTENED_COCKTAIL` curation event and now stores those components inside `solutions[0].composition` with the final addition set to `10 ML_PER_L`. | Regenerate `data/merge_yaml/merged/artificial_deep_lake_vitamin_medium__83e173f7.yaml` from `data/normalized_yaml/bacterial/artificial_deep_lake_vitamin_medium.yaml`; do not edit the generated YAML by hand. |

No blockers found: the generated YAML is schema-valid and its ID and source grounding agree with the normalized owner.

## Recommended Edits

1. Regenerate the merge layer so `data/merge_yaml/merged/artificial_deep_lake_vitamin_medium__83e173f7.yaml` reflects the current `NESTED_FLATTENED_COCKTAIL` state from `data/normalized_yaml/bacterial/artificial_deep_lake_vitamin_medium.yaml`.
2. Confirm that the regenerated record contains a `Vitamin solution` descriptor at `10 ML_PER_L` and no direct final-medium `Biotin`, `Vitamin B12`, or `Thiamine HCl` ingredient rows.

## Follow-up Checks

- Run the narrow merge freshness or merge verification gate for `data/normalized_yaml/bacterial/artificial_deep_lake_vitamin_medium.yaml`.
- Re-run the focused schema, strict, reference, and term validators on the regenerated `data/merge_yaml/merged/artificial_deep_lake_vitamin_medium__83e173f7.yaml`.
- Manually compare the regenerated merge against JCM medium 170 to confirm the basal ingredients, pH, preparation step, and nested vitamin stock all remain aligned.

## Additional Notes

- An exact gitignore-independent search for `CultureMech:002530`, `mediadive.medium:J170`, and `NESTED_FLATTENED_COCKTAIL` in the normalized owner and generated record found the same stable ID/source in both files and the post-merge nesting event only in the normalized owner.
