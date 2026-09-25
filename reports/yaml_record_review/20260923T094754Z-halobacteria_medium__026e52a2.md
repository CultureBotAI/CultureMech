# YAML Record Review: Halobacteria Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/halobacteria_medium__026e52a2.yaml
- Started UTC: 2026-09-23T09:46:00Z
- Finished UTC: 2026-09-23T09:47:54Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/halobacteria_medium__026e52a2.yaml`, a
generated `MediaRecipe` with `id: CultureMech:008953`, `category: archaea`,
`physical_state: SOLID_AGAR`, and `media_term.term.id: TOGO:M2369`.

The generated record is a single-source merge from the maintained Togo parent
`data/normalized_yaml/archaea/TOGO_M2369_Halobacteria_Medium.yaml`, which cites
DSMZ Medium 372 as its source. Future fixes belong in that normalized parent or
in the Togo importer, then require regeneration of `data/merge_yaml/merged/`.

## Validation

All focused structural validators passed on the generated YAML:

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halobacteria_medium__026e52a2.yaml` | Passed |
| `python scripts/validate_strict.py data/merge_yaml/merged/halobacteria_medium__026e52a2.yaml --out /private/tmp/halobacteria_medium__026e52a2.strict.tsv --workers 1 --quiet` | Passed, 0 error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/halobacteria_medium__026e52a2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/halobacteria_medium__026e52a2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |

Embedded `MediaRecipe.curation_history` was not checked: the repository's
`just validate-history` target validates standalone files under `history/`,
not embedded curation events in generated media YAML.

## Identity and Grounding

The record denotes the correct DSMZ/Togo recipe: Togo M2369 is
`Halobacteria Medium` and links to DSMZ_Medium372.pdf, which names
`372. HALOBACTERIA MEDIUM`. The solid state is supported by the 20 g agar row.

Most primary ingredient groundings match the DSMZ formula. One stale secondary
grounding remains: `MgSO4 x 7 H2O` has `term: CHEBI:31795`, magnesium sulfate
heptahydrate, but its `mediaingredientmech_chebi_term` is still
`CHEBI:32599`, generic magnesium sulfate.

## Evidence

Supported by inspected DSMZ, MediaDive, and Togo sources:

- DSMZ Medium 372 is `HALOBACTERIA MEDIUM`.
- The medium uses 5 g yeast extract, 5 g casamino acids, 1 g Na-glutamate,
  2 g KCl, 3 g Na3-citrate, 20 g `MgSO4 x 7 H2O`, 200 g NaCl, 20 g agar, and
  distilled water to 1000 ml.
- `FeCl2 x 4 H2O` is 36 mg, which is 0.036 g/L in a 1 L final medium.
- `MnCl2 x 4 H2O` is 0.36 mg, which is 0.00036 g/L in a 1 L final medium.
- The pH range is 7.0 to 7.2.
- DSMZ carries a strain-specific soluble-starch instruction for DSM 102807,
  DSM 102808, and DSM 102809.

Unsupported or incomplete claims:

- The generated `FeCl2 x 4 H2O` row says 36 g/L rather than 0.036 g/L.
- The generated `MnCl2 x 4 H2O` row says 0.36 g/L rather than 0.00036 g/L.
- Distilled water is recorded as 1000 g/L even though the source says to add
  water to a final volume of 1000 ml.
- The generated Togo record omits the pH range and the final-volume/pH
  preparation steps that Togo exposes from the DSMZ recipe.
- The Fisher BioReagents BP1422 qualifier on yeast extract is absent.
- The DSMZ soluble-starch instruction is not represented as variants or as an
  explicit unresolved strain-scoped note.

## Completeness

- The record has no `target_organisms` or `growth_metrics`; no organism-growth
  claims are asserted or missing evidence.
- Source identity is recoverable through `media_term` and `notes`, but there
  are no first-class `sources` entries for Togo M2369 or DSMZ Medium 372.
- An exact `rg --no-ignore --hidden` search over `data/merge_yaml` and
  `data/normalized_yaml` for `TOGO:M2369`, `DSMZ_Medium372`, `DSMZ Medium: 372`,
  and the source label found the reviewed Togo parent plus independent direct
  DSMZ/MediaDive and KOMODO records for the same DSMZ Medium 372 recipe.

## Findings

### Blocker

None found.

### Major

1. Two milligram salts were imported as g/L values with their raw milligram
   numbers. The generated record overstates `FeCl2 x 4 H2O` and
   `MnCl2 x 4 H2O` by 1000-fold relative to DSMZ, MediaDive, and Togo. Owner:
   `data/normalized_yaml/archaea/TOGO_M2369_Halobacteria_Medium.yaml` or the
   Togo unit-conversion path.

2. The final-water representation is wrong. DSMZ and Togo specify a final
   volume of 1000 ml, but the generated row says `1000 G_PER_L`. Owner: the
   Togo normalized parent or importer.

3. pH and preparation evidence was dropped. Togo exposes pH 7.0 to 7.2 and
   final-volume/pH preparation comments, but the generated record has no
   `ph_range` or `preparation_steps`. Owner: the Togo normalized parent or
   importer.

4. The reviewed Togo record is split from the already-correct direct
   DSMZ/MediaDive and KOMODO 372 imports. Those parents already contain the
   correct 0.036 and 0.00036 g/L conversions and should reconcile with Togo
   M2369 after the Togo unit bugs are repaired. Owner: Togo M2369 plus the
   duplicate/merge rules.

5. DSMZ's strain-specific 20 g/L soluble-starch instruction is absent. Owner:
   the normalized DSMZ, KOMODO, and Togo 372 parents or a maintained
   strain-variant overlay.

### Minor

1. `MgSO4 x 7 H2O` still has a stale generic
   `mediaingredientmech_chebi_term`, despite the primary `term` being
   heptahydrate-specific. Owner: the normalized parent ingredient grounding.

2. The DSMZ yeast-extract product qualifier `Fisher BioReagents BP1422` is
   absent from the Togo import. Owner: the Togo normalized parent or importer.

3. First-class `sources` are absent; the Togo and DSMZ source identifiers are
   stored only in `media_term` and `notes`. Owner: the normalized parent or
   importer.

## Recommended Edits

1. Convert `FeCl2 x 4 H2O` from 36 mg to 0.036 g/L and `MnCl2 x 4 H2O` from
   0.36 mg to 0.00036 g/L in the Togo M2369 parent.
2. Replace `Distilled water: 1000 G_PER_L` with a final-volume representation
   of 1000 ml.
3. Add the pH 7.0 to 7.2 range and the DSMZ/Togo final-volume and pH-adjustment
   preparation steps.
4. Model the soluble-starch instruction for DSM 102807, DSM 102808, and
   DSM 102809 as explicit strain-scoped variants or as a concrete unresolved
   discussion.
5. Refresh the `MgSO4 x 7 H2O` secondary grounding so it matches
   `CHEBI:31795`, and preserve the yeast-extract `Fisher BioReagents BP1422`
   qualifier if the importer supports product attributes.
6. Merge or link Togo M2369 with the direct DSMZ/KOMODO Medium 372 records once
   ingredient amounts and pH/preparation fields are reconciled.
7. Regenerate merge products after the normalized inputs or merge rules are
   fixed.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the edited Togo
  M2369 parent.
- Fetch Togo M2369, MediaDive 372, and DSMZ_Medium372.pdf again and compare
  trace-salt units, pH, final volume, and the soluble-starch instruction.
- Re-run merge freshness checks and an ignored-file-inclusive exact search for
  `TOGO:M2369` and `mediadive.medium:372` to confirm the repaired Togo import
  no longer remains as a separate erroneous canonical record.

## Additional Notes

None found.
