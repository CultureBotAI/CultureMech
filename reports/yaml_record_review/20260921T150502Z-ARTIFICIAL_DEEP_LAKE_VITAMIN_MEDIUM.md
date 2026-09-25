# YAML Record Review: artificial_deep_lake_vitamin_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ARTIFICIAL_DEEP_LAKE_VITAMIN_MEDIUM.yaml
- Started UTC: 2026-09-21T15:03:23Z
- Finished UTC: 2026-09-21T15:05:03Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/ARTIFICIAL_DEEP_LAKE_VITAMIN_MEDIUM.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M162_Artificial_Deep_Lake_Vitamin_Medium.yaml` |
| Stable ID | `CultureMech:008185` |
| Name | `artificial_deep_lake_vitamin_medium` |
| Original name | `Artificial Deep Lake Vitamin Medium` |
| Category | `bacterial` |
| Merge state | Single-source merge from `TOGO_M162_Artificial_Deep_Lake_Vitamin_Medium` with fingerprint `98d45e3e8b0c901cb5d36e1668ccf870323240dc49e87ec906ffd60211119ffe` |

The reviewed file is generated from the normalized TOGO/JCM import above. Future edits should fix that normalized YAML or the TOGO import and solution-migration paths that created the flattened stock; regenerate this merge product instead of editing it directly.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARTIFICIAL_DEEP_LAKE_VITAMIN_MEDIUM.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARTIFICIAL_DEEP_LAKE_VITAMIN_MEDIUM.yaml --out /private/tmp/ARTIFICIAL_DEEP_LAKE_VITAMIN_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARTIFICIAL_DEEP_LAKE_VITAMIN_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARTIFICIAL_DEEP_LAKE_VITAMIN_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, and no focused validator for embedded `MediaRecipe.curation_history` arrays is exposed. |

The documented `just validate-*` wrappers remain blocked for this environment by project dependency resolution under Python 3.13, so this review used the equivalent no-project Python 3.11 validators already cached under `/private/tmp/uv-cache-culturemech-review`.

## Identity and Grounding

- **Medium identity is correct.** `TOGO:M162` is `Artificial Deep Lake Vitamin Medium`, imported from `JCM_M170`; JCM medium 170 has the same name and source formulation.
- **The liquid-vs-solid distinction is correct.** The JCM/JCM_M170 page describes a basal liquid recipe and says Noble agar can be added when preparing solid medium; sibling TOGO `M163` is the solid counterpart and includes 20 g/L Noble Agar, but the current M162 record omits agar and is correctly `LIQUID`.
- **The basal salts and yeast extract are source-supported.** NaCl, magnesium chloride hexahydrate, magnesium sulfate heptahydrate, KCl, calcium chloride dihydrate, sodium succinate, and Yeast extract amounts match JCM and the TOGO `M162` API.
- **The vitamin stock has been flattened incorrectly.** JCM and TOGO keep the vitamin compounds and 1 L stock water under a separately prepared Vitamin solution; the generated record carries those stock contents as final-medium ingredients and leaves an empty `solutions[0].composition`.

## Evidence

- The TOGO API returned `gm` `http://togomedium.org/medium/M162`, `name` `Artificial Deep Lake Vitamin Medium`, `original_media_id` `JCM_M170`, `src_url` pointing to the JCM medium 170 page, and `ph` `7.4`, matching the local `TOGO:M162` identity.
- The inspected JCM medium 170 HTML gives the same basal recipe as the local record and lists `Vitamin solution (see below)` as a 10.0 ml addition, followed by a separate Vitamin solution containing 0.1 g biotin, 0.1 g Vitamin B12, 0.1 g thiamine HCl, and 1.0 L distilled water.
- The JCM prose supports preparation claims that are missing from the TOGO record: bring the basal medium to 990 ml, adjust pH to 7.4, autoclave before adding vitamins, cool to 50 C, and add the vitamin solution aseptically after filter sterilization.
- `data/normalized_yaml/bacterial/artificial_deep_lake_vitamin_medium.yaml`, a MediaDive/JCM `J170` sibling for the same source page, already nests the three stock-strength vitamin ingredients under a `Vitamin solution` descriptor at `10 ML_PER_L`. That record is useful as a local fix precedent, but the JCM page remains the primary source.

## Completeness

- The source URL and TOGO/JCM identifiers are sufficient to recover the formulation; no structured `references` block is present.
- No `target_organisms`, `growth_metrics`, or incubation conditions are present. That is acceptable because the inspected JCM medium page is a formulation, not a growth assay for a named strain.
- The absent pH and preparation fields are consequential: following the generated record alone would not preserve the basal volume, pH, autoclaving, cooling, or filter-sterilized aseptic stock addition from the source.
- A gitignore-independent `find` search under `reports/yaml_record_review` found no pre-existing `*ARTIFICIAL_DEEP_LAKE_VITAMIN_MEDIUM.md` report before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The TOGO subcomponent was flattened into final-medium ingredients and then water was incorrectly merged. The final record has direct `Biotin`, `Thiamine.HCl`, and `Vitamin B12` ingredients at `0.1 G_PER_L`, plus `distilled water` as `991.0 G_PER_L` with a duplicate-merge note. | JCM and TOGO put those three vitamins and 1.0 L distilled water inside the Vitamin solution subcomponent. The final medium receives 10 ml of that stock and separately has basal volume brought to 990 ml; adding those two water rows and representing the sum as g/L changes both the stock boundary and the dimension. | `data/normalized_yaml/bacterial/TOGO_M162_Artificial_Deep_Lake_Vitamin_Medium.yaml`; likely also the TOGO import or `scripts/cleanup_media_quality.py` duplicate-water path. |
| Major | The represented stock addition has an empty composition and the wrong amount unit. | JCM and TOGO specify 10.0 ml of Vitamin solution; the generated record has `solutions[0].composition: []` and `10 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M162_Artificial_Deep_Lake_Vitamin_Medium.yaml`; likely also `scripts/migrate_solutions_from_ingredients.py`. |
| Major | JCM pH and preparation details are missing. | JCM gives pH 7.4, a 990 ml basal preparation volume, autoclaving before vitamin addition, cooling to 50 C, and aseptic addition of filter-sterilized vitamin solution. None of those instructions is represented in the generated or normalized TOGO record. | `data/normalized_yaml/bacterial/TOGO_M162_Artificial_Deep_Lake_Vitamin_Medium.yaml`. |

No blockers found: the YAML is valid, `CultureMech:008185` points to the intended TOGO/JCM medium, and sibling `M163` appears to carry the solid-agar variant rather than being conflated into this liquid record.

## Recommended Edits

1. Apply the stock-nesting shape already present in `data/normalized_yaml/bacterial/artificial_deep_lake_vitamin_medium.yaml` to `data/normalized_yaml/bacterial/TOGO_M162_Artificial_Deep_Lake_Vitamin_Medium.yaml`, preserving JCM as the supporting source:
   - keep only the basal salts and Yeast extract as direct ingredients;
   - remove stock-only `Biotin`, `Thiamine.HCl`, `Vitamin B12`, and 1 L stock water from direct final-medium ingredients;
   - add a `Vitamin solution` descriptor containing the three 0.1 g/L stock vitamin components;
   - set the stock addition to `10 ML_PER_L`.
2. Restore source-scoped preparation details for 990 ml basal volume, final pH 7.4, autoclaving, cooling to 50 C, and aseptic addition of the filter-sterilized vitamin stock.
3. Add or refine a TOGO importer or post-import migration regression that prevents named subcomponents from becoming direct final-medium ingredients, then regenerate `data/merge_yaml/merged/ARTIFICIAL_DEEP_LAKE_VITAMIN_MEDIUM.yaml`.

## Follow-up Checks

- Re-run `just validate-schema data/normalized_yaml/bacterial/TOGO_M162_Artificial_Deep_Lake_Vitamin_Medium.yaml` and `just validate-strict data/normalized_yaml/bacterial/TOGO_M162_Artificial_Deep_Lake_Vitamin_Medium.yaml` after the normalized edit.
- Regenerate the merge layer and confirm the generated record no longer contains final-medium `0.1 G_PER_L` vitamin rows, `991.0 G_PER_L` distilled water, or an empty Vitamin solution descriptor.
- Manually compare the regenerated generated YAML against TOGO `M162`, JCM medium 170, and sibling `M163` to confirm that the liquid and solid variants stay distinct.

## Additional Notes

- `find data/normalized_yaml -iname '*artificial*deep*lake*vitamin*medium*.yaml' -print` found three normalized records: the TOGO `M162` liquid record reviewed here, the sibling MediaDive/JCM `J170` record, and TOGO `M163`, the JCM solid-agar variant.
- The JCM URL cited in the source note was live at review time and returned medium 170, `ARTIFICIAL DEEP LAKE VITAMIN MEDIUM`.
