# YAML Record Review: desulfobacter_medium_for_dsm_10631

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfobacter_medium_for_dsm_10631.yaml`
- Started UTC: 2026-09-22T17:58:50Z
- Finished UTC: 2026-09-22T17:58:50Z
- Verdict: needs curation

## Target

Generated bacterial `desulfobacter_medium_for_dsm_10631` record for TOGO M2546, a DSMZ Medium 193 variant for DSM 10631.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The generated record is grounded to TOGO M2546 and points back to DSMZ Medium 193. The current DSMZ 193 PDF still documents DSM 10631 as a variant that omits Na-acetate and adds 1.00 g/L yeast extract plus 2.50 g/L Na-L-lactate from sterile anoxic stocks after autoclaving.

The complex/undefined classification is supported for this DSM 10631 variant by the yeast extract supplement.

## Evidence

TOGO M2546 has a multi-solution structure over Solution A through Solution F. All six solution additions are represented as `solutions` entries with raw source volumes in `G_PER_L`: Solution A `941.5`, Solution B `1`, Solution C `30`, Solution D `10`, Solution E `10`, and Solution F `10`.

The stock definitions were also flattened into top-level ingredients. The generated `Distilled water` row is `3980.0 G_PER_L` because seven distinct water rows from Solution A, selenite-tungstate, Solution B, Solution C, Solution D, Solution E, and Solution F were summed.

Milligram trace-stock rows became gram-per-liter rows. Examples include Na2MoO4 x 2 H2O `36 G_PER_L`, H3BO3 `6 G_PER_L`, MnCl2 x 4 H2O `100 G_PER_L`, CoCl2 x 6 H2O `190 G_PER_L`, NiCl2 x 6 H2O `24 G_PER_L`, CuCl2 x 2 H2O `2 G_PER_L`, and ZnCl2 `70 G_PER_L`.

Selenite-tungstate and Wolin's vitamin solution components are also top-level. The vitamin rows are the source milligram amounts emitted as `G_PER_L`, for example Biotin `2 G_PER_L`, Thiamine-HCl `5 G_PER_L`, Pyridoxine-HCl `10 G_PER_L`, Folic acid `2 G_PER_L`, Vitamin B12 `0.1 G_PER_L`, and D-Ca-pantothenate `5 G_PER_L`.

TOGO gas condition rows became variable ingredients: `Carbon dioxide gas`, `Nitrogen gas`, and `N2 gas`. In DSMZ 193 they are gassing atmospheres for anaerobic solution preparation, not medium solutes.

## Completeness

The generated record lacks the DSMZ 193 preparation workflow: Solution A sparging with 80% N2 and 20% CO2 to pH below 6, separate autoclaving of Solution B under 80% N2/20% CO2, autoclaving of the reduced stocks under 100% N2, filter sterilization of the appropriate stock, ordered addition of stocks to sterile Solution A, final pH 7.1-7.4, the optional sodium dithionite note, and the 5-10% transfer inoculum note.

The DSM 10631 instruction to omit Na-acetate is not captured as structured variant logic; the generated file simply contains the replacement yeast extract and lactate rows.

## Findings

- Needs curation: six solution additions are encoded with `G_PER_L` concentrations equal to milliliter stock volumes.
- Needs curation: stock-internal water rows were summed into an impossible `3980.0 G_PER_L` top-level row.
- Needs curation: trace-element milligram rows and vitamin milligram rows were imported as gram-per-liter amounts.
- Needs curation: Selenite-tungstate, Trace element solution SL-10, Wolin's vitamin solution, carbonate, sulfide, and DSM 10631 lactate/yeast stocks are flattened or empty.
- Needs curation: N2 and CO2 gassing atmospheres are represented as variable-concentration ingredients.
- Needs curation: DSMZ preparation steps, pH 7.1-7.4, and DSM 10631 omit/replace semantics are absent.

## Recommended Edits

- Refresh `data/normalized_yaml/bacterial/desulfobacter_medium_for_dsm_10631.yaml` against the current DSMZ Medium 193 PDF.
- Represent DSM 10631 as a variant of base DSMZ 193 that omits Na-acetate and adds yeast extract plus Na-L-lactate after autoclaving.
- Preserve Solutions A through E and nested stock recipes as structured solutions with volumes instead of top-level `G_PER_L` rows.
- Convert trace and vitamin stock milligram rows to stock-internal concentrations under their own stock records.
- Move N2 and CO2 out of ingredients and into preparation or condition fields.
- Restore the DSMZ preparation workflow, final pH range, optional dithionite note, and 5-10% transfer note.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after regeneration.
- Confirm no source stock volume appears as `G_PER_L`.
- Confirm water rows are scoped to their own solution records and no longer summed.
- Confirm trace and vitamin amounts are not three orders of magnitude too high.
- Confirm DSM 10631 lacks Na-acetate but keeps yeast extract and Na-L-lactate as post-autoclave additions.

## Additional Notes

TOGO M2546, MediaDive REST medium 193, and the DSMZ Medium 193 PDF were reachable during review.
