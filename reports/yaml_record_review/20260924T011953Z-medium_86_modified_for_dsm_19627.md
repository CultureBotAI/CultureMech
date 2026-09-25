# YAML Record Review: medium_86_modified_for_dsm_19627
- Repository: CultureMech
- Record: `data/merge_yaml/merged/medium_86_modified_for_dsm_19627.yaml`
- Started UTC: 2026-09-24T01:19:24Z
- Finished UTC: 2026-09-24T01:19:53Z
- Verdict: needs curation

## Target
- Reviewed generated merged record `CultureMech:006680` / `medium_86_modified_for_dsm_19627`.
- Current generated record has source term `komodo.medium:86_19627`, DSMZ source note `mediadive.medium:86`, pH 9.0, `LIQUID`, and 17 ingredient rows.
- Exact source-ID and owner checks included ignored files. `find data/normalized_yaml -name 'medium_86_modified_for_dsm_19627*.yaml' -print` found only `data/normalized_yaml/bacterial/medium_86_modified_for_dsm_19627.yaml`; the exact `komodo.medium:86_19627` scan found only that owner, the generated record, and normalized index entries.
- The generated record is a one-source merge of its normalized owner.

## Validation
- Open schema validation: passed with no issues reported by `linkml-validate`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file and reported 0 ERROR rows.
- Reference validation: passed; the validator reported 0 checks and no failures.
- Term validation: passed.
- Embedded history validation: Not checked; the available history validator targets standalone `history/` files rather than embedded `MediaRecipe.curation_history` entries.

## Identity and Grounding
- The normalized owner is the only exact owner for `medium_86_modified_for_dsm_19627` under `data/normalized_yaml`.
- The generated `media_term` preserves the KOMODO identifier `komodo.medium:86_19627` and original name `MEDIUM 86 MODIFIED FOR DSM 19627`.
- The live MediaDive page for DSMZ 86 lists DSM 19627, so the source record points at a DSMZ medium that is linked to the encoded strain.
- `KNO3` and `NaNO3` have correct primary CHEBI terms but still keep legacy `mediaingredientmech_term` links to `MediaIngredientMech:000170` and `MediaIngredientMech:000171`, while the surrounding rows use `mediaingredientmech_chebi_term`.

## Evidence
- The live MediaDive REST record for DSMZ Medium 86 identifies the source formula as `CASTENHOLZ MEDIUM`, pH 8.2, and a 1000 ml main solution.
- Live DSMZ 86 lists Nitrilotriacetic acid 0.1 g, CaSO4 x 2 H2O 0.06 g, MgSO4 x 7 H2O 0.1 g, NaCl 0.008 g, KNO3 0.103 g, NaNO3 0.689 g, Na2HPO4 x 2 H2O 0.14 g, FeCl3 x 6 H2O 0.00047 g, MnSO4 x H2O 0.0022 g, ZnSO4 x 7 H2O 0.0005 g, H3BO3 0.0005 g, CuSO4 x 5 H2O 0.000025 g, Na2MoO4 x 2 H2O 0.000025 g, CoCl2 x 6 H2O 0.000046 g, Tryptone 1 g, Yeast extract 1 g, and Distilled water 1000 ml.
- The generated CultureMech concentrations match the live DSMZ 86 source amounts after converting DSMZ milligram and microgram entries to g/L.
- The KOMODO pH 9.0 and `pH buffer: Na-sesquicarbonate` modification differs from DSMZ 86, which adjusts pH to 8.2 with NaOH.

## Completeness
- The generated record keeps the 16 DSMZ 86 non-water ingredients and adds the note-derived `Na` placeholder for the KOMODO `pH buffer: Na-sesquicarbonate` note.
- The generated record has pH, liquid state, broad applications, source notes, the KOMODO source term, CHEBI grounding for the chemically specific rows, merge provenance, and curation history.
- No standalone citation object is present. Evidence currently lives in free-text notes and curation history.

## Findings
- `KNO3` and `NaNO3` are only partially migrated to CHEBI keying. Their primary terms are `CHEBI:63043` and `CHEBI:63005`, but their secondary groundings remain legacy `mediaingredientmech_term` values rather than CHEBI-keyed `mediaingredientmech_chebi_term` values.
- The note-derived `Na` ingredient is not chemically specific. It appears to have been extracted from `pH buffer: Na-sesquicarbonate`, then defaulted to a variable concentration, which records elemental sodium rather than the sodium sesquicarbonate buffer named in the note.

## Recommended Edits
- Replace the KNO3 and NaNO3 legacy `mediaingredientmech_term` mappings with `mediaingredientmech_chebi_term` mappings keyed to `CHEBI:63043` and `CHEBI:63005`, or remove the secondary links if the primary CHEBI term is now the canonical grounding.
- Remove the bare `Na` placeholder unless the pH-buffer note can be converted to a specific sodium sesquicarbonate ingredient with an evidence-backed concentration or volume.
- Re-check the KOMODO 86_19627 source row before retaining pH 9.0, because the copied DSMZ 86 formula itself is pH 8.2 adjusted with NaOH.

## Follow-up Checks
- Re-run open schema, strict, reference, and term validation on any regenerated merged record.
- Repeat exact owner and source-ID scans with ignored files included after curation.
- Compare the final pH-buffer handling against both live DSMZ 86 and the KOMODO source row.

## Additional Notes
- Empty optional fields were not treated as defects.
- No GitHub issues, pull requests, or comments were opened as part of this generated-record review.
