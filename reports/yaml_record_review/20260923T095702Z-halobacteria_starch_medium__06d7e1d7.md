# YAML Record Review: Halobacteria Starch Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/halobacteria_starch_medium__06d7e1d7.yaml
- Started UTC: 2026-09-23T09:55:36Z
- Finished UTC: 2026-09-23T09:57:02Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/halobacteria_starch_medium__06d7e1d7.yaml`, a
generated `MediaRecipe` with `id: CultureMech:010369`, `category: archaea`,
`physical_state: SOLID_AGAR`, and `media_term.term.id: TOGO:M946`.

The generated record is a single-source merge from the maintained Togo parent
`data/normalized_yaml/archaea/TOGO_M946_Halobacteria_Starch_Medium.yaml`, which
imports the solid `JCM_M904-2` form of JCM GRMD 904. Future fixes belong in
that normalized parent or in the Togo importer, then require regeneration of
`data/merge_yaml/merged/`.

## Validation

All focused structural validators passed on the generated YAML:

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halobacteria_starch_medium__06d7e1d7.yaml` | Passed |
| `python scripts/validate_strict.py data/merge_yaml/merged/halobacteria_starch_medium__06d7e1d7.yaml --out /private/tmp/halobacteria_starch_medium__06d7e1d7.strict.tsv --workers 1 --quiet` | Passed, 0 error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/halobacteria_starch_medium__06d7e1d7.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/halobacteria_starch_medium__06d7e1d7.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |

Embedded `MediaRecipe.curation_history` was not checked: the repository's
`just validate-history` target validates standalone files under `history/`,
not embedded curation events in generated media YAML.

## Identity and Grounding

The source identity is correct. Togo M946 names `Halobacteria Starch Medium`,
identifies its original medium as `JCM_M904-2`, and points to JCM GRMD 904.
The solid state is source-supported because M946 includes the JCM solid
variant's 20 g/L agar addition.

Several exact source chemicals are represented only partially. Sodium glutamate
monohydrate is left ungrounded even though the direct MediaDive/JCM parent has
a specific ChEBI mapping, and trisodium citrate dihydrate is grounded to
generic sodium citrate.

## Evidence

Supported by inspected JCM, Togo, and MediaDive sources:

- JCM 904 is `HALOBACTERIA STARCH MEDIUM`.
- The base recipe contains 10 g soluble starch, 1 g sodium glutamate
  monohydrate, 3 g trisodium citrate dihydrate, 20 g `MgSO4 x 7 H2O`, 2 g KCl,
  200 g NaCl, 36 mg `FeCl2 x 4 H2O`, and 0.36 mg `MnCl2 x 4 H2O`.
- Togo M946 and JCM both put the medium at pH 7.0 to 7.2.
- Togo M946 is the solid form with 20 g/L agar.

Unsupported or incomplete claims:

- The generated `FeCl2 x 4 H2O` row says 36 g/L, but JCM, MediaDive, and Togo
  say 36 mg per liter.
- The generated `MnCl2 x 4 H2O` row says 0.36 g/L, but JCM, MediaDive, and
  Togo say 0.36 mg per liter.
- Distilled water is recorded as `1 G_PER_L` even though Togo records 1 L and
  JCM uses enough distilled water to bring the recipe to 1.0 L.
- The generated Togo record omits the pH 7.0 to 7.2 adjustment and final-volume
  preparation text that Togo exposes from JCM.
- The generated record omits the JCM default autoclaving condition.

## Completeness

- The record has no `target_organisms` or `growth_metrics`; no organism-growth
  claims are asserted or missing evidence.
- Source identity is recoverable through `media_term` and `notes`, but there
  are no first-class `sources` entries for Togo M946 or JCM GRMD 904.
- An exact `rg --no-ignore --hidden` search over `data/merge_yaml` and
  `data/normalized_yaml` for `TOGO:M946`, `JCM_M904-2`, the JCM GRMD 904 URL,
  and the source label found the reviewed M946 solid parent, the M945 liquid
  sibling, and the direct JCM/MediaDive J904 import from the same JCM page.

## Findings

### Blocker

None found.

### Major

1. The iron and manganese milligram rows were imported as g/L values. The
   generated `FeCl2 x 4 H2O` and `MnCl2 x 4 H2O` concentrations are 1000-fold
   too high. Owner:
   `data/normalized_yaml/archaea/TOGO_M946_Halobacteria_Starch_Medium.yaml` or
   the Togo unit-conversion path.

2. The final-water representation is wrong. The source recipe is made to 1 L,
   but the generated record stores distilled water as `1 G_PER_L`. Owner: the
   Togo normalized parent or importer.

3. Togo/JCM pH and preparation evidence was dropped. Togo preserves the
   final-volume, pH 7.0 to 7.2, and solid-agar comments; the generated record
   has no `preparation_steps` or pH field. Owner: the Togo normalized parent or
   importer.

4. The M946 solid recipe is not linked to its corresponding M945 liquid
   recipe. Both come from JCM GRMD 904, and M946 is the solid variant with
   20 g/L agar. Owner: normalized variant metadata for M945 and M946.

### Minor

1. Sodium glutamate monohydrate lacks the exact grounding present on the direct
   MediaDive/JCM import, and trisodium citrate dihydrate is grounded only to
   generic sodium citrate. Owner: the Togo normalized ingredient groundings and
   packaged MediaIngredientMech label index.

2. First-class `sources` are absent; the Togo and JCM source identifiers are
   stored only in `media_term` and `notes`. Owner: the normalized parent or
   importer.

## Recommended Edits

1. Convert `FeCl2 x 4 H2O` to 36 mg/L and `MnCl2 x 4 H2O` to 0.36 mg/L in
   the Togo M946 parent.
2. Replace `Distilled water: 1 G_PER_L` with a final-volume representation of
   1 L.
3. Add the pH 7.0 to 7.2 range, bring-to-1-L preparation text, and JCM default
   autoclaving condition.
4. Add a solid-variant relationship from M946 to the M945 liquid Halobacteria
   Starch Medium.
5. Recheck sodium glutamate monohydrate and trisodium citrate dihydrate against
   the packaged MIM label index and OAK.
6. Regenerate merge products after repairing the Togo parent or importer.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the edited M946 and
  M945 normalized records.
- Fetch Togo M946, Togo M945, MediaDive J904, and JCM GRMD 904 again and
  compare pH, agar placement, trace-salt units, and final-volume text.
- Run `just validate-media-variant-links` after adding the M946/M945 solid
  variant relation.

## Additional Notes

The direct MediaDive/JCM J904 import has the correct mg/L trace-salt units and
pH but represents the base liquid recipe. Keep M946 as a distinct solid variant
rather than merging away its agar addition.
