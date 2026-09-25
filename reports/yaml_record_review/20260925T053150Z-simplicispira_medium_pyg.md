# YAML Record Review: simplicispira_medium_pyg

- Repository: CultureMech
- Record: data/merge_yaml/merged/simplicispira_medium_pyg.yaml
- Started UTC: 2026-09-25T05:31:50Z
- Finished UTC: 2026-09-25T05:31:50Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:001088`, `simplicispira_medium_pyg`, from `data/merge_yaml/merged/simplicispira_medium_pyg.yaml`.

The target record is a direct MediaDive/DSMZ import for DSMZ medium 1607, `SIMPLICISPIRA MEDIUM (PYG)`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to DSMZ medium 1607.

No same-source duplicate was found in the sorted generated YAML list.

## Evidence

The DSMZ medium 1607 PDF and MediaDive REST payload both define the recipe as 3.0 g Bacto peptone, 5.0 g yeast extract, 10.0 ml glycerol, 15.0 g agar, and 1000.0 ml distilled water.

Both sources specify adjustment to pH 7.2.

## Completeness

The generated record preserves Bacto peptone, yeast extract, agar, and pH 7.2.

The generated record converts 10.0 ml glycerol to `10 G_PER_L`.

The required 1000 ml distilled water row is absent from the generated ingredients.

## Findings

MediaDive milliliter units were normalized into `G_PER_L` for glycerol.

The final distilled-water solvent row was dropped.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/simplicispira_medium_pyg.yaml` to preserve 10 ml glycerol with a volume unit.

Add the 1000 ml distilled water row from DSMZ medium 1607.

Regenerate the merged YAML after repairing the normalized source.

## Follow-up Checks

Confirm the regenerated record has 10 ml/L glycerol, not 10 g/L.

Confirm the regenerated record has 1000 ml/L distilled water.

Confirm pH 7.2 and solid agar physical state are preserved.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
