# YAML Record Review: tissierella_sp_medium_creatinine

- Repository: CultureMech
- Record: `data/merge_yaml/merged/tissierella_sp_medium_creatinine.yaml`
- Started UTC: 2026-09-25T13:17:53Z
- Finished UTC: 2026-09-25T13:17:53Z
- Verdict: needs curation

## Target

Reviewed generated merged YAML for DSMZ medium 557, `TISSIERELLA SP. MEDIUM (CREATININE)`.

The generated record merges four sources: `creatinine_nmh_medium`, `for_dsm_6876`, `for_dsm_6877`, and `tissierella_sp_medium_creatinine`.

## Validation

- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 errors; the TSV contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed; the only diagnostic was the known eutils/pkg_resources startup warning.
- Embedded curation history: Not checked; the available history validator targets standalone `history/` records, not `MediaRecipe.curation_history`.

## Identity and Grounding

The medium identity is grounded to DSMZ medium 557 by `media_term.term.id: mediadive.medium:557`, the DSMZ link in `notes`, and KOMODO synonyms that map to DSMZ 557 variants.

DSMZ medium 557 lists a final volume of 1003 ml, 1 ml Trace element solution SL-11, 1 ml selenite-tungstate solution, and 1 ml 10x Wolin's vitamin solution.

## Evidence

The generated parent salts, yeast extract, resazurin, phosphates, bicarbonate, creatinine, cysteine, and sulfide match the DSMZ parent recipe after normalization to the 1003 ml final volume.

Trace element solution SL-11, selenite-tungstate solution, and Wolin's vitamin solution are separate stocks in the DSMZ source and are added at 1 ml per 1003 ml complete medium.

## Completeness

No target organisms are present; that empty optional field is not a defect in this formulation review.

The record treats `for_dsm_6877` as a source duplicate of the creatinine parent even though DSMZ states that DSM 6877 replaces creatinine with 6.80 g/L N-methylhydantoin as substrate.

## Findings

- Major issue: Trace element solution SL-11 is flattened at stock concentrations. Its EDTA, FeCl2 x 4 H2O, zinc, manganese, boron, cobalt, copper, nickel, and molybdate entries are stock-recipe values and should not appear as final g/L parent concentrations.
- Major issue: stock flattening crosses a duplicate boundary. `MnCl2 x 4 H2O` is recorded as 0.1598205 g/L by adding the source-backed 0.06 g parent amount to the 0.1 g/L SL-11 stock recipe value.
- Major issue: selenite-tungstate and Wolin vitamin stock rows are also recorded at stock concentrations even though each stock contributes only 1 ml to 1003 ml complete medium.
- Major issue: the DSM 6877 N-methylhydantoin formulation needs an explicit variant or a separate source record; it is not the same formulation as the creatinine parent.

## Recommended Edits

- Restore SL-11, selenite-tungstate solution, and Wolin's 10x vitamin solution as nested components, or dilute their ingredients with the 1 ml per 1003 ml factor while preserving component provenance.
- Prevent duplicate merging across parent and stock recipe levels.
- Represent the DSM 6877 N-methylhydantoin substitution as a variant with 6.80 g/L N-methylhydantoin replacing creatinine, if the KOMODO 557.2 record is retained.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after editing the normalized DSMZ and KOMODO sources and regenerating the merge.
- Confirm that DSM 6876 and DSM 6877 variant semantics are assigned to the correct KOMODO source IDs before changing `merged_from`.

## Additional Notes

Exact local source search found only the expected normalized DSMZ and KOMODO siblings for this merge. Ignored files were included for duplicate-report checks with `find`, and no pre-existing ignored report for this generated record was found.
