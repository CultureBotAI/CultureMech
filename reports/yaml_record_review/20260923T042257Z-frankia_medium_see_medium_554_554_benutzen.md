# YAML Record Review: frankia_medium_see_medium_554_554_benutzen

- Repository: CultureMech
- Record: data/merge_yaml/merged/frankia_medium_see_medium_554_554_benutzen.yaml
- Started UTC: 2026-09-23T04:20:45Z
- Finished UTC: 2026-09-23T04:22:57Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:001687` / `frankia_medium_see_medium_554_554_benutzen`, DSMZ Medium 552.
- Compared it with maintained source `data/normalized_yaml/bacterial/frankia_medium_see_medium_554_554_benutzen.yaml`.
- Cross-checked DSMZ Medium 552 through MediaDive REST and the linked DSMZ Medium 552 PDF; inspected DSMZ Medium 554 only to disambiguate the title redirect.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass with 0 error rows.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- `mediadive.medium:552` correctly identifies DSMZ Medium 552, whose source title names FRANKIA MEDIUM and points readers to medium 554.
- Medium 552 should stay distinct from DSMZ Medium 554 / N-Z-AMINE-MEDIUM because the inspected DSMZ PDFs differ at least in final pH: pH 7.0 for 552 and pH 7.2 for 554.
- The generated and normalized `physical_state: LIQUID` is not supported by the DSMZ 552 PDF because the authoritative PDF includes agar.
- The `Starch` row is only broadly grounded to CHEBI starch and drops MediaDive's soluble-starch source attribute.
- Yeast extract and N-Z amine are ungrounded complex ingredients; that is acceptable pending a suitable exact vocabulary term.

## Evidence

- MediaDive REST for medium 552 matches the generated ingredients for glucose, starch, yeast extract, N-Z amine, and CaCO3 at 10, 20, 5, 5, and 1 g/L, and it reports pH 7.0.
- The linked DSMZ Medium 552 PDF includes those same rows but also lists agar at 15 g per 1000 ml, making the current liquid state and missing-agar formula incomplete relative to the PDF named in `notes`.
- The generated preparation step preserves the DSMZ 552 NaOH pH-adjustment instruction.
- The generated record correctly did not exact-merge with DSMZ 554, which has the related N-Z-AMINE-MEDIUM label and pH 7.2 source recipe.

## Completeness

- The generated record is incomplete for DSMZ 552 because the source PDF's agar component is missing.
- Physical state is incomplete or stale because DSMZ 552 should be represented as an agar medium when the PDF is treated as authoritative.
- Exact ignored-inclusive lookup for `mediadive.medium:552`, `CultureMech:001687`, and the DSMZ Medium 552 PDF URL covered `data/normalized_yaml` and `data/merge_yaml/merged`; it found this generated record and a single maintained DSMZ 552 owner in `data/normalized_yaml/bacterial`.
- Empty optional organism, variant, reference, and discussion slots are acceptable for this imported DSMZ formulation.

## Findings

- Major: DSMZ Medium 552 is missing the 15 g/L agar row present in the linked DSMZ PDF; the fix belongs in `data/normalized_yaml/bacterial/frankia_medium_see_medium_554_554_benutzen.yaml` or the MediaDive/DSMZ importer input if that source is regenerated.
- Major: `physical_state: LIQUID` conflicts with the agar-containing DSMZ Medium 552 PDF and should be recast after the agar row is restored.
- Minor: the source-specific soluble-starch form is lost in the `Starch` ingredient row even though both the DSMZ PDF and MediaDive REST indicate soluble starch.

## Recommended Edits

- Add DSMZ Medium 552's 15 g/L agar component to `data/normalized_yaml/bacterial/frankia_medium_see_medium_554_554_benutzen.yaml`.
- Change the normalized DSMZ 552 physical state from `LIQUID` to the agar state used elsewhere in the corpus after restoring agar.
- Preserve the soluble-starch supplied form in the starch ingredient row.
- Regenerate `data/merge_yaml/merged/frankia_medium_see_medium_554_554_benutzen.yaml` after normalized curation.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated DSMZ 552 YAML.
- Confirm the generated DSMZ 552 record contains agar at 15 g/L, keeps pH 7.0, and remains separate from DSMZ 554 / `n_z_amine_medium`.
- Confirm the starch row carries soluble-starch source context.
- Confirm embedded curation-history timestamps are parseable after regeneration.

## Additional Notes

- MediaDive REST for medium 552 omits the agar row that appears in the linked DSMZ PDF. Because this record stores the DSMZ PDF as its source link, this review treats the PDF omission as a normalized import defect rather than a generated merge defect.
