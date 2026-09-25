# YAML Record Review: Columbia Blood Agar With 5% Horse Blood

- Repository: CultureMech
- Record: `data/merge_yaml/merged/columbia_blood_agar_with_5_horse_blood.yaml`
- Started UTC: `2026-09-22T10:45:00Z`
- Finished UTC: `2026-09-22T10:49:35Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:009317` for TOGO Medium `M276`, `Columbia Blood Agar With 5% Horse Blood`, generated from the old merge of `data/normalized_yaml/bacterial/TOGO_M276_Columbia_Blood_Agar_With_5_Horse_Blood.yaml` and `data/normalized_yaml/bacterial/TOGO_M211_Columbia_Blood_Agar_With_10_Horse_Blood.yaml` on merge fingerprint `032d0de23baa45e99a5880f7737f71db8e993472847207379bc0f24e829424d7`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/columbia_blood_agar_with_5_horse_blood.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The top-level TOGO identity points to the 5% horse-blood formulation from TOGO `M276` / JCM Medium 282.

The generated record is stale relative to `data/normalized_yaml/bacterial/TOGO_M276_Columbia_Blood_Agar_With_5_Horse_Blood.yaml`. The maintained input now represents the JCM 282 formula as 1 L Columbia blood agar base, Oxoid CM331, plus sterile defibrinated horse blood at `5 PERCENT_V_V`, with preparation steps and a source-duplicate link to the direct JCM / MediaDive record.

The generated duplicate merge is too broad. It merged TOGO `M276` / JCM 282 with TOGO `M211` / JCM 218 even though the inspected JCM pages identify different final blood supplements: 5% horse blood for JCM 282 and 10% horse blood for JCM 218.

## Evidence

The inspected JCM 282 page supports the 5% record: prepare Columbia blood agar base, Oxoid CM331, sterilize and cool it to about 45 C, aseptically add 5% final sterile defibrinated horse blood, then mix and dispense. TOGO M276 mirrors that JCM source and exposes the same 1 L base plus `conc_value: 5`, `conc_unit: %` horse-blood supplement.

The inspected JCM 218 page is explicitly `COLUMBIA BLOOD AGAR WITH 10% HORSE BLOOD`; TOGO M211 likewise exposes a `conc_value: 10`, `conc_unit: %` horse-blood supplement. It should not be an exact synonym or source duplicate of the 5% branch.

## Completeness

The generated record is missing the maintained input's corrected `1000 ML_PER_L` base quantity, `5 PERCENT_V_V` horse-blood quantity, blood grounding, preparation steps, references, data-quality flags, and 2026-09-06 repair history.

No target organism or growth evidence is present. That is an empty optional area for this source-only branch.

## Findings

- Major: the generated record still represents one liter of Columbia blood agar base as `1 G_PER_L`.
- Major: the generated record still represents 5% horse blood as a schema-defaulted `VARIABLE` concentration.
- Major: the generated merge treats the 10% JCM 218 / TOGO M211 recipe as an exact synonym of the 5% JCM 282 / TOGO M276 recipe.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/` from the repaired `data/normalized_yaml/bacterial/TOGO_M276_Columbia_Blood_Agar_With_5_Horse_Blood.yaml` so the generated record carries the 1 L base, 5% horse blood, preparation steps, references, quality flags, and parent source-duplicate link.
- Keep `data/normalized_yaml/bacterial/TOGO_M211_Columbia_Blood_Agar_With_10_Horse_Blood.yaml` separate from TOGO M276 because JCM 218 and JCM 282 differ in final horse-blood percentage.
- Review duplicate detection so blood-percentage differences are included in the fingerprint.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm the generated M276 branch has `1000 ML_PER_L` Columbia blood agar base and `5 PERCENT_V_V` defibrinated horse blood.
- Confirm the M276 generated record no longer lists `columbia_blood_agar_with_10_horse_blood` as a synonym or `TOGO_M211_Columbia_Blood_Agar_With_10_Horse_Blood` in `merged_from`.
- Confirm its `parent_media` still points to `data/normalized_yaml/bacterial/columbia_blood_agar_with_5_horse_blood.yaml` as the direct JCM 282 source duplicate.

## Additional Notes

Empty optional fields are not defects.
