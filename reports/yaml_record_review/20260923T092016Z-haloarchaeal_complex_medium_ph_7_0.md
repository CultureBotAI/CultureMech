# YAML Record Review: haloarchaeal_complex_medium_ph_7_0

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0.yaml
- Started UTC: 2026-09-23T09:18:28Z
- Finished UTC: 2026-09-23T09:20:16Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007882 |
| Name | haloarchaeal_complex_medium_ph_7_0 |
| Original name | Haloarchaeal Complex Medium PH 7.0 |
| Category | archaea |
| Generated path | data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0.yaml |
| Maintained parent | data/normalized_yaml/archaea/TOGO_M1346_Haloarchaeal_Complex_Medium_PH_7.0.yaml |
| Merge fingerprint | e029779802cd8c24b4f7a8aa4748a5889b0d051a1cbe8296b8d33b48a22070e1 |

This is the generated August 2026 merge product for Togo Medium M1346, which
Togo imported from JCM `JCM_M1252`. Future edits belong in the Togo normalized
parent, the Togo importer, or source-equivalence merge logic; generated YAML
should be regenerated afterward.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0.yaml` | Passed |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0.yaml --out /private/tmp/haloarchaeal_complex_medium_ph_7_0.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | The repository's documented `just validate-history` check validates standalone files under `history/`; this generated MediaRecipe carries only embedded `curation_history` |

`just` validators were not used because this project currently resolves `llvmlite==0.46.0`
under Python 3.13 and fails inside setuptools before the record can be validated.

## Identity and Grounding

- The target `media_term` identifies Togo `M1346`, labeled `Haloarchaeal Complex
  Medium PH 7.0`.
- Togo M1346 metadata reports `original_media_id: JCM_M1252`, source pH `7.0`,
  and the same JCM `GRMD=1252` source URL named by this record.
- The live JCM `GRMD=1252` page identifies medium 1252 as `HALOARCHAEAL COMPLEX
  MEDIUM PH 7.0`; MediaDive `J1252` is a direct JCM import of the same liquid
  recipe.
- Togo M1347/JCM `JCM_M1252-2` is the solid-medium form with 20 g/L agar added.
  It should remain a related solid variant, not be collapsed into the liquid
  M1346 record.
- The `CaCl2 x H2O` row is under-specified and wrongly grounded. The live JCM
  page lists `CaCl2 x 2 H2O`, while this record says `CaCl2 x H2O` and grounds
  the row to anhydrous calcium chloride.

## Evidence

Supported by inspected sources:

- JCM `GRMD=1252`, MediaDive `J1252`, and Togo M1346 support the M1252 identity,
  liquid state, and most dry-ingredient amounts.
- Togo M1346 supports the 1 L distilled water item, the 26.8 g magnesium sulfate
  heptahydrate item, the 23 g magnesium chloride hexahydrate item, the 184 g
  sodium chloride item, and all 0.2 g organic-acid salt rows in a 1 L recipe.
- JCM and MediaDive support the instruction to dissolve the components in
  distilled water, bring volume to 1.0 L, and adjust pH to 7.0.
- Togo M1347 and the JCM optional-agar note support a sibling solid recipe with
  20 g/L agar, which is correctly absent from this liquid M1346 record.

Unsupported or incomplete in this generated record:

- The `Distilled water` row is imported as `1 G_PER_L`; Togo M1346 states 1 L
  water and the JCM page says to bring the formulation to 1.0 L.
- The source pH 7.0 is absent from the target record.
- The JCM/Togo preparation instruction is absent from the target record.
- Calcium chloride is represented as `CaCl2 x H2O` and grounded to anhydrous
  `CHEBI:3312`, while the live JCM page lists `CaCl2 x 2 H2O`.
- The direct MediaDive/JCM `J1252` record is split from this Togo M1346 record
  even though both point to JCM `GRMD=1252`.

## Completeness

- The target captures the high-salt liquid recipe and keeps the M1347 optional
  agar as a separate record, which is the right high-level split.
- The target is not complete enough to execute as written because the water unit
  is wrong, pH 7.0 is missing, and the dissolve/bring-to-volume preparation
  step is missing.
- The source-equivalent direct JCM record is still split from this Togo M1346
  record; an exact `rg --no-ignore --hidden` search for
  `JCM_M1252\b|GRMD=1252\b|TOGO:M1346\b|mediadive\.medium:J1252\b` across
  `data/merge_yaml` and `data/normalized_yaml` found this Togo M1346 record, the
  direct MediaDive/JCM J1252 record, and the solid Togo M1347/JCM_M1252-2
  variant.
- The complex `Yeast extract` and `Fish peptone (Fluka)` ingredients are
  correctly left ungrounded.
- Empty organism-specific growth slots are acceptable; this source recipe does
  not assert a narrow strain growth observation.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Distilled water is imported with the wrong unit. | Togo M1346 reports `Distilled water` as 1 L, while the generated YAML writes `value: '1'` and `unit: G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M1346_Haloarchaeal_Complex_Medium_PH_7.0.yaml` or the Togo import/unit-normalization transform. |
| Major | The pH and source preparation instruction are missing. | Togo M1346 metadata has `ph: 7.0`, and both Togo M1346 and JCM `GRMD=1252` say to dissolve components in distilled water, bring volume to 1.0 L, and adjust pH to 7.0. | Add `ph_value` and `preparation_steps` to the maintained Togo parent, or preserve them in the Togo importer. |
| Major | Calcium chloride has the wrong hydration and CHEBI grounding. | JCM `GRMD=1252` lists `CaCl2 x 2 H2O`; the record says `CaCl2 x H2O` and grounds the row to anhydrous `CHEBI:3312`. | Correct the normalized parent to the JCM calcium salt and ground it to the exact CHEBI hydrated form if available; otherwise remove the near-miss anhydrous grounding. |
| Major | Togo M1346 and MediaDive/JCM J1252 remain split into separate generated records. | Togo M1346 has `original_media_id: JCM_M1252` and JCM `GRMD=1252`; MediaDive `J1252` links to the same JCM page and has the same liquid ingredient list. | Add a source-equivalence or merge-key repair so Togo M1346 and MediaDive/JCM J1252 collapse into one generated liquid recipe, then regenerate. |

## Recommended Edits

1. Fix the Togo M1346 parent so `Distilled water` is represented as 1 L per
   liter, not 1 g/L.
2. Add `ph_value: 7.0` and the JCM/Togo dissolve, bring-to-1-L, and pH
   adjustment instruction to the maintained Togo parent.
3. Recheck the calcium chloride hydrate against JCM `GRMD=1252`; correct the
   preferred term and CHEBI grounding to the dihydrate when an exact term exists
   or leave it explicitly ungrounded.
4. Add a structured JCM `GRMD=1252` reference to the maintained parent so the
   reference validator can inspect the source URL.
5. Add a source-identity merge rule or equivalence overlay for Togo M1346 and
   MediaDive/JCM J1252 while keeping the agar-containing Togo M1347 as the solid
   variant.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated
  `haloarchaeal_complex_medium_ph_7_0` output.
- Inspect the regenerated liquid YAML and confirm it has 1 L/L water, pH 7.0,
  the JCM dissolve-and-adjust preparation text, a corrected calcium chloride
  hydrate row, no 20 g/L agar row, and a structured JCM reference.
- Search `data/merge_yaml/merged` for exact `JCM_M1252`, `mediadive.medium:J1252`,
  and Togo `M1346` tokens with `rg --no-ignore --hidden`; after equivalence
  repair they should identify one merged liquid source recipe group.
- Re-fetch Togo M1346, Togo M1347, JCM `GRMD=1252`, and MediaDive `J1252` to
  confirm the regenerated liquid and solid records still match the live source
  records.

## Additional Notes

- The live JCM `GRMD=1252` page was reachable and generally agreed with
  MediaDive `J1252`, except for the calcium chloride hydrate string.
- Togo M1347 and generated
  `data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0__87d10cc2.yaml`
  are the agar-containing solid version of this recipe.
