# YAML Record Review: haloarchaeal_complex_medium_ph_9_0

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0__3032741c.yaml
- Started UTC: 2026-09-23T09:31:51Z
- Finished UTC: 2026-09-23T09:32:32Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002420 |
| Name | haloarchaeal_complex_medium_ph_9_0 |
| Original name | HALOARCHAEAL COMPLEX MEDIUM PH 9.0 |
| Category | archaea |
| Generated path | data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0__3032741c.yaml |
| Maintained parent | data/normalized_yaml/archaea/haloarchaeal_complex_medium_ph_9_0.yaml |
| Merge fingerprint | 3032741c3b8f8c77077c738e3dde9938fedde0c43fe4bef36fa1f301f62d1f7d |

This is the generated August 2026 merge product for MediaDive/JCM medium `J1254`.
Future edits belong in `data/normalized_yaml/archaea/haloarchaeal_complex_medium_ph_9_0.yaml`
or in source-equivalence merge logic; generated YAML should be regenerated
afterward.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0__3032741c.yaml` | Passed |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0__3032741c.yaml --out /private/tmp/haloarchaeal_complex_medium_ph_9_0_3032741c.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0__3032741c.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0__3032741c.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | The repository's documented `just validate-history` check validates standalone files under `history/`; this generated MediaRecipe carries only embedded `curation_history` |

`just` validators were not used because this project currently resolves `llvmlite==0.46.0`
under Python 3.13 and fails inside setuptools before the record can be validated.

## Identity and Grounding

- `media_term` is correctly grounded to `mediadive.medium:J1254` labeled
  `HALOARCHAEAL COMPLEX MEDIUM PH 9.0`.
- MediaDive `J1254` reports source `JCM` and links to JCM `GRMD=1254`.
- The live JCM `GRMD=1254` page identifies medium 1254 as `HALOARCHAEAL COMPLEX
  MEDIUM PH 9.0`; Togo M1349 is a source-equivalent projection of the same JCM
  liquid recipe.
- Togo M1350/JCM `JCM_M1254-2` is the solid-medium form with 20 g/L agar added.
  It should remain a related solid variant, not be collapsed into the liquid
  J1254 record.
- The `CaCl2 x H2O` ingredient label is supported by JCM 1254 and MediaDive
  J1254, but the row is grounded to anhydrous calcium chloride rather than an
  exact calcium chloride monohydrate term.

## Evidence

Supported by inspected sources:

- JCM `GRMD=1254` and MediaDive `J1254` support the JCM identity, liquid state,
  pH 9.0, 16 dry ingredients, and the post-autoclave pH adjustment with
  autoclaved 10% w/v Na2CO3 solution.
- JCM and MediaDive support the instruction to dissolve the components in
  distilled water, bring volume to 1.0 L, add 20 g/L agar only when preparing
  solid medium, and autoclave before adding the pH-adjustment Na2CO3 solution.
- Togo M1349 supports a liquid source-equivalent projection of the JCM M1254
  formulation.
- Togo M1350 and the JCM optional-agar note support a sibling solid recipe with
  20 g/L agar.

Unsupported or incomplete in this generated record:

- The `CaCl2 x H2O` row is grounded to anhydrous `CHEBI:3312`.
- `Fish peptone` has lost the source qualifier `(Fluka)` in this generated
  output; JCM, MediaDive, and Togo all carry the Fluka qualifier.
- `NaNO3` still carries `mediaingredientmech_term: MediaIngredientMech:000171`
  despite the 2026-06-05 migration away from legacy MediaIngredientMech IDs.
- The 10% w/v Na2CO3 solution appears only in prose, so its concentration is not
  available as a structured pH-adjustment reagent.
- The source URL appears only in `notes`, so the reference validator could not
  inspect the JCM source.
- The direct JCM record is split from Togo M1349 even though both point to the
  same JCM `GRMD=1254` liquid formula.

## Completeness

- The target includes pH 9.0 and the JCM preparation note that distilled water
  is added to a 1 L final volume.
- Unlike the Togo M1349 projection, the direct JCM record correctly omits water
  as a quantified `1 G_PER_L` ingredient.
- The target is complete enough to capture the Na2CO3 adjustment in prose but
  not complete enough for structured queries that need the Na2CO3 stock strength
  or post-autoclave addition.
- An exact `rg --no-ignore --hidden` search for
  `JCM_M1254\b|GRMD=1254\b|TOGO:M1349\b|mediadive\.medium:J1254\b` across
  `data/merge_yaml` and `data/normalized_yaml` found this direct MediaDive/JCM
  record, the liquid Togo M1349 record, and the solid Togo M1350/JCM_M1254-2
  variant.
- Empty organism-specific growth slots are acceptable; this source recipe does
  not assert a narrow strain growth observation.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The calcium chloride monohydrate row is grounded to anhydrous calcium chloride. | JCM and MediaDive identify the ingredient as `CaCl2 x H2O`; the YAML grounds it to `CHEBI:3312` calcium dichloride. | Ground `data/normalized_yaml/archaea/haloarchaeal_complex_medium_ph_9_0.yaml` to the exact calcium chloride monohydrate CHEBI term if available; otherwise remove the near-miss anhydrous grounding. |
| Major | Togo M1349 and MediaDive/JCM J1254 remain split into separate generated records. | Togo M1349 has `original_media_id: JCM_M1254` and JCM `GRMD=1254`; MediaDive `J1254` links to the same JCM page and has the same liquid ingredient list. | After repairing the Togo M1349 water and pH fields, add a source-equivalence or merge-key repair so Togo M1349 and MediaDive/JCM J1254 collapse into one generated liquid recipe. |
| Minor | The fish peptone source qualifier was dropped. | JCM, MediaDive, and Togo all specify Fish peptone with the Fluka qualifier, while the generated direct JCM row says only `Fish peptone`. | Restore `Fish peptone (Fluka)` in the maintained direct JCM parent. |
| Minor | The `NaNO3` row still has a legacy `mediaingredientmech_term`. | The generated row has the correct `term: CHEBI:63005` but still includes `mediaingredientmech_term: MediaIngredientMech:000171` after a curation event that claims legacy MediaIngredientMech IDs were replaced. | Remove the stale legacy MIM slot from the maintained parent. |
| Minor | The JCM source is not in structured `references`. | The URL appears only in free text under `notes`, so the reference validator ran 0 checks. | Add a structured JCM `GRMD=1254` reference to the maintained parent. |

## Recommended Edits

1. Correct the calcium chloride monohydrate grounding to an exact hydrated term
   or leave it explicitly ungrounded.
2. Restore the `Fish peptone (Fluka)` qualifier in
   `data/normalized_yaml/archaea/haloarchaeal_complex_medium_ph_9_0.yaml`.
3. Remove the stale `mediaingredientmech_term` from the `NaNO3` row.
4. Add a structured JCM `GRMD=1254` reference to the maintained parent.
5. Optionally model the post-autoclave 10% w/v Na2CO3 solution as a structured
   pH-adjustment reagent while preserving the source wording in
   `preparation_steps`.
6. After the Togo M1349 parent is repaired, add a source-identity merge rule or
   equivalence overlay for Togo M1349 and MediaDive/JCM J1254 while keeping the
   agar-containing Togo M1350 as the solid variant.
7. Regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated
  `haloarchaeal_complex_medium_ph_9_0` output.
- Inspect the regenerated liquid YAML and confirm it has a corrected calcium
  chloride monohydrate row, `Fish peptone (Fluka)`, no legacy
  `mediaingredientmech_term`, a structured JCM reference, no 20 g/L agar row,
  and pH 9.0.
- Search `data/merge_yaml/merged` for exact `JCM_M1254`, `mediadive.medium:J1254`,
  and Togo `M1349` tokens with `rg --no-ignore --hidden`; after equivalence
  repair they should identify one merged liquid source recipe group.
- Re-fetch Togo M1349, Togo M1350, JCM `GRMD=1254`, and MediaDive `J1254` to
  confirm the regenerated liquid and solid records still match the live source
  records.

## Additional Notes

- The live JCM `GRMD=1254` page was reachable and agreed with MediaDive `J1254`.
- The direct JCM record's bring-to-1-L preparation note is a sound way to carry
  the final water volume without a synthetic 1 g/L water ingredient.
