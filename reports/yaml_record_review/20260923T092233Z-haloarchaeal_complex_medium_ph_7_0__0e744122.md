# YAML Record Review: haloarchaeal_complex_medium_ph_7_0

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0__0e744122.yaml
- Started UTC: 2026-09-23T09:21:52Z
- Finished UTC: 2026-09-23T09:22:33Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002418 |
| Name | haloarchaeal_complex_medium_ph_7_0 |
| Original name | HALOARCHAEAL COMPLEX MEDIUM PH 7.0 |
| Category | archaea |
| Generated path | data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0__0e744122.yaml |
| Maintained parent | data/normalized_yaml/archaea/haloarchaeal_complex_medium_ph_7_0.yaml |
| Merge fingerprint | 0e7441227a470a460532d48129f7bac59c048d2bced7532a7f142deffdd020dd |

This is the generated August 2026 merge product for MediaDive/JCM medium `J1252`.
Future edits belong in `data/normalized_yaml/archaea/haloarchaeal_complex_medium_ph_7_0.yaml`
or in the source-equivalence merge logic, then `data/merge_yaml/merged/` should
be regenerated.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0__0e744122.yaml` | Passed |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0__0e744122.yaml --out /private/tmp/haloarchaeal_complex_medium_ph_7_0_0e744122.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0__0e744122.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0__0e744122.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | The repository's documented `just validate-history` check validates standalone files under `history/`; this generated MediaRecipe carries only embedded `curation_history` |

`just` validators were not used because this project currently resolves `llvmlite==0.46.0`
under Python 3.13 and fails inside setuptools before the record can be validated.

## Identity and Grounding

- `media_term` is correctly grounded to `mediadive.medium:J1252` labeled
  `HALOARCHAEAL COMPLEX MEDIUM PH 7.0`.
- MediaDive `J1252` reports source `JCM` and links to JCM `GRMD=1252`.
- The live JCM `GRMD=1252` page identifies medium 1252 as `HALOARCHAEAL COMPLEX
  MEDIUM PH 7.0`; Togo M1346 is a source-equivalent projection of the same JCM
  liquid recipe.
- Togo M1347/JCM `JCM_M1252-2` is the solid-medium form with 20 g/L agar added.
  It should remain a related solid variant, not be collapsed into the liquid
  J1252 record.
- The `CaCl2 x H2O` row is wrongly identified. The live JCM page lists
  `CaCl2 x 2 H2O`, while this record says `CaCl2 x H2O` and grounds the row to
  anhydrous calcium chloride.

## Evidence

Supported by inspected sources:

- JCM `GRMD=1252` and MediaDive `J1252` support the JCM identity, liquid state,
  pH 7.0, and all dry-ingredient amounts other than the calcium hydrate string.
- JCM and MediaDive support the instruction to dissolve the components in
  distilled water, bring volume to 1.0 L, adjust pH to 7.0, and add 20 g/L agar
  only when preparing solid medium.
- Togo M1346 supports a liquid source-equivalent projection of the JCM M1252
  formulation.
- Togo M1347 and the JCM optional-agar note support a sibling solid recipe with
  20 g/L agar.

Unsupported or incomplete in this generated record:

- The calcium chloride row uses the MediaDive `CaCl2 x H2O` spelling and an
  anhydrous CHEBI grounding, while the live JCM page lists `CaCl2 x 2 H2O`.
- `Fish peptone` has lost the source qualifier `(Fluka)` in this generated
  output; JCM, MediaDive, and Togo all carry the Fluka qualifier.
- The direct JCM record is split from Togo M1346 even though both point to the
  same JCM `GRMD=1252` liquid formula.
- The source URL appears only in `notes`, so the reference validator could not
  inspect the JCM source.

## Completeness

- The target includes pH 7.0 and the JCM preparation note that distilled water
  is added to a 1 L final volume.
- Unlike the Togo M1346 projection, the direct JCM record correctly omits water
  as a quantified `1 G_PER_L` ingredient.
- An exact `rg --no-ignore --hidden` search for
  `JCM_M1252\b|GRMD=1252\b|TOGO:M1346\b|mediadive\.medium:J1252\b` across
  `data/merge_yaml` and `data/normalized_yaml` found this direct MediaDive/JCM
  record, the liquid Togo M1346 record, and the solid Togo M1347/JCM_M1252-2
  variant.
- The complex `Yeast extract` and source-qualified fish peptone ingredients are
  correctly left ungrounded.
- Empty organism-specific growth slots are acceptable; this source recipe does
  not assert a narrow strain growth observation.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Calcium chloride has the wrong hydration and CHEBI grounding. | JCM `GRMD=1252` lists `CaCl2 x 2 H2O`; the record says `CaCl2 x H2O` and grounds the row to anhydrous `CHEBI:3312`. | Correct `data/normalized_yaml/archaea/haloarchaeal_complex_medium_ph_7_0.yaml` to the JCM calcium salt and ground it to the exact CHEBI hydrated form if available; otherwise remove the near-miss anhydrous grounding. |
| Major | Togo M1346 and MediaDive/JCM J1252 remain split into separate generated records. | Togo M1346 has `original_media_id: JCM_M1252` and JCM `GRMD=1252`; MediaDive `J1252` links to the same JCM page and has the same liquid ingredient list. | After repairing the Togo M1346 water and pH fields, add a source-equivalence or merge-key repair so Togo M1346 and MediaDive/JCM J1252 collapse into one generated liquid recipe. |
| Minor | The fish peptone source qualifier was dropped. | JCM, MediaDive, and Togo all specify Fish peptone with the Fluka qualifier, while the generated direct JCM row says only `Fish peptone`. | Restore `Fish peptone (Fluka)` in the maintained direct JCM parent. |
| Minor | The JCM source is not in structured `references`. | The URL appears only in free text under `notes`, so the reference validator ran 0 checks. | Add a structured JCM `GRMD=1252` reference to the maintained parent. |

## Recommended Edits

1. Recheck the calcium chloride hydrate against JCM `GRMD=1252`; correct the
   preferred term and CHEBI grounding to the dihydrate when an exact term exists
   or leave it explicitly ungrounded.
2. Restore the `Fish peptone (Fluka)` qualifier in
   `data/normalized_yaml/archaea/haloarchaeal_complex_medium_ph_7_0.yaml`.
3. Add a structured JCM `GRMD=1252` reference to the maintained parent so the
   reference validator can inspect the source URL.
4. After the Togo M1346 parent is repaired, add a source-identity merge rule or
   equivalence overlay for Togo M1346 and MediaDive/JCM J1252 while keeping the
   agar-containing Togo M1347 as the solid variant.
5. Regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated
  `haloarchaeal_complex_medium_ph_7_0` output.
- Inspect the regenerated liquid YAML and confirm it has a corrected calcium
  chloride hydrate row, `Fish peptone (Fluka)`, a structured JCM reference, no
  20 g/L agar row, and pH 7.0.
- Search `data/merge_yaml/merged` for exact `JCM_M1252`, `mediadive.medium:J1252`,
  and Togo `M1346` tokens with `rg --no-ignore --hidden`; after equivalence
  repair they should identify one merged liquid source recipe group.
- Re-fetch Togo M1346, Togo M1347, JCM `GRMD=1252`, and MediaDive `J1252` to
  confirm the regenerated liquid and solid records still match the live source
  records.

## Additional Notes

- The live JCM `GRMD=1252` page was reachable and generally agreed with
  MediaDive `J1252`, except for the calcium chloride hydrate string.
- The direct JCM record's bring-to-1-L preparation note is a sound way to carry
  the final water volume without a synthetic 1 g/L water ingredient.
