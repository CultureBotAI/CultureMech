# YAML Record Review: Halobacteria MH4.2 Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/halobacteria_mh4_2_medium__0874ae5b.yaml
- Started UTC: 2026-09-23T09:51:53Z
- Finished UTC: 2026-09-23T09:52:22Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/halobacteria_mh4_2_medium__0874ae5b.yaml`, a
generated `MediaRecipe` with `id: CultureMech:007652`, `category: archaea`,
`physical_state: SOLID_AGAR`, and `media_term.term.id: TOGO:M1130`.

The generated record is a single-source merge from the maintained Togo parent
`data/normalized_yaml/archaea/TOGO_M1130_Halobacteria_MH4.2_Medium.yaml`, which
imports the solid `JCM_M1061-2` form of JCM GRMD 1061. Future fixes belong in
that normalized parent or in the Togo solution/unit importer, then require
regeneration of `data/merge_yaml/merged/`.

## Validation

All focused structural validators passed on the generated YAML:

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halobacteria_mh4_2_medium__0874ae5b.yaml` | Passed |
| `python scripts/validate_strict.py data/merge_yaml/merged/halobacteria_mh4_2_medium__0874ae5b.yaml --out /private/tmp/halobacteria_mh4_2_medium__0874ae5b.strict.tsv --workers 1 --quiet` | Passed, 0 error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/halobacteria_mh4_2_medium__0874ae5b.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/halobacteria_mh4_2_medium__0874ae5b.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |

Embedded `MediaRecipe.curation_history` was not checked: the repository's
`just validate-history` target validates standalone files under `history/`,
not embedded curation events in generated media YAML.

## Identity and Grounding

The source identity is correct. Togo M1130 names `Halobacteria MH4.2 Medium`,
identifies its original medium as `JCM_M1061-2`, and points to JCM GRMD 1061.
The solid physical state is supported because M1130 includes the JCM solid
variant's 20 g agar addition.

Most simple-salt groundings are exact. `Trisodium citrate x 2 H2O` is grounded
only to generic sodium citrate, so a curator should either verify an exact
dihydrate mapping or leave the hydrated formula ungrounded.

## Evidence

Supported by inspected JCM, Togo, and MediaDive sources:

- JCM 1061 is `HALOBACTERIA MH4.2 MEDIUM`.
- M1130 contains sodium pyruvate, trisodium citrate dihydrate, BD-Difco yeast
  extract, BD-Difco tryptone, K2HPO4, NH4Cl, NaCl, `MgSO4 x 7 H2O`, K2SO4,
  `FeCl2 x 4 H2O`, `MnCl2 x 4 H2O`, 100 ml of 0.5 M Tris-HCl pH 8.0,
  1 ml of SL-6 trace-element solution from Togo M158, and 20 g agar.
- Togo and JCM both instruct bringing the medium to 1.0 L.

Unsupported or incomplete claims:

- The generated `FeCl2 x 4 H2O` row says 36 g/L, but JCM and Togo say 36 mg.
- The generated `MnCl2 x 4 H2O` row says 0.36 g/L, but JCM and Togo say
  0.36 mg.
- Distilled water is recorded as `1 G_PER_L` even though Togo records 1 L and
  JCM uses enough distilled water to bring the recipe to 1.0 L.
- The generated solutions for 0.5 M Tris-HCl and SL-6 have empty composition,
  default name `Unknown solution`, and imported concentrations of `100 G_PER_L`
  and `1 G_PER_L`; those source rows are volume additions of 100 ml and 1 ml.
- The SL-6 row no longer resolves to the Togo M158 stock solution.
- The bring-to-1-L and solid-agar preparation instruction is absent.

## Completeness

- The record has no `target_organisms` or `growth_metrics`; no organism-growth
  claims are asserted or missing evidence.
- Source identity is recoverable through `media_term` and `notes`, but there
  are no first-class `sources` entries for Togo M1130 or JCM GRMD 1061.
- An exact `rg --no-ignore --hidden` search over `data/merge_yaml` and
  `data/normalized_yaml` for `TOGO:M1130`, `JCM_M1061-2`, the JCM GRMD 1061
  URL, and the source label found the reviewed M1130 solid parent, the M1129
  liquid sibling, and the direct JCM/MediaDive J1061 import.

## Findings

### Blocker

None found.

### Major

1. Milligram trace salts were imported as g/L values with their milligram
   numbers preserved. `FeCl2 x 4 H2O` and `MnCl2 x 4 H2O` are 1000-fold too
   high. Owner:
   `data/normalized_yaml/archaea/TOGO_M1130_Halobacteria_MH4.2_Medium.yaml` or
   the Togo unit-conversion path.

2. Volume-based solution additions were corrupted into empty g/L solution
   stubs. The source adds 100 ml 0.5 M Tris-HCl pH 8.0 and 1 ml SL-6
   trace-element solution, but the generated record has two `Unknown solution`
   entries with empty `composition` and `G_PER_L` units. Owner: the Togo parent
   or `solution-migrator-v1.0`.

3. The SL-6 trace stock reference is not resolvable. Togo M1130 explicitly
   points to Medium M158, but the generated solution keeps only free-text
   notes. Owner: the Togo M1130 solution reference and the Togo M158 stock
   record under `data/normalized_yaml/bacterial/togo_medium_m158.yaml`.

4. The final water and preparation representation is incomplete. The source
   instructs adding components to distilled water and bringing the recipe to
   1.0 L; the generated record instead stores `Distilled water: 1 G_PER_L` and
   has no `preparation_steps`. Owner: the Togo parent or importer.

5. The M1130 solid recipe and M1129 liquid recipe are split without an explicit
   variant relation. M1129 is the same JCM page's liquid variant without agar.
   Owner: normalized variant metadata for M1129 and M1130.

### Minor

1. `Trisodium citrate x 2 H2O` is grounded to generic sodium citrate. Owner:
   the normalized ingredient grounding and the packaged MediaIngredientMech
   label index.

2. First-class `sources` are absent; the Togo and JCM source identifiers are
   stored only in `media_term` and `notes`. Owner: the normalized parent or
   importer.

## Recommended Edits

1. Convert `FeCl2 x 4 H2O` to 0.036 g/L and `MnCl2 x 4 H2O` to 0.00036 g/L.
2. Restore the 100 ml Tris-HCl and 1 ml SL-6 additions as volume additions,
   preserving Tris-HCl's 0.5 M, pH 8.0 qualifier.
3. Replace the free-text SL-6 stub with a resolvable link to the maintained
   Togo M158 SL-6 trace-element stock.
4. Replace `Distilled water: 1 G_PER_L` with a final-volume representation and
   restore the bring-to-1-L preparation text with the 20 g agar instruction.
5. Add a liquid/solid variant relationship between M1129 and M1130.
6. Recheck the trisodium citrate dihydrate grounding against the packaged MIM
   label index and OAK.
7. Regenerate the generated merge YAML after repairing the Togo normalized
   parent or importer.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the edited M1130,
  M1129, and M158 normalized records.
- Fetch Togo M1130, Togo M1129, Togo M158, JCM GRMD 1061, and JCM GRMD 167
  again to verify the two MH4.2 variants and the SL-6 stock boundary.
- Run solution-reference validation after replacing the free-text M158 note
  with a resolvable stock-solution reference.
- Run `just validate-media-variant-links` after adding the M1130/M1129 variant
  edge.

## Additional Notes

The separate direct MediaDive/JCM J1061 generated record is stale in a different
way: it scales main ingredients by a 101 ml volume, flattens SL-6 stock
components into the main medium, and leaves the SL-6 pH 3.6 step as a
final-medium preparation step. Use it only as a source-identity lead.
