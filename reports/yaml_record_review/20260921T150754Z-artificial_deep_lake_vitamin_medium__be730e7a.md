# YAML Record Review: artificial_deep_lake_vitamin_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/artificial_deep_lake_vitamin_medium__be730e7a.yaml
- Started UTC: 2026-09-21T15:06:24Z
- Finished UTC: 2026-09-21T15:07:55Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/artificial_deep_lake_vitamin_medium__be730e7a.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M163_Artificial_Deep_Lake_Vitamin_Medium.yaml` |
| Stable ID | `CultureMech:008195` |
| Name | `artificial_deep_lake_vitamin_medium` |
| Original name | `Artificial Deep Lake Vitamin Medium` |
| Category | `bacterial` |
| Merge state | Single-source merge from `TOGO_M163_Artificial_Deep_Lake_Vitamin_Medium` with fingerprint `be730e7aa014b21b43698d60dbe2b977212e8b4c0c22b663c5996814b5d11c34` |

The reviewed file is a generated merge product. The authoritative record is the normalized TOGO/JCM `M163` solid-agar variant above; fix that normalized YAML or the importer/migrator path, then regenerate this merge product.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/artificial_deep_lake_vitamin_medium__be730e7a.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/artificial_deep_lake_vitamin_medium__be730e7a.yaml --out /private/tmp/artificial_deep_lake_vitamin_medium__be730e7a.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/artificial_deep_lake_vitamin_medium__be730e7a.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/artificial_deep_lake_vitamin_medium__be730e7a.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, and no focused validator for embedded `MediaRecipe.curation_history` arrays is exposed. |

The documented `just validate-*` wrappers remain blocked for this environment by project dependency resolution under Python 3.13, so this review used the equivalent no-project Python 3.11 validators already cached under `/private/tmp/uv-cache-culturemech-review`.

## Identity and Grounding

- **Medium identity is correct.** The generated record is grounded to `TOGO:M163`, and the TOGO API identifies `M163` as `Artificial Deep Lake Vitamin Medium` from `JCM_M170-2`.
- **The solid-agar variant is distinct from the liquid `M162` record.** TOGO `M163` carries the same basal salts as `M162`, adds 20 g/L Noble Agar, and uses the same JCM medium 170 URL; the record's `SOLID_AGAR` physical state and direct Noble Agar ingredient are source-supported.
- **The Vitamin solution cross-reference is incomplete.** TOGO represents `Vitamin solution (see Medium [M162])` as a 10 ml addition with `reference_media_id: M162`; the generated record keeps the name and a free-text note but has an empty composition and rewrites the amount as `10 G_PER_L`.

## Evidence

- The TOGO `M163` API returned `gm` `http://togomedium.org/medium/M163`, `original_media_id` `JCM_M170-2`, and the expected JCM `GRMD=170` source URL.
- JCM medium 170 supports the basal formulation, the pH 7.4 preparation, and the instruction to add 20.0 g/L Noble Agar for solid medium.
- TOGO `M163` specifically adds `Noble Agar (BD-Difco)` at 20 g/L and keeps the final-medium `Vitamin solution` addition as 10 ml, pointing to Medium `M162` for the stock rather than inlining vitamin stock ingredients.

## Completeness

- The source URL and TOGO/JCM identifiers are sufficient to recover the formulation, and the `M162` cross-reference is visible in the solution note, but it is not a resolved internal link or a usable stock composition.
- No `ph_value` or `preparation_steps` are present even though the source says to adjust to pH 7.4, prepare the basal medium to 990 ml, autoclave, cool to 50 C, and add filter-sterilized vitamin solution aseptically.
- No `target_organisms`, `growth_metrics`, or incubation conditions are present. That is acceptable because the inspected JCM medium page is a formulation, not a growth assay for a named strain.
- A gitignore-independent `find` search under `reports/yaml_record_review` found no pre-existing `*artificial_deep_lake_vitamin_medium__be730e7a.md` report before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The `M162` Vitamin solution cross-reference is unresolved and has the wrong unit. | TOGO `M163` adds 10 ml of `Vitamin solution (see Medium [M162])`; the generated and normalized records contain `composition: []`, `notes: Cross-reference to Medium M162`, and `concentration.unit: G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M163_Artificial_Deep_Lake_Vitamin_Medium.yaml`; likely also `scripts/migrate_solutions_from_ingredients.py`. |
| Major | Source pH and preparation instructions are missing. | The shared JCM medium 170 source tells the curator to bring the basal medium to 990 ml, adjust pH to 7.4, autoclave, cool to 50 C, and aseptically add the filter-sterilized vitamin solution. None of that detail is represented in `ph_value` or `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M163_Artificial_Deep_Lake_Vitamin_Medium.yaml`. |

No blockers found: the YAML is valid, the intended `TOGO:M163` identity is correct, and the solid agar ingredient is not conflated with the liquid `M162` target.

## Recommended Edits

1. Replace the empty Vitamin solution descriptor with a resolved representation of the `M162` vitamin stock and set the addition to 10 ml per liter, not `10 G_PER_L`.
2. Add source-scoped `ph_value: 7.4` and preparation detail for 990 ml basal volume, autoclaving, cooling to 50 C, and aseptic addition of the filter-sterilized vitamin stock.
3. Preserve the 20 g/L Noble Agar row and `SOLID_AGAR` state, then regenerate `data/merge_yaml/merged/artificial_deep_lake_vitamin_medium__be730e7a.yaml`.

## Follow-up Checks

- Re-run `just validate-schema data/normalized_yaml/bacterial/TOGO_M163_Artificial_Deep_Lake_Vitamin_Medium.yaml` and `just validate-strict data/normalized_yaml/bacterial/TOGO_M163_Artificial_Deep_Lake_Vitamin_Medium.yaml` after the normalized edit.
- Re-run `just validate-references data/normalized_yaml/bacterial/TOGO_M163_Artificial_Deep_Lake_Vitamin_Medium.yaml` if the `M162` stock is represented with an internal reference.
- Regenerate the merge layer and confirm the generated record has the pH/preparation fields and no longer contains an empty `10 G_PER_L` Vitamin solution.

## Additional Notes

- The inspected JCM `GRMD=170` page is shared by the liquid `M162` and solid `M163` TOGO records; reviewing this solid variant still required the `M163` TOGO API because only `M163` exposes the 20 g/L agar row as part of the target medium.
- An exact gitignore-independent search for `TOGO:M163`, `M170-2`, `CultureMech:008195`, and `Medium [M162]` in the normalized owner and generated record found the same target identity and cross-reference in both files.
