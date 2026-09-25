# YAML Record Review: thermococcus_stetteri_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermococcus_stetteri_medium__77e25d6a.yaml
- Started UTC: 2026-09-25T12:00:05Z
- Finished UTC: 2026-09-25T12:00:05Z
- Verdict: needs curation

## Target
Reviewed the generated merge of TOGO M151, M152, and M233 for Thermococcus Stetteri/Litoralis/Fumicolans media.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with 0 checks.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The canonical record is grounded to TOGO:M151.
- TOGO M151 is JCM_M160, TOGO M152 is JCM_M161, and TOGO M233 is JCM_M241.
- The three TOGO records share the Modified Brock's salt base reference but differ in final yeast extract, peptone, and pH conditions, so they are related variants rather than exact source duplicates.

## Evidence
- M151 records final pH 6.5 with 3 g yeast extract and 0.5 g peptone.
- M152 says to use Medium 160 with 1.0 g/L final yeast extract, 5.0 g/L final peptone, and pH 7.2.
- M233 says to use Medium 160 with 0.5 g/L final yeast extract, 2.0 g/L final peptone, and pH 7.5.
- M151, M152, and M233 all include 1 L of Modified Brock's salt base solution M156 and anaerobic N2 handling.

## Completeness
- The canonical recipe retains M151's NaCl, resazurin, sulfur, yeast extract, and peptone rows.
- The Modified Brock's salt base reference is empty and stored as 1 G_PER_L.
- The M151, M152, and M233 pH values are not represented.

## Findings
- Three variant recipes with different final pH and peptone or yeast extract concentrations were merged into one canonical record.
- The 1 L Modified Brock's salt base M156 cross-reference was converted to an empty solution at 1 G_PER_L instead of being linked or expanded.
- The 1 mg resazurin row was imported as 1 G_PER_L.
- H2SO4 and N2 were modeled as variable-concentration ingredients even though the source uses them for pH adjustment and anaerobic gas handling.
- The sterile Na2S x 9H2O addition described in the M151/M233 preparation text is absent.

## Recommended Edits
- Keep M151 as the base recipe and split M152 and M233 into explicit pH/nutrient variants, or create separate generated records if the local variant model cannot represent them.
- Preserve Modified Brock's salt base M156 as a medium reference or expand it without converting 1 L into 1 G_PER_L.
- Correct the resazurin mg conversion.
- Move H2SO4, N2, and Na2S x 9H2O into preparation or stock-addition fields rather than top-level solute rows.

## Follow-up Checks
- Rebuild the records and verify that M151, M152, and M233 remain distinguishable by pH, yeast extract, and peptone concentration.
- Re-run schema, strict, reference, and term validation on the rebuilt records.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
