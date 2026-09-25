# YAML Record Review: pyruvate_minimal_media

- Repository: CultureMech
- Record: data/merge_yaml/merged/pyruvate_minimal_media.yaml
- Started UTC: 2026-09-25T00:01:16Z
- Finished UTC: 2026-09-25T00:01:46Z
- Verdict: needs curation

## Target

Reviewed generated MediaRecipe `CultureMech:007020` for
`pyruvate_minimal_media`.

- Generated record: `data/merge_yaml/merged/pyruvate_minimal_media.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/pyruvate_minimal_media.yaml`
- Generated from: `pyruvate_minimal_media`
- Source identity: `MEDIADB:131`
- Merge fingerprint: `984bb5093ac87b7e447cdc459c5e33fd4ea5fc4735dd0912eaca1cbfaf277b58`

`data/merge_yaml/merged` is generated output. Fix the normalized owner and then
regenerate this target.

## Validation

- Open LinkML validation: Passed; `linkml-validate` reported `No issues found`.
- Strict validation: Passed; `scripts/validate_strict.py` wrote a one-line TSV
  with only the header and reported 0 ERROR rows.
- LinkML reference validation: Passed; 1 file validated, 0 reference checks
  were applicable, and all validations passed.
- LinkML term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` embedded in merged
  YAML.

## Identity and Grounding

The MediaDB identity is valid and unique. Live MediaDB medium 131 serves
`Pyruvate minimal media`, the tab-delimited export for medium 131 lists the same
14 compounds and millimolar amounts, and `MEDIADB:131` is the right local source
identifier. An ignored-file-inclusive exact search for `MEDIADB:131`, the
MediaDB 131 import note, and the MediaDB medium 131 URL found only this owner,
this generated record, and normalized index entries.

Most available MediaDB CHEBI ids are represented, but iron remains incomplete in
the owner. The tab-delimited MediaDB export names `Iron(III) chloride` and gives
CHEBI id `CHEBI:30808`; the normalized owner has the restored ingredient name
but still has no `term` or CHEBI-keyed MediaIngredientMech field for that row.

## Evidence

Live MediaDB medium 131 lists 14 compounds: pyruvate, ammonium sulfate, calcium
chloride anhydrous, cobalt chloride, cupric chloride, dibasic sodium phosphate,
Iron(III) chloride, magnesium sulfate, manganese chloride, potassium dihydrogen
phosphate, sodium chloride, sodium molybdate, thiamine HCl, and zinc chloride.
The millimolar values in the generated and normalized YAML match the MediaDB
tab-delimited export.

The MediaDB page associates the formulation with three growth records for
`Escherichia coli BW25113`, `Escherichia coli BW25113_gnd-`, and
`Escherichia coli BW25113_zwf-` on Pyruvate minimal media. MediaDB source 38
identifies the source as Zhao et al. 2003 in Applied Microbiology and
Biotechnology with PubMed ID 14661115.

## Completeness

The record has the full 14-compound MediaDB formula, but it is incomplete for
provenance and source-linked biology. It does not capture the three MediaDB
growth associations as target-organism or growth evidence, and its curation
history cites a different paper than MediaDB source 38 for medium 131.

## Findings

- The generated file is stale relative to the normalized owner. It still carries
  the malformed preferred term `'''Iron(III'`, while the owner has the
  2026-08-31 `REPAIRED_MEDIADB_TRUNCATED_NAME` repair that restores
  `Iron(III) chloride`.
- The restored `Iron(III) chloride` row is still ungrounded even though the
  MediaDB tab-delimited export supplies CHEBI id `CHEBI:30808`.
- The import history cites `Mazumdar et al. (2014) PLOS One`, but the live
  MediaDB page for medium 131 links the recipe to source 38, `Zhao et al, 2003`.
  This should be repaired so provenance for `MEDIADB:131` points to the same
  source MediaDB displays.
- MediaDB exposes three growth records for this medium, all for the BW25113,
  gnd-, and zwf- Escherichia coli strains used with Pyruvate minimal media.
  Those organism/growth associations are absent from the MediaRecipe.
- The preparation steps are generic MediaDB defaults rather than
  source-grounded instructions. MediaDB 131 does not provide an explicit pH or
  filtration instruction, so the `ADJUST_PH` and `FILTER_STERILIZE` steps should
  be verified against the Zhao 2003 method or removed.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/pyruvate_minimal_media.yaml` from the
  normalized owner so the `Iron(III) chloride` name repair reaches generated
  output.
- Ground `Iron(III) chloride` with the CHEBI id provided by MediaDB or document
  why that exact source grounding is not usable.
- Correct the MediaDB 131 source citation from the stale Mazumdar 2014 note to
  Zhao et al. 2003 / PubMed 14661115.
- Add source-backed target organisms or growth evidence for the three MediaDB
  Pyruvate minimal media growth records.
- Verify the generic dissolve, pH-adjustment, and filter-sterilization steps
  against Zhao et al. 2003 before keeping them as asserted protocol text.

## Follow-up Checks

- Re-run open, strict, reference, and term validation after regeneration.
- Run an ignored-file-inclusive exact search for `MEDIADB:131`, the medium 131
  URL, and `Zhao et al` to make sure MediaDB 131 has one owner and corrected
  provenance.
- Compare the repaired owner with both the live MediaDB medium page and the
  tab-delimited export, checking the 14 compound names, millimolar values, CHEBI
  ids, source 38, and growth-data links.

## Additional Notes

Empty optional fields were not treated as defects. No GitHub issues, PR
comments, or source YAML edits were made during this review pass.
