# YAML Record Review: Lysine salt; Schaechter et al

- Repository: CultureMech
- Record: `data/merge_yaml/merged/lysine_salt_schaechter_et_al.yaml`
- Started UTC: 2026-09-23T20:44:30Z
- Finished UTC: 2026-09-23T20:45:43Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/lysine_salt_schaechter_et_al.yaml`
- Maintained owner: `data/normalized_yaml/bacterial/lysine_salt_schaechter_et_al.yaml`
- CultureMech ID: `CultureMech:007132`
- Media term: `MEDIADB:236`
- Merge fingerprint: `5a9182edd7c64b0788a3c21a1e3f555c686ab343b3ab3ba7f0100bc3e093427c`
- Merge sources: `lysine_salt_schaechter_et_al`
- Ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` found the maintained MediaDB owner, generated indexes, the generated merged record, and historical archive rows; it did not find a second maintained owner for exact `CultureMech:007132` or `MEDIADB:236`.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows in `/private/tmp/lysine_salt_schaechter_et_al.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history` entries were not checked as standalone history records.

## Identity and Grounding

The record's identifier, name, and `MEDIADB:236` media term identify MediaDB medium 236, `Lysine salt; schaechter et al`. The generated recipe is a one-source merge of the maintained bacterial YAML owner.

The MediaDB medium page lists the same six compounds with the same millimolar amounts in the YAML: L-Lysine 0.957658 mM, Citrate 5.20497 mM, Dibasic sodium phosphate 28.0899 mM, Potassium chloride 9.92605 mM, Magnesium sulfate 0.405729 mM, and Sodium ammonium phosphate 8.32187 mM.

## Evidence

- MediaDB `/defined_media/media/236/` confirms medium 236 is `Lysine salt; schaechter et al`, has exactly six compounds, links one organism, links one source, and links one growth-data record.
- MediaDB `/defined_media/media_text/236/` confirms the six compound names and amounts imported into the YAML.
- MediaDB `/defined_media/sources/84/` identifies the primary source as Schaechter et al. 1958, "Dependency on medium and temperature of cell size and chemical composition during balanced growth of salmonella typhimurium", in `J. Gen. Microbiol.`, with PMID 13611202.
- MediaDB `/defined_media/growthdata/460/` links this medium to `Salmonella enterica Typhimurium LT2`, pH 7.0, and growth rate 0.43 1/h.

## Completeness

The formula itself is complete relative to the MediaDB compound table: every listed MediaDB compound is represented at the same concentration.

The record is not complete as an evidence-backed CultureMech curation. It lacks structured source references for the MediaDB page and Schaechter et al. primary source, has no `target_organisms` entry for the MediaDB-linked `Salmonella enterica Typhimurium LT2` growth condition, and carries generic preparation steps that are not present on the MediaDB medium, source, or growth-data pages.

## Findings

1. The record drops the source graph that MediaDB exposes. MediaDB medium 236 links source 84, and source 84 resolves to Schaechter et al. 1958 with PMID 13611202. The YAML only has a `media_term` for `MEDIADB:236` and a free-text `notes` URL, so downstream consumers cannot traverse a structured primary citation for the imported recipe.

2. The MediaDB growth target is missing. MediaDB medium 236 links growth data 460 for `Salmonella enterica Typhimurium LT2`; the growth-data page records pH 7.0 and growth rate 0.43 1/h. The YAML has no `target_organisms` block, which loses the organism this media record is known to support.

3. The generated preparation steps overclaim the evidence. Neither the MediaDB medium page, tab-delimited export, source page, nor growth-data page specifies 0.22 um filtration, and the formula page does not specify a pH-adjustment step. Those instructions should be replaced with source-backed steps after checking the primary paper, or omitted if the source does not provide them.

## Recommended Edits

- In `data/normalized_yaml/bacterial/lysine_salt_schaechter_et_al.yaml`, add structured source references for MediaDB medium 236 and the Schaechter et al. 1958 primary source.
- Add a `target_organisms` entry for `Salmonella enterica Typhimurium LT2`, grounded to the MediaDB growth-data record and carrying the observed pH 7.0 and growth rate 0.43 1/h where the schema permits.
- Confirm Schaechter et al. 1958 before adding any pH-adjustment or sterilization instructions; if the primary paper does not specify 0.22 um filtration, remove the generic `FILTER_STERILIZE` step.
- Keep the six imported millimolar ingredients unchanged unless primary-source review shows a MediaDB transcription error.
- Regenerate merged YAML and rerun open schema, strict, reference, and term validation.

## Follow-up Checks

- Re-check the primary article behind PMID 13611202 for preparation details and exact organism/strain notation.
- Confirm whether Sodium ammonium phosphate has a stable ChEBI mapping before adding one manually.
- Re-run an ignored-inclusive exact search for `MEDIADB:236` after curation to ensure the source still has a single maintained owner.

## Additional Notes

The MediaDB formula page says the medium is not minimal, while CultureMech represents `medium_type` and `composition_type` as `DEFINED`. That is internally consistent: a chemically defined medium can be non-minimal.
