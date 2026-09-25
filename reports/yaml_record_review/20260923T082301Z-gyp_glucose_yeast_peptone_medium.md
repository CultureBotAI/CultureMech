# YAML Record Review: GYP GLUCOSE-YEAST-Peptone medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/gyp_glucose_yeast_peptone_medium.yaml`
- Started UTC: 2026-09-23T08:21:39Z
- Finished UTC: 2026-09-23T08:23:01Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:006668`, `gyp_glucose_yeast_peptone_medium`, merged from KOMODO/DSMZ 852 duplicate records and the fungal DSMZ / MediaDive 852 source record.

## Validation

- LinkML validation: passed.
- Strict validation: passed with 0 ERROR rows in `/private/tmp/gyp_glucose_yeast_peptone_medium.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked: the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The KOMODO base record, eight KOMODO strain-specific `852_*` records, and the fungal DSMZ/MediaDive 852 record all point to DSMZ Medium 852 and share the same local ingredient signature. Exact ignored-file-inclusive search found those expected source records under `data/normalized_yaml/bacterial` and `data/normalized_yaml/fungal`; it did not find a separate generated record for the fungal DSMZ 852 parent.

Glucose, Na-acetate, Agar, MgSO4 x 7 H2O, MnSO4 x 4 H2O, FeSO4 x 7 H2O, and NaCl are grounded. Yeast extract and Peptone remain ungrounded complex components.

## Evidence

The DSMZ Medium 852 PDF lists 20 g Glucose, 10 g Yeast extract, 10 g tryptic Peptone, 10 g Na-acetate, 5 ml Salt solution, and 1000 ml Distilled water. The separate 1000 ml Salt solution contains 40 g MgSO4 x 7 H2O, 2 g MnSO4 x 4 H2O, 2 g FeSO4 x 7 H2O, and 2 g NaCl. For solid medium, DSMZ adds 10 g/L bacteriological agar, adjusts to pH 6.8, and adds filter-sterilized salt solution after medium sterilization.

The generated record preserves pH 6.8 and the top-level glucose, yeast extract, peptone, acetate, and agar values. It flattens the salt solution at stock strength and drops the post-sterilization/filter-sterilization preparation step.

## Completeness

The generated ingredient set is incomplete because the 5 ml Salt solution addition and its 1000 ml stock recipe are not represented. Provenance is also ambiguous: `merged_from` lists `gyp_glucose_yeast_peptone_medium` twice without the bacterial/fungal path distinction, and the generated `media_term` keeps only `komodo.medium:852` even though the exact merge also includes the fungal DSMZ / MediaDive 852 parent.

## Findings

- The DSMZ Salt solution is flattened at stock strength. Only 5 ml of the 1000 ml stock should be added, but the generated recipe emits the stock's 40 g/L MgSO4 x 7 H2O, 2 g/L MnSO4 x 4 H2O, 2 g/L FeSO4 x 7 H2O, and 2 g/L NaCl as top-level final-medium rows.
- The DSMZ preparation step is missing, including the bacteriological-agar context, pH 6.8 adjustment text, and instruction to add filter-sterilized salt solution after medium sterilization.
- Generated provenance is ambiguous for the duplicate `gyp_glucose_yeast_peptone_medium.yaml` basenames from `data/normalized_yaml/bacterial` and `data/normalized_yaml/fungal`; `merged_from` lists the same basename twice.
- The generated `media_term` keeps only `komodo.medium:852`; the DSMZ / MediaDive 852 identity is only implicit.
- The embedded KOMODO import history timestamp `2026-01-27T01:15:03.fZ` is malformed.
- Yeast extract and Peptone remain ungrounded. These are complex ingredients, but they should be checked against available mappings.

## Recommended Edits

- Preserve DSMZ Medium 852 Salt solution as a nested 1000 ml stock recipe and connect it to the main medium as a 5 ml addition.
- Preserve the DSMZ preparation step about bacteriological agar, pH 6.8, and adding filter-sterilized salt solution after sterilization.
- Make exact-merge provenance path-qualified when source basenames collide across categories.
- Make the DSMZ / MediaDive 852 source identity explicit in regenerated provenance, not only through the fungal category and source index.
- Fix the malformed KOMODO history timestamp in the normalized KOMODO parent.
- Attempt complex-component groundings for Yeast extract and Peptone.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validators after recuration.
- Revalidate embedded `curation_history` once the KOMODO timestamp is corrected upstream.
- Recompare the regenerated record against DSMZ Medium 852 and verify that only 5 ml of the salt solution is added to the main recipe.

## Additional Notes

None found.
