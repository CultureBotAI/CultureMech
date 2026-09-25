# YAML Record Review: haloarchaeal_complex_medium_ph_9_0

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0.yaml
- Started UTC: 2026-09-23T09:25:49Z
- Finished UTC: 2026-09-23T09:27:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007885 |
| Name | haloarchaeal_complex_medium_ph_9_0 |
| Original name | Haloarchaeal Complex Medium PH 9.0 |
| Category | archaea |
| Generated path | data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0.yaml |
| Maintained parent | data/normalized_yaml/archaea/TOGO_M1349_Haloarchaeal_Complex_Medium_PH_9.0.yaml |
| Merge fingerprint | 94429ccfa238a8c8ae03a8db6937779ec3afa4d63f64546fbcd653cb307d41b4 |

This is the generated August 2026 merge product for Togo Medium M1349, which
Togo imported from JCM `JCM_M1254`. Future edits belong in the Togo normalized
parent, the Togo importer, or source-equivalence merge logic; generated YAML
should be regenerated afterward.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0.yaml` | Passed |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0.yaml --out /private/tmp/haloarchaeal_complex_medium_ph_9_0.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | The repository's documented `just validate-history` check validates standalone files under `history/`; this generated MediaRecipe carries only embedded `curation_history` |

`just` validators were not used because this project currently resolves `llvmlite==0.46.0`
under Python 3.13 and fails inside setuptools before the record can be validated.

## Identity and Grounding

- The target `media_term` identifies Togo `M1349`, labeled `Haloarchaeal Complex
  Medium PH 9.0`.
- Togo M1349 metadata reports `original_media_id: JCM_M1254`, source pH `9.0`,
  and the same JCM `GRMD=1254` source URL named by this record.
- The live JCM `GRMD=1254` page identifies medium 1254 as `HALOARCHAEAL COMPLEX
  MEDIUM PH 9.0`; MediaDive `J1254` is a direct JCM import of the same liquid
  recipe.
- Togo M1350/JCM `JCM_M1254-2` is the solid-medium form with 20 g/L agar added.
  It should remain a related solid variant, not be collapsed into the liquid
  M1349 record.
- The `CaCl2 x H2O` ingredient label is supported by JCM 1254 and the Togo
  projection, but the row is grounded to anhydrous calcium chloride rather than
  an exact calcium chloride monohydrate term.

## Evidence

Supported by inspected sources:

- JCM `GRMD=1254`, MediaDive `J1254`, and Togo M1349 support the M1254 identity,
  pH 9.0 liquid state, 16 dry ingredients, and post-autoclave adjustment with
  10% w/v Na2CO3 solution.
- JCM, MediaDive, and Togo M1349 support the 0.1 g/L `MgCl2 x 6 H2O`, 0.1 g/L
  `CaCl2 x H2O`, and 0.5 g/L `NaNO3` rows that distinguish this pH 9.0 medium
  from the pH 7.0 JCM 1252 formulation.
- Togo M1350 and the JCM optional-agar note support a sibling solid recipe with
  20 g/L agar, which is correctly absent from this liquid M1349 record.
- The complex `Yeast extract` and `Fish peptone (Fluka)` ingredients are
  correctly left ungrounded.

Unsupported or incomplete in this generated record:

- The `Distilled water` row is imported as `1 G_PER_L`; Togo M1349 states 1 L
  water and the JCM page says to bring the formulation to 1.0 L.
- The source pH 9.0 is absent from the target record.
- The JCM/Togo preparation instruction is absent from the target record,
  including the post-autoclave pH adjustment with autoclaved 10% w/v Na2CO3
  solution.
- The `Na2CO3 solution` is represented as an empty solution at variable
  concentration, so the 10% w/v stock concentration and pH-adjustment role are
  not recoverable from structured fields.
- The `CaCl2 x H2O` row is grounded to anhydrous `CHEBI:3312`.
- The direct MediaDive/JCM `J1254` record is split from this Togo M1349 record
  even though both point to JCM `GRMD=1254`.

## Completeness

- The target captures the high-salt pH 9.0 liquid recipe and keeps the M1350
  optional agar as a separate record, which is the right high-level split.
- The target is not complete enough to execute as written because the water unit
  is wrong, pH 9.0 is missing, and the required 10% w/v Na2CO3
  post-autoclave pH adjustment is not represented as a preparation step.
- The source-equivalent direct JCM record is still split from this Togo M1349
  record; an exact `rg --no-ignore --hidden` search for
  `JCM_M1254\b|GRMD=1254\b|TOGO:M1349\b|mediadive\.medium:J1254\b` across
  `data/merge_yaml` and `data/normalized_yaml` found this Togo M1349 record, the
  direct MediaDive/JCM J1254 record, and the solid Togo M1350/JCM_M1254-2
  variant.
- Empty organism-specific growth slots are acceptable; this source recipe does
  not assert a narrow strain growth observation.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Distilled water is imported with the wrong unit. | Togo M1349 reports `Distilled water` as 1 L, while the generated YAML writes `value: '1'` and `unit: G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M1349_Haloarchaeal_Complex_Medium_PH_9.0.yaml` or the Togo import/unit-normalization transform. |
| Major | The pH and source preparation instruction are missing. | Togo M1349 metadata has `ph: 9.0`, and JCM `GRMD=1254` says to bring volume to 1.0 L, autoclave, then adjust pH to 9.0 with autoclaved 10% w/v Na2CO3 solution. | Add `ph_value` and ordered `preparation_steps` to the maintained Togo parent, or preserve them in the Togo importer. |
| Major | The Na2CO3 pH-adjustment solution is lossy. | Togo M1349 carries `conc_value: 10` and `conc_unit: (w/v)` for `Na2CO3 solution`; the generated YAML has `composition: []` and `concentration: {value: variable, unit: VARIABLE}`. | Preserve the 10% w/v stock identity in the maintained Togo parent or model it as a pH-adjustment reagent in the preparation step. |
| Major | The calcium chloride monohydrate row is grounded to anhydrous calcium chloride. | JCM, Togo, and MediaDive all identify the ingredient as `CaCl2 x H2O`; the YAML grounds it to `CHEBI:3312` calcium dichloride. | Ground the row to the exact calcium chloride monohydrate CHEBI term if available; otherwise remove the near-miss anhydrous grounding. |
| Major | Togo M1349 and MediaDive/JCM J1254 remain split into separate generated records. | Togo M1349 has `original_media_id: JCM_M1254` and JCM `GRMD=1254`; MediaDive `J1254` links to the same JCM page and has the same liquid ingredient list. | Add a source-equivalence or merge-key repair so Togo M1349 and MediaDive/JCM J1254 collapse into one generated liquid recipe, then regenerate. |

## Recommended Edits

1. Fix the Togo M1349 parent so `Distilled water` is represented as 1 L per
   liter, not 1 g/L.
2. Add `ph_value: 9.0` and ordered preparation steps for dissolving ingredients,
   bringing the volume to 1.0 L, autoclaving, and adjusting pH with autoclaved
   10% w/v Na2CO3 solution.
3. Represent the 10% w/v Na2CO3 solution without the empty
   variable-concentration solution placeholder.
4. Correct the calcium chloride monohydrate grounding to an exact hydrated term
   or leave it explicitly ungrounded.
5. Add a structured JCM `GRMD=1254` reference to the maintained parent.
6. Add a source-identity merge rule or equivalence overlay for Togo M1349 and
   MediaDive/JCM J1254 while keeping the agar-containing Togo M1350 as the solid
   variant.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated
  `haloarchaeal_complex_medium_ph_9_0` liquid output.
- Inspect the regenerated liquid YAML and confirm it has 1 L/L water, pH 9.0,
  post-autoclave 10% w/v Na2CO3 pH adjustment, a corrected calcium chloride
  monohydrate row, no 20 g/L agar row, and a structured JCM reference.
- Search `data/merge_yaml/merged` for exact `JCM_M1254`, `mediadive.medium:J1254`,
  and Togo `M1349` tokens with `rg --no-ignore --hidden`; after equivalence
  repair they should identify one merged liquid source recipe group.
- Re-fetch Togo M1349, Togo M1350, JCM `GRMD=1254`, and MediaDive `J1254` to
  confirm the regenerated liquid and solid records still match the live source
  records.

## Additional Notes

- The live JCM `GRMD=1254` page was reachable and agreed with MediaDive `J1254`.
- Togo M1350 and generated
  `data/merge_yaml/merged/haloarchaeal_complex_medium_ph_9_0__1addd263.yaml`
  are the agar-containing solid version of this pH 9.0 recipe.
