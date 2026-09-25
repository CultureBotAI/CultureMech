# YAML Record Review: Halobacteria HMD Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/halobacteria_hmd_medium__9679a774.yaml
- Started UTC: 2026-09-23T09:43:23Z
- Finished UTC: 2026-09-23T09:44:46Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/halobacteria_hmd_medium__9679a774.yaml`, a
generated `MediaRecipe` with `id: CultureMech:010338`, `category: archaea`,
`physical_state: SOLID_AGAR`, and `media_term.term.id: TOGO:M918`.

The generated record is a single-source merge from the maintained Togo parent
`data/normalized_yaml/archaea/TOGO_M918_Halobacteria_HMD_Medium.yaml`, which
imports the solid HMD variant `JCM_M878-2` from Togo Medium M918 and cites JCM
GRMD 878 as the original source. Future fixes belong in that normalized parent
or in the Togo importer, then require regeneration of `data/merge_yaml/merged/`.

## Validation

All focused structural validators passed on the generated YAML:

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halobacteria_hmd_medium__9679a774.yaml` | Passed |
| `python scripts/validate_strict.py data/merge_yaml/merged/halobacteria_hmd_medium__9679a774.yaml --out /private/tmp/halobacteria_hmd_medium__9679a774.strict.tsv --workers 1 --quiet` | Passed, 0 error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/halobacteria_hmd_medium__9679a774.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/halobacteria_hmd_medium__9679a774.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |

Embedded `MediaRecipe.curation_history` was not checked: the repository's
`just validate-history` target validates standalone files under `history/`,
not embedded curation events in generated media YAML.

## Identity and Grounding

The record identifies the solid variant of JCM 878 correctly. Togo M918 is
`Halobacteria HMD Medium`, points back to `JCM_M878-2`, and carries the same JCM
GRMD 878 URL as the original source. The 18 g/L agar ingredient makes
`physical_state: SOLID_AGAR` appropriate for this variant.

Most inorganic salts are grounded to appropriate ChEBI terms. The exception is
`K2SO4 x 7 H2O`: the source and Togo both say a heptahydrate, but the record is
grounded to `CHEBI:32036`, `potassium sulfate`.

## Evidence

Supported by inspected JCM, Togo, and MediaDive sources:

- JCM GRMD 878 is `HALOBACTERIA HMD MEDIUM`.
- Togo M918 represents the solid `JCM_M878-2` variant.
- The recipe contains 20 g `MgCl2 x 6 H2O`, 5 g `K2SO4 x 7 H2O`, 0.1 g
  `CaCl2 x 2 H2O`, 0.1 g NH4Cl, 0.05 g KH2PO4, 0.1 g Yeast extract
  (BD-Difco), 0.5 g Casamino acids (BD-Difco), 180 g NaCl, and 18 g/L agar.
- Components are added to distilled water and brought to 1.0 L.
- The medium is adjusted to pH 7.0 to 7.2.
- JCM applies its default autoclaving instruction unless stated otherwise.

Unsupported or incomplete claims:

- The generated distilled-water row says `1 G_PER_L`, but Togo M918 represents
  it as 1 L of distilled water.
- The generated record omits the pH 7.0 to 7.2 adjustment and the bring-to-1-L
  preparation comment that Togo exposes from JCM.
- The generated record omits the JCM default autoclaving condition.
- `K2SO4 x 7 H2O` is not supported by an anhydrous potassium sulfate grounding.

## Completeness

- The record has no `target_organisms` or `growth_metrics`; no organism-growth
  claims are asserted or missing evidence.
- Source identity is recoverable through `media_term` and `notes`, but there
  are no first-class `sources` entries for Togo M918 or JCM GRMD 878.
- An exact `rg --no-ignore --hidden` search over `data/merge_yaml` and
  `data/normalized_yaml` for `TOGO:M918`, `JCM_M878-2`, the JCM GRMD 878 URL,
  and the source label found the reviewed M918 record, the M917 liquid sibling,
  and the direct JCM/MediaDive J878 normalized parent.

## Findings

### Blocker

None found.

### Major

1. Distilled water has the wrong unit. Togo M918 states 1 L, but the generated
   record uses `value: '1'` with `unit: G_PER_L`. Owner:
   `data/normalized_yaml/archaea/TOGO_M918_Halobacteria_HMD_Medium.yaml` or the
   Togo importer.

2. Preparation and pH details from the cited source were dropped. The generated
   M918 record has no `ph_value` and no preparation steps even though JCM/Togo
   specify bring-to-1-L and pH 7.0 to 7.2 steps; the record also omits the JCM
   default autoclave condition. Owner: the Togo normalized parent or importer.

3. `K2SO4 x 7 H2O` is grounded to anhydrous potassium sulfate. Because the
   source hydrate string is explicit, the ingredient needs a verified
   hydrate-specific mapping or should be left unresolved. Owner: the
   normalized parent ingredient `term` mapping and the packaged
   MediaIngredientMech label index.

4. M918 is not linked to the corresponding liquid HMD parent. Togo M917 imports
   `JCM_M878` from the same JCM page without agar, while M918 imports the
   `JCM_M878-2` solid variant with 18 g/L agar. Owner: normalized variant
   metadata for `TOGO_M918_Halobacteria_HMD_Medium.yaml` and
   `TOGO_M917_Halobacteria_HMD_Medium.yaml`.

### Minor

1. First-class `sources` are absent; the Togo URL and JCM accession are present
   only in free-text `notes` and `media_term`. Owner: the normalized parent or
   importer.

## Recommended Edits

1. Correct the distilled-water representation to 1 L or an explicit final
   volume, not `1 G_PER_L`.
2. Copy Togo/JCM's pH 7.0 to 7.2 adjustment and bring-to-1-L preparation text
   into the normalized M918 parent, and preserve JCM's default 121 C for
   15 minutes autoclaving instruction.
3. Recheck `K2SO4 x 7 H2O` against the packaged MIM label index and OAK; remove
   `CHEBI:32036` unless a curator verifies that it is the best exact hydrate
   representation available.
4. Add a solid-variant relationship from M918 to the M917 liquid HMD medium
   after both records have correct water, pH, and preparation fields.
5. Add first-class Togo/JCM source entries if the importer supports them.
6. Regenerate `data/merge_yaml/merged/halobacteria_hmd_medium__9679a774.yaml`
   after the maintained inputs are repaired.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the edited M918 and
  M917 normalized records.
- Fetch Togo M918 and JCM GRMD 878 again and compare ingredient quantities,
  pH, agar placement, and preparation comments against the generated canonical
  record.
- Run `just validate-media-variant-links` after adding the M918/M917 solid
  variant relation.

## Additional Notes

Togo M918 has no top-level `ph` field in its API `meta` block, but it preserves
the JCM pH instruction in `comments`; the importer should not drop that comment
when `meta.ph` is absent.
