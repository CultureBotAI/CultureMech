# YAML Record Review: supplemented_bg11_mutant

- Repository: CultureMech
- Record: `data/merge_yaml/merged/supplemented_bg11_mutant.yaml`
- Started UTC: 2026-09-25T08:50:09Z
- Finished UTC: 2026-09-25T08:52:26Z
- Verdict: needs curation

## Target

Generated merged record `CultureMech:007292` for `supplemented_bg11_mutant`, with
`MEDIADB:388`, fingerprint
`2621a6fda9988804f409d010fafabe30d0256f03e3815d70d1df56d27bb37f56`, and one
merged source, `supplemented_bg11_mutant`.

## Validation

- LinkML schema: passed; exited 0 with no diagnostics.
- Strict validator: passed with 0 ERROR rows.
- Reference validator: passed with 0 checks.
- Term validator: passed.
- Embedded `curation_history`: Not checked: the available history validator checks
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The record is correctly grounded to MediaDB medium 388. The live MediaDB medium
page is titled `Supplemented bg11 (mutant)`, exposes a tab-delimited
`media_text/388` export, lists source 136 as `Anderson sl et al, 1991`, and
links one growth record, 755, for `Synechocystis pcc6803 psbA on Supplemented
bg11 (mutant)`.

Local normalized source `data/normalized_yaml/bacterial/supplemented_bg11_mutant.yaml`
has already repaired the SQL-parser truncation of names containing parentheses:
`original_name` and `media_term.term.label` are `Supplemented BG11 (Mutant)`,
and the truncated `'''Fe(III` ingredient is `Fe(III)dicitrate`. The generated
merged record is stale relative to that normalized source and still contains the
broken `'''Supplemented BG11 (Mutant` and `'''Fe(III` values.

## Evidence

MediaDB `media_text/388` lists the same 21 compounds and millimolar amounts as
the generated record, including `Diuron` at `0.01`, `Fe(III)dicitrate` at
`0.0245`, `Glucose` at `5.0`, `Kanamycin` at `1.032e-05`, `Chloramphenicol` at
`3.095e-05`, and `Spectinomycin` at `6.018e-05`.

MediaDB source 136 identifies the literature source as Anderson SL et al.,
1991, in Journal of Bacteriology, with the title `Light-activated heterotrophic
growth of the cyanobacterium Synechocystis sp. strain PCC 6803: a
blue-light-requiring process.` PubMed record `PMID:1902208` confirms that title,
DOI `10.1128/jb.173.9.2761-2767.1991`, and PMCID `PMC207855`.

MediaDB growth-data record 755 explicitly links organism `Synechocystis
pcc6803 psbA`, medium 388, source 136, growth rate `0.024`, pH `8.0`, and
temperature `31.0`.

## Completeness

The ingredient set is complete for the MediaDB 388 export. The generated record
does not yet preserve the linked MediaDB growth evidence as `target_organisms`,
conditions, or a source-backed reference, and its import-level notes cite the
generic MediaDB article rather than source 136 for this formulation.

No source-backed pH or filtration preparation was present on MediaDB medium 388
itself. The generic `ADJUST_PH` and 0.22 um `FILTER_STERILIZE` steps are not
supported by the fetched MediaDB medium/export pages.

## Findings

- The generated merge is stale relative to the normalized MediaDB repair:
  `original_name`, `media_term.term.label`, and `Fe(III)dicitrate` still contain
  the old truncation artifacts in `data/merge_yaml/merged/supplemented_bg11_mutant.yaml`.
- The generated merge is also missing term groundings now present on the
  normalized source for `Kanamycin`, `Streptomycin`, `Chloramphenicol`, and
  `Spectinomycin`.
- The MediaDB growth record for `Synechocystis pcc6803 psbA` on medium 388 is
  absent from `target_organisms`, so the record loses explicit growth evidence
  that MediaDB already exposes.
- The generic `ADJUST_PH` and `FILTER_STERILIZE` preparation steps are not
  evidenced by the MediaDB 388 page or tab-delimited export.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/supplemented_bg11_mutant.yaml` from
  `data/normalized_yaml/bacterial/supplemented_bg11_mutant.yaml` so the repaired
  MediaDB names and antibiotic CHEBI groundings are carried into the generated
  merge.
- Extend the MediaDB import or a post-import curator to add source 136, PMID
  1902208, DOI `10.1128/jb.173.9.2761-2767.1991`, and growth-data record 755
  as explicit evidence for `Synechocystis pcc6803 psbA` growth on MediaDB 388.
- Remove or qualify the source-unspecified generic preparation steps unless a
  source page, MediaDB SQL field, or primary publication passage supports them.

## Follow-up Checks

- After regenerating merged YAML, verify that `MEDIADB:388` still appears once
  and that `merge_fingerprint` remains
  `2621a6fda9988804f409d010fafabe30d0256f03e3815d70d1df56d27bb37f56`.
- Compare generated ingredient names against `media_text/388` and confirm that
  `Fe(III)dicitrate` appears without the triple-quote truncation artifact.
- Confirm that the added target organism and reference preserve the MediaDB
  growth-record link to `Synechocystis pcc6803 psbA`, pH 8.0, 31.0 C, and source
  136.

## Additional Notes

None found
