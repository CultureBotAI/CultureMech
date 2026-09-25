# YAML Record Review: artificial_seawater_base_with_thiosulfate_as_the_electron_donor

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml
- Started UTC: 2026-09-21T15:15:24Z
- Finished UTC: 2026-09-21T15:16:45Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml` |
| Stable ID | `CultureMech:008841` |
| Name | `artificial_seawater_base_with_thiosulfate_as_the_electron_donor` |
| Original name | `Artificial seawater base with thiosulfate as the electron donor` |
| Category | `bacterial` |
| Merge state | Single-source merge from `artificial_seawater_base_with_thiosulfate_as_the_electron_donor` with fingerprint `56d84f1f811c62af899070183b301188bcfdeb8edc3a3c2018f34769aa19e91f` |

The reviewed record is a stale generated merge. The normalized owner has a 2026-09-12 repair event that corrected TOGO `M2252` after this generated record was last merged on 2026-08-06.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml --out /private/tmp/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, and no focused validator for embedded `MediaRecipe.curation_history` arrays is exposed. |

The documented `just validate-*` wrappers remain blocked for this environment by project dependency resolution under Python 3.13, so this review used the equivalent no-project Python 3.11 validators already cached under `/private/tmp/uv-cache-culturemech-review`.

## Identity and Grounding

- **Medium identity is correct.** TOGO `M2252` identifies `Artificial seawater base with thiosulfate as the electron donor`, which matches `CultureMech:008841`.
- **The generated merge is stale.** The current normalized owner changed `Artificial seawater` from `1 G_PER_L` to `1000.0 ML_PER_L`, renamed and grounded `O2` as dioxygen, and added 25 C static O2-gradient context plus references; the generated record still has the old `1 G_PER_L` seawater and ungrounded `O2` rows.
- **The unmapped artificial seawater base is intentional in the normalized owner.** The repaired normalized notes keep it without a single-compound ontology grounding because the source lists a complex seawater mixture.

## Evidence

- The TOGO API returned `gm` `http://togomedium.org/medium/M2252` with components `Artificial seawater`, `thiosulfate`, and `O2`.
- TOGO lists `Artificial seawater` as 1 L and `thiosulfate` as 10 mM; the repaired normalized owner preserves these as 1000.0 ml/L artificial seawater and 10.0 mM thiosulfate.
- TOGO comments state that strain MC-1 was grown microaerobically with thiosulfate as the electron donor and incubated statically under an O2 gradient at 25 C in the dark; the repaired normalized owner captures the incubation context, but the generated merge does not.

## Completeness

- The generated merge is missing the post-repair references to TOGO `M2252` and the supporting PMC article.
- The generated merge is also missing the curated `temperature_value`, `aeration`, `incubation_atmosphere`, and data-quality flags from the normalized owner.
- A gitignore-independent `find` search under `reports/yaml_record_review` found no pre-existing `*Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.md` report before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale relative to the repaired normalized owner. | `data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml` was generated on 2026-08-06 and still has `Artificial seawater` at `1 G_PER_L` plus ungrounded `O2`. The normalized owner has a 2026-09-12 `RESOLVED_TOGO_M2252_ARTIFICIAL_SEAWATER_THIOSULFATE_SCORE15` event that corrects those rows and adds incubation context and references. | Regenerate `data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml` from `data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml`; do not edit the generated YAML by hand. |

No blockers found: the generated YAML is schema-valid and still points to the intended `TOGO:M2252` identity.

## Recommended Edits

1. Regenerate the merge layer so `data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml` reflects the current repaired normalized record.
2. Confirm that the regenerated record contains `Artificial seawater` at `1000.0 ML_PER_L`, `Oxygen gas` grounded to `CHEBI:15379`, the 25 C static O2-gradient context, and the TOGO/PMC references.

## Follow-up Checks

- Run the narrow merge freshness or merge verification gate for `data/normalized_yaml/bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml`.
- Re-run the focused schema, strict, reference, and term validators on the regenerated `data/merge_yaml/merged/Artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml`.
- Manually compare the regenerated merge against TOGO `M2252` and the normalized owner's 2026-09-12 curation note.

## Additional Notes

- An exact gitignore-independent search for `CultureMech:008841`, `TOGO:M2252`, `RESOLVED_TOGO_M2252`, `1000.0`, `dioxygen`, and `static O2` in the normalized owner and generated record found the post-repair details only in the normalized owner.
