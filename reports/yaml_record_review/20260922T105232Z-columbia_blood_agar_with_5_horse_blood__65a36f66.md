# YAML Record Review: COLUMBIA BLOOD AGAR WITH 5% HORSE BLOOD

- Repository: CultureMech
- Record: `data/merge_yaml/merged/columbia_blood_agar_with_5_horse_blood__65a36f66.yaml`
- Started UTC: `2026-09-22T10:49:35Z`
- Finished UTC: `2026-09-22T10:52:32Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:002640` for direct JCM / MediaDive Medium `J282`, `COLUMBIA BLOOD AGAR WITH 5% HORSE BLOOD`, generated from the old merge of `data/normalized_yaml/bacterial/columbia_blood_agar_with_5_horse_blood.yaml` and `data/normalized_yaml/bacterial/columbia_blood_agar_with_10_horse_blood.yaml` on merge fingerprint `65a36f666eb9394e683a29e16d90ca2f547fcd597c2ed06f478d1aeb209d5502`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/columbia_blood_agar_with_5_horse_blood__65a36f66.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The source identity on the canonical record is JCM Medium 282, the 5% horse-blood Columbia blood agar formula. The generated ingredient list is internally inconsistent with that identity: it contains `Defibrinated horse blood` at `10 PERCENT_V_V`, which is the JCM 218 sibling formula.

The inspected JCM pages confirm the boundary. JCM 282 is `COLUMBIA BLOOD AGAR WITH 5% HORSE BLOOD`; JCM 218 is `COLUMBIA BLOOD AGAR WITH 10% HORSE BLOOD`. They should remain separate media or explicit variants, not exact synonyms in one canonical merge.

## Evidence

JCM 282 supports preparing Columbia blood agar base, Oxoid CM331, sterilizing and cooling to about 45 C, then aseptically adding 5% final sterile defibrinated horse blood. JCM 218 has the same procedure but adds 10% final sterile defibrinated horse blood.

The maintained direct JCM records expand the Oxoid CM331 commercial base into pancreatic digest of casein, peptic digest of animal tissue, beef extract, yeast extract, corn starch, sodium chloride, and agar. Those rows may be supportable from an Oxoid product specification, but the inspected JCM pages do not disclose that internal composition and the YAML does not cite an inspected CM331 product sheet.

## Completeness

The generated merge mixes the 5% and 10% sibling formulas and drops the 2026-09-06 source-duplicate links that connect each direct JCM / MediaDive record with its TOGO import.

Both maintained direct inputs also retain `physical_state: LIQUID`, even though JCM 218 and 282 are agar media dispensed into tubes or petri dishes.

No target organism or growth evidence is present. That is an empty optional area for these source-only JCM records.

## Findings

- Blocker: the generated JCM 282 / 5% record contains `Defibrinated horse blood` at `10 PERCENT_V_V`.
- Major: JCM 218 and JCM 282 differ in final horse-blood percentage but were merged into one generated canonical record.
- Major: the direct maintained JCM 218 and JCM 282 inputs both have `physical_state: LIQUID`, contradicting the agar source.
- Major: the Oxoid CM331 ingredient expansion is not source-grounded to an inspected product specification in the record.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/` after the September source-duplicate-link repairs so the direct JCM 282 record keeps its TOGO M276 child while staying separate from JCM 218.
- Repair duplicate detection so 5% and 10% blood additions create distinct fingerprints.
- In `data/normalized_yaml/bacterial/columbia_blood_agar_with_5_horse_blood.yaml` and `data/normalized_yaml/bacterial/columbia_blood_agar_with_10_horse_blood.yaml`, set `physical_state: SOLID_AGAR`.
- Either replace the Oxoid CM331 expansion with an opaque Columbia blood agar base component or add an inspected Oxoid CM331 product citation that supports each expanded base ingredient and concentration.

## Follow-up Checks

- Validate the regenerated JCM 282 record with open schema, strict, reference, and term validators.
- Confirm the JCM 282 generated record has 5% defibrinated horse blood, not 10%.
- Confirm the JCM 218 source is no longer a synonym or `merged_from` member of the JCM 282 record.
- Confirm each direct JCM record links only to its matching TOGO source duplicate: JCM 282 to TOGO M276 and JCM 218 to TOGO M211.
- Confirm both direct records are `SOLID_AGAR`.

## Additional Notes

Empty optional fields are not defects.
