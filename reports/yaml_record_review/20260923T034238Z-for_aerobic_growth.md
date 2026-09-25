# YAML Record Review: for_aerobic_growth

- Repository: CultureMech
- Record: data/merge_yaml/merged/for_aerobic_growth.yaml
- Started UTC: 2026-09-23T03:41:13Z
- Finished UTC: 2026-09-23T03:42:38Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:005065` / `for_aerobic_growth`, the KOMODO Medium 350.1 record for DSMZ Medium 350's aerobic-growth variant.
- Compared it with sibling KOMODO Medium 350 / `data/normalized_yaml/bacterial/KOMODO_350_CELLULOMONAS_FERMENTANS_medium.yaml`.
- Cross-checked both KOMODO sources against the DSMZ Medium 350 PDF and the MediaDive REST payload for medium 350.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass; 0 total ERROR rows in `/private/tmp/for_aerobic_growth.strict.tsv`.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- The KOMODO identity is internally coherent: `komodo.medium:350.1` and the record label both identify the "For aerobic growth" variant of DSMZ Medium 350.
- The generated record incorrectly treats KOMODO 350.1 as an exact duplicate of KOMODO 350 even though DSMZ defines 350.1 as a modification of the base anaerobic recipe.
- Defined small-molecule ingredients are grounded appropriately.
- Yeast extract is ungrounded; that is acceptable as a complex ingredient.
- The variable NaOH pH-adjuster row is grounded, but it is derived from the DSMZ preparation note rather than the ingredient table.

## Evidence

- DSMZ 350 and MediaDive 350 assert the base recipe with K2HPO4, KH2PO4, (NH4)2SO4, MgCl2 x 6 H2O, CaCl2 x 2 H2O, FeSO4 x 7 H2O, Yeast extract, a 5 g/L Cellobiose or Cellulose substrate choice, NaHCO3, Resazurin, L-Cysteine HCl x H2O, and Distilled water.
- DSMZ explicitly says aerobic growth omits Resazurin and Cysteine.
- The generated `for_aerobic_growth` record still includes both Resazurin and L-Cysteine HCl x H2O, so it is the anaerobic base formula while labeled as the aerobic variant.
- DSMZ and MediaDive also include preparation steps for pH adjustment to 7.4 with 8 M NaOH and anaerobic handling with separately sterilized Cellobiose, NaHCO3, and cysteine; the generated record has only a variable NaOH row and no `preparation_steps`.
- The DSMZ Cellobiose or Cellulose (MN 300) substrate alternative is collapsed to Cellobiose only.

## Completeness

- The generated recipe is compositionally complete for the DSMZ 350 base recipe except for the Cellulose alternative and Distilled water.
- It is incomplete and over-specified for the aerobic variant because it keeps anaerobic indicator/reducer rows that should be omitted.
- Source preparation instructions are absent.

## Findings

- Needs curation: the aerobic KOMODO 350.1 variant was merged as an exact duplicate of KOMODO 350 and was not curated as a variant that omits Resazurin and L-Cysteine HCl x H2O.
- Needs curation: DSMZ preparation text is missing, including pH adjustment to 7.4 with 8 M NaOH and anaerobic stock-handling instructions for the base recipe.
- Needs curation: the Cellobiose or Cellulose (MN 300) alternative is lost.
- Minor issue: the KOMODO import's first embedded curation-history timestamp is malformed as `2026-01-27T01:15:02.fZ`.

## Recommended Edits

- Split KOMODO 350 and KOMODO 350.1 semantically: keep DSMZ Medium 350 as the base anaerobic recipe and represent `for_aerobic_growth` as a variant that omits Resazurin and L-Cysteine HCl x H2O.
- Restore DSMZ preparation steps to the base recipe and attach the aerobic-omission instruction to the aerobic variant.
- Preserve the 5 g/L Cellobiose versus Cellulose (MN 300) substrate choice rather than flattening it to only Cellobiose.
- Regenerate `data/merge_yaml/merged/for_aerobic_growth.yaml` after variant curation.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated KOMODO 350.1 YAML.
- Confirm the aerobic variant no longer contains Resazurin or L-Cysteine HCl x H2O.
- Confirm KOMODO 350 and 350.1 no longer collapse into a same-fingerprint exact duplicate merge.
- Confirm `ph_value: 7.4` is retained and embedded curation-history timestamps are parseable after regeneration.

## Additional Notes

- The current record is faithful to the enriched KOMODO 350/350.1 duplicate data in `data/normalized_yaml`, so the repair belongs in normalized KOMODO curation or the DSMZ resolver rather than in generated YAML alone.
