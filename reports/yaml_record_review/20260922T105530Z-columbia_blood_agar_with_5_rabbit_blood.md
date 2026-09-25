# YAML Record Review: Columbia Blood Agar With 5% Rabbit Blood

- Repository: CultureMech
- Record: `data/merge_yaml/merged/columbia_blood_agar_with_5_rabbit_blood.yaml`
- Started UTC: `2026-09-22T10:52:32Z`
- Finished UTC: `2026-09-22T10:55:30Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:009988` for TOGO Medium `M591`, `Columbia Blood Agar With 5% Rabbit Blood`, generated from `data/normalized_yaml/bacterial/TOGO_M591_Columbia_Blood_Agar_With_5_Rabbit_Blood.yaml` on merge fingerprint `03bd875601b9f2023123f4926c21de93042cfa62c2496d5da1dc990c91d5efee`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/columbia_blood_agar_with_5_rabbit_blood.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The source identity is coherent. TOGO `M591` mirrors JCM Medium 586, and both sources identify the recipe as `COLUMBIA BLOOD AGAR WITH 5% RABBIT BLOOD`.

The generated record is stale relative to the maintained TOGO input. `data/normalized_yaml/bacterial/TOGO_M591_Columbia_Blood_Agar_With_5_Rabbit_Blood.yaml` now represents the formula as one liter of Columbia blood agar base, Oxoid CM331, plus sterile defibrinated rabbit blood at `5 PERCENT_V_V`.

## Evidence

The inspected JCM 586 page supports the repaired preparation: prepare Columbia blood agar base, Oxoid CM331, according to the manufacturer's direction, sterilize and cool to about 45 C, aseptically add 5% final sterile defibrinated rabbit blood, then mix and dispense. TOGO M591 exposes the same 1 L base component and `conc_value: 5`, `conc_unit: %` rabbit-blood supplement.

The reviewed generated record still contains the old TOGO import shape: the 1 L base is `1 G_PER_L`, and 5% rabbit blood was lost into a schema-defaulted `VARIABLE` concentration.

## Completeness

The generated file is missing the maintained input's `1000 ML_PER_L` base quantity, `5 PERCENT_V_V` rabbit-blood quantity, UBERON blood grounding, preparation steps, TOGO and JCM references, data-quality flags, 2026-09-06 repair history, and source-duplicate parent link to the direct JCM / MediaDive record.

No target organism or growth evidence is present. That is an empty optional area for this source-only TOGO/JCM branch.

## Findings

- Major: the generated record still represents one liter of Columbia blood agar base as `1 G_PER_L`.
- Major: the generated record still represents 5% rabbit blood as a schema-defaulted `VARIABLE` concentration.
- Major: the generated output predates the maintained source-duplicate repair and is missing the direct JCM parent link plus source references.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/` from the repaired `data/normalized_yaml/bacterial/TOGO_M591_Columbia_Blood_Agar_With_5_Rabbit_Blood.yaml`.
- Preserve `1000 ML_PER_L` Columbia blood agar base, `5 PERCENT_V_V` defibrinated rabbit blood, JCM preparation steps, TOGO and JCM references, blood grounding, data-quality flags, and the `parent_media` source-duplicate link.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm the regenerated M591 branch has `1000 ML_PER_L` Columbia blood agar base and `5 PERCENT_V_V` defibrinated rabbit blood.
- Confirm the regenerated M591 branch still links to `data/normalized_yaml/bacterial/columbia_blood_agar_with_5_rabbit_blood.yaml` as a source duplicate.

## Additional Notes

Empty optional fields are not defects.
