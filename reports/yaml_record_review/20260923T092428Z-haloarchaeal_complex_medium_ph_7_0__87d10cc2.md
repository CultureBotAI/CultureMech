# YAML Record Review: haloarchaeal_complex_medium_ph_7_0

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0__87d10cc2.yaml
- Started UTC: 2026-09-23T09:23:51Z
- Finished UTC: 2026-09-23T09:24:28Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007883 |
| Name | haloarchaeal_complex_medium_ph_7_0 |
| Original name | Haloarchaeal Complex Medium PH 7.0 |
| Category | archaea |
| Generated path | data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0__87d10cc2.yaml |
| Maintained parent | data/normalized_yaml/archaea/TOGO_M1347_Haloarchaeal_Complex_Medium_PH_7.0.yaml |
| Merge fingerprint | 87d10cc2048837da3da40fea4893a597e7b2ccafd9d66f90ed7365ebad4ec158 |

This is the generated August 2026 merge product for Togo Medium M1347, which
Togo imported from the `JCM_M1252-2` solid variant of JCM `GRMD=1252`. Future
edits belong in the Togo normalized parent or the Togo importer; generated YAML
should be regenerated afterward.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0__87d10cc2.yaml` | Passed |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0__87d10cc2.yaml --out /private/tmp/haloarchaeal_complex_medium_ph_7_0_87d10cc2.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0__87d10cc2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/haloarchaeal_complex_medium_ph_7_0__87d10cc2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | The repository's documented `just validate-history` check validates standalone files under `history/`; this generated MediaRecipe carries only embedded `curation_history` |

`just` validators were not used because this project currently resolves `llvmlite==0.46.0`
under Python 3.13 and fails inside setuptools before the record can be validated.

## Identity and Grounding

- The target `media_term` identifies Togo `M1347`, labeled `Haloarchaeal Complex
  Medium PH 7.0`.
- Togo M1347 metadata reports `original_media_id: JCM_M1252-2` and the same JCM
  `GRMD=1252` source URL named by this record.
- The live JCM `GRMD=1252` page gives the pH 7.0 liquid formulation and an
  explicit optional 20 g/L agar addition for preparing solid medium; Togo M1347
  is the Togo expansion of that solid form.
- Togo M1346 and MediaDive/JCM `J1252` are the corresponding liquid recipes and
  should remain separate from this agar-containing solid variant.
- The `CaCl2 x H2O` row is under-specified and wrongly grounded. The live JCM
  page lists `CaCl2 x 2 H2O`, while this record says `CaCl2 x H2O` and grounds
  the row to anhydrous calcium chloride.

## Evidence

Supported by inspected sources:

- JCM `GRMD=1252` and Togo M1347 support the solid-variant identity, 20 g/L agar
  addition, and most dry-ingredient amounts.
- JCM supports the instruction to dissolve the non-agar components in distilled
  water, bring volume to 1.0 L, and adjust pH to 7.0.
- Togo M1347 supports a solid recipe with all liquid M1252 ingredients plus
  20 g/L agar.
- Togo M1346 and MediaDive `J1252` support distinct liquid forms without a flat
  agar ingredient.
- CHEBI `CHEBI:2509` is the correct grounding for agar.

Unsupported or incomplete in this generated record:

- The `Distilled water` row is imported as `1 G_PER_L`; Togo M1347 states 1 L
  water and the JCM page says to bring the formulation to 1.0 L.
- The source pH 7.0 is absent from the target record.
- The JCM/Togo preparation instruction is absent from the target record.
- Calcium chloride is represented as `CaCl2 x H2O` and grounded to anhydrous
  `CHEBI:3312`, while the live JCM page lists `CaCl2 x 2 H2O`.
- The source URL appears only in `notes`, so the reference validator could not
  inspect the JCM source.

## Completeness

- The target correctly includes agar and `physical_state: SOLID_AGAR`.
- The target is not complete enough to execute as written because the water unit
  is wrong, pH 7.0 is missing, and the dissolve/bring-to-volume preparation
  step is missing.
- An exact `rg --no-ignore --hidden` search for
  `JCM_M1252\b|GRMD=1252\b|TOGO:M1346\b|mediadive\.medium:J1252\b` across
  `data/merge_yaml` and `data/normalized_yaml` found this solid Togo M1347
  record plus the liquid Togo M1346 and direct MediaDive/JCM J1252 records.
- The complex `Yeast extract` and `Fish peptone (Fluka)` ingredients are
  correctly left ungrounded.
- Empty organism-specific growth slots are acceptable; this source recipe does
  not assert a narrow strain growth observation.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Distilled water is imported with the wrong unit. | Togo M1347 reports `Distilled water` as 1 L, while the generated YAML writes `value: '1'` and `unit: G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M1347_Haloarchaeal_Complex_Medium_PH_7.0.yaml` or the Togo import/unit-normalization transform. |
| Major | The pH and source preparation instruction are missing. | JCM `GRMD=1252` says to dissolve components in distilled water, bring volume to 1.0 L, and adjust pH to 7.0 before its solid-medium agar note; this generated record has no `ph_value` or `preparation_steps`. | Add `ph_value` and `preparation_steps` to the maintained Togo parent, or preserve them in the Togo importer. |
| Major | Calcium chloride has the wrong hydration and CHEBI grounding. | JCM `GRMD=1252` lists `CaCl2 x 2 H2O`; the record says `CaCl2 x H2O` and grounds the row to anhydrous `CHEBI:3312`. | Correct the normalized parent to the JCM calcium salt and ground it to the exact CHEBI hydrated form if available; otherwise remove the near-miss anhydrous grounding. |
| Minor | The JCM source is not in structured `references`. | The URL appears only in free text under `notes`, so the reference validator ran 0 checks. | Add a structured JCM `GRMD=1252` reference to the maintained parent. |

## Recommended Edits

1. Fix the Togo M1347 parent so `Distilled water` is represented as 1 L per
   liter, not 1 g/L.
2. Add `ph_value: 7.0` and the JCM/Togo dissolve, bring-to-1-L, pH adjustment,
   and solid-medium agar instruction to the maintained Togo parent.
3. Recheck the calcium chloride hydrate against JCM `GRMD=1252`; correct the
   preferred term and CHEBI grounding to the dihydrate when an exact term exists
   or leave it explicitly ungrounded.
4. Add a structured JCM `GRMD=1252` reference to the maintained parent so the
   reference validator can inspect the source URL.
5. Regenerate `data/merge_yaml/merged/` while keeping Togo M1347 as a solid
   variant separate from liquid Togo M1346 and MediaDive/JCM J1252.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated
  solid `haloarchaeal_complex_medium_ph_7_0` output.
- Inspect the regenerated solid YAML and confirm it has 1 L/L water, pH 7.0,
  the JCM dissolve-and-adjust preparation text, 20 g/L agar, a corrected calcium
  chloride hydrate row, `physical_state: SOLID_AGAR`, and a structured JCM
  reference.
- Search `data/merge_yaml/merged` for exact `JCM_M1252-2` and Togo `M1347`
  tokens with `rg --no-ignore --hidden`; after repair they should identify one
  generated solid-variant recipe.
- Re-fetch Togo M1346, Togo M1347, JCM `GRMD=1252`, and MediaDive `J1252` to
  confirm the regenerated liquid and solid records still match the live source
  records.

## Additional Notes

- The live JCM `GRMD=1252` page was reachable.
- The M1347 record should keep agar as a normal ingredient because this record
  represents the source's solid-medium variant rather than the base liquid
  recipe.
