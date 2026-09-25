# YAML Record Review: haloarchaeal_complex_medium_ph_9_0

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0__1addd263.yaml
- Started UTC: 2026-09-23T09:29:18Z
- Finished UTC: 2026-09-23T09:30:11Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007887 |
| Name | haloarchaeal_complex_medium_ph_9_0 |
| Original name | Haloarchaeal Complex Medium PH 9.0 |
| Category | archaea |
| Generated path | data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0__1addd263.yaml |
| Maintained parent | data/normalized_yaml/archaea/TOGO_M1350_Haloarchaeal_Complex_Medium_PH_9.0.yaml |
| Merge fingerprint | 1addd263d9429df28f47198d6fd46c5f809ea6bcbc06a79f0269e636e1c7f2b3 |

This is the generated August 2026 merge product for Togo Medium M1350, which
Togo imported from the `JCM_M1254-2` solid variant of JCM `GRMD=1254`. Future
edits belong in the Togo normalized parent or the Togo importer; generated YAML
should be regenerated afterward.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0__1addd263.yaml` | Passed |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0__1addd263.yaml --out /private/tmp/haloarchaeal_complex_medium_ph_9_0_1addd263.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0__1addd263.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0__1addd263.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | The repository's documented `just validate-history` check validates standalone files under `history/`; this generated MediaRecipe carries only embedded `curation_history` |

`just` validators were not used because this project currently resolves `llvmlite==0.46.0`
under Python 3.13 and fails inside setuptools before the record can be validated.

## Identity and Grounding

- The target `media_term` identifies Togo `M1350`, labeled `Haloarchaeal Complex
  Medium PH 9.0`.
- Togo M1350 metadata reports `original_media_id: JCM_M1254-2` and the same JCM
  `GRMD=1254` source URL named by this record.
- The live JCM `GRMD=1254` page gives the pH 9.0 liquid formulation and an
  explicit optional 20 g/L agar addition for preparing solid medium; Togo M1350
  is the Togo expansion of that solid form.
- Togo M1349 and MediaDive/JCM `J1254` are the corresponding liquid recipes and
  should remain separate from this agar-containing solid variant.
- The `CaCl2 x H2O` ingredient label is supported by JCM 1254 and the Togo
  projection, but the row is grounded to anhydrous calcium chloride rather than
  an exact calcium chloride monohydrate term.

## Evidence

Supported by inspected sources:

- JCM `GRMD=1254` and Togo M1350 support the solid-variant identity, 20 g/L agar
  addition, 16 dry non-agar ingredients, and post-autoclave adjustment with
  10% w/v Na2CO3 solution.
- JCM, MediaDive, and Togo support the 0.1 g/L `MgCl2 x 6 H2O`, 0.1 g/L
  `CaCl2 x H2O`, and 0.5 g/L `NaNO3` rows that distinguish this pH 9.0 medium
  from the pH 7.0 JCM 1252 formulation.
- Togo M1349 and MediaDive `J1254` support distinct liquid forms without a flat
  agar ingredient.
- CHEBI `CHEBI:2509` is the correct grounding for agar.

Unsupported or incomplete in this generated record:

- The `Distilled water` row is imported as `1 G_PER_L`; Togo M1350 states 1 L
  water and the JCM page says to bring the formulation to 1.0 L.
- The source pH 9.0 is absent from the target record.
- The JCM/Togo preparation instruction is absent from the target record,
  including the post-autoclave pH adjustment with autoclaved 10% w/v Na2CO3
  solution.
- The `Na2CO3 solution` is represented as an empty solution at variable
  concentration, so the 10% w/v stock concentration and pH-adjustment role are
  not recoverable from structured fields.
- The `CaCl2 x H2O` row is grounded to anhydrous `CHEBI:3312`.
- The source URL appears only in `notes`, so the reference validator could not
  inspect the JCM source.

## Completeness

- The target correctly includes agar and `physical_state: SOLID_AGAR`.
- The target is not complete enough to execute as written because the water unit
  is wrong, pH 9.0 is missing, and the required 10% w/v Na2CO3
  post-autoclave pH adjustment is not represented as a preparation step.
- An exact `rg --no-ignore --hidden` search for
  `JCM_M1254-2\b|TOGO:M1350\b` across `data/merge_yaml` and
  `data/normalized_yaml` found only this Togo M1350 source in normalized and
  generated forms.
- The complex `Yeast extract` and `Fish peptone (Fluka)` ingredients are
  correctly left ungrounded.
- Empty organism-specific growth slots are acceptable; this source recipe does
  not assert a narrow strain growth observation.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Distilled water is imported with the wrong unit. | Togo M1350 reports `Distilled water` as 1 L, while the generated YAML writes `value: '1'` and `unit: G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M1350_Haloarchaeal_Complex_Medium_PH_9.0.yaml` or the Togo import/unit-normalization transform. |
| Major | The pH and source preparation instruction are missing. | JCM `GRMD=1254` says to bring volume to 1.0 L, add agar for solid medium, autoclave, then adjust pH to 9.0 with autoclaved 10% w/v Na2CO3 solution; this generated record has no `ph_value` or `preparation_steps`. | Add `ph_value` and ordered `preparation_steps` to the maintained Togo parent, or preserve them in the Togo importer. |
| Major | The Na2CO3 pH-adjustment solution is lossy. | Togo M1350 carries `conc_value: 10` and `conc_unit: (w/v)` for `Na2CO3 solution`; the generated YAML has `composition: []` and `concentration: {value: variable, unit: VARIABLE}`. | Preserve the 10% w/v stock identity in the maintained Togo parent or model it as a pH-adjustment reagent in the preparation step. |
| Major | The calcium chloride monohydrate row is grounded to anhydrous calcium chloride. | JCM and Togo identify the ingredient as `CaCl2 x H2O`; the YAML grounds it to `CHEBI:3312` calcium dichloride. | Ground the row to the exact calcium chloride monohydrate CHEBI term if available; otherwise remove the near-miss anhydrous grounding. |
| Minor | The JCM source is not in structured `references`. | The URL appears only in free text under `notes`, so the reference validator ran 0 checks. | Add a structured JCM `GRMD=1254` reference to the maintained parent. |

## Recommended Edits

1. Fix the Togo M1350 parent so `Distilled water` is represented as 1 L per
   liter, not 1 g/L.
2. Add `ph_value: 9.0` and ordered preparation steps for dissolving ingredients,
   bringing the volume to 1.0 L, adding 20 g/L agar, autoclaving, and adjusting
   pH with autoclaved 10% w/v Na2CO3 solution.
3. Represent the 10% w/v Na2CO3 solution without the empty
   variable-concentration solution placeholder.
4. Correct the calcium chloride monohydrate grounding to an exact hydrated term
   or leave it explicitly ungrounded.
5. Add a structured JCM `GRMD=1254` reference to the maintained parent.
6. Regenerate `data/merge_yaml/merged/` while keeping Togo M1350 as a solid
   variant separate from liquid Togo M1349 and MediaDive/JCM J1254.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated
  solid `haloarchaeal_complex_medium_ph_9_0` output.
- Inspect the regenerated solid YAML and confirm it has 1 L/L water, pH 9.0,
  post-autoclave 10% w/v Na2CO3 pH adjustment, 20 g/L agar, a corrected calcium
  chloride monohydrate row, `physical_state: SOLID_AGAR`, and a structured JCM
  reference.
- Search `data/merge_yaml/merged` for exact `JCM_M1254-2` and Togo `M1350`
  tokens with `rg --no-ignore --hidden`; after repair they should identify one
  generated solid-variant recipe.
- Re-fetch Togo M1349, Togo M1350, JCM `GRMD=1254`, and MediaDive `J1254` to
  confirm the regenerated liquid and solid records still match the live source
  records.

## Additional Notes

- The live JCM `GRMD=1254` page was reachable.
- The M1350 record should keep agar as a normal ingredient because this record
  represents the source's solid-medium variant rather than the base liquid
  recipe.
