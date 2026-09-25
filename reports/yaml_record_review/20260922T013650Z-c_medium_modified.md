# YAML Record Review: C Medium, Modified

- Repository: CultureMech
- Record: data/merge_yaml/merged/c_medium_modified.yaml
- Started UTC: 2026-09-22T01:36:50Z
- Finished UTC: 2026-09-22T01:36:50Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:000057`, `c_medium_modified`, `C Medium, Modified`.
- Merge lineage: three source recipes on fingerprint `e460b3462356b3d1b4d31a899a2486362fb8834cd9d001924cb289c16a7b7afa`.
- Canonical owner: `data/normalized_yaml/algae/CCAP_C Medium_ Modified.yaml`.
- Incorrectly merged owners: `data/normalized_yaml/algae/c_medium_modified.yaml` and `data/normalized_yaml/algae/mdy_v.yaml`.
- Claimed source identity: CCAP `C_Modified`, PDF `MR_C_Modified.pdf`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The intended target is CCAP C Medium, Modified for freshwater green algae.
- The generated merge is stale relative to the active normalized CCAP owners: the owners gained source metadata, preparation steps, and a repaired `Na2EDTA` first row on 2026-08-25 and 2026-09-13, after this 2026-08-06 merge was generated.
- `mdy_v` is not a synonym for C Medium, Modified; it cites CCAP `MR_MDY_V.pdf`, has pH 6.8, and is a different CCAP algae medium that happened to share the same broken six-row trace-element extraction.
- The source trace-element stock lists `ZnCl2.6H2O`; the generated merge still has the malformed label `ZnCl .6H O` and an anhydrous zinc dichloride grounding.

## Evidence

- `MR_C_Modified.pdf` specifies final-medium rows for 1 L: 0.1 g `KNO3`, 0.15 g `Ca(NO3).4H2O`, 0.05 g disodium glycerophosphate, 0.04 g `MgSO4.7H2O`, 0.5 g Tris, 3 ml trace element solution, 1 ml vitamin B1, 1 ml vitamin B12, and 10 ml biotin.
- The same PDF instructs dissolving Tris in 900 ml distilled water, bringing the medium to 1 L, adding 15 g/L Bacterial Agar for agar, autoclaving at 15 psi for 15 minutes, and targeting final pH 7.5.
- The six ingredients in the generated record are not the C Medium final composition; they are the trace-element stock defined beneath the main recipe.
- The source also defines three filter-sterile vitamin stocks that are referenced by the final recipe but absent from this generated record.

## Completeness

- The generated merge has a partial trace-element stock recipe only.
- The generated merge is missing every final-medium ingredient and all vitamin stock additions.
- The generated merge is missing the repaired preparation steps that already exist in the normalized owners.
- The generated merge preserves CCAP PDF provenance in `references`, but the structured `sources` slot from the active owner has not propagated.

## Findings

- The first generated ingredient is a parser artifact named `Add to 1000 ml of distilled water` with a 0.75 g/L concentration; the active normalized owners have already corrected this to `Na2EDTA`.
- `ZnCl .6H O` is malformed and is grounded to anhydrous zinc dichloride even though the CCAP trace-element stock specifies `ZnCl2.6H2O`.
- C Medium, Modified is represented by the trace-element stock only, with no `KNO3`, `Ca(NO3).4H2O`, glycerophosphate, `MgSO4.7H2O`, Tris, 3 ml trace element solution, 1 ml vitamin B1, 1 ml vitamin B12, or 10 ml biotin rows.
- The generated merge lost the active owners' preparation steps for 900 ml water, final 1 L volume, optional agar, final pH 7.5, and autoclaving.
- MDY-V was merged into C Medium, Modified as a synonym solely because both different CCAP PDFs initially collapsed to the same six-row trace-element stock signature.

## Recommended Edits

- Regenerate merged YAML from the active normalized owners before judging this specific artifact again.
- Curate the CCAP import/repair path so `MR_C_Modified.pdf` produces a final C Medium record with constituent trace-element, vitamin B1, vitamin B12, and biotin stock references.
- Keep the trace-element stock composition as a subordinate stock recipe rather than as the final medium.
- Fix the zinc chloride hexahydrate label and grounding.
- Remove `mdy_v` from the C Medium, Modified merge family and ensure MDY-V remains a distinct CCAP record.
- Add the PDF's bibliographic references if the schema has a maintained place for literature provenance.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against both C Medium normalized owners.
- Regenerate the merge and confirm that the 2026-08-25 and 2026-09-13 owner repairs are present.
- Compare the regenerated C Medium page against `MR_C_Modified.pdf`, including the final recipe, trace stock, vitamin stocks, optional agar, pH 7.5, and 15 psi autoclaving instruction.

## Additional Notes

- A gitignore-independent search for `CultureMech:000057`, `CCAP_C Medium_ Modified`, `C_Modified`, `mdy_v`, and the merge fingerprint found the expected CCAP C owner, duplicate local C owner, distinct algae and bacterial `mdy_v` owners, the generated C and MDY-V merges, current registry/index/report rows, label-plausibility reports, source-duplicate proposal reports, and stale archived validation rows.
