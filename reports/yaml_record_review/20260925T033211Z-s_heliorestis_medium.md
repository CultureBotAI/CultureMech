# YAML Record Review: s_heliorestis_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/s_heliorestis_medium.yaml`
- Started UTC: `2026-09-25T03:32:11Z`
- Finished UTC: `2026-09-25T03:32:11Z`
- Verdict: needs curation

## Target

Reviewed the generated merge record for `s_heliorestis_medium`, a two-source merge of:

- `data/normalized_yaml/bacterial/KOMODO_1381_S_HELIORESTIS_medium.yaml`
- `data/normalized_yaml/bacterial/s_heliorestis_medium.yaml`

The generated record is canonicalized to the KOMODO Medium 1381 copy and merges it with the direct DSMZ/MediaDive Medium 1381 source. KOMODO explicitly cites DSMZ 1381 and the two local sources are true source duplicates, but both carry the same flattened Trace elements stock and sulfide error.

## Validation

- Open schema validation: Passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: Passed; `scripts/validate_strict.py` exited 0 and reported 0 total error rows.
- Reference validation: Passed; `linkml-reference-validator` ran 0 checks and reported all checks passed.
- Term validation: Passed; `linkml-term-validator` exited 0 after the expected `eutils` / `pkg_resources` warning.
- Embedded `curation_history`: Not checked. `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The KOMODO 1381 and DSMZ/MediaDive 1381 sources represent the same DSMZ `1/2 S-degree HELIORESTIS MEDIUM` formula and are appropriate source duplicates.

The generated record should not use the KOMODO `? S? HELIORESTIS medium` label as the canonical human-readable name. That spelling is a lossy import of DSMZ's original half-strength `S-degree` title and should be normalized or canonicalized from the DSMZ source.

## Evidence

DSMZ Medium 1381 lists pH 9.0-9.5 and final volume 1000 ml. The parent recipe has 1 ml EDTA 1%, 0.5 g `KH2PO4`, 0.5 g `NH4Cl`, 1.63 g Bicine, 0.2 g `MgSO4 x 7 H2O`, 0.075 g `CaCl2`, 2.5 g `Na2CO3`, 2.5 g `NaHCO3`, 1 g Na-acetate, 0.1 g Yeast extract, 0.25 g `Na2S x 9 H2O`, 1 g Na-pyruvate, 1 ml Trace elements, 20 ug Vitamin B12, and 1000 ml distilled water.

The DSMZ Trace elements stock is copied from Medium 1147 and contains, per liter, 5.2 g EDTA, 190 mg `CoCl2 x 6 H2O`, 0.1 g `MnCl2 x 4 H2O`, 1.5 g `FeCl2 x 4 H2O`, 6 mg `H3BO3`, 17 mg `CuCl2 x 2 H2O`, 188 mg `Na2MoO4 x 2 H2O`, 25 mg `NiCl2 x 6 H2O`, 70 mg `ZnCl2`, 30 mg `VOSO4 x 2 H2O`, 2 mg `Na2WO4 x 2 H2O`, 2 mg `NaHSeO3`, and 1000 ml deionized water. DSMZ instructs preparation under N2 gas and post-autoclave addition of Vitamin B12, `NaHCO3`, `Na2CO3`, and sulfide as single sterile stock solutions.

## Completeness

The generated record preserves pH 9.0-9.5 and most direct gram-scale DSMZ parent ingredients.

It loses or corrupts these details:

- The 1 ml/L Trace elements aliquot is absent.
- Every Trace elements stock component is flattened into the parent at full stock strength.
- The parent EDTA aliquot and Trace elements EDTA stock are summed into `5.21 G_PER_L`.
- DSMZ lists 0.25 g `Na2S x 9 H2O`, but the generated record has `0.5 G_PER_L`.
- Parent distilled water and Trace elements deionized water are absent.
- Post-autoclave sterile stock additions are absent from the generated preparation metadata.
- The canonical name is based on a garbled KOMODO label.

## Findings

- `needs curation`: The Trace elements stock was flattened into the parent recipe. DSMZ calls for 1 ml/L Trace elements, but the generated parent contains all trace-metal ingredients at their 1 L stock concentrations.
- `needs curation`: EDTA from two different scopes was merged into one parent value. The source has 1 ml of 1% EDTA in the main solution and 5.2 g EDTA in the 1 L Trace elements stock; the generated file sums them as `5.21 G_PER_L`.
- `needs curation`: The sulfide amount disagrees with DSMZ. DSMZ Medium 1381 lists 0.25 g `Na2S x 9 H2O`, while the generated record reports `0.5 G_PER_L`.
- `needs curation`: The parent 1 ml/L Trace elements aliquot and both water rows are absent, so the generated record cannot recover the intended 1000-fold dilution of the trace stock.
- `needs curation`: DSMZ says Vitamin B12, `NaHCO3`, `Na2CO3`, and sulfide are added as single sterile stock solutions after autoclaving; the generated merge loses that preparation step.
- `pass with minor issues`: `NiCl2 x 6 H2O` is grounded to CHEBI:34887, `nickel dichloride`; that identifier is too broad for a hexahydrate-labeled row and should either use a hydrate-specific term if one exists or be left ungrounded.
- `pass with minor issues`: The KOMODO/DSMZ duplicate relationship is valid, but the canonical label should come from DSMZ rather than the garbled KOMODO text.

## Recommended Edits

- Do not hand-edit `data/merge_yaml/merged/s_heliorestis_medium.yaml`; fix the normalized DSMZ/MediaDive and KOMODO inputs, then rerun the merge.
- Preserve DSMZ 1381 Trace elements as a nested stock with a 1 ml parent aliquot.
- Keep the parent EDTA and Trace elements EDTA rows scoped separately instead of summing them.
- Correct `Na2S x 9 H2O` to the DSMZ 0.25 g/L source amount unless a separate stock-concentration field explains the current 0.5 g/L value.
- Restore parent distilled water and Trace elements deionized water in their source scopes.
- Preserve the N2 preparation atmosphere and post-autoclave sterile-stock additions for Vitamin B12, `NaHCO3`, `Na2CO3`, and sulfide.
- Correct or remove the `NiCl2 x 6 H2O` grounding to anhydrous nickel dichloride.
- Canonicalize the generated name from the DSMZ `1/2 S-degree HELIORESTIS MEDIUM` label, not from the KOMODO `? S?` import artifact.

## Follow-up Checks

- Rerun open schema, strict, reference, and term validation on both edited normalized source files.
- Regenerate `data/merge_yaml/merged/s_heliorestis_medium.yaml` and verify that Trace elements no longer appears as direct parent trace-metal rows.
- Verify that EDTA exists separately as a parent EDTA aliquot and a Trace elements stock row.
- Verify that the generated parent has `Na2S x 9 H2O` at the source 0.25 g/L value.
- Run an exact ignored-file-inclusive search for `KOMODO_1381_S_HELIORESTIS_medium`, `mediadive.medium:1381`, and `s_heliorestis_medium` before changing duplicate links.

## Additional Notes

The absence of `target_organisms` was not treated as a defect for this generated record review. The Trace elements stock is shared with DSMZ Medium 1147; any fix for stock flattening here should be checked against RV5 Medium as well.
