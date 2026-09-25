# YAML Record Review: petri_cellulose_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/petri_cellulose_medium.yaml
- Started UTC: 2026-09-24T20:35:19Z
- Finished UTC: 2026-09-24T20:35:19Z
- Verdict: needs curation

## Target

Generated bacterial MediaRecipe `CultureMech:007959`, `petri_cellulose_medium`, from the maintained TOGO/NBRC owner `data/normalized_yaml/bacterial/petri_cellulose_medium.yaml`.

The record represents TOGO M1421 / NBRC medium 18, Petri-Cellulose Medium. The generated recipe contains distilled water, four mineral salts, and an empty `Cellulose*` solution stub at 10 g/L.

## Validation

- Open LinkML validation: Passed with no issues.
- Strict validator: Passed; `/private/tmp/petri_cellulose_medium.strict.tsv` was header-only, so there were 0 strict errors.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The source identity is internally consistent: TOGO M1421 names NBRC `NBRC_M18`, and the NBRC medium 18 page is Petri-Cellulose Medium.

An exact ignored-inclusive search found no other maintained owner or generated record for `TOGO:M1421`, NBRC `NO=18`, or `NBRC_M18`.

## Evidence

TOGO M1421 and the NBRC medium 18 page both support 10 g Cellulose, 0.4 g Ca(NO3)2 x 4 H2O, 0.15 g K2HPO4, 0.15 g MgSO4 x 7 H2O, 0.06 g KCl, 1 L distilled water, and pH 7.0.

The NBRC source footnote specifies the cellulose as Whatman No. 1 filter paper pieces, 5 mm square. This is an ingredient note, not a stock solution definition.

The inorganic salts have appropriate CHEBI groundings; cellulose is currently ungrounded, which is acceptable until the filter-paper qualifier is curated deliberately.

## Completeness

The four mineral salts and the source identity are preserved, but the maintained owner and generated record mis-scope the cellulose source row and omit pH 7.0.

The source water row is also represented as `1 G_PER_L`, although TOGO M1421 and NBRC medium 18 specify a 1 L volume.

## Findings

1. Needs curation: `Cellulose*` is encoded as an empty `solutions` entry. NBRC and TOGO list 10 g cellulose directly in the medium, with a footnote defining it as Whatman No. 1 filter paper pieces.
2. Needs curation: `ph_value: 7.0` is missing even though both TOGO M1421 and NBRC medium 18 specify pH 7.0.
3. Needs curation: `Distilled water` is encoded as `1 G_PER_L`; the source specifies 1 L.

## Recommended Edits

1. Move `Cellulose*` back to the final `ingredients` list at 10 g/L and preserve the filter-paper footnote as an ingredient note.
2. Add `ph_value: 7.0`.
3. Encode the distilled water row as a 1 L source volume rather than `1 G_PER_L`.

## Follow-up Checks

1. Re-run open, strict, reference, and term validation on the repaired maintained owner and regenerated merged record.
2. Repeat an exact ignored-inclusive search for `TOGO:M1421`, `NBRC_M18`, `NO=18`, and `CultureMech:007959` to confirm no duplicate Petri-Cellulose owner appears.

## Additional Notes

The exact ignored-inclusive duplicate search covered `data`, `src`, and `scripts` for `TOGO:M1421`, `NBRC_M18`, `NO=18`, `CultureMech:007959`, and `petri_cellulose_medium`.
