# YAML Record Review: thermoplasma_volcanium_medium__5a145f50

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoplasma_volcanium_medium__5a145f50.yaml`
- Started UTC: 2026-09-25T10:34:00Z
- Finished UTC: 2026-09-25T10:39:01Z
- Verdict: needs curation

## Target

- Reviewed generated direct DSMZ 398 record `CultureMech:001507`.
- Media term: `mediadive.medium:398`, `THERMOPLASMA VOLCANIUM MEDIUM`.
- Merge sources: direct `thermoplasma_volcanium_medium.yaml` and KOMODO `for_dsm_4301.yaml`.

## Validation

- Schema validation: passed; exited 0 with no diagnostics.
- Strict validation: passed; `/private/tmp/thermoplasma_volcanium_medium__5a145f50.strict.tsv` was header-only with 1 line and 0 error rows.
- Reference validation: passed; 0 checks were configured for this record.
- Term validation: passed; only the known `eutils`/`pkg_resources` deprecation warning was emitted.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged YAML.

## Identity and Grounding

- DSMZ Medium 398 and MediaDive medium 398 identify Thermoplasma Volcanium Medium.
- DSMZ 398 treats sulfur as an anaerobic-only addition and calls out DSM 4301 as a strain-specific meat-extract variant.
- An exact ignored-inclusive search found a second KOMODO DSMZ 398 generated record at `THERMOPLASMA_VOLCANIUM_MEDIUM.yaml` and the `for_dsm_4301.yaml` normalized source folded into the reviewed direct merge.

## Evidence

- `/private/tmp/DSMZ_Medium398.txt` lists the seven main non-water ingredients, sulfur for anaerobic media only, distilled water 1000 ml, acidification to about pH 2, and the pH 2 to 3 final check.
- `/private/tmp/mediadive_398.json` mirrors the DSMZ 398 ingredient list and three preparation steps.
- Local duplicate detection was rerun with `rg --no-ignore --hidden` against exact current source IDs and filenames, so ignored generated indexes were included.

## Completeness

- The generated record preserves the DSMZ ingredient amounts and preparation text.
- The source 1000 ml distilled-water row is missing.
- The anaerobic-only sulfur condition is kept only as an ingredient note.
- DSM 4301 is represented as a source duplicate even though DSMZ specifies 0.5 g/L meat extract for that strain.

## Findings

- The DSMZ 398 water basis is absent.
- Sulfur is grounded to `CHEBI:26833`, sulfur atom, instead of elemental sulfur.
- `for_dsm_4301` should be a strain-specific variant with 0.5 g/L meat extract rather than a source duplicate with the same ingredient signature.
- DSMZ 398 is split across this direct merge and the KOMODO generated `THERMOPLASMA_VOLCANIUM_MEDIUM.yaml`.

## Recommended Edits

- Preserve distilled water when importing DSMZ 398.
- Reground sulfur to elemental sulfur and keep the anaerobic-only sulfur condition as structured preparation or variant context.
- Convert the DSM 4301 KOMODO record to a Thermoplasma Volcanium variant that adds meat extract.
- Merge or retire the standalone KOMODO DSMZ 398 target after the direct and KOMODO normalized records agree.

## Follow-up Checks

- Rebuild the merged YAML and confirm DSMZ 398 has water, elemental sulfur, and a DSM 4301 variant rather than a source-duplicate synonym.
- Re-run schema, strict, reference, and term validation on the regenerated DSMZ 398 target.
- Re-run exact ignored-inclusive searches for `mediadive.medium:398`, `komodo.medium:398.1`, and `thermoplasma_volcanium_medium.yaml`.

## Additional Notes

None found.
