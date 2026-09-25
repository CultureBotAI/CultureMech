# YAML Record Review: artificial_seawater_for_halophiles

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml
- Started UTC: 2026-09-21T15:12:25Z
- Finished UTC: 2026-09-21T15:13:56Z
- Verdict: pass with minor issues

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml` |
| Stable ID | `CultureMech:000298` |
| Name | `artificial_seawater_for_halophiles` |
| Original name | `ARTIFICIAL SEAWATER FOR HALOPHILES` |
| Category | `archaea` |
| Merge state | Single-source merge from `artificial_seawater_for_halophiles` with fingerprint `8278fa6adfb30f4a7d2322c08cf9c5435365077b782482f87ae9b095c43b9404` |

The target is the generated merge for the archaeal MediaDive/JCM `J457` record. `find data/normalized_yaml -iname '*artificial*seawater*for*halophiles*.yaml' -print` also found a TOGO `M457` bacterial sibling; this generated merge resolves only to the archaeal owner above.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml --out /private/tmp/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, and no focused validator for embedded `MediaRecipe.curation_history` arrays is exposed. |

The documented `just validate-*` wrappers remain blocked for this environment by project dependency resolution under Python 3.13, so this review used the equivalent no-project Python 3.11 validators already cached under `/private/tmp/uv-cache-culturemech-review`.

## Identity and Grounding

- **Medium identity is correct.** The live JCM `GRMD=457` page identifies medium 457 as `ARTIFICIAL SEAWATER FOR HALOPHILES`, matching the local `mediadive.medium:J457` grounding and stable `CultureMech:000298` record.
- **The archaeal source category is not conflated with the TOGO copy.** The generated record is a single-source merge from `data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml`, while `data/normalized_yaml/bacterial/artificial_seawater_for_halophiles.yaml` is a separate TOGO `M457` import.
- **The ingredient amounts, pH, and preparation text match JCM.** The 11 source ingredients, final pH 7.4, and the instructions to add all components except NaHCO3 and sodium pyruvate before autoclaving, then add filter-sterilized 8% NaHCO3 and 25% sodium pyruvate aseptically, are represented.

## Evidence

- The JCM page lists NaCl, magnesium chloride hexahydrate, magnesium sulfate heptahydrate, KCl, sodium bicarbonate, sodium nitrate, calcium chloride dihydrate, potassium dihydrogen phosphate, ammonium chloride, yeast extract, and sodium pyruvate at the same per-liter amounts as the record.
- JCM states that the pH is adjusted to 7.4 with 1 M Tris base; the record stores `ph_value: 7.4` and keeps Tris in the preparation step rather than turning it into a direct fixed ingredient.
- JCM states that NaHCO3 and sodium pyruvate are filter-sterilized as 8% and 25% weight/volume solutions and added aseptically; the record preserves that detail in `preparation_steps`.

## Completeness

- The original JCM URL remains live and recovers the authoritative formulation.
- Optional organism and growth-evidence fields are empty; the inspected source page is a formulation and does not assert a growth outcome for a named strain.
- The record has a legacy `mediaingredientmech_term` on the `NaNO3` row despite having the correct `CHEBI:63005` sodium nitrate grounding.
- A gitignore-independent `find` search under `reports/yaml_record_review` found no pre-existing `*ARTIFICIAL_SEAWATER_FOR_HALOPHILES.md` report before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Minor | The `NaNO3` row still uses a deprecated legacy `mediaingredientmech_term` instead of a CHEBI-keyed `mediaingredientmech_chebi_term`. | The record's 2026-06-05 migration event says 9 legacy MIM links were replaced, but `NaNO3` still has `mediaingredientmech_term: MediaIngredientMech:000171` while its primary term is already `CHEBI:63005` sodium nitrate. | `data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml`. |

No blockers or major findings found.

## Recommended Edits

1. Replace the `NaNO3` legacy `mediaingredientmech_term` with a CHEBI-keyed `mediaingredientmech_chebi_term` for `CHEBI:63005` sodium nitrate in `data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml`.
2. Regenerate `data/merge_yaml/merged/ARTIFICIAL_SEAWATER_FOR_HALOPHILES.yaml`.

## Follow-up Checks

- Re-run `just validate-schema data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml` and `just validate-strict data/normalized_yaml/archaea/artificial_seawater_for_halophiles.yaml` after the MIM link edit.
- Regenerate the merge and confirm the generated `NaNO3` row no longer contains a legacy `mediaingredientmech_term`.

## Additional Notes

- An exact gitignore-independent search for `CultureMech:000298`, `mediadive.medium:J457`, `mediaingredientmech_term`, and `NaNO3` across the normalized owner and generated record found the same legacy `NaNO3` link in both files.
