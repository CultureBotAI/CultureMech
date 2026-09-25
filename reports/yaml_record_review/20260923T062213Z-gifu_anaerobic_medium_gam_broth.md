# YAML Record Review: gifu_anaerobic_medium_gam_broth

- Repository: CultureMech
- Record: data/merge_yaml/merged/gifu_anaerobic_medium_gam_broth.yaml
- Started UTC: 2026-09-23T06:20:35Z
- Finished UTC: 2026-09-23T06:22:13Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:009239` is the Togo import for Togo M2684, `Gifu anaerobic medium (GAM) broth`.

The generated record derives from `data/normalized_yaml/bacterial/gifu_anaerobic_medium_gam_broth.yaml`. An ignored-file-inclusive exact search for `TOGO:M2684`, `M2684`, and `gifu_anaerobic_medium_gam_broth` found only that maintained source row, this generated record, and normalized source indexes.

## Validation

`linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gifu_anaerobic_medium_gam_broth.yaml` passed.

`scripts/validate_strict.py data/merge_yaml/merged/gifu_anaerobic_medium_gam_broth.yaml --workers 1 --quiet` passed with 0 error rows.

`linkml-reference-validator validate data data/merge_yaml/merged/gifu_anaerobic_medium_gam_broth.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` passed with 0 checks.

`linkml-term-validator validate-data data/merge_yaml/merged/gifu_anaerobic_medium_gam_broth.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `TOGO:M2684` identity, label, category, complex/undefined classification, and liquid state agree with the Togo M2684 payload.

The commercial `GAM broth (Nissui)` component is correctly left ungrounded because it is an undefined proprietary product rather than a single ChEBI chemical.

## Evidence

Togo M2684 lists 1 L distilled water and 59 g GAM broth (Nissui).

Togo M2684 also carries a comment reporting that Clostridium perfringens strains were cultured in GAM broth or GAM agar plates at 37 C under anaerobic conditions using AnaeroPack.

The maintained normalized row already records the 1000 ml water amount, 59 g/L GAM broth, a 37 C temperature value, the Togo URL as a reference, and a `RESOLVED_TOGO_SPARSE_SCORE20` curation event from 2026-09-10.

## Completeness

The generated record is stale relative to the maintained normalized row: it still has distilled water as `1 G_PER_L` and lacks the source annotations, 37 C temperature, reference, quality flags, and 2026-09-10 repair event.

No formula row from the current Togo M2684 payload is absent.

Empty pH, preparation-step, variant, and publication slots are acceptable because Togo M2684 does not provide those details.

## Findings

- Major: `data/merge_yaml/merged/gifu_anaerobic_medium_gam_broth.yaml` is stale relative to `data/normalized_yaml/bacterial/gifu_anaerobic_medium_gam_broth.yaml`; it has the old `1 G_PER_L` water row instead of the repaired 1000 ml/L water row.
- Minor: The generated record omits the maintained source annotations, `temperature_value: 37.0`, Togo reference, data-quality flags, and 2026-09-10 curation event.

## Recommended Edits

- Regenerate this merge from `data/normalized_yaml/bacterial/gifu_anaerobic_medium_gam_broth.yaml` so the current Togo M2684 repair is reflected in the generated layer.
- After regeneration, confirm the generated record preserves the GAM broth product as ungrounded and does not introduce a fake small-molecule term.

## Follow-up Checks

- Re-run merge freshness or regeneration checks and confirm `data/merge_yaml/merged/gifu_anaerobic_medium_gam_broth.yaml` contains `1000 ML_PER_L`, `temperature_value: 37.0`, and the 2026-09-10 `RESOLVED_TOGO_SPARSE_SCORE20` history entry.
- Re-run LinkML, strict, reference, and term validation on the regenerated generated YAML.

## Additional Notes

The exact source search used `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged`, so ignored generated records and index files were included.
