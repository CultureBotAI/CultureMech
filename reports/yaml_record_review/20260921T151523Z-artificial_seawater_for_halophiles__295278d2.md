# YAML Record Review: artificial_seawater_for_halophiles

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/artificial_seawater_for_halophiles__295278d2.yaml
- Started UTC: 2026-09-21T15:13:56Z
- Finished UTC: 2026-09-21T15:15:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/artificial_seawater_for_halophiles__295278d2.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/artificial_seawater_for_halophiles.yaml` |
| Stable ID | `CultureMech:009844` |
| Name | `artificial_seawater_for_halophiles` |
| Original name | `Artificial Seawater For Halophiles` |
| Category | `bacterial` |
| Merge state | Single-source merge from `artificial_seawater_for_halophiles` with fingerprint `295278d27a07e86607b1c3f18326926f9741857eea519bb91d9a55a04c637fd1` |

The target is the generated merge for the TOGO `M457` copy of JCM medium 457. Its source label overlaps the archaeal MediaDive `J457` record, but it has a distinct `TOGO:M457` grounding and stable ID, so this review covers only the bacterial normalized owner above.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/artificial_seawater_for_halophiles__295278d2.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/artificial_seawater_for_halophiles__295278d2.yaml --out /private/tmp/artificial_seawater_for_halophiles__295278d2.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/artificial_seawater_for_halophiles__295278d2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/artificial_seawater_for_halophiles__295278d2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, and no focused validator for embedded `MediaRecipe.curation_history` arrays is exposed. |

The documented `just validate-*` wrappers remain blocked for this environment by project dependency resolution under Python 3.13, so this review used the equivalent no-project Python 3.11 validators already cached under `/private/tmp/uv-cache-culturemech-review`.

## Identity and Grounding

- **Medium identity is correct.** TOGO `M457` and the live JCM `GRMD=457` page both identify `Artificial Seawater For Halophiles`.
- **The imported salts and yeast extract are source-supported.** The JCM table lists the same NaCl, magnesium chloride hexahydrate, magnesium sulfate heptahydrate, KCl, NaHCO3, NaNO3, calcium chloride dihydrate, KH2PO4, NH4Cl, yeast extract, and sodium pyruvate amounts.
- **The `Tris base` direct ingredient is not source-supported.** JCM mentions 1 M Tris base only as the pH adjuster; TOGO parsed that prose into a component and the local schema defaulter preserved it as a variable direct ingredient.
- **The pH and preparation text were not imported.** TOGO exposes pH 7.4 and a comment with the same autoclave and filter-sterile addition instructions as JCM, but the normalized record has no `ph_value` or `preparation_steps`.

## Evidence

- The TOGO API returned `gm` `http://togomedium.org/medium/M457`, `original_media_id` `JCM_M457`, `ph` `7.4`, and the expected JCM source URL.
- The same TOGO payload included the source comment telling the curator to add all components except NaHCO3 and sodium pyruvate to distilled water, adjust to pH 7.4 with 1 M Tris base, autoclave, filter-sterilize 8% NaHCO3 and 25% sodium pyruvate solutions, and add them aseptically.
- The generated and normalized records have `Tris base` at `VARIABLE` concentration under `ingredients`, matching the 2026-02-03 defaulting event rather than a source recipe row.

## Completeness

- The source identity and original JCM URL are recoverable from the notes.
- The lack of organism and growth-evidence fields is acceptable because the inspected source page only defines a recipe.
- The recipe is incomplete without pH and preparation instructions: following the record as structured loses the autoclave boundary and the aseptic bicarbonate/pyruvate additions.
- A gitignore-independent `find` search under `reports/yaml_record_review` found no pre-existing `*artificial_seawater_for_halophiles__295278d2.md` report before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The pH-adjuster prose was imported as a variable direct `Tris base` ingredient. | JCM uses 1 M Tris base only to adjust pH to 7.4; neither the JCM ingredient table nor the TOGO ingredient list assigns a fixed recipe amount to Tris. The CultureMech record now presents it as an ingredient with `value: variable`. | `data/normalized_yaml/bacterial/artificial_seawater_for_halophiles.yaml`; likely also the TOGO importer/defaulting path. |
| Major | Source pH and preparation instructions are missing. | TOGO and JCM both give pH 7.4, autoclaving, and post-sterilization aseptic addition of filter-sterilized 8% NaHCO3 and 25% sodium pyruvate stocks; the generated and normalized records have no `ph_value` or `preparation_steps`. | `data/normalized_yaml/bacterial/artificial_seawater_for_halophiles.yaml`. |

No blockers found: the YAML validates and the `TOGO:M457` identity is correct.

## Recommended Edits

1. Remove the variable direct `Tris base` ingredient from `data/normalized_yaml/bacterial/artificial_seawater_for_halophiles.yaml` and keep Tris scoped to the pH-adjustment preparation text.
2. Add `ph_value: 7.4` and preparation instructions for the basal autoclave step plus aseptic addition of filter-sterilized 8% NaHCO3 and 25% sodium pyruvate solutions.
3. Regenerate `data/merge_yaml/merged/artificial_seawater_for_halophiles__295278d2.yaml`.

## Follow-up Checks

- Re-run `just validate-schema data/normalized_yaml/bacterial/artificial_seawater_for_halophiles.yaml` and `just validate-strict data/normalized_yaml/bacterial/artificial_seawater_for_halophiles.yaml` after the normalized edit.
- Regenerate the merge and manually compare it against TOGO `M457` and JCM medium 457 to confirm that Tris is no longer direct while pH 7.4 and the aseptic bicarbonate/pyruvate additions remain represented.

## Additional Notes

- Exact gitignore-independent searches for `CultureMech:009844`, `TOGO:M457`, `Tris base`, and the `Added default concentration` curation note in the normalized owner and generated record found the same variable Tris ingredient in both files.
