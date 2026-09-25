# YAML Record Review: COLUMBIA BLOOD AGAR WITH 5% RABBIT BLOOD

- Repository: CultureMech
- Record: `data/merge_yaml/merged/columbia_blood_agar_with_5_rabbit_blood__0ed590f0.yaml`
- Started UTC: `2026-09-22T10:55:30Z`
- Finished UTC: `2026-09-22T10:58:15Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:002933` for direct JCM / MediaDive Medium `J586`, `COLUMBIA BLOOD AGAR WITH 5% RABBIT BLOOD`, generated from the old merge of `data/normalized_yaml/bacterial/columbia_blood_agar_with_5_rabbit_blood.yaml` and `data/normalized_yaml/bacterial/anaero_columbia_agar_with_rabbit_blood.yaml` on merge fingerprint `0ed590f0a7fd8f5f7ecfb6e154b3cb73ae069564be3381b3fd62e37a61302cb2`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/columbia_blood_agar_with_5_rabbit_blood__0ed590f0.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The canonical identity is JCM Medium 586, Columbia blood agar base with a 5% final sterile defibrinated rabbit-blood addition.

The generated merge is overbroad. The inspected JCM 690 sibling is not the same recipe text; it instructs users to use the commercial product `Anaero Columbia agar with rabbit blood (BD-BBL)` and does not disclose the product's internal formula. The local JCM 690 normalized file expands that opaque product as if it were ordinary Columbia agar base plus 5% rabbit blood, and the generated output aliases it to JCM 586.

## Evidence

JCM 586 supports preparing Columbia blood agar base, Oxoid CM331, according to directions, sterilizing and cooling to about 45 C, then aseptically adding 5% final sterile defibrinated rabbit blood.

JCM 690 supports only a named ready product from BD-BBL. It does not state that this commercial Anaero Columbia agar product has the same CM331 composition as JCM 586 or that it can be reconstructed from the same seven Columbia base ingredients plus 5% rabbit blood.

## Completeness

The generated JCM 586 record lacks the September source-duplicate link to `data/normalized_yaml/bacterial/TOGO_M591_Columbia_Blood_Agar_With_5_Rabbit_Blood.yaml`.

Both direct maintained inputs retain `physical_state: LIQUID`, even though JCM 586 is a rabbit-blood agar formula and JCM 690 is a named agar product.

No target organism or growth evidence is present. That is an empty optional area for these source-only JCM records.

## Findings

- Major: JCM 690's opaque BD-BBL Anaero Columbia agar product is merged as an exact synonym of the explicit JCM 586 Columbia blood agar base plus 5% rabbit blood recipe.
- Major: the JCM 690 normalized record expands a commercial product whose composition the inspected JCM 690 page does not disclose.
- Major: the direct JCM 586 and JCM 690 normalized inputs both have `physical_state: LIQUID`, contradicting their agar identities.
- Major: the generated JCM 586 record predates the source-duplicate link to the repaired TOGO M591 record.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/` after the September source-duplicate-link repair so JCM 586 carries its TOGO M591 child link.
- Remove `anaero_columbia_agar_with_rabbit_blood` from the JCM 586 exact merge and either keep it as an opaque Anaero Columbia agar product or cite an inspected BD-BBL product specification before expanding its formula.
- In `data/normalized_yaml/bacterial/columbia_blood_agar_with_5_rabbit_blood.yaml` and `data/normalized_yaml/bacterial/anaero_columbia_agar_with_rabbit_blood.yaml`, set `physical_state: SOLID_AGAR`.

## Follow-up Checks

- Validate the regenerated JCM 586 record with open schema, strict, reference, and term validators.
- Confirm `anaero_columbia_agar_with_rabbit_blood` is no longer a synonym or `merged_from` member of the JCM 586 record unless the BD-BBL product formula is source-proven equivalent.
- Confirm JCM 586 links to TOGO M591 as a source duplicate.
- Confirm both maintained direct records are `SOLID_AGAR`.

## Additional Notes

Empty optional fields are not defects.
