# YAML Record Review: Halobacterium Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/halobacterium_medium__42aeae1c.yaml
- Started UTC: 2026-09-23T10:00:06Z
- Finished UTC: 2026-09-23T10:01:16Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/halobacterium_medium__42aeae1c.yaml`, a
generated `MediaRecipe` with `id: CultureMech:008957`, `category: archaea`,
`physical_state: SOLID_AGAR`, and `media_term.term.id: TOGO:M2373`.

The generated record is a single-source merge from the maintained Togo parent
`data/normalized_yaml/archaea/TOGO_M2373_Halobacterium_Medium.yaml`, which
cites DSMZ Medium 97. Future fixes belong in that normalized parent or in the
Togo importer, then require regeneration of `data/merge_yaml/merged/`.

## Validation

All focused structural validators passed on the generated YAML:

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halobacterium_medium__42aeae1c.yaml` | Passed |
| `python scripts/validate_strict.py data/merge_yaml/merged/halobacterium_medium__42aeae1c.yaml --out /private/tmp/halobacterium_medium__42aeae1c.strict.tsv --workers 1 --quiet` | Passed, 0 error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/halobacterium_medium__42aeae1c.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/halobacterium_medium__42aeae1c.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |

Embedded `MediaRecipe.curation_history` was not checked: the repository's
`just validate-history` target validates standalone files under `history/`,
not embedded curation events in generated media YAML.

## Identity and Grounding

The source identity is correct. Togo M2373 is `Halobacterium Medium` and cites
DSMZ_Medium97.pdf, which names `97. HALOBACTERIUM MEDIUM`. The solid state is
source-supported by 20 g agar.

The primary hydrate groundings are mostly correct, including iron(II) sulfate
heptahydrate and manganese(II) sulfate monohydrate. `MgSO4 x 7 H2O` has a
correct primary `term`, but its `mediaingredientmech_chebi_term` still points
to generic magnesium sulfate.

## Evidence

Supported by inspected DSMZ, MediaDive, and Togo sources:

- DSMZ Medium 97 is `HALOBACTERIUM MEDIUM`.
- The recipe contains 7.5 g casamino acids, 10 g yeast extract, 3 g
  Na3-citrate, 2 g KCl, 20 g `MgSO4 x 7 H2O`, 0.05 g `FeSO4 x 7 H2O`,
  0.2 mg `MnSO4 x H2O`, 250 g NaCl, 20 g agar, and distilled water to 1000 ml.
- The pH is adjusted to 7.4.
- Agar is added after dissolving the other ingredients in water and adjusting
  pH.

Unsupported or incomplete claims:

- The generated `MnSO4 x H2O` row says 0.2 g/L, but DSMZ, MediaDive, and Togo
  say 0.2 mg/L.
- Distilled water is recorded as 1000 g/L even though the source says
  1000 ml.
- The generated Togo record omits the source pH 7.4 and the agar-after-pH
  preparation instruction.

## Completeness

- The record has no `target_organisms` or `growth_metrics`; no organism-growth
  claims are asserted or missing evidence.
- Source identity is recoverable through `media_term` and `notes`, but there
  are no first-class `sources` entries for Togo M2373 or DSMZ Medium 97.
- An exact `rg --no-ignore --hidden` search over `data/merge_yaml` and
  `data/normalized_yaml` for `TOGO:M2373`, `DSMZ_Medium97`,
  `DSMZ Medium: 97`, and the source label found the reviewed Togo parent plus
  independent direct DSMZ/MediaDive and KOMODO records for the same DSMZ
  Medium 97 recipe.

## Findings

### Blocker

None found.

### Major

1. `MnSO4 x H2O` is 1000-fold too high. The source amount is 0.2 mg/L, but the
   generated Togo record stores 0.2 g/L. Owner:
   `data/normalized_yaml/archaea/TOGO_M2373_Halobacterium_Medium.yaml` or the
   Togo unit-conversion path.

2. The final-water representation is wrong. DSMZ and Togo specify 1000 ml
   distilled water, but the generated record stores `1000 G_PER_L`. Owner: the
   Togo normalized parent or importer.

3. pH and preparation evidence was dropped. Togo exposes the pH 7.4 and
   agar-after-pH instruction from DSMZ, but the generated record has no
   `ph_value` or `preparation_steps`. Owner: the Togo normalized parent or
   importer.

4. The reviewed Togo record is split from the already-correct direct
   DSMZ/MediaDive and KOMODO Medium 97 records. Those parents already contain
   the correct 0.0002 g/L manganese conversion and should reconcile with Togo
   M2373 after the Togo unit bugs are repaired. Owner: Togo M2373 plus the
   duplicate/merge rules.

### Minor

1. `MgSO4 x 7 H2O` still has a stale generic
   `mediaingredientmech_chebi_term`, despite the primary `term` being
   heptahydrate-specific. Owner: the normalized parent ingredient grounding.

2. First-class `sources` are absent; the Togo and DSMZ source identifiers are
   stored only in `media_term` and `notes`. Owner: the normalized parent or
   importer.

## Recommended Edits

1. Convert `MnSO4 x H2O` from 0.2 mg/L to 0.0002 g/L in the Togo M2373 parent.
2. Replace `Distilled water: 1000 G_PER_L` with 1000 ml distilled water or a
   structured final-volume representation.
3. Add pH 7.4 and the source preparation instruction that agar is added after
   dissolving the other ingredients in water and adjusting pH.
4. Refresh the `MgSO4 x 7 H2O` secondary grounding so it matches
   `CHEBI:31795`.
5. Merge or link Togo M2373 with the direct DSMZ/KOMODO Medium 97 records once
   ingredient amounts and preparation fields are reconciled.
6. Regenerate merge products after repairing the Togo parent or importer.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the edited Togo
  M2373 parent.
- Fetch Togo M2373, MediaDive 97, and DSMZ_Medium97.pdf again and compare
  manganese units, water volume, pH, and agar preparation order.
- Re-run merge freshness checks and an ignored-file-inclusive exact search for
  `TOGO:M2373`, `mediadive.medium:97`, and `komodo.medium:97` to confirm the
  repaired Togo import no longer remains as a separate erroneous canonical
  record.

## Additional Notes

None found.
