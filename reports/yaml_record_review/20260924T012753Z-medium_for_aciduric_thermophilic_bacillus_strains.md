# YAML Record Review: medium_for_aciduric_thermophilic_bacillus_strains
- Repository: CultureMech
- Record: `data/merge_yaml/merged/medium_for_aciduric_thermophilic_bacillus_strains.yaml`
- Started UTC: 2026-09-24T01:27:05Z
- Finished UTC: 2026-09-24T01:27:53Z
- Verdict: needs curation

## Target
- Reviewed generated merged record `CultureMech:000277` / `medium_for_aciduric_thermophilic_bacillus_strains`.
- Current generated record has primary source term `mediadive.medium:674`, pH 4.3, `SOLID_AGAR`, and 9 ingredient rows.
- Exact source-ID and owner checks included ignored files. `find` found both `data/normalized_yaml/archaea/medium_for_aciduric_thermophilic_bacillus_strains.yaml` and `data/normalized_yaml/bacterial/medium_for_aciduric_thermophilic_bacillus_strains.yaml`; exact `mediadive.medium:674` and `komodo.medium:674` scans found those two owners, the generated canonical record for the DSMZ ID, and normalized index entries.
- The generated merge collapsed the DSMZ owner in `archaea` and the KOMODO owner in `bacterial`, both of which have the same normalized basename.

## Validation
- Open schema validation: passed with no issues reported by `linkml-validate`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file and reported 0 ERROR rows.
- Reference validation: passed; the validator reported 0 checks and no failures.
- Term validation: passed.
- Embedded history validation: Not checked; the available history validator targets standalone `history/` files rather than embedded `MediaRecipe.curation_history` entries.

## Identity and Grounding
- The live DSMZ 674 formula and the KOMODO 674 copy have the same ingredient concentrations.
- The generated record keeps the DSMZ `mediadive.medium:674` term and correctly preserves the DSMZ preparation steps.
- The generated record does not preserve `komodo.medium:674` in `media_term`, `synonyms`, or any other source-ID field even though the merge history records two merged sources.
- The `merged_from` list contains `medium_for_aciduric_thermophilic_bacillus_strains` twice, so it cannot distinguish the archaea DSMZ owner from the bacterial KOMODO owner.

## Evidence
- The live MediaDive REST record for DSMZ Medium 674 identifies the source formula as `MEDIUM FOR ACIDURIC, THERMOPHILIC BACILLUS STRAINS`.
- Live DSMZ 674 uses 500 ml Solution A and 500 ml Solution B in a 1000 ml main solution.
- Solution A contains (NH4)2SO4 0.4 g/L, MgSO4 x 7 H2O 1 g/L, CaCl2 x 2 H2O 0.5 g/L, KH2PO4 6 g/L, Yeast extract 2 g/L, Tryptone 2 g/L, Glucose 2 g/L, Starch 2 g/L, and Distilled water 500 ml. Solution B contains Agar 40 g/L and Distilled water 500 ml.
- The generated CultureMech concentrations match those live DSMZ 674 source amounts, and it preserves the source instructions to sterilize Solutions A and B separately, pour A into B after cooling, and adjust pH to 4.3.

## Completeness
- The generated record keeps all 9 normalized owner non-water ingredient rows.
- The generated record has pH, agar state, both DSMZ preparation steps, broad applications, the DSMZ source term, CHEBI grounding for all defined-chemical rows, merge provenance, and curation history.
- The generated record loses the KOMODO source identifier and has ambiguous duplicate `merged_from` entries because both source files share a basename.

## Findings
- Source provenance for `komodo.medium:674` is lost in the generated canonical record; an exact generated-file scan no longer finds that source ID.
- `merged_from` is ambiguous because both merged source files had the same basename in different normalized category directories.
- The canonical record carries primary `category: archaea` even though the DSMZ source title is for aciduric, thermophilic Bacillus strains and the duplicate KOMODO owner is categorized as bacterial.

## Recommended Edits
- Preserve category-qualified source paths or source IDs when merging identically named normalized records from different category directories.
- Add `komodo.medium:674` as a synonym/source on the generated canonical record or ensure merge provenance exposes it in another structured field.
- Review the `archaea` category assignment for DSMZ Medium 674 and the generated primary category; prefer `bacterial` unless source evidence supports keeping an archaeal category.

## Follow-up Checks
- Re-run open schema, strict, reference, and term validation on any regenerated merged record.
- Repeat exact DSMZ and KOMODO source-ID scans with ignored files included after merge-provenance repair.
- Compare the regenerated record against live DSMZ 674 to verify preparation steps still survive the merge.

## Additional Notes
- Empty optional fields were not treated as defects.
- No GitHub issues, pull requests, or comments were opened as part of this generated-record review.
