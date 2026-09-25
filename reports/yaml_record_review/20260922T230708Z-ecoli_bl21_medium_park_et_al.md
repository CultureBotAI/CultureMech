# YAML Record Review: ecoli_bl21_medium_park_et_al

- Repository: CultureMech
- Record: data/merge_yaml/merged/ecoli_bl21_medium_park_et_al.yaml
- Started UTC: 2026-09-22T23:05:05Z
- Finished UTC: 2026-09-22T23:07:08Z
- Verdict: needs curation

## Target

Generated MediaDB 277 record `CultureMech:007177`, named `ecoli_bl21_medium_park_et_al`.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation against `scripts/validate_strict.py`: passed; `/private/tmp/ecoli_bl21_medium_park_et_al.strict.tsv` contained the header row only.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the focused history validator targets standalone files under `history/`, not inline `MediaRecipe.curation_history` entries.

## Identity and Grounding

The record is still identifiable as MediaDB medium 277, "Ecoli bl21 medium; park et al". The source trail is weak: the note only links to the MediaDB home page and the curation history cites Mazumdar et al. 2014 as MediaDB's umbrella publication, while the medium name itself points to an underlying Park et al. formulation that is not cited.

The generated record is stale relative to `data/normalized_yaml/bacterial/ecoli_bl21_medium_park_et_al.yaml`: an August 2026 repair restored `Fe(III)dicitrate`, but this generated record still has the truncated label `'Fe(III`.

Several components remain ungrounded or under-grounded for a defined medium, including Fe(III)dicitrate, beta-D-glucose in the generated copy, ammonium phosphate, sodium EDTA, and zinc acetate.

## Evidence

The local normalized record says the importer pulled MediaDB medium 277 from the Institute for Systems Biology MediaDB and records a name-repair event that matched the truncated Fe(III) prefix against MediaDB 277's own compound list in `media_database.07Oct2015.sql`.

The generated file still has fourteen millimolar ingredient rows copied from that MediaDB import. It also has three generic generated preparation steps: dissolve all ingredients, adjust pH "if specified in original formulation", and filter-sterilize with a 0.22 um filter.

## Completeness

The medium is defined and contains all fourteen imported millimolar rows, but it is not source-faithful enough for review. Missing pieces include the actual Park et al. citation, explicit E. coli BL21 target metadata, exact hydration or salt states for the ambiguous salts, and any source-backed pH or sterilization instructions.

## Findings

- The generated Fe ingredient label is truncated to `'Fe(III`; the normalized source has already repaired it to `Fe(III)dicitrate`.
- beta-D-glucose lost the `CHEBI:15903` grounding that is present in the normalized source.
- Fe(III)dicitrate, ammonium phosphate, sodium EDTA, and zinc acetate have no primary ChEBI term.
- The preparation steps are generic and partly unsupported: `Adjust pH if specified in original formulation` encodes uncertainty as an instruction, and the 0.22 um filtration step is not traceable to the visible MediaDB provenance.
- Target organism metadata for E. coli BL21 is absent.
- The record lacks a specific Park et al. source citation.

## Recommended Edits

- Regenerate this record from the repaired normalized MediaDB 277 YAML so `Fe(III)dicitrate` and the beta-D-glucose grounding survive in `data/merge_yaml/merged`.
- Re-ground Fe(III)dicitrate, ammonium phosphate, sodium EDTA, and zinc acetate to exact ChEBI terms, with salt and hydration state checked against the raw MediaDB compound list.
- Replace placeholder preparation steps with only source-backed instructions; drop the conditional pH step unless the source specifies a pH.
- Add E. coli BL21 as structured target-organism metadata if the source confirms that target.
- Attach the underlying Park et al. citation or record that MediaDB does not expose it.

## Follow-up Checks

- Re-run open, strict, reference, and term validators after rebuilding.
- Compare the rebuilt record against MediaDB 277, especially the Fe(III)dicitrate and zinc/EDTA rows.
- Search with ignored files included for stale truncated `'Fe(III` labels after regenerating MediaDB outputs.

## Additional Notes

An ignored-inclusive `find` for `media_database.07Oct2015.sql` and MediaDB-related local files found import and repair code but did not find the raw SQL dump in this checkout.
