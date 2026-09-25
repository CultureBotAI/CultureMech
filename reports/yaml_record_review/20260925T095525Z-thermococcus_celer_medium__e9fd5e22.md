# YAML Record Review: THERMOCOCCUS CELER medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermococcus_celer_medium__e9fd5e22.yaml`
- Started UTC: 2026-09-25T09:53:30Z
- Finished UTC: 2026-09-25T09:55:25Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:004669`
- Merge fingerprint: `e9fd5e22ae3c9d8b72a2644407d69184dea2d3a19defc12eb8fb009ea1225270`
- Merged sources: `KOMODO_266_THERMOCOCCUS_CELER_medium`, `thermococcus_celer_medium`
- Media term: `komodo.medium:266`
- Source medium: KOMODO Medium 266 / DSMZ Medium 266, "THERMOCOCCUS CELER MEDIUM"

## Validation

- LinkML schema validation: Passed with `No issues found`.
- Strict schema validation: Passed; 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: Passed; 0 reference checks and no errors.
- Term validation: Passed. The only stderr output was the expected `eutils` warning about `pkg_resources`.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not the embedded `MediaRecipe.curation_history` array in this merged YAML.

## Identity and Grounding

- The KOMODO branch explicitly cites `mediadive.medium:266` and has been merged with the direct DSMZ Medium 266 import, which is the right source-duplicate grouping.
- Ingredient identities and amounts match the MediaDive REST and DSMZ PDF recipe for Medium 266: 40 g/L NaCl, 1 mg/L resazurin, 2 g/L yeast extract, 5 g/L powdered sulfur, and the listed Modified Brock's salts.
- The generated record keeps the KOMODO-centered `media_term`; the direct `mediadive.medium:266` identifier remains only inside notes and merge provenance.
- `parent_media.path` points to `data/normalized_yaml/bacterial/thermococcus_celer_medium.yaml`, but the exact ignored-file search found the direct DSMZ parent at `data/normalized_yaml/archaea/thermococcus_celer_medium.yaml`.

## Evidence

- MediaDive REST `266` and the DSMZ Medium 266 PDF agree on the ingredient table and pH 5.8.
- The direct normalized DSMZ file has preparation steps for final pH adjustment and anaerobic preparation under 100% nitrogen, including separately prepared yeast extract, sulfur, and Na2S x 9 H2O additions.
- The generated KOMODO/DSMZ merge output has no `preparation_steps`, showing that the source duplicate merge kept KOMODO's ingredient-only surface and dropped DSMZ's protocol text.
- Exact ignored-file search found only the KOMODO 266 and direct DSMZ Medium 266 normalized records for `mediadive.medium:266`/`komodo.medium:266`; both are listed in `merged_from`.

## Completeness

- Required scalar fields, ingredient concentrations, `parent_media`, duplicate provenance, curation history, and `merged_from` are present.
- No organisms or strain links are expected for this medium-level import.
- DSMZ preparation instructions are incomplete in the merged output because they were present in the DSMZ parent and lost during source duplicate selection.

## Findings

- Medium - The generated merge drops DSMZ Medium 266 preparation steps, including the explicit anaerobic nitrogen workflow and separate stock handling.
- Medium - `parent_media.path` carries a stale `data/normalized_yaml/bacterial/...` path for an archaeal DSMZ parent that actually resides under `data/normalized_yaml/archaea/...`.
- Low - The canonical `media_term` after merging still points to `komodo.medium:266`; the direct DSMZ identifier survives only as note text and merge provenance.

## Recommended Edits

- Fix the KOMODO/DSMZ source-duplicate merge path so source duplicate children do not discard preparation steps that are present only on the direct DSMZ parent.
- Correct the KOMODO normalized record's `parent_media.path` to `data/normalized_yaml/archaea/thermococcus_celer_medium.yaml`.
- Prefer carrying `mediadive.medium:266` as a structured term or secondary provenance field when a KOMODO record is resolved to an exact DSMZ source.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated KOMODO/DSMZ Medium 266 branch.
- Re-run exact ignored-file search for `KOMODO_266_THERMOCOCCUS_CELER_medium`, `mediadive.medium:266`, `DSMZ_Medium266.pdf`, and `CultureMech:001365` to confirm the parent path and merge membership.
- Compare the regenerated preparation text against the DSMZ Medium 266 PDF and MediaDive REST `266`.

## Additional Notes

None found.
