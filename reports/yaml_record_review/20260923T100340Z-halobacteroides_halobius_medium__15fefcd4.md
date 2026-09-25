# YAML Record Review: Halobacteroides Halobius Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/halobacteroides_halobius_medium__15fefcd4.yaml
- Started UTC: 2026-09-23T10:02:22Z
- Finished UTC: 2026-09-23T10:03:40Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/halobacteroides_halobius_medium__15fefcd4.yaml`,
a generated `MediaRecipe` with `id: CultureMech:009291`, `category: bacterial`,
`physical_state: LIQUID`, and `media_term.term.id: TOGO:M2740`.

The generated record is a single-source merge from the maintained Togo parent
`data/normalized_yaml/bacterial/TOGO_M2740_Halobacteroides_Halobius_Medium.yaml`,
which cites DSMZ Medium 588. Future fixes belong in that normalized parent or
in the Togo importer, then require regeneration of `data/merge_yaml/merged/`.

## Validation

All focused structural validators passed on the generated YAML:

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halobacteroides_halobius_medium__15fefcd4.yaml` | Passed |
| `python scripts/validate_strict.py data/merge_yaml/merged/halobacteroides_halobius_medium__15fefcd4.yaml --out /private/tmp/halobacteroides_halobius_medium__15fefcd4.strict.tsv --workers 1 --quiet` | Passed, 0 error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/halobacteroides_halobius_medium__15fefcd4.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/halobacteroides_halobius_medium__15fefcd4.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |

Embedded `MediaRecipe.curation_history` was not checked: the repository's
`just validate-history` target validates standalone files under `history/`,
not embedded curation events in generated media YAML.

## Identity and Grounding

The source identity is correct. Togo M2740 is
`Halobacteroides Halobius Medium` and cites DSMZ_Medium588.pdf, which names
`588. HALOBACTEROIDES HALOBIUS MEDIUM`. The liquid physical state is
source-supported because no solidifying agent is listed.

Ingredient groundings for the salts, resazurin, PIPES, glucose, and
cysteine-HCl hydrate are appropriately specific. The `N2` row is not a medium
ingredient; DSMZ uses nitrogen as the anaerobic atmosphere for preparing the
salts, glucose, and PIPES separately.

## Evidence

Supported by inspected DSMZ, MediaDive, and Togo sources:

- DSMZ Medium 588 contains 87.8 g NaCl, 20.3 g `MgCl2 x 6 H2O`, 7.35 g
  `CaCl2 x 2 H2O`, 3.7 g KCl, 5 g yeast extract, 0.5 g
  `Cysteine-HCl x H2O`, 0.0001 g resazurin, 5 g glucose, 12.096 g PIPES, and
  1000 ml distilled water.
- The pH is 6.5.
- Salts in 850 ml water, glucose as 50 ml of a 10% solution, and PIPES as
  100 ml of 400 mM solution are prepared separately under nitrogen using normal
  anaerobic techniques.
- Glucose and PIPES are added using anaerobic techniques.

Unsupported or incomplete claims:

- Distilled water is recorded as `1000 G_PER_L` even though the source says
  1000 ml.
- `N2` is represented as a variable-concentration ingredient even though the
  source only uses nitrogen as a preparation atmosphere.
- The generated record omits pH 6.5 and the preparation instructions for
  separate salt, glucose, and PIPES solutions under nitrogen.

## Completeness

- The record has no `target_organisms` or `growth_metrics`; no organism-growth
  claims are asserted or missing evidence.
- Source identity is recoverable through `media_term` and `notes`, but there
  are no first-class `sources` entries for Togo M2740 or DSMZ Medium 588.
- An exact `rg --no-ignore --hidden` search over `data/merge_yaml` and
  `data/normalized_yaml` for `TOGO:M2740`, `DSMZ_Medium588`,
  `DSMZ Medium: 588`, and the source label found the reviewed Togo parent plus
  independent direct DSMZ/MediaDive and KOMODO records for the same DSMZ
  Medium 588 recipe.

## Findings

### Blocker

None found.

### Major

1. Nitrogen gas was imported as a medium ingredient. DSMZ/Togo use N2 as the
   atmosphere for anaerobic preparation, not as a variable medium component.
   Owner:
   `data/normalized_yaml/bacterial/TOGO_M2740_Halobacteroides_Halobius_Medium.yaml`
   or the Togo gas importer.

2. The generated record lost all anaerobic preparation structure. It needs to
   preserve pH 6.5 and the separate salt, glucose, and PIPES preparations under
   nitrogen, including anaerobic addition of glucose and PIPES. Owner: the Togo
   normalized parent or importer.

3. The final-water representation is wrong. DSMZ and Togo specify 1000 ml
   distilled water, but the generated record stores `1000 G_PER_L`. Owner: the
   Togo normalized parent or importer.

4. The reviewed Togo record is split from the direct DSMZ/MediaDive and KOMODO
   Medium 588 records. After N2 and water are repaired, Togo M2740 should
   reconcile with the direct DSMZ import. Owner: Togo M2740 plus the
   duplicate/merge rules.

### Minor

1. First-class `sources` are absent; the Togo and DSMZ source identifiers are
   stored only in `media_term` and `notes`. Owner: the normalized parent or
   importer.

## Recommended Edits

1. Remove the `N2` ingredient row and represent nitrogen as an anaerobic
   atmosphere/preparation condition.
2. Add pH 6.5 and the source preparation text describing 850 ml salts, 50 ml
   10% glucose, 100 ml 400 mM PIPES, and anaerobic addition.
3. Replace `Distilled water: 1000 G_PER_L` with 1000 ml distilled water or a
   structured final-volume representation.
4. Add first-class Togo/DSMZ sources if the importer supports them.
5. Merge or link Togo M2740 with the direct DSMZ/KOMODO Medium 588 records once
   the N2 and water defects are corrected.
6. Regenerate merge products after repairing the Togo parent or importer.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the edited Togo
  M2740 parent.
- Fetch Togo M2740, MediaDive 588, and DSMZ_Medium588.pdf again and compare
  pH, water volume, nitrogen atmosphere, and anaerobic preparation wording.
- Re-run merge freshness checks and an ignored-file-inclusive exact search for
  `TOGO:M2740`, `mediadive.medium:588`, and `komodo.medium:588` to confirm the
  repaired Togo import no longer remains as a separate erroneous canonical
  record.

## Additional Notes

The KOMODO 588 parent also carries `Aerobic: Yes` in free-text notes despite
copying a DSMZ recipe that requires anaerobic technique; fix that separate
KOMODO provenance bug when reviewing the direct/KOMODO merged record.
