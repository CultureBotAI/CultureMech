# YAML Record Review: Columbia Blood Agar With 5% Sheep Blood

- Repository: CultureMech
- Record: `data/merge_yaml/merged/columbia_blood_agar_with_5_sheep_blood.yaml`
- Started UTC: `2026-09-22T10:58:15Z`
- Finished UTC: `2026-09-22T11:01:42Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:009063` for TOGO Medium `M248`, `Columbia Blood Agar With 5% Sheep Blood`, generated from `data/normalized_yaml/bacterial/TOGO_M248_Columbia_Blood_Agar_With_5_Sheep_Blood.yaml` on merge fingerprint `54452d86f4bd4271b235feca97d91580860c7687e21e7484a81523865e3555e3`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/columbia_blood_agar_with_5_sheep_blood.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The source identity is coherent. TOGO `M248` mirrors JCM Medium 256, and both sources identify the recipe as `COLUMBIA BLOOD AGAR WITH 5% SHEEP BLOOD`.

The generated record is stale relative to the maintained TOGO input. `data/normalized_yaml/bacterial/TOGO_M248_Columbia_Blood_Agar_With_5_Sheep_Blood.yaml` now represents the formula as one liter of Columbia blood agar base, Oxoid CM331, plus sterile defibrinated sheep blood at `5 PERCENT_V_V`.

## Evidence

The inspected JCM 256 page supports the repaired preparation: prepare Columbia blood agar base, Oxoid CM331, according to the manufacturer's direction, sterilize and cool to about 45 C, aseptically add 5% final sterile defibrinated sheep blood, then mix and dispense. TOGO M248 exposes the same 1 L base component and `conc_value: 5`, `conc_unit: %` sheep-blood supplement.

The reviewed generated record still contains the old TOGO import shape: the 1 L base is `1 G_PER_L`, and 5% sheep blood was lost into a schema-defaulted `VARIABLE` concentration.

## Completeness

The generated file is missing the maintained input's `1000 ML_PER_L` base quantity, `5 PERCENT_V_V` sheep-blood quantity, UBERON blood grounding, preparation steps, TOGO and JCM references, data-quality flags, 2026-09-06 repair history, and source-duplicate parent link to the direct JCM / MediaDive record.

No target organism or growth evidence is present. That is an empty optional area for this source-only TOGO/JCM branch.

## Findings

- Major: the generated record still represents one liter of Columbia blood agar base as `1 G_PER_L`.
- Major: the generated record still represents 5% sheep blood as a schema-defaulted `VARIABLE` concentration.
- Major: the generated output predates the maintained source-duplicate repair and is missing the direct JCM parent link plus source references.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/` from the repaired `data/normalized_yaml/bacterial/TOGO_M248_Columbia_Blood_Agar_With_5_Sheep_Blood.yaml`.
- Preserve `1000 ML_PER_L` Columbia blood agar base, `5 PERCENT_V_V` defibrinated sheep blood, JCM preparation steps, TOGO and JCM references, blood grounding, data-quality flags, and the `parent_media` source-duplicate link.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm the regenerated M248 branch has `1000 ML_PER_L` Columbia blood agar base and `5 PERCENT_V_V` defibrinated sheep blood.
- Confirm the regenerated M248 branch still links to `data/normalized_yaml/bacterial/columbia_blood_agar_with_5_sheep_blood.yaml` as a source duplicate.

## Additional Notes

Empty optional fields are not defects.
