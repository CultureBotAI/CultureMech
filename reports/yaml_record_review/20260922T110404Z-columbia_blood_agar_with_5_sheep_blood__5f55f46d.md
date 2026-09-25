# YAML Record Review: COLUMBIA BLOOD AGAR WITH 5% SHEEP BLOOD

- Repository: CultureMech
- Record: `data/merge_yaml/merged/columbia_blood_agar_with_5_sheep_blood__5f55f46d.yaml`
- Started UTC: `2026-09-22T11:01:42Z`
- Finished UTC: `2026-09-22T11:04:04Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:002614` for direct JCM / MediaDive Medium `J256`, `COLUMBIA BLOOD AGAR WITH 5% SHEEP BLOOD`, generated from `data/normalized_yaml/bacterial/columbia_blood_agar_with_5_sheep_blood.yaml` on merge fingerprint `5f55f46d74db9adfdb5cf72c32dfa58e0b7900e0467e0dbca57ed338a3667514`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/columbia_blood_agar_with_5_sheep_blood__5f55f46d.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The source identity is correct: JCM Medium 256 is `COLUMBIA BLOOD AGAR WITH 5% SHEEP BLOOD`, and the generated record preserves the 5% sheep-blood formulation.

The generated record predates the maintained direct input's 2026-09-06 link to `data/normalized_yaml/bacterial/TOGO_M248_Columbia_Blood_Agar_With_5_Sheep_Blood.yaml`, which is a TOGO import of the same JCM 256 source-catalogue formulation.

## Evidence

The inspected JCM 256 page supports preparing Columbia blood agar base, Oxoid CM331, according to directions, sterilizing and cooling to about 45 C, then aseptically adding 5% final sterile defibrinated sheep blood.

The maintained direct input expands Oxoid CM331 into pancreatic digest of casein, peptic digest of animal tissue, beef extract, yeast extract, corn starch, sodium chloride, and agar. Those rows may be supportable from an Oxoid product specification, but the inspected JCM 256 page does not disclose that internal composition and the YAML does not cite an inspected CM331 product sheet.

## Completeness

The generated record has not yet carried forward the maintained `variant_children` source-duplicate link to the repaired TOGO M248 import.

The maintained direct input still has `physical_state: LIQUID`, even though JCM 256 is an agar medium dispensed into tubes or petri dishes.

No target organism or growth evidence is present. That is an empty optional area for this source-only JCM branch.

## Findings

- Major: `physical_state` is `LIQUID` in `data/normalized_yaml/bacterial/columbia_blood_agar_with_5_sheep_blood.yaml`, contradicting the JCM agar source.
- Major: the Oxoid CM331 ingredient expansion is not source-grounded to an inspected product specification in the record.
- Major: the generated output predates the maintained source-duplicate link to the repaired TOGO M248 record.

## Recommended Edits

- In `data/normalized_yaml/bacterial/columbia_blood_agar_with_5_sheep_blood.yaml`, set `physical_state: SOLID_AGAR`.
- Either replace the Oxoid CM331 expansion with an opaque Columbia blood agar base component or add an inspected Oxoid CM331 product citation that supports each expanded base ingredient and concentration.
- Regenerate `data/merge_yaml/merged/` so the direct JCM 256 generated record carries its TOGO M248 source-duplicate child.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm the regenerated JCM 256 record is `SOLID_AGAR`.
- Confirm the JCM 256 generated record links to TOGO M248 as a source duplicate.
- Confirm the Oxoid CM331 base is either opaque or backed by an inspected product source.

## Additional Notes

Empty optional fields are not defects.
