# YAML Record Review: Microaerophilic Thermus Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/microaerophilic_thermus_medium__96d8cfe7.yaml`
- Started UTC: 2026-09-24T06:18:40Z
- Finished UTC: 2026-09-24T06:18:40Z
- Verdict: needs curation

## Target

- Reviewed merged record `data/merge_yaml/merged/microaerophilic_thermus_medium__96d8cfe7.yaml`.
- Editable normalized source: `data/normalized_yaml/bacterial/TOGO_M935_Microaerophilic_Thermus_Medium.yaml`.
- TOGO medium: `TOGO:M935`, Microaerophilic Thermus Medium.
- JCM source: Medium 894.

## Validation

- LinkML open-schema validation: passed; `No issues found`.
- Strict validation: passed with 0 errors; `validate_strict.py` scanned 1 file and produced only the TSV header.
- Reference validation: passed; 1 file, 0 checks.
- Term validation: passed.
- Embedded history: Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The recipe identity is coherent: TOGO `M935`, JCM Medium 894, and the generated YAML all identify Microaerophilic Thermus Medium.
- JCM 894 defines the recipe by saying to use JCM Medium 276, adjust to pH 8.0, and cultivate under N2-O2 99:1.
- JCM Medium 276 is Castenholz medium, which contains 900 ml water, 1 g Tryptone, 1 g yeast extract, and 100 ml Castenholz basal salt solution from JCM Medium 273.
- The normalized source already resolves this nested chain and points `Castenholz basal salt solution` to the JCM Medium 273 composition.

## Evidence

- TOGO M935 carries the same main-medium rows as JCM 276: 900 ml water, 1 g yeast extract, 1 g tryptone, and 100 ml Castenholz basal salt solution.
- The generated record converted 900 ml water to `900 G_PER_L` and the 100 ml Castenholz addition to an empty `Unknown solution` at `100 G_PER_L`.
- The generated record has no `ph_value`, even though TOGO M935 reports pH 8.0 and JCM 894 says to adjust the referenced medium to pH 8.0.
- The generated record keeps Nitrogen gas and Oxygen gas as variable ingredients but drops the source gas atmosphere, N2-O2 99:1.
- The normalized source has already repaired water to `900.0 ML_PER_L`, the Castenholz addition to `100.0 ML_PER_L`, pH to 8.0, the Oxygen gas term to `CHEBI:15379`, and the Castenholz basal salt nested composition.

## Completeness

- The generated record is incomplete relative to both the JCM source and the repaired normalized source.
- Castenholz basal salt solution is present only as an empty placeholder, so all JCM Medium 273 component detail is absent from the generated recipe.
- The pH 8.0 and N2-O2 99:1 cultivation condition are absent from the generated recipe.

## Findings

- The generated file is stale relative to `data/normalized_yaml/bacterial/TOGO_M935_Microaerophilic_Thermus_Medium.yaml`.
- `Distilled water` is published as 900 g/L rather than 900 ml/L.
- `Castenholz basal salt solution` is published as an empty 100 g/L `Unknown solution`, not as a 100 ml/L nested solution.
- The generated record omits pH 8.0.
- The generated record omits the N2-O2 99:1 gas atmosphere from the preparation context.
- Oxygen gas is ungrounded in the generated file even though the normalized source has `CHEBI:15379`.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/microaerophilic_thermus_medium__96d8cfe7.yaml` from the repaired normalized source.
- Confirm the regenerated file preserves `900.0 ML_PER_L` water and a `100.0 ML_PER_L` Castenholz basal salt addition.
- Confirm the regenerated file includes pH 8.0 and the N2-O2 99:1 cultivation condition.
- Confirm the nested JCM Medium 273 Castenholz basal salt composition is present after merge generation.
- No additional normalized-source edit was apparent from this review.

## Follow-up Checks

- Re-run focused open-schema, strict, reference, and term validators for `data/merge_yaml/merged/microaerophilic_thermus_medium__96d8cfe7.yaml`.
- Verify no milliliter quantities are emitted as `G_PER_L`.
- Verify the `Castenholz basal salt solution` is not an empty `Unknown solution`.

## Additional Notes

- Empty optional fields were not treated as defects.
