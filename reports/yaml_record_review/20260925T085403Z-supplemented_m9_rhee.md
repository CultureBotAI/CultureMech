# YAML Record Review: supplemented_m9_rhee

- Repository: CultureMech
- Record: `data/merge_yaml/merged/supplemented_m9_rhee.yaml`
- Started UTC: 2026-09-25T08:52:44Z
- Finished UTC: 2026-09-25T08:54:05Z
- Verdict: needs curation

## Target

Generated merged record `CultureMech:007006` for `supplemented_m9_rhee`, with
`MEDIADB:119`, fingerprint
`23ab0551cc3cf62ceec785612763dea2f292eb802b72fbe3f58751e09277c70d`, and one
merged source, `supplemented_m9_rhee`.

## Validation

- LinkML schema: passed.
- Strict validator: passed with 0 ERROR rows.
- Reference validator: passed with 0 checks.
- Term validator: passed.
- Embedded `curation_history`: Not checked: the available history validator checks
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The record is correctly grounded to MediaDB medium 119. The live MediaDB medium
page is titled `Supplemented m9 (rhee)`, lists 15 compounds, points to source 26
as `Rhee et al, 1997`, and links growth-data records 242 and 243 for two
`Escherichia coli JM109` strains on the same medium.

Local normalized source `data/normalized_yaml/bacterial/supplemented_m9_rhee.yaml`
has already repaired the MediaDB SQL-parser truncation for this record:
`original_name` and `media_term.term.label` are `Supplemented m9 (rhee)`, and
the truncated `'''Iron(III` ingredient has been restored to
`Iron(III) chloride`. The generated merge predates that repair and still
contains both broken values.

## Evidence

MediaDB `media_text/119` lists the same 15 compounds and millimolar amounts as
the generated record, including `beta-D-Glucose` at `77.7087`, `L-Proline` at
`0.86858`, `Ammonium chloride` at `18.6947`, `Thiamine HCl` at `0.1`, and
`Iron(III) chloride` at `0.01998`.

MediaDB source 26 identifies the source as Rhee et al., 1997, in Journal of
Biotechnology, with the title `Influence of the medium composition and plasmid
combination on the growth of recombinant escherichia coli jm109 and on the
production of the fusion protein ecori::spa`. PubMed record `PMID:9232030`
confirms the same article and DOI `10.1016/s0168-1656(97)00058-8`.

MediaDB growth-data record 242 links `Escherichia coli JM109`, medium 119, source
26, growth rate `0.001` 1/h, pH `7.0`, and temperature `30.0`. Record 243 links
`Escherichia coli JM109[pEcoR4,pRK248cI,pMTC48]` to the same medium/source at
growth rate `0.58` 1/h, pH `7.0`, and temperature `30.0`, with notes that the
strain contains plasmids pRK248cl, EcoR4, and pMTC48.

## Completeness

The generated ingredient set is complete for the MediaDB 119 export, modulo the
stale repaired name for `Iron(III) chloride`.

The record does not yet preserve either MediaDB growth-data row as an explicit
`target_organisms` entry. Because record 243 depends on plasmid content, that
curation should retain the full strain label or split it into a defensible
variant/evidence note rather than collapsing it to generic `E. coli`.

No source-backed preparation pH or 0.22 um filtration step was present on the
fetched MediaDB 119 page or tab-delimited export.

## Findings

- The generated merge is stale relative to the normalized MediaDB repair:
  `original_name`, `media_term.term.label`, and `Iron(III) chloride` still
  contain the old parenthesis-truncation artifacts.
- The generated merge is missing the `beta-D-Glucose` CHEBI grounding already
  present on the normalized source.
- Growth-data records 242 and 243 are absent from `target_organisms`, so the
  explicit MediaDB organism, growth-rate, pH, temperature, and plasmid-context
  evidence is not modeled in CultureMech.
- The generic `ADJUST_PH` and `FILTER_STERILIZE` preparation steps are not
  evidenced by MediaDB 119.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/supplemented_m9_rhee.yaml` from
  `data/normalized_yaml/bacterial/supplemented_m9_rhee.yaml` so the repaired
  MediaDB name, `Iron(III) chloride`, and `beta-D-Glucose` grounding are carried
  into the generated merge.
- Add MediaDB source 26, PMID 9232030, DOI
  `10.1016/s0168-1656(97)00058-8`, and growth-data records 242 and 243 as
  explicit target-organism evidence.
- Remove or mark source-unknown generic preparation steps unless a MediaDB SQL
  field or the Rhee et al. article supports them for medium 119.

## Follow-up Checks

- After regeneration, verify that `MEDIA_DB:119` is not introduced as a typo and
  the record retains exactly `MEDIADB:119`.
- Confirm the generated record preserves the fingerprint
  `23ab0551cc3cf62ceec785612763dea2f292eb802b72fbe3f58751e09277c70d`.
- Confirm that the record no longer contains the triple-quote truncation
  artifacts before adding growth evidence.

## Additional Notes

None found
