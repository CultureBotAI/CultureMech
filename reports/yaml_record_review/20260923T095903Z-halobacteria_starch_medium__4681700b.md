# YAML Record Review: HALOBACTERIA STARCH MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/halobacteria_starch_medium__4681700b.yaml
- Started UTC: 2026-09-23T09:58:24Z
- Finished UTC: 2026-09-23T09:59:03Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/halobacteria_starch_medium__4681700b.yaml`, a
generated `MediaRecipe` with `id: CultureMech:003253`, `category: archaea`,
`physical_state: LIQUID`, `ph_value: 7.1`, and
`media_term.term.id: mediadive.medium:J904`.

The generated record is a single-source merge from the maintained parent
`data/normalized_yaml/archaea/halobacteria_starch_medium.yaml`, which imports
JCM Medium J904 through MediaDive. Future fixes belong in that normalized
parent or in the MediaDive/JCM importer, then require regeneration of
`data/merge_yaml/merged/`.

## Validation

All focused structural validators passed on the generated YAML:

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halobacteria_starch_medium__4681700b.yaml` | Passed |
| `python scripts/validate_strict.py data/merge_yaml/merged/halobacteria_starch_medium__4681700b.yaml --out /private/tmp/halobacteria_starch_medium__4681700b.strict.tsv --workers 1 --quiet` | Passed; emitted a header-only TSV |
| `linkml-reference-validator validate data data/merge_yaml/merged/halobacteria_starch_medium__4681700b.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/halobacteria_starch_medium__4681700b.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |

Embedded `MediaRecipe.curation_history` was not checked: the repository's
`just validate-history` target validates standalone files under `history/`,
not embedded curation events in generated media YAML.

## Identity and Grounding

The record identifies the correct JCM/MediaDive recipe. MediaDive J904 and JCM
GRMD 904 both name `HALOBACTERIA STARCH MEDIUM`, and the generated
ingredient amounts preserve JCM's g versus mg units.

The base JCM recipe is liquid. JCM's 20 g/L agar instruction is explicitly for
preparing solid medium, so the current `physical_state: LIQUID` is defensible
only if that solid-agar instruction is modeled as a separate variant rather
than as an unconditional step on the liquid record.

## Evidence

Supported by inspected JCM, MediaDive, and Togo sources:

- JCM 904 is `HALOBACTERIA STARCH MEDIUM`.
- The base recipe contains 10 g soluble starch, 1 g sodium glutamate
  monohydrate, 3 g trisodium citrate dihydrate, 20 g `MgSO4 x 7 H2O`, 2 g KCl,
  200 g NaCl, 36 mg `FeCl2 x 4 H2O`, and 0.36 mg `MnCl2 x 4 H2O`.
- The base recipe is brought to 1.0 L and adjusted to pH 7.0 to 7.2.
- The 20 g/L agar addition is only for preparation of a solid medium.

Unsupported or incomplete claims:

- The generated record collapses the pH range to `ph_value: 7.1` even though
  the JCM page says pH 7.0 to 7.2.
- The generated `preparation_steps` attach the solid-agar instruction to the
  liquid recipe without modeling the solid JCM_M904-2/Togo M946 variant.
- Distilled water is absent as an ingredient even though the source says to
  bring the recipe to 1.0 L with distilled water.
- JCM's default autoclaving condition is absent.
- Soluble starch is reduced to `Starch`, losing the soluble qualifier that
  JCM, MediaDive, and Togo all preserve.
- Trisodium citrate dihydrate is grounded to generic sodium citrate.

## Completeness

- The record has no `target_organisms` or `growth_metrics`; no organism-growth
  claims are asserted or missing evidence.
- Source identity is recoverable through `media_term` and `notes`, but there
  are no first-class `sources` entries for MediaDive J904 or JCM GRMD 904.
- An exact `rg --no-ignore --hidden` search over `data/merge_yaml` and
  `data/normalized_yaml` for `mediadive.medium:J904`, `JCM Medium J904`, the
  JCM GRMD 904 URL, and the source label found the reviewed direct
  MediaDive/JCM parent plus the Togo M945 liquid and M946 solid imports from
  the same JCM page.

## Findings

### Blocker

None found.

### Major

1. The pH range is collapsed to a scalar. JCM and Togo state pH 7.0 to 7.2,
   while the generated direct record stores only `ph_value: 7.1`. Owner:
   `data/normalized_yaml/archaea/halobacteria_starch_medium.yaml` or the
   MediaDive/JCM importer.

2. The liquid record carries an unscoped solid-medium instruction. The source's
   agar instruction belongs to a solid variant, not to the base liquid recipe.
   Owner: the direct JCM parent and variant metadata linking it to the M946
   solid import.

### Minor

1. Distilled water is present only as preparation prose. Owner: the normalized
   parent or importer.

2. The soluble qualifier on soluble starch and the hydrate specificity of
   trisodium citrate dihydrate are not fully preserved. Owner: the normalized
   ingredient labels and groundings.

3. JCM's default autoclaving condition is absent. Owner: the normalized parent
   or importer.

4. First-class `sources` are absent; the JCM source identifier is stored only
   in `media_term` and `notes`. Owner: the normalized parent or importer.

## Recommended Edits

1. Replace `ph_value: 7.1` with `ph_range` 7.0 to 7.2.
2. Move the solid-agar instruction into an explicit relation to the M946 solid
   Togo variant, or otherwise scope it so the liquid recipe does not require
   agar.
3. Add distilled water as a final-volume component or preserve final volume in
   a structured way equivalent to the source.
4. Preserve the soluble starch qualifier and recheck trisodium citrate
   dihydrate against the packaged MIM label index and OAK.
5. Add JCM's default autoclaving condition if the importer supports JCM-wide
   defaults.
6. Regenerate the generated merge YAML after repairing the normalized parent.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the edited direct
  J904 normalized record.
- Fetch MediaDive J904, JCM GRMD 904, Togo M945, and Togo M946 again and
  confirm the base liquid recipe, the solid agar variant, pH, and mg units.
- Run `just validate-media-variant-links` after linking the base J904 liquid
  recipe to the solid M946 variant.

## Additional Notes

The separate Togo M945 and M946 imports have incorrect g/L conversions for the
JCM milligram trace-salt rows. Use them only for source identity and
liquid/solid variant evidence until those Togo unit bugs are fixed.
